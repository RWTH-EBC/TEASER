# created June 2015
# by TEASER4 Development Team

"""BuildingElement

This module contains the Base class for all building elements.
"""

from __future__ import division
from teaser.Logic.BuildingObjects.BuildingPhysics.Layer import Layer
from teaser.Logic.BuildingObjects.BuildingPhysics.Material import Material
import teaser.Data.SchemaBindings.TypeBuildingBind as tb_bind
import teaser.Logic.Utilis as utilis

import numpy as np
import random
import warnings


class BuildingElement(object):

    '''Building element class.

    This is the base class for all building elements.

    Parameters
    ----------

    parent : ThermalZone()
        The parent class of this object, the ThermalZone the BE belongs to.
        Allows for better control of hierarchical structures.
        Default is None.

    Note
    ----------

    The listed attributes are just the ones that are set by the user Calculated
    values are not included in this list


    Attributes
    ----------


    internal_id : float
        Random id for the destinction between different elements

    name : str
        Individual name

    construction_type : str
        Type of construction ("heavy" or "light")

    year_of_refurbishment : int
        Year of refurbishment

    year_of_construction : int
        Year of first construction

    area : float
        Area of building element

    tilt : float
        Tilt against horizontal

    orientation : float
        Compass direction of building element (0 : north, 90: est, 180: south,
        270: west)

    inner_convection : float
        Constant heat transfer coefficient of convection inner side

    inner_radiation : float
        Constant heat transfer coefficient of radiation inner side

    outer_convection : float
        Constant heat transfer coefficient of convection outer side
        for inner walls and ground floor zero

    outer_radiation : float
        Constant heat transfer coefficient of radiation outer side
        for inner walls and ground floor zero

    layer : list
        List of all layers of a building element (to be filled with Layer
        objects). Use element.layer = None to delete all layers of the building
        element

    Raises
    ----------
    None
    '''

    def __init__(self, parent=None):
        '''Constructor for Thermal zone

        '''

        self.internal_id = random.random()

        self.name = None
        self._construction_type = None
        self._year_of_retrofit = None
        self._year_of_construction = None
        self.building_age_group = [None, None]

        self._area = None
        self._tilt = None
        self._orientation = None
        self._inner_convection = None
        self._inner_radiation = None
        self._outer_convection = None
        self._outer_radiation = None

        self._layer = []

        #values for the AixLib Export
        self.emissivity = 0.0   # Should we use the ir_emissivity here?
                                # Better use in the thermal zone i think
        self.parent = parent

        # Calculated values for each Building Element
        self.r1 = 0.0
        self.r2 = 0.0
        self.r3 = 0.0
        self.c1 = 0.0
        self.c2 = 0.0
        self.c1_korr = 0.0
        self.ua_value = 0.0
        self.r_conduc = 0.0
        self.r_inner_conv = 0.0
        self.r_inner_rad = 0.0
        self.r_inner_comb = 0.0
        self.r_outer_conv = 0.0
        self.r_outer_rad = 0.0
        self.r_outer_comb = 0.0

    def calc_ua_value(self):
        '''U*A value for building element.

        Calculates the U*A value and thermal resistances of a building element.
        '''

        self.ua_value = 0.0
        self.r_conduc = 0.0
        self.r_inner_conv = 0.0
        self.r_inner_rad = 0.0
        self.r_inner_comb = 0.0
        self.r_outer_conv = 0.0
        self.r_outer_rad = 0.0
        self.r_outer_comb = 0.0

        for count_layer in self.layer:
            self.r_conduc += (count_layer.thickness /
                              count_layer.material.thermal_conduc)

        self.r_inner_conv = (1 / self.inner_convection) * (1 / self.area)
        self.r_inner_rad = (1 / self.inner_radiation) * (1 / self.area)
        self.r_inner_comb = 1 / (1 / self.r_inner_conv + 1 / self.r_inner_rad)

        if self.outer_convection is not None \
                and self.outer_radiation is not None:

            self.r_outer_conv = (1 / self.outer_convection) * (1 / self.area)
            self.r_outer_rad = (1 / self.outer_radiation) * (1 / self.area)
            self.r_outer_comb = 1 / \
                (1 / self.r_outer_conv + 1 / self.r_outer_rad)

        self.ua_value = (1 / (self.r_inner_comb + self.r_conduc *
                              (1 / self.area) + self.r_outer_comb))

    def gather_element_properties(self):
        '''Helper function for matrix calculation.

        Gathers all material properties of the building element and returns
        them as a np.array. Needed for the calculation of the matrix in
        equivalent_res(t_bt) especially for walls.

        Returns
        ----------
        np.number_of_layer
        np.density
        np.thermal_conduc
        np.heat_capac
        np.thickness
        '''

        number_of_layer = len(self.layer)
        density = np.zeros(number_of_layer)
        thermal_conduc = np.zeros(number_of_layer)
        heat_capac = np.zeros(number_of_layer)
        thickness = np.zeros(number_of_layer)

        for i in range(number_of_layer):

            density[i] = self.layer[i].material.density
            thermal_conduc[i] = self.layer[i].material.thermal_conduc
            heat_capac[i] = self.layer[i].material.heat_capac
            thickness[i] = self.layer[i].thickness

        return number_of_layer, density, thermal_conduc, heat_capac, thickness


    def add_layer(self, position, layer):
        '''Adds a layer at a certain position

        This function adds a Layer instance to the layer list at a given position

        Parameters
        ----------
        position : int
            position in the wall starting from 0 (inner side)

        '''

        self._layer.insert(position, layer)

    def add_layer_list(self, layer_list):
        '''Appends a layer set to the layer list

        Parameters
        ----------
        layer_list : [Layer instance]
            list of sorted layer instances
        '''
        for lay_count in layer_list:
            self._layer.append(lay_count)



    def load_type_element(self, year, construction):
        '''Typical element loader.

        Loads typical building elements according to their construction
        year and their construction type from a XML.

        This function will only work if the parents to Building are set.

        Parameters
        ----------
        year : int
            Year of construction

        construction : str
            Construction type, code list ('heavy', 'light')

        Raises
        ----------
        Assert if parents to Building are not set
        '''

        ass_error_1 = "You need to specify parents for element and thermalzone"

        assert self.parent.parent.parent is not None, ass_error_1

        self.year_of_construction = year

        if type(self).__name__ == 'OuterWall':

            for out_wall in self.parent.parent.parent.\
                    data.element_bind.OuterWall:
                if out_wall.building_age_group[0] <= year and \
                    year <= out_wall.building_age_group[1] and \
                        out_wall.construction_type == construction:
                    self.set_basic_data(out_wall)
                    for pyxb_layer in out_wall.Layers.layer:

                        layer = Layer(self)
                        material = Material(layer)
                        self.set_layer_data(material, layer, pyxb_layer)

        elif type(self).__name__ == 'InnerWall':

            for in_wall in self.parent.parent.\
                    parent.data.element_bind.InnerWall:
                if in_wall.building_age_group[0] <= year and \
                    year <= in_wall.building_age_group[1] and \
                        in_wall.construction_type == construction:
                    self.set_basic_data(in_wall)
                    for pyxb_layer in in_wall.Layers.layer:

                        layer = Layer(self)
                        material = Material(layer)
                        self.set_layer_data(material, layer, pyxb_layer)

        elif type(self).__name__ == 'Floor':

            for floor in self.parent.parent.parent.data.element_bind.Floor:
                if floor.building_age_group[0] <= year and \
                    year <= floor.building_age_group[1] and \
                        floor.construction_type == construction:
                    self.set_basic_data(floor)
                    for pyxb_layer in floor.Layers.layer:

                        layer = Layer(self)
                        material = Material(layer)
                        self.set_layer_data(material, layer, pyxb_layer)

        elif type(self).__name__ == 'Ceiling':

            for ceiling in self.parent.parent.\
                    parent.data.element_bind.Ceiling:
                if ceiling.building_age_group[0] <= year and \
                    year <= ceiling.building_age_group[1] and \
                        ceiling.construction_type == construction:
                    self.set_basic_data(ceiling)
                    for pyxb_layer in ceiling.Layers.layer:

                        layer = Layer(self)
                        material = Material(layer)
                        self.set_layer_data(material, layer, pyxb_layer)

        elif type(self).__name__ == 'GroundFloor':

            for gr_floor in self.parent.parent.\
                    parent.data.element_bind.GroundFloor:
                if gr_floor.building_age_group[0] <= year and \
                    year <= gr_floor.building_age_group[1] and \
                        gr_floor.construction_type == construction:
                    self.set_basic_data(gr_floor)
                    for pyxb_layer in gr_floor.Layers.layer:

                        layer = Layer(self)
                        material = Material(layer)
                        self.set_layer_data(material, layer, pyxb_layer)

        elif type(self).__name__ == 'Rooftop':

            for roof in self.parent.parent.parent.data.element_bind.Rooftop:
                if roof.building_age_group[0] <= year and \
                    year <= roof.building_age_group[1] and \
                        roof.construction_type == construction:
                    self.set_basic_data(roof)
                    for pyxb_layer in roof.Layers.layer:

                        layer = Layer(self)
                        material = Material(layer)
                        self.set_layer_data(material, layer, pyxb_layer)

        elif type(self).__name__ == 'Window':

            for win in self.parent.parent.parent.data.element_bind.Window:
                if win.building_age_group[0] <= year and \
                    year <= win.building_age_group[1] and \
                        win.construction_type == construction:
                    self.set_basic_data(win)
                    for pyxb_layer in win.Layers.layer:

                        layer = Layer(self)
                        material = Material(layer)
                        self.set_layer_data(material, layer, pyxb_layer)

    def set_layer_data(self, material, layer, pyxb_class):
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

    def set_basic_data(self, pyxb_class):
        '''Helper function for load_type_element to set the layer data.

        Parameters
        ----------
        pyxb_class :
            Pyxb class represantation of xml
        '''

        self.building_age_group = pyxb_class.building_age_group
        self.construction_type = pyxb_class.construction_type
        self.inner_radiation = pyxb_class.inner_radiation
        self.inner_convection = pyxb_class.inner_convection

        if type(self).__name__ == 'OuterWall' or \
                type(self).__name__ == 'Rooftop':
            self.inner_radiation = pyxb_class.inner_radiation
            self.inner_convection = pyxb_class.inner_convection
            self.outer_radiation = pyxb_class.outer_radiation
            self.outer_convection = pyxb_class.outer_convection

        elif type(self).__name__ == 'InnerWall' or \
                type(self).__name__ == 'Ceiling' or \
                type(self).__name__ == 'Floor' or \
                type(self).__name__ == 'GroundFloor':

            pass

        elif type(self).__name__ == 'Window':

            self.outer_radiation = pyxb_class.outer_radiation
            self.outer_convection = pyxb_class.outer_convection
            self.g_value = pyxb_class.g_value
            self.a_conv = pyxb_class.a_conv
            self.shading_g_total = pyxb_class.shading_g_total
            self.shading_max_irr = pyxb_class.shading_max_irr

    def save_type_element(self, path=None, file_name=None):
        '''Typical element saver.

        Saves typical building elements according to their construction
        year and their construction type in the the XML file for type buidling
        elements. If the Project parent is set, it automatically saves it to
        the file given in Project.data. Alternatively you can specify a path to
        a file of TypeBuildingElements. If this file does not exist,
        a new file is created.

        Parameters
        ----------

        path : str
            path where unique file should be stored
        name : strt
            name of of unique file

        '''

        if self.parent is not None:
            path = self.parent.parent.parent.data.path_tb
            xml_parse = self.parent.parent.parent.data.element_bind
        else:
            path = path + "\\" + file_name + ".xml"
            try:
                xml_file = open(utilis.get_full_path(path))
                xml_parse = tb_bind.CreateFromDocument(xml_file.read())
            except:
                xml_parse = tb_bind.TypeBuildingElements()

        add_to_xml = True
        warning_text = ("Construction Type and building age "
                        "group already exist in this XML, consider revising "
                        "your inputs. The Element is NOT saved into XML")
        if type(self).__name__ == "OuterWall":

            for check in xml_parse.OuterWall:
                if check.building_age_group == self.building_age_group and\
                   check.construction_type == self.construction_type:
                    warnings.warn(warning_text)
                    add_to_xml = False
                    break

            if add_to_xml is True:

                pyxb_wall = tb_bind.OuterWallType()
                self.set_basic_data_pyxb(pyxb_wall)
                pyxb_wall.Layers = tb_bind.LayersType()
                self.set_layer_data_pyxb(pyxb_wall)

                xml_parse.OuterWall.append(pyxb_wall)

        elif type(self).__name__ == 'InnerWall':

            for check in xml_parse.InnerWall:
                if check.building_age_group == self.building_age_group and\
                   check.construction_type == self.construction_type:
                    warnings.warn(warning_text)
                    add_to_xml = False
                    break

            if add_to_xml is True:

                pyxb_wall = tb_bind.InnerWallType()
                self.set_basic_data_pyxb(pyxb_wall)
                pyxb_wall.Layers = tb_bind.LayersType()
                self.set_layer_data_pyxb(pyxb_wall)

                xml_parse.InnerWall.append(pyxb_wall)

        elif type(self).__name__ == 'Ceiling':

            for check in xml_parse.Ceiling:
                if check.building_age_group == self.building_age_group and\
                   check.construction_type == self.construction_type:
                    warnings.warn(warning_text)
                    add_to_xml = False
                    break

            if add_to_xml is True:

                pyxb_wall = tb_bind.CeilingType()
                self.set_basic_data_pyxb(pyxb_wall)
                pyxb_wall.Layers = tb_bind.LayersType()
                self.set_layer_data_pyxb(pyxb_wall)

                xml_parse.Ceiling.append(pyxb_wall)

        elif type(self).__name__ == 'Floor':

            for check in xml_parse.Floor:
                if check.building_age_group == self.building_age_group and\
                   check.construction_type == self.construction_type:
                    warnings.warn(warning_text)
                    add_to_xml = False
                    break

            if add_to_xml is True:

                pyxb_wall = tb_bind.FloorType()
                self.set_basic_data_pyxb(pyxb_wall)
                pyxb_wall.Layers = tb_bind.LayersType()
                self.set_layer_data_pyxb(pyxb_wall)

                xml_parse.Floor.append(pyxb_wall)

        elif type(self).__name__ == 'GroundFloor':

            for check in xml_parse.GroundFloor:
                if check.building_age_group == self.building_age_group and\
                   check.construction_type == self.construction_type:
                    warnings.warn(warning_text)
                    add_to_xml = False
                    break

            if add_to_xml is True:

                pyxb_wall = tb_bind.GroundFloorType()
                self.set_basic_data_pyxb(pyxb_wall)
                pyxb_wall.Layers = tb_bind.LayersType()
                self.set_layer_data_pyxb(pyxb_wall)

                xml_parse.GroundFloor.append(pyxb_wall)

        elif type(self).__name__ == 'Rooftop':

            for check in xml_parse.Rooftop:
                if check.building_age_group == self.building_age_group and\
                   check.construction_type == self.construction_type:
                    warnings.warn(warning_text)
                    add_to_xml = False
                    break

            if add_to_xml is True:

                pyxb_wall = tb_bind.RooftopType()
                self.set_basic_data_pyxb(pyxb_wall)
                pyxb_wall.Layers = tb_bind.LayersType()
                self.set_layer_data_pyxb(pyxb_wall)

                xml_parse.Rooftop.append(pyxb_wall)

        elif type(self).__name__ == 'Window':

            for check in xml_parse.Window:
                if check.building_age_group == self.building_age_group and\
                   check.construction_type == self.construction_type:
                    warnings.warn(warning_text)
                    add_to_xml = False
                    break

            if add_to_xml is True:

                pyxb_wall = tb_bind.WindowType()
                self.set_basic_data_pyxb(pyxb_wall)
                pyxb_wall.Layers = tb_bind.LayersType()
                self.set_layer_data_pyxb(pyxb_wall)

                xml_parse.Window.append(pyxb_wall)

        if add_to_xml is True:

            out_file = open(utilis.get_full_path(path),"w")

            out_file.write(xml_parse.toDOM().toprettyxml())

    def set_basic_data_pyxb(self, pyxb_class):
        '''Helper function for save_type_element to set the layer data.

        Parameters
        ----------
        pyxb_class :
            Pyxb class represantation of xml
        '''

        pyxb_class.building_age_group = self.building_age_group
        pyxb_class.construction_type = self.construction_type

        pyxb_class.inner_radiation = self.inner_radiation
        pyxb_class.inner_convection = self.inner_convection

        if type(self).__name__ == 'InnerWall' or \
                type(self).__name__ == 'Ceiling' or \
                type(self).__name__ == 'Floor' or \
                type(self).__name__ == 'GroundFloor':

            pass

        elif type(self).__name__ == 'Window':

            pyxb_class.outer_radiation = self.outer_radiation
            pyxb_class.outer_convection = self.outer_convection
            pyxb_class.g_value = self.g_value
            pyxb_class.a_conv = self.a_conv
            pyxb_class.shading_g_total = self.shading_g_total
            pyxb_class.shading_max_irr = self.shading_max_irr

        elif type(self).__name__ == 'OuterWall' or\
                type(self).__name__ == 'Rooftop':

            pyxb_class.outer_radiation = self.outer_radiation
            pyxb_class.outer_convection = self.outer_convection

    def set_layer_data_pyxb(self, pyxb_class):
        '''Helper function for save_type_element to set the layer data.

        Parameters
        ----------
        pyxb_class
            pyxb class represantation of xml
        '''

        for layer in self.layer:

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

    def set_calc_default(self):
        '''Sets all calculated values of the Building Element to zero
        '''
        self.r1 = 0.0
        self.r2 = 0.0
        self.r3 = 0.0
        self.c1 = 0.0
        self.c2 = 0.0
        self.c1_korr = 0.0
        self.ua_value = 0.0
        self.r_conduc = 0.0
        self.r_inner_conv = 0.0
        self.r_inner_rad = 0.0
        self.r_inner_comb = 0.0
        self.r_outer_conv = 0.0
        self.r_outer_rad = 0.0
        self.r_outer_comb = 0.0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):

            self._name = value.replace(" ", "")
        else:
            try:
                value = str(value)
                self._name = value.replace(" ", "")

            except ValueError:
                print("Can't convert name to string")

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        if value is not None:

            ass_error_1 = "Parent has to be an instance of ThermalZone()"

            assert type(value).__name__ == "ThermalZone", ass_error_1

            self.__parent = value

            if type(self).__name__ == "OuterWall" \
                    or type(self).__name__ == "Rooftop" \
                    or type(self).__name__ == "GroundFloor":
                self.__parent.outer_walls.append(self)
            if type(self).__name__ == "InnerWall" \
                    or type(self).__name__ == "Ceiling" \
                    or type(self).__name__ == "Floor":
                self.__parent.inner_walls.append(self)
            if type(self).__name__ == "Window":
                self.__parent.windows.append(self)

            if self.parent.parent is not None:
                self.year_of_construction = \
                    self.parent.parent.year_of_construction
            else:
                pass
        else:

            self.__parent = None

    @property
    def year_of_retrofit(self):
        return self._year_of_retrofit

    @year_of_retrofit.setter
    def year_of_retrofit(self, value):
        
        if isinstance(value, int):
            pass
        elif value is None:
            pass
        else:
            try:
                value = int(value)
            except:
                raise ValueError("Can't convert year of retrofit to float")
                
        if value is not None:
            if self.year_of_construction is not None:
                self._year_of_retrofit = value
            else:
                raise ValueError("Specify year of construction first")


    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        """
        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert orientation to float")        
        """
        self._orientation = value
        if type(self).__name__ == "OuterWall":
            if self.parent.parent is not None and self.area is not None:
                self.parent.parent.fill_outer_area_dict()
        elif type(self).__name__ == "Window":
            if self.parent.parent is not None and self.area is not None:
                self.parent.parent.fill_window_area_dict()

    @property
    def layer(self):
        return self._layer

    @layer.setter
    def layer(self, value):

        if value is None:
            self._layer = []
        else:
            ass_error_1 = "Value has to be an instance of Layer()"

            assert isinstance(value, Layer), ass_error_1

        if self.inner_convection is not None and\
                self.inner_radiation is not None and\
                self.area is not None:
            self.calc_ua_value()

    @property
    def inner_convection(self):
        return self._inner_convection

    @inner_convection.setter
    def inner_convection(self, value):
        
        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert inner convection to float")

        if value is not None:
            self._inner_convection = value
        if self.inner_convection is not None and\
                self.inner_radiation is not None and\
                self.area is not None:
            self.calc_ua_value()

    @property
    def inner_radiation(self):
        return self._inner_radiation

    @inner_radiation.setter
    def inner_radiation(self, value):
        

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert inner radiation to float")

        if value is not None:
            self._inner_radiation = value
        if self.inner_convection is not None and\
                self.inner_radiation is not None and\
                self.area is not None:
            self.calc_ua_value()

    @property
    def outer_convection(self):
        return self._outer_convection

    @outer_convection.setter
    def outer_convection(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert outer convection to float")

        if value is not None:
            self._outer_convection = value
        if self.inner_convection is not None and\
                self.inner_radiation is not None and\
                self.area is not None:
            self.calc_ua_value()

    @property
    def outer_radiation(self):
        return self._outer_radiation

    @outer_radiation.setter
    def outer_radiation(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert outer radiation to float")

        if value is not None:
            self._outer_radiation = value
        if self.inner_convection is not None and\
                self.inner_radiation is not None and\
                self.area is not None:
            self.calc_ua_value()

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert element area to float")   
        
        if value is not None:
            self._area = value
        if type(self).__name__ == "OuterWall"\
                    or type(self).__name__ == "Rooftop" \
                    or type(self).__name__ == "GroundFloor":
            if self.parent.parent is not None and self.orientation is not None:
                self.parent.parent.fill_outer_area_dict()
        elif type(self).__name__ == "Window":
            if self.parent.parent is not None and self.orientation is not None:
                self.parent.parent.fill_window_area_dict()
        if self.inner_convection is not None and\
                self.inner_radiation is not None and\
                self.area is not None:
            self.calc_ua_value()

    @property
    def tilt(self):        
        return self._tilt

    @tilt.setter
    def tilt(self, value):

        if isinstance(value, float):
            self._tilt = value
        elif value is None:
            self._tilt = value
        else:
            try:
                value = float(value)
                self._tilt = value
            except:
                raise ValueError("Can't convert tilt to float")
                
    @property
    def year_of_construction(self):        
        return self._year_of_construction

    @year_of_construction.setter
    def year_of_construction(self, value):

        if isinstance(value, float):
            self._year_of_construction = value
        elif value is None:
            self._year_of_construction = value
        else:
            try:
                value = int(value)
                self._year_of_construction = value
            except:
                raise ValueError("Can't convert year to int")


    @property
    def construction_type(self):
        return self._construction_type

    @construction_type.setter
    def construction_type(self, value):

        self._construction_type = value


