"""This module contains function for BESMod model generation"""

import os
from typing import Optional, Union, List, Dict
from mako.template import Template
from mako.lookup import TemplateLookup
import teaser.logic.utilities as utilities
import teaser.data.output.modelica_output as modelica_output
from teaser.logic.buildingobjects.building import Building


def export_besmod(
        buildings: Union[List[Building], Building],
        prj: 'Project',
        path: Optional[str] = None,
        examples: Optional[List[str]] = None,
        THydSup_nominal: Optional[Union[float, Dict[str, float]]] = None,
        QBuiOld_flow_design: Optional[Dict[str, Dict[str, float]]] = None,
        THydSupOld_design: Optional[Union[float, Dict[str, float]]] = None,
        custom_examples: Optional[Dict[str, str]] = None,
        custom_script: Optional[Dict[str, str]] = None
) -> None:
    """
    Export building models for BESMod simulations.

    This function generates BESMod.Systems.Demand.Building.TEASERThermalZone models
    for one or more TEASER buildings. It also allows exporting examples from
    BESMod.Examples, including the building models.

    Parameters
    ----------
    buildings : Union[List[Building], Building]
        TEASER Building instances to export as BESMod models. Can be a single
        Building or a list of Buildings.
    prj : Project
        TEASER Project instance containing project metadata such as library
        versions and weather file paths.
    examples : Optional[List[str]]
        Names of BESMod examples to export alongside the building models.
        Supported Examples: "TEASERHeatLoadCalculation", "HeatPumpMonoenergetic", and "GasBoilerBuildingOnly".
    path : Optional[str]
        Alternative output path for storing the exported files. If None, the default TEASER output path is used.
    THydSup_nominal : Optional[Union[float, Dict[str, float]]]
        Nominal supply temperature(s) for the hydraulic system. Required for
        certain examples (e.g., HeatPumpMonoenergetic, GasBoilerBuildingOnly).
        See docstring of teaser.data.output.besmod_output.convert_input() for further information.
    QBuiOld_flow_design : Optional[Dict[str, Dict[str, float]]]
        For partially retrofitted systems specify the old nominal heat flow
        of all zones in the Buildings in a nested dictionary with
        the building names and in a level below the zone names as keys.
        By default, only the radiator transfer system is not retrofitted in BESMod.
    THydSupOld_design : Optional[Union[float, Dict[str, float]]]
        Design supply temperatures for old, non-retrofitted hydraulic systems.
    custom_examples: Optional[Dict[str, str]]
        Specify custom examples with a dictionary containing the example name as the key and
        the path to the corresponding custom mako template as the value.
    custom_script: Optional[Dict[str, str]]
        Specify custom .mos scripts for the existing and custom examples with a dictionary
        containing the example name as the key and the path to the corresponding custom mako template as the value.

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

    if prj.used_library_calc != "AixLib":
        raise AttributeError("BESMod export is only implemented for AixLib calculation.")

    if examples is None:
        examples = []

    if not isinstance(examples, list):
        examples = [examples]

    supported_examples = [
        "TEASERHeatLoadCalculation",
        "HeatPumpMonoenergetic",
        "GasBoilerBuildingOnly",
    ]

    for exp in examples:
        if exp not in supported_examples:
            raise ValueError(
                f"Example {exp} is not supported. "
                f"Supported examples are {supported_examples}."
            )

    if THydSup_nominal is None and any(
            example in examples for example in ["HeatPumpMonoenergetic", "GasBoilerBuildingOnly"]
    ):
        raise ValueError(
            "Examples 'HeatPumpMonoenergetic' and 'GasBoilerBuildingOnly' "
            "require the `THydSup_nominal` parameter."
        )

    t_hyd_sup_nominal_bldg = convert_input(THydSup_nominal, buildings)
    t_hyd_sup_old_design_bldg = (
        convert_input(THydSupOld_design, buildings)
        if THydSupOld_design
        else {bldg.name: "systemParameters.THydSup_nominal" for bldg in buildings}
    )

    if QBuiOld_flow_design is None:
        QBuiOld_flow_design = {
            bldg.name: "systemParameters.QBui_flow_nominal" for bldg in buildings
        }
    else:
        QBuiOld_flow_design = {
            bldg.name: _convert_to_zone_array(bldg, QBuiOld_flow_design[bldg.name])
            for bldg in buildings
        }

    if custom_script is None:
        custom_script = {}

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
        'BESMod(version="' + prj.buildings[-1].library_attr.besmod_version + '")']
    modelica_output.create_package(
        path=path,
        name=prj.name,
        uses=uses)
    modelica_output.create_package_order(
        path=path,
        package_list=buildings)
    modelica_output.copy_weather_data(prj.weather_file_path, dir_resources)

    for i, bldg in enumerate(buildings):
        bldg.bldg_height = bldg.number_of_floors * bldg.height_of_floors
        start_time_zones = []
        width_zones = []
        amplitude_zones = []
        t_set_zone_nominal = []
        for tz in bldg.thermal_zones:
            heating_profile = tz.use_conditions.heating_profile
            t_set_nominal, start_time, width, amplitude = _convert_heating_profile(heating_profile)
            t_set_zone_nominal.append(t_set_nominal)
            amplitude_zones.append(amplitude)
            start_time_zones.append(start_time)
            width_zones.append(width)

        bldg_path = os.path.join(path, bldg.name)
        utilities.create_path(bldg_path)
        utilities.create_path(os.path.join(bldg_path, bldg.name + "_DataBase"))
        bldg.library_attr.modelica_gains_boundary(path=bldg_path)

        with open(utilities.get_full_path(
                os.path.join(bldg_path, bldg.name + ".mo")), 'w') as out_file:
            out_file.write(building_template.render_unicode(
                bldg=bldg))
            out_file.close()

        def write_example_mo(example_template, example):
            with open(utilities.get_full_path(
                    os.path.join(bldg_path, example + bldg.name + ".mo")), 'w') as model_file:
                model_file.write(example_template.render_unicode(
                    bldg=bldg,
                    project=prj,
                    TOda_nominal=bldg.thermal_zones[0].t_outside,
                    THydSup_nominal=t_hyd_sup_nominal_bldg[bldg.name],
                    TSetZone_nominal=t_set_zone_nominal,
                    QBuiOld_flow_design=QBuiOld_flow_design[bldg.name],
                    THydSupOld_design=t_hyd_sup_old_design_bldg[bldg.name],
                    setBakTSetZone_amplitude=amplitude_zones,
                    setBakTSetZone_startTime=start_time_zones,
                    setBakTSetZone_width=width_zones))
                model_file.close()

        for exp in examples:
            exp_template = Template(
                filename=utilities.get_full_path(
                    "data/output/modelicatemplate/BESMod/Example_" + exp),
                lookup=lookup)
            if exp in custom_script.keys():
                example_sim_plot_script = Template(
                    filename=custom_script[exp],
                    lookup=lookup)
            else:
                example_sim_plot_script = Template(
                    filename=utilities.get_full_path(
                        "data/output/modelicatemplate/BESMod/Script_" + exp),
                    lookup=lookup)
            _help_example_script(bldg, dir_dymola, example_sim_plot_script, exp)
            write_example_mo(exp_template, exp)
        bldg_package = [exp + bldg.name for exp in examples]
        if custom_examples:
            for exp, c_path in custom_examples.items():
                bldg_package.append(exp + bldg.name)
                exp_template = Template(
                    filename=c_path,
                    lookup=lookup)
                write_example_mo(exp_template, exp)
                if exp in custom_script.keys():
                    example_sim_plot_script = Template(
                        filename=custom_script[exp],
                        lookup=lookup)
                    _help_example_script(bldg, dir_dymola, example_sim_plot_script, exp)

        bldg_package.append(bldg.name + "_DataBase")
        modelica_output.create_package(path=bldg_path, name=bldg.name, within=bldg.parent.name)
        modelica_output.create_package_order(
            path=bldg_path,
            package_list=[bldg],
            extra=bldg_package)

        zone_path = os.path.join(bldg_path, bldg.name + "_DataBase")

        for zone in bldg.thermal_zones:
            zone.use_conditions.with_heating = False
            with open(utilities.get_full_path(os.path.join(
                    zone_path,
                    bldg.name + '_' + zone.name + '.mo')), 'w') as out_file:
                if type(zone.model_attr).__name__ == "FourElement":
                    out_file.write(zone_template_4.render_unicode(zone=zone))
                else:
                    raise NotImplementedError("BESMod export is only implemented for four elements.")
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


def convert_input(building_zones_input: Union[float, Dict[Union[int, str], Union[float, Dict[str, float]]]],
                  buildings: List[Building]) -> Dict[str, str]:
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
    building_zones_input : Union[float, Dict[Union[int, str], Union[float, Dict[str, float]]]]
        Input value(s) for BESMod parameters. Can be a single value, a dictionary keyed by construction year,
        or a dictionary keyed by building name.
        Example:
        - Single value: 328.15
        - Dictionary keyed by construction year: {1970: 348.15, 1990: 328.15}
        - Dictionary keyed by building name: {
            "Building1": 328.15,
            "Building2": {
                "Zone1": 328.15,
                "Zone2": 308.15
            }
        }
    buildings : List[Building]
        List of TEASER Building instances.

    Returns
    -------
    Dict[str, str]
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


def _convert_heating_profile(heating_profile):
    """
    Convert a 24-hour heating profile for BESMod export.

    This function analyzes a 24-hour heating profile to extract:
    - The nominal temperature.
    - Start time of setbacks (if any).
    - Width of setback intervals.
    - Amplitude of the heating variation.

    Parameters
    ----------
    heating_profile : list[float]
        List of 24 hourly heating temperatures.

    Returns
    -------
    t_set_zone_nominal : float
        Maximum temperature in the profile, used as the nominal set point.
    start_time : int
        Start time of the setback interval in seconds.
    width : float
        Width of the setback interval as a percentage of the day.
    amplitude : float
        Difference between the minimum and nominal temperatures.

    Raises
    ------
    ValueError
        If the profile has more than two distinct intervals or does not have 24 values.
    """

    if len(heating_profile) != 24:
        raise ValueError("Only 24 hours heating profiles can be used for BESMod export.")
    change_count = 0
    change_indexes = []
    for i in range(1, len(heating_profile)):
        if heating_profile[i] != heating_profile[i - 1]:
            change_count += 1
            change_indexes.append(i)
    t_set_zone_nominal = max(heating_profile)
    amplitude = min(heating_profile) - t_set_zone_nominal
    if change_count == 0:
        amplitude = 0
        start_time = 0
        width = 1e-50
    elif change_count == 1:
        if heating_profile[0] < heating_profile[-1]:
            start_time = 0
            width = 100 * change_indexes[0] / 24
        else:
            start_time = change_indexes[0] * 3600
            width = 100 * (24 - change_indexes[0]) / 24
    elif change_count == 2:
        start_time = change_indexes[1] * 3600
        width = 100 * (24 - change_indexes[1] + change_indexes[0]) / 24
    else:
        raise ValueError("You have more than two temperature intervals in the heating profile."
                         "BESMod can only handel one heating set back.")
    return t_set_zone_nominal, start_time, width, amplitude


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
