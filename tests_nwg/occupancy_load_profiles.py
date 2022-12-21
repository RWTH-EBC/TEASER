"""This module contains function to adjust the UseConditions """


def adjust_use_conditions(use_cond, zone_usage, data_class):
    """Adjust use conditions according to individually defined configurations in JSON files

    Parameters
    ----------
    use_cond : UseConditions()
        Instance of TEASERs
        BuildingObjects.UseConditions

    zone_usage : str
        code list for zone_usage as defined in JSON File

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.

    """
    conditions_bind = data_class.conditions_bind

    use_cond.usage = zone_usage

    use_cond.persons = conditions_bind[zone_usage]["persons"]

    use_cond.machines = conditions_bind[zone_usage]["machines"]
    use_cond.lighting_power = conditions_bind[zone_usage]["lighting_power"]

    use_cond.persons_profile = conditions_bind[zone_usage]["persons_profile"]
    use_cond.machines_profile = conditions_bind[zone_usage]["machines_profile"]
    use_cond.lighting_profile = conditions_bind[zone_usage]["lighting_profile"]

