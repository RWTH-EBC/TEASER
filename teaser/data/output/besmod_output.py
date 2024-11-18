"""This module contains function for BESMod model generation"""

import os
from mako.template import Template
from mako.lookup import TemplateLookup
import teaser.logic.utilities as utilities
import teaser.data.output.modelica_output as modelica_output


def export_besmod(
        buildings,
        prj,
        path=None,
        examples=None,
        THydSup_nominal=None,
        QBuiOld_flow_design=None,
        THydSupOld_design=None):
    """Exports buildings for BESMod simulation

    Exports one (if internal_id is not None) or all buildings as
    BESMod.Systems.Demand.Building.TEASERThermalZone models. Additionally,
    BESMod.Examples can be specified and directly exported including the building.

    This function uses Mako Templates specified in
    data.output.modelicatemplates.BESMod

    Parameters
    ----------

    buildings : list of Building instances
        list of TEASER Building instances that are exported to BESMod
        building TEASERThermalZone models. Additionally, the buildings are export
        into the BESMod examples specified in the parameter examples
    prj : instance of Project
        Instance of TEASER Project object to access Project related
        information, e.g. name or version of used libraries
    path : string
        if the Files should not be stored in default output path of TEASER,
        an alternative path can be specified as a full paths
    examples: [string]
        BESMod examples which are exported with the buildings

    Attributes
    ----------

    lookup : TemplateLookup object
        Instance of mako.TemplateLookup to store general functions for templates
    zone_template_4 : Template object
        Template for ThermalZoneRecord using 4 element model
    model_template : Template object
        Template for MultiZone model
    """

    if not isinstance(buildings, list):
        buildings = [buildings]

    if THydSup_nominal is None and ("HeatPumpMonoenergetic" or "GasBoilerBuildingOnly" in examples):
        raise ValueError("For the examples HeatPumpMonoenergetic and GasBoilerBuildingOnly "
                         "the parameter THydSup_nominal needs to be set.")
    # construct dict {bldg.name: THydSup_nominal_actual_value}
    THydSup_nominal_bldg = _convert_THydSup_nominl_input(THydSup_nominal, buildings)
    if THydSupOld_design is None:
        THydSupOld_design_bldg = {bldg.name: "systemParameters.THydSup_nominal" for bldg in buildings}
    else:
        THydSupOld_design_bldg = _convert_THydSup_nominl_input(THydSupOld_design, buildings)

    if QBuiOld_flow_design is None:
        QBuiOld_flow_design = {bldg.name: "systemParameters.QBui_flow_nominal" for bldg in buildings}
    else:
        QBuiOld_flow_design = {bldg.name: _convert_to_zone_array(bldg, QBuiOld_flow_design[bldg.name]) for bldg in buildings}

    supported_examples = ["TEASERHeatLoadCalculation",
                          "HeatPumpMonoenergetic",
                          "GasBoilerBuildingOnly"]

    dir_resources = utilities.create_path(os.path.join(path, "Resources"))
    dir_scripts = utilities.create_path(os.path.join(dir_resources, "Scripts"))
    dir_dymola = utilities.create_path(os.path.join(dir_scripts, "Dymola"))

    lookup = TemplateLookup(directories=[utilities.get_full_path(
        os.path.join('data', 'output', 'modelicatemplate'))])
    zone_template_4 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib"
            "/AixLib_ThermalZoneRecord_FourElement"),
        lookup=lookup)
    model_template = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/BESMod/Building"),
        lookup=lookup)

    uses = [
        'Modelica(version="' + prj.modelica_info.version + '")',
        'AixLib(version="' + prj.buildings[-1].library_attr.version + '")',
        'BESMod(version="0.5.0")']  # ToDo fwu-hst: BESMod version make attribute of AixLib?
    modelica_output.create_package(
        path=path,
        name=prj.name,
        uses=uses)
    modelica_output.create_package_order(
        path=path,
        package_list=buildings)
    modelica_output.copy_weather_data(prj.weather_file_path, dir_resources)

    for i, bldg in enumerate(buildings):
        bldg.bldg_height = bldg.number_of_floors * bldg.height_of_floors  # ToDo fwu-hst: better place? Create logic/calculation/besmod.py as for aixlib?

        ass_error = "BESMod export is only implemented for AixLib calculation."
        assert bldg.used_library_calc == 'AixLib', ass_error

        bldg_path = os.path.join(path, bldg.name)
        utilities.create_path(bldg_path)
        utilities.create_path(os.path.join(bldg_path, bldg.name + "_DataBase"))
        bldg.library_attr.modelica_gains_boundary(path=bldg_path)

        example_bldg = [exp + bldg.name for exp in examples]
        example_bldg.append(bldg.name + "_DataBase")

        modelica_output.create_package(path=bldg_path, name=bldg.name, within=bldg.parent.name)
        modelica_output.create_package_order(
            path=bldg_path,
            package_list=[bldg],
            extra=example_bldg)

        with open(utilities.get_full_path(
                os.path.join(bldg_path, bldg.name + ".mo")), 'w') as out_file:
            out_file.write(model_template.render_unicode(
                bldg=bldg,
                weather=bldg.parent.weather_file_path,
                modelica_info=bldg.parent.modelica_info))
            out_file.close()

        for exp in examples:
            example_template = Template(
                filename=utilities.get_full_path(
                    "data/output/modelicatemplate/BESMod/Example_" + exp),
                lookup=lookup)
            example_sim_plot_script = Template(
                filename=utilities.get_full_path(
                    "data/output/modelicatemplate/BESMod/Script_" + exp),
                lookup=lookup)

            with open(utilities.get_full_path(
                    os.path.join(bldg_path, exp + bldg.name + ".mo")), 'w') as out_file:
                out_file.write(example_template.render_unicode(
                    bldg=bldg,
                    project=prj,
                    TOda_nominal=bldg.thermal_zones[0].t_outside,
                    THydSup_nominal=THydSup_nominal_bldg[bldg.name],
                    QBuiOld_flow_design=QBuiOld_flow_design[bldg.name],
                    THydSupOld_design=THydSupOld_design_bldg[bldg.name]))
                out_file.close()

            _help_example_script(bldg, dir_dymola, example_sim_plot_script, exp)

        zone_path = os.path.join(bldg_path, bldg.name + "_DataBase")

        for zone in bldg.thermal_zones:
            zone.use_conditions.with_heating = False
            with open(utilities.get_full_path(os.path.join(
                    zone_path,
                    bldg.name + '_' + zone.name + '.mo')), 'w') as out_file:
                if type(zone.model_attr).__name__ == "OneElement":
                    raise NotImplementedError("BESMod export is only implemented for four elements.")
                elif type(zone.model_attr).__name__ == "TwoElement":
                    raise NotImplementedError("BESMod export is only implemented for four elements.")
                elif type(zone.model_attr).__name__ == "ThreeElement":
                    raise NotImplementedError("BESMod export is only implemented for four elements.")
                elif type(zone.model_attr).__name__ == "FourElement":
                    out_file.write(zone_template_4.render_unicode(zone=zone))

                out_file.close()

        modelica_output.create_package(
            path=zone_path,
            name=bldg.name + '_DataBase',
            within=prj.name + '.' + bldg.name)
        modelica_output.create_package_order(
            path=zone_path,
            package_list=bldg.thermal_zones,
            addition=bldg.name + "_")

    # _copy_script_unit_tests(os.path.join(dir_scripts, "runUnitTests.py"))
    # _copy_reference_results(dir_resources, prj)  # ToDo fwu-hst: Creat reference results for example models

    print("Exports can be found here:")
    print(path)


