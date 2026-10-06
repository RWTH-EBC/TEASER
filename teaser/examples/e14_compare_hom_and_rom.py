# # Example 14: Compare the AixLib HOM with the ROM exported next to it
# The `aixlib_high_order_single_family_house` archetype describes one building
# twice: as a high order model (HOM), which keeps all ten rooms and their walls,
# and as the reduced order model (ROM) TEASER exports for every archetype, whose
# ten rooms are merged into a single thermal zone. `export_besmod` with
# `export_with_hom=True` writes both of them into the same project, driven by the
# same weather and the same user profiles (BESMod's `TEASERHOMtoROM` reduces the
# HOM's room-wise profiles to the merged zone), so they can be simulated against
# each other directly.
#
# This example runs that comparison: it exports the two models, simulates both in
# Dymola and reports how far the ROM is from the HOM in heating energy, heating
# power and zone temperature, i.e. how much of the HOM's behaviour survives the
# merge into one zone.
#
# ## The single-zone ROM
# The ROM is BESMod's `TEASERThermalSingleZone`: AixLib's four element model,
# like `TEASERThermalZone` for every other TEASER building, but for a building
# that is one merged zone and still uses its inner geometry. From the rooms,
# the archetype derives what the aggregated areas alone cannot tell
# (`calc_rom_inner_heat_transfer_parameters`):
# - the roof and the ground floor only exchange long wave radiation with the
#   surfaces of their own floor
# - the solar radiation through a window only reaches the room it enters
# - the windows exchange no long wave radiation inside, as in the HOM
# - only the part of the roof group facing the zone counts, the rest is the
#   integrated attic's envelope
#
# The outer surfaces are treated as in the HOM (`hom_surface_coefficients`),
# and the natural ventilation comes from the user profile alone instead of
# being added to AixLib's ventilation controller. Pass `use_old=True` to export
# the building against `TEASERThermalZone` instead, without all of this.
#
# By default both models are driven the way the archetype is meant to be used:
# with the internal gains of its use conditions and each room at its own set
# temperature (`room_t_set_nominal`). `validation=True` leaves the internal
# gains out and sets every room to 20 degC, so that the two models differ in
# nothing but their buildings.
#
# ## Prerequisites
# You can not run this example using the online
# [jupyter-notebook](https://mybinder.org/v2/gh/RWTH-EBC/TEASER/main?labpath=docs%2Fjupyter_notebooks),
# as you need Dymola installed on your device. You also need:
# 1. ebcpy - for Dymola API interaction (`pip install ebcpy`)
# 2. IBPSA, AixLib and BESMod. If their paths are not provided, this example
#    tries to clone them using git. BESMod has to support the HOM export, i.e.
#    contain `Systems.Demand.Building.TEASERThermalSingleZone` - BESMod's
#    `Examples.TEASERExport.HighOrderArchetypeExample` is this export.
# 3. matplotlib, for the plot of the comparison (`plot=False` skips it)

import os
import subprocess
from pathlib import Path

import numpy as np

from teaser.project import Project

# Where each library is cloned from if neither a path nor its environment
# variable says where it already is
LIBRARIES = {
    "IBPSA": ("https://github.com/ibpsa/modelica-ibpsa", "IBPSA", "IBPSA_PATH"),
    "AixLib": ("https://github.com/RWTH-EBC/AixLib", "AixLib", "AIXLIB_PATH"),
    "BESMod": ("https://github.com/RWTH-EBC/BESMod", "BESMod", "BESMOD_PATH"),
}


def _library_package(name, path, clone_directory):
    """Returns the package.mo of one Modelica library

    Takes the given path, else the library's environment variable
    (IBPSA_PATH, AIXLIB_PATH, BESMOD_PATH), else clones it from GitHub.
    """
    url, package_directory, variable = LIBRARIES[name]
    if path is None:
        path = os.environ.get(variable)
    if path is not None:
        return Path(path)
    repository = Path(clone_directory).joinpath(name)
    if not repository.exists():
        print(f"Cloning {name} to {repository}...")
        repository.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", url, str(repository)], check=True)
    return repository.joinpath(package_directory, "package.mo")


