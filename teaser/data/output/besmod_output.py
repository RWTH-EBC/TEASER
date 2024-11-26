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
    """
    Export building models for BESMod simulations.

    This function generates BESMod.Systems.Demand.Building.TEASERThermalZone models
    for one or more TEASER buildings. It also allows exporting examples from
    BESMod.Examples, including the building models.

    Parameters
    ----------
    buildings : list[Building] or Building
        TEASER Building instances to export as BESMod models. Can be a single
        Building or a list of Buildings.
    prj : Project
        TEASER Project instance containing project metadata such as library
        versions and weather file paths.
    path : str, optional
        Output directory path for the exported files. If not specified,
        the default output path in TEASER is used.
    examples : list[str], optional
        Names of BESMod examples to export alongside the building models.
    THydSup_nominal : float or dict, optional
        Nominal supply temperature(s) for the hydraulic system. Required for
        certain examples (e.g., HeatPumpMonoenergetic, GasBoilerBuildingOnly).
        See docstring of teaser.data.output.besmod_output.convert_input() for further information.
    QBuiOld_flow_design : dict, optional
        For partially retrofitted systems specify the old nominal heat flow
        of the Buildings in a dictionary with the building names as keys.
        By default, only the radiator transfer system is not retrofitted in BESMod.
    THydSupOld_design : float or dict, optional
        Design supply temperatures for old not retrofitted hydraulic systems.

    Raises
    ------
    ValueError
        If given example is not supported.
    ValueError
        If `THydSup_nominal` is not provided for examples requiring it.
    AssertionError
        If the used library for calculations is not AixLib.
    NotImplementedError
        If a building uses a thermal zone model other than the four-element model.

    Notes
    -----
    The function uses Mako templates for generating Modelica models.
    """

    if not isinstance(buildings, list):
        buildings = [buildings]

    if not isinstance(examples, list):
        examples = [examples]
    supported_examples = ["TEASERHeatLoadCalculation",
                          "HeatPumpMonoenergetic",
                          "GasBoilerBuildingOnly"]
    for exp in examples:
        if exp not in supported_examples:
            raise ValueError(f"Example {exp} is not supported. "
                             f"Supported examples are {supported_examples}.")

    if THydSup_nominal is None and any(
            example in examples for example in ["HeatPumpMonoenergetic", "GasBoilerBuildingOnly"]):
        raise ValueError("Examples 'HeatPumpMonoenergetic' and 'GasBoilerBuildingOnly' "
                         "require the `THydSup_nominal` parameter.")

    THydSup_nominal_bldg = convert_input(THydSup_nominal, buildings)
    THydSupOld_design_bldg = convert_input(THydSupOld_design, buildings) if THydSupOld_design else \
        {bldg.name: "systemParameters.THydSup_nominal" for bldg in buildings}

    if QBuiOld_flow_design is None:
        QBuiOld_flow_design = {bldg.name: "systemParameters.QBui_flow_nominal" for bldg in buildings}
    else:
        QBuiOld_flow_design = {bldg.name: _convert_to_zone_array(bldg, QBuiOld_flow_design[bldg.name]) for bldg in
                               buildings}

    dir_resources = utilities.create_path(os.path.join(path, "Resources"))
    dir_scripts = utilities.create_path(os.path.join(dir_resources, "Scripts"))
    dir_dymola = utilities.create_path(os.path.join(dir_scripts, "Dymola"))
    template_path = utilities.get_full_path("data/output/modelicatemplate")
    lookup = TemplateLookup(directories=[template_path])

    zone_template_4 = Template(
        filename=os.path.join(template_path, "AixLib/AixLib_ThermalZoneRecord_FourElement"),
        lookup=lookup)
    building_template = Template(
        filename=os.path.join(template_path, "BESMod/Building"),
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

        set_back_times = bldg.thermal_zones[0].use_conditions.set_back_times
        start_time_set_back = 0
        hours_set_back = 0
        if set_back_times:
            start_time_set_back = bldg.thermal_zones[0].use_conditions.set_back_times[1] * 3600
            hours_set_back = 24 - bldg.thermal_zones[0].use_conditions.set_back_times[1] + \
                             bldg.thermal_zones[0].use_conditions.set_back_times[0]

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
            out_file.write(building_template.render_unicode(
                bldg=bldg))
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
                    THydSupOld_design=THydSupOld_design_bldg[bldg.name],
                    startTimeSetBack=start_time_set_back,
                    hoursSetBack=hours_set_back))
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

    print("Exports can be found here:")
    print(path)


