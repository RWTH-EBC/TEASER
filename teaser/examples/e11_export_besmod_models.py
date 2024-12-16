# # Example 11: Export Modelica models for BESMod library using TEASER API
# This module demonstrates how to export building models from a TEASER project
# to ready-to-run simulation models for the Modelica BESMod library.
# BESMod enables seamless integration with state-of-the-art energy systems,
# such as heat pumps and photovoltaic systems. These systems can be utilized
# to generate primary energy demand curves (e.g., for electricity or gas) or
# to conduct in-depth analyses of building energy systems. In contrast,
# AixLib focuses on ideal heat demand calculation, and IBPSA on
# free floating temperature without an ideal heater.
# You can execute this example using
# [jupyter-notebook](https://mybinder.org/v2/gh/RWTH-EBC/TEASER/main?labpath=docs%2Fjupyter_notebooks)

import teaser.examples.e1_generate_archetype as e1
import teaser.logic.utilities as utilities
import os


def example_export_besmod():
    """This function demonstrates the export to Modelica library BESMod using
    the API function of TEASER"""

    # ## Standard export
    # In e1_generate_archetype we created a Project with three archetype
    # buildings to get this Project we rerun this example

    prj = e1.example_generate_archetype()

    # Configure project settings to ensure compatibility with BESMod. The BESMod
    # library uses the AixLib.ThermalZones.ReducedOrder.ThermalZone.ThermalZone model
    # with 4 elements for the demand building model. Other numbers of elements are possible,
    # but compatability with ARoof for PV and AFloor for UFH systems must be checked first.
    # Set these parameters in the project:
    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 4

    # BESMod allows building models to be included in predefined example energy systems:
    examples = [
        "TEASERHeatLoadCalculation",  # Ideal electric heater for heat load calculations
        "HeatPumpMonoenergetic",  # Heat pump with radiators, buffer and DHW storage, and PV
        "GasBoilerBuildingOnly"  # Gas boiler with radiators
    ]

    # For the hydraulic systems, you have to specify a nominal supply temperature
    # for heat transfer, e.g. in radiators.
    # Multiple options are available:

    # Option 1: Set a single value for all buildings and zones.
    THydSup_nominal = 55 + 273.15

    # Option 2: Set values for each building or thermal zone.
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

    # Option 3: Specify values based on construction year.
    # Here, the value of the next higher specified year is set to the building.
    # The classification here is taken from:
    # https://www.ffe.de/projekte/waermepumpen-fahrplan-finanzielle-kipppunkte-zur-modernisierung-mit-waermepumpen-im-wohngebaeudebestand/
    THydSup_nominal = {
        1950: 90 + 273.15,
        1980: 70 + 273.15,
        2010: 55 + 273.15,
        2024: 35 + 273.15
    }

    # In the examples, the parameters for BESMod.Systems.UserProfiles.TEASERProfiles are configured,
    # including internal gains and heating profiles for each zone.
    # BESMod requires 24-hour heating profiles, which are used
    # to define the parameters of the `setBakTSetZone` Pulse block.
    # By default, the TEASER profiles are applied, but these can be customized if needed.

    # Additionally, location-specific parameters must be set, which can be achieved using the following function.
    # The default values provided here correspond to Mannheim.
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
    # run prj.calc_all_buildings() function which is here already done in the set_location_parameters function.

    # Export all buildings to BESMod and include them in predefined example systems.
    path = prj.export_besmod(
        THydSup_nominal=THydSup_nominal,
        path=None,
        examples=examples
    )

    # ## Partial retrofit export
    # The partial retrofit option of the energy system in BESMod can also be utilized.
    # For more information on this see BESMod.UsersGuide.GettingStarted.Parameterization.
    # To enable this here, the nominal heat flow of each zone in the building must be extracted prior to the retrofit.
    QBuiOld_flow_design = {
        bldg.name: {
            tz.name: tz.model_attr.heat_load for tz in bldg.thermal_zones
        }
        for bldg in prj.buildings
    }

    # Retrofit project buildings and recalculate parameters.
    prj.name = "ArchetypeExample_partial_retrofit"
    prj.retrofit_all_buildings(
        year_of_retrofit=2015,
        type_of_retrofit="adv_retrofit",
        window_type='Alu- oder Stahlfenster, Isolierverglasung',
        material='EPS_perimeter_insulation_top_layer'
    )
    prj.calc_all_buildings()

    # By default, radiator transfer systems are not retrofitted when the
    # QBuiOld_flow_design parameter is provided and differs from the new nominal heat flow.
    # Additionally, new THydSup_nominal temperatures can be specified alongside
    # THydSupOld_design values, which are used for radiator sizing but not for control settings.

    path = prj.export_besmod(
        THydSup_nominal=THydSup_nominal,
        QBuiOld_flow_design=QBuiOld_flow_design,
        path=None,
        examples=examples
    )

    # ## Custom export
    # Additionally, we have the flexibility to define custom templates for including buildings in specific setups.
    # For instance, a custom template is defined here to include the building in the
    # ModelicaConferencePaper example from BESMod, which features an integrated battery system.

    # Custom template
    # ```
    # < %namespace file = "/modelica_language/" import="get_list" / >
    # within ${bldg.parent.name}.${bldg.name};
    # model ModelicaConferencePaper${bldg.name}
    #     extends BESMod.Examples.ModelicaConferencePaper.PartialModelicaConferenceUseCase(
    #       redeclare ${bldg.name} building,
    #       redeclare BESMod.Systems.UserProfiles.TEASERProfiles
    #       userProfiles(fileNameIntGains=Modelica.Utilities.Files.loadResource(
    #               "modelica://${bldg.parent.name}/${bldg.name}/InternalGains_${bldg.name}.txt"),
    #                setBakTSetZone(amplitude=${get_list(setBakTSetZone_amplitude)},
    #                               width =${get_list(setBakTSetZone_width)},
    #                               startTime =${get_list(setBakTSetZone_startTime)})),
    #     systemParameters(nZones=${len(bldg.thermal_zones)},
    #                      QBui_flow_nominal = building.QRec_flow_nominal,
    #                      TOda_nominal =${TOda_nominal},
    #                      TSetZone_nominal =${get_list(TSetZone_nominal)},
    #                      THydSup_nominal =${THydSup_nominal},
    #                      QBuiOld_flow_design =${QBuiOld_flow_design},
    #                      THydSupOld_design =${THydSupOld_design},
    #                      filNamWea = Modelica.Utilities.Files.loadResource(
    #                           "modelica://${bldg.parent.name}/Resources/${bldg.parent.weather_file_name}")));
    #
    #    extends Modelica.Icons.Example;
    #
    #     annotation(experiment(StopTime=172800,
    #                           Interval=600,
    #                           Tolerance=1e-06),
    #                __Dymola_Commands(file=
    #                                  "Resources/Scripts/Dymola/${bldg.name}/ModelicaConferencePaper${bldg.name}.mos"
    #                                  "Simulate and plot"));
    # end
    # ModelicaConferencePaper${bldg.name};
    # ```

    prj.name = "ArchetypeExample_custom"

    custom_template_path = os.path.join(
        os.path.dirname(__file__), "examplefiles", "custom_besmod_templates"
    )
    custom_example_template = {"ModelicaConferencePaper": os.path.join(custom_template_path, "custom_template.txt")}

    # The template also includes a .mos script as part of its annotation.
    # By default, the provided examples export a basic "simulate and plot" script,
    # which is incorporated into their annotation, as shown in the custom example.
    # Additionally, you have the flexibility to modify the template for existing examples
    # and define custom scripts for your tailored examples.

    custom_script = {"HeatPumpMonoenergetic": os.path.join(custom_template_path, "custom_script_hp_mono.txt"),
                     "ModelicaConferencePaper": os.path.join(custom_template_path, "custom_script.txt")}

    path = prj.export_besmod(
        THydSup_nominal=THydSup_nominal,
        path=None,
        examples=examples,
        custom_examples=custom_example_template,
        custom_script=custom_script
    )

    return path


if __name__ == '__main__':
    example_export_besmod()

    print("Example 11: That's it! :)")
