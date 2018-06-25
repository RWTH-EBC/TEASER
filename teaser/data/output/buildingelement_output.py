# Created April 2016
# TEASER Development Team

"""buildingelement_ouput.py

This module contains function to save building element classes
"""

import teaser.data.bindings.v_0_6.typeelement_bind as tb_bind
import teaser.logic.utilities as utilities
import warnings
import pyxb


def save_type_element(element, data_class):
    """Typical element saver.

    Saves typical building elements according to their construction
    year and their construction type in the XML file for type building
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

    element_binding = data_class.element_bind
    element_binding.version = "0.6"
    add_to_xml = True

    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        tb_bind.Namespace, 'elements')

    warning_text = ("Construction Type and building age "
                    "group already exist in this XML, consider revising "
                    "your inputs. The Element is NOT saved into XML")
    if type(element).__name__ == "OuterWall":

        for check in element_binding.OuterWall:
            if check.building_age_group == element.building_age_group and\
               check.construction_type == element.construction_type:
                warnings.warn(warning_text)
                add_to_xml = False
                break

        if add_to_xml is True:

            pyxb_wall = tb_bind.OuterWallType()
            _set_basic_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)
            pyxb_wall.Layers = tb_bind.LayersType()
            _set_layer_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)

            element_binding.OuterWall.append(pyxb_wall)

    if type(element).__name__ == "Door":

        for check in element_binding.Door:
            if check.building_age_group == element.building_age_group and\
               check.construction_type == element.construction_type:
                warnings.warn(warning_text)
                add_to_xml = False
                break

        if add_to_xml is True:

            pyxb_wall = tb_bind.DoorType()
            _set_basic_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)
            pyxb_wall.Layers = tb_bind.LayersType()
            _set_layer_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)

            element_binding.Door.append(pyxb_wall)

    elif type(element).__name__ == 'InnerWall':

        for check in element_binding.InnerWall:
            if check.building_age_group == element.building_age_group and\
               check.construction_type == element.construction_type:
                warnings.warn(warning_text)
                add_to_xml = False
                break

        if add_to_xml is True:

            pyxb_wall = tb_bind.InnerWallType()
            _set_basic_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)
            pyxb_wall.Layers = tb_bind.LayersType()
            _set_layer_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)

            element_binding.InnerWall.append(pyxb_wall)

    elif type(element).__name__ == 'Ceiling':

        for check in element_binding.Ceiling:
            if check.building_age_group == element.building_age_group and\
               check.construction_type == element.construction_type:
                warnings.warn(warning_text)
                add_to_xml = False
                break

        if add_to_xml is True:

            pyxb_wall = tb_bind.CeilingType()
            _set_basic_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)
            pyxb_wall.Layers = tb_bind.LayersType()
            _set_layer_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)

            element_binding.Ceiling.append(pyxb_wall)

    elif type(element).__name__ == 'Floor':

        for check in element_binding.Floor:
            if check.building_age_group == element.building_age_group and\
               check.construction_type == element.construction_type:
                warnings.warn(warning_text)
                add_to_xml = False
                break

        if add_to_xml is True:

            pyxb_wall = tb_bind.FloorType()
            _set_basic_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)
            pyxb_wall.Layers = tb_bind.LayersType()
            _set_layer_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)

            element_binding.Floor.append(pyxb_wall)

    elif type(element).__name__ == 'GroundFloor':

        for check in element_binding.GroundFloor:
            if check.building_age_group == element.building_age_group and\
               check.construction_type == element.construction_type:
                warnings.warn(warning_text)
                add_to_xml = False
                break

        if add_to_xml is True:

            pyxb_wall = tb_bind.GroundFloorType()
            _set_basic_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)
            pyxb_wall.Layers = tb_bind.LayersType()
            _set_layer_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)

            element_binding.GroundFloor.append(pyxb_wall)

    elif type(element).__name__ == 'Rooftop':

        for check in element_binding.Rooftop:
            if check.building_age_group == element.building_age_group and\
               check.construction_type == element.construction_type:
                warnings.warn(warning_text)
                add_to_xml = False
                break

        if add_to_xml is True:

            pyxb_wall = tb_bind.RooftopType()
            _set_basic_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)
            pyxb_wall.Layers = tb_bind.LayersType()
            _set_layer_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)

            element_binding.Rooftop.append(pyxb_wall)

    elif type(element).__name__ == 'Window':

        for check in element_binding.Window:
            if check.building_age_group == element.building_age_group and\
               check.construction_type == element.construction_type:
                warnings.warn(warning_text)
                add_to_xml = False
                break

        if add_to_xml is True:

            pyxb_wall = tb_bind.WindowType()
            _set_basic_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)
            pyxb_wall.Layers = tb_bind.LayersType()
            _set_layer_data_pyxb(element=element,
                                 pyxb_class=pyxb_wall)

            element_binding.Window.append(pyxb_wall)

    if add_to_xml is True:

        out_file = open(utilities.get_full_path(data_class.path_tb), "w")

        out_file.write(element_binding.toDOM().toprettyxml())


def delete_type_element(element, data_class):
    """Deletes typical element.

    Deletes typical building elements according to their construction
    year and their construction type in the the XML file for type building
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

    element_binding = data_class.element_bind

    if type(element).__name__ == "OuterWall":
        for check in element_binding.OuterWall:
            if check.building_age_group == element.building_age_group and \
               check.construction_type == element.construction_type:
                element_binding.OuterWall.remove(check)
                break

    if type(element).__name__ == "Door":
        for check in element_binding.Door:
            if check.building_age_group == element.building_age_group and \
               check.construction_type == element.construction_type:
                element_binding.Door.remove(check)
                break

    elif type(element).__name__ == 'InnerWall':

        for check in element_binding.InnerWall:
            if check.building_age_group == element.building_age_group and \
                    check.construction_type == element.construction_type:
                element_binding.InnerWall.remove(check)
                break

    elif type(element).__name__ == 'Ceiling':

        for check in element_binding.Ceiling:
            if check.building_age_group == element.building_age_group and \
                    check.construction_type == element.construction_type:
                element_binding.Ceiling.remove(check)
                break

    elif type(element).__name__ == 'Floor':

        for check in element_binding.Floor:
            if check.building_age_group == element.building_age_group and \
                    check.construction_type == element.construction_type:
                element_binding.Floor.remove(check)
                break

    elif type(element).__name__ == 'GroundFloor':

        for check in element_binding.GroundFloor:
            if check.building_age_group == element.building_age_group and \
                    check.construction_type == element.construction_type:
                element_binding.GroundFloor.remove(check)
                break

    elif type(element).__name__ == 'Rooftop':

        for check in element_binding.Rooftop:
            if check.building_age_group == element.building_age_group and \
                    check.construction_type == element.construction_type:
                element_binding.Rooftop.remove(check)
                break

    elif type(element).__name__ == 'Window':

        for check in element_binding.Window:
            if check.building_age_group == element.building_age_group and \
                    check.construction_type == element.construction_type:
                element_binding.Window.remove(check)
                break

    out_file = open(utilities.get_full_path(data_class.path_tb), "w")

    out_file.write(element_binding.toDOM().toprettyxml())


