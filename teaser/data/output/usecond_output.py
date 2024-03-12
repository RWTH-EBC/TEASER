"""This module contains function to save UseConditions classes."""

import collections
import json
import warnings
import teaser.logic.utilities as utilities


def save_use_conditions(use_cond, data_class):
    """Use conditions saver.

    Saves use conditions according to their geometry_data type in the the JSON file
    for use conditions in InputData. If the Project parent is set, it
    automatically saves it to the file given in Project.data. Alternatively
    you can specify a path to a file of UseConditions. If this
    file does not exist, a new file is created.

    Parameters
    ----------
    bound_cond : UseCondtiions()
        Instance of TEASERs
        BuildingObjects.UseCondtiions
    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.ile

    """
    if use_cond.geometry_data in data_class.conditions_bind.keys():
        add_to_json = False
        warnings.warn(
            "geometry_data already exist in this JSON, consider "
            + "revising your inputs. The UseConditions is  "
            + "NOT saved into JSON"
        )
    else:
        add_to_json = True

    data_class.conditions_bind["version"] = "0.7"

    if add_to_json is True:
        data_class.conditions_bind[use_cond.geometry_data] = collections.OrderedDict()
        data_class.conditions_bind[use_cond.geometry_data][
            "typical_length"
        ] = use_cond.typical_length
        data_class.conditions_bind[use_cond.geometry_data][
            "typical_width"
        ] = use_cond.typical_width
        data_class.conditions_bind[use_cond.geometry_data][
            "with_heating"
        ] = use_cond.with_heating
        data_class.conditions_bind[use_cond.geometry_data][
            "T_threshold_heating"
        ] = use_cond.T_threshold_heating
        data_class.conditions_bind[use_cond.geometry_data][
            "T_threshold_cooling"
        ] = use_cond.T_threshold_cooling
        data_class.conditions_bind[use_cond.geometry_data][
            "with_cooling"
        ] = use_cond.with_cooling
        data_class.conditions_bind[use_cond.geometry_data][
            "fixed_heat_flow_rate_persons"
        ] = use_cond.fixed_heat_flow_rate_persons
        data_class.conditions_bind[use_cond.geometry_data][
            "activity_degree_persons"
        ] = use_cond.activity_degree_persons
        data_class.conditions_bind[use_cond.geometry_data][
            "activity_degree_persons"
        ] = use_cond.activity_degree_persons
        data_class.conditions_bind[use_cond.geometry_data]["persons"] = use_cond.persons
        data_class.conditions_bind[use_cond.geometry_data][
            "internal_gains_moisture_no_people"
        ] = use_cond.internal_gains_moisture_no_people
        data_class.conditions_bind[use_cond.geometry_data][
            "ratio_conv_rad_persons"
        ] = use_cond.ratio_conv_rad_persons
        data_class.conditions_bind[use_cond.geometry_data]["machines"] = use_cond.machines
        data_class.conditions_bind[use_cond.geometry_data][
            "ratio_conv_rad_machines"
        ] = use_cond.ratio_conv_rad_machines
        data_class.conditions_bind[use_cond.geometry_data][
            "lighting_power"
        ] = use_cond.lighting_power
        data_class.conditions_bind[use_cond.geometry_data][
            "ratio_conv_rad_lighting"
        ] = use_cond.ratio_conv_rad_lighting
        data_class.conditions_bind[use_cond.geometry_data][
            "use_constant_infiltration"
        ] = use_cond.use_constant_infiltration
        data_class.conditions_bind[use_cond.geometry_data][
            "infiltration_rate"
        ] = use_cond.infiltration_rate
        data_class.conditions_bind[use_cond.geometry_data][
            "max_user_infiltration"
        ] = use_cond.max_user_infiltration
        data_class.conditions_bind[use_cond.geometry_data][
            "max_overheating_infiltration"
        ] = use_cond.max_overheating_infiltration
        data_class.conditions_bind[use_cond.geometry_data][
            "max_summer_infiltration"
        ] = use_cond.max_summer_infiltration
        data_class.conditions_bind[use_cond.geometry_data][
            "winter_reduction_infiltration"
        ] = use_cond.winter_reduction_infiltration
        data_class.conditions_bind[use_cond.geometry_data]["min_ahu"] = use_cond.min_ahu
        data_class.conditions_bind[use_cond.geometry_data]["max_ahu"] = use_cond.max_ahu
        data_class.conditions_bind[use_cond.geometry_data]["with_ahu"] = use_cond.with_ahu
        data_class.conditions_bind[use_cond.geometry_data][
            "heating_profile"
        ] = use_cond.heating_profile
        data_class.conditions_bind[use_cond.geometry_data][
            "cooling_profile"
        ] = use_cond.cooling_profile
        data_class.conditions_bind[use_cond.geometry_data][
            "persons_profile"
        ] = use_cond.persons_profile
        data_class.conditions_bind[use_cond.geometry_data][
            "machines_profile"
        ] = use_cond.machines_profile
        data_class.conditions_bind[use_cond.geometry_data][
            "lighting_profile"
        ] = use_cond.lighting_profile
        data_class.conditions_bind[use_cond.geometry_data][
            "with_ideal_thresholds"
        ] = use_cond.with_ideal_thresholds

    with open(utilities.get_full_path(data_class.path_uc), "w") as file:
        file.write(
            json.dumps(data_class.conditions_bind, indent=4, separators=(",", ": "))
        )
