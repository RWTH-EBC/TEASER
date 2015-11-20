# created June 2015
# by TEASER4 Development Team

"""This module includes the Buidling class
"""
import random
import numpy as np
import inspect
import scipy.io
import teaser.Logic.Utilis as utilis

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
    central_ahu : BuildingAHU.py object
        BuildingAHU.py object with information about central AHU 
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

        self._central_ahu = None
        self._year_of_retrofit = None

        self._thermal_zones = []
        self._thermal_zones = []
        self._outer_area = {}
        self._window_area = {}

        self.volume = 0
        self.sum_heating_load = 0
        self.sum_cooling_load = 0

        self.file_ahu = None
        self.file_internal_gains = None
        self.file_set_t = None
        self.file_weather = None

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

    def create_timeline(self, duration_profile = 86400, time_step = 3600):
        ''' Creates a timeline for building boundary conditions

        This function creates a list with a equidistant timeline given the
        duration of the profile in seconds (default one day, 86400 s) and the
        time_step in seconds (default one hour, 3600 s). Needed for boundary
        input of the building for Modelica simulation
        
        Note
        ----------
        As Python starts from counting the range from zero, but Modelica needs
        0 as start value and additional 24 entries. We add one interation 
        step in the time line.

        Parameters
        ----------
        duration_profile : int
            duration of the profile in seconds (default one day, 86400 s)
        time_step : int
            time step used in the profile in seconds (default one hour, 3600 s)


        Returns
        ---------
        time_line : [[int]]
            list of time steps as preparation for the output of boundary 
            conditions
        '''
        ass_error_1 = "duration musst be a multiple of time_step"

        assert float(duration_profile/time_step).is_integer(), ass_error_1

        time_line = []

        for i in range(int(duration_profile/time_step)+1):
            time_line.append([i*time_step])
        return time_line
    
    def modelica_set_temp(self, path = None):
        '''creates .mat file for set temperatures for each zone

        This function creates a matfile (-v4) for set temperatures of each 
        zone
        
        1. Row: heat set temperature of all zones
        2. Row: cool set temperature of all zones

        Parameters
        ----------
        path : str
            optional path, when matfile is exported seperately
                
        '''
        pass
        if self.file_set_t is None:
            self.file_set_t = "\\Tset_Building.mat"
        else:
            pass

        if path is None:
            path = utilis.get_default_path() + self.file_set_t
        else:
            path = utilis.create_path(path) + self.file_set_t
            
        t_set_heat = [0]
        t_set_cool = [0]
        for zone_count in self.thermal_zones:
            t_set_heat.append(zone_count.use_conditions.set_temp_heat)
            t_set_cool.append(zone_count.use_conditions.set_temp_cool)
            

        scipy.io.savemat(path,
                         mdict={'Tset': [t_set_heat,t_set_cool]},
                         appendmat = False,
                         format = '4')
    
    
    def modelica_AHU_boundary(self,
                              time_line = None,
                              profile_temperature_AHU = None,
                              profile_min_relative_humidity = None,
                              profile_max_relative_humidity = None,
                              profile_status_AHU = None,
                              path = None):
        '''creates .mat file for AHU boundary conditions (building)

        This function creates a matfile (-v4) for building AHU boundary 
        conditions
        
        1. Column : time step
        2. Column : desired AHU profile temperature
        3. Column : Desired minimal relative humidity
        4. Column : desired maximal relative humidity 
        5. Columb : AHU status (On/Off)

        Parameters
        ----------
        time_line :[[int]]
            list of time steps 
        profile_temperature_AHU : [float]
            timeline of temperatures requirements for AHU simulation
        profile_min_relative_humidity : [float]
            timeline of relative humidity requirements for AHU simulation
        profile_max_relative_humidity : [float]
            timeline of relative humidity requirements for AHU simulation
        profile_status_AHU : [int]
            timeline of status of the AHU simulation (on/off)
        path : str
            optional path, when matfile is exported seperately

        '''
        
        if time_line is None:
            time_line = self.create_timeline()
        if profile_temperature_AHU is None:
            profile_temperature_AHU = self.profile_temperature_AHU
        if profile_min_relative_humidity is None:
            profile_min_relative_humidity = self.profile_min_relative_humidity
        if profile_max_relative_humidity is None:
            profile_max_relative_humidity = self.profile_max_relative_humidity
        if profile_status_AHU is None:
            profile_status_AHU = self.profile_status_AHU
            
        ass_error_1 = "time line and input have to have the same length"
        
        assert len(time_line) == len(profile_temperature_AHU), \
                            (ass_error_1 + ",profile_temperature_AHU")
        assert len(time_line) == len(profile_min_relative_humidity), \
                            (ass_error_1 + ",profile_min_relative_humidity")
        assert len(time_line) == len(profile_max_relative_humidity), \
                            (ass_error_1 + ",profile_max_relative_humidity")
        assert len(time_line) == len(profile_status_AHU), \
                            (ass_error_1 + ",profile_status_AHU")
        
        
        for i, time in enumerate(time_line):

            time.append(profile_temperature_AHU[i])
            time.append(profile_min_relative_humidity[i])
            time.append(profile_max_relative_humidity[i])
            time.append(profile_status_AHU[i])

        ahu_boundary = np.array(time_line)
        
        if self.file_ahu is None:
            self.file_ahu = "\\AHU_Building.mat"
        else:
            pass

        if path is None:
            path = utilis.get_default_path() + self.file_ahu
        else:
            path = utilis.create_path(path) + self.file_ahu

        scipy.io.savemat(path,
                         mdict={'AHU': ahu_boundary},
                         appendmat = False,
                         format = '4')
    
    def modelica_gains_boundary(self, 
                                time_line = None,
                                path = None):
        '''creates .mat file for internal gains boundary conditions (building)

        This function creates a matfile (-v4) for building internal gains 
        boundary conditions. It collects all internal gain profiles of the
        zones and stores them into one file. The file is extended for each 
        zone. Only applicable if zones are defined
        
        1. Column : time step
        2,5,8,...  Column : profile_persons
        3,6,9,...  Column : profile_machines
        4,7,10,... Column : profile_lighting
        
        Note
        ----------
        When time line is created, we need to add a 0 to first element of
        all boundaries. This is due to to expected format in Modelica.
        
        Parameters
        ----------
        time_line :[[int]]
            list of time steps 
        path : str
            optional path, when matfile is exported seperately
        
        '''     
        if self.file_internal_gains is None:
            self.file_internal_gains = "\\InternalGains_Building.mat"
        else:
            pass

        for zone_count in self.thermal_zones:
            if time_line is None:
                duration= len(zone_count.use_conditions.profile_persons) * \
                            3600
                time_line = self.create_timeline(duration_profile = duration)
                zone_count.use_conditions.profile_persons.insert(0,0)
                zone_count.use_conditions.profile_machines.insert(0,0)
                zone_count.use_conditions.profile_lighting.insert(0,0)
                
            ass_error_1 = "time line and input have to have the same length"

            assert len(time_line) == len(zone_count.use_conditions.profile_persons), \
                                (ass_error_1 + ",profile_persons")
            assert len(time_line) == len(zone_count.use_conditions.profile_machines), \
                                (ass_error_1 + ",profile_machines")
            assert len(time_line) == len(zone_count.use_conditions.profile_lighting), \
                                (ass_error_1 + ",profile_lighting")
            
            for i, time in enumerate(time_line):

                time.append(zone_count.use_conditions.profile_persons[i])
                time.append(zone_count.use_conditions.profile_machines[i])
                time.append(zone_count.use_conditions.profile_lighting[i])

        internal_boundary = np.array(time_line)

        if path is None:
            path = utilis.get_default_path() + self.file_internal_gains
        else:
            path = utilis.create_path(path) + self.file_internal_gains

        scipy.io.savemat(path,
                         mdict={'Internals': internal_boundary},
                         appendmat = False,
                         format = '4')
    
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
    
    @property
    def central_ahu(self):
        return self._central_ahu
        
    @central_ahu.setter
    def central_ahu(self, value):

        ass_error_1 = "A central AHU has to be an instance of BuildingAHU()"

        assert type(value).__name__ == "BuildingAHU", ass_error_1

        self._central_ahu = value
