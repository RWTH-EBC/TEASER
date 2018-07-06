# created June 2015
# by TEASER4 Development Team

"""This module includes the ThermalZone class
"""
from __future__ import division
import random
import re
import warnings
from teaser.logic.buildingobjects.calculation.one_element import OneElement
from teaser.logic.buildingobjects.calculation.two_element import TwoElement
from teaser.logic.buildingobjects.calculation.three_element import ThreeElement
from teaser.logic.buildingobjects.calculation.four_element import FourElement


class ThermalZone(object):
    """Thermal zone class.

    This class is used to manage information and parameter calculation for
    thermal zones. Each thermal zone has one specific calculation method,
    which is specific to the used model (model_attr). For new model
    implementation this attribute can be assigned to new classes.

    Parameters
    ----------
    parent: Building()
        The parent class of this object, the Building the zone belongs to.
        Allows for better control of hierarchical structures. If not None it
        adds this ThermalZone instance to Building.thermal_zones.
        Default is None

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
        Infiltration rate of zone. Default value aligned to
        :cite:`DeutschesInstitutfurNormung.2007`
    outer_walls : list
        List of OuterWall instances.
    doors : list
        List of Door instances.
    rooftops : list
        List of Rooftop instances.
    ground_floors : list
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
    model_attr : instance of OneElement(), TwoElement(), ThreeElement() or
                FourElement()
        Instance of OneElement(), TwoElement(), ThreeElement() or
        FourElement(), that holds all calculation functions and attributes
        needed for the specific model.
    typical_length : float [m]
        normative typical length of the thermal zone
    typical_width : float [m]
        normative typical width of the thermal zone
    t_inside : float [K]
        Normative indoor temperature for static heat load calculation.
        The input of t_inside is ALWAYS in Kelvin
    t_outside : float [K]
        Normative outdoor temperature for static heat load calculation.
        The input of t_inside is ALWAYS in Kelvin
    t_ground : float [K]
        Temperature directly at the outer side of ground floors for static
        heat load calculation.
        The input of t_ground is ALWAYS in Kelvin
    density_air : float [kg/m3]
        average density of the air in the thermal zone
    heat_capac_air : float [J/K]
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
        self._infiltration_rate = 0.4
        self._outer_walls = []
        self._doors = []
        self._rooftops = []
        self._ground_floors = []
        self._windows = []
        self._inner_walls = []
        self._floors = []
        self._ceilings = []
        self._use_conditions = None
        self.model_attr = None
        self.typical_length = None
        self.typical_width = None
        self._t_inside = 293.15
        self._t_outside = 261.15
        self.density_air = 1.25
        self.heat_capac_air = 1002
        self.t_ground = 286.15

    def calc_zone_parameters(
            self,
            number_of_elements=2,
            merge_windows=False,
            t_bt=5):
        """RC-Calculation for the thermal zone

        Based on the input parameters (used model) this function instantiates
        the corresponding calculation Class (e.g. TwoElement) and calculates
        the zone parameters. Currently the function is able to distinguishes
        between the number of elements, we distinguish between:
            - one element: all outer walls are aggregated into one element,
            inner wall are neglected
            - two elements: exterior and interior walls are aggregated
            - three elements: like 2, but floor or roofs are aggregated
            separately
            - four elements: roofs and floors are aggregated separately

        For all four options we can chose if the thermal conduction through
        the window is considered in a separate resistance or not.

        Parameters
        ----------
        number_of_elements : int
            defines the number of elements, that area aggregated, between 1
            and 4, default is 2

        merge_windows : bool
            True for merging the windows into the outer walls, False for
            separate resistance for window, default is False (Only
            supported for IBPSA)

        t_bt : float
            Time constant according to VDI 6007 (default t_bt = 5)
        """

        if number_of_elements == 1:
            self.model_attr = OneElement(
                thermal_zone=self,
                merge_windows=merge_windows,
                t_bt=t_bt)
            self.model_attr.calc_attributes()
        elif number_of_elements == 2:
            self.model_attr = TwoElement(
                thermal_zone=self,
                merge_windows=merge_windows,
                t_bt=t_bt)
            self.model_attr.calc_attributes()
        elif number_of_elements == 3:
            self.model_attr = ThreeElement(
                thermal_zone=self,
                merge_windows=merge_windows,
                t_bt=t_bt)
            self.model_attr.calc_attributes()
        elif number_of_elements == 4:
            self.model_attr = FourElement(
                thermal_zone=self,
                merge_windows=merge_windows,
                t_bt=t_bt)
            self.model_attr.calc_attributes()

    def find_walls(self, orientation, tilt):
        """Returns all outer walls with given orientation and tilt

        This function returns a list of all OuterWall elements with the
        same orientation and tilt.

        Parameters
        ----------
        orientation : float [degree]
            Azimuth of the desired walls.
        tilt : float [degree]
            Tilt against the horizontal of the desired walls.

        Returns
        -------
        elements : list
            List of OuterWalls instances with desired orientation and tilt.
        """
        elements = []
        for i in self.outer_walls:
            if i.orientation == orientation and i.tilt == tilt:
                elements.append(i)
            else:
                pass
        return elements

    def find_doors(self, orientation, tilt):
        """Returns all outer walls with given orientation and tilt

        This function returns a list of all Doors elements with the
        same orientation and tilt.

        Parameters
        ----------
        orientation : float [degree]
            Azimuth of the desired walls.
        tilt : float [degree]
            Tilt against the horizontal of the desired walls.

        Returns
        -------
        elements : list
            List of Doors instances with desired orientation and tilt.
        """
        elements = []
        for i in self.doors:
            if i.orientation == orientation and i.tilt == tilt:
                elements.append(i)
            else:
                pass
        return elements

    def find_rts(self, orientation, tilt):
        """Returns all rooftops with given orientation and tilt

        This function returns a list of all Rooftop elements with the
        same orientation and tilt.

        Parameters
        ----------
        orientation : float [degree]
            Azimuth of the desired rooftops.
        tilt : float [degree]
            Tilt against the horizontal of the desired rooftops.

        Returns
        -------
        elements : list
            List of Rooftop instances with desired orientation and tilt.
        """
        elements = []
        for i in self.rooftops:
            if i.orientation == orientation and i.tilt == tilt:
                elements.append(i)
            else:
                pass
        return elements

    def find_gfs(self, orientation, tilt):
        """Returns all ground floors with given orientation and tilt

        This function returns a list of all GroundFloor elements with the
        same orientation and tilt.

        Parameters
        ----------
        orientation : float [degree]
            Azimuth of the desired ground floors.
        tilt : float [degree]
            Tilt against the horizontal of the desired ground floors.

        Returns
        -------
        elements : list
            List of GroundFloor instances with desired orientation and tilt.
        """
        elements = []
        for i in self.ground_floors:
            if i.orientation == orientation and i.tilt == tilt:
                elements.append(i)
            else:
                pass
        return elements

    def find_wins(self, orientation, tilt):
        """Returns all windows with given orientation and tilt

        This function returns a list of all Window elements with the
        same orientation and tilt.

        Parameters
        ----------
        orientation : float [degree]
            Azimuth of the desired windows.
        tilt : float [degree]
            Tilt against the horizontal of the desired windows.

        Returns
        -------
        elements : list
            List of Window instances with desired orientation and tilt.
        """
        elements = []
        for i in self.windows:
            if i.orientation == orientation and i.tilt == tilt:
                elements.append(i)
            else:
                pass
        return elements

    def set_inner_wall_area(self):
        """Sets the inner wall area according to zone area

        Sets the inner wall area according to zone area size if type building
        approach is used. This function covers Floors, Ceilings and InnerWalls.
        """

        ass_error_1 = "You need to specify parent for thermal zone"

        assert self.parent is not None, ass_error_1

        for floor in self.floors:
            floor.area = (
                (self.parent.number_of_floors - 1) /
                self.parent.number_of_floors) * self.area
        for ceiling in self.ceilings:
            ceiling.area = (
                (self.parent.number_of_floors - 1) /
                self.parent.number_of_floors) * self.area

        for wall in self.inner_walls:
            typical_area = self.typical_length * self.typical_width

            avg_room_nr = self.area / typical_area

            wall.area = (avg_room_nr * (self.typical_length *
                                        self.parent.height_of_floors +
                                        2 * self.typical_width *
                                        self.parent.height_of_floors))

    def set_volume_zone(self):
        """Sets the zone volume according to area and height of floors

        Sets the volume of a zone according area and height of floors
        (building attribute).
        """

        ass_error_1 = "you need to specify parent for thermal zone"

        assert self.parent is not None, ass_error_1

        self.volume = self.area * self.parent.height_of_floors

    def retrofit_zone(
            self,
            type_of_retrofit=None,
            window_type=None,
            material=None):
        """Retrofits all walls and windows in the zone.

        Function call for all elements facing the ambient or ground.
        Distinguishes if the parent building is a archetype of type 'iwu' or
        'tabula_de'. If TABULA is used, it will use the pre-defined wall
        constructions of TABULA.

        This function covers OuterWall, Rooftop, GroundFloor and Window.

        Parameters
        ----------
        type_of_retrofit : str
            The classification of retrofit, if the archetype building
            approach of TABULA is used.
        window_type : str
            Default: EnEv 2014
        material : str
            Default: EPS035
        """

        if type_of_retrofit is None:
            type_of_retrofit = 'retrofit'

        if type(self.parent).__name__ in [
            "SingleFamilyHouse", "TerracedHouse", "MultiFamilyHouse",
                "ApartmentBlock"]:
            for wall_count in self.outer_walls \
                    + self.rooftops + self.ground_floors + self.doors + \
                    self.windows:
                if "adv_retrofit" in wall_count.construction_type:
                    warnings.warn(
                        "already highest available standard"
                        + self.parent.name + wall_count.name)
                elif "standard" in wall_count.construction_type:
                    wall_count.load_type_element(
                        year=self.parent.year_of_construction,
                        construction=wall_count.construction_type.replace(
                            "standard", type_of_retrofit))
                else:
                    wall_count.load_type_element(
                        year=self.parent.year_of_construction,
                        construction=wall_count.construction_type.replace(
                            "retrofit", type_of_retrofit))
        else:

            for wall_count in self.outer_walls:
                wall_count.retrofit_wall(
                    self.parent.year_of_retrofit,
                    material)
            for roof_count in self.rooftops:
                roof_count.retrofit_wall(
                    self.parent.year_of_retrofit,
                    material)
            for ground_count in self.ground_floors:
                ground_count.retrofit_wall(
                    self.parent.year_of_retrofit,
                    material)
            for win_count in self.windows:
                win_count.replace_window(
                    self.parent.year_of_retrofit,
                    window_type)

    def delete(self):
        """Deletes the actual thermal zone safely.

        This deletes the current thermal Zone and also refreshes the
        thermal_zones list in the parent Building.
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

        ass_error_1 = ("building_element has to be an instance of OuterWall,"
                       " Rooftop, GroundFloor, Window, InnerWall, "
                       "Ceiling or Floor")

        assert type(building_element).__name__ in (
            "OuterWall", "Rooftop", "GroundFloor",
            "InnerWall", "Ceiling", "Floor",
            "Window"), ass_error_1

        if type(building_element).__name__ == "OuterWall":
            self._outer_walls.append(building_element)
        elif type(building_element).__name__ == "GroundFloor":
            self._ground_floors.append(building_element)
        elif type(building_element).__name__ == "Rooftop":
            self._rooftops.append(building_element)
        elif type(building_element).__name__ == "InnerWall":
            self._inner_walls.append(building_element)
        elif type(building_element).__name__ == "Ceiling":
            self._ceilings.append(building_element)
        elif type(building_element).__name__ == "Floor":
            self._floors.append(building_element)
        elif type(building_element).__name__ == "Window":
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
    def doors(self):
        return self._doors

    @doors.setter
    def doors(self, value):
        if value is None:
            self._doors = []

    @property
    def rooftops(self):
        return self._rooftops

    @rooftops.setter
    def rooftops(self, value):
        if value is None:
            self._rooftops = []

    @property
    def ground_floors(self):
        return self._ground_floors

    @ground_floors.setter
    def ground_floors(self, value):
        if value is None:
            self._ground_floors = []

    @property
    def ceilings(self):
        return self._ceilings

    @ceilings.setter
    def ceilings(self, value):
        if value is None:
            self._ceilings = []

    @property
    def floors(self):
        return self._floors

    @floors.setter
    def floors(self, value):
        if value is None:
            self._floors = []

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
