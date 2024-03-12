"""This module contains function to load UseConditions classes."""


def load_use_conditions(use_cond, zone_geometry_data, data_class):
    """Load use conditions from JSON, according to DIN 18599,
    SIA2024 in addition some AixLib specific use conditions for central AHU
    are defined.

    Parameters
    ----------
    use_cond : UseConditions()
        Instance of TEASERs
        BuildingObjects.UseConditions

    zone_geometry_data : str
        code list for zone_geometry_data according to 18599

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.

    """
    conditions_bind = data_class.conditions_bind

    use_cond.geometry_data = zone_geometry_data

    use_cond.typical_length = conditions_bind[zone_geometry_data]["typical_length"]
    use_cond.typical_width = conditions_bind[zone_geometry_data]["typical_width"]
    use_cond.with_heating = conditions_bind[zone_geometry_data]["with_heating"]
    use_cond.T_threshold_heating = conditions_bind[zone_geometry_data]["T_threshold_heating"]
    use_cond.T_threshold_cooling = conditions_bind[zone_geometry_data]["T_threshold_cooling"]
    use_cond.with_cooling = conditions_bind[zone_geometry_data]["with_cooling"]
    use_cond.fixed_heat_flow_rate_persons = conditions_bind[zone_geometry_data][
        "fixed_heat_flow_rate_persons"
    ]
    use_cond.activity_degree_persons = conditions_bind[zone_geometry_data][
        "activity_degree_persons"
    ]
    use_cond.persons = conditions_bind[zone_geometry_data]["persons"]
    use_cond.internal_gains_moisture_no_people = conditions_bind[zone_geometry_data][
        "internal_gains_moisture_no_people"
    ]
    use_cond.ratio_conv_rad_persons = conditions_bind[zone_geometry_data][
        "ratio_conv_rad_persons"
    ]
    use_cond.machines = conditions_bind[zone_geometry_data]["machines"]
    use_cond.ratio_conv_rad_machines = conditions_bind[zone_geometry_data][
        "ratio_conv_rad_machines"
    ]
    use_cond.lighting_power = conditions_bind[zone_geometry_data]["lighting_power"]
    use_cond.ratio_conv_rad_lighting = conditions_bind[zone_geometry_data][
        "ratio_conv_rad_lighting"
    ]
    use_cond.use_constant_infiltration = conditions_bind[zone_geometry_data][
        "use_constant_infiltration"
    ]
    use_cond.infiltration_rate = conditions_bind[zone_geometry_data]["infiltration_rate"]
    use_cond.max_user_infiltration = conditions_bind[zone_geometry_data][
        "max_user_infiltration"
    ]
    use_cond.max_overheating_infiltration = conditions_bind[zone_geometry_data][
        "max_overheating_infiltration"
    ]
    use_cond.max_summer_infiltration = conditions_bind[zone_geometry_data][
        "max_summer_infiltration"
    ]
    use_cond.winter_reduction_infiltration = conditions_bind[zone_geometry_data][
        "winter_reduction_infiltration"
    ]
    use_cond.min_ahu = conditions_bind[zone_geometry_data]["min_ahu"]
    use_cond.max_ahu = conditions_bind[zone_geometry_data]["max_ahu"]
    use_cond.with_ahu = conditions_bind[zone_geometry_data]["with_ahu"]
    use_cond.heating_profile = conditions_bind[zone_geometry_data]["heating_profile"]
    use_cond.cooling_profile = conditions_bind[zone_geometry_data]["cooling_profile"]
    use_cond.persons_profile = conditions_bind[zone_geometry_data]["persons_profile"]
    use_cond.machines_profile = conditions_bind[zone_geometry_data]["machines_profile"]
    use_cond.lighting_profile = conditions_bind[zone_geometry_data]["lighting_profile"]
    use_cond.with_ideal_thresholds = conditions_bind[zone_geometry_data][
        "with_ideal_thresholds"
    ]
