"""This module contains function for BESMod model generation"""

import os
import shutil
import warnings
import numpy as np
from typing import Optional, Union, List, Dict
from mako.template import Template
from mako.lookup import TemplateLookup
import teaser.logic.utilities as utilities
import teaser.data.output.modelica_output as modelica_output
from teaser.logic.buildingobjects.building import Building
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor

# Emissivity of every wall record in AixLib's own OFD collections. TEASER's
# materials carry no emissivity of their own and would default to 0.9.
AIXLIB_WALL_EPS = 0.95

# AixLib's FLground_*_loHalf / _upHalf records cut the 0.25 m concrete slab of
# the ground plate into 0.15 m on the screed side and 0.10 m on the side of
# the outer insulation.
GROUND_PLATE_INNER_SLAB_FRACTION = 0.6


def export_besmod(
        buildings: Union[List[Building], Building],
        prj: 'Project',
        path: Optional[str] = None,
        examples: Optional[List[str]] = None,
        THydSup_nominal: Optional[Union[float, Dict[str, float]]] = None,
        QBuiOld_flow_design: Optional[Dict[str, Dict[str, float]]] = None,
        QRoomOld_flow_design: Optional[Dict[str, Dict[str, float]]] = None,
        THydSupOld_design: Optional[Union[float, Dict[str, float]]] = None,
        custom_examples: Optional[Dict[str, str]] = None,
        custom_script: Optional[Dict[str, str]] = None,
        export_with_hom: bool = True,
        heater_radiative_fraction: float = 0.35,
        rom_heating_curve_max_room: bool = True,
        export_with_spawn: bool = False,
        spawn_epw_path: Optional[str] = None,
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
    QRoomOld_flow_design : Optional[Dict[str, Dict[str, float]]]
        Room-wise equivalent of QBuiOld_flow_design, used by the HOM export
        (AixLibHighOrderSingleFamilyHouse) instead of QBuiOld_flow_design:
        a nested dictionary with the building names and, one level below,
        the room names (bldg.room_name_nr) as keys. Only needs entries for
        HOM buildings you want a custom value for - other buildings, and
        HOM buildings without an entry here, fall back to the same default
        as QBuiOld_flow_design.
    THydSupOld_design : Optional[Union[float, Dict[str, float]]]
        Design supply temperatures for old, non-retrofitted hydraulic systems.
    custom_examples: Optional[Dict[str, str]]
        Specify custom examples with a dictionary containing the example name as the key and
        the path to the corresponding custom mako template as the value.
    custom_script: Optional[Dict[str, str]]
        Specify custom .mos scripts for the existing and custom examples with a dictionary
        containing the example name as the key and the path to the corresponding custom mako template as the value.
    export_with_hom: bool
        Also exports the AixLib HOM of AixLibHighOrderSingleFamilyHouse
        buildings, next to their ROM.
    heater_radiative_fraction: float
        Radiative fraction of the ideal heater's heat flow in the
        TEASERHeatLoadCalculation example (BESMod's IdealHeaterFraRad), the
        rest is convective. Default is 0.35.
    rom_heating_curve_max_room: bool
        Evaluates the heating curve of the ROM exported next to the HOM at
        the set temperature of its warmest room, as the HOM's heating curve
        is, instead of at the zone's own set temperature (the rooms' set
        temperatures weighted by fac_room_t_set). Only the HeatPumpMonoenergetic
        and GasBoilerBuildingOnly examples have a heating curve. Default is
        True.
    export_with_spawn: bool
        Also exports AixLibHighOrderSingleFamilyHouse buildings as BESMod's
        SpawnHighOrder with the EnergyPlus model TEASER writes for them
        (energyplus_output.export_idf), in the TEASERHeatLoadCalculation and
        GasBoilerBuildingOnly examples with the suffix "_Spawn". The
        HeatPumpMonoenergetic example needs mechanical ventilation, which
        SpawnHighOrder does not have. Default is False.
    spawn_epw_path: str
        EnergyPlus weather file for the Spawn models, the same weather as
        the project's weather file. By default the project's weather file
        with the suffix .epw.

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

    if path is None:
        path = utilities.get_full_path("")

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
    elif THydSup_nominal is None:
        THydSup_nominal = 328.15
        if custom_examples:
            warnings.warn("If you set THydSup_nominal in your custom examples template, "
                          "please provide it in the export. "
                          "Otherwise, the default value of 328.15 K will be used.")

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

    if QRoomOld_flow_design is None:
        QRoomOld_flow_design = {
            bldg.name: "systemParameters.QBui_flow_nominal" for bldg in buildings
        }
    else:
        QRoomOld_flow_design = {
            bldg.name: (
                _convert_to_room_array(bldg, QRoomOld_flow_design[bldg.name])
                if bldg.name in QRoomOld_flow_design
                else "systemParameters.QBui_flow_nominal"
            )
            for bldg in buildings
        }

    if custom_script is None:
        custom_script = {}

    dir_resources = utilities.create_path(os.path.join(path, "Resources"))
    dir_scripts = utilities.create_path(os.path.join(dir_resources, "Scripts"))
    dir_dymola = utilities.create_path(os.path.join(dir_scripts, "Dymola"))
    template_path = utilities.get_full_path("data/output/modelicatemplate")
    lookup = TemplateLookup(directories=[template_path])

    building_template = Template(
        filename=os.path.join(template_path, "BESMod/Building"),
        lookup=lookup)

    building_hom_aixlib_template = Template(
        filename=os.path.join(template_path, "BESMod/Building_hom_aixlib_dim"),
        lookup=lookup)
    building_spawn_template = Template(
        filename=os.path.join(template_path, "BESMod/Building_spawn"),
        lookup=lookup)
    room_wise_profile_template = Template(
        filename=os.path.join(template_path, "BESMod/room_wise_profile_record"),
        lookup=lookup)
    single_wall_template = Template(
        filename=os.path.join(template_path, "BESMod/single_wall_record"),
        lookup=lookup)
    multi_inner_wall_template = Template(
        filename=os.path.join(template_path, "BESMod/multi_inner_wall_record"),
        lookup=lookup)
    window_simple_template = Template(
        filename=os.path.join(template_path, "BESMod/window_simple_record"),
        lookup=lookup)
    surface_orientation_template = Template(
        filename=os.path.join(template_path, "BESMod/surface_orientation_record"),
        lookup=lookup)
    wall_types = ['OW', 'roof', 'roof_attic', 'IW_vert_half', 'IW2_vert_half',
                  'IW_hori_upHalf', 'IW_hori_loHalf', 'ground_floor_loHalf',
                  'ground_floor_upHalf', 'IW_hori_att_upHalf', 'IW_hori_att_loHalf']

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
        # TEASERThermalSingleZone takes BuildingSingleZoneBaseRecord,
        # TEASERThermalZone AixLib's own ZoneBaseRecord (the BESMod/Building
        # template picks the model by the same property)
        if bldg.exports_single_zone_rom:
            zone_template_4 = Template(
                filename=os.path.join(template_path, "BESMod/BuildingSingleThermalZoneRecord_FourElement"),
                lookup=lookup)
        else:
            zone_template_4 = Template(
                filename=os.path.join(template_path, "AixLib/AixLib_ThermalZoneRecord_FourElement"),
                lookup=lookup)
        bldg.bldg_height = bldg.number_of_floors * bldg.height_of_floors
        start_time_zones = []
        hours_set_back_zones = []
        d_temp_set_back_zones = []
        t_set_zone_nominal = []
        for tz in bldg.thermal_zones:
            heating_profile = tz.use_conditions.heating_profile
            # _convert_heating_profile's own t_set_nominal (max of the
            # simulated setpoint schedule) is intentionally not used here:
            # the nominal/design temperature used for system sizing is a
            # separate concept from the simulated setpoint schedule, and
            # is tz.t_inside (settable independently, e.g. via a room-wise
            # aggregation for the AixLib HOM archetype - see
            # AixLibHighOrderSingleFamilyHouse.t_set_nominal_aggregation).
            # Only the setback *shape* (start/duration/depth) still comes
            # from the schedule itself.
            _, start_time, hours_set_back, d_temp_set_back = _convert_heating_profile(heating_profile)
            t_set_zone_nominal.append(tz.t_inside)
            d_temp_set_back_zones.append(d_temp_set_back)
            start_time_zones.append(start_time)
            hours_set_back_zones.append(hours_set_back)

        bldg_path = os.path.join(path, bldg.name)
        utilities.create_path(bldg_path)
        utilities.create_path(os.path.join(bldg_path, bldg.name + "_DataBase"))
        bldg.library_attr.modelica_gains_boundary(path=bldg_path)

        is_hom_archetype = type(bldg).__name__ == "AixLibHighOrderSingleFamilyHouse"
        export_hom = export_with_hom and is_hom_archetype
        export_spawn = export_with_spawn and is_hom_archetype
        hom_profiles = None
        if export_hom or export_spawn:
            hom_profiles = _write_hom_user_profiles(
                bldg=bldg,
                bldg_path=bldg_path,
                profile_template=room_wise_profile_template)
        if export_spawn:
            _write_spawn_building(bldg, bldg_path, dir_resources,
                                  building_spawn_template, spawn_epw_path)
            skipped = [exp for exp in examples if exp not in SPAWN_EXAMPLES]
            if skipped:
                warnings.warn(
                    f"{bldg.name} is exported as Spawn model only in "
                    f"{', '.join(SPAWN_EXAMPLES)}, not in {', '.join(skipped)}: "
                    f"SpawnHighOrder has no mechanical ventilation.")
        if export_hom:
            hom_template_kwargs = bldg.top_level_geo_params
            with open(os.path.join(bldg_path, bldg.name + "_HOM.mo"), 'w') as out_file:
                out_file.write(building_hom_aixlib_template.render_unicode(
                    bldg=bldg,
                    zone=bldg.thermal_zones[0],
                    fra_rad_int_gai=1 - hom_profiles["fac_conv"],
                    **hom_template_kwargs))
                out_file.close()

        with open(os.path.join(bldg_path, bldg.name + ".mo"), 'w') as out_file:
            out_file.write(building_template.render_unicode(
                bldg=bldg,
                export_hom=export_hom))
            out_file.close()

        def room_resolved_suffixes(example):
            suffixes = ["_HOM"] if export_hom else []
            if export_spawn and example in SPAWN_EXAMPLES:
                suffixes.append("_Spawn")
            return suffixes

        def write_example_mo(example_template, example, suffix=""):
            # the room resolved examples' templates name their building and
            # themselves with the suffix, "_HOM" or "_Spawn"
            with open(os.path.join(bldg_path, example + bldg.name + suffix + ".mo"),
                      'w') as model_file:
                model_file.write(example_template.render_unicode(
                    bldg=bldg,
                    project=prj,
                    # The ROM example templates branch on this to drive the
                    # single merged zone with the HOM's room-wise user
                    # profiles (BESMod's TEASERHOMtoROM, weighted by
                    # bldg.fac_room_t_set / fac_room_nat_vent) instead of
                    # the zone-wise ones, so the ROM and the HOM exported
                    # next to it see the same user behaviour.
                    export_hom=export_hom,
                    hom_profiles=hom_profiles,
                    heater_radiative_fraction=heater_radiative_fraction,
                    rom_heating_curve_max_room=rom_heating_curve_max_room,
                    TOda_nominal=bldg.thermal_zones[0].t_outside,
                    THydSup_nominal=t_hyd_sup_nominal_bldg[bldg.name],
                    TSetZone_nominal=t_set_zone_nominal,
                    QBuiOld_flow_design=QBuiOld_flow_design[bldg.name],
                    QRoomOld_flow_design=QRoomOld_flow_design[bldg.name],
                    THydSupOld_design=t_hyd_sup_old_design_bldg[bldg.name],
                    dTSetBack=d_temp_set_back_zones,
                    startTimeSetBack=start_time_zones,
                    hoursSetBack=hours_set_back_zones,
                    suffix=suffix))
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

            # The room resolved buildings take the "*HOM" template variant
            # (e.g. Example_TEASERHeatLoadCalculationHOM), written as
            # "{exp}{bldg.name}_HOM.mo" and "{exp}{bldg.name}_Spawn.mo"
            # alongside the ROM's "{exp}{bldg.name}.mo".
            for suffix in room_resolved_suffixes(exp):
                exp_hom_key = exp + "HOM"
                exp_hom_template = Template(
                    filename=utilities.get_full_path(
                        "data/output/modelicatemplate/BESMod/Example_" + exp_hom_key),
                    lookup=lookup)
                if exp_hom_key in custom_script.keys():
                    example_hom_sim_plot_script = Template(
                        filename=custom_script[exp_hom_key],
                        lookup=lookup)
                else:
                    example_hom_sim_plot_script = Template(
                        filename=utilities.get_full_path(
                            "data/output/modelicatemplate/BESMod/Script_" + exp_hom_key),
                        lookup=lookup)
                _help_example_script(bldg, dir_dymola, example_hom_sim_plot_script, exp, suffix=suffix)
                write_example_mo(exp_hom_template, exp, suffix=suffix)
        bldg_package = [exp + bldg.name for exp in examples]

        if export_hom:
            bldg_package.append(bldg.name + "_HOM")
            bldg_package.extend(exp + bldg.name + "_HOM" for exp in examples)
        if export_spawn:
            bldg_package.append(bldg.name + "_Spawn")
            bldg_package.extend(exp + bldg.name + "_Spawn" for exp in examples
                                if exp in SPAWN_EXAMPLES)

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
            with open(os.path.join(
                    zone_path,
                    bldg.name + '_' + zone.name + '.mo'), 'w') as out_file:
                if type(zone.model_attr).__name__ == "FourElement":
                    out_file.write(zone_template_4.render_unicode(zone=zone))
                else:
                    raise NotImplementedError("BESMod export is only implemented for four elements.")
                out_file.close()

        if export_hom:
            wall_path = os.path.join(zone_path, "Walls")
            utilities.create_path(wall_path)
            for wall_type in wall_types:
                write_wall_record(wall_path=wall_path,
                                  wall_type=wall_type,
                                  single_wall_template=single_wall_template,
                                  bldg=bldg)

            with open(os.path.join(
                    wall_path,
                    bldg.name + '_wallTypes.mo'), 'w') as out_file:
                out_file.write(multi_inner_wall_template.render_unicode(bldg=bldg))
                out_file.close()
            # Sourced from an actual (and, if applicable, retrofitted) zone
            # window rather than re-derived fresh from year_of_construction,
            # so retrofit is reflected here too. u_value is area-independent
            # (ua_value / area), so any window works regardless of its area.
            window = bldg.thermal_zones[0].windows[0]
            window.calc_ua_value()
            with open(os.path.join(
                    wall_path,
                    bldg.name + '_windowSimple.mo'), 'w') as out_file:
                out_file.write(window_simple_template.render_unicode(bldg=bldg,
                                                                     Uw=window.u_value,
                                                                     g=window.g_value,
                                                                     frame_fraction=window.frame_fraction))
                out_file.close()
            modelica_output.create_package(
                path=wall_path,
                name='Walls',
                within=prj.name + '.' + bldg.name + '.' + bldg.name + '_DataBase')
            modelica_output.create_package_order(
                path=wall_path,
                package_list=[],
                extra=[bldg.name + "_" + w for w in ['windowSimple', 'wallTypes'] + wall_types])

            # The HOM's Modelica geometry is fixed - its rooms always face
            # the North/East/South/West radiation ports of
            # AixLibHighOrderOFD - so the building's orientation (and any
            # rotate_building applied to it) reaches the HOM solely through
            # this record, which redirects those ports. It also carries the
            # archetype's own roof_tilt, which is
            # therefore not necessarily the 45 deg of AixLib's own
            # SurfaceOrientationData_N_E_S_W_RoofN_Roof_S.
            if bldg.rotation_pending_recalculation:
                warnings.warn(
                    f"{bldg.name} was rotated after its parameters were last "
                    "calculated, so the exported ROM zone record still holds "
                    "the orientations from before the rotation while the HOM's "
                    "SurfaceOrientation record holds the rotated ones. Call "
                    "calc_all_buildings() after rotate_building() to export "
                    "the two consistently.")
            surfaces = bldg.surface_orientations
            with open(os.path.join(
                    zone_path,
                    bldg.name + '_SurfaceOrientation.mo'), 'w') as out_file:
                out_file.write(surface_orientation_template.render_unicode(
                    bldg=bldg,
                    rotation=bldg.rotation,
                    names=[name for name, _, _ in surfaces],
                    azimut=[_to_aixlib_azimuth(orientation)
                            for _, orientation, _ in surfaces],
                    tilt=[tilt for _, _, tilt in surfaces]))
                out_file.close()
            extra_data_base_package = ["Walls",
                                       bldg.name + "_SurfaceOrientation",
                                       bldg.name + "_TSetProfile"]
        else:
            extra_data_base_package = None

        modelica_output.create_package(
            path=zone_path,
            name=bldg.name + '_DataBase',
            within=prj.name + '.' + bldg.name)
        modelica_output.create_package_order(
            path=zone_path,
            package_list=bldg.thermal_zones,
            addition=bldg.name + "_",
            extra=extra_data_base_package)

    print("Exports can be found here:")
    print(path)


def _to_aixlib_azimuth(orientation):
    """Convert a TEASER orientation into an AixLib surface azimuth

    Parameters
    ----------
    orientation : float
        orientation in TEASER's convention, i.e. degrees clockwise from
        North

    Returns
    -------
    float
        the same direction as the azimuth AixLib's SurfaceOrientation
        records are written in - 0 is South, East is negative, West is
        positive - normalized to (-180, 180]

    This is the degree-valued counterpart of the azmiut_conv Mako def the
    ROM templates use (conversion/azmiut_conv), which returns radians:
    SurfaceOrientationBaseDataDefinition declares both Azimut and Tilt in
    Modelica.Units.NonSI.Angle_deg.
    """
    azimuth = (orientation - 180.0) % 360.0
    return azimuth - 360.0 if azimuth > 180.0 else azimuth


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


def _convert_to_room_array(bldg, room_dict):
    """
    Convert a dictionary of room values to a BESMod-compatible array string,
    ordered by the building's room_name_nr (1..10) - the room-wise
    counterpart to _convert_to_zone_array, used for the HOM export.

    Parameters
    ----------
    bldg : AixLibHighOrderSingleFamilyHouse
        TEASER Building instance with a room_name_nr attribute.
    room_dict : dict
        Dictionary with room names as keys and room parameter values as
        values.

    Returns
    -------
    str
        Array string for BESMod parameter input.

    Raises
    ------
    KeyError
        If the dictionary is missing room names present in the building.
    """
    room_names = set(bldg.room_name_nr)
    if room_names == set(room_dict.keys()):
        ordered_values = bldg._order_by_room_nr(room_dict)
        return "{" + ",".join(str(value) for value in ordered_values) + "}"
    else:
        raise KeyError(f"{room_names - set(room_dict.keys())} rooms missing in given dictionary.")


def _convert_heating_profile(heating_profile):
    """
    Convert a 24-hour heating profile for BESMod export.

    This function analyzes a 24-hour heating profile to extract:
    - The nominal temperature.
    - Start time of setbacks (if any).
    - hours_set_back of setback intervals.
    - d_temp_set_back of the heating variation.

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
    hours_set_back : float
        hours of the setback interval in h.
    d_temp_set_back : float
        Absolute difference between the minimum and nominal temperatures.

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
    d_temp_set_back = abs(min(heating_profile) - t_set_zone_nominal)
    if change_count == 0:
        d_temp_set_back = 0
        start_time = 0
        hours_set_back = 0
    elif change_count == 1:
        if heating_profile[0] < heating_profile[-1]:
            start_time = 0
            hours_set_back = change_indexes[0]
        else:
            start_time = change_indexes[0] * 3600
            hours_set_back = (24 - change_indexes[0])
    elif change_count == 2:
        start_time = change_indexes[1] * 3600
        hours_set_back = (24 - change_indexes[1] + change_indexes[0])
    else:
        raise ValueError("You have more than two temperature intervals in the heating profile."
                         "BESMod can only handel one heating set back.")
    return t_set_zone_nominal, start_time, hours_set_back, d_temp_set_back


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


# The examples with a Spawn variant: SpawnHighOrder has no mechanical
# ventilation, which the HeatPumpMonoenergetic example uses
SPAWN_EXAMPLES = ("TEASERHeatLoadCalculation", "GasBoilerBuildingOnly")


def _attic_air_change_rate(bldg):
    """The attic's air change rate [1/h] the archetype takes"""
    from teaser.logic.archetypebuildings.aixlib_high_order.singlefamilyhouse         import _ATTIC_AIR_CHANGE_RATES
    if bldg.attic_air_change_rate is not None:
        return float(bldg.attic_air_change_rate)
    return _ATTIC_AIR_CHANGE_RATES[bldg.attic_infiltration_class]


def _write_spawn_building(bldg, bldg_path, dir_resources, template,
                          spawn_epw_path=None):
    """Writes the IDF and the SpawnHighOrder building of a HOM archetype

    The IDF goes next to the building model, the EnergyPlus weather file
    into the package's Resources, next to the project's weather file.
    """
    from teaser.data.output.energyplus_output import export_idf
    from teaser.logic.archetypebuildings.aixlib_high_order.geometry import (
        building_geometry)

    prj = bldg.parent
    if spawn_epw_path is None:
        spawn_epw_path = os.path.splitext(prj.weather_file_path)[0] + ".epw"
    if not os.path.isfile(spawn_epw_path):
        raise FileNotFoundError(
            f"The Spawn export needs an EnergyPlus weather file of the same "
            f"weather as {prj.weather_file_path}; give it as spawn_epw_path "
            f"(not found: {spawn_epw_path}).")
    shutil.copy(spawn_epw_path, dir_resources)

    idf_file = bldg.name + "_Spawn.idf"
    export_idf(bldg, os.path.join(bldg_path, idf_file))
    zones = building_geometry(bldg)
    rooms = sorted(bldg.room_name_nr, key=bldg.room_name_nr.get)
    unheated = list(bldg.unheated_room_envelope_elements)
    names = rooms + unheated
    volumes = [zones[name].volume for name in names]
    areas = [zones[name].floor_area for name in names]
    attic = unheated[0]
    roofs = sum(s.area for zone in zones.values() for s in zone.surfaces
                if s.kind == "Roof")
    with open(os.path.join(bldg_path, bldg.name + "_Spawn.mo"), "w") as out_file:
        out_file.write(template.render_unicode(
            bldg=bldg,
            idf_file=idf_file,
            epw_file=os.path.basename(spawn_epw_path),
            zone_names="{" + ", ".join(f'"{name}"' for name in names) + "}",
            volumes=volumes[:len(rooms)] + [volumes[-1]],
            areas=areas[:len(rooms)],
            heights=[v / a for v, a in zip(volumes, areas)][:len(rooms)],
            # as AixLibHighOrder takes them: all floor areas, both floors and
            # the attic's mean height, all roof areas
            a_bui=sum(areas),
            h_bui=2 * bldg.top_level_geo_params["height_of_floors"]
            + zones[attic].volume / zones[attic].floor_area,
            a_roo=roofs,
            vent_rate_attic=_attic_air_change_rate(bldg)))


def _help_example_script(bldg, dir_dymola, test_script_template, example, suffix=""):
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
    suffix : str
        Appended to the output filename after bldg.name, e.g. "_HOM".
    """

    dir_building = utilities.create_path(os.path.join(dir_dymola, bldg.name))
    with open(os.path.join(dir_building, example + bldg.name + suffix + ".mos"), 'w') as out_file:
        out_file.write(test_script_template.render_unicode(
            project=bldg.parent,
            bldg=bldg,
            suffix=suffix
        ))
        out_file.close()


def _write_hom_user_profiles(bldg, bldg_path, profile_template):
    """Writes the room-wise user profiles the HOM and the ROM exported next
    to it are both driven with

    The internal gains are the zone's use conditions, the same the ROM
    exported on its own takes - persons, machines and lighting per m2 times
    the rooms' floor area - spread over the rooms and the hours as
    room_internal_gains_profiles are: each day, those daily courses are
    scaled so that together they give the building that day's energy of the
    use conditions' schedules. The table has the time stamps TEASER's own
    internal gains file uses, one column per room, ordered by room_name_nr,
    and a last, empty one for the Attic, like BESMod's InternalGainsHOM.
    Persons, machines and lighting each have their own convective share;
    the HOM and the ROM take their gains as one signal, so they get the
    share of the three over the year.

    The set temperatures are room_t_set_nominal, following the zone's
    heating profile: each room is set back by as much as the profile is
    below its maximum.

    Parameters
    ----------
    bldg : AixLibHighOrderSingleFamilyHouse
        the building, with its parameters calculated
    bldg_path : str
        the building's package, which the gains file is written to; the
        set temperature record goes to its _DataBase package
    profile_template : Template
        BESMod/room_wise_profile_record

    Returns
    -------
    dict
        file_internal_gains (name of the gains file in the building's
        package), fac_conv (convective share of the gains) and t_set_profile
        (the set temperature record, as a Modelica class path)
    """
    zone = bldg.thermal_zones[0]
    use_cond = zone.use_conditions
    rooms = sorted(bldg.room_name_nr, key=bldg.room_name_nr.get)
    floor_areas = np.array([bldg.detailed_geo[room]["floor"]["area"] for room in rooms])

    # W/m2 and convective share of each gain, by its schedule
    gains = {
        "persons_profile": (use_cond.persons * use_cond.fixed_heat_flow_rate_persons
                            * use_cond.activity_degree_persons,
                            use_cond.ratio_conv_rad_persons),
        "machines_profile": (use_cond.machines, use_cond.ratio_conv_rad_machines),
        "lighting_profile": (use_cond.lighting_power, use_cond.ratio_conv_rad_lighting),
    }
    specific = sum(np.asarray(use_cond.schedules[profile], dtype=float) * value
                   for profile, (value, _) in gains.items())
    energy = {profile: np.asarray(use_cond.schedules[profile], dtype=float).sum() * value
              for profile, (value, _) in gains.items()}
    total = sum(energy.values())
    fac_conv = (sum(energy[profile] * ratio for profile, (_, ratio) in gains.items()) / total
                if total > 0 else 1.0)

    # the rooms' daily courses, scaled to each day's energy of the building
    shape = np.array([bldg.room_internal_gains_profiles[room] for room in rooms],
                     dtype=float)
    if shape.shape != (len(rooms), 24) or shape.sum() <= 0:
        raise ValueError(
            f"room_internal_gains_profiles of {bldg.name} need 24 hourly values "
            f"for each of its rooms, and some gains.")
    daily_energy = (specific.reshape(-1, 24) * floor_areas.sum()).sum(axis=1)
    room_gains = np.concatenate(
        [shape * energy / shape.sum() for energy in daily_energy], axis=1)

    file_internal_gains = "InternalGains_" + bldg.name + "_HOM.txt"
    with open(os.path.join(bldg_path, file_internal_gains), "w") as out_file:
        out_file.write("#1\n")
        out_file.write(f"double Internals({room_gains.shape[1]}, {len(rooms) + 2})\n")
        for hour in range(room_gains.shape[1]):
            row = [(hour + 1) * 3600] + list(room_gains[:, hour]) + [0.0]
            out_file.write("\t".join(str(float(x)) for x in row) + "\n")

    heating_profile = np.asarray(use_cond.heating_profile, dtype=float)
    set_back = heating_profile - heating_profile.max()
    t_set_nominal = np.array([bldg.room_t_set_nominal[room] for room in rooms])
    rows = [[hour * 3600] + list(t_set_nominal + set_back[hour])
            for hour in range(len(heating_profile))]
    rows.append([len(heating_profile) * 3600] + rows[-1][1:])
    database_path = os.path.join(bldg_path, bldg.name + "_DataBase")
    with open(os.path.join(database_path, bldg.name + "_TSetProfile.mo"), "w") as out_file:
        out_file.write(profile_template.render_unicode(
            bldg=bldg,
            name="TSetProfile",
            description="Room-wise set temperatures, room_t_set_nominal "
                        "following the heating profile of the zone",
            rows=[[float(value) for value in row] for row in rows]))

    return {
        "file_internal_gains": file_internal_gains,
        "fac_conv": float(fac_conv),
        "t_set_profile": f"{bldg.parent.name}.{bldg.name}.{bldg.name}_DataBase."
                         f"{bldg.name}_TSetProfile",
    }


def _find_wall_type_element(elements, element_construction_type=None):
    """Find the first element matching element_construction_type.

    Used by write_wall_record to source the generic material/layer stack
    for a HOM wall-type record from an actual (already generated and, if
    applicable, retrofitted) zone element, instead of re-deriving a fresh
    element straight from year/construction. This keeps the exported HOM
    wall types consistent with whatever retrofit was actually applied to
    the zone, rather than always reflecting the original construction.

    Relies on the genuine per-room elements (element_construction_type is
    None or "LoadBearing") being added to the zone before the unheated-room
    equivalent-resistance elements in
    AixLibHighOrderSingleFamilyHouse.generate_archetype, so the first match
    (in insertion order) is always a genuine element and never one of the
    equivalent ones (which are currently left untagged, also None).
    """
    for element in elements:
        if element.element_construction_type == element_construction_type:
            return element
    raise ValueError(
        "No element with element_construction_type="
        f"{element_construction_type!r} found for HOM wall-type export."
    )


def _merge_equal_layers(layers):
    """Merge neighbouring (thickness, material) layers of the same material

    AixLib's records hold e.g. the gypsum plaster and gypsum board of the
    light inner walls as one 0.0275 m layer, which TEASER's elements keep
    as two layers of the same material.
    """
    merged = []
    for thickness, material in layers:
        if merged and all(
                getattr(merged[-1][1], attr) == getattr(material, attr)
                for attr in ("density", "thermal_conduc", "heat_capac")):
            merged[-1] = (merged[-1][0] + thickness, merged[-1][1])
        else:
            merged.append((thickness, material))
    return merged


def _vertical_half(layers):
    """Room side half of a symmetric inner wall, cut in its middle layer"""
    quotient, remainder = divmod(len(layers), 2)
    half = [(layer.thickness, layer.material) for layer in layers[:quotient]]
    if remainder:
        middle = layers[quotient]
        half.append((middle.thickness / 2, middle.material))
    return _merge_equal_layers(list(reversed(half)))


def _horizontal_half(bldg, element_class, construction_type):
    """Heated room's half of a horizontal inner element in AixLib's order

    For aixlib_* construction data, TypeElements_AixLib.json holds the halves
    themselves (CeilingHalf/FloorHalf between two heated rooms,
    CeilingAttic/FloorAttic towards the Attic), converted from AixLib's own
    CE*_loHalf / FL*_upHalf records, so each is exported with all of its
    layers. Other construction data only has the whole construction under
    Ceiling/Floor, which is cut in two instead: the ceiling's half keeps its
    innermost layer, the floor's all but its outermost.
    """
    element = element_class(parent=None)
    element.element_construction_type = construction_type
    type_element_key = element.load_type_element(
        year=bldg.year_of_construction,
        construction=bldg.construction_data.value,
        data_class=bldg.data_class,
    )
    layers = element.layer
    pre_split = type_element_key is not None and type_element_key.startswith(
        element_class.__name__ + construction_type)
    if not pre_split:
        layers = layers[:1] if element_class is Ceiling else layers[:-1]
    return [(layer.thickness, layer.material) for layer in reversed(layers)]


def _ground_plate_half(layers, upper):
    """One half of the ground plate, cut in its heaviest layer

    groundPlate_low_half runs from that cut to the room side (screed last),
    groundPlate_upp_half from the cut to the outside, as in AixLib's
    FLground_*_loHalf / _upHalf records.
    """
    slab = max(range(len(layers)),
               key=lambda i: layers[i].thickness * layers[i].material.density)
    inner = GROUND_PLATE_INNER_SLAB_FRACTION * layers[slab].thickness
    if upper:
        return [(layers[slab].thickness - inner, layers[slab].material)] + [
            (layer.thickness, layer.material) for layer in layers[slab + 1:]]
    return [(inner, layers[slab].material)] + [
        (layer.thickness, layer.material) for layer in reversed(layers[:slab])]


def write_wall_record(wall_path, wall_type, single_wall_template, bldg):
    """Writes the AixLib wall record of one HOM wall type

    The layers are taken from the building's (possibly retrofitted) zone
    elements where the HOM has an equivalent, and are written in AixLib's
    order, i.e. with wall[1] as the outside layer.
    """
    zone = bldg.thermal_zones[0]
    if wall_type == 'OW':
        element = _find_wall_type_element(zone.outer_walls)
    elif wall_type == 'roof':
        element = _find_wall_type_element(zone.rooftops)
    elif wall_type == 'roof_attic':
        # The attic's own envelope is not part of the (merged) zone - only
        # its equivalent-resistance stand-ins are (see
        # AixLibHighOrderSingleFamilyHouse.generate_archetype) - but is kept
        # as a persistent, retrofittable element on the building itself
        # (unheated_room_envelope_elements), so this reflects retrofit too.
        element = bldg.unheated_room_envelope_elements["Attic"]["roof1"]
    if wall_type in ('OW', 'roof', 'roof_attic'):
        layers = [(layer.thickness, layer.material) for layer in reversed(element.layer)]
    elif wall_type == 'IW_vert_half':
        layers = _vertical_half(_find_wall_type_element(zone.inner_walls).layer)
    elif wall_type == 'IW2_vert_half':
        layers = _vertical_half(
            _find_wall_type_element(zone.inner_walls, "LoadBearing").layer)
    elif wall_type in ('ground_floor_upHalf', 'ground_floor_loHalf'):
        layers = _ground_plate_half(
            _find_wall_type_element(zone.ground_floors).layer,
            upper=wall_type == 'ground_floor_upHalf')
    elif wall_type == 'IW_hori_loHalf':
        layers = _horizontal_half(bldg, Ceiling, "Half")
    elif wall_type == 'IW_hori_upHalf':
        layers = _horizontal_half(bldg, Floor, "Half")
    elif wall_type == 'IW_hori_att_loHalf':
        layers = _horizontal_half(bldg, Ceiling, "Attic")
    elif wall_type == 'IW_hori_att_upHalf':
        layers = _horizontal_half(bldg, Floor, "Attic")
    else:
        raise NotImplementedError("This wall type does not exit")
    if not layers:
        # Guard against silently writing a record with n=0 (which does not
        # translate in Modelica)
        raise ValueError(
            f"No layers selected for wall type {wall_type!r} of building "
            f"{bldg.name!r}.")
    if bldg.construction_data.value.startswith("aixlib"):
        eps = AIXLIB_WALL_EPS
    else:
        eps = layers[-1][1].ir_emissivity
    with open(os.path.join(
            wall_path,
            bldg.name + '_' + wall_type + '.mo'), 'w') as out_file:
        out_file.write(single_wall_template.render_unicode(
            bldg=bldg, wall_type=wall_type,
            d=[thickness for thickness, _ in layers],
            rho=[material.density for _, material in layers],
            conductivity=[material.thermal_conduc for _, material in layers],
            c=[material.heat_capac * 1000 for _, material in layers],  # kJ/kgK to J/kgK
            eps=eps,
            n=len(layers)))
