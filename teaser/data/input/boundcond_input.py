"""This module contains function to load UseConditions classes."""


def load_use_conditions(bound_cond, zone_usage, data_class):
    """load use conditions according to DIN 18599 and SIA2024

    loads Use conditions specified in the XML, according to DIN 18599,
    SIA2024 in addition some AixLib specific use conditions for central AHU
    are defined.

    Parameters
    ----------
    bound_cond : BoundaryConditions()
        Instance of TEASERs
        BuildingObjects.BoundaryConditions.BoundaryConditions

    zone_usage : str
        code list for zone_usage according to 18599

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.
    """

    conditions_bind = data_class.conditions_bind

    bound_cond.usage = zone_usage

    bound_cond.typical_length = conditions_bind[zone_usage]["typical_length"]
    bound_cond.typical_width = conditions_bind[zone_usage]["typical_width"]
    bound_cond.with_heating = conditions_bind[zone_usage]["with_heating"]
    bound_cond.with_cooling = conditions_bind[zone_usage]["with_cooling"]
    bound_cond.persons = conditions_bind[zone_usage]["persons"]
    bound_cond.ratio_conv_rad_persons = conditions_bind[zone_usage][
        "ratio_conv_rad_persons"]
    bound_cond.machines = conditions_bind[zone_usage]["machines"]
    bound_cond.ratio_conv_rad_machines = conditions_bind[zone_usage][
        "ratio_conv_rad_machines"]
    bound_cond.lighting_power = conditions_bind[
        zone_usage][
        "lighting_power"]
    bound_cond.ratio_conv_rad_lighting = conditions_bind[
        zone_usage]["ratio_conv_rad_lighting"]
    bound_cond.use_constant_infiltration = conditions_bind[
        zone_usage]["use_constant_infiltration"]
    bound_cond.infiltration_rate = conditions_bind[zone_usage][
        "infiltration_rate"]
    bound_cond.max_user_infiltration = conditions_bind[
        zone_usage]["max_user_infiltration"]
    bound_cond.max_overheating_infiltration = conditions_bind[
        zone_usage]["max_overheating_infiltration"]
    bound_cond.max_summer_infiltration = conditions_bind[
        zone_usage]["max_summer_infiltration"]
    bound_cond.winter_reduction_infiltration = conditions_bind[
        zone_usage]["winter_reduction_infiltration"]
    bound_cond.min_ahu = conditions_bind[zone_usage]["min_ahu"]
    bound_cond.max_ahu = conditions_bind[zone_usage]["max_ahu"]
    bound_cond.heating_profile = conditions_bind[zone_usage]["heating_profile"]
    bound_cond.cooling_profile = conditions_bind[zone_usage]["cooling_profile"]
    bound_cond.persons_profile = conditions_bind[zone_usage]["persons_profile"]
    bound_cond.machines_profile = conditions_bind[
        zone_usage]["machines_profile"]
    bound_cond.lighting_profile = conditions_bind[
        zone_usage]["lighting_profile"]