def example_compare_hom_and_rom(
        stop_time=86400 * 365,
        output_interval=900,
        use_old=False,
        plot=True,
        show_plot=True,
        path_ibpsa=None,
        path_aixlib=None,
        path_besmod=None,
        export_path=None,
        validation=False,
):
    """Simulates the HOM and the ROM of one archetype and compares them

    Parameters
    ----------
    stop_time : float
        simulated period in seconds, starting at the beginning of the year
    output_interval : float
        interval of the stored results in seconds
    use_old : bool
        exports the ROM against BESMod's older TEASERThermalZone, i.e. without
        the room-wise parameters the archetype derives for the single-zone
        model - useful to see what those parameters are worth
    plot : bool
        plots the two models against each other
    show_plot : bool
        opens the plot in a window, which blocks until it is closed. Without
        it, the plot is left to the caller to show
    path_ibpsa, path_aixlib, path_besmod : str
        paths to the package.mo of each library. Cloned from GitHub if None.
    export_path : str
        where the Modelica project is exported to. TEASER's default if None.
    validation : bool
        compares the buildings alone: no internal gains, and every room at a
        constant 20 degC

    Returns
    -------
    dict
        the comparison of the ROM against the HOM
    """
    # ## Checking for Dymola first
    # Cloning the three libraries takes a while, so find out whether there is
    # anything to simulate with before starting.
    from ebcpy import DymolaAPI, TimeSeriesData

    if not DymolaAPI.get_dymola_install_paths():
        raise FileNotFoundError(
            "No Dymola installation found - this example can not be run "
            "without it.")

    # ## Exporting the HOM and the ROM
    # Both come out of one and the same archetype building, so every difference
    # between them is the merge of the ten rooms into a single zone.
    prj = Project()
    prj.name = "CompareHOMandROM1984_170"
    prj.add_residential(
        construction_data='aixlib_S',
        geometry_data='aixlib_high_order_single_family_house',
        name="SingleFamilyHouse",
        year_of_construction=1984,
        net_leased_area=170.0,
        number_of_floors=2,
        height_of_floors=2.6)

    bldg = prj.buildings[0]
    if validation:
        # Every room at 20 degC, without a set back. room_t_set_nominal only
        # takes effect once the archetype is generated again, which also
        # loads its use conditions anew - so those come after.
        bldg.room_t_set_nominal = {room: 293.15 for room in bldg.room_name_nr}
        bldg.generate_archetype()
        use_conditions = bldg.thermal_zones[0].use_conditions
        use_conditions.heating_profile = [293.15] * 24
        use_conditions.persons = 0.0
        use_conditions.machines = 0.0
        use_conditions.use_maintained_illuminance = False
        use_conditions.lighting_power = 0.0
    bldg.use_old = use_old
    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 4

    # BESMod's default weather, TRY2015 Potsdam, and its design temperature
    prj.set_location_parameters(t_outside=273.15 - 12.6,
                                t_ground=273.15 + 13,
                                weather_file_path=r"D:\01_git\BESMod\BESMod\Resources\WeatherData\TRY2015_522361130393_Jahr_City_Potsdam.mos",
                                calc_all_buildings=False)

    prj.calc_all_buildings()

    path_export = Path(prj.export_besmod(
        examples=["TEASERHeatLoadCalculation"],
        THydSup_nominal=55 + 273.15,
        path=export_path,
        export_with_hom=True))

    # The ROM keeps the building's name, the HOM gets the "_HOM" suffix
    rom_model = f"{prj.name}.{bldg.name}.TEASERHeatLoadCalculation{bldg.name}"
    hom_model = rom_model + "_HOM"

    # ## Simulating both
    save_path = path_export.parent.joinpath(path_export.name + "_SimulationResults")
    packages = [
        _library_package("IBPSA", path_ibpsa, save_path.parent),
        _library_package("AixLib", path_aixlib, save_path.parent),
        _library_package("BESMod", path_besmod, save_path.parent),
        path_export.joinpath("package.mo"),
    ]

    # The single-zone ROM extends a BESMod model that older releases of the
    # library do not have yet, so say so before Dymola does
    besmod_model = packages[2].parent.joinpath(
        "Systems", "Demand", "Building", "TEASERThermalSingleZone.mo")
    if not use_old and not besmod_model.exists():
        raise FileNotFoundError(
            f"{besmod_model} is missing - the BESMod at {packages[2]} does not "
            "have the single-zone building model the ROM export needs. Point "
            "path_besmod (or BESMOD_PATH) at a BESMod that has it, or pass "
            "use_old=True to compare against the older TEASERThermalZone.")

    dym_api = DymolaAPI(
        working_directory=save_path.joinpath("DymolaWorkingDirectory"),
        model_name=rom_model,
        packages=[str(package) for package in packages],
        show_window=False,
        equidistant_output=True,
        n_cpu=1,
    )
    dym_api.set_sim_setup(sim_setup={
        "start_time": 0,
        "stop_time": stop_time,
        "output_interval": output_interval,
    })
    try:
        result_files = dym_api.simulate(
            return_option="savepath",
            model_names=[rom_model, hom_model],
            savepath=str(save_path),
            result_file_name=["rom", "hom"],
        )
    finally:
        dym_api.close()

    # ## Comparing the results
    # The ideal heater of the TEASERHeatLoadCalculation example holds every
    # zone at its set temperature, so what the two models disagree about is the
    # heating power it takes to do so. The HOM has one heater per room, which
    # have to be summed up before they can be compared to the ROM's single one.
    results = {name: TimeSeriesData(file).to_df()
               for name, file in zip(("rom", "hom"), result_files)}

    comparison = _compare_results(results["rom"], results["hom"])
    print(f"\nROM against HOM over {stop_time / 86400:.0f} days"
          f"{' (use_old)' if use_old else ''}"
          f"{' (validation)' if validation else ''}:")
    print(f"  heating energy HOM   {comparison['energy_hom']:9.1f} kWh")
    print(f"  heating energy ROM   {comparison['energy_rom']:9.1f} kWh"
          f"   ({comparison['energy_deviation'] * 100:+.2f} %)")
    print(f"  RMSE heating power   {comparison['rmse_power']:9.1f} W")
    print(f"  RMSE zone temperature{comparison['rmse_temperature']:9.4f} K")

    if plot:
        figure = plot_comparison(results["rom"], results["hom"], comparison)
        # names the window after the case, as two of them can be open
        if figure.canvas.manager is not None:
            figure.canvas.manager.set_window_title(
                "Example 14" + (" use_old" if use_old else "")
                + (" validation" if validation else ""))
        if show_plot:
            import matplotlib.pyplot as plt
            plt.show()
    return comparison


