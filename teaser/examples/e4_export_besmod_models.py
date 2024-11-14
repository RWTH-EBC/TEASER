# # Example 2: Export Modelica models for AixLib library using TEASER API

# This module contains an example how to export buildings from a TEASER
# project to ready-to-run simulation models for Modelica library AixLib. These
# models will only simulate using Dymola, the reason for this are state
# machines that are used in one AixLib specific AHU model.
# You can run this example using the [jupyter-notebook](https://mybinder.org/v2/gh/RWTH-EBC/TEASER/master?labpath=docs%2Fjupyter_notebooks)

import teaser.examples.e1_generate_archetype as e1
import teaser.logic.utilities as utilities
import os


def example_export_besmod():
    """This function demonstrates the export to Modelica library AixLib using
    the API function of TEASER"""

    # In e1_generate_archetype we created a Project with three archetype
    # buildings to get this Project we rerun this example

    prj = e1.example_generate_archetype()

    # To make sure the export is using the desired parameters you should
    # always set model settings in the Project.
    # Project().used_library_calc specifies the used Modelica library
    # Project().number_of_elements_calc sets the models order
    # For more information on models we'd like to refer you to the docs. By
    # default TEASER uses a weather file provided in
    # teaser.data.input.inputdata.weatherdata. You can use your own weather
    # file by setting Project().weather_file_path. However we will use default
    # weather file.
    # Be careful: Dymola does not like whitespaces in names and filenames,
    # thus we will delete them anyway in TEASER.

    # for CI testing purpose we set the reference result folder

    prj.dir_reference_results = utilities.get_full_path(
        os.path.join(
            "examples",
            "examplefiles",
            "ReferenceResults",
            "Dymola"))

    print(prj.dir_reference_results)

    prj.used_library_calc = 'AixLib'  # ToDo fwu-hst: Always AixLib? If true, put it in explicit in besmod_output
    prj.number_of_elements_calc = 4
    prj.weather_file_path = utilities.get_full_path(
        os.path.join(
            "data",
            "input",
            "inputdata",
            "weatherdata",
            "DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos"))  # ToDo fwu-hst: add to export (look at AixLib export)

    # To make sure the parameters are calculated correctly we recommend to
    # run calc_all_buildings() function

    prj.calc_all_buildings()

    # To export the ready-to-run models simply call Project.export_aixlib().
    # You can specify the path, where the model files should be saved.
    # None means, that the default path in your home directory
    # will be used. If you only want to export one specific building, you can
    # pass over the internal_id of that building and only this model will be
    # exported. In this case we want to export all buildings to our home
    # directory, thus we are passing over None for both parameters.

    examples = ["TEASERHeatLoadCalculation",
                "HeatPumpMonoenergetic",
                "GasBoilerBuildingOnly"]

    THydSup_nominal = 55 + 273.15
    THydSup_nominal = {1950: 90+273.15, 1980: 70+273.15, 2010: 55+273.15, 2024: 35+273.15}
    THydSup_nominal = {"ResidentialBuilding": 328.15,
                       "OfficeBuilding": 328.15,
                       "InstituteBuilding": 343.15,
                       "InstituteBuildingMoisture": 343.15,
                       "ResidentialBuildingTabula": 328.15,
                       "ResidentialBuildingTabulaMulti": 328.15}

    path = prj.export_besmod(
        THydSup_nominal=THydSup_nominal,
        internal_id=None,
        path=r"D:\fwu-hst\TEASEROutput_besmod",
        examples=examples,
        report=True
    )


    QBuiOld_flow_design = {}
    for bldg in prj.buildings:
        QBuiOld_flow_design[bldg.name] = {}
        for tz in bldg.thermal_zones:
            QBuiOld_flow_design[bldg.name][tz.name] = tz.model_attr.heat_load
    # ToDo fwu-hst: set t_outside for heat_load calculation?
    prj.name = "ArchetypeExample_partial_retrofit"

    prj.retrofit_all_buildings(
        year_of_retrofit=2015,
        type_of_retrofit="adv_retrofit",
        window_type='Alu- oder Stahlfenster, Isolierverglasung',
        material='EPS_perimeter_insulation_top_layer')

    prj.calc_all_buildings()

    path = prj.export_besmod(
        THydSup_nominal=THydSup_nominal,
        QBuiOld_flow_design=QBuiOld_flow_design,
        internal_id=None,
        path=r"D:\fwu-hst\TEASEROutput_besmod",
        examples=examples,
        report=True
    )

    prj.name = "ArchetypeExample_total_retrofit"

    path = prj.export_besmod(
        THydSup_nominal=THydSup_nominal,
        internal_id=None,
        path=r"D:\fwu-hst\TEASEROutput_besmod",
        examples=examples,
        report=True
    )

    return path


if __name__ == '__main__':

    example_export_besmod()

    print("Example 2: That's it! :)")
