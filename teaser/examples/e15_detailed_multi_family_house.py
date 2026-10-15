# # Example 15: Generate the detailed multi family house and export it
# The `detailed_multi_family_house` archetype builds a multi family house room
# by room from Kühn/Nikolowski's floor plan: a staircase with a flat of six
# rooms on either side of it, on number_of_floors storeys, over an unheated
# basement and below an unheated attic with a gable roof. The building grows
# by storeys (`number_of_floors`) and by staircases side by side
# (`number_of_staircases`, two flats per staircase and storey), and its flats
# are scaled to `net_leased_area_per_flat`. Its construction data,
# `detailed_mfh_standard`, has three age groups: up to 1978, 1979 to 1994
# and from 2021 on.
#
# From the rooms' three-dimensional geometry, TEASER derives the thermal
# zones of the reduced order model (ROM), one for the building or one per
# flat, and integrates the unheated spaces into them by temperature factors.
# The same geometry is exported as EnergyPlus model with every room as a
# zone, which BESMod simulates as Spawn of EnergyPlus model next to the ROM.
#
# The defaults and assumptions of the archetype are listed in
# `teaser/logic/archetypebuildings/detailed_mfh/ASSUMPTIONS.md`.
# You can run this example using the [jupyter-notebook](https://mybinder.org/v2/gh/RWTH-EBC/TEASER/main?labpath=docs%2Fjupyter_notebooks)

import os

from teaser.project import Project
from teaser.logic import utilities
from teaser.data.output.energyplus_output import export_idf


def example_detailed_multi_family_house(spawn_epw_path=None):
    """Generates the detailed multi family house in several variants and
    exports it to AixLib, BESMod and EnergyPlus

    Parameters
    ----------
    spawn_epw_path : str
        The project's weather as .epw file. With it, the BESMod export also
        contains the room-wise Spawn of EnergyPlus model. BESMod has one in
        Resources/Spawn/Potsdam_TRY2015_normal.epw, to be used with the .mos
        file next to it as the project's weather.

    Returns
    -------
    prj : Project
    """

    prj = Project()
    prj.name = "DetailedMultiFamilyHouse"

    # ## The building as drawn
    # Five storeys with one staircase, i.e. ten flats of 64.9 m2 each, as
    # Kühn/Nikolowski's plan has them, built in 1990. `net_leased_area` is
    # left out, as the plan sets it.

    mfh_1990 = prj.add_residential(
        construction_data="detailed_mfh_standard",
        geometry_data="detailed_multi_family_house",
        name="MFH1990",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.5,
        net_leased_area=None)

    print(f"{mfh_1990.name}: {mfh_1990.number_of_flats} flats, "
          f"{mfh_1990.net_leased_area:.1f} m2, "
          f"{mfh_1990.geometry.length:.2f} m x {mfh_1990.geometry.depth:.2f} m")

    # The geometry knows every room, staircase, the basement and the attic,
    # named F{storey}_A{flat}_{room type}, storey 0 being the ground floor
    # and the flats numbered from west to east.

    print("Rooms of the first flat:",
          [room for room in mfh_1990.geometry.heated_rooms
           if room.startswith("F0_A1_")])

    # ## Zoning
    # By default, all heated rooms form one thermal zone. `zoning = "flat"`
    # gives each flat its own zone, and any function from a room's ZoneInfo
    # (its storey, flat, room_type, ...) to a zone name gives other zonings.
    # Every change of the settings needs `generate_archetype()` afterwards.

    mfh_1990.zoning = "flat"
    mfh_1990.generate_archetype()
    print(f"Zoning per flat: {len(mfh_1990.thermal_zones)} zones")

    # ## The unheated spaces
    # The basement, the staircase and the attic are no thermal zones. A heated
    # room's wall or slab towards them loses heat to the outside air instead,
    # reduced by the temperature factor of the space, which follows from the
    # steady-state heat balance of all unheated spaces at the design
    # temperatures.

    for space, temperature in mfh_1990.unheated_temperatures.items():
        print(f"{space} at design conditions: {temperature - 273.15:.1f} degC")

    # ## More storeys, more staircases, larger flats
    # A building of 2025 with six storeys and two staircases side by side, so
    # 24 flats, each of 77 m2. By default the rooms are stretched along the
    # building's length only (`scaling = "length"`); `"proportional"`
    # stretches them in both directions. A neighbouring building on the west
    # side makes that gable wall adiabatic.

    mfh_2025 = prj.add_residential(
        construction_data="detailed_mfh_standard",
        geometry_data="detailed_multi_family_house",
        name="MFH2025",
        year_of_construction=2025,
        number_of_floors=6,
        height_of_floors=2.5,
        net_leased_area=None,
        number_of_staircases=2,
        net_leased_area_per_flat=77.0,
        neighbour_buildings=1)

    print(f"{mfh_2025.name}: {mfh_2025.number_of_flats} flats, "
          f"{mfh_2025.net_leased_area:.1f} m2, "
          f"{mfh_2025.geometry.length:.2f} m x {mfh_2025.geometry.depth:.2f} m")

    # The building can be turned like every TEASER building. With rotation 0,
    # the living rooms face south.

    mfh_2025.rotate_building(90)

    # ## Heat loads
    # TEASER calculates the heat load room by room, each room at its own
    # design temperature (`room_t_set_nominal`, 24 degC in the bath), and
    # sums it up to the zones. TEASER warns that the zones have no ground
    # floor: they lose heat to the basement through stand-ins, not to the
    # ground.

    prj.used_library_calc = "AixLib"
    prj.number_of_elements_calc = 4
    prj.calc_all_buildings()

    for bldg in (mfh_1990, mfh_2025):
        print(f"{bldg.name}: heat load {bldg.sum_heat_load / 1000:.1f} kW, "
              f"{bldg.sum_heat_load / bldg.net_leased_area:.1f} W/m2")

    # ## Export
    # The ROM goes to AixLib and BESMod as for every TEASER building, the
    # BESMod export with one zone per thermal zone of the ROM. With
    # `export_with_spawn=True` and the project's weather as .epw file, the
    # BESMod export adds a Spawn of EnergyPlus model of the building, room by
    # room, with each room's internal gains and set temperature, in
    # TEASERHeatLoadCalculation, HeatPumpSimple and GasBoilerBuildingOnly.
    # Spawn needs a short path to its working directory on Windows.

    if spawn_epw_path is not None:
        prj.weather_file_path = os.path.splitext(spawn_epw_path)[0] + ".mos"
        prj.calc_all_buildings()

    path = prj.export_aixlib(
        path=os.path.join(utilities.get_default_path(), prj.name, "AixLib"))
    print("AixLib export:", path)

    path = prj.export_besmod(
        examples=["TEASERHeatLoadCalculation", "HeatPumpSimple",
                  "GasBoilerBuildingOnly"],
        THydSup_nominal=328.15,
        path=os.path.join(utilities.get_default_path(), prj.name, "BESMod"),
        export_with_spawn=spawn_epw_path is not None,
        spawn_epw_path=spawn_epw_path)
    print("BESMod export:", path)

    # The EnergyPlus model alone, e.g. to run it in EnergyPlus directly:
    # `run_period_days` adds a run period of the first days of the year.

    path = export_idf(
        mfh_1990,
        os.path.join(utilities.get_default_path(), prj.name, "EnergyPlus",
                     mfh_1990.name + ".idf"),
        run_period_days=14)
    print("EnergyPlus model:", path)

    return prj


if __name__ == "__main__":
    example_detailed_multi_family_house()

    print("Example 15: That's it! :)")