# The quantities the comparison is made of, named for one zone - the HOM has
# ten of each, the ROM one
POWER = "electrical.outBusElect.tra.PHea[1].value"
ENERGY = "electrical.outBusElect.tra.PHea[1].integral"
TEMPERATURE = "building.buiMeaBus.TZoneMea[1]"
# The HOM's room temperatures averaged by room volume, the way the archetype
# aggregates them for the merged zone
TEMPERATURE_HOM = "outputs.building.TBuiVolAve"
# and the lowest and highest of them
TEMPERATURE_HOM_MIN = "outputs.building.TBuiMin"
TEMPERATURE_HOM_MAX = "outputs.building.TBuiMax"


def _zone_columns(df, template):
    """The per zone columns behind one quantity, in zone order"""
    prefix, suffix = template.split("[")[0] + "[", "]" + template.split("]")[1]
    columns = sorted(
        (c for c in df.columns
         if c.startswith(prefix) and c.endswith(suffix)),
        key=lambda c: int(c.split("[")[1].split("]")[0]))
    return df[columns].to_numpy()


def _sum_over_zones(df, template):
    """Sums a quantity the models have one of per zone (10 for the HOM, 1 for
    the ROM) into a single time series"""
    return _zone_columns(df, template).sum(axis=1)


def _compare_results(rom, hom):
    """Compares the ROM's single zone against the HOM's ten rooms"""
    power_rom = _sum_over_zones(rom, POWER)
    power_hom = _sum_over_zones(hom, POWER)
    energy_rom = _sum_over_zones(rom, ENERGY)[-1] / 3.6e6
    energy_hom = _sum_over_zones(hom, ENERGY)[-1] / 3.6e6

    temperature_rom = _sum_over_zones(rom, TEMPERATURE)
    temperature_hom = hom[TEMPERATURE_HOM].to_numpy()

    return {
        "energy_rom": energy_rom,
        "energy_hom": energy_hom,
        "energy_deviation": energy_rom / energy_hom - 1,
        "rmse_power": float(np.sqrt(((power_rom - power_hom) ** 2).mean())),
        "max_power_deviation": float(np.abs(power_rom - power_hom).max()),
        "rmse_temperature": float(
            np.sqrt(((temperature_rom - temperature_hom) ** 2).mean())),
    }


