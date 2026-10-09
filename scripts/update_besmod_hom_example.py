"""Regenerates BESMod's example of TEASER's HOM export

BESMod.Examples.TEASERExport.HighOrderArchetypeExample is TEASER's archetype of
AixLib's high order single family house, exported with export_with_hom=True
and export_with_spawn=True: the building as single zone ROM, as HOM and as
Spawn of EnergyPlus model, in TEASER's four example energy systems (the Spawn
model in the three without mechanical ventilation). Whenever the archetype or the BESMod export changes in a way
that shows in the exported models, run this script against a BESMod checkout
to bring the example in line, and let BESMod's regression tests update their
reference results:

    python scripts/update_besmod_hom_example.py D:/01_git/BESMod/BESMod/package.mo

The path is BESMod's package.mo (or the directory holding it), as for
example e14; without it, the script takes the environment variable
BESMOD_PATH. The script exports the building and changes the export only
where BESMod's examples differ from what TEASER writes for a user:

- the package is BESMod.Examples.TEASERExport.HighOrderArchetypeExample
- the weather is BESMod's pair of weather files for Spawn (TRY2015 Potsdam,
  .mos and .epw), which TEASER is given for the heat loads, instead of an own
  copy of it, and the IDF of the Spawn model goes next to it
- the room-wise internal gains repeat every day, and the user profiles read
  them periodically, so only one day of them goes to BESMod's Resources
- the .mos scripts go to BESMod's Resources/Scripts/Dymola and, for the HOM,
  plot the volume averaged and the lowest and highest room temperature
  rather than zone 1, which in the HOM is only the living room
"""

import argparse
import os
import re
import shutil
import tempfile
import warnings
from pathlib import Path

import numpy as np

from teaser.project import Project

PACKAGE = "HighOrderArchetypeExample"
BUILDING = "SingleFamilyHouse"
FULL_NAME = f"BESMod.Examples.TEASERExport.{PACKAGE}"
EXAMPLES = ["TEASERHeatLoadCalculation", "HeatPumpMonoenergetic", "HeatPumpSimple",
            "GasBoilerBuildingOnly"]
# BESMod's weather files for Spawn, the same weather as .mos and .epw
WEATHER = ("Resources", "Spawn", "Potsdam_TRY2015_normal")
IDF = f"{PACKAGE}_{BUILDING}.idf"
GAINS = f"InternalGains{PACKAGE}.txt"


def export_building(path, weather_file, epw_file):
    """Exports the archetype the BESMod example is made of, to path"""
    prj = Project()
    prj.name = PACKAGE
    prj.add_residential(
        construction_data="aixlib_S",
        geometry_data="aixlib_high_order_single_family_house",
        name=BUILDING,
        year_of_construction=1984,
        net_leased_area=170.0,
        number_of_floors=2,
        height_of_floors=2.6)
    prj.used_library_calc = "AixLib"
    prj.number_of_elements_calc = 4
    # Potsdam's design temperature, for the weather BESMod's examples run with
    prj.set_location_parameters(t_outside=273.15 - 12.6,
                                t_ground=273.15 + 13,
                                weather_file_path=str(weather_file),
                                calc_all_buildings=False)
    prj.calc_all_buildings()
    with warnings.catch_warnings():
        # that HeatPumpMonoenergetic has no Spawn variant
        warnings.simplefilter("ignore", UserWarning)
        return Path(prj.export_besmod(examples=EXAMPLES,
                                      THydSup_nominal=55 + 273.15,
                                      path=str(path),
                                      export_with_hom=True,
                                      export_with_spawn=True,
                                      spawn_epw_path=str(epw_file)))


def _write(path, text):
    """Writes text with Unix line endings, as BESMod's files have them
    (Path.write_text only takes newline from Python 3.10)"""
    with open(path, "w", encoding="utf-8", newline="\n") as file:
        file.write(text)


def _one_day_of_gains(year_file, day_file):
    """Writes the first day of TEASER's room-wise internal gains, which
    repeat every day, as a table running from 0 to 24 h"""
    table = np.loadtxt(year_file, skiprows=2)
    if np.abs(table[24:, 1:] - table[:-24, 1:]).max() != 0:
        raise ValueError(
            f"The internal gains in {year_file} do not repeat every day, so "
            f"one day of them would not do for the whole year any more.")
    # the yearly table starts at 1 h, at the end of the first hour
    day = np.vstack([np.r_[0.0, table[23, 1:]], table[:24]])
    Path(day_file).parent.mkdir(parents=True, exist_ok=True)
    with open(day_file, "w", newline="\n") as file:
        file.write("#1\n")
        file.write(f"double Internals({day.shape[0]}, {day.shape[1]})\n")
        for row in day:
            file.write("\t".join(f"{value:.10g}" for value in row) + "\n")


