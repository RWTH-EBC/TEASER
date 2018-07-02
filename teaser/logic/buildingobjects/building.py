# created June 2015
# by TEASER4 Development Team

"""This module includes the Building class
"""
import inspect
import random
import re
import warnings
from teaser.logic.buildingobjects.calculation.aixlib import AixLib
from teaser.logic.buildingobjects.calculation.ibpsa import IBPSA


from teaser.logic.buildingobjects.buildingsystems.buildingahu \
    import BuildingAHU


class Building(object):
    """Building Class

    This class is used to manage information and parameter calculation for
    Buildings. It is the base class for all archetype buildings and holds a
    list containing all ThermalZones instances. In addition it can hold an
    optional attribute for CentralAHU instance, that is e.g. needed for
    AixLib Simulation models.

    Parameters
    ----------

    parent: Project()
        The parent class of this object, the Project the Building belongs to.
        Allows for better control of hierarchical structures. If not None it
        adds this Building instance to Project.buildings.
        (default: None)
    name : str
        Individual name (default: None)
    year_of_construction : int
        Year of first construction (default: None)
    net_leased_area : float [m2]
        Total net leased area of building. This is area is NOT the footprint
        of a building (default: None)
    with_ahu : Boolean
        If set to True, an empty instance of BuildingAHU is instantiated and
        assigned to attribute central_ahu. This instance holds information for
        central Air Handling units. Default is False.

    Attributes
    ----------
    central_ahu : instance of BuildingAHU
        Teaser Instance of BuildingAHU if a central AHU is embedded into the
        building (currently mostly needed for AixLib simulation).
    number_of_floors : int
        number of floors above ground (default: None)
    height_of_floors : float [m]
        Average height of the floors (default: None)
    internal_id : float
        Random id for the distinction between different buildings.
    year_of_retrofit : int
        Year of last retrofit.
    type_of_building : string
        Type of a Building (e.g. Building (unspecified), Office etc.).
    building_id : None
        ID of building, can be set by the user to keep track of a building
        even outside of TEASER, e.g. in a simulation or in post-processing.
        This is not the same as internal_id, as internal_id is e.g. not
        exported to Modelica models!
    street_name : string
        Name of the street the building is located at. (optional)
    city : string
        Name of the city the building is located at. (optional)
    longitude : float [degree]
        Longitude of building location.
    latitude : float [degree]
        Latitude of building location.
    thermal_zones : list
        List with instances of ThermalZone(), that are located in this building.
    gml_surfaces : list
        List of all containing surfaces described by CityGML, the list
        should be filled with SurfaceGML class from Data.Input.citygml_input.
        This list is only used if this instance of a building was instantiated
        the CityGML Loader module.
    outer_area : dict [degree: m2]
        Dictionary with orientation as key and sum of outer wall areas of
        that direction as value.
    window_area : dict [degree: m2]
        Dictionary with orientation as key and sum of window areas of
        that direction as value.
    bldg_height : float [m]
        Total building height.
    volume : float [m3]
        Total volume of all thermal zones.
    sum_heat_load : float [W]
        Total heating load of all thermal zones.
    sum_cooling_load : float [W]
        Total heating load of all thermal zones. (currently not supported)
    number_of_elements_calc : int
        Number of elements that are used for thermal zone calculation in this
        building.
        1: OneElement
        2: TwoElement
        3: ThreeElement
        4: FourElement
    merge_windows_calc : boolean
        True for merging the windows into the outer wall's RC-combination,
        False for separate resistance for window, default is False. (Only
        supported for IBPSA)
    used_library_calc : str
        'AixLib' for https://github.com/RWTH-EBC/AixLib
        'IBPSA' for https://github.com/ibpsa/modelica
    library_attr : Annex() or AixLib() instance
        Classes with specific functions and attributes for building models in
        IBPSA and AixLib. Python classes can be found in calculation package.

    """

    def __init__(
            self,
            parent=None,
            name=None,
            year_of_construction=None,
            net_leased_area=None,
            with_ahu=False):
        """Constructor of Building Class
        """

        self.parent = parent
        self.name = name
        self.year_of_construction = year_of_construction
        self.net_leased_area = net_leased_area
        self._with_ahu = with_ahu
        if with_ahu is True:
            self.central_ahu = BuildingAHU(self)
        else:
            self._central_ahu = None

        self.number_of_floors = None
        self.height_of_floors = None
        self.internal_id = random.random()
        self._year_of_retrofit = None
        self.type_of_building = type(self).__name__
        self.building_id = None
        self.street_name = ""
        self.city = ""
        self.longitude = 6.05
        self.latitude = 50.79

        self._thermal_zones = []
        self.gml_surfaces = []
        self._outer_area = {}
        self._window_area = {}

        self.bldg_height = None
        self.volume = 0
        self.sum_heat_load = 0
        self.sum_cooling_load = 0

        self._number_of_elements_calc = 2
        self._merge_windows_calc = False
        self._used_library_calc = "AixLib"

        self.library_attr = None

    def set_height_gml(self):
        """Calculates the height of a building from CityGML data

        With given gml surfaces, this function computes the height of a
        building of LoD 1 and LoD 2 buildings from CityGML data. All
        z-coordinates are evaluated and the minimum z-value is subtracted
        by the maximal value.

        """
        if self.bldg_height is not None:
            pass
        else:
            max_help = 0
            min_help = 9999
            for surface in self.gml_surfaces:
                z_value = surface.gml_surface[2::3]
                max_help = max(max_help, max(z_value))
                min_help = min(min_help, min(z_value))

            self.bldg_height = max_help - min_help

    def get_footprint_gml(self):
        """Gets the footprint surface of a building from CityGML data

        with given gml surfaces, this function computes and returns the
        footprint area of a building from LoD 0 to LoD2 from CityGML data.
        This is done by either analysing the ground floor or the flat roof.

        Returns
        ----------
        surface area : float
            footprint area of a gml building

        """

        for surface in self.gml_surfaces:
            if surface.surface_orientation == -2 and surface.surface_tilt == \
                    0.0:
                return surface.surface_area
        for surface in self.gml_surfaces:
            if surface.surface_orientation == -1 and surface.surface_tilt == \
                    0.0:
                return surface.surface_area

    def set_gml_attributes(self, height_of_floor=3.5):
        """Sets building attributes from CityGML data

        Computes the net_leased_area depending on the footprint area,
        the number and the height of floors. If the number of floors is
        specified before it will use this value, if not it will compute the
        number of floors based on the gml building height and the average
        height of the floors. If the number of floors is zero it'll be set to
        one. If the net leased area is below 50.0 sqm it'll be set to 50.0.

        Parameters
        ----------
        height_of_floor : float
            average height of each floor of the building, the default value
            is 3.5 and is absolutely random.
        """

        if self.bldg_height is None:
            raise AttributeError("Building height needs to be defined for gml")

        if self.height_of_floors is None and self.number_of_floors is None:
            self.height_of_floors = height_of_floor
        elif self.height_of_floors is None and self.number_of_floors is not \
                None:
            self.height_of_floors = self.bldg_height / self.number_of_floors
        else:
            pass

        if self.number_of_floors is not None:
            self.net_leased_area = self.get_footprint_gml() * \
                self.number_of_floors
            return

        else:
            self.number_of_floors = int(round((self.bldg_height /
                                               self.height_of_floors)))
            if self.number_of_floors == 0:
                self.number_of_floors = 1

            self.net_leased_area = self.get_footprint_gml() * \
                self.number_of_floors

            if self.net_leased_area < 50.0:
                self.net_leased_area = 50.0

    def set_outer_wall_area(
            self,
            new_area,
            orientation):
        """Outer area wall setter

        sets the outer wall area of all walls of one direction and weights
        them according to zone size. This function covers OuterWalls,
        Rooftops, GroundFloors.

        Parameters
        ----------
        new_area : float
            new_area of all outer walls of one orientation
        orientation : float
            orientation of the obtained walls
        """

        for zone in self.thermal_zones:
            for wall in zone.outer_walls:
                if wall.orientation == orientation:
                    wall.area = (
                        ((new_area / self.net_leased_area) * zone.area) /
                        sum(count.orientation == orientation for count in
                            zone.outer_walls))

            for roof in zone.rooftops:
                if roof.orientation == orientation:
                    roof.area = (
                        ((new_area / self.net_leased_area) * zone.area) /
                        sum(count.orientation == orientation for count in
                            zone.rooftops))

            for ground in zone.ground_floors:
                if ground.orientation == orientation:
                    ground.area = (
                        ((new_area / self.net_leased_area) * zone.area) /
                        sum(count.orientation == orientation for count in
                            zone.ground_floors))

            for door in zone.doors:
                if door.orientation == orientation:
                    door.area = (
                        ((new_area / self.net_leased_area) * zone.area) /
                        sum(count.orientation == orientation for count in
                            zone.doors))

    def set_window_area(
            self,
            new_area,
            orientation):
        """Window area setter

        sets the window area of all windows of one direction and weights
        them according to zone size

        Parameters
        ----------
        new_area : float
            new_area of all window of one orientation
        orientation : float
            orientation of the obtained windows
        """

        for zone in self.thermal_zones:
            for win in zone.windows:
                if win.orientation == orientation:
                    win.area = (
                        ((new_area / self.net_leased_area) * zone.area) /
                        sum(count.orientation == orientation for count in
                            zone.windows))

    def get_outer_wall_area(self, orientation):
        """Get aggregated wall area of one orientation

        Returns the area of all outer walls of one direction. This function
        covers OuterWalls, GroundFloors and Rooftops.

        Parameters
        ----------
        orientation : float
            orientation of the obtained wall
        Returns
        ----------
        sum_area : float
            area of all walls of one direction
        """

        sum_area = 0.0
        for zone_count in self.thermal_zones:
            for wall_count in zone_count.outer_walls:
                if wall_count.orientation == orientation and\
                        wall_count.area is not None:
                    sum_area += wall_count.area
            for roof_count in zone_count.rooftops:
                if roof_count.orientation == orientation and \
                        roof_count.area is not None:
                    sum_area += roof_count.area
            for ground_count in zone_count.ground_floors:
                if ground_count.orientation == orientation and \
                        ground_count.area is not None:
                    sum_area += ground_count.area
        return sum_area

    def get_window_area(self, orientation):
        """Get aggregated window area of one orientation

        returns the area of all windows of one direction

        Parameters
        ----------
        orientation : float
            orientation of the obtained windows
        Returns
        ----------
        sum_area : float
            area of all windows of one direction
        """

        sum_area = 0.0
        for zone_count in self.thermal_zones:
            for win_count in zone_count.windows:
                if win_count.orientation == orientation and\
                        win_count.area is not None:
                    sum_area += win_count.area
        return sum_area

    def get_inner_wall_area(self):
        """Get aggregated inner wall area

        Returns the area of all inner walls. This function covers InnerWalls,
        Ceilings and Floors.

        Returns
        ----------
        sum_area : float
            area of all inner walls

        """

        sum_area = 0.0
        for zone_count in self.thermal_zones:
            for wall_count in zone_count.inner_walls:
                sum_area += wall_count.area
            for floor in zone_count.floors:
                sum_area += floor.area
            for ceiling in zone_count.ceilings:
                sum_area += ceiling.area
        return sum_area

    def fill_outer_area_dict(self):
        """Fills the attribute outer_area

        Fills the dictionary outer_area with the sum of outer wall area
        corresponding to the orientations of the building. This function
        covers OuterWalls, GroundFloors and Rooftops.

        """
        self.outer_area = {}
        for zone_count in self.thermal_zones:
            for wall_count in zone_count.outer_walls:
                self.outer_area[wall_count.orientation] = None
            for roof in zone_count.rooftops:
                self.outer_area[roof.orientation] = None
            for ground in zone_count.ground_floors:
                self.outer_area[ground.orientation] = None

        for key in self.outer_area:
            self.outer_area[key] = self.get_outer_wall_area(key)

    def fill_window_area_dict(self):
        """Fills the attribute

        Fills the dictionary window_area with the sum of window area
        corresponding to the orientations of the building.

        """
        self.window_area = {}
        for zone_count in self.thermal_zones:
            for win_count in zone_count.windows:
                self.window_area[win_count.orientation] = None

        for key in self.window_area:
            self.window_area[key] = self.get_window_area(key)

    def calc_building_parameter(
            self,
            number_of_elements=2,
            merge_windows=False,
            used_library='AixLib'):
        """calc all building parameters

        This functions calculates the parameters of all zones in a building
        sums norm heat load of all zones
        sums volume of all zones

        Parameters
        ----------
        number_of_elements : int
            defines the number of elements, that area aggregated, between 1
            and 4, default is 2
        merge_windows : bool
            True for merging the windows into the outer walls, False for
            separate resistance for window, default is False
        used_library : str
            used library (AixLib and IBPSA are supported)
        """

        self._number_of_elements_calc = number_of_elements
        self._merge_windows_calc = merge_windows
        self._used_library_calc = used_library

        for zone in self.thermal_zones:
            zone.calc_zone_parameters(
                number_of_elements=number_of_elements,
                merge_windows=merge_windows,
                t_bt=5)
            self.sum_heat_load += zone.model_attr.heat_load

        if self.used_library_calc == self.library_attr.__class__.__name__:
            if self.used_library_calc == 'AixLib':
                self.library_attr.calc_auxiliary_attr()
            else:
                pass
        elif self.library_attr is None:
            if self.used_library_calc == 'AixLib':
                self.library_attr = AixLib(parent=self)
                self.library_attr.calc_auxiliary_attr()
            elif self.used_library_calc == 'IBPSA':
                self.library_attr = IBPSA(parent=self)
        else:
            warnings.warn("You set conflicting options for the used library "
                          "in Building or Project class and "
                          "calculation function of building. Your library "
                          "attributes are set to default using the library "
                          "you indicated in the function call, which is: " +
                          self.used_library_calc)

            if self.used_library_calc == 'AixLib':
                self.library_attr = AixLib(parent=self)
                self.library_attr.calc_auxiliary_attr()
            elif self.used_library_calc == 'IBPSA':
                self.library_attr = IBPSA(parent=self)

    def retrofit_building(
            self,
            year_of_retrofit=None,
            type_of_retrofit=None,
            window_type=None,
            material=None):
        """Retrofits all zones in the building

        Function call for each zone.

        After retrofit, all parameters are calculated directly.

        Parameters
        ----------
        year_of_retrofit : float
            Year of last retrofit.
        type_of_retrofit : str
            The classification of retrofit, if the archetype building
            approach of TABULA is used.
        window_type : str
            Default: EnEv 2014
        material : str
            Default: EPS035
        """

        #  Set self.sum_heat_load to zero to prevent summing up of old and new
        #  design heat load calculation values (see #518)
        self.sum_heat_load = 0

        if year_of_retrofit is not None:
            self.year_of_retrofit = year_of_retrofit

        for zone in self.thermal_zones:
            zone.retrofit_zone(type_of_retrofit, window_type, material)

        self.calc_building_parameter(
            number_of_elements=self.number_of_elements_calc,
            merge_windows=self.merge_windows_calc,
            used_library=self.used_library_calc)

    def rotate_building(self, angle):
        """Rotates the building to a given angle

        This function covers OuterWall, Rooftop (if not flat roof) and Windows.

        Parameters
        ----------

        angle: float
            rotation of the building clockwise, between 0 and 360 degrees
        """

        for zone_count in self.thermal_zones:
            new_angle = None
            for wall_count in zone_count.outer_walls:
                new_angle = wall_count.orientation + angle
                if new_angle > 360.0:
                    wall_count.orientation = new_angle - 360.0
                else:
                    wall_count.orientation = new_angle
            for roof_count in zone_count.rooftops:
                if roof_count.orientation != -1:
                    new_angle = roof_count.orientation + angle
                    if new_angle > 360.0:
                        roof_count.orientation = new_angle - 360.0
                    else:
                        roof_count.orientation = new_angle
                else:
                    pass
            for win_count in zone_count.windows:
                new_angle = win_count.orientation + angle
                if new_angle > 360.0:
                    win_count.orientation = new_angle - 360.0
                else:
                    win_count.orientation = new_angle

    def add_zone(self, thermal_zone):
        """Adds a thermal zone to the corresponding list

        This function adds a ThermalZone instance to the the thermal_zones list

        Parameters
        ----------
        thermal_zone : ThermalZone()
            ThermalZone() instance of TEASER
        """

        ass_error_1 = "Zone has to be an instance of ThermalZone()"

        assert type(thermal_zone).__name__ == "ThermalZone", ass_error_1

        self._thermal_zones.append(thermal_zone)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):

        if value is not None:

            ass_error_1 = "Parent has to be an instance of Project()"

            assert type(value).__name__ == "Project", ass_error_1

            self.__parent = value

            if inspect.isclass(Building):
                if self in self.__parent.buildings:
                    pass
                else:
                    self.__parent.buildings.append(self)

        else:

            self.__parent = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            regex = re.compile('[^a-zA-z0-9]')
            self.__name = regex.sub('', value)
        else:
            try:
                value = str(value)
                regex = re.compile('[^a-zA-z0-9]')
                self.__name = regex.sub('', value)
            except ValueError:
                print("Can't convert name to string")

        if self.__name[0].isdigit():
            self.__name = "B" + self.__name

    @property
    def year_of_construction(self):
        return self.__year_of_construction

    @year_of_construction.setter
    def year_of_construction(self, value):

        if isinstance(value, int) or value is None:

            self.__year_of_construction = value
        else:
            try:
                value = int(value)
                self.__year_of_construction = value

            except:
                raise ValueError("Can't convert year of construction to int")

    @property
    def number_of_floors(self):
        return self.__number_of_floors

    @number_of_floors.setter
    def number_of_floors(self, value):

        if isinstance(value, int) or value is None:

            self.__number_of_floors = value
        else:
            try:
                value = int(value)
                self.__number_of_floors = value

            except:
                raise ValueError("Can't convert number of floors to int")

    @property
    def height_of_floors(self):
        return self.__height_of_floors

    @height_of_floors.setter
    def height_of_floors(self, value):

        if isinstance(value, float) or value is None:

            self.__height_of_floors = value
        else:
            try:
                value = float(value)
                self.__height_of_floors = value

            except:
                raise ValueError("Can't convert height of floors to float")

    @property
    def net_leased_area(self):
        return self.__net_leased_area

    @net_leased_area.setter
    def net_leased_area(self, value):

        if isinstance(value, float):
            self.__net_leased_area = value
        elif value is None:
            self.__net_leased_area = value
        else:
            try:
                value = float(value)
                self.__net_leased_area = value
            except:
                raise ValueError("Can't convert net leased area to float")

    @property
    def thermal_zones(self):
        return self._thermal_zones

    @thermal_zones.setter
    def thermal_zones(self, value):

        if value is None:
            self._thermal_zones = []

    @property
    def outer_area(self):
        return self._outer_area

    @outer_area.setter
    def outer_area(self, value):
        self._outer_area = value

    @property
    def window_area(self):
        return self._window_area

    @window_area.setter
    def window_area(self, value):
        self._window_area = value

    @property
    def year_of_retrofit(self):
        return self._year_of_retrofit

    @year_of_retrofit.setter
    def year_of_retrofit(self, value):
        if self.year_of_construction is not None:
            self._year_of_retrofit = value
        else:
            raise ValueError("Specify year of construction first")

    @property
    def with_ahu(self):
        return self._with_ahu

    @with_ahu.setter
    def with_ahu(self, value):

        if value is True and self.central_ahu is None:
            self.central_ahu = BuildingAHU(self)
            self._with_ahu = True
        elif value is False and self.central_ahu:
            self.central_ahu = None
            self._with_ahu = False

    @property
    def central_ahu(self):
        return self._central_ahu

    @central_ahu.setter
    def central_ahu(self, value):

        if value is None:
            self._central_ahu = value
        else:

            ass_error_1 = "central AHU has to be an instance of BuildingAHU()"

            assert type(value).__name__ == "BuildingAHU", ass_error_1

            self._central_ahu = value

    @property
    def number_of_elements_calc(self):

        return self._number_of_elements_calc

    @number_of_elements_calc.setter
    def number_of_elements_calc(self, value):

        ass_error_1 = "calculation_method has to be 1,2,3 or 4"

        assert value != [1, 2, 3, 4], ass_error_1

        if self.parent is None and value is None:
            self._number_of_elements_calc = 2
        elif self.parent is not None and value is None:
            self._number_of_elements_calc = self.parent.number_of_elements_calc
        elif value is not None:
            self._number_of_elements_calc = value

    @property
    def merge_windows_calc(self):

        return self._merge_windows_calc

    @merge_windows_calc.setter
    def merge_windows_calc(self, value):

        ass_error_1 = "merge windows needs to be True or False"

        assert value != [True, False], ass_error_1

        if self.parent is None and value is None:
            self._merge_windows_calc = 2
        elif self.parent is not None and value is None:
            self._merge_windows_calc = self.parent.merge_windows_calc
        elif value is not None:
            self._merge_windows_calc = value

    @property
    def used_library_calc(self):

        return self._used_library_calc

    @used_library_calc.setter
    def used_library_calc(self, value):

        ass_error_1 = "used library needs to be AixLib or IBPSA"

        assert value != ["AixLib", "IBPSA"], ass_error_1

        if self.parent is None and value is None:
            self._used_library_calc = "AixLib"
        elif self.parent is not None and value is None:
            self._used_library_calc = self.parent.used_library_calc
        elif value is not None:
            self._used_library_calc = value

        if self.used_library_calc == 'AixLib':
            self.library_attr = AixLib(parent=self)
        elif self.used_library_calc == 'IBPSA':
            self.library_attr = IBPSA(parent=self)
