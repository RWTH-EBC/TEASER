#Created April 2016
#TEASER 4 Development Team

"""buildingelement_input.py

This module contains function to load building element classes
"""

from teaser.logic.buildingobjects.BuildingPhysics.Layer import Layer
from teaser.logic.buildingobjects.BuildingPhysics.Material import Material


def load_type_element(element, year, construction):
    '''Typical element loader.

    Loads typical building elements according to their construction
    year and their construction type from a XML. The elements are created by
    using IWU building characteristics combined with normative material data.

    This function will only work if the parents to Building are set.

    Parameters
    ----------
    element : BuildingElement()
        Instance of BuildingElement or inherited Element of TEASER

    year : int
        Year of construction

    construction : str
        Construction type, code list ('heavy', 'light')

    Raises
    ----------
    Assert if parents to Building are not set
    '''

    ass_error_1 = "You need to specify parents for element and thermalzone"

    assert element.parent.parent.parent is not None, ass_error_1

    element.year_of_construction = year

    if type(element).__name__ == 'OuterWall':

        for out_wall in element.parent.parent.parent.\
                data.element_bind.OuterWall:
            if out_wall.building_age_group[0] <= year <= \
                    out_wall.building_age_group[1] and \
                    out_wall.construction_type == construction:
                _set_basic_data(element=element,
                                pyxb_class=out_wall)
                for pyxb_layer in out_wall.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(element=element,
                                    material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer)

    elif type(element).__name__ == 'InnerWall':

        for in_wall in element.parent.parent.\
                parent.data.element_bind.InnerWall:
            if in_wall.building_age_group[0] <= year <= \
                    in_wall.building_age_group[1] and \
                    in_wall.construction_type == construction:
                _set_basic_data(element=element,
                                pyxb_class=in_wall)
                for pyxb_layer in in_wall.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(element=element,
                                    material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer)

    elif type(element).__name__ == 'Floor':

        for floor in element.parent.parent.parent.data.element_bind.Floor:
            if floor.building_age_group[0] <= year <= \
                    floor.building_age_group[1] and \
                    floor.construction_type == construction:
                _set_basic_data(element=element,
                                pyxb_class=floor)
                for pyxb_layer in floor.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(element=element,
                                    material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer)

    elif type(element).__name__ == 'Ceiling':

        for ceiling in element.parent.parent.\
                parent.data.element_bind.Ceiling:
            if ceiling.building_age_group[0] <= year <= \
                    ceiling.building_age_group[1] and \
                    ceiling.construction_type == construction:
                _set_basic_data(element=element,
                                pyxb_class=ceiling)
                for pyxb_layer in ceiling.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(element=element,
                                    material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer)

    elif type(element).__name__ == 'GroundFloor':

        for gr_floor in element.parent.parent.\
                parent.data.element_bind.GroundFloor:
            if gr_floor.building_age_group[0] <= year <= \
                    gr_floor.building_age_group[1] and \
                    gr_floor.construction_type == construction:
                _set_basic_data(element=element,
                                pyxb_class=gr_floor)
                for pyxb_layer in gr_floor.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(element=element,
                                    material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer)

    elif type(element).__name__ == 'Rooftop':

        for roof in element.parent.parent.parent.data.element_bind.Rooftop:
            if roof.building_age_group[0] <= year <= \
                    roof.building_age_group[1] and \
                    roof.construction_type == construction:
                _set_basic_data(element=element,
                                pyxb_class=roof)
                for pyxb_layer in roof.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(element=element,
                                    material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer)

    elif type(element).__name__ == 'Window':

        for win in element.parent.parent.parent.data.element_bind.Window:
            if win.building_age_group[0] <= year <= \
                    win.building_age_group[1] and win.construction_type == \
                    construction:
                _set_basic_data(element=element,
                                pyxb_class=win)
                for pyxb_layer in win.Layers.layer:

                    layer = Layer(element)
                    material = Material(layer)
                    _set_layer_data(element=element,
                                    material=material,
                                    layer=layer,
                                    pyxb_class=pyxb_layer)

def _set_layer_data(element, material, layer, pyxb_class):
    '''Helper function for load_type_element to set the layer data.

    Parameters
    ----------
    material : Material()
        Material() instance of TEASER

    layer : Layer()
        Layer() instance of TEASER

    pyxb_class :
        Pyxb class represantation of xml
    '''

    layer.thickness = pyxb_class.thickness
    layer.id = pyxb_class.id

    material.name = pyxb_class.Material.name
    material.density = pyxb_class.Material.density
    material.thermal_conduc = pyxb_class.Material.thermal_conduc
    material.heat_capac = pyxb_class.Material.heat_capac
    if pyxb_class.Material.solar_absorp is not None:
        material.solar_absorp = pyxb_class.Material.solar_absorp
    if pyxb_class.Material.ir_emissivity is not None:
        material.ir_emissivity = pyxb_class.Material.ir_emissivity

def _set_basic_data(element, pyxb_class):
    '''Helper function for load_type_element to set the layer data.

    Parameters
    ----------
    pyxb_class :
        Pyxb class represantation of xml
    '''

    element.building_age_group = pyxb_class.building_age_group
    element.construction_type = pyxb_class.construction_type
    element.inner_radiation = pyxb_class.inner_radiation
    element.inner_convection = pyxb_class.inner_convection

    if type(element).__name__ == 'OuterWall' or \
            type(element).__name__ == 'Rooftop':
        element.inner_radiation = pyxb_class.inner_radiation
        element.inner_convection = pyxb_class.inner_convection
        element.outer_radiation = pyxb_class.outer_radiation
        element.outer_convection = pyxb_class.outer_convection

    elif type(element).__name__ == 'InnerWall' or \
            type(element).__name__ == 'Ceiling' or \
            type(element).__name__ == 'Floor' or \
            type(element).__name__ == 'GroundFloor':

        pass

    elif type(element).__name__ == 'Window':

        element.outer_radiation = pyxb_class.outer_radiation
        element.outer_convection = pyxb_class.outer_convection
        element.g_value = pyxb_class.g_value
        element.a_conv = pyxb_class.a_conv
        element.shading_g_total = pyxb_class.shading_g_total
        element.shading_max_irr = pyxb_class.shading_max_irr