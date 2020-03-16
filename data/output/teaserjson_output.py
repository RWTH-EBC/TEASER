"""Saves alls Project data into a json."""

import json
import collections


def save_teaser_json(path, project):
    """Save a project to a JSON file.

    The function needs to be written.

    Parameters
    ----------
    path: string
        complete path to the output file
    project: Project()
        Teaser instance of Project()

    """
    if path.endswith("json"):
        path = path
    else:
        path = path + ".json"

    prj_out = collections.OrderedDict()
    prj_out["project"] = collections.OrderedDict()
    prj_out["project"]["version"] = "0.7"
    prj_out["project"]["name"] = project.name
    prj_out["project"]["weather_file_path"] = project.weather_file_path
    prj_out["project"]["number_of_elements_calc"] = project.number_of_elements_calc
    prj_out["project"]["merge_windows_calc"] = project.merge_windows_calc
    prj_out["project"]["used_library_calc"] = project.used_library_calc
    prj_out["project"]["modelica_info"] = collections.OrderedDict()
    prj_out["project"]["modelica_info"]["start_time"] = project.modelica_info.start_time
    prj_out["project"]["modelica_info"]["stop_time"] = project.modelica_info.stop_time
    prj_out["project"]["modelica_info"][
        "interval_output"
    ] = project.modelica_info.interval_output
    prj_out["project"]["modelica_info"][
        "current_solver"
    ] = project.modelica_info.current_solver
    prj_out["project"]["modelica_info"][
        "equidistant_output"
    ] = project.modelica_info.equidistant_output
    prj_out["project"]["modelica_info"][
        "results_at_events"
    ] = project.modelica_info.results_at_events
    prj_out["project"]["modelica_info"]["version"] = project.modelica_info.version
    prj_out["project"]["buildings"] = collections.OrderedDict()
    __building_class = {
        "Building": {"method": "undefined", "usage": "undefined"},
        "Office": {"method": "bmvbs", "usage": "office"},
        "Institute": {"method": "bmvbs", "usage": "institute"},
        "Institute4": {"method": "bmvbs", "usage": "institute4"},
        "Institute8": {"method": "bmvbs", "usage": "institute8"},
        "SingleFamilyDwelling": {"method": "iwu", "usage": "single_family_dwelling"},
        "SingleFamilyHouse": {"method": "tabula_de", "usage": "single_family_house"},
        "TerracedHouse": {"method": "tabula_de", "usage": "terraced_house"},
        "MultiFamilyHouse": {"method": "tabula_de", "usage": "multi_family_house"},
        "ApartmentBlock": {"method": "tabula_de", "usage": "apartment_block"},
    }

    for bldg in project.buildings:
        prj_out["project"]["buildings"][bldg.name] = collections.OrderedDict()
        prj_out["project"]["buildings"][bldg.name][
            "classification"
        ] = collections.OrderedDict()
        prj_out["project"]["buildings"][bldg.name]["classification"]["class"] = type(
            bldg
        ).__name__
        prj_out["project"]["buildings"][bldg.name]["classification"][
            "method"
        ] = __building_class[type(bldg).__name__]["method"]
        prj_out["project"]["buildings"][bldg.name]["street_name"] = bldg.street_name
        prj_out["project"]["buildings"][bldg.name]["city"] = bldg.city
        prj_out["project"]["buildings"][bldg.name][
            "year_of_construction"
        ] = bldg.year_of_construction
        prj_out["project"]["buildings"][bldg.name][
            "year_of_retrofit"
        ] = bldg.year_of_retrofit
        prj_out["project"]["buildings"][bldg.name][
            "number_of_floors"
        ] = bldg.number_of_floors
        prj_out["project"]["buildings"][bldg.name][
            "height_of_floors"
        ] = bldg.height_of_floors
        prj_out["project"]["buildings"][bldg.name][
            "net_leased_area"
        ] = bldg.net_leased_area
        prj_out["project"]["buildings"][bldg.name]["outer_area"] = bldg.outer_area
        prj_out["project"]["buildings"][bldg.name]["window_area"] = bldg.window_area
        if bldg.central_ahu is not None:
            ahu_out = collections.OrderedDict()
            ahu_out["heating"] = bldg.central_ahu.heating
            ahu_out["cooling"] = bldg.central_ahu.cooling
            ahu_out["dehumidification"] = bldg.central_ahu.dehumidification
            ahu_out["humidification"] = bldg.central_ahu.humidification
            ahu_out["heat_recovery"] = bldg.central_ahu.heat_recovery
            ahu_out[
                "by_pass_dehumidification"
            ] = bldg.central_ahu.by_pass_dehumidification
            ahu_out["efficiency_recovery"] = bldg.central_ahu.efficiency_recovery
            ahu_out[
                "efficiency_recovery_false"
            ] = bldg.central_ahu.efficiency_recovery_false
            ahu_out[
                "min_relative_humidity_profile"
            ] = bldg.central_ahu.min_relative_humidity_profile
            ahu_out[
                "max_relative_humidity_profile"
            ] = bldg.central_ahu.max_relative_humidity_profile
            ahu_out["v_flow_profile"] = bldg.central_ahu.v_flow_profile
            ahu_out["temperature_profile"] = bldg.central_ahu.temperature_profile
            prj_out["project"]["buildings"][bldg.name]["central_ahu"] = ahu_out
        else:
            pass
        prj_out["project"]["buildings"][bldg.name][
            "thermal_zones"
        ] = collections.OrderedDict()
        for zone in bldg.thermal_zones:

            zone_out = collections.OrderedDict()

            zone_out["area"] = zone.area
            zone_out["volume"] = zone.volume
            zone_out["use_conditions"] = collections.OrderedDict()
            zone_out["use_conditions"]["usage"] = zone.use_conditions.usage

            zone_out["use_conditions"][
                "typical_length"
            ] = zone.use_conditions.typical_length
            zone_out["use_conditions"][
                "typical_width"
            ] = zone.use_conditions.typical_width
            zone_out["use_conditions"][
                "with_heating"
            ] = zone.use_conditions.with_heating
            zone_out["use_conditions"][
                "with_ideal_thresholds"
            ] = zone.use_conditions.with_ideal_thresholds
            zone_out["use_conditions"][
                "T_threshold_heating"
            ] = zone.use_conditions.T_threshold_heating
            zone_out["use_conditions"][
                "T_threshold_cooling"
            ] = zone.use_conditions.T_threshold_cooling
            zone_out["use_conditions"][
                "with_cooling"
            ] = zone.use_conditions.with_cooling
            zone_out["use_conditions"][
                "fixed_heat_flow_rate_persons"
            ] = zone.use_conditions.fixed_heat_flow_rate_persons
            zone_out["use_conditions"][
                "activity_degree_persons"
            ] = zone.use_conditions.activity_degree_persons
            zone_out["use_conditions"]["persons"] = zone.use_conditions.persons
            zone_out["use_conditions"][
                "internal_gains_moisture_no_people"
            ] = zone.use_conditions.internal_gains_moisture_no_people
            zone_out["use_conditions"][
                "ratio_conv_rad_persons"
            ] = zone.use_conditions.ratio_conv_rad_persons
            zone_out["use_conditions"]["machines"] = zone.use_conditions.machines
            zone_out["use_conditions"][
                "ratio_conv_rad_machines"
            ] = zone.use_conditions.ratio_conv_rad_machines
            zone_out["use_conditions"][
                "lighting_power"
            ] = zone.use_conditions.lighting_power
            zone_out["use_conditions"][
                "ratio_conv_rad_lighting"
            ] = zone.use_conditions.ratio_conv_rad_lighting
            zone_out["use_conditions"][
                "use_constant_infiltration"
            ] = zone.use_conditions.use_constant_infiltration
            zone_out["use_conditions"][
                "infiltration_rate"
            ] = zone.use_conditions.infiltration_rate
            zone_out["use_conditions"][
                "max_user_infiltration"
            ] = zone.use_conditions.max_user_infiltration
            zone_out["use_conditions"][
                "max_overheating_infiltration"
            ] = zone.use_conditions.max_overheating_infiltration
            zone_out["use_conditions"][
                "max_summer_infiltration"
            ] = zone.use_conditions.max_summer_infiltration
            zone_out["use_conditions"][
                "winter_reduction_infiltration"
            ] = zone.use_conditions.winter_reduction_infiltration
            zone_out["use_conditions"]["min_ahu"] = zone.use_conditions.min_ahu
            zone_out["use_conditions"]["max_ahu"] = zone.use_conditions.max_ahu
            zone_out["use_conditions"]["with_ahu"] = zone.use_conditions.with_ahu
            zone_out["use_conditions"][
                "heating_profile"
            ] = zone.use_conditions.heating_profile
            zone_out["use_conditions"][
                "cooling_profile"
            ] = zone.use_conditions.cooling_profile
            zone_out["use_conditions"][
                "persons_profile"
            ] = zone.use_conditions.persons_profile
            zone_out["use_conditions"][
                "machines_profile"
            ] = zone.use_conditions.machines_profile
            zone_out["use_conditions"][
                "lighting_profile"
            ] = zone.use_conditions.lighting_profile

            zone_out["outer_walls"] = collections.OrderedDict()
            zone_out["doors"] = collections.OrderedDict()
            zone_out["rooftops"] = collections.OrderedDict()
            zone_out["ground_floors"] = collections.OrderedDict()
            zone_out["windows"] = collections.OrderedDict()
            zone_out["inner_walls"] = collections.OrderedDict()
            zone_out["floors"] = collections.OrderedDict()
            zone_out["ceilings"] = collections.OrderedDict()

            for out_wall in zone.outer_walls:
                zone_out["outer_walls"][out_wall.name] = collections.OrderedDict()
                set_basic_data(zone_out["outer_walls"][out_wall.name], out_wall)
                set_layer_data(zone_out["outer_walls"][out_wall.name], out_wall)
            for door in zone.doors:
                zone_out["doors"][door.name] = collections.OrderedDict()
                set_basic_data(zone_out["doors"][door.name], door)
                set_layer_data(zone_out["doors"][door.name], door)
            for roof in zone.rooftops:
                zone_out["rooftops"][roof.name] = collections.OrderedDict()
                set_basic_data(zone_out["rooftops"][roof.name], roof)
                set_layer_data(zone_out["rooftops"][roof.name], roof)
            for gf in zone.ground_floors:
                zone_out["ground_floors"][gf.name] = collections.OrderedDict()
                set_basic_data(zone_out["ground_floors"][gf.name], gf)
                set_layer_data(zone_out["ground_floors"][gf.name], gf)
            for win in zone.windows:
                zone_out["windows"][win.name] = collections.OrderedDict()
                set_basic_data(zone_out["windows"][win.name], win)
                set_layer_data(zone_out["windows"][win.name], win)
            for iw in zone.inner_walls:
                zone_out["inner_walls"][iw.name] = collections.OrderedDict()
                set_basic_data(zone_out["inner_walls"][iw.name], iw)
                set_layer_data(zone_out["inner_walls"][iw.name], iw)
            for floor in zone.floors:
                zone_out["floors"][floor.name] = collections.OrderedDict()
                set_basic_data(zone_out["floors"][floor.name], floor)
                set_layer_data(zone_out["floors"][floor.name], floor)
            for ceil in zone.ceilings:
                zone_out["ceilings"][ceil.name] = collections.OrderedDict()
                set_basic_data(zone_out["ceilings"][ceil.name], ceil)
                set_layer_data(zone_out["ceilings"][ceil.name], ceil)

            prj_out["project"]["buildings"][bldg.name]["thermal_zones"][
                zone.name
            ] = zone_out

    with open(path, "w") as file:
        file.write(json.dumps(prj_out, indent=4, separators=(",", ": ")))


