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
        print('Loaded ',scenarios.__len__(),' scenarios')
        return scenarios
    except:
        print('Error while loading scenarios')


def generate_bldg(prj, scenario):
    #TODO: add building type features with dict or json file

    if scenario['Building_class'] == "non_residential":
        prj.add_non_residential(
            method='bmvbs',
            usage=scenario['Building_type'],
            name=str(scenario['Scenario_number'])+"_"+str(scenario['Building_type']),
            year_of_construction=scenario['Year_of_construction'],
            number_of_floors=4,
            height_of_floors=3.5,
            net_leased_area=scenario['Net_Area'])

    elif scenario['Building_class'] == "residential":
        prj.add_residential(
            method='tabula_de',
            usage=scenario['Building_type'],
            name=str(scenario['Scenario_number'])+"_"+str(scenario['Building_type']),
            year_of_construction=scenario['Year_of_construction'],
            number_of_floors=2,
            height_of_floors=3,
            net_leased_area=scenario['Net_Area'],
            construction_type='tabula_standard')
    else:
        print("Could not resolve building class")
        pass
    return prj

def export_aixlib_model(prj,model_path,location):

    weather_data = {"Aachen":                   "TRY2015_507931060546_Jahr_City_Aachen.mos",
                    "Garmisch-Partenkirchen":   "TRY2015_474849111318_Jahr_City_Garmisch-Partenkirchen.mos",
                    "München":                  "TRY2015_481308115636_Jahr_City_Muenchen.mos",
                    "Frankfurt":                "TRY2015_501260086749_Jahr_City_Frankfurt.mos",
                    "Gerolstein":               "TRY2015_502252066685_Jahr_City_Gerolstein.mos",
                    "Greifswald":               "TRY2015_541071133759_Jahr_City_Greifswald.mos"
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

if __name__ == "__main__":

    setup_name = "20220210_efh_wettervergleich"
    basepath = pathlib.Path('N:\Forschung\EBC0741_ZIM_SmartSenseIAQ_NK\Data\Simulationen\Referenzszenarien').joinpath(setup_name)
    scenarios = load_scenarios(basepath.joinpath("scenarios.xlsx"))
    model_export_path = basepath.joinpath("models")

    for index,scenario in scenarios.iterrows():
        scenario_name = "S"+str(scenario['Scenario_number'])+"_"+str(scenario['Building_type'])
        prj = generate_project(name=scenario_name)
        prj = generate_bldg(prj, scenario)
        export_aixlib_model(prj, model_export_path.joinpath(scenario_name), scenario['Location'])

        simulate(
            aixlib_mo=r"D:\pse\GIT\AixLib\AixLib\package.mo",
            teaser_mo=model_export_path.joinpath(scenario_name,prj.name,"package.mo"),
            building_mo=prj.name+"."+prj.buildings[0].name+"."+prj.buildings[0].name,
            savepath=model_export_path.parent.joinpath("sim_results",scenario_name),
            result_file_name= prj.buildings[0].name,
            n_cpu=1
        )