def _convert_THydSup_nominl_input(THydSup_nominal, buildings):
    bldg_names = [bldg.name for bldg in buildings]
    if isinstance(THydSup_nominal, (float, int)):
        return {bldg.name: f"fill({THydSup_nominal},systemParameters.nZones)" for bldg in buildings}
    elif isinstance(THydSup_nominal, dict):
        THydSup_nominal_bldg = {}
        if isinstance(list(THydSup_nominal.keys())[0], int):
            for bldg in buildings:
                temperature = _get_next_higher_year_value(THydSup_nominal, bldg.year_of_construction)
                THydSup_nominal_bldg[bldg.name] = f"fill({temperature},systemParameters.nZones)"
        elif set(list(THydSup_nominal.keys())) == set(bldg_names):
            for bldg in buildings:
                if isinstance(THydSup_nominal[bldg.name], (int, float)):
                    THydSup_nominal_bldg[bldg.name] = f"fill({THydSup_nominal[bldg.name]},systemParameters.nZones)"
                elif isinstance(THydSup_nominal[bldg.name], dict):
                    THydSup_nominal_bldg[bldg.name] = _convert_to_zone_array(bldg, THydSup_nominal[bldg.name])
                else:
                    raise ValueError("If THydSup_nominal is specified for all buildings in a dictionary "
                                     "the values must be either a single value for all thermal zones or "
                                     "a dict with all building.thermal_zones.name as keys.")
        else:
            raise ValueError("If THydSup_nominal is given by a dictionary "
                             "the keys must be all building names or construction years.")
        return THydSup_nominal_bldg


def _convert_to_zone_array(bldg, zone_dict):
    tz_names = [tz.name for tz in bldg.thermal_zones]
    if set(tz_names) == set(list(zone_dict.keys())):
        array_string = "{"
        for tz in tz_names:
            array_string += str(zone_dict[tz]) + ","
        return array_string[:-2] + "}"
    else:
        raise ValueError("Given thermal zones in dictionary are not matching.")


def _get_next_higher_year_value(years_dict, given_year):
    years = sorted(years_dict.keys())
    for year in years:
        if year > given_year:
            return years_dict[year]
    return years_dict[years[-1]]


def _help_example_script(bldg, dir_dymola, test_script_template, example):
    """Create a script for the simulation and basic plotting of the examples

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
    with open(utilities.get_full_path(os.path.join(
            dir_building, example + bldg.name + ".mos")), 'w') as out_file:
        out_file.write(test_script_template.render_unicode(
            project=bldg.parent,
            bldg=bldg
        ))
        out_file.close()
