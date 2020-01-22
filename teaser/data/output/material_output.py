"""This module contains function to save material classes."""
import warnings
import json
import teaser.logic.utilities as utilities
import collections


def save_material(material, data_class):
    """Material saver.

    Saves material and their properties the JSON file for type building
    elements. If the Project parent is set, it automatically saves it to
    the file given in Project.data. Alternatively you can specify a path to
    a file with Materials. If this file does not exist, a new file is created.

    Parameters
    ----------
    material : Material()
        instance of TEASERS Material class

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.

    """
    data_class.material_bind["version"] = "0.7"
    add_to_json = True

    warning_text = ("Material with same name and same properties already "
                    "exists in JSON, consider this material or revising your "
                    "properties")

    for id, check in data_class.material_bind.items():
        if id != "version":
            if check["name"] == material.name and \
                    check["density"] == material.density and \
                    check["thermal_conduc"] == material.thermal_conduc and \
                    check["heat_capac"] == material.heat_capac and \
                    check[
                        "thickness_default"] == material.thickness_default and \
                    check["thickness_list"] == material.thickness_list:

                warnings.warn(warning_text)
                print(material.name)
                add_to_json = False
                break

    if add_to_json is True:
        data_class.material_bind[
            material.material_id] = collections.OrderedDict()
        data_class.material_bind[
            material.material_id]["name"] = material.name
        data_class.material_bind[
            material.material_id]["density"] = material.density
        data_class.material_bind[
            material.material_id]["thermal_conduc"] = material.thermal_conduc
        data_class.material_bind[
            material.material_id]["heat_capac"] = material.heat_capac
        data_class.material_bind[
            material.material_id][
                "thickness_default"] = material.thickness_default
        data_class.material_bind[
            material.material_id]["thickness_list"] = material.thickness_list
        data_class.material_bind[
            material.material_id]["solar_absorp"] = material.solar_absorp

    with open(utilities.get_full_path(data_class.path_mat), 'w') as file:
        file.write(json.dumps(
            data_class.material_bind,
            indent=4,
            separators=(',', ': ')))