def plot_comparison(rom, hom, comparison):
    """Plots the ROM against the HOM over the simulated period

    Three panels over one shared time axis rather than one panel with two
    scales: the heating power the two models call for, the heating energy that
    adds up to, and the zone temperature they hold. The HOM's ten room
    temperatures are reduced to the one the merged zone would have, by room
    volume, and shown with the band from their lowest to their highest - the
    rooms spread much wider than their average (the bathroom alone is designed
    for 24 instead of 20 degrees), and that spread is precisely what the ROM
    cannot have.

    The same two colours mean the same two models in all three panels, so only
    the first one carries a legend, and the third one for the band.
    """
    import matplotlib.pyplot as plt

    # categorical slots 1 and 2, and the ink the labels wear - a series colour
    # is for the marks only, never for text
    color_hom, color_rom = "#2a78d6", "#eb6834"
    ink, ink_muted, surface = "#0b0b0b", "#52514e", "#fcfcfb"

    # The sample at t = 0 holds the initial values, before the solver has
    # done anything, and its two models start from different ones. Plotting
    # it would spend a third of the temperature axis on one meaningless
    # point, so the plot starts at the first real one. The metrics, which are
    # taken over the whole result, do include it.
    plotted = slice(1, None)
    days = rom.index.to_numpy()[plotted] / 86400.0
    power_rom = _sum_over_zones(rom, POWER)[plotted] / 1000.0
    power_hom = _sum_over_zones(hom, POWER)[plotted] / 1000.0
    energy_rom = _sum_over_zones(rom, ENERGY)[plotted] / 3.6e6
    energy_hom = _sum_over_zones(hom, ENERGY)[plotted] / 3.6e6
    temperature_rom = _sum_over_zones(rom, TEMPERATURE)[plotted] - 273.15
    temperature_hom = hom[TEMPERATURE_HOM].to_numpy()[plotted] - 273.15
    temperature_hom_min = hom[TEMPERATURE_HOM_MIN].to_numpy()[plotted] - 273.15
    temperature_hom_max = hom[TEMPERATURE_HOM_MAX].to_numpy()[plotted] - 273.15

    figure, axes = plt.subplots(3, 1, sharex=True, figsize=(9.0, 8.0),
                                facecolor=surface)
    for axis in axes:
        axis.set_facecolor(surface)
        axis.spines[["top", "right"]].set_visible(False)
        axis.spines[["left", "bottom"]].set_color(ink_muted)
        axis.tick_params(colors=ink_muted, labelsize=9)
        axis.grid(axis="y", color="#e3e2de", linewidth=0.5)
        axis.set_axisbelow(True)

    axes[0].plot(days, power_hom, color=color_hom, linewidth=2.0, label="HOM")
    axes[0].plot(days, power_rom, color=color_rom, linewidth=2.0, label="ROM")
    axes[0].set_ylabel("heating power in kW", color=ink, fontsize=10)
    axes[0].legend(frameon=False, labelcolor=ink, fontsize=9, ncols=2,
                   loc="upper right")
    axes[0].annotate(f"RMSE {comparison['rmse_power'] / 1000:.2f} kW",
                     xy=(1.0, 0.86), xycoords="axes fraction",
                     xytext=(-2, 0), textcoords="offset points",
                     ha="right", va="top", color=ink, fontsize=9)

    axes[1].plot(days, energy_hom, color=color_hom, linewidth=2.0)
    axes[1].plot(days, energy_rom, color=color_rom, linewidth=2.0)
    axes[1].set_ylabel("heating energy in kWh", color=ink, fontsize=10)
    # one direct label rather than a number on every point: where the two end up
    axes[1].annotate(f"{comparison['energy_deviation'] * 100:+.1f} %",
                     xy=(days[-1], energy_rom[-1]),
                     xytext=(-6, 6), textcoords="offset points",
                     ha="right", color=ink, fontsize=9)

    axes[2].fill_between(days, temperature_hom_min, temperature_hom_max,
                         color=color_hom, alpha=0.18, linewidth=0,
                         label="HOM rooms, lowest to highest")
    axes[2].plot(days, temperature_hom, color=color_hom,
                 linewidth=2.0)
    axes[2].plot(days, temperature_rom, color=color_rom, linewidth=2.0)
    axes[2].set_ylabel("zone temperature in °C", color=ink, fontsize=10)
    axes[2].legend(frameon=False, labelcolor=ink, fontsize=9,
                   loc="lower right")
    axes[2].set_xlabel("time in days", color=ink, fontsize=10)
    axes[2].annotate(f"RMSE {comparison['rmse_temperature']:.3f} K",
                     xy=(1.0, 1.0), xycoords="axes fraction",
                     xytext=(-2, -4), textcoords="offset points",
                     ha="right", va="top", color=ink, fontsize=9)

    figure.suptitle("The reduced order model against the high order model "
                    "it was merged from", color=ink, fontsize=12, x=0.125,
                    ha="left")
    figure.tight_layout()
    return figure


