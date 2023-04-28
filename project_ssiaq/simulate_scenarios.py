import teaser.logic.utilities as utilities
import os
import pathlib
import easygui as gui
import pandas as pd
from datetime import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
# Imports from ebcpy
from ebcpy import DymolaAPI, TimeSeriesData, FMU_API
from ebcpy.utils.conversion import convert_tsd_to_modelica_txt


def generate_project(name):
    from teaser.project import Project
    prj = Project(load_data=True)
    prj.name = name
    return prj


def load_scenarios(scenario_file=None):
    if scenario_file is None:
        default_path = 'N:\Forschung\EBC0741_ZIM_SmartSenseIAQ_NK\Data\AP6_Anlagen und Gebäudebaukasten'
        scenario_file = gui.fileopenbox("Choose Scenario File", default=default_path)

    try:
        scenarios = pd.read_excel(scenario_file)

        ass_error_building_class = "only 'residential' and 'non_residential' are valid building classes for archetype generation"
        assert scenarios.Building_class.isin(["residential", "non_residential"]).all(), ass_error_building_class

        ass_error_building_type = "check building types for typos"
        assert scenarios.Building_type.isin(["single_family_house",
                                             "multi_family_house",
                                             "terraced_house",
                                             "apartment_block",
                                             "office",
                                             "school",
                                             "hotel"
                                             ]).all(), ass_error_building_type

        ass_error_net_area = "check if net area is betwenn 10 and 20000 "
        assert scenarios.Net_Area.between(10,20000).all(), ass_error_net_area

        ass_error_year_of_construction = "check if year of construction is betwenn 1850 and 2023 "
        assert scenarios.Year_of_construction.between(1850,2023).all(), ass_error_year_of_construction

        ass_error_modernization = "only 'non-modernized' and 'modernized' are valid modernization states"
        assert scenarios.Modernization_state.isin(["non-modernized", "modernized"]).all(), ass_error_modernization

        ass_error_equipment = "only 'natural_ventilation' and 'air_conditioned' are valid equipment states"
        assert scenarios.Equipment.isin(["natural_ventilation", "air_conditioned"]).all(), ass_error_equipment

        ass_error_usage = "only 'standard' are valid usage types"
        assert scenarios.Usage_profile.isin(["standard"]).all(), ass_error_usage

        ass_error_location = "check locations for typos"
        assert scenarios.Location.isin(["Aachen",
                                        "München",
                                        "Gerolstein",
                                        "Frankfurt",
                                        "Garmisch-Partenkirchen",
                                        "Greifswald"]).all(), ass_error_location

        ass_error_control = "only 'reference', 'demand_driven' and 'MPC' are valid equipment states"
        assert scenarios.Control_strategy.isin(["reference",
                                              "demand_driven",
                                              "MPC"]).all(), ass_error_control
    except AssertionError as err:
        print('Error while loading scenarios')
        print(err)
    else:
        print('Loaded ', scenarios.__len__(), ' scenarios')
        return scenarios



def generate_bldg(prj, scenario):
    # TODO: add building type features with dict or json file

    if scenario['Building_class'] == "non_residential":
        if scenario['Equipment'] == 'air_conditioned':
            ahu_usage = True
        else:
            ahu_usage = False

        if scenario['Building_type'] in ["hotel","school"]:
            method = "dataNWG"
        else:
            method = "bmvbs"

        prj.add_non_residential(
            method=method,
            usage=scenario['Building_type'],
            name=str(scenario['Scenario_number']) + "_" + str(scenario['Building_type']),
            year_of_construction=scenario['Year_of_construction'],
            with_ahu=ahu_usage,
            number_of_floors=3,
            height_of_floors=3.5,
            net_leased_area=scenario['Net_Area'],
            control_type=scenario['Control_strategy'])

    elif scenario['Building_class'] == "residential":
        if scenario['Modernization_state'] == "modernized":
            construction_type = 'tabula_retrofit'
        else:
            construction_type = 'tabula_standard'

        prj.add_residential(
            method='tabula_de',
            usage=scenario['Building_type'],
            name=str(scenario['Scenario_number']) + "_" + str(scenario['Building_type']),
            year_of_construction=scenario['Year_of_construction'],
            number_of_floors=2,
            height_of_floors=3,
            net_leased_area=scenario['Net_Area'],
            construction_type=construction_type)
    else:
        print("Could not resolve building class")
        pass
    return prj


def export_aixlib_model(prj, model_path, location):
    weather_data = {"Aachen": "TRY2015_507931060546_Jahr_City_Aachen.mos",
                    "Garmisch-Partenkirchen": "TRY2015_474849111318_Jahr_City_Garmisch-Partenkirchen.mos",
                    "München": "TRY2015_481308115636_Jahr_City_Muenchen.mos",
                    "Frankfurt": "TRY2015_501260086749_Jahr_City_Frankfurt.mos",
                    "Gerolstein": "TRY2015_502252066685_Jahr_City_Gerolstein.mos",
                    "Greifswald": "TRY2015_541071133759_Jahr_City_Greifswald.mos"
                    }

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
            weather_data[location]))

    prj.calc_all_buildings()

    path = prj.export_aixlib(
        internal_id=None,
        path=model_path)

    return path


def simulate(
        aixlib_mo,
        teaser_mo,
        building_mo,
        savepath,
        result_file_name,
        cd=None,
        n_cpu=1,
        with_plot=True
):
    """
    Arguments of this example:
    :param str aixlib_mo:
        Path to the package.mo of the AixLib.
        This example was tested for AixLib version 1.0.0.
    :param str cd:
        Path in which to store the output.
        Default is the examples\results folder
    :param int n_cpu:
        Number of processes to use
    :param bool with_plot:
        Show the plot at the end of the script. Default is True.
    """

    # General settings
    if cd is None:
        cd = pathlib.Path(__file__).parent.joinpath("results")

    dym_api = DymolaAPI(
        model_name=building_mo,
        cd=cd,
        n_cpu=n_cpu,
        packages=[aixlib_mo, teaser_mo],
        show_window=True,
        n_restart=-1,
        equidistant_output=False,
        extract_variables=False
    )

    simulation_setup = {"start_time": 0,
                        "stop_time": 31536000,
                        "output_interval": 1000}

    dym_api.set_sim_setup(sim_setup=simulation_setup)

    dym_api.simulate(
        return_option="savepath",
        savepath=savepath,
        result_file_name=result_file_name
    )
    dym_api.close()


if __name__ == "__main__":

    setup_name = "20230425_test"
    basepath = pathlib.Path('N:\Forschung\EBC0741_ZIM_SmartSenseIAQ_NK\Data\Simulationen/02_Bedarfsorierntierte_Regelung').joinpath(
        setup_name)
    scenarios = load_scenarios(basepath.joinpath("scenarios.xlsx"))
    model_export_path = basepath.joinpath("models")

    for index, scenario in scenarios.iterrows():
        scenario_name = "S" + str(scenario['Scenario_number']) + "_" + str(scenario['Building_type'])
        prj = generate_project(name=scenario_name)
        prj = generate_bldg(prj, scenario)
        export_aixlib_model(prj, model_export_path.joinpath(scenario_name), scenario['Location'])

        simulate(
            aixlib_mo=r"D:\GIT\AixLib\AixLib\package.mo",
            teaser_mo=model_export_path.joinpath(scenario_name, prj.name, "package.mo"),
            building_mo=prj.name + "." + prj.buildings[0].name + "." + prj.buildings[0].name,
            savepath=model_export_path.parent.joinpath("sim_results", scenario_name),
            result_file_name=prj.buildings[0].name,
            n_cpu=1
        )