def set_basic_data(wall_out, element):
    """Set basic data of building elements.

    Parameters
    ----------
    wall_out : collection.OrderedDict
        OrderedDict for walls

    element : TEASERClass
        teaser class representation of a building element

    """
    wall_out["year_of_construction"] = element.year_of_construction
    wall_out["year_of_retrofit"] = element.year_of_retrofit
    wall_out["construction_type"] = element.construction_type

    wall_out["area"] = element.area
    wall_out["tilt"] = element.tilt
    wall_out["orientation"] = element.orientation

    wall_out["inner_radiation"] = element.inner_radiation
    wall_out["inner_convection"] = element.inner_convection

    if (
        type(element).__name__ == "OuterWall"
        or type(element).__name__ == "Rooftop"
        or type(element).__name__ == "Door"
    ):

        wall_out["outer_radiation"] = element.outer_radiation
        wall_out["outer_convection"] = element.outer_convection

    elif type(element).__name__ == "Window":

        wall_out["outer_radiation"] = element.outer_radiation
        wall_out["outer_convection"] = element.outer_convection
        wall_out["g_value"] = element.g_value
        wall_out["a_conv"] = element.a_conv
        wall_out["shading_g_total"] = element.shading_g_total
        wall_out["shading_max_irr"] = element.shading_max_irr


def set_layer_data(wall_out, element):
    """Set layer data of building element.

    Parameters
    ----------
    wall_out : collection.OrderedDict
        OrderedDict for walls

    element : TEASERClass
        teaser class representation of a building element

    """
    layer_dict = collections.OrderedDict()
    for layer in element.layer:

        layer_dict[layer.id] = collections.OrderedDict()
        layer_dict[layer.id]["thickness"] = layer.thickness
        layer_dict[layer.id]["material"] = collections.OrderedDict()
        layer_dict[layer.id]["material"]["name"] = layer.material.name
        layer_dict[layer.id]["material"]["density"] = layer.material.density
        layer_dict[layer.id]["material"][
            "thermal_conduc"
        ] = layer.material.thermal_conduc
        layer_dict[layer.id]["material"]["heat_capac"] = layer.material.heat_capac
        layer_dict[layer.id]["material"]["solar_absorp"] = layer.material.solar_absorp
        layer_dict[layer.id]["material"]["ir_emissivity"] = layer.material.ir_emissivity

    wall_out["layer"] = layer_dict
