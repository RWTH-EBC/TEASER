# created June 2015
# by TEASER4 Development Team

"""This module includes the Buidling class
"""
import random
# import collections
import inspect


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
    street_name : string
        name of the street the building is located at
    city : string
        name of the city the building is located at
    thermal_zones : list
        list of all containing thermal zones (ThermalZone())
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

    def __init__(self, parent=None, name=None,
                 year_of_construction=None,
                 number_of_floors=None,
                 height_of_floors=None,
                 net_leased_area=None):
        '''Constructor of Building Class
        '''

        self.internal_id = random.random()

        self.parent = parent
        self.name = name
        self.street_name = ""
        self.city = ""

        self.type_of_building = type(self).__name__

        self.year_of_construction = year_of_construction

        if number_of_floors is not None:
            self.number_of_floors = float(number_of_floors)
        else:
            self.number_of_floors = number_of_floors
        if height_of_floors is not None:
            self.height_of_floors = float(height_of_floors)
        else:
            self.height_of_floors = height_of_floors
        if net_leased_area is not None:
            self.net_leased_area = float(net_leased_area)
        else:
            self.net_leased_area = net_leased_area

        self._year_of_retrofit = None

        self._thermal_zones = []
        self._thermal_zones = []
        self._outer_area = {}
        self._window_area = {}

        self.volume = 0
        self.sum_heating_load = 0
        self.sum_cooling_load = 0

        self.file_ahu = ""
        self.file_internal_gains = ""
        self.file_set_t = ""
        self.file_weather = ""

        self._calculation_method = self.parent.calculation_method

    def set_outer_wall_area(self, new_area, orientation):
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
                if wall_count.orientation == orientation:
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
                if win_count.orientation == orientation:
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

    def set_specific_wall_area(self, spec_zone, spec_wall, new_area):
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
        for zone_count in self.thermal_zones:
            for win_count in zone_count.outer_walls:
                self.window_area[win_count.orientation] = None

        for key in self.window_area:
            self.window_area[key] = self.get_window_area(key)

    def calc_building_parameter(self, calculation_core):
        '''calc all building parameters

        This functions calculates the parameters of all zones in a building
        sums norm heat load of all zones
        sums volume of all zones

        Parameters
        ----------

        calculation_core : string
            setter of the used calculation core ('vdi' or 'ebc'), default:'vdi'

        '''
        self._calculation_method = calculation_core

        for zone in self.thermal_zones:
            zone.calc_zone_parameters(calculation_core)
            self.volume += zone.volume
            self.sum_heating_load += zone.heating_load

    def retrofit_building(self, year_of_retrofit=None,
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

        self.calc_building_parameter(self._calculation_method)

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

                self.__parent.list_of_buildings.append(self)
        else:
            pass

    @property
    def thermal_zones(self):
        return self._thermal_zones

    @thermal_zones.setter
    def thermal_zones(self, value):

        ass_error_1 = "A thermal zone has to be an instance of ThermalZone()"

        assert type(value).__name__ == "ThermalZone", ass_error_1

        if self.thermal_zones is None:
            self._thermal_zones = [value]
        else:
            self._thermal_zones.append(value)

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
        self.__window_area = value

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
