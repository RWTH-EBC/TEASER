
# Example 14: Compare the AixLib HOM with the ROM exported next to it
The `aixlib_high_order_single_family_house` archetype describes one building
twice: as a high order model (HOM), which keeps all ten rooms and their walls,
and as the reduced order model (ROM) TEASER exports for every archetype, whose
ten rooms are merged into a single thermal zone. `export_besmod` with
`export_with_hom=True` writes both of them into the same project, driven by the
same weather and the same user profiles (BESMod's `TEASERHOMtoROM` reduces the
HOM's room-wise profiles to the merged zone), so they can be simulated against
each other directly.

This example runs that comparison: it exports the two models, simulates both in
Dymola and reports how far the ROM is from the HOM in heating energy, heating
power and zone temperature, i.e. how much of the HOM's behaviour survives the
merge into one zone. With `with_spawn=True`, the same building also runs as
Spawn of EnergyPlus model (`export_with_spawn`): the same rooms, constructions
and user profiles, but EnergyPlus' physics, as an independent third model.

The models start differently - the HOM's walls at a fixed temperature, the
Spawn model's after EnergyPlus' warm-up days - so the first `init_days` (4)
are left out of the metrics.

## The single-zone ROM
The ROM is BESMod's `TEASERThermalSingleZone`: AixLib's four element model,
like `TEASERThermalZone` for every other TEASER building, but for a building
that is one merged zone and still uses its inner geometry. From the rooms,
the archetype derives what the aggregated areas alone cannot tell
(`calc_rom_inner_heat_transfer_parameters`):
- the roof and the ground floor only exchange long wave radiation with the
  surfaces of their own floor
- the solar radiation through a window only reaches the room it enters
- the windows exchange no long wave radiation inside, as in the HOM
- only the part of the roof group facing the zone counts, the rest is the
  integrated attic's envelope

The outer surfaces are treated as in the HOM (`hom_surface_coefficients`),
and the natural ventilation comes from the user profile alone instead of
being added to AixLib's ventilation controller. Pass `use_old=True` to export
the building against `TEASERThermalZone` instead, without all of this.

By default both models are driven the way the archetype is meant to be used:
with the internal gains of its use conditions and each room at its own set
temperature (`room_t_set_nominal`). `validation=True` leaves the internal
gains out and sets every room to 20 degC, so that the two models differ in
nothing but their buildings.

## Why the Spawn model differs
The Spawn model has the HOM's geometry, constructions, user profiles, attic
and corridor air exchange, but EnergyPlus' physics, which is kept as it is.
Over a year (TRY2015 Potsdam, 1984, 170 m2, first 4 days left out) it needs
1.9 % (validation) to 2.8 % (default) less heating energy than the HOM, from
these differences:
- EnergyPlus places the beam solar radiation where it hits, mostly on the
  floor, which stores it and gives it off later. The HOM puts it into its
  rooms' radiation star, which spreads it over all surfaces at once,
  including the windows it partly leaves through. So in the heating season
  the Spawn model heats about 100 W more around midday and about 270 W less
  at night, and uses the solar gains a little better over the year.
- EnergyPlus takes a window's U-value with standard surface films and
  computes with its own, which lose less heat than the HOM's fixed U-value,
  and its interior convection (TARP) gives smaller coefficients than
  AixLib's. The two partly cancel: in ten January days, the windows alone
  account for about 7.5 and the convection for about 4.7 percentage points.
- EnergyPlus solves the conduction through the walls exactly, the HOM with
  one node per layer. This has little effect: three nodes per layer change
  the HOM's heating energy by 0.08 % and its day-night difference to the
  Spawn model by 10 %.
- EnergyPlus warms the walls up before the start, the HOM starts them at a
  fixed 16 degC, which makes the first days differ by up to 50 % - hence
  `init_days`.

## Prerequisites
You can not run this example using the online
[jupyter-notebook](https://mybinder.org/v2/gh/RWTH-EBC/TEASER/main?labpath=docs%2Fjupyter_notebooks),
as you need Dymola installed on your device. You also need:
1. ebcpy - for Dymola API interaction (`pip install ebcpy`)
2. IBPSA, AixLib and BESMod. If their paths are not provided, this example
   tries to clone them using git. BESMod has to support the HOM export, i.e.
   contain `Systems.Demand.Building.TEASERThermalSingleZone` - BESMod's
   `Examples.TEASERExport.HighOrderArchetypeExample` is this export.
3. matplotlib, for the plot of the comparison (`plot=False` skips it)
4. for `with_spawn`: the Buildings library with its Spawn binaries installed
   (see Buildings.ThermalZones.EnergyPlus_24_2_0.UsersGuide.Installation)

```python
import os
import subprocess
from pathlib import Path

import numpy as np

from teaser.logic import utilities
from teaser.project import Project
```

Where each library is cloned from if neither a path nor its environment
variable says where it already is

```python
LIBRARIES = {
    "IBPSA": ("https://github.com/ibpsa/modelica-ibpsa", "IBPSA", "IBPSA_PATH"),
    "AixLib": ("https://github.com/RWTH-EBC/AixLib", "AixLib", "AIXLIB_PATH"),
    "BESMod": ("https://github.com/RWTH-EBC/BESMod", "BESMod", "BESMOD_PATH"),
    "Buildings": ("https://github.com/lbl-srg/modelica-buildings", "Buildings",
                  "BUILDINGS_PATH"),
}


def _library_package(name, path, clone_directory):
    """Returns the package.mo of one Modelica library

    Takes the given path, else the library's environment variable
    (IBPSA_PATH, AIXLIB_PATH, BESMOD_PATH, BUILDINGS_PATH), else clones it
    from GitHub.
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
```

## Checking for Dymola first
Cloning the three libraries takes a while, so find out whether there is
anything to simulate with before starting.

```python
from ebcpy import DymolaAPI, TimeSeriesData

if not DymolaAPI.get_dymola_install_paths():
    raise FileNotFoundError(
        "No Dymola installation found - this example can not be run "
        "without it.")
```

## Finding the libraries
BESMod also provides the weather both models run with.

```python
clone_directory = Path(export_path or utilities.get_default_path())
packages = [
    _library_package("IBPSA", path_ibpsa, clone_directory),
    _library_package("AixLib", path_aixlib, clone_directory),
    _library_package("BESMod", path_besmod, clone_directory),
]
if with_spawn:
    packages.append(
        _library_package("Buildings", path_buildings, clone_directory))
besmod = packages[2].parent
```

The single-zone ROM extends a BESMod model that older releases of the
library do not have yet, so say so before Dymola does

```python
besmod_model = besmod.joinpath(
    "Systems", "Demand", "Building", "TEASERThermalSingleZone.mo")
if not use_old and not besmod_model.exists():
    raise FileNotFoundError(
        f"{besmod_model} is missing - the BESMod at {packages[2]} does not "
        "have the single-zone building model the ROM export needs. Point "
        "path_besmod (or BESMOD_PATH) at a BESMod that has it, or pass "
        "use_old=True to compare against the older TEASERThermalZone.")
```

## Exporting the HOM and the ROM
Both come out of one and the same archetype building, so every difference
between them is the merge of the ten rooms into a single zone.

```python
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
```

TRY2015 Potsdam and its design temperature, from the pair of weather
files BESMod has for Spawn, so that all models run with the same weather

```python
weather = besmod.joinpath("Resources", "Spawn", "Potsdam_TRY2015_normal")
prj.set_location_parameters(t_outside=273.15 - 12.6,
                            t_ground=273.15 + 13,
                            weather_file_path=str(weather) + ".mos",
                            calc_all_buildings=False)

prj.calc_all_buildings()

path_export = Path(prj.export_besmod(
    examples=["TEASERHeatLoadCalculation"],
    THydSup_nominal=55 + 273.15,
    path=export_path,
    export_with_hom=True,
    export_with_spawn=with_spawn,
    spawn_epw_path=str(weather) + ".epw" if with_spawn else None))
```

The ROM keeps the building's name, the HOM and the Spawn model get the
"_HOM" and "_Spawn" suffix

```python
models = {"rom": f"{prj.name}.{bldg.name}.TEASERHeatLoadCalculation{bldg.name}"}
models["hom"] = models["rom"] + "_HOM"
if with_spawn:
    models["spawn"] = models["rom"] + "_Spawn"
```

## Simulating them

```python
save_path = path_export.parent.joinpath(path_export.name + "_SimulationResults")
packages.append(path_export.joinpath("package.mo"))

result_files = {}
```

Spawn runs with CVODE, as BESMod's own Spawn examples do

```python
for names, solver in ((("rom", "hom"), "Dassl"), (("spawn",), "Cvode")):
    names = [name for name in names if name in models]
    if not names:
        continue
    dym_api = DymolaAPI(
        working_directory=save_path.joinpath("DymolaWorkingDirectory"),
        model_name=models[names[0]],
        packages=[str(package) for package in packages],
        show_window=False,
        equidistant_output=True,
        n_cpu=1,
    )
    dym_api.set_sim_setup(sim_setup={
        "start_time": 0,
        "stop_time": stop_time,
        "output_interval": output_interval,
        "solver": solver,
    })
    try:
        files = dym_api.simulate(
            return_option="savepath",
            model_names=[models[name] for name in names],
            savepath=str(save_path),
            result_file_name=names,
        )
    finally:
        dym_api.close()
    result_files.update(zip(names, files if isinstance(files, list) else [files]))
```

## Comparing the results
The ideal heater of the TEASERHeatLoadCalculation example holds every
zone at its set temperature, so what the models disagree about is the
heating power it takes to do so. The HOM and the Spawn model have one
heater per room, which are summed up for the comparison. The models
start differently - the HOM's walls at TWalls_start, the Spawn model's
after EnergyPlus' warm-up days - so the first init_days are left out of
the metrics.

```python
results = {name: TimeSeriesData(file).to_df()
           for name, file in result_files.items()}
rooms = sorted(bldg.room_name_nr, key=bldg.room_name_nr.get)
room_volumes = np.array([bldg.room_volumes[room] for room in rooms])
comparison = _compare_results(results, room_volumes, init_days)
print(f"\nAgainst the HOM over {stop_time / 86400:.0f} days, the first "
      f"{comparison['init_days']:g} left out"
      f"{' (use_old)' if use_old else ''}"
      f"{' (validation)' if validation else ''}:")
print(f"  heating energy HOM   {comparison['energy_hom']:9.1f} kWh")
for name, label in (("", "ROM"), ("_spawn", "Spawn")):
    if f"energy{name or '_rom'}" not in comparison:
        continue
    energy = comparison["energy_rom" if not name else "energy_spawn"]
    print(f"  heating energy {label:6s}{energy:9.1f} kWh"
          f"   ({comparison['energy_deviation' + name] * 100:+.2f} %)"
          f", RMSE {comparison['rmse_power' + name]:7.1f} W"
          f" and {comparison['rmse_temperature' + name]:.4f} K")

if plot:
    figure = plot_comparison(results, room_volumes, comparison)
    # names the window after the case, as two of them can be open
    if figure.canvas.manager is not None:
        figure.canvas.manager.set_window_title(
            "Example 14" + (" use_old" if use_old else "")
            + (" validation" if validation else ""))
    if show_plot:
        import matplotlib.pyplot as plt
        plt.show()


e quantities the comparison is made of, named for one zone - the HOM and
e Spawn model have ten of each, the ROM one
R = "electrical.outBusElect.tra.PHea[1].value"
GY = "electrical.outBusElect.tra.PHea[1].integral"
ERATURE = "building.buiMeaBus.TZoneMea[1]"
e HOM's room temperatures averaged by room volume, the way the archetype
gregates them for the merged zone
ERATURE_HOM = "outputs.building.TBuiVolAve"
d the lowest and highest of them
ERATURE_HOM_MIN = "outputs.building.TBuiMin"
ERATURE_HOM_MAX = "outputs.building.TBuiMax"


_zone_columns(df, template):
"""The per zone columns behind one quantity, in zone order"""
prefix, suffix = template.split("[")[0] + "[", "]" + template.split("]")[1]
columns = sorted(
    (c for c in df.columns
     if c.startswith(prefix) and c.endswith(suffix)),
    key=lambda c: int(c.split("[")[1].split("]")[0]))


_sum_over_zones(df, template):
"""Sums a quantity the models have one of per zone (10 for the HOM and the
Spawn model, 1 for the ROM) into a single time series"""


_temperature(name, df, room_volumes):
"""The zone temperature of a model: the ROM's one zone, the HOM's and
the Spawn model's rooms averaged by room volume"""
if name == "rom":
if name == "hom":
rooms = _zone_columns(df, TEMPERATURE)[:, :len(room_volumes)]


_compare_results(results, room_volumes, init_days):
"""Compares the ROM, and the Spawn model if simulated, against the HOM,
after the first init_days

The keys without a suffix are the ROM's, those with "_spawn" the Spawn
model's.
"""
time = results["hom"].index.to_numpy()
if init_days * 86400 >= time[-1]:
    # too short a period to leave the start out
    init_days = 0
after = time >= init_days * 86400

def energy(df):
    integral = _sum_over_zones(df, ENERGY)

power_hom = _sum_over_zones(results["hom"], POWER)[after]
temperature_hom = _temperature("hom", results["hom"], room_volumes)[after]
comparison = {"init_days": init_days,
              "energy_hom": energy(results["hom"])}
for name, suffix in (("rom", ""), ("spawn", "_spawn")):
    if name not in results:
        continue
    df = results[name]
    power = _sum_over_zones(df, POWER)[after]
    temperature = _temperature(name, df, room_volumes)[after]
    comparison[f"energy_{name}"] = energy(df)
    comparison["energy_deviation" + suffix] = (
        comparison[f"energy_{name}"] / comparison["energy_hom"] - 1)
    comparison["rmse_power" + suffix] = float(
        np.sqrt(((power - power_hom) ** 2).mean()))
    comparison["max_power_deviation" + suffix] = float(
        np.abs(power - power_hom).max())
    comparison["rmse_temperature" + suffix] = float(
        np.sqrt(((temperature - temperature_hom) ** 2).mean()))


plot_comparison(results, room_volumes, comparison):
"""Plots the ROM, and the Spawn model if simulated, against the HOM

Three panels over one shared time axis rather than one panel with two
scales: the heating power the models call for, the heating energy that
adds up to, and the zone temperature they hold. The HOM's ten room
temperatures are reduced to the one the merged zone would have, by room
volume, and shown with the band from their lowest to their highest - the
rooms spread much wider than their average (the bathroom alone is designed
for 24 instead of 20 degrees), and that spread is precisely what the ROM
cannot have. The start the metrics leave out is shaded, and the heating
energy counts from its end.

The same colours mean the same models in all three panels, so only the
first one carries a legend, and the third one for the band.
"""
import matplotlib.pyplot as plt
```

categorical slots 1 to 3, and the ink the labels wear - a series colour
is for the marks only, never for text

```python
colors = {"hom": "#2a78d6", "rom": "#eb6834", "spawn": "#1f9e6e"}
labels = {"hom": "HOM", "rom": "ROM", "spawn": "Spawn"}
ink, ink_muted, surface = "#0b0b0b", "#52514e", "#fcfcfb"
```

The sample at t = 0 holds the initial values, before the solver has
done anything, and the models start from different ones. Plotting it
would spend a third of the temperature axis on one meaningless point,
so the plot starts at the first real one.

```python
plotted = slice(1, None)
hom = results["hom"]
time = hom.index.to_numpy()
days = time[plotted] / 86400.0
init = comparison["init_days"] * 86400

figure, axes = plt.subplots(3, 1, sharex=True, figsize=(9.0, 8.0),
                            facecolor=surface)
for axis in axes:
    axis.set_facecolor(surface)
    axis.spines[["top", "right"]].set_visible(False)
    axis.spines[["left", "bottom"]].set_color(ink_muted)
    axis.tick_params(colors=ink_muted, labelsize=9)
    axis.grid(axis="y", color="#e3e2de", linewidth=0.5)
    axis.set_axisbelow(True)
    if init:
        axis.axvspan(0, init / 86400, color="#e3e2de", alpha=0.6,
                     linewidth=0)

axes[2].fill_between(
    days, hom[TEMPERATURE_HOM_MIN].to_numpy()[plotted] - 273.15,
    hom[TEMPERATURE_HOM_MAX].to_numpy()[plotted] - 273.15,
    color=colors["hom"], alpha=0.18, linewidth=0,
    label="HOM rooms, lowest to highest")
for name in ("hom", "rom", "spawn"):
    if name not in results:
        continue
    df = results[name]
    integral = _sum_over_zones(df, ENERGY)
    energy = (integral - np.interp(init, time, integral)) / 3.6e6
    energy[time < init] = np.nan
    axes[0].plot(days, _sum_over_zones(df, POWER)[plotted] / 1000.0,
                 color=colors[name], linewidth=1.5, label=labels[name])
    axes[1].plot(days, energy[plotted], color=colors[name], linewidth=2.0)
    axes[2].plot(days, _temperature(name, df, room_volumes)[plotted]
                 - 273.15, color=colors[name], linewidth=1.5)
    if name != "hom":
        suffix = "" if name == "rom" else "_spawn"
        # one direct label where each ends up, rather than a number on
        # every point
        axes[1].annotate(
            f"{labels[name]} {comparison['energy_deviation' + suffix] * 100:+.1f} %",
            xy=(days[-1], energy[-1]), xytext=(-6, 6 if name == "rom" else -12),
            textcoords="offset points", ha="right", color=ink, fontsize=9)

axes[0].set_ylabel("heating power in kW", color=ink, fontsize=10)
axes[0].legend(frameon=False, labelcolor=ink, fontsize=9, ncols=3,
               loc="upper right")
rmse = "  ".join(
    f"{labels[name]} {comparison['rmse_power' + suffix] / 1000:.2f} kW"
    for name, suffix in (("rom", ""), ("spawn", "_spawn"))
    if name in results)
axes[0].annotate(f"RMSE {rmse}", xy=(1.0, 0.86), xycoords="axes fraction",
                 xytext=(-2, 0), textcoords="offset points",
                 ha="right", va="top", color=ink, fontsize=9)
axes[1].set_ylabel("heating energy in kWh", color=ink, fontsize=10)
axes[2].set_ylabel("zone temperature in °C", color=ink, fontsize=10)
axes[2].legend(frameon=False, labelcolor=ink, fontsize=9,
               loc="lower right")
axes[2].set_xlabel("time in days", color=ink, fontsize=10)
rmse = "  ".join(
    f"{labels[name]} {comparison['rmse_temperature' + suffix]:.3f} K"
    for name, suffix in (("rom", ""), ("spawn", "_spawn"))
    if name in results)
axes[2].annotate(f"RMSE {rmse}", xy=(1.0, 1.0), xycoords="axes fraction",
                 xytext=(-2, -4), textcoords="offset points",
                 ha="right", va="top", color=ink, fontsize=9)

figure.suptitle("The reduced order and the Spawn model against the high "
                "order model" if "spawn" in results else
                "The reduced order model against the high order model "
                "it was merged from", color=ink, fontsize=12, x=0.125,
                ha="left")
figure.tight_layout()
```
