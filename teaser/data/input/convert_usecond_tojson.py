import ipdb
import teaser.data.output.usecond_output as usecond_output
from teaser.data.dataclass import DataClass
from teaser.logic.buildingobjects.useconditions import UseConditions
import json
import collections
data_class = DataClass()

conditions_bind = data_class.conditions_bind

output = collections.OrderedDict()
true_false_dict = {0: False, 1: True}
for usage in conditions_bind.BoundaryConditions:

    uc = UseConditions()
    uc.usage = usage.usage
    uc.typical_length = usage.typical_length
    uc.typical_width = usage.typical_width
    uc.with_heating = True
    uc.with_cooling = False
    uc.persons = usage.InternalGains.persons
    uc.ratio_conv_rad_persons = 0.5
    uc.machines = usage.InternalGains.machines
    uc.ratio_conv_rad_machines = 0.75
    uc.lighting_power = usage.InternalGains.lighting_power
    uc.ratio_conv_rad_lighting = usage.Lighting.ratio_conv_rad_lighting
    uc.use_constant_infiltration = true_false_dict[
        usage.AHU.use_constant_ach_rate]
    uc.infiltration_rate = usage.AHU.base_ach
    uc.max_user_infiltration = usage.AHU.max_user_ach
    uc.max_overheating_infiltration = usage.AHU.max_overheating_ach
    uc.max_summer_infiltration = usage.AHU.max_summer_ach
    uc.winter_reduction_infiltration = usage.AHU.winter_reduction
    uc.min_ahu = usage.AHU.min_ahu
    uc.max_ahu = usage.AHU.max_ahu
    uc.with_ahu = true_false_dict[usage.AHU.with_ahu]
    uc.heating_profile = 25 * [usage.RoomClimate.set_temp_heat]
    uc.cooling_profile = 25 * [usage.RoomClimate.set_temp_heat]
    uc.persons_profile = usage.InternalGains.profile_persons
    uc.machines_profile = usage.InternalGains.profile_machines
    uc.lighting_profile = usage.InternalGains.profile_lighting
    output = usecond_output.save_use_conditions(uc, output)


with open("zone_all.json", 'a') as file:
    file.write(json.dumps(
        output,
        indent=4,
        separators=(',', ': ')))
