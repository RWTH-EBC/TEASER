# # Example 4: Export Modelica models for BESMod library using TEASER API

# This module contains an example how to export buildings from a TEASER
# project to ready-to-run simulation models for Modelica library BESMod.
# You can run this example using the [jupyter-notebook](https://mybinder.org/v2/gh/RWTH-EBC/TEASER/master?labpath=docs%2Fjupyter_notebooks)

import teaser.examples.e1_generate_archetype as e1
import teaser.logic.utilities as utilities
import os


def example_export_besmod(save_dir_path=None):
    """This function demonstrates the export to Modelica library BESMod using
    the API function of TEASER"""

    # In e1_generate_archetype we created a Project with three archetype
    # buildings to get this Project we rerun this example

    prj = e1.example_generate_archetype()

    # To make sure the export is using the desired parameters you should
    # always set model settings in the Project.
    # The TEASER building in BESMod uses the AixLib.ThermalZones.ReducedOrder.ThermalZone.ThermalZone model
    # with 4 elements, so we have to set these project settings

    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 4

    # With these information we could already export the building models
    # which extend from BESMod.Systems.Demand.Building.TEASERThermalZone.
    # But we have also the option to include these building models directly in
    # predefined example building energy systems. These systems are:
    # "TEASERHeatLoadCalculation" which is a system with an ideal electric heater for heat load calculation.
    # "HeatPumpMonoenergetic" which is a system with a heat pump and an electric heater in serial,
    # buffer and DHW storages, radiators and PV.
    # "GasBoilerBuildingOnly" which is a system with a gas boiler and radiators.

    examples = ["TEASERHeatLoadCalculation",
                "HeatPumpMonoenergetic",
                "GasBoilerBuildingOnly"]

    # For the examples with hydraulic system, we need further parameters to get fully parameterized ready to run model.
    # This is manly the nominal hydraulic supply temperature. We have different options to set this value.
    # First, we can set one value for all buildings and thermal zones in the project.
    THydSup_nominal = 55 + 273.15
    # Second, we can set the value separately for each building and with in the building also for each thermal zone.
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
    # Third, we can specify the value for a building by the construction year. Here the value of the next higher
    # specified year is set to the building. The classification here is taken from
    # https://www.ffe.de/projekte/waermepumpen-fahrplan-finanzielle-kipppunkte-zur-modernisierung-mit-waermepumpen-im-wohngebaeudebestand/
    THydSup_nominal = {1950: 90 + 273.15, 1980: 70 + 273.15, 2010: 55 + 273.15, 2024: 35 + 273.15}

    # The parameters for the BESMod.Systems.UserProfiles.TEASERProfiles are also set in the export of
    # the examples. The internal gains file which is exported with the building is set and heating set backs
    # are extracted from the heating_profile of each zone and directly set in the setBakTSetZone Pulse block.
    # BESMod only allows 24 hours heating profiles.

    # We also need to set location specific parameters which we can do with the following function.
    # The values we set here are the default values which correspond to Mannheim.

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

    # To make sure the parameters are calculated correctly we recommend to
    # run prj.calc_all_buildings() function which is here already done in the set_location_parameters function

    # Now we export all building in the project and also include it in all optional examples.
    path = prj.export_besmod(
        THydSup_nominal=THydSup_nominal,
        path=save_dir_path,
        examples=examples
    )

    # We can also utilize the partial retrofit option of the energy system in BESMod.
    # For that we need to extract the nominal heat flow of each zone in the building
    # and then retrofit the buildings here in TEASER.

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
        material='EPS_perimeter_insulation_top_layer'
    )
    prj.calc_all_buildings()

    # When we now set heat flow of the old building design.
    # By default, the radiator transfer systems are not retrofitted when the
    # QBuiOld_flow_design parameter is set and different to the new nominal heat flow.
    # We would also have the option to set new THycSup_nominal temperatures and set
    # the old temperatures with THydSupOld_design which are used for the sizing of the radiators
    # but not in the controls.

    path = prj.export_besmod(
        THydSup_nominal=THydSup_nominal,
        QBuiOld_flow_design=QBuiOld_flow_design,
        path=save_dir_path,
        examples=examples
    )

    # If QBuiOld_flow_design is not set the energy system is also totally retrofitted to the new heat demand.
    # We have also the option to define custom templates into which the building should be included.
    # For example, we have here a custom template where the building is included in the
    # ModelicaConferencePaper example in BESMod which als includes a battery.

    prj.name = "ArchetypeExample_total_retrofit"

    custom_template_path = os.path.join(
        os.path.dirname(__file__), "examplefiles", "custom_besmod_templates"
    )
    custom_example_template = {"ModelicaConferencePaper": os.path.join(custom_template_path,"custom_template.txt")}

    # Also .mos scripts can be generated with a template and exported together with the model.
    # For the existing examples a basic simulate and plot .mos script is exported

    custom_script = {"HeatPumpMonoenergetic": os.path.join(custom_template_path,"custom_script_hp_mono.txt"),
                     "ModelicaConferencePaper": os.path.join(custom_template_path,"custom_script.txt")}
    path = prj.export_besmod(
        THydSup_nominal=THydSup_nominal,
        path=save_dir_path,
        examples=examples,
        custom_examples=custom_example_template,
        custom_script=custom_script
    )

    return path


if __name__ == '__main__':
    example_export_besmod(save_dir_path=r"D:\fwu-hst\TEASEROutput_besmod")

    print("Example 4: That's it! :)")