def _convert_model(text):
    """Moves one exported model into BESMod"""
    text = re.sub(r"(?<![\w.])" + PACKAGE + r"(?=[.;])", FULL_NAME, text)
    text = re.sub(
        r'"modelica://' + PACKAGE + r'/' + BUILDING
        + r'/InternalGains_\w+\.txt"',
        f'"modelica://BESMod/Resources/{GAINS}"', text)
    text = text.replace(f'"modelica://{PACKAGE}/{BUILDING}/{BUILDING}_Spawn.idf"',
                        f'"modelica://BESMod/Resources/Spawn/{IDF}"')
    # and the documentation naming it
    text = text.replace(f" {BUILDING}_Spawn.idf.", f" Resources/Spawn/{IDF}.")
    text = text.replace(f'"modelica://{PACKAGE}/Resources/',
                        f'"modelica://BESMod/{"/".join(WEATHER[:-1])}/')
    text = re.sub(
        r'"Resources/Scripts/Dymola/' + BUILDING + r'/(\w+\.mos)"',
        rf'"modelica://BESMod/Resources/Scripts/Dymola/Examples/TEASERExport/'
        rf'{PACKAGE}/{BUILDING}/\1"', text)
    for leftover in ('"modelica://' + PACKAGE, '"Resources/Scripts'):
        if leftover in text:
            raise ValueError(
                f"The export changed: {leftover} is left in a model after its "
                f"conversion to BESMod, update this script.")
    return text


def _convert_script(text, hom):
    """Moves one exported .mos script into BESMod"""
    if f'simulateModel("{PACKAGE}.' not in text:
        raise ValueError("The export changed: a .mos script does not simulate "
                         "the exported model any more, update this script.")
    text = text.replace(f'simulateModel("{PACKAGE}.',
                        f'simulateModel("{FULL_NAME}.')
    if hom:
        text = text.replace(
            'y={"ventilation.generation.TSup.T","ventilation.generation.weaBus.'
            'TDryBul","building.buiMeaBus.TZoneMea[1]"}, grid=true, subPlot=3, '
            'colors={{28,108,200},{238,46,47},{0,140,72}}',
            'y={"ventilation.generation.TSup.T","ventilation.generation.weaBus.'
            'TDryBul","outputs.building.TBuiVolAve","outputs.building.TBuiMin",'
            '"outputs.building.TBuiMax"}, grid=true, subPlot=3, '
            'colors={{28,108,200},{238,46,47},{0,140,72},{217,67,180},{0,0,0}}')
    return text


def _package_mo():
    return f'''within BESMod.Examples.TEASERExport;
package {PACKAGE} "TEASER's AixLib high order single family house, as reduced order, high order and Spawn model"
  extends Modelica.Icons.Package;

  annotation (Documentation(info="<html>
<p>
  The single family house of AixLib's high order model (HOM), generated by
  TEASER's archetype <code>AixLibHighOrderSingleFamilyHouse</code> for a building
  of 1984 with 170 m&sup2; and exported with <code>export_with_hom=True</code> and
  <code>export_with_spawn=True</code>. Every example therefore comes as up to three models,
  with the same energy system:
</p>
<ul>
  <li>without suffix, the building as TEASER's single zone reduced order model
  (<a href=\\"modelica://BESMod.Systems.Demand.Building.TEASERThermalSingleZone\\">TEASERThermalSingleZone</a>),
  with the user profiles of the ten rooms merged into its one zone by
  <a href=\\"modelica://BESMod.Systems.UserProfiles.TEASERHOMtoROM\\">TEASERHOMtoROM</a></li>
  <li>with the suffix <code>_HOM</code>, the same building as AixLib's high order model
  (<a href=\\"modelica://BESMod.Systems.Demand.Building.AixLibHighOrder\\">AixLibHighOrder</a>)
  with its ten heated rooms and the user profiles room by room
  (<a href=\\"modelica://BESMod.Systems.UserProfiles.AixLibHighOrderProfiles\\">AixLibHighOrderProfiles</a>)</li>
  <li>with the suffix <code>_Spawn</code>, the same rooms, constructions and user profiles as
  Spawn of EnergyPlus model
  (<a href=\\"modelica://BESMod.Systems.Demand.Building.SpawnHighOrder\\">SpawnHighOrder</a>)
  with the IDF TEASER writes (<code>modelica://BESMod/Resources/Spawn/{IDF}</code>), in the
  examples without mechanical ventilation, which SpawnHighOrder does not have. It needs the
  Buildings library with its Spawn binaries.</li>
</ul>
<p>
  The walls, windows and surface orientations of the HOM are TEASER's own records in
  <code>{BUILDING}_DataBase</code>, so both models are built from the same construction data,
  and all are sized from the same room-wise heat loads. Compared to the export, the weather is
  BESMod's pair of weather files for Spawn (TRY2015 Potsdam as .mos and .epw, which TEASER was
  given for the heat loads) and the internal gains are reduced to the one day they repeat
  (<code>modelica://BESMod/Resources/{GAINS}</code>).
</p>
<p>
  TEASER's example <code>e14_compare_hom_and_rom.py</code> compares the three models, and
  TEASER's script <code>scripts/update_besmod_hom_example.py</code> regenerates this package.
</p>
</html>"));
end {PACKAGE};
'''


