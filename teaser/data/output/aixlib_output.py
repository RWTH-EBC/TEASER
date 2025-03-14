"""This module contains function for AixLib model generation"""

import os
import warnings
import shutil
from mako.template import Template
from mako.lookup import TemplateLookup
import teaser.logic.utilities as utilities
import teaser.data.output.modelica_output as modelica_output


def export_multizone(
        buildings,
        prj,
        path=None,
        use_postprocessing_calc=False,
        export_vars=None,
        custom_multizone_template_path=None):
    """Exports models for AixLib library

    Exports a building for
    AixLib.ThermalZones.ReducedOrder.Multizone.MultizoneEquipped models
    using the ThermalZoneEquipped and supporting models, like tables and weather
    model. Depending on chosen calculation method the parameter set to 1,2,
    3 or 4 element model. By default it uses the  correction for solar
    glazing (corG) and decoupled heat conduction through windows (
    merge_windows=False). In contrast to versions < 0.5 TEASER now does not
    support any other model options, as we observed no need, since single
    ThermalZones are identical with IBPSA models. If you miss one of the
    old options please contact us.

    This function uses Mako Templates specified in
    data.output.modelicatemplates.AixLib

    Parameters
    ----------

    buildings : list of instances of Building
        list of TEASER instances of a Building that is exported to a AixLib
        MultizoneEquipped models. If you want to export a single building,
        please pass it over as a list containing only that building.
    prj : instance of Project
        Instance of TEASER Project object to access Project related
        information, e.g. name or version of used libraries
    path : string
        if the Files should not be stored in default output path of TEASER,
        an alternative path can be specified as a full path
    use_postprocessing_calc : bool
        If activated the exported model will use the multizonePostProcessing
        to calculate common outputs for simulation time like total heating
        demands. Only supported for Aixlib. Default is False.
    export_vars : str
        Holds the string about which variables to export following the
        __Dymola_selection syntax.
    custom_multizone_template_path : str
        if a custom template for writing the multizone model should be used,
        its path can be specified as a full path

    Attributes
    ----------

    lookup : TemplateLookup object
        Instance of mako.TemplateLookup to store general functions for templates
    zone_template_1 : Template object
        Template for ThermalZoneRecord using 1 element model
    zone_template_2 : Template object
        Template for ThermalZoneRecord using 2 element model
    zone_template_3 : Template object
        Template for ThermalZoneRecord using 3 element model
    zone_template_4 : Template object
        Template for ThermalZoneRecord using 4 element model
    zone_template_5 : Template object
        Template for ThermalZoneRecord using 5 element model
    model_template : Template object
        Template for MultiZone model
    """

    if path is None:
        path = utilities.get_full_path("")

    lookup = TemplateLookup(directories=[utilities.get_full_path(
        os.path.join('data', 'output', 'modelicatemplate'))])
    zone_template_1 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib"
            "/AixLib_ThermalZoneRecord_OneElement"),
        lookup=lookup)
    zone_template_2 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib"
            "/AixLib_ThermalZoneRecord_TwoElement"),
        lookup=lookup)
    zone_template_3 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib"
            "/AixLib_ThermalZoneRecord_ThreeElement"),
        lookup=lookup)
    zone_template_4 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib"
            "/AixLib_ThermalZoneRecord_FourElement"),
        lookup=lookup)
    zone_template_5 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib"
            "/AixLib_ThermalZoneRecord_FiveElement"),
        lookup=lookup)
    if custom_multizone_template_path:
        model_template = Template(
            filename=custom_multizone_template_path,
            lookup=lookup)
    else:
        model_template = Template(
            filename=utilities.get_full_path(
                "data/output/modelicatemplate/AixLib/AixLib_Multizone"),
            lookup=lookup)
    test_script_template = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/modelica_test_script"),
        lookup=lookup)

    dir_resources = utilities.create_path(os.path.join(path, "Resources"))
    dir_scripts = utilities.create_path(os.path.join(dir_resources, "Scripts"))
    dir_dymola = utilities.create_path(os.path.join(dir_scripts, "Dymola"))

    uses = [
        'Modelica(version="' + prj.modelica_info.version + '")',
        'AixLib(version="' + prj.buildings[-1].library_attr.version + '")']
    modelica_output.create_package(
        path=path,
        name=prj.name,
        uses=uses)
    modelica_output.create_package_order(
        path=path,
        package_list=buildings,
        extra=None)
    if not prj.weather_file_path.startswith("modelica:"):
        modelica_output.copy_weather_data(prj.weather_file_path, path)
    if prj.t_soil_mode == 3:
        if not prj.t_soil_file_path.startswith("modelica:"):
            modelica_output.copy_weather_data(prj.t_soil_file_path, path)

    for i, bldg in enumerate(buildings):

        ass_error = "You chose IBPSA calculation, " \
                    "but want to export AixLib models, " \
                    "this is not possible"

        assert bldg.used_library_calc == 'AixLib', ass_error

        bldg_path = os.path.join(path, bldg.name)
        utilities.create_path(bldg_path)
        utilities.create_path(os.path.join(bldg_path, bldg.name + "_DataBase"))
        bldg.library_attr.modelica_set_temp(path=bldg_path)
        bldg.library_attr.modelica_set_temp_cool(path=bldg_path)
        bldg.library_attr.modelica_AHU_boundary(
            path=bldg_path)
        bldg.library_attr.modelica_gains_boundary(
            path=bldg_path)

        modelica_output.create_package(path=bldg_path, name=bldg.name, within=bldg.parent.name)
        modelica_output.create_package_order(
            path=bldg_path,
            package_list=[bldg],
            extra=[bldg.name + "_DataBase"])

        if bldg.building_id is None:
            bldg.building_id = i
        else:
            try:
                bldg.building_id = int(bldg.building_id)
            except UserWarning:
                warnings.warn("Cannot convert building_id to integer, "
                              "is set to ", i, "which is the enumeration "
                                               "number of the building in "
                                               "the project list.")
                bldg.building_id = i
        with open(os.path.join(bldg_path, bldg.name + ".mo"), 'w') as out_file:

            out_file.write(model_template.render_unicode(
                bldg=bldg,
                weather=bldg.parent.weather_file_path,
                modelica_info=bldg.parent.modelica_info,
                use_postprocessing_calc=use_postprocessing_calc,
                export_vars=export_vars))
            out_file.close()

        _help_test_script(bldg, dir_dymola, test_script_template)

        zone_path = os.path.join(bldg_path, bldg.name + "_DataBase")

        for zone in bldg.thermal_zones:

            with open(os.path.join(zone_path, bldg.name + '_' + zone.name + '.mo'),
                'w') as out_file:
                if type(zone.model_attr).__name__ == "OneElement":
                    out_file.write(zone_template_1.render_unicode(zone=zone))
                elif type(zone.model_attr).__name__ == "TwoElement":
                    out_file.write(zone_template_2.render_unicode(zone=zone))
                elif type(zone.model_attr).__name__ == "ThreeElement":
                    out_file.write(zone_template_3.render_unicode(zone=zone))
                elif type(zone.model_attr).__name__ == "FourElement":
                    out_file.write(zone_template_4.render_unicode(zone=zone))
                elif type(zone.model_attr).__name__ == "FiveElement":
                    out_file.write(zone_template_5.render_unicode(zone=zone))

                out_file.close()

        modelica_output.create_package(
            path=zone_path,
            name=bldg.name + '_DataBase',
            within=prj.name + '.' + bldg.name)
        modelica_output.create_package_order(
            path=zone_path,
            package_list=bldg.thermal_zones,
            addition=bldg.name + "_",
            extra=None)

    _copy_script_unit_tests(os.path.join(dir_scripts, "runUnitTests.py"))
    _copy_reference_results(dir_resources, prj)

    print("Exports can be found here:")
    print(path)


