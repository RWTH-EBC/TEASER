"""This module contains function to save building element classes."""

import teaser.logic.utilities as utilities
import warnings
import collections
import json


def save_type_element(element, data_class):
    """Save information about building element to json.

    Saves typical building elements according to their construction
    year and their construction type in the json file for type building
    elements. If the Project parent is set, it automatically saves it to
    the file given in Project.data. Alternatively you can specify a path to
    a file of TypeBuildingElements. If this file does not exist,
    a new file is created.

    Parameters
    ----------
    element : BuildingElement()
        Instance of BuildingElement or inherited Element of TEASER

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.

    """
    data_class.element_bind["version"] = "0.7"
    add_to_json = True

    warning_text = (
        "Construction Type and building age "
        "group already exist in this json, consider revising "
        "your inputs. The Element is NOT saved into json"
    )

    check_str = "{}_{}_{}".format(
        type(element).__name__, element.building_age_group, element.construction_type
    )

    if check_str in data_class.element_bind.keys():
        warnings.warn(warning_text)
        add_to_json = False
        return

    if add_to_json is True:
        data_class.element_bind[check_str] = collections.OrderedDict()

        _set_basic_data_json(
            element=element, wall_out=data_class.element_bind[check_str]
        )

        _set_layer_data_json(
            element=element, wall_out=data_class.element_bind[check_str]
        )

    with open(utilities.get_full_path(data_class.path_tb), "w") as file:
        file.write(
            json.dumps(data_class.element_bind, indent=4, separators=(",", ": "))
        )


def delete_type_element(element, data_class):
    """Delete typical element in json.

    Deletes typical building elements according to their construction
    year and their construction type in the the json file for type building
    elements. If the Project parent is set, it automatically saves it to
    the file given in Project.data. Alternatively you can specify a path to
    a file of TypeBuildingElements. If this file does not exist,
    a new file is created.
    Parameters
    ----------
    element : BuildingElement()
        Instance of BuildingElement or inherited Element of TEASER
    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.

    """
    check_str = "{}_{}_{}".format(
        type(element).__name__, element.building_age_group, element.construction_type
    )

    del data_class.element_bind[check_str]

    with open(utilities.get_full_path(data_class.path_tb), "w") as file:
        file.write(
            json.dumps(data_class.element_bind, indent=4, separators=(",", ": "))
        )


def _set_basic_data_json(element, wall_out):
    """Set basic data of building element.

    Helper function.

    Parameters
    ----------
    element : BuildingElement()
        Instance of BuildingElement or inherited Element of TEASER
    wall_out: dictionary
        Dictionary with information about walls.

    """
    wall_out["building_age_group"] = element.building_age_group
    wall_out["construction_type"] = element.construction_type
    wall_out["inner_radiation"] = element.inner_radiation
    wall_out["inner_convection"] = element.inner_convection

    if type(element).__name__ == "Window":

        wall_out["outer_radiation"] = element.outer_radiation
        wall_out["outer_convection"] = element.outer_convection
        wall_out["g_value"] = element.g_value
        wall_out["a_conv"] = element.a_conv
        wall_out["shading_g_total"] = element.shading_g_total
        wall_out["shading_max_irr"] = element.shading_max_irr

    elif (
        type(element).__name__ == "OuterWall"
        or type(element).__name__ == "Rooftop"
        or type(element).__name__ == "Door"
    ):

        wall_out["outer_radiation"] = element.outer_radiation
        wall_out["outer_convection"] = element.outer_convection


def _set_layer_data_json(element, wall_out):
    """Set layer data of building element.

    Helper function.

    Parameters
    ----------
    element : BuildingElement()
        Instance of BuildingElement or inherited Element of TEASER
    wall_out: dictionary
        Dictionary with information about walls.

    """
    layer_dict = collections.OrderedDict()
    for layer in element.layer:

        layer_dict[layer.id] = collections.OrderedDict()
        layer_dict[layer.id]["thickness"] = layer.thickness
        layer_dict[layer.id]["material"] = collections.OrderedDict()
        layer_dict[layer.id]["material"]["name"] = layer.material.name
        layer_dict[layer.id]["material"]["material_id"] = layer.material.material_id

    wall_out["layer"] = layer_dict