def convert_input(building_zones_input, buildings):
    """
    Convert input values for BESMod zone specific parameters to a dictionary.

    Supports single values, dictionaries keyed by construction year, or
    dictionaries keyed by building names.
    If single values are given then all buildings and zones get this values set.
    If a dictionary keyed by construction year is given then all zones of a building get the
    value set of the next higher year corresponding to the construction year of the building.
    If a dictionary keyed by building name is given the value must be a single value for all zones
    or another dictionary specifying for each zone name a value.

    Parameters
    ----------
    building_zones_input : float, int, or dict
        Input value(s) for BESMod parameters. Can be a single value, or a
        dictionary keyed by construction year, or building name.
    buildings : list[Building]
        List of TEASER Building instances.

    Returns
    -------
    dict
        Dictionary mapping building names to BESMod parameter input strings.

    Raises
    ------
    ValueError
        If the input dictionary has invalid values.
    KeyError
        If the input dictionary is missing required keys.
    """
    bldg_names = [bldg.name for bldg in buildings]
    if isinstance(building_zones_input, (float, int)):
        return {bldg.name: f"fill({building_zones_input},systemParameters.nZones)" for bldg in buildings}
    elif isinstance(building_zones_input, dict):
        t_hyd_sup_nominal_bldg = {}
        if isinstance(list(building_zones_input.keys())[0], int):
            for bldg in buildings:
                temperature = _get_next_higher_year_value(building_zones_input, bldg.year_of_construction)
                t_hyd_sup_nominal_bldg[bldg.name] = f"fill({temperature},systemParameters.nZones)"
        elif set(list(building_zones_input.keys())) == set(bldg_names):
            for bldg in buildings:
                if isinstance(building_zones_input[bldg.name], (int, float)):
                    t_hyd_sup_nominal_bldg[
                        bldg.name] = f"fill({building_zones_input[bldg.name]},systemParameters.nZones)"
                elif isinstance(building_zones_input[bldg.name], dict):
                    t_hyd_sup_nominal_bldg[bldg.name] = _convert_to_zone_array(bldg, building_zones_input[bldg.name])
                else:
                    raise ValueError("If THydSup_nominal is specified for all buildings in a dictionary "
                                     "the values must be either a single value for all thermal zones or "
                                     "a dict with all building.thermal_zones.name as keys.")
        else:
            raise KeyError("If THydSup_nominal is given by a dictionary "
                           "the keys must be all building names or construction years.")
        return t_hyd_sup_nominal_bldg


def _convert_to_zone_array(bldg, zone_dict):
    """
    Convert a dictionary of zone values to a BESMod-compatible array string.

    Parameters
    ----------
    bldg : Building
        TEASER Building instance.
    zone_dict : dict
        Dictionary with zone names as keys and zone parameter values as values.

    Returns
    -------
    str
        Array string for BESMod parameter input.

    Raises
    ------
    KeyError
        If the dictionary is missing zone names present in the building.
    """
    tz_names = [tz.name for tz in bldg.thermal_zones]
    if set(tz_names) == set(list(zone_dict.keys())):
        array_string = "{"
        for tz in tz_names:
            array_string += str(zone_dict[tz]) + ","
        return array_string[:-1] + "}"
    else:
        raise KeyError(f"{set(tz_names) - set(list(zone_dict.keys()))} thermal zones missing in given dictionary.")


def _get_next_higher_year_value(years_dict, given_year):
    """
        Get the next higher value for a given year from a dictionary.

        Parameters
        ----------
        years_dict : dict
            Dictionary with years as keys and corresponding values.
        given_year : int
            Year to find the next higher value for.

        Returns
        -------
        float or int
            Value corresponding to the next higher year. If no higher year is found,
            returns the value of the latest year.
        """
    years = sorted(years_dict.keys())
    for year in years:
        if year > given_year:
            return years_dict[year]
    return years_dict[years[-1]]


def _help_example_script(bldg, dir_dymola, test_script_template, example):
    """
    Create a .mos script for simulating and plotting BESMod examples from a Mako template.

    Parameters
    ----------
    bldg : Building
        TEASER Building instance for which the script is created.
    dir_dymola : str
        Output directory for Dymola scripts.
    test_script_template : Template
        Mako template for the simulation script.
    example : str
        Name of the BESMod example.
    """

    dir_building = utilities.create_path(os.path.join(dir_dymola, bldg.name))
    with open(os.path.join(dir_building, example + bldg.name + ".mos"), 'w') as out_file:
        out_file.write(test_script_template.render_unicode(
            project=bldg.parent,
            bldg=bldg
        ))
        out_file.close()
