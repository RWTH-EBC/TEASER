# created June 2015
# by TEASER4 Development Team

"""This module includes the Buidling class
"""
import random
import re
import numpy as np
import inspect
import scipy.io
import teaser.Logic.Utilis as utilis
from teaser.Logic.BuildingObjects.BuildingSystems.BuildingAHU \
    import BuildingAHU

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

    def __init__(self,
                 parent=None,
                 name=None,
                 year_of_construction=None,
                 number_of_floors=None,
                 height_of_floors=None,
                 net_leased_area=None,
                 with_ahu=False):

        '''Constructor of Building Class
        '''

        self.internal_id = random.random()

        self.parent = parent
        self.name = name
        self.street_name = ""
        self.city = ""

        self.type_of_building = type(self).__name__

        self.year_of_construction = year_of_construction
        self._central_ahu = None
        self.with_ahu = with_ahu
        
        if with_ahu is True:
            self.central_ahu = BuildingAHU(self)
        
        
        self.number_of_floors = number_of_floors
        self.height_of_floors = height_of_floors
        self.net_leased_area = net_leased_area

        self._year_of_retrofit = None

        self._thermal_zones = []
        self._outer_area = {}
        self._window_area = {}

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
        self._calculation_method = None

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

    def calc_building_parameter(self, calculation_method=None):
        '''calc all building parameters

        This functions calculates the parameters of all zones in a building
        sums norm heat load of all zones
        sums volume of all zones

        Parameters
        ----------

        calculation_method : string
            setter of the used calculation core ('vdi' or 'ebc'), default:'vdi'

        '''
        if calculation_method is not None:
            self.calculation_method = calculation_method
        else:
            pass

        for zone in self.thermal_zones:
            zone.calc_zone_parameters(self.calculation_method)
            self.sum_heating_load += zone.heating_load
        self.compare_list()

    def compare_list(self):
        '''dirty dirty function!!!!

        compares orientation, tilts etc

        to do: implement function, that sorts outer_walls and windows
        '''
        nr_of_orientation = {}

        for zone in self.thermal_zones:
            nr_of_orientation[zone] = list(set(zone.orientation_wall) | set(
                                                        zone.orientation_win))
            nr_of_orientation[zone].sort()


        for key, value in nr_of_orientation.items():
            self.orientation_bldg = list(set(self.orientation_bldg) | set(value))
        self.orientation_bldg.sort()

        try:
            i = self.orientation_bldg.index(-2)
            del self.orientation_bldg[i]
        except:
            pass

        if self.orientation_bldg[0] == -1 or None:
            self.orientation_bldg.insert(len(self.orientation_bldg), self.orientation_bldg.pop(0))

        for zone in self.thermal_zones:
            for test in self.orientation_bldg:
                if zone.find_wall(test) is not None:
                    zone.weightfactor_ow.append(zone.find_wall(test).wf_out)
                else:
                    zone.weightfactor_ow.append(0)
                if zone.find_win(test) is not None:
                    zone.weightfactor_win.append(zone.find_win(test).wf_out)
                else:
                    zone.weightfactor_win.append(0)

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

        self.calc_building_parameter(self.calculation_method)

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

        !AixLib sepcific!        
        
        1. Row: heat set temperature of all zones
        2. Row: cool set temperature of all zones

        Parameters
        ----------
        path : str
            optional path, when matfile is exported seperately
                
        '''
        
        if self.file_set_t is None:
            self.file_set_t = "\\Tset_"+self.name+".mat"
        else:
            pass

        if path is None:
            path = utilis.get_default_path()
        else:
            pass
        
        utilis.create_path(path) 
        path = path + self.file_set_t

        t_set_heat = [0]
        
        for zone_count in self.thermal_zones:
            t_set_heat.append(zone_count.use_conditions.set_temp_heat)

        scipy.io.savemat(path,
                         mdict={'Tset': [t_set_heat]},
                         appendmat = False,
                         format = '4')
    
    
    def modelica_AHU_boundary(self,
                              time_line = None,
                              path = None):
        '''creates .mat file for AHU boundary conditions (building)

        This function creates a matfile (-v4) for building AHU boundary 
        conditions
        
        !AixLib sepcific!

        Known limitation:        
        
        1. Column : time step
        2. Column : desired AHU profile temperature
        3. Column : Desired minimal relative humidity
        4. Column : desired maximal relative humidity 
        5. Columb : AHU status (On/Off)

        Parameters
        ----------
        time_line :[[int]]
            list of time steps 
        path : str
            optional path, when matfile is exported seperately
            
        Attributes
        ----------
        profile_temperature : [float]
            timeline of temperatures requirements for AHU simulation
        profile_min_relative_humidity : [float]
            timeline of relative humidity requirements for AHU simulation
        profile_max_relative_humidity : [float]
            timeline of relative humidity requirements for AHU simulation
        profile_v_flow : [int]
            timeline of desired relative v_flow of the AHU simulation (0..1)

        '''
        
        if self.file_ahu is None:
            self.file_ahu = "\\AHU_"+self.name+".mat"
        else:
            pass

        if path is None:
            path = utilis.get_default_path()
        else:
            pass
        
        utilis.create_path(path)
        path = path + self.file_ahu
        
        if time_line is None:
            time_line = self.create_timeline()
        if self.with_ahu is True:
            profile_temperature = \
                        self.central_ahu.profile_temperature
            profile_min_relative_humidity = \
                        self.central_ahu.profile_min_relative_humidity
            profile_max_relative_humidity = \
                        self.central_ahu.profile_max_relative_humidity
            profile_v_flow = \
                        self.central_ahu.profile_v_flow
        else:
            #Dummy values for Input Table (based on discussion with pme)
            time_line = [[0],[3600]]
            profile_temperature = [293.15,293.15]
            profile_min_relative_humidity = [0,0]
            profile_max_relative_humidity = [1,1]
            profile_v_flow = [0,1]
            
        
        ass_error_1 = "time line and input have to have the same length"
        
        assert len(time_line) == len(profile_temperature), \
                            (ass_error_1 + ",profile_temperature_AHU")
        assert len(time_line) == len(profile_min_relative_humidity), \
                            (ass_error_1 + ",profile_min_relative_humidity")
        assert len(time_line) == len(profile_max_relative_humidity), \
                            (ass_error_1 + ",profile_max_relative_humidity")
        assert len(time_line) == len(profile_v_flow), \
                            (ass_error_1 + ",profile_status_AHU")
        
        
        for i, time in enumerate(time_line):

            time.append(profile_temperature[i])
            time.append(profile_min_relative_humidity[i])
            time.append(profile_max_relative_humidity[i])
            time.append(profile_v_flow[i])

        ahu_boundary = np.array(time_line)
        
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

        !AixLib sepcific!        
        
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
            self.file_internal_gains = "\\InternalGains_"+self.name+".mat"
        else:
            pass

        if path is None:
            path = utilis.get_default_path()
        else:
            pass
        
        utilis.create_path(path) 
        path = path + self.file_internal_gains

        for zone_count in self.thermal_zones:
            if time_line is None:
                duration= len(zone_count.use_conditions.profile_persons) * \
                            3600
                time_line = self.create_timeline(duration_profile = duration)
            
#            zone_count.use_conditions.profile_persons.insert(0,0)
#            zone_count.use_conditions.profile_machines.insert(0,0)
#            zone_count.use_conditions.profile_lighting.insert(0,0)

            ass_error_1 = "time line and input have to have the same length"
            
            assert len(time_line)-1 == len(zone_count.use_conditions.profile_persons), \
                                (ass_error_1 + ",profile_persons")
            assert len(time_line)-1 == len(zone_count.use_conditions.profile_machines), \
                                (ass_error_1 + ",profile_machines")
            assert len(time_line)-1 == len(zone_count.use_conditions.profile_lighting), \
                                (ass_error_1 + ",profile_lighting")
            
            for i, time in enumerate(time_line):
                
                if i == 0:
                    time.append(0)
                    time.append(0)
                    time.append(0)
                else:
                    time.append(zone_count.use_conditions.profile_persons[i-1])
                    time.append(zone_count.use_conditions.profile_machines[i-1])
                    time.append(zone_count.use_conditions.profile_lighting[i-1])

#            zone_count.use_conditions.profile_persons.pop(0)
#            zone_count.use_conditions.profile_machines.pop(0)
#            zone_count.use_conditions.profile_lighting.pop(0)
        internal_boundary = np.array(time_line)

        scipy.io.savemat(path,
                         mdict={'Internals': internal_boundary},
                         appendmat=False,
                         format='4')

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
    def calculation_method(self):

        return self._calculation_method

    @calculation_method.setter
    def calculation_method(self, value):

        ass_error_1 = "calculation_method has to be vdi or ebc"

        assert value != "ebc" or value != "vdi", ass_error_1

        if self.parent is None and value is None:
            self._calculation_method = "vdi"
        elif self.parent is not None and value is None:
            self._calculation_method = self.parent.calculation_method
        elif value is not None:
            self._calculation_method = value
