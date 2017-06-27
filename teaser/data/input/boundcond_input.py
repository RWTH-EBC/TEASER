# Created April 2016
# TEASER Development Team

"""boundcond_input.py

This module contains function to load boundary conditions classes
"""


def load_boundary_conditions(bound_cond, zone_usage, data_class):
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

    for usage in conditions_bind.BoundaryConditions:

        if usage.usage == zone_usage:

            bound_cond.typical_length = usage.typical_length
            bound_cond.typical_width = usage.typical_width

            bound_cond.usage = usage.usage
            bound_cond.usage_time = usage.UsageOperationTime.usage_time
            bound_cond.daily_usage_hours = \
                usage.UsageOperationTime.daily_usage_hours
            bound_cond.yearly_usage_days = \
                usage.UsageOperationTime.yearly_usage_days
            bound_cond.yearly_usage_hours_day = \
                usage.UsageOperationTime.yearly_usage_hours_day
            bound_cond.yearly_usage_hours_night = \
                usage.UsageOperationTime.yearly_usage_hours_night
            bound_cond.daily_operation_ahu_cooling = \
                usage.UsageOperationTime.daily_operation_ahu_cooling
            bound_cond.yearly_heating_days = \
                usage.UsageOperationTime.yearly_heating_days
            bound_cond.yearly_ahu_days = \
                usage.UsageOperationTime.yearly_ahu_days
            bound_cond.yearly_cooling_days = \
                usage.UsageOperationTime.yearly_cooling_days
            bound_cond.daily_operation_heating = \
                usage.UsageOperationTime.daily_operation_heating
            if float(data_class.conditions_bind.version) >= 0.4:
                bound_cond.maintained_illuminance = \
                    usage.Lighting.maintained_illuminance
            else:
                bound_cond.maintained_illuminance = \
                    usage.Lighting.maintained_illuminace
            bound_cond.usage_level_height = usage.Lighting.usage_level_height
            bound_cond.red_factor_visual = usage.Lighting.red_factor_visual
            bound_cond.rel_absence = usage.Lighting.rel_absence
            bound_cond.room_index = usage.Lighting.room_index
            bound_cond.part_load_factor_lighting = \
                usage.Lighting.part_load_factor_lighting
            bound_cond.ratio_conv_rad_lighting = \
                usage.Lighting.ratio_conv_rad_lighting

            bound_cond.set_temp_heat = usage.RoomClimate.set_temp_heat
            bound_cond.set_temp_cool = usage.RoomClimate.set_temp_cool
            bound_cond.temp_set_back = usage.RoomClimate.temp_set_back
            bound_cond.min_temp_heat = usage.RoomClimate.min_temp_heat
            bound_cond.max_temp_cool = usage.RoomClimate.max_temp_cool
            bound_cond.rel_humidity = usage.RoomClimate.rel_humidity
            bound_cond.cooling_time = usage.RoomClimate.cooling_time
            bound_cond.heating_time = usage.RoomClimate.heating_time
            bound_cond.min_air_exchange = usage.RoomClimate.min_air_exchange
            bound_cond.rel_absence_ahu = usage.RoomClimate.rel_absence_ahu
            bound_cond.part_load_factor_ahu = \
                usage.RoomClimate.part_load_factor_ahu

            bound_cond.persons = usage.InternalGains.persons
            bound_cond.profile_persons = usage.InternalGains.profile_persons
            bound_cond.machines = usage.InternalGains.machines
            bound_cond.profile_machines = usage.InternalGains.profile_machines
            bound_cond.lighting_power = usage.InternalGains.lighting_power
            bound_cond.profile_lighting = usage.InternalGains.profile_lighting
            bound_cond.min_ahu = usage.AHU.min_ahu
            bound_cond.max_ahu = usage.AHU.max_ahu
            bound_cond.with_ahu = usage.AHU.with_ahu
            bound_cond.use_constant_ach_rate = usage.AHU.use_constant_ach_rate
            bound_cond.base_ach = usage.AHU.base_ach
            bound_cond.max_user_ach = usage.AHU.max_user_ach
            bound_cond.max_overheating_ach = usage.AHU.max_overheating_ach
            bound_cond.max_summer_ach = usage.AHU.max_summer_ach
            bound_cond.winter_reduction = usage.AHU.winter_reduction
