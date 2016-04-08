# created June 2015
# by TEASER4 Development Team

"""BuildingElement

This module contains the Base class for all building elements.
"""

from __future__ import division
from teaser.Logic.BuildingObjects.BuildingPhysics.Layer import Layer


import numpy as np
import random
import warnings
import re


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


    def add_layer(self, layer, position=None):
        '''Adds a layer at a certain position

        This function adds a Layer instance to the layer list at a given position

        Parameters
        ----------
        position : int
            position in the wall starting from 0 (inner side)

        '''
        ass_error_1 = "Layer has to be an instance of Layer()"

        assert isinstance(layer, Layer), ass_error_1

        if position is None:
            self._layer.append(layer)
        else:
            self._layer.insert(position, layer)

    def add_layer_list(self, layer_list):
        '''Appends a layer set to the layer list

        Parameters
        ----------
        layer_list : [Layer instance]
            list of sorted layer instances
        '''
        ass_error_1 = "Layer has to be an instance of Layer()"
        for lay_count in layer_list:

            assert isinstance(lay_count, Layer), ass_error_1

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

        import teaser.Data.Input.buildingelement_input as buildingelement_input

        buildingelement_input.load_type_element(element=self,
                                                year=year,
                                                construction=construction)

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

        import teaser.Data.Output.buildingelement_output as \
            buildingelement_output

        buildingelement_output.save_type_element(element=self,
                                                 path=path,
                                                 file_name=file_name)


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
            regex = re.compile('[^a-zA-z0-9]')
            self._name = regex.sub('', value)
        else:
            try:
                value = str(value)
                regex = re.compile('[^a-zA-z0-9]')
                self._name = regex.sub('', value)
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