def _copy_reference_results(dir_resources, prj):
    """Copy reference results to modelica output.

    Parameters
    ----------
    dir_resources : str
        Resources directory of the modelica output
    prj : teaser.project.Project
        Project to be exported
    """

    if prj.dir_reference_results is not None:
        dir_ref_out = os.path.join(dir_resources, "ReferenceResults")
        if not os.path.exists(dir_ref_out):
            os.mkdir(dir_ref_out)
        dir_ref_out_dymola = os.path.join(dir_ref_out, "Dymola")
        if not os.path.exists(dir_ref_out_dymola):
            os.mkdir(dir_ref_out_dymola)
        for filename in os.listdir(prj.dir_reference_results):
            if filename.endswith(".txt"):
                shutil.copy2(
                    os.path.join(prj.dir_reference_results, filename),
                    os.path.join(dir_ref_out_dymola, filename)
                )


def _help_test_script(bldg, dir_dymola, test_script_template):
    """Create a test script for regression testing with BuildingsPy

    Parameters
    ----------
    bldg : teaser.logic.buildingobjects.building.Building
        Building for which test script is created
    dir_dymola : str
        Output directory for Dymola scripts
    test_script_template : mako.template.Template
        Template for the test script

    Returns
    -------
    dir_scripts : str
        Path to the scripts directory
    """

    dir_building = os.path.join(dir_dymola, bldg.name)
    if not os.path.exists(dir_building):
        os.mkdir(dir_building)
    with open(os.path.join(dir_building, bldg.name + ".mos"), 'w') as out_file:

        names_variables = []
        for i, zone in enumerate(bldg.thermal_zones):
            names_variables.append(f"multizone.PHeater[{i+1}]")
            names_variables.append(f"multizone.PCooler[{i+1}]")
            names_variables.append(f"multizone.TAir[{i+1}]")
        out_file.write(test_script_template.render_unicode(
            project=bldg.parent,
            bldg=bldg,
            stop_time=3600 * 24 * 365,
            names_variables=names_variables,
        ))
        out_file.close()


def _copy_script_unit_tests(destination_path):
    """Copies the script to run the unit tests.

    Parameters
    ----------
    destination_path : str
        path of where the weather file should be placed
    """

    source_path = utilities.get_full_path("data/output/runUnitTests.py")
    shutil.copy2(source_path, destination_path)