if __name__ == '__main__':
    comparisons = {}
    for validation in (True, False):
        comparisons[validation] = example_compare_hom_and_rom(
            export_path=r"D:\03_TEASER_dev\test_hom_export"
                        + ("_validation" if validation else "_default"),
            path_besmod=r"D:\01_git\BESMod\BESMod\package.mo",
            path_ibpsa=r"D:\01_git\BESMod\installed_dependencies\IBPSA\IBPSA\package.mo",
            path_aixlib=r"D:\01_git\BESMod\installed_dependencies\AixLib\AixLib\package.mo",
            validation=validation,
            # both plots open together at the end instead
            show_plot=True)

    print(f"\n{'':26s}{'validation':>12s}{'default':>12s}")
    for key, label, factor, unit in (
            ("energy_hom", "heating energy HOM", 1, "kWh"),
            ("energy_rom", "heating energy ROM", 1, "kWh"),
            ("energy_deviation", "deviation", 100, "%"),
            ("rmse_power", "RMSE heating power", 1, "W"),
            ("rmse_temperature", "RMSE zone temperature", 1, "K")):
        print(f"{label + ' [' + unit + ']':26s}"
              + "".join(f"{comparisons[v][key] * factor:12.2f}" for v in (True, False)))

    import matplotlib.pyplot as plt
    plt.show()

    print("Example 14: That's it! :)")