def _set_basic_data_pyxb(element, pyxb_class):
    """Helper function for save_type_element to set the layer data.

    Parameters
    ----------
    pyxb_class :
        Pyxb class representation of xml
    """

    pyxb_class.building_age_group = element.building_age_group
    pyxb_class.construction_type = element.construction_type

    pyxb_class.inner_radiation = element.inner_radiation
    pyxb_class.inner_convection = element.inner_convection

    if type(element).__name__ == 'InnerWall' or \
            type(element).__name__ == 'Ceiling' or \
            type(element).__name__ == 'Floor' or \
            type(element).__name__ == 'GroundFloor':

        pass

    elif type(element).__name__ == 'Window':

        pyxb_class.outer_radiation = element.outer_radiation
        pyxb_class.outer_convection = element.outer_convection
        pyxb_class.g_value = element.g_value
        pyxb_class.a_conv = element.a_conv
        pyxb_class.shading_g_total = element.shading_g_total
        pyxb_class.shading_max_irr = element.shading_max_irr

    elif type(element).__name__ == 'OuterWall' or\
            type(element).__name__ == 'Rooftop' or\
            type(element).__name__ == 'Door':

        pyxb_class.outer_radiation = element.outer_radiation
        pyxb_class.outer_convection = element.outer_convection


def _set_layer_data_pyxb(element, pyxb_class):
    """Helper function for save_type_element to set the layer data.

    Parameters
    ----------
    pyxb_class
        pyxb class representation of xml
    """

    for layer in element.layer:

        pyxb_layer = tb_bind.layerType()

        pyxb_layer.id = layer.id
        pyxb_layer.thickness = layer.thickness
        pyxb_layer.material = layer.material.name
        pyxb_layer.material.material_id = layer.material.material_id

        pyxb_class.Layers.append(pyxb_layer)
