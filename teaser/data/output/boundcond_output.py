# Created April 2016
# TEASER Development Team


"""boundcond_output.py

This module contains function to save boundary conditions classes
"""

import teaser.data.bindings.v_0_6.boundaryconditions_bind as uc_bind
import teaser.logic.utilities as utilities
import warnings
import pyxb


def save_bound_conditions(bound_cond, data_class):
    """Use conditions saver.

    Saves use conditions according to their usage type in the the XML file
    for use conditions in InputData. If the Project parent is set, it
    automatically saves it to the file given in Project.data. Alternatively
    you can specify a path to a file of UseConditions. If this
    file does not exist, a new file is created.

    Parameters
    ----------

    bound_cond : BoundaryConditions()
        Instance of TEASERs
        BuildingObjects.BoundaryConditions.BoundaryConditions

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.ile
    """

    conditions_bind = data_class.conditions_bind
    add_to_xml = True

    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        uc_bind.Namespace, 'usecond')

    for check in conditions_bind.BoundaryConditions:
        if check.usage == bound_cond.usage:
            warnings.warn("Usage already exist in this XML, consider " +
                          "revising your inputs. The UseConditions is  " +
                          "NOT saved into XML")
            add_to_xml = False
            break
    conditions_bind.version = "0.6"
    if add_to_xml is True:

        usage_pyxb = uc_bind.BoundaryConditionsType()
        usage_pyxb.UsageOperationTime = uc_bind.UsageOperationTimeType()
        usage_pyxb.Lighting = uc_bind.LightingType()
        usage_pyxb.RoomClimate = uc_bind.RoomClimateType()
        usage_pyxb.InternalGains = uc_bind.InternalGainsType()
        usage_pyxb.AHU = uc_bind.AHUType()

        usage_pyxb.usage = bound_cond.usage

        usage_pyxb.UsageOperationTime.usage_time =\
            bound_cond.usage_time
        usage_pyxb.UsageOperationTime.daily_usage_hours = \
            bound_cond.daily_usage_hours
        usage_pyxb.UsageOperationTime.yearly_usage_days = \
            bound_cond.yearly_usage_days
        usage_pyxb.UsageOperationTime.yearly_usage_hours_day = \
            bound_cond.yearly_usage_hours_day
        usage_pyxb.UsageOperationTime.yearly_usage_hours_night = \
            bound_cond.yearly_usage_hours_night
        usage_pyxb.UsageOperationTime.daily_operation_ahu_cooling = \
            bound_cond.daily_operation_ahu_cooling
        usage_pyxb.UsageOperationTime.yearly_heating_days = \
            bound_cond.yearly_heating_days
        usage_pyxb.UsageOperationTime.yearly_ahu_days = \
            bound_cond.yearly_ahu_days
        usage_pyxb.UsageOperationTime.yearly_cooling_days = \
            bound_cond.yearly_cooling_days
        usage_pyxb.UsageOperationTime.daily_operation_heating = \
            bound_cond.daily_operation_heating

        usage_pyxb.Lighting.maintained_illuminance = \
            bound_cond.maintained_illuminance
        usage_pyxb.Lighting.usage_level_height = bound_cond.usage_level_height
        usage_pyxb.Lighting.red_factor_visual = bound_cond.red_factor_visual
        usage_pyxb.Lighting.rel_absence = bound_cond.rel_absence
        usage_pyxb.Lighting.room_index = bound_cond.room_index
        usage_pyxb.Lighting.part_load_factor_lighting = \
            bound_cond.part_load_factor_lighting
        usage_pyxb.Lighting.ratio_conv_rad_lighting = \
            bound_cond.ratio_conv_rad_lighting

        usage_pyxb.RoomClimate.set_temp_heat = bound_cond.set_temp_heat
        usage_pyxb.RoomClimate.set_temp_cool = bound_cond.set_temp_cool
        usage_pyxb.RoomClimate.temp_set_back = bound_cond.temp_set_back
        usage_pyxb.RoomClimate.min_temp_heat = bound_cond.min_temp_heat
        usage_pyxb.RoomClimate.max_temp_cool = bound_cond.max_temp_cool
        usage_pyxb.RoomClimate.rel_humidity = bound_cond.rel_humidity
        usage_pyxb.RoomClimate.cooling_time = bound_cond.cooling_time
        usage_pyxb.RoomClimate.heating_time = bound_cond.heating_time
        usage_pyxb.RoomClimate.min_air_exchange = bound_cond.min_air_exchange
        usage_pyxb.RoomClimate.rel_absence_ahu = bound_cond.rel_absence_ahu
        usage_pyxb.RoomClimate.part_load_factor_ahu = \
            bound_cond.part_load_factor_ahu

        usage_pyxb.InternalGains.persons = bound_cond.persons
        usage_pyxb.InternalGains.profile_persons = bound_cond.profile_persons
        usage_pyxb.InternalGains.machines = bound_cond.machines
        usage_pyxb.InternalGains.profile_machines = bound_cond.profile_machines
        usage_pyxb.InternalGains.lighting_power = bound_cond.lighting_power
        usage_pyxb.InternalGains.profile_lighting = bound_cond.profile_lighting

        usage_pyxb.AHU.min_ahu = bound_cond.min_ahu
        usage_pyxb.AHU.max_ahu = bound_cond.max_ahu
        usage_pyxb.AHU.with_ahu = bound_cond.with_ahu
        usage_pyxb.AHU.use_constant_ach_rate = bound_cond.use_constant_ach_rate
        usage_pyxb.AHU.base_ach = bound_cond.base_ach
        usage_pyxb.AHU.max_user_ach = bound_cond.max_user_ach
        usage_pyxb.AHU.max_overheating_ach = bound_cond.max_overheating_ach
        usage_pyxb.AHU.max_summer_ach = bound_cond.max_summer_ach
        usage_pyxb.AHU.winter_reduction = bound_cond.winter_reduction

        usage_pyxb.typical_length = bound_cond.typical_length
        usage_pyxb.typical_width = bound_cond.typical_width

        conditions_bind.append(usage_pyxb)

        out_file = open(utilities.get_full_path(data_class.path_uc), 'w')

        out_file.write(conditions_bind.toDOM().toprettyxml())
