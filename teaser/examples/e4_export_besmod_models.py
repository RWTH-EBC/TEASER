# # Example 2: Export Modelica models for AixLib library using TEASER API

# This module contains an example how to export buildings from a TEASER
# project to ready-to-run simulation models for Modelica library BESMod.
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


    prj.dir_reference_results = utilities.get_full_path(
        os.path.join(
            "examples",
            "examplefiles",
            "ReferenceResults",
            "Dymola"))

    print(prj.dir_reference_results)

    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 4

    Residential = [
        bldg for bldg in prj.buildings if bldg.name == "ResidentialBuilding"][0]

    Residential.thermal_zones[0].use_conditions.set_back_times = [5, 22]
    Residential.thermal_zones[0].use_conditions.heating_set_back = -3
    # Residential.thermal_zones[0].use_conditions.calc_adj_schedules()

    weather_file_path = utilities.get_full_path(
        os.path.join(
            "data",
            "input",
            "inputdata",
            "weatherdata",
            "DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos"))


    prj.set_location_parameters(t_outside=262.65,
                                t_ground=286.15,
                                weather_file_path=weather_file_path,
                                calc_all_buildings=True)

    # prj.calc_all_buildings()

    examples = ["TEASERHeatLoadCalculation",
                "HeatPumpMonoenergetic",
                "GasBoilerBuildingOnly"]

    THydSup_nominal = 55 + 273.15
    THydSup_nominal = {1950: 90+273.15, 1980: 70+273.15, 2010: 55+273.15, 2024: 35+273.15}
    THydSup_nominal = {"ResidentialBuilding": 328.15,
                       "OfficeBuilding": 328.15,
                       "InstituteBuilding": {"Office": 343.15,
                                             "Floor": 343.15,
                                             "Storage": 343.15,
                                             "Meeting": 343.15,
                                             "Restroom": 343.15,
                                             "ICT": 343.15,
                                             "Laboratory": 328.15},
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

    custom_template = {"ModelicaConferencePaper": r"D:\fwu-hst\00_temp\custom_template.txt"}
    custom_script = {"HeatPumpMonoenergetic": r"D:\fwu-hst\00_temp\custom_script_hp_mono.txt",
                     "ModelicaConferencePaper": r"D:\fwu-hst\00_temp\custom_script.txt"}

    path = prj.export_besmod(
        THydSup_nominal=THydSup_nominal,
        internal_id=None,
        path=r"D:\fwu-hst\TEASEROutput_besmod",
        examples=examples,
        custom_examples=custom_template,
        custom_script=custom_script,
        report=True
    )

    return path


if __name__ == '__main__':

    example_export_besmod()

    print("Example 2: That's it! :)")
