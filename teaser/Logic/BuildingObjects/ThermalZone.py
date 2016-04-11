# created June 2015
# by TEASER4 Development Team
from __future__ import division
import math
import re
import collections
import random
import warnings
import re


class ThermalZone(object):
    '''This class represents a Thermal Zone in a building


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
        Random id for the destinction between different zones

    name : str
        Individual name

    area : float
        Area of zone im m^2

    volume : float
        Volume of zone in m^3

    infiltration_rate : float
        Infiltration rate of zone in 1/h

    outer_walls : list
        List with all outer walls including ground floor and rooftop

    use_conditions : instance of UseConditions()
        Class of UseConditions with all relevant information for the usage
        of the thermal zone

    inner_walls : list
        List with all inner walls including  floor and ceiling

    typical_length : list
        List with all inner walls including  floor and ceiling
        
    t_inside : float
        normative indoor temperature for static heat load calculation.
        The input of t_inside is ALWAYS in Kelvin
        
    t_outside : float
        normative outdoor temperature for static heat load calculation.
        The input of t_inside is ALWAYS in Kelvin
    '''

    def __init__(self, parent=None):
        '''Constructor for ThermalZone

        '''

        self.parent = parent
        self.internal_id = random.random()
        self.name = None
        self._area = None
        self._volume = None
        self._infiltration_rate = 0.5
        self._outer_walls = []
        self._inner_walls = []
        self._windows = []
        self._use_conditions = None
        self.typical_length = None
        self.typical_width = None
        self._t_inside = 293.15
        self._t_outside = 261.15
        self.density_air = 1.19     # only export for now
        self.heat_capac_air = 1007  # only export for now
        self.t_ground = 286.15  # groundtemperature of for the simulation

        # Calculated values for InnerWall for each Zone
        self.r1_iw = 0.0
        self.c1_iw = 0.0
        self.ua_value_iw = 0.0
        self.r_conv_iw = 0.0
        self.r_rad_iw = 0.0
        self.r_comb_iw = 0.0
        self.area_iw = 0.0
        self.alpha_conv_iw = 0.0
        self.alpha_rad_iw = 0.0
        self.alpha_comb_iw = 0.0

        # Calculated values for OuterWall for each Zone
        self.r1_ow = 0.0
        self.c1_ow = 0.0
        self.r_rest_ow = 0.0
        self.r_total = 0.0
        self.weightfactor_ow = []
        self.weightfactor_ow_dict = {}
        self.weightfactor_ground = []
        self.tilt_wall = []
        self.orientation_wall = []
        self.ua_value_ow = 0.0
        self.r_conv_inner_ow = 0.0
        self.r_rad_inner_ow = 0.0
        self.r_comb_inner_ow = 0.0
        self.r_conv_outer_ow = 0.0
        self.r_rad_outer_ow = 0.0
        self.r_comb_outer_ow = 0.0
        self.area_ow = 0.0
        self.alpha_comb_inner_ow = 0.0
        self.alpha_conv_inner_ow = 0.0
        self.alpha_comb_outer_ow = 0.0
        self.alpha_conv_outer_ow = 0.0
        self.r_rad_ow_iw = 0.0

        # Calculated values for windows for each Zone
        self.r1_win = 0.0
        self.weightfactor_win = []
        self.g_sunblind_list = []
        self.window_area_list = []
        self.orientation_win = []
        self.tilt_win = []
        self.ua_value_win = 0.0
        self.r_conv_inner_win = 0.0
        self.r_rad_inner_win = 0.0
        self.r_comb_inner_win = 0.0
        self.r_conv_outer_win = 0.0
        self.r_rad_outer_win = 0.0
        self.r_comb_outer_win = 0.0
        self.area_win = 0.0
        self.alpha_conv_inner_win = 0.0
        self.alpha_comb_outer_win = 0.0
        self.alpha_conv_outer_win = 0.0
        self.weighted_g_value = 0.0
        self.heating_load = 0.0
        self.cooling_load = 0.0

    def calc_zone_parameters(self, calculation_core='vdi'):
        '''RC-Calculation.

        This functions calculates and sets all necessary parameters for the
        zone. The Algorithm follows the VDI 6007 standard ('vdi') or an
        adapted version ('ebc').

        Parameters
        ----------
        calculation_core : str
            Setter of the used calculation core ('vdi' or 'ebc'), default:'vdi'
        '''

        self.set_calc_default()
        # Calculation of the equivalent resistances and capacities
        if len(self.outer_walls) > 0:
            for out_wall in self.outer_walls:
                out_wall.calc_equivalent_res()
                out_wall.calc_ua_value()
                self.orientation_wall.append(out_wall.orientation)
                self.tilt_wall.append(out_wall.tilt)

        else:
            warnings.warn("No outer walls are defined")

        if len(self.inner_walls) > 0:
            for in_wall in self.inner_walls:
                in_wall.calc_equivalent_res()
                in_wall.calc_ua_value()

        else:
            warnings.warn("No outer walls are defined")

        if len(self.windows) > 0:
            for win in self.windows:
                win.calc_equivalent_res()
                win.calc_ua_value()
                self.orientation_win.append(win.orientation)
                self.tilt_win.append(win.tilt)

        else:
            warnings.warn("No outer walls are defined")

        self.combine_building_elements()
        self.parallel_connection(calculation_core)
        self.calc_weightfactors(calculation_core)
        self.calc_heat_load()

    def parallel_connection(self, calculation_core, t_bt=5):
        '''Parallel connection of several building elements.

        According to VDI 6007 this function sets all building element of the
        same type in parallel and calculates the total resistance and active
        capacity.

        Parameters
        ----------
        calculation_core : str
            Setter of the used calculation core ('vdi' or 'ebc')

        t_bt : int
            Time constant according to VDI 6007 (default t_bt = 5)
        '''

        omega = 2 * math.pi / 86400 / t_bt
        if len(self.outer_walls) > 0:

            if len(self.outer_walls) == 1:
                self.r1_ow = self.outer_walls[0].r1
                self.c1_ow = self.outer_walls[0].c1_korr

            else:
                self.r1_ow, self.c1_ow = \
                        self.calc_rc_wall_help(self.outer_walls, omega)
        else:
            pass

        if len(self.inner_walls) > 0:

            if len(self.inner_walls) == 1:
                self.r1_iw = self.inner_walls[0].r1
                self.c1_iw = self.inner_walls[0].c1

            else:
                self.r1_iw, self.c1_iw = \
                        self.calc_rc_wall_help(self.inner_walls, omega)
        else:
            pass

        if calculation_core == 'vdi':

            if len(self.outer_walls) > 0 and len(self.windows) > 0:
                for win_count in self.windows:
                    self.r1_win += 1/(win_count.r1/6)

                self.r1_ow = 1/(1/self.r1_ow + (self.r1_win))
                self.r_total = 1/(self.ua_value_ow + self.ua_value_win)
                self.r_rad_ow_iw = 1/((1/self.r_rad_inner_ow) +
                                      (1/self.r_rad_inner_win))
                self.r_rest_ow = self.r_total - self.r1_ow - \
                    1/((1/self.r_conv_inner_ow) +
                       (1/self.r_conv_inner_win)+(1/self.r_rad_ow_iw))
            else:
                warnings.warn("As no outer walls or no windows are defined\
                    lumped parameter cannot be calculated")

        elif calculation_core == 'ebc':
            if len(self.outer_walls) > 0 and len(self.windows) > 0:
                sum_r1_win = 0
                for win_count in self.windows:
                    sum_r1_win += 1/((win_count.r1) + win_count.r_outer_comb)

                self.r1_win = 1/sum_r1_win

                self.r1_ow = 1/(1/self.r1_ow)

                self.r_total = 1/(self.ua_value_ow)
                self.r_rad_ow_iw = 1/((1/self.r_rad_inner_ow))
                self.r_rest_ow = self.r_total - self.r1_ow - \
                    1/(1/self.r_conv_inner_ow+1/self.r_rad_ow_iw)
            else:
                warnings.warn("As no outer walls or no windows are defined\
                    lumped parameter cannot be calculated")

        else:
            raise ValueError("specify calculation method correctly")

    def calc_rc_wall_help(self, element_list, omega):
        '''Matrix calculation.

        This is a helper function for def parallel_connection() to keep the
        code clean.

        Parameters
        ----------
        wall_count : list
            List of inner or outer walls

        omega : float
            VDI 6007 frequency

        Returns
        ----------
        r1 : float
            VDI 6007 resistance for inner or outer walls

        c1 : float
            VDI 6007 capacity for inner or outer walls
        '''

        for wall_count in range(len(element_list)-1):

            if wall_count == 0:

                r1 = (element_list[wall_count].r1 *
                      element_list[wall_count].c1**2 +
                      element_list[wall_count+1].r1 *
                      element_list[wall_count+1].c1**2 + omega**2 *
                      element_list[wall_count].r1 *
                      element_list[wall_count+1].r1 *
                      (element_list[wall_count].r1 +
                      element_list[wall_count+1].r1) *
                      element_list[wall_count].c1**2 *
                      element_list[wall_count+1].c1**2) / \
                    ((element_list[wall_count].c1 +
                      element_list[wall_count+1].c1)**2 + omega**2 *
                     (element_list[wall_count].r1 +
                      element_list[wall_count+1].r1)**2 *
                     element_list[wall_count].c1**2 *
                     element_list[wall_count+1].c1**2)

                c1 = ((element_list[wall_count].c1 +
                       element_list[wall_count+1].c1)**2 + omega**2 *
                      (element_list[wall_count].r1 +
                       element_list[wall_count+1].r1)**2 *
                      element_list[wall_count].c1**2 *
                      element_list[wall_count+1].c1**2) / \
                    (element_list[wall_count].c1 +
                     element_list[wall_count+1].c1 + omega**2 *
                     (element_list[wall_count].r1**2 *
                     element_list[wall_count].c1 +
                     element_list[wall_count+1].r1**2 *
                     element_list[wall_count+1].c1) *
                     element_list[wall_count].c1 *
                     element_list[wall_count+1].c1)
            else:
                r1x = r1
                c1x = c1
                r1 = (r1x * c1x**2 + element_list[wall_count+1].r1 *
                      element_list[wall_count+1].c1**2 +
                      omega**2 * r1x * element_list[wall_count+1].r1 *
                      (r1x + element_list[wall_count+1].r1) *
                      c1x**2 * element_list[wall_count+1].c1**2) / \
                    ((c1x + element_list[wall_count+1].c1)**2 +
                     omega**2 * (r1x + element_list[wall_count+1].r1)**2 *
                     c1x**2 * element_list[wall_count+1].c1**2)

                c1 = ((c1x+element_list[wall_count+1].c1)**2 + omega**2 *
                      (r1x + element_list[wall_count+1].r1)**2 * c1x**2 *
                      element_list[wall_count+1].c1**2) / \
                     (c1x + element_list[wall_count+1].c1 + omega**2 *
                      (r1x**2 * c1x + element_list[wall_count+1].r1**2 *
                       element_list[wall_count+1].c1) * c1x *
                      element_list[wall_count+1].c1)
        return r1, c1

    def combine_building_elements(self):
        '''Combines values of several building elements.

        Sums UA-Values, R-Values and area. Calculates the weighted coeffiecient
        of heat transfer for walls, windows. Calculates the weighted g-Value
        for windows.
        '''

        sum_r_conv_iw = 0
        sum_r_rad_iw = 0
        sum_r_comb_iw = 0
        sum_r_conv_inner_ow = 0
        sum_r_rad_inner_ow = 0
        sum_r_comb_inner_ow = 0
        sum_r_conv_outer_ow = 0
        sum_r_rad_outer_ow = 0
        sum_r_comb_outer_ow = 0
        sum_r_conv_inner_win = 0
        sum_r_rad_inner_win = 0
        sum_r_comb_inner_win = 0
        sum_r_conv_outer_win = 0
        sum_r_rad_outer_win = 0
        sum_r_comb_outer_win = 0
        sum_g_value = 0
        sum_area_ow_rt = 0

        for wall_count in self.inner_walls:
            self.ua_value_iw += wall_count.ua_value

            sum_r_conv_iw += 1/(wall_count.r_inner_conv)
            sum_r_rad_iw += 1/(wall_count.r_inner_rad)
            sum_r_comb_iw += 1/(wall_count.r_inner_comb)

            self.area_iw += wall_count.area

        self.r_conv_iw = 1/sum_r_conv_iw
        self.r_rad_iw = 1/sum_r_rad_iw
        self.r_comb_iw = 1/sum_r_comb_iw

        self.alpha_conv_iw = (1/(self.r_conv_iw*self.area_iw))
        self.alpha_rad_iw = 1/(self.r_rad_iw*self.area_iw)
        self.alpha_comb_iw = 1/(self.r_comb_iw*self.area_iw)

        for wall_count in self.outer_walls:

            self.ua_value_ow += wall_count.ua_value

            sum_r_conv_inner_ow += 1/(wall_count.r_inner_conv)
            sum_r_rad_inner_ow += 1/(wall_count.r_inner_rad)
            sum_r_comb_inner_ow += 1/(wall_count.r_inner_comb)

            self.area_ow += wall_count.area

            if type(wall_count).__name__ == "OuterWall" \
                    or type(wall_count).__name__ == "Rooftop":
                sum_r_conv_outer_ow += 1/(wall_count.r_outer_conv)
                sum_r_rad_outer_ow += 1/(wall_count.r_outer_rad)
                sum_r_comb_outer_ow += 1/(wall_count.r_outer_comb)
                sum_area_ow_rt += wall_count.area
            else:
                pass

        self.r_conv_inner_ow = 1/sum_r_conv_inner_ow
        self.r_rad_inner_ow = 1/sum_r_rad_inner_ow
        self.r_comb_inner_ow = 1/sum_r_comb_inner_ow
        self.r_conv_outer_ow = 1/sum_r_conv_outer_ow
        self.r_rad_outer_ow = 1/sum_r_rad_outer_ow
        self.r_comb_outer_ow = 1/sum_r_comb_outer_ow

        self.alpha_conv_inner_ow = (1/(self.r_conv_inner_ow*self.area_ow))
        self.alpha_comb_inner_ow = (1/(self.r_comb_inner_ow*self.area_ow))
        self.alpha_conv_outer_ow = (1/(self.r_conv_outer_ow*sum_area_ow_rt))
        self.alpha_comb_outer_ow = (1/(self.r_comb_outer_ow*sum_area_ow_rt))

        for count_win in self.windows:

            self.ua_value_win += count_win.ua_value

            sum_r_conv_inner_win += 1/(count_win.r_inner_conv)
            sum_r_rad_inner_win += 1/(count_win.r_inner_rad)
            sum_r_comb_inner_win += 1/(count_win.r_inner_comb)
            sum_r_conv_outer_win += 1/(count_win.r_outer_conv)
            sum_r_rad_outer_win += 1/(count_win.r_outer_rad)
            sum_r_comb_outer_win += 1/(count_win.r_outer_comb)

            sum_g_value += count_win.g_value * count_win.area

            self.area_win += count_win.area

        self.r_conv_inner_win = 1/sum_r_conv_inner_win
        self.r_rad_inner_win = 1/sum_r_rad_inner_win
        self.r_comb_inner_win = 1/sum_r_comb_inner_win
        self.r_conv_outer_win = 1/sum_r_conv_outer_win
        self.r_rad_outer_win = 1/sum_r_rad_outer_win
        self.r_comb_outer_win = 1/sum_r_comb_outer_win

        self.alpha_conv_inner_win = (1/(self.r_conv_inner_win*self.area_win))
        self.alpha_comb_outer_win = (1/(self.r_comb_outer_win*self.area_win))
        self.alpha_conv_outer_win = (1/(self.r_conv_outer_win*self.area_win))

        self.weighted_g_value = sum_g_value / self.area_win

    def calc_weightfactors(self, calculation_core):
        '''Calculation of weightfactors.

        Calculates the weightfactors of the outer walls, including ground and
        windows.

        Parameters
        ----------
        calculation_core : str
            Setter of the used calculation core ('vdi' or 'ebc'), default:'vdi'
        '''

        if calculation_core == 'vdi':

            for wall in self.outer_walls:
                wall.wf_out = wall.ua_value/(self.ua_value_ow +
                                                     self.ua_value_win)
                if type(wall).__name__ == "GroundFloor":
                    self.weightfactor_ground.append(wall.wf_out)
                else:
                    pass

            for win in self.windows:
                win.wf_out = win.ua_value/(self.ua_value_ow +
                                                     self.ua_value_win)

        elif calculation_core == 'ebc':

            for wall in self.outer_walls:
                wall.wf_out = wall.ua_value/self.ua_value_ow
                if type(wall).__name__ == "GroundFloor":
                    self.weightfactor_ground.append(wall.wf_out)
                else:
                    pass

            for win in self.windows:
                win.wf_out = win.ua_value/self.ua_value_win

        else:
            raise ValueError("specify calculation method correctly")


    def find_wall(self, orientation):
        wall_list = []
        for i in self.outer_walls:
            if i.orientation == orientation:
                wall_list.append(i)
            else:
                pass
        if len(wall_list) != 0:
            return wall_list
        else:
            return None

    def find_win(self, orientation):
        win_list = []
        for i in self.windows:
            if i.orientation == orientation:
                return i
            else:
                pass
        else:
            return None

    def find_win_wall(self, orientation):
        win_list = []
        wall_list = []
        for i in self.outer_walls:
            if i.orientation == orientation:
                wall_list.append(i)
                if self.find_win(orientation) in win_list:
                    win_list.append(None)
                else:
                    win_list.append(self.find_win(orientation))
            else:
                pass
        if len(wall_list) != 0:
            return wall_list, win_list
        else:
            return None


    def set_inner_wall_area(self):
        '''Sets the inner wall area.

        Sets the inner wall area according to zone area size if type building
        approach is used.
        '''

        ass_error_1 = "You need to specify parent for thermal zone"

        assert self.parent is not None, ass_error_1

        for wall in self.inner_walls:
            if type(wall).__name__ == "Ceiling"\
              or type(wall).__name__ == "Floor":

                wall.area = ((self.parent.number_of_floors-1) /
                             self.parent.number_of_floors)*self.area
            else:
                typical_area = self.typical_length*self.typical_width

                avg_room_nr = self.area/typical_area

                wall.area = (avg_room_nr*(self.typical_length *
                                          self.parent.height_of_floors +
                                          2*self.typical_width *
                                          self.parent.height_of_floors))

    def set_volume_zone(self):
        '''Sets the zone volume.

        Sets the volume of a zone according area and height of floors
        (building attribute).
        '''

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

    def calc_heat_load(self):
        '''Norm heat load calculation.

        Calculates the norm heat load of the thermal zone.
        '''

        _heat_capac_air = 1.002
        _density_air = 1.25

        self.heating_load = ((self.ua_value_ow+self.ua_value_win) +
                             self.volume * self.infiltration_rate *
                             _heat_capac_air*_density_air) * \
                            (self.t_inside - self.t_outside)

    def retrofit_zone(self, window_type=None, material=None):
        '''Retrofits all walls and windows in the zone.
        '''

        for wall_count in self.outer_walls:
            wall_count.retrofit_wall(self.parent.year_of_retrofit, material)
        for win_count in self.windows:
            win_count.replace_window(self.parent.year_of_retrofit, window_type)

    def set_calc_default(self):

        # Calculated values for InnerWall for each Zone
        self.r1_iw = 0.0
        self.c1_iw = 0.0
        self.ua_value_iw = 0.0
        self.r_conv_iw = 0.0
        self.r_rad_iw = 0.0
        self.r_comb_iw = 0.0
        self.area_iw = 0.0
        self.alpha_conv_iw = 0.0
        self.alpha_rad_iw = 0.0
        self.alpha_comb_iw = 0.0

        # Calculated values for OuterWall for each Zone
        self.r1_ow = 0.0
        self.c1_ow = 0.0
        self.r_rest_ow = 0.0
        self.r_total = 0.0
        self.weightfactor_ow = []
        self.weightfactor_ground = []
        self.orientation_wall = []
        self.ua_value_ow = 0.0
        self.r_conv_inner_ow = 0.0
        self.r_rad_inner_ow = 0.0
        self.r_comb_inner_ow = 0.0
        self.r_conv_outer_ow = 0.0
        self.r_rad_outer_ow = 0.0
        self.r_comb_outer_ow = 0.0
        self.area_ow = 0.0
        self.alpha_comb_inner_ow = 0.0
        self.alpha_conv_inner_ow = 0.0
        self.alpha_comb_outer_ow = 0.0
        self.alpha_conv_outer_ow = 0.0
        self.r_rad_ow_iw = 0.0

        # Calculated values for windows for each Zone
        self.r1_win = 0.0
        self.weightfactor_win = []
        self.g_sunblind_list = []
        self.window_area_list = []
        self.orientation_win = []
        self.ua_value_win = 0.0
        self.r_conv_inner_win = 0.0
        self.r_rad_inner_win = 0.0
        self.r_comb_inner_win = 0.0
        self.r_conv_outer_win = 0.0
        self.r_rad_outer_win = 0.0
        self.r_comb_outer_win = 0.0
        self.area_win = 0.0
        self.alpha_conv_inner_win = 0.0
        self.alpha_comb_outer_win = 0.0
        self.alpha_conv_outer_win = 0.0
        self.weighted_g_value = 0.0

        self.heating_load = 0.0
        self.cooling_load = 0.0

    def delete(self):
        '''Deletes the actual thermal zone and refreshs the thermal zones of
        the building
        '''
        for index, tz in enumerate(self.parent.thermal_zones):
            if tz.internal_id == self.internal_id:
                self.parent.net_leased_area -= self.area
                self.parent.thermal_zones.pop(index)

                break
    def add_element(self, building_element):
        '''Adds a building element to the corresponding list

        This function adds a BuildingElement instance to the the list
        depending on the type of the Building Element

        Parameters
        ----------
        building_element : BuildingElement()
            inherited objects of BuildingElement() instance of TEASER

        '''

        ass_error_1 = ("building element has to be an instance of OuterWall(),"
        " Rooftop(), GroundFloor(), Window(), InnerWall(), Ceiling() or "
                       "Floor()")

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

        elif type(building_element).__name__ in ("Window"):
            self._windows.append(building_element)



    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        if value is not None:
            ass_error_1 = "Parent has to be an instance of Building()"

            assert type(value).__name__ == "Building" \
                or type(value).__name__ == "Office"\
                or type(value).__name__ == "Institute"\
                or type(value).__name__ == "Institute4"\
                or type(value).__name__ == "Institute8" \
                or type(value).__name__ == "Residential", ass_error_1

            self.__parent = value

        if type(value).__name__ == "Building" \
           or type(value).__name__ == "Office" \
           or type(value).__name__ == "Institute" \
           or type(value).__name__ == "Institute4" \
           or type(value).__name__ == "Institute8" \
           or type(value).__name__ == "Residential":

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

        assert type(value).__name__ == ("UseConditions") or \
            type(value).__name__ == ("UseConditions18599"), ass_error_1

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
