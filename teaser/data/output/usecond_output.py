"""This module contains function to save UseConditions classes."""

import collections
import json


def save_use_conditions(use_cond, conditions_data):
    """Documentation is missing.
    """

    add_to_json = True

    conditions_data["version"] = "0.7"
    if add_to_json is True:
        conditions_data[use_cond.usage] = collections.OrderedDict()
        conditions_data[use_cond.usage][
            "typical_length"] = use_cond.typical_length
        conditions_data[use_cond.usage][
            "typical_width"] = use_cond.typical_width
        conditions_data[use_cond.usage][
            "with_heating"] = use_cond.with_heating
        conditions_data[use_cond.usage][
            "with_cooling"] = use_cond.with_cooling
        conditions_data[use_cond.usage][
            "persons"] = use_cond.persons
        conditions_data[use_cond.usage][
            "ratio_conv_rad_persons"] = use_cond.ratio_conv_rad_persons
        conditions_data[use_cond.usage][
            "machines"] = use_cond.machines
        conditions_data[use_cond.usage][
            "ratio_conv_rad_machines"] = use_cond.ratio_conv_rad_machines
        conditions_data[use_cond.usage][
            "lighting_power"] = use_cond.lighting_power
        conditions_data[use_cond.usage][
            "ratio_conv_rad_lighting"] = use_cond.ratio_conv_rad_lighting
        conditions_data[use_cond.usage][
            "use_constant_infiltration"] = use_cond.use_constant_infiltration
        conditions_data[use_cond.usage][
            "infiltration_rate"] = use_cond.infiltration_rate
        conditions_data[use_cond.usage][
            "max_user_infiltration"] = use_cond.max_user_infiltration
        conditions_data[
            use_cond.usage][
            "max_overheating_infiltration"] = use_cond.max_overheating_infiltration
        conditions_data[use_cond.usage][
            "max_summer_infiltration"] = use_cond.max_summer_infiltration
        conditions_data[
            use_cond.usage][
            "winter_reduction_infiltration"] = use_cond.winter_reduction_infiltration
        conditions_data[use_cond.usage][
            "min_ahu"] = use_cond.min_ahu
        conditions_data[use_cond.usage][
            "max_ahu"] = use_cond.max_ahu
        conditions_data[use_cond.usage][
            "heating_profile"] = use_cond.heating_profile
        conditions_data[use_cond.usage][
            "cooling_profile"] = use_cond.cooling_profile
        conditions_data[use_cond.usage][
            "persons_profile"] = use_cond.persons_profile
        conditions_data[use_cond.usage][
            "machines_profile"] = use_cond.machines_profile
        conditions_data[use_cond.usage][
            "lighting_profile"] = use_cond.lighting_profile

    return conditions_data
