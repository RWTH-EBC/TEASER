# created June 2015
# by TEASER4 Development Team

from __future__ import division
import math
import random
import warnings
import re
from teaser.logic.buildingobjects.calculation.two_element import TwoElement

class ThermalZone(object):
    """This class represents a Thermal Zone in a building


    Parameters
    ----------
    parent: Building()
        The parent class of this object, the Building the zone belongs to.
        Allows for better control of hierarchical structures.
        Default is None

    Note
    ----------

    The listed attributes are just the ones that are set by the user Calculated
    values are not included in this list

    Attributes
    ----------

    internal_id : float
        Random id for the distinction between different zones.
    name : str
        Individual name.
    area : float [m2]
        Thermal zone area.
    volume : float [m3]
        Thermal zone volume.
    infiltration_rate : float [1/h]
        Infiltration rate of zone.
    outer_walls : list
        List of OuterWall instances.
    rooftops : list
        List of Rooftop instances.
    groundfloors : list
        List of GroundFloor instances.
    windows : list
        List of Window instances.
    inner_walls : list
        List of InnerWall instances.
    floors : list
        List of Floor instances.
    ceilings: list
        List of Ceiling instances.
    use_conditions : instance of UseConditions()
        Instance of UseConditions with all relevant information for the usage
        of the thermal zone
    calc_attr : instance of OneElement(), TwoElement(), ThreeElement() or
                FourElement()
        Instance of OneElement(), TwoElement(), ThreeElement() or
        FourElement(), that holds all calculation functions and attributes
        needed for the specific model.

    typical_length : list
        normative typical length of the thermal zone
    typical_width : list
        normative typical width of the thermal zone
    t_inside : float
        normative indoor temperature for static heat load calculation.
        The input of t_inside is ALWAYS in Kelvin
    t_outside : float
        normative outdoor temperature for static heat load calculation.
        The input of t_inside is ALWAYS in Kelvin
    t_ground : float
        slab temperature directly at the outer side of ground floors.
        The input of t_ground is ALWAYS in Kelvin
    density_air : float
        average density of the air in the thermal zone
    heat_capac_air : float
        average heat capacity of the air in the thermal zone
    """

    def __init__(self, parent=None):
        """Constructor for ThermalZone

        """

        self.parent = parent

        self.internal_id = random.random()
        self.name = None
        self._area = None
        self._volume = None
        self._infiltration_rate = 0.5 # TODO is this value actually used?
        self._outer_walls = []
        self.rooftops = []
        self.ground_floors = []
        self._windows = []
        self._inner_walls = []
        self.floors = []
        self.ceilings = []
        self._use_conditions = None
        self.calc_attr = None
        self.typical_length = None # TODO move this to use conditions?
        self.typical_width = None
        self._t_inside = 293.15
        self._t_outside = 261.15
        self.density_air = 1.19  # only export for now
        self.heat_capac_air = 1007  # only export for now
        self.t_ground = 286.15  # Move this to building module?


    def calc_zone_parameters(self,
                             number_of_elements=2,
                             merge_windows=False,
                             t_bt=5):
        """RC-Calculation for the thermal zone

        This functions calculates and sets all necessary parameters for the
        zone. The method distinguishes between the number of elements,
        we distinguish between:
            - one element: all walls are aggregated into one element
            - two elements: exterior and interior walls are aggregated
            - three elements: like 2, but floor are aggregated separately
            - four elements: like 3 bit roofs are aggregated separately

        For all four options we can chose if the thermal conduction through
        the window is considered in a separate resistance or not.

        Parameters
        ----------
        number_of_elements : int
            defines the number of elements, that area aggregated, between 1
            and 4, default is 2

        merge_windows : bool
            True for merging the windows into the outer walls, False for
            separate resistance for window, default is False

        t_bt : int
            Time constant according to VDI 6007 (default t_bt = 5)
        """

        if number_of_elements == 1:
            pass
        elif number_of_elements == 2:
            self.calc_attr = TwoElement(
                thermal_zone=self,
                merge_windows=merge_windows,
                t_bt=t_bt)
        elif number_of_elements == 3:
            pass
        elif number_of_elements == 4:
            pass
        self.calc_heat_load(number_of_elements=number_of_elements)

    def find_walls(self, orientation, tilt):
        """
        this function returns a list of all wall elemnts with the same
        orientation and tilt to sum them in the building
        """
        located = []
        for i in self.outer_walls:
            if i.orientation == orientation and i.tilt == tilt:
                located.append(i)
            else:
                pass
        return located

    def find_rts(self, orientation, tilt):
        """
        this function returns a list of all wall elemnts with the same
        orientation and tilt to sum them in the building
        """
        located = []
        for i in self.rooftops:
            if i.orientation == orientation and i.tilt == tilt:
                located.append(i)
            else:
                pass
        return located


    def find_gfs(self, orientation, tilt):
        """
        this function returns a list of all wall elemnts with the same
        orientation and tilt to sum them in the building
        """
        located = []
        for i in self.ground_floors:
            if i.orientation == orientation and i.tilt == tilt:
                located.append(i)
            else:
                pass
        return located

    def find_wins(self, orientation, tilt):
        """
        this function returns a list of all window elemnts with the same
        orientation and tilt to sum them in the building
        """
        located = []
        for i in self.windows:
            if i.orientation == orientation and i.tilt == tilt:
                located.append(i)
            else:
                pass
        return located

    def set_inner_wall_area(self):
        """Sets the inner wall area.

        Sets the inner wall area according to zone area size if type building
        approach is used.
        """

        ass_error_1 = "You need to specify parent for thermal zone"

        assert self.parent is not None, ass_error_1

        for floor in self.floors:
            floor.area = ((self.parent.number_of_floors - 1) /
                         self.parent.number_of_floors) * self.area
        for ceiling in self.ceilings:
            ceiling.area = ((self.parent.number_of_floors - 1) /
                          self.parent.number_of_floors) * self.area

        for wall in self.inner_walls:
            typical_area = self.typical_length * self.typical_width

            avg_room_nr = self.area / typical_area

            wall.area = (avg_room_nr * (self.typical_length *
                                        self.parent.height_of_floors +
                                        2 * self.typical_width *
                                        self.parent.height_of_floors))

    def set_volume_zone(self):
        """Sets the zone volume.

        Sets the volume of a zone according area and height of floors
        (building attribute).
        """

        ass_error_1 = "you need to specify parent for thermal zone"

        assert self.parent is not None, ass_error_1

        self.volume = self.area * self.parent.height_of_floors
        """
        if len(self.parent.thermal_zones) == 1:
            self.volume = self.area * self.parent.height_of_floors
        else:
            if self.typical_length == None \
                and self.typical_width == None:
                self.volume = self.area * self.parent.height_of_floors
            else:
                self.volume = self.typical_length*\
                    self.typical_width * self.parent.height_of_floors
        """

    def calc_heat_load(self, number_of_elements=2):
        """Norm heat load calculation.

        Calculates the norm heat load of the thermal zone.
        """

        _heat_capac_air = 1.002
        _density_air = 1.25

        if number_of_elements == 1 or number_of_elements == 2:
            self.heating_load = ((self.calc_attr.ua_value_ow +
                                  self.calc_attr.ua_value_win) +
                                 self.volume * self.infiltration_rate *
                                 _heat_capac_air * _density_air) * \
                                (self.t_inside - self.t_outside)
        elif number_of_elements == 3:
            self.heating_load = ((self.calc_attr.ua_value_ow + self.calc_attr.ua_value_gf +
                                  self.calc_attr.ua_value_win) +
                                 self.volume * self.infiltration_rate *
                                 _heat_capac_air * _density_air) * \
                                (self.t_inside - self.t_outside)
        elif number_of_elements == 4:
            self.heating_load = ((self.calc_attr.ua_value_ow + self.calc_attr.ua_value_gf +
                                  self.calc_attr.ua_value_rt + self.calc_attr.ua_value_win) +
                                 self.volume * self.infiltration_rate *
                                 _heat_capac_air * _density_air) * \
                                (self.t_inside - self.t_outside)

    def retrofit_zone(self, window_type=None, material=None):
        """Retrofits all walls and windows in the zone.
        """

        for wall_count in self.outer_walls:
            wall_count.retrofit_wall(self.parent.year_of_retrofit, material)
        for win_count in self.windows:
            win_count.replace_window(self.parent.year_of_retrofit, window_type)

    def delete(self):
        """Deletes the actual thermal zone and refreshs the thermal zones of
        the building
        """
        for index, tz in enumerate(self.parent.thermal_zones):
            if tz.internal_id == self.internal_id:
                self.parent.net_leased_area -= self.area
                self.parent.thermal_zones.pop(index)

                break

    def add_element(self, building_element):
        """Adds a building element to the corresponding list

        This function adds a BuildingElement instance to the the list
        depending on the type of the Building Element

        Parameters
        ----------
        building_element : BuildingElement()
            inherited objects of BuildingElement() instance of TEASER

        """

        ass_error_1 = ("building element has to be an instance of OuterWall(),"
                       " Rooftop(), GroundFloor(), Window(), InnerWall(), "
                       "Ceiling() or Floor()")

        assert type(building_element).__name__ in ("OuterWall", "Rooftop",
                                                   "GroundFloor", "InnerWall",
                                                   "Ceiling", "Floor",
                                                   "Window"), ass_error_1

        if type(building_element).__name__ in ("OuterWall", "Rooftop",
                                               "GroundFloor"):
            self._outer_walls.append(building_element)

        elif type(building_element).__name__ in ("InnerWall",
                                                 "Ceiling", "Floor"):
            self._inner_walls.append(building_element)

        elif type(building_element).__name__ in "Window":
            self._windows.append(building_element)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        from teaser.logic.buildingobjects.building import Building
        import inspect
        if value is not None:
            if inspect.isclass(Building):
                self.__parent = value
                self.__parent.thermal_zones.append(self)

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
    def outer_walls(self):
        return self._outer_walls

    @outer_walls.setter
    def outer_walls(self, value):

        if value is None:
            self._outer_walls = []

    @property
    def inner_walls(self):
        return self._inner_walls

    @inner_walls.setter
    def inner_walls(self, value):

        if value is None:
            self._inner_walls = []

    @property
    def windows(self):
        return self._windows

    @windows.setter
    def windows(self, value):

        if value is None:
            self._windows = []

    @property
    def use_conditions(self):
        return self._use_conditions

    @use_conditions.setter
    def use_conditions(self, value):
        ass_error_1 = "Use condition has to be an instance of UseConditions()"

        assert type(value).__name__ == "UseConditions" or \
               type(value).__name__ == "BoundaryConditions", ass_error_1

        if value is not None:
            self._use_conditions = value
            self.typical_length = value.typical_length
            self.typical_width = value.typical_width
        self._use_conditions = value

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
                raise ValueError("Can't convert zone area to float")

        if self.parent is not None:
            if self._area is None:
                if self.parent.net_leased_area is None:
                    self.parent.net_leased_area = 0.0
                self._area = value
                self.parent.net_leased_area += value
            else:
                self.parent.net_leased_area -= self._area
                self.parent.net_leased_area += value
                self._area = value
        else:
            self._area = value

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert zone volume to float")

        if self.parent is not None:
            if self._volume is None:
                self._volume = value
                self.parent.volume += value
            else:
                self.parent.volume -= self._volume
                self.parent.volume += value
                self._volume = value
        else:
            self._volume = value

    @property
    def infiltration_rate(self):
        return self._infiltration_rate

    @infiltration_rate.setter
    def infiltration_rate(self, value):

        if isinstance(value, float):
            self._infiltration_rate = value
        elif value is None:
            self._infiltration_rate = value
        else:
            try:
                value = float(value)
                self._infiltration_rate = value
            except:
                raise ValueError("Can't convert infiltration rate to float")

    @property
    def t_inside(self):
        return self._t_inside

    @t_inside.setter
    def t_inside(self, value):
        if isinstance(value, float):
            self._t_inside = value
        elif value is None:
            self._t_inside = value
        else:
            try:
                value = float(value)
                self._t_inside = value
            except:
                raise ValueError("Can't convert temperature to float")

    @property
    def t_outside(self):
        return self._t_outside

    @t_outside.setter
    def t_outside(self, value):

        if isinstance(value, float):
            self._t_outside = value
        elif value is None:
            self._t_outside = value
        else:
            try:
                value = float(value)
                self._t_outside = value
            except:
                raise ValueError("Can't convert temperature to float")
