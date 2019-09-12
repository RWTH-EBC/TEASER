"""OLD! Will be deleted in future version.

This module contains function to load boundary conditions classes
"""
import warnings


def load_boundary_conditions(bound_cond, zone_usage, data_class):
    """Function to load old XML files into new UseConditions class.

    ATTENTION: This function should only be used if you defined your own
    UseConditions.xml file!

    Loads Use conditions specified in the XML, according to DIN 18599,
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

    warnings.warn(
        "This function should only be used to transform old XML files"
        "and will be deleted within the next versions of TEASER")

    conditions_bind = data_class.conditions_bind

    for usage in conditions_bind.BoundaryConditions:

        if usage.usage == zone_usage:

            bound_cond.typical_length = usage.typical_length
            bound_cond.typical_width = usage.typical_width

            bound_cond.usage = usage.usage

            bound_cond.set_temp_heat = [usage.RoomClimate.set_temp_heat, ]
            bound_cond.set_temp_cool = [usage.RoomClimate.set_temp_cool, ]

            bound_cond.persons = usage.InternalGains.persons
            bound_cond.persons_profile = usage.InternalGains.profile_persons
            bound_cond.machines = usage.InternalGains.machines
            bound_cond.machines_profile = usage.InternalGains.profile_machines
            bound_cond.lighting_power = usage.InternalGains.lighting_power
            bound_cond.lighting_profile = usage.InternalGains.profile_lighting
            bound_cond.ratio_conv_rad_lighting = \
                usage.Lighting.ratio_conv_rad_lighting
            bound_cond.min_ahu = usage.AHU.min_ahu
            bound_cond.max_ahu = usage.AHU.max_ahu
            bound_cond.with_ahu = usage.AHU.with_ahu
            bound_cond.use_constant_infiltration = \
                usage.AHU.use_constant_ach_rate
            bound_cond.base_infiltration = usage.AHU.base_ach
            bound_cond.max_user_infiltration = usage.AHU.max_user_ach
            bound_cond.max_overheating_infiltration = \
                usage.AHU.max_overheating_ach
            bound_cond.max_summer_infiltration = usage.AHU.max_summer_ach
            bound_cond.winter_reduction_infiltration = \
                usage.AHU.winter_reduction
