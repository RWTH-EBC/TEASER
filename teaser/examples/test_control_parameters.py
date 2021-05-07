import teaser.logic.utilities as utilities
import os
import warnings

import pandas as pd
import datetime
import json
import collections
import multiprocessing

# helper scripts
import utils.simulate as sim
import utils.read_results as res

def test_generate_archetype():
    from teaser.project import Project

    prj = Project(load_data=True)
    prj.name = "ArchetypeEFH"

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="ResidentialBuilding",
        year_of_construction=1990,
        number_of_floors=1,
        height_of_floors=3.0,
        net_leased_area=200.0,
        construction_type="heavy")

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanel7040",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

    return prj

def test_export_aixlib():
    prj = test_generate_archetype()

    prj.dir_reference_results = utilities.get_full_path(
        os.path.join(
            "examples",
            "examplefiles",
            "ReferenceResults",
            "Dymola"))

    print(prj.dir_reference_results)

    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 2
    prj.weather_file_path = utilities.get_full_path(
        os.path.join(
            "data",
            "input",
            "inputdata",
            "weatherdata",
            "DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos"))

    prj.calc_all_buildings()

    path = prj.export_aixlib(
        internal_id=None,
        path=None)

    return path

if __name__ == '__main__':
    #test_export_aixlib()

    DIR_SCRIPT = os.path.abspath(os.path.dirname(__file__))
    DIR_TOP = os.path.abspath(DIR_SCRIPT)
    #random_name = random_choice()
    index = pd.date_range(datetime.datetime(2020, 1, 1), periods=8761, freq="H")

    #prj = Project(load_data=True)
    # prj.name = "Shamrock_Park_{}_{}".format("fbkk", "ref")
    #prj.name = "Shamrock_Park_{}_{}".format(random_name, "ref")

    info_path = os.path.join(DIR_TOP, "shamrock_park")
    prj = test_generate_archetype()
    prj.weather_file_path = utilities.get_full_path(
        os.path.join(
            "data",
            "input",
            "inputdata",
            "weatherdata",
            "DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos"))

    RESULTS_PATH = os.path.join(DIR_TOP, "results")
    prj.export_aixlib()
    prj.save_project()

    sim.queue_simulation(
        sim_function=sim.simulate,
        prj=prj,
        results_path=RESULTS_PATH,
        number_of_workers=multiprocessing.cpu_count() - 3,
    )
    for bldg in prj.buildings:
        signals = [
            "multizone.PHeater[{}]".format(i + 1)
            for i in range(len(bldg.thermal_zones))
        ]
        signals += [
            "multizone.PCooler[{}]".format(i + 1)
            for i in range(len(bldg.thermal_zones))
        ]
        res.read_results(
            prj=prj,
            signals=signals,
            buildings=[bldg],
            index=index,
            results_path=os.path.join(RESULTS_PATH, prj.name),
            csv_path=os.path.join(RESULTS_PATH, prj.name, "demand_csv"),
        )

    print("That's it! :)")

