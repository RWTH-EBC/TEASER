# created June 2015
# by TEASER4 Development Team

"""This module includes the Buidling class
"""
import random
import re
import numpy as np
import inspect
import scipy.io
import teaser.logic.utilities as utilitis
from teaser.logic.buildingobjects.buildingsystems.buildingahu \
    import BuildingAHU
import teaser.logic.simulation.aixlib as aixlib


class Building(object):
    '''Building Class

    This class represents a general building

    Parameters
    ----------

    parent: Project()
        The parent class of this object, the Project the Building belongs to.
        Allows for better control of hierarchical structures.
        (default: None)
    name : str
        individual name (default: None)
    year_of_construction : int
        year of first construction (default: None)
    number_of_floors : int
        number of floors above ground (default: None)
    height_of_floors : float
        average height of the floors (default: None)
    net_leased_area = float
        total net leased area of building (default: None)
    with_ahu : Boolean
        If set to True, an empty instance of BuildingAHU is instantiated, to be
        filled with AHU information

    Note: the listed attributes are just the ones that are set by the user
          calculated values are not included in this list

    Attributes
    ----------

    internal_id : float
        random id for the destinction between different buildings
    year_of_retrofit : int
        year of last retrofit
    type_of_building : string
        Type of a Building (e.g. Building (unspecified), Office etc.)
    building_id : None
        ID of building, can be set by the user to keep track of a building
        even outside of TEASER, e.g. in a simulation or in post-processing
    street_name : string
        name of the street the building is located at
    city : string
        name of the city the building is located at
    thermal_zones : list
        list of all containing thermal zones (ThermalZone())
    gml_surfaces : list
        list of all containing surfaces described by CityGML, the list should be
        filled with SurfaceGML class from Data.Input.citygml_input
    outer_area : dict
        dict with outer wall area and orientation
    window_area : dict
        dict with window area and orientation
    file_ahu : string
        path of AHU Matlab file for boundary condition
    file_internal_gains : string
        path of internal gains Matlab file for boundary condition
    file_set_t : string
        path of temperature Matlab file for boundary condition
    '''

    def __init__(self,
                 parent=None,
                 name=None,
                 year_of_construction=None,
                 net_leased_area=None,
                 with_ahu=False):

        '''Constructor of Building Class
        '''

        self.internal_id = random.random()

        self.parent = parent
        self.name = name
        self.building_id = None
        self.street_name = ""
        self.city = ""

        self.type_of_building = type(self).__name__

        self.year_of_construction = year_of_construction
        self._central_ahu = None
        self.with_ahu = with_ahu

        if with_ahu is True:
            self.central_ahu = BuildingAHU(self)

        self.number_of_floors = None
        self.height_of_floors = None
        self.net_leased_area = net_leased_area
        self.bldg_height = None

        self._year_of_retrofit = None

        self._thermal_zones = []
        self._outer_area = {}
        self._window_area = {}

        self.gml_surfaces = []

        self.volume = 0
        self.sum_heating_load = 0
        self.sum_cooling_load = 0

        #additional simulation parameters
        self.longitude = None
        self.latitude = None

        self.file_ahu = None
        self.file_internal_gains = None
        self.file_set_t = None
        self.file_weather = None

        self.orientation_bldg = []
        self.tilt_bldg = []
        self.orient_tilt = []
        self._number_of_elements_calc = 2
        self._merge_windows_calc = False
        self._used_library_calc = "AixLib"

    def set_height_gml(self):
        """calculates the height of a building from CityGML data

        with given gml surfaces, this function computes the height of a building
        of LoD 1 and LoD 2 buildings from CityGML data. All z-coordinates are
        evaluated and the minimum z-value is subtracted by the maximal value.
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
        """gets the footprint surface of a building from CityGML data

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

    def set_gml_attributes(self,
                           height_of_floor=3.5):
        """sets building attributes from CityGML data

        computes the net_leased_area depending on the footprint area,
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
            raise AttributeError("building height needs to be defined for gml")

        if self.height_of_floors is None and self.number_of_floors is None:
            self.height_of_floors = height_of_floor
        elif self.height_of_floors is None and self.number_of_floors is not \
                None:
            self.height_of_floors = self.bldg_height/self.number_of_floors
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

    def set_outer_wall_area(self,
                            new_area,
                            orientation):
        '''Outer area wall setter

        sets the outer wall area of all walls of one direction and weights
        them according to zone size

        Parameters
        ----------

        new_area : float
            new_area of all outer walls of one orientation
        orientation : float
            orientation of the obtained walls
        '''

        for zone in self.thermal_zones:
            for wall in zone.outer_walls:
                if wall.orientation == orientation:
                    wall.area = ((new_area / self.net_leased_area) * zone.area)

    def set_window_area(self, new_area, orientation):
        '''Window area setter

        sets the window area of all windows of one direction and weights
        them according to zone size

        Parameters
        ----------

        new_area : float
            new_area of all window of one orientation
        orientation : float
            orientation of the obtained windows
        '''

        for zone in self.thermal_zones:
            for win in zone.windows:
                if win.orientation == orientation:
                    win.area = ((new_area / self.net_leased_area) * zone.area)

    def get_outer_wall_area(self, orientation):
        '''Get aggregated outer wall area of one orientation

        returns the area of all outer walls of one direction

        Parameters
        ----------

        orientation : float
            orientation of the obtained wall

        Returns
        ----------

        sum_area : float
            area of all walls of one direction
        '''

        sum_area = 0.0
        for zone_count in self.thermal_zones:
            for wall_count in zone_count.outer_walls:
                if wall_count.orientation == orientation and\
                        wall_count.area is not None:
                    sum_area += (wall_count.area)
        return sum_area

    def get_window_area(self, orientation):
        '''Get aggregated window area of one orientation

        returns the area of all windows of one direction

        Parameters
        ----------

        orientation : float
            orientation of the obtained windows

        Returns
        ----------

        sum_area : float
            area of all windows of one direction

        '''

        sum_area = 0.0
        for zone_count in self.thermal_zones:
            for win_count in zone_count.windows:
                if win_count.orientation == orientation and\
                        win_count.area is not None:
                    sum_area += (win_count.area)
        return sum_area

    def get_inner_wall_area(self):
        '''get all inner wall area

        returns the area of all inner walls

        Returns
        ----------

        sum_area : float
            area of all inner walls
        '''

        sum_area = 0.0
        for zone_count in self.thermal_zones:
            for wall_count in zone_count.inner_walls:
                sum_area += (wall_count.area)
        return sum_area

    def set_specific_wall_area(self,
                               spec_zone,
                               spec_wall,
                               new_area):
        '''set one specific wall area

        sets the area of a specific wall in a specific zone and weights the
        rest of the walls according to their zone size

        Parameters
        ----------

        spec_zone : ThermalZone()
            pointer to the corresponding zone
        spec_wall : OuterWall()
            pointer to the corresponding wall
        new_area : float
            new area of specific wall
        '''

        spec_wall.area = new_area
        actual_area = self.get_outer_wall_area(spec_wall.orientation)-new_area
        for zone_count in self.thermal_zones:
            for wall_count in zone_count.outer_walls:
                if wall_count.orientation == spec_wall.orientation:
                    if wall_count is spec_wall:
                        pass
                    elif zone_count is spec_zone:
                        wall_count.area = \
                            (actual_area * (zone_count.area /
                                            self.net_leased_area)) / \
                            (float(len(zone_count.outer_walls)) - 1)
                    else:
                        wall_count.area = \
                            (actual_area * (zone_count.area /
                                            self.net_leased_area)) / \
                            (float(len(zone_count.outer_walls)))

    def fill_outer_area_dict(self):
        '''fill the outer area dict

        fills self.outer_area with the sum of outer wall area corresponding to
        the orientations of the building
        '''
        self.outer_area = {}
        for zone_count in self.thermal_zones:
            for wall_count in zone_count.outer_walls:
                self.outer_area[wall_count.orientation] = None

        for key in self.outer_area:
            self.outer_area[key] = self.get_outer_wall_area(key)

    def fill_window_area_dict(self):
        '''fill the window area dict

        fills self.window_area with all the sum of window area corresponding to
        the orientations of the building

        '''
        self.window_area = {}
        for zone_count in self.thermal_zones:
            for win_count in zone_count.windows:
                self.window_area[win_count.orientation] = None

        for key in self.window_area:
            self.window_area[key] = self.get_window_area(key)

    def calc_building_parameter(self,
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
            used library (AixLib and Annex60 are supported)
        """

        self._number_of_elements_calc = number_of_elements
        self._merge_windows_calc = merge_windows
        self._used_library_calc = used_library

        for zone in self.thermal_zones:
            zone.calc_zone_parameters(number_of_elements=number_of_elements,
                                      merge_windows=merge_windows,
                                      t_bt=5)
            self.sum_heating_load += zone.heating_load

        if self.used_library_calc == 'AixLib':
            aixlib.compare_orientation(self)
        elif self.used_library_calc == 'Annex60':
            import teaser.logic.simulation.annex as annex

            annex.compare_orientation(self, number_of_elements=number_of_elements)


    def retrofit_building(self,
                          year_of_retrofit=None,
                          window_type=None,
                          material=None):
        ''' Retrofits all zones in the building

        Function call for each zone.

        After retrofit, all parameters are calculated directly.

        Parameters
        ----------
        window_type : str
            Default: EnEv 2014
        material : str
            Default: EPS035
        '''
        if year_of_retrofit is not None:
            self.year_of_retrofit = year_of_retrofit
        else:
            pass

        for zone in self.thermal_zones:
            zone.retrofit_zone(window_type, material)

        self.calc_building_parameter(
            number_of_elements=self.number_of_elements_calc,
            merge_windows=self.merge_windows_calc,
            used_library=self.used_library_calc)

    def rotate_building(self, angle):
        '''rotates the building to a given angle

        Parameters
        ----------

        angle: float
            rotation of the building clockwise, between 0 and 360 degrees

        '''

        for zone_count in self.thermal_zones:
            new_angle = None
            for wall_count in zone_count.outer_walls:
                if type(wall_count).__name__ == "OuterWall":
                    new_angle = wall_count.orientation + angle
                    if new_angle > 360.0:
                        wall_count.orientation = new_angle - 360.0
                    else:
                        wall_count.orientation = new_angle
                else:
                    pass
            for win_count in zone_count.windows:
                new_angle = win_count.orientation + angle
                if new_angle > 360.0:
                    win_count.orientation = new_angle - 360.0
                else:
                    win_count.orientation = new_angle



    def add_zone(self, thermal_zone):
        '''Adds a thermal zone to the corresponding list

        This function adds a ThermalZone instance to the the thermal_zones list

        Parameters
        ----------
        thermal_zone : ThermalZone()
            ThermalZone() instance of TEASER

        '''

        ass_error_1 = ("Zone has to be an instance of ThermalZone()")

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
        # some improvement needed here
        # self._outer_area = collections.OrderedDict(self._outer_area.keys())
        return self._outer_area

    @outer_area.setter
    def outer_area(self, value):
        # some improvement needed here
        self._outer_area = value

    @property
    def window_area(self):
        # some improvement needed here
        return self._window_area

    @window_area.setter
    def window_area(self, value):
        # some improvement needed here
        self._window_area = value

    @property
    def year_of_retrofit(self):
        # some improvement needed here
        return self._year_of_retrofit

    @year_of_retrofit.setter
    def year_of_retrofit(self, value):
        if self.year_of_construction is not None:
            self._year_of_retrofit = value
        else:
            raise ValueError("Specify year of construction first")

    @property
    def central_ahu(self):
        return self._central_ahu

    @central_ahu.setter
    def central_ahu(self, value):

        ass_error_1 = "central AHU has to be an instance of BuildingAHU()"

        assert type(value).__name__ == ("BuildingAHU"), ass_error_1

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

        ass_error_1 = "used library needs to be AixLib or Annex60"

        assert value != ["AixLib", "Annex60"], ass_error_1

        if self.parent is None and value is None:
            self._used_library_calc = 2
        elif self.parent is not None and value is None:
            self._used_library_calc = self.parent.used_library_calc
        elif value is not None:
            self._used_library_calc = value
