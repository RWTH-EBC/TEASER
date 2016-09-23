#Created April 2016
#TEASER 4 Development Team

"""buildingelement_ouput.py

This module contains function to save building element classes
"""

import teaser.data.bindings.v_0_3_9.typeelement_bind as tb_bind
import teaser.logic.utilities as utilitis
import warnings


def save_type_element(element, path=None, file_name=None):
    '''Typical element saver.

    Saves typical building elements according to their construction
    year and their construction type in the the XML file for type buidling
    elements. If the Project parent is set, it automatically saves it to
    the file given in Project.data. Alternatively you can specify a path to
    a file of TypeBuildingElements. If this file does not exist,
    a new file is created.

    Parameters
    ----------

    element : BuildingElement()
        Instance of BuildingElement or inherited Element of TEASER

    path : str
        path where unique file should be stored
    name : strt
        name of of unique file

    '''

    if element.parent is not None:
        path = element.parent.parent.parent.data.path_tb
        xml_parse = element.parent.parent.parent.data.element_bind
    else:
        path = path + "/" + file_name + ".xml"
        try:
            xml_file = open(utilitis.get_full_path(path))
            xml_parse = tb_bind.CreateFromDocument(xml_file.read())
        except:
            xml_parse = tb_bind.TypeBuildingElements()
    xml_parse.version = "0.3.9"
    add_to_xml = True
    warning_text = ("Construction Type and building age "
                    "group already exist in this XML, consider revising "
                    "your inputs. The Element is NOT saved into XML")
    if type(element).__name__ == "OuterWall":

        for check in xml_parse.OuterWall:
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


            xml_parse.OuterWall.append(pyxb_wall)

    elif type(element).__name__ == 'InnerWall':

        for check in xml_parse.InnerWall:
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

            xml_parse.InnerWall.append(pyxb_wall)

    elif type(element).__name__ == 'Ceiling':

        for check in xml_parse.Ceiling:
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

            xml_parse.Ceiling.append(pyxb_wall)

    elif type(element).__name__ == 'Floor':

        for check in xml_parse.Floor:
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

            xml_parse.Floor.append(pyxb_wall)

    elif type(element).__name__ == 'GroundFloor':

        for check in xml_parse.GroundFloor:
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

            xml_parse.GroundFloor.append(pyxb_wall)

    elif type(element).__name__ == 'Rooftop':

        for check in xml_parse.Rooftop:
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

            xml_parse.Rooftop.append(pyxb_wall)

    elif type(element).__name__ == 'Window':

        for check in xml_parse.Window:
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

            xml_parse.Window.append(pyxb_wall)

    if add_to_xml is True:

        out_file = open(utilitis.get_full_path(path),"w")

        out_file.write(xml_parse.toDOM().toprettyxml())

def _set_basic_data_pyxb(element, pyxb_class):
    '''Helper function for save_type_element to set the layer data.

    Parameters
    ----------
    pyxb_class :
        Pyxb class represantation of xml
    '''

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
            type(element).__name__ == 'Rooftop':

        pyxb_class.outer_radiation = element.outer_radiation
        pyxb_class.outer_convection = element.outer_convection

def _set_layer_data_pyxb(element, pyxb_class):
    '''Helper function for save_type_element to set the layer data.

    Parameters
    ----------
    pyxb_class
        pyxb class represantation of xml
    '''

    for layer in element.layer:

        pyxb_layer = tb_bind.layerType()

        pyxb_layer.id = layer.id
        pyxb_layer.thickness = layer.thickness

        pyxb_material = tb_bind.MaterialType()

        pyxb_material.name = layer.material.name
        pyxb_material.density = layer.material.density
        pyxb_material.thermal_conduc = layer.material.thermal_conduc
        pyxb_material.heat_capac = layer.material.heat_capac
        pyxb_material.solar_absorp = layer.material.solar_absorp
        pyxb_material.ir_emissivity = layer.material.ir_emissivity

        pyxb_layer.Material = pyxb_material

        pyxb_class.Layers.append(pyxb_layer)
