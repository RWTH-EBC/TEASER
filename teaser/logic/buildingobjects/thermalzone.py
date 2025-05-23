# created June 2015
# by TEASER4 Development Team

"""This module includes the ThermalZone class
"""
from __future__ import division
import math
import random
import re
import warnings
from teaser.logic.buildingobjects.calculation.one_element import OneElement
from teaser.logic.buildingobjects.calculation.two_element import TwoElement
from teaser.logic.buildingobjects.calculation.three_element import ThreeElement
from teaser.logic.buildingobjects.calculation.four_element import FourElement
from teaser.logic.buildingobjects.calculation.five_element import FiveElement


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
    interzonal_walls : list
        List of InterzonalWall instances.
    interzonal_floors : list
        List of InterzonalFloor instances.
    interzonal_ceilings: list
        List of InterzonalCeiling instances.
    use_conditions : UseConditions
        Instance of UseConditions with all relevant information for the usage
        of the thermal zone
    model_attr : Union[OneElement, TwoElement, ThreeElement, FourElement,
    FiveElement]
        Instance of OneElement(), TwoElement(), ThreeElement(),
        FourElement(), or FiveElement() that holds all calculation functions
        and attributes needed for the specific model.
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
    t_ground_amplitude : float [K]
        Temperature amplitude of the ground over the year
    time_to_minimal_t_ground : int [s]
        Time between simulation time 0 (not: start_time) and the minimum of
        the ground temperature if the sine option for ground temperature is
        chosen. Default: 6004800 (noon of Mar 11 as published by Virginia Tech
        (https://www.builditsolar.com/Projects/Cooling/EarthTemperatures.htm)
        for a depth of 5 ft)
    density_air : float [kg/m3]
        average density of the air in the thermal zone
    heat_capac_air : float [J/K]
        average heat capacity of the air in the thermal zone
    number_of_floors : float
        number of floors of the zone. If None, parent's number_of_floors is used
    height_of_floors : float [m]
        average height of floors of the zone. If None, parent's height_of_floors
        is used

    """

    def __init__(self, parent=None):
        """Constructor for ThermalZone
        """

        self.parent = parent

        self.internal_id = random.random()
        self.name = None
        self._area = None
        self._volume = None
        self._outer_walls = []
        self._doors = []
        self._rooftops = []
        self._ground_floors = []
        self._windows = []
        self._inner_walls = []
        self._floors = []
        self._ceilings = []
        self._interzonal_walls = []
        self._interzonal_floors = []
        self._interzonal_ceilings = []
        self._use_conditions = None
        self._t_inside = 293.15
        self._t_outside = 261.15
        self.density_air = 1.25
        self.heat_capac_air = 1002
        self._t_ground = 286.15
        self._t_ground_amplitude = 0
        self.time_to_minimal_t_ground = 6004800

        self._number_of_floors = None
        self._height_of_floors = None

    def calc_zone_parameters(
            self,
            number_of_elements=2,
            merge_windows=False,
            t_bt=5,
            t_bt_layer=7
    ):
        """RC-Calculation for the thermal zone

        Based on the input parameters (used model) this function instantiates
        the corresponding calculation Class (e.g. TwoElement) and calculates
        the zone parameters. Currently, the function is able to distinguishes
        between the number of elements, we distinguish between:

            - one element: all outer walls are aggregated into one element,
              inner wall are neglected
            - two elements: exterior and interior walls are aggregated
            - three elements: like 2, but floor or roofs are aggregated
              separately
            - four elements: roofs and floors are aggregated separately
            - five elements: includes borders to adjacent zones

        For all four options we can choose if the thermal conduction through
        the window is considered in a separate resistance or not.

        Parameters
        ----------
        number_of_elements : int
            defines the number of elements, that area aggregated, between 1
            and 5, default is 2

        merge_windows : bool
            True for merging the windows into the outer walls, False for
            separate resistance for window, default is False (Only
            supported for IBPSA)

        t_bt : float
            Time constant according to VDI 6007 (default t_bt = 5)
        t_bt_layer: float
            Time constant according to VDI 6007 for aggragation of layers (default t_bt = 7)
        """

        if number_of_elements == 1:
            self.model_attr = OneElement(
                thermal_zone=self,
                merge_windows=merge_windows,
                t_bt=t_bt,
                t_bt_layer=t_bt_layer)
            self.model_attr.calc_attributes()
        elif number_of_elements == 2:
            self.model_attr = TwoElement(
                thermal_zone=self,
                merge_windows=merge_windows,
                t_bt=t_bt,
                t_bt_layer=t_bt_layer)
            self.model_attr.calc_attributes()
        elif number_of_elements == 3:
            self.model_attr = ThreeElement(
                thermal_zone=self,
                merge_windows=merge_windows,
                t_bt=t_bt,
                t_bt_layer=t_bt_layer)
            self.model_attr.calc_attributes()
        elif number_of_elements == 4:
            self.model_attr = FourElement(
                thermal_zone=self,
                merge_windows=merge_windows,
                t_bt=t_bt,
                t_bt_layer=t_bt_layer
            )
            self.model_attr.calc_attributes()
        elif number_of_elements == 5:
            self.model_attr = FiveElement(
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

    def find_izes_outer(self, orientation=None, tilt=None, add_reversed=False):
        """Returns all interzonal elements with given orientation and tilt

        This function returns a list of all InterzonalWall, InterzonalCeiling
        and InterzonalFloor elements that are to be lumped with outer elements
        or exported as borders to adjacent zones, optionally reduced to those
        with given orientation and tilt.

        Parameters
        ----------
        orientation : float [degree]
            Azimuth of the desired elements.
        tilt : float [degree]
            Tilt against the horizontal of the desired elements.
        add_reversed : bool
            also consider the elements with method_interzonal_export
            'outer_reversed' (only for lumping to borders with adjacent zones)

        Returns
        -------
        elements : list
            List of InterzonalWall, InterzonalCeiling and InterzonalFloor
            instances with desired orientation and tilt.
        """
        elements = []
        for i in self.interzonal_elements:
            if ((i.orientation == orientation or orientation is None)
                    and (i.tilt == tilt or tilt is None)):
                if i.interzonal_type_export == 'outer_ordered' or (
                        add_reversed and i.interzonal_type_export == 'outer_reversed'
                ):
                    elements.append(i)
            else:
                pass
        return elements

    def set_inner_wall_area(self):
        """Sets the inner wall area according to zone area

        Sets the inner wall area according to zone area size if type building
        approach is used. This function covers Floors, Ceilings and InnerWalls.
        Approximation approach depends on the building's
        inner_wall_approximation_approach attribute.

        """

        ass_error_1 = "You need to specify parent for thermal zone"

        assert self.parent is not None, ass_error_1

        for floor in self.floors:
            floor.area = ((self.number_of_floors - 1) / self.number_of_floors) \
                         * self.area
        for ceiling in self.ceilings:
            ceiling.area = ((self.number_of_floors - 1)
                            / self.number_of_floors) * self.area

        typical_area = self.use_conditions.typical_length * \
            self.use_conditions.typical_width

        avg_room_nr = self.area / typical_area

        approximation_approach \
            = self.parent.inner_wall_approximation_approach
        if approximation_approach not in (
                'teaser_default',
                'typical_minus_outer',
                'typical_minus_outer_extended'
        ):
            warnings.warn(f'Inner wall approximation approach '
                          f'{approximation_approach} unknown. '
                          f'Falling back to teaser_default.')
            approximation_approach = 'teaser_default'
        if approximation_approach == 'typical_minus_outer':
            wall_area = ((int(avg_room_nr)
                          + math.sqrt(avg_room_nr - int(avg_room_nr)))
                         * (2 * self.use_conditions.typical_length
                            * self.height_of_floors
                            + 2 * self.use_conditions.typical_width
                            * self.height_of_floors))
            for other_verticals in self.outer_walls + self.interzonal_walls\
                    + self.windows + self.doors:
                wall_area -= other_verticals.area
            wall_area = max(0.01, wall_area)
        elif approximation_approach == 'typical_minus_outer_extended':
            wall_area = ((int(avg_room_nr)
                          + math.sqrt(avg_room_nr - int(avg_room_nr)))
                         * (2 * self.use_conditions.typical_length
                            * self.height_of_floors
                            + 2 * self.use_conditions.typical_width
                            * self.height_of_floors))
            for other_verticals in self.outer_walls + self.interzonal_walls\
                    + self.doors:
                wall_area -= other_verticals.area
            for pot_vert_be in self.rooftops + self.windows:
                wall_area -= pot_vert_be.area \
                             * math.sin(pot_vert_be.tilt * math.pi / 180)
            wall_area -= max(0.0, sum(gf.area for gf in self.ground_floors)
                             - self.area)
            wall_area = max(0.01, wall_area)
        else:
            wall_area = (avg_room_nr
                         * (self.use_conditions.typical_length
                            * self.height_of_floors
                            + 2 * self.use_conditions.typical_width
                            * self.height_of_floors))

        for wall in self.inner_walls:
            wall.area = wall_area

    def set_volume_zone(self):
        """Sets the zone volume according to area and height of floors

        Sets the volume of a zone according area and height of floors
        (building attribute).
        """

        ass_error_1 = "you need to specify parent for thermal zone"

        assert self.parent is not None, ass_error_1

        self.volume = self.area * self.height_of_floors

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
                if "adv_retrofit" in wall_count.construction_data:
                    warnings.warn(
                        "already highest available standard"
                        + self.parent.name + wall_count.name)
                elif "standard" in wall_count.construction_data:
                    wall_count.load_type_element(
                        year=self.parent.year_of_construction,
                        construction=wall_count.construction_data.replace(
                            "standard", type_of_retrofit))
                else:
                    wall_count.load_type_element(
                        year=self.parent.year_of_construction,
                        construction=wall_count.construction_data.replace(
                            "retrofit", type_of_retrofit))
        else:

            for element_count in (
                    self.outer_walls
                    + self.rooftops
                    + self.ground_floors
                    + self.interzonal_elements
            ):
                element_count.retrofit_wall(
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
            "InterzonalWall", "InterzonalCeiling", "InterzonalFloor",
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
        elif type(building_element).__name__ == "InterzonalWall":
            self._interzonal_walls.append(building_element)
        elif type(building_element).__name__ == "InterzonalCeiling":
            self._interzonal_ceilings.append(building_element)
        elif type(building_element).__name__ == "InterzonalFloor":
            self._interzonal_floors.append(building_element)
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
        regex = re.compile('[^a-zA-z0-9]')
        if isinstance(value, str):
            name = regex.sub('', value)
        else:
            try:
                name = regex.sub('', str(value))
            except ValueError:
                print("Can't convert name to string")

        # check if another zone with same name exists
        tz_names = [tz._name for tz in self.parent.thermal_zones[:-1]]
        if name in tz_names:
            i = 1
            while True:
                name_add = f"{name}_{i}"
                if name_add not in tz_names:
                    name = name_add
                    break
                i += 1
        self._name = name

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
    def interzonal_walls(self):
        return self._interzonal_walls

    @interzonal_walls.setter
    def interzonal_walls(self, value):

        if value is None:
            self._interzonal_walls = []

    @property
    def interzonal_ceilings(self):
        return self._interzonal_ceilings

    @interzonal_ceilings.setter
    def interzonal_ceilings(self, value):

        if value is None:
            self._interzonal_ceilings = []

    @property
    def interzonal_floors(self):
        return self._interzonal_floors

    @interzonal_floors.setter
    def interzonal_floors(self, value):

        if value is None:
            self._interzonal_floors = []

    @property
    def interzonal_elements(self):
        return self.interzonal_walls + self.interzonal_ceilings \
            + self.interzonal_floors

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

        assert type(value).__name__ == "UseConditions", ass_error_1

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
    def number_of_floors(self):
        if self._number_of_floors is None:
            if self.parent is not None:
                number_of_floors = self.parent.number_of_floors
            else:
                number_of_floors = None
        else:
            number_of_floors = self._number_of_floors
        return number_of_floors

    @number_of_floors.setter
    def number_of_floors(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except ValueError:
                raise ValueError("Can't convert zone number_of_floors to float")

        self._number_of_floors = value

    @property
    def height_of_floors(self):
        if self._height_of_floors is None:
            if self.parent is not None:
                height_of_floors = self.parent.height_of_floors
            else:
                height_of_floors = None
        else:
            height_of_floors = self._height_of_floors
        return height_of_floors

    @height_of_floors.setter
    def height_of_floors(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except ValueError:
                raise ValueError("Can't convert zone height_of_floors to float")

        self._height_of_floors = value

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
            except ValueError:
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

    @property
    def t_ground(self):
        return self._t_ground

    @t_ground.setter
    def t_ground(self, value):

        if isinstance(value, float):
            self._t_ground = value
        elif value is None:
            self._t_ground = value
        else:
            try:
                value = float(value)
                self._t_ground = value
            except:
                raise ValueError("Can't convert temperature to float")

    @property
    def t_ground_amplitude(self):
        return self._t_ground_amplitude

    @t_ground_amplitude.setter
    def t_ground_amplitude(self, value):

        if isinstance(value, float):
            self._t_ground_amplitude = value
        elif value is None:
            self._t_ground_amplitude = value
        else:
            try:
                value = float(value)
                self._t_ground_amplitude = value
            except:
                raise ValueError("Can't convert temperature to float")