def update_besmod_hom_example(besmod_path=None, weather_file=None,
                              epw_file=None):
    """Regenerates BESMod.Examples.TEASERExport.HighOrderArchetypeExample

    Parameters
    ----------
    besmod_path : str
        BESMod's package.mo or the directory holding it, by default the
        environment variable BESMOD_PATH.
    weather_file : str
        Weather file TEASER calculates the heat loads with, by default
        BESMod's TRY2015 Potsdam for Spawn, which the examples run with.
    epw_file : str
        The same weather for EnergyPlus, by default BESMod's.

    Returns
    -------
    besmod : pathlib.Path
        The BESMod package directory the example was written to.
    """
    if besmod_path is None:
        besmod_path = os.environ.get("BESMOD_PATH")
    if besmod_path is None:
        raise ValueError("Give BESMod's package.mo, or set BESMOD_PATH.")
    besmod = Path(besmod_path)
    if besmod.name == "package.mo":
        besmod = besmod.parent
    if weather_file is None:
        weather_file = besmod.joinpath(*WEATHER).with_suffix(".mos")
    if epw_file is None:
        epw_file = besmod.joinpath(*WEATHER).with_suffix(".epw")
    destination = besmod.joinpath("Examples", "TEASERExport", PACKAGE)
    scripts = besmod.joinpath("Resources", "Scripts", "Dymola", "Examples",
                              "TEASERExport", PACKAGE, BUILDING)

    with tempfile.TemporaryDirectory() as export_directory:
        export = export_building(export_directory, weather_file, epw_file)

        for directory in (destination, scripts):
            if directory.exists():
                shutil.rmtree(directory)
        shutil.copytree(export.joinpath(BUILDING),
                        destination.joinpath(BUILDING),
                        ignore=shutil.ignore_patterns("*.txt", "*.idf"))
        spawn = besmod.joinpath(*WEATHER[:-1])
        spawn.mkdir(parents=True, exist_ok=True)
        shutil.copy(export.joinpath(BUILDING, f"{BUILDING}_Spawn.idf"),
                    spawn.joinpath(IDF))
        _one_day_of_gains(
            export.joinpath(BUILDING, f"InternalGains_{BUILDING}_HOM.txt"),
            besmod.joinpath("Resources", GAINS))
        for model in destination.joinpath(BUILDING).rglob("*.mo"):
            _write(model, _convert_model(model.read_text(encoding="utf-8")))

        scripts.mkdir(parents=True)
        for script in export.joinpath(
                "Resources", "Scripts", "Dymola", BUILDING).glob("*.mos"):
            _write(scripts.joinpath(script.name),
                   _convert_script(script.read_text(encoding="utf-8"),
                                   hom=script.stem.endswith("_HOM")))

    _write(destination.joinpath("package.mo"), _package_mo())
    _write(destination.joinpath("package.order"), BUILDING + "\n")

    order = besmod.joinpath("Examples", "TEASERExport", "package.order")
    if order.exists():
        entries = order.read_text(encoding="utf-8").split()
        if PACKAGE not in entries:
            with open(order, "a", encoding="utf-8", newline="\n") as file:
                file.write(PACKAGE + "\n")
    return besmod


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("besmod_path", nargs="?", default=None,
                        help="BESMod's package.mo or the directory holding "
                             "it, by default BESMOD_PATH")
    besmod = update_besmod_hom_example(parser.parse_args().besmod_path)
    print(f"Updated {besmod.joinpath('Examples', 'TEASERExport', PACKAGE)}")
