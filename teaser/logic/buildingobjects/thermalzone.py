# created June 2015
# by TEASER4 Development Team

from __future__ import division
import math
import random
import warnings
import re


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

    rooftops : list
        List with rooftops if number of elements is 4

    grounfdloors : list
        List with grounfdloors if number of elements is >2

    outerwalls_help : list
        List with outer walls and rooftops if number of elements is >2
        List with outer walls only if number of elements is 4

    windows : list
        List with windows

    use_conditions : instance of UseConditions()
        Class of UseConditions with all relevant information for the usage
        of the thermal zone

    inner_walls : list
        List with all inner walls including  floor and ceiling

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

    consider_heat_capacity : bool
        decides whether air capacity is considered or not within the simulation

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
        self._infiltration_rate = 0.5
        self._outer_walls = []
        self._inner_walls = []
        self.rooftops = []
        self.ground_floors = []
        self._windows = []
        self.outer_walls_help = []
        self._use_conditions = None
        self.typical_length = None
        self.typical_width = None
        self._t_inside = 293.15
        self._t_outside = 261.15
        self.density_air = 1.19  # only export for now
        self.heat_capac_air = 1007  # only export for now
        self.t_ground = 286.15  # groundtemperature of for the simulation
        self.consider_air_capacity = True

        # Calculated values for InnerWall for each Zone
        self.r1_iw = 0.0
        self.c1_iw = 0.0
        self.ua_value_iw = 0.0
        self.r_conv_iw = 0.0
        self.r_rad_iw = 0.0
        self.r_comb_iw = 0.0
        self.area_iw = 0.0
        self.r_conv_inner_iw = 0.0
        self.r_rad_inner_iw = 0.0
        self.r_comb_inner_iw = 0.0
        self.r_conv_outer_iw = 0.0
        self.r_rad_outer_iw = 0.0
        self.r_comb_outer_iw = 0.0

        self.alpha_conv_inner_iw = 0.0
        self.alpha_rad_inner_iw = 0.0
        self.alpha_comb_inner_iw = 0.0

        self.alpha_conv_outer_iw = 0.0
        self.alpha_rad_outer_iw = 0.0
        self.alpha_comb_outer_iw = 0.0

        # Calculated values for OuterWall for each Zone
        self.r1_ow = 0.0
        self.c1_ow = 0.0
        self.r_rest_ow = 0.0
        self.r_total_ow = 0.0

        self.weightfactor_ow = []
        self.weightfactor_ground = []
        self.tilt_wall = []
        self.orientation_wall = []
        self.outer_walls_areas = []

        self.ua_value_ow = 0.0
        self.r_conv_inner_ow = 0.0
        self.r_rad_inner_ow = 0.0
        self.r_comb_inner_ow = 0.0
        self.r_conv_outer_ow = 0.0
        self.r_rad_outer_ow = 0.0
        self.r_comb_outer_ow = 0.0
        self.area_ow = 0.0

        self.alpha_conv_inner_ow = 0.0
        self.alpha_rad_inner_ow = 0.0
        self.alpha_comb_inner_ow = 0.0

        self.alpha_conv_outer_ow = 0.0
        self.alpha_rad_outer_ow = 0.0
        self.alpha_comb_outer_ow = 0.0

        self.ir_emissivity_outer_ow = 0.0
        self.ir_emissivity_inner_ow = 0.0
        self.solar_absorp_ow = 0.0

        self.r_rad_ow_iw = 0.0

        # Calculated values for Rooftop for each Zone
        self.r1_rt = 0.0
        self.c1_rt = 0.0
        self.r_rest_rt = 0.0
        self.r_total_rt = 0.0
        self.weightfactor_rt = []
        self.tilt_rt = []
        self.orientation_rt = []
        self.ua_value_rt = 0.0
        self.r_conv_inner_rt = 0.0
        self.r_rad_inner_rt = 0.0
        self.r_comb_inner_rt = 0.0
        self.r_conv_outer_rt = 0.0
        self.r_rad_outer_rt = 0.0
        self.r_comb_outer_rt = 0.0
        self.area_rt = 0.0

        self.alpha_conv_inner_rt = 0.0
        self.alpha_rad_inner_rt = 0.0
        self.alpha_comb_inner_rt = 0.0

        self.alpha_conv_outer_rt = 0.0
        self.alpha_rad_outer_rt = 0.0
        self.alpha_comb_outer_rt = 0.0

        self.ir_emissivity_outer_rt = 0.0
        self.ir_emissivity_inner_rt = 0.0
        self.solar_absorp_rt = 0.0

        self.r_rad_rt_iw = 0.0

        # Calculated values for GroundFlor for each Zone
        self.r1_gf = 0.0
        self.c1_gf = 0.0
        self.r_rest_gf = 0.0
        self.r_total_gf = 0.0
        self.weightfactor_gf = []
        self.tilt_gf = []
        self.orientation_gf = []
        self.ua_value_gf = 0.0
        self.r_conv_inner_gf = 0.0
        self.r_rad_inner_gf = 0.0
        self.r_comb_inner_gf = 0.0
        self.r_conv_outer_gf = 0.0
        self.r_rad_outer_gf = 0.0
        self.r_comb_outer_gf = 0.0
        self.area_gf = 0.0

        self.alpha_conv_inner_gf = 0.0
        self.alpha_rad_inner_gf = 0.0
        self.alpha_comb_inner_gf = 0.0

        self.alpha_conv_outer_gf = 0.0
        self.alpha_rad_outer_gf = 0.0
        self.alpha_comb_outer_gf = 0.0

        self.ir_emissivity_inner_gf = 0.0
        self.solar_absorp_gf = 0.0  # necessary? @PRemmen

        self.r_rad_gf_iw = 0.0

        # Calculated values for windows for each Zone
        self.r1_win = 0.0
        self.weightfactor_win = []
        self.g_sunblind_list = []
        self.window_areas = []
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
        self.alpha_rad_inner_win = 0.0
        self.alpha_comb_inner_win = 0.0

        self.alpha_conv_outer_win = 0.0
        self.alpha_rad_outer_win = 0.0
        self.alpha_comb_outer_win = 0.0
        self.solar_absorp_win = 0.0
        self.ir_emissivity_win = 0.0

        self.weighted_g_value = 0.0
        self.heating_load = 0.0
        self.cooling_load = 0.0

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

        self.set_calc_default()

        if len(self.outer_walls) > 0:
            for out_wall in self.outer_walls:
                out_wall.calc_equivalent_res()
                out_wall.calc_ua_value()
        else:
            warnings.warn("No outer walls are defined, this will cause you a "
                          "lot of troubles")

        if len(self.inner_walls) > 0:
            for in_wall in self.inner_walls:
                in_wall.calc_equivalent_res()
                in_wall.calc_ua_value()
        else:
            warnings.warn("No inner walls are defined")

        if len(self.windows) > 0:
            for win in self.windows:
                win.calc_equivalent_res()
                win.calc_ua_value()
        else:
            warnings.warn("No window are defined, this may eventually cause "
                          "you some troubles")

        self.sum_building_elements()
        if number_of_elements == 1:
            self.calc_one_element(merge_windows=merge_windows, t_bt=t_bt)
            self.calc_wf_one_element(merge_windows=merge_windows)
        elif number_of_elements == 2:
            self.calc_two_element(merge_windows=merge_windows, t_bt=t_bt)
            self.calc_wf_two_element(merge_windows=merge_windows)
        elif number_of_elements == 3:
            self.calc_three_element(merge_windows=merge_windows, t_bt=t_bt)
            self.calc_wf_three_element(merge_windows=merge_windows)
        elif number_of_elements == 4:
            self.calc_four_element(merge_windows=merge_windows, t_bt=t_bt)
            self.calc_wf_four_element(merge_windows=merge_windows)

        self.calc_heat_load(number_of_elements=number_of_elements)

    def calc_one_element(self,
                         merge_windows,
                         t_bt):

        pass

    def calc_two_element(self,
                         merge_windows,
                         t_bt):
        """calcs lumped parameter for two element model

        Parameters
        ----------

        merge_windows : bool
            True for merging the windows into the outer walls, False for
            separate resistance for window, default is False
        """
        omega = 2 * math.pi / 86400 / t_bt

        self.ua_value_ow += (self.ua_value_gf + self.ua_value_rt)

        if self.r_conv_inner_gf != 0:
            self.r_conv_inner_ow = 1 / ((1 / self.r_conv_inner_ow) + (
                1 / self.r_conv_inner_gf))
        if self.r_rad_inner_gf != 0:
            self.r_rad_inner_ow = 1 / ((1 / self.r_rad_inner_ow) + (
                1 / self.r_rad_inner_gf))

        if self.r_conv_inner_rt != 0:
            self.r_conv_inner_ow = 1 / ((1 / self.r_conv_inner_ow) + (
                1 / self.r_conv_inner_rt))
        if self.r_rad_inner_rt != 0:
            self.r_rad_inner_ow = 1 / ((1 / self.r_rad_inner_ow) + (
                1 / self.r_rad_inner_rt))

        if len(self.outer_walls) > 0:
            if len(self.outer_walls) == 1:
                self.r1_ow = self.outer_walls[0].r1
                self.c1_ow = self.outer_walls[0].c1_korr
            else:
                self.r1_ow, self.c1_ow = \
                    self.calc_chain_matrix(self.outer_walls, omega)
        else:
            pass

        if len(self.inner_walls) > 0:
            if len(self.inner_walls) == 1:
                self.r1_iw = self.inner_walls[0].r1
                self.c1_iw = self.inner_walls[0].c1
            else:
                self.r1_iw, self.c1_iw = \
                    self.calc_chain_matrix(self.inner_walls, omega)
        else:
            pass

        if merge_windows is False:
            # this used to be calculation_core = ebc
            if len(self.outer_walls) > 0 and len(self.windows) > 0:
                sum_r1_win = 0
                for win_count in self.windows:
                    sum_r1_win += 1 / (win_count.r1 + win_count.r_outer_comb)

                self.r1_win = 1 / sum_r1_win

                self.r1_ow = 1 / (1 / self.r1_ow)

                self.r_total_ow = 1 / self.ua_value_ow
                self.r_rad_ow_iw = 1 / (1 / self.r_rad_inner_ow)
                self.r_rest_ow = self.r_total_ow - self.r1_ow - \
                    1 / (1 / self.r_conv_inner_ow + 1 / self.r_rad_ow_iw)
                self.ir_emissivity_outer_ow = \
                    ((self.ir_emissivity_outer_ow * self.area_ow) +
                     (self.ir_emissivity_outer_rt *
                      self.area_rt)) / \
                    (self.area_ow + self.area_rt)
                self.ir_emissivity_inner_ow = \
                    ((self.ir_emissivity_inner_ow * self.area_ow) +
                     (self.ir_emissivity_inner_rt * self.area_rt) +
                     (self.ir_emissivity_inner_gf *
                      self.area_gf)) / \
                    (self.area_ow + self.area_rt + self.area_gf)
                self.solar_absorp_ow = \
                    ((self.solar_absorp_ow * self.area_ow) +
                     (self.solar_absorp_rt * self.area_rt) +
                     (self.solar_absorp_gf * self.area_gf)) / \
                    (self.area_ow + self.area_rt + self.area_gf)

            else:
                warnings.warn("As no outer walls or no windows are defined\
                    lumped parameter cannot be calculated")

        if merge_windows is True:
            # this used to be calculation_core = vdi
            if len(self.outer_walls) > 0:
                for win_count in self.windows:
                    self.r1_win += 1 / (win_count.r1 / 6)

                self.r1_ow = 1 / (1 / self.r1_ow + self.r1_win)
                self.r_total_ow = 1 / (self.ua_value_ow + self.ua_value_win)
                self.r_rad_ow_iw = 1 / ((1 / self.r_rad_inner_ow) +
                                        (1 / self.r_rad_inner_win))
                self.r_rest_ow = self.r_total_ow - self.r1_ow - \
                    1 / ((1 / self.r_conv_inner_ow) + (1 /
                                                       self.r_conv_inner_win) +
                         (1 / self.r_rad_ow_iw))
                self.ir_emissivity_outer_ow = \
                    ((self.ir_emissivity_outer_ow * self.area_ow) +
                     (self.ir_emissivity_outer_rt * self.area_rt) +
                     (self.ir_emissivity_win * self.area_win)) / \
                    (self.area_ow + self.area_rt + self.area_win)
                self.ir_emissivity_inner_ow = \
                    ((self.ir_emissivity_inner_ow * self.area_ow) +
                     (self.ir_emissivity_inner_rt * self.area_rt) +
                     (self.ir_emissivity_inner_gf * self.area_gf) +
                     (self.ir_emissivity_win * self.area_win)) / \
                    (self.area_ow + self.area_rt + self.area_gf +
                     self.area_win)
                self.solar_absorp_ow = \
                    ((self.solar_absorp_ow * self.area_ow) +
                     (self.solar_absorp_rt * self.area_rt) +
                     (self.solar_absorp_gf * self.area_gf) +
                     (self.solar_absorp_win * self.area_win)) / \
                    (self.area_ow + self.area_rt + self.area_gf +
                     self.area_win)

            else:
                warnings.warn("As no outer walls or no windows are defined\
                    lumped parameter cannot be calculated")

        self.area_ow += (self.area_gf + self.area_rt)
        self.alpha_conv_inner_ow = (1 / (self.r_conv_inner_ow * self.area_ow))
        self.alpha_rad_inner_ow = (1 / (self.r_rad_inner_ow * self.area_ow))

    def calc_three_element(self,
                           merge_windows,
                           t_bt):
        """calcs lumped parameter for three element model
        """
        omega = 2 * math.pi / 86400 / t_bt

        for wall in self.outer_walls:
            if type(wall).__name__ == "OuterWall" or type(wall).__name__ == \
                    "Rooftop":
                self.outer_walls_help.append(wall)
            if type(wall).__name__ == "GroundFloor":
                self.ground_floors.append(wall)

        self.ua_value_ow += self.ua_value_rt

        if self.r_conv_inner_rt != 0:
            self.r_conv_inner_ow = 1 / ((1 / self.r_conv_inner_ow) + (
                1 / self.r_conv_inner_rt))
        if self.r_rad_inner_rt != 0:
            self.r_rad_inner_ow = 1 / ((1 / self.r_rad_inner_ow) + (
                1 / self.r_rad_inner_rt))

        if len(self.outer_walls_help) > 0:
            if len(self.outer_walls_help) == 1:
                self.r1_ow = self.outer_walls_help[0].r1
                self.c1_ow = self.outer_walls_help[0].c1_korr
            else:
                self.r1_ow, self.c1_ow = \
                    self.calc_chain_matrix(self.outer_walls_help, omega)
        else:
            pass

        if len(self.ground_floors) > 0:
            with_ground_floors = True
            if len(self.ground_floors) == 1:
                self.r1_gf = self.ground_floors[0].r1
                self.c1_gf = self.ground_floors[0].c1_korr
            else:
                self.r1_gf, self.c1_gf = \
                    self.calc_chain_matrix(self.ground_floors, omega)
        else:
            with_ground_floors = False

        if len(self.inner_walls) > 0:
            if len(self.inner_walls) == 1:
                self.r1_iw = self.inner_walls[0].r1
                self.c1_iw = self.inner_walls[0].c1
            else:
                self.r1_iw, self.c1_iw = \
                    self.calc_chain_matrix(self.inner_walls, omega)
        else:
            pass

        if merge_windows is False:
            if len(self.outer_walls) > 0 and len(self.windows) > 0:
                sum_r1_win = 0
                for win_count in self.windows:
                    sum_r1_win += 1 / (win_count.r1 + win_count.r_outer_comb)

                self.r1_win = 1 / sum_r1_win

                self.r1_ow = 1 / (1 / self.r1_ow)
                if with_ground_floors:
                    self.r1_gf = 1 / (1 / self.r1_gf)

                self.r_total_ow = 1 / self.ua_value_ow
                if with_ground_floors:
                    self.r_total_gf = 1 / self.ua_value_gf

                self.r_rad_ow_iw = 1 / (1 / self.r_rad_inner_ow)
                if with_ground_floors:
                    self.r_rad_gf_iw = 1 / (1 / self.r_rad_inner_gf)

                self.r_rest_ow = self.r_total_ow - self.r1_ow - \
                    1 / (1 / self.r_conv_inner_ow + 1 / self.r_rad_ow_iw)
                if with_ground_floors:
                    self.r_rest_gf = self.r_total_gf - self.r1_gf - \
                        1 / (1 / self.r_conv_inner_gf + 1 / self.r_rad_gf_iw)
                self.ir_emissivity_outer_ow = \
                    ((self.ir_emissivity_outer_ow * self.area_ow) +
                     (self.ir_emissivity_outer_rt *
                      self.area_rt)) / \
                    (self.area_ow + self.area_rt)
                self.ir_emissivity_inner_ow = \
                    ((self.ir_emissivity_inner_ow * self.area_ow) +
                     (self.ir_emissivity_inner_rt * self.area_rt)) / \
                    (self.area_ow + self.area_rt)
                self.solar_absorp_ow = \
                    ((self.solar_absorp_ow * self.area_ow) +
                     (self.solar_absorp_rt * self.area_rt)) / \
                    (self.area_ow + self.area_rt)
            else:
                warnings.warn("As no outer walls or no windows are defined\
                    lumped parameter cannot be calculated")

        if merge_windows is True:
            if len(self.outer_walls) > 0:
                for win_count in self.windows:
                    self.r1_win += 1 / (win_count.r1 / 6)

                self.r1_ow = 1 / (1 / self.r1_ow + self.r1_win)
                if with_ground_floors:
                    self.r1_gf = 1 / (1 / self.r1_gf)

                self.r_total_ow = 1 / (self.ua_value_ow + self.ua_value_win)
                if with_ground_floors:
                    self.r_total_gf = 1 / self.ua_value_gf

                self.r_rad_ow_iw = 1 / ((1 / self.r_rad_inner_ow) +
                                        (1 / self.r_rad_inner_win))
                if with_ground_floors:
                    self.r_rad_gf_iw = 1 / (1 / self.r_rad_inner_gf)

                self.r_rest_ow = self.r_total_ow - self.r1_ow - \
                    1 / ((1 / self.r_conv_inner_ow) + (1 /
                                                       self.r_conv_inner_win) +
                         (1 / self.r_rad_ow_iw))
                if with_ground_floors:
                    self.r_rest_gf = self.r_total_gf - self.r1_gf - \
                        1 / (1 / self.r_conv_inner_gf + 1 / self.r_rad_gf_iw)
                self.ir_emissivity_outer_ow = \
                    ((self.ir_emissivity_outer_ow * self.area_ow) +
                     (self.ir_emissivity_outer_rt * self.area_rt) +
                     (self.ir_emissivity_win * self.area_win)) / \
                    (self.area_ow + self.area_rt + self.area_win)
                self.ir_emissivity_inner_ow = \
                    ((self.ir_emissivity_inner_ow * self.area_ow) +
                     (self.ir_emissivity_inner_rt * self.area_rt) +
                     (self.ir_emissivity_win * self.area_win)) / \
                    (self.area_ow + self.area_rt + self.area_win)
                self.solar_absorp_ow = \
                    ((self.solar_absorp_ow * self.area_ow) +
                     (self.solar_absorp_rt * self.area_rt) +
                     (self.solar_absorp_win * self.area_win)) / \
                    (self.area_ow + self.area_rt + self.area_win)
            else:
                warnings.warn("As no outer walls or no windows are defined\
                    lumped parameter cannot be calculated")

        self.area_ow += self.area_rt
        self.alpha_conv_inner_ow = (1 / (self.r_conv_inner_ow * self.area_ow))
        self.alpha_rad_inner_ow = (1 / (self.r_rad_inner_ow * self.area_ow))

    def calc_four_element(self,
                          merge_windows,
                          t_bt):
        """calcs lumped parameter for two element model
        """
        omega = 2 * math.pi / 86400 / t_bt

        for wall in self.outer_walls:
            if type(wall).__name__ == "OuterWall":
                self.outer_walls_help.append(wall)
            if type(wall).__name__ == "Rooftop":
                self.rooftops.append(wall)
            if type(wall).__name__ == "GroundFloor":
                self.ground_floors.append(wall)

        if len(self.outer_walls_help) > 0:
            if len(self.outer_walls_help) == 1:
                self.r1_ow = self.outer_walls_help[0].r1
                self.c1_ow = self.outer_walls_help[0].c1_korr
            else:
                self.r1_ow, self.c1_ow = \
                    self.calc_chain_matrix(self.outer_walls_help, omega)
        else:
            pass

        if len(self.rooftops) > 0:
            with_rooftops = True
            if len(self.rooftops) == 1:
                self.r1_rt = self.rooftops[0].r1
                self.c1_rt = self.rooftops[0].c1_korr
            else:
                self.r1_rt, self.c1_rt = \
                    self.calc_chain_matrix(self.rooftops, omega)
        else:
            with_rooftops = False

        if len(self.ground_floors) > 0:
            with_ground_floors = True
            if len(self.ground_floors) == 1:
                self.r1_gf = self.ground_floors[0].r1
                self.c1_gf = self.ground_floors[0].c1_korr
            else:
                self.r1_gf, self.c1_gf = \
                    self.calc_chain_matrix(self.ground_floors, omega)
        else:
            with_ground_floors = False

        if len(self.inner_walls) > 0:
            if len(self.inner_walls) == 1:
                self.r1_iw = self.inner_walls[0].r1
                self.c1_iw = self.inner_walls[0].c1
            else:
                self.r1_iw, self.c1_iw = \
                    self.calc_chain_matrix(self.inner_walls, omega)
        else:
            pass

        if merge_windows is False:
            if len(self.outer_walls) > 0 and len(self.windows) > 0:
                sum_r1_win = 0
                for win_count in self.windows:
                    sum_r1_win += 1 / (win_count.r1 + win_count.r_outer_comb)

                self.r1_win = 1 / sum_r1_win

                self.r1_ow = 1 / (1 / self.r1_ow)
                if with_ground_floors:
                    self.r1_gf = 1 / (1 / self.r1_gf)
                if with_rooftops:
                    self.r1_rt = 1 / (1 / self.r1_rt)

                self.r_total_ow = 1 / self.ua_value_ow
                if with_ground_floors:
                    self.r_total_gf = 1 / self.ua_value_gf
                if with_rooftops:
                    self.r_total_rt = 1 / self.ua_value_rt

                self.r_rad_ow_iw = 1 / (1 / self.r_rad_inner_ow)
                if with_ground_floors:
                    self.r_rad_gf_iw = 1 / (1 / self.r_rad_inner_gf)
                if with_rooftops:
                    self.r_rad_rt_iw = 1 / (1 / self.r_rad_inner_rt)

                self.r_rest_ow = self.r_total_ow - self.r1_ow - \
                    1 / (1 / self.r_conv_inner_ow + 1 / self.r_rad_ow_iw)
                if with_ground_floors:
                    self.r_rest_gf = self.r_total_gf - self.r1_gf - \
                        1 / (1 / self.r_conv_inner_gf + 1 / self.r_rad_gf_iw)
                if with_rooftops:
                    self.r_rest_rt = self.r_total_rt - self.r1_rt - \
                        1 / (1 / self.r_conv_inner_rt + 1 / self.r_rad_rt_iw)

            else:
                warnings.warn("As no outer walls or no windows are defined\
                    lumped parameter cannot be calculated")

        if merge_windows is True:
            # this used to be calculation_core = vdi
            if len(self.outer_walls) > 0:
                for win_count in self.windows:
                    self.r1_win += 1 / (win_count.r1 / 6)

                self.r1_ow = 1 / (1 / self.r1_ow + self.r1_win)
                if with_ground_floors:
                    self.r1_gf = 1 / (1 / self.r1_gf)
                if with_rooftops:
                    self.r1_rt = 1 / (1 / self.r1_rt)

                self.r_total_ow = 1 / (self.ua_value_ow + self.ua_value_win)
                if with_ground_floors:
                    self.r_total_gf = 1 / self.ua_value_gf
                if with_rooftops:
                    self.r_total_rt = 1 / self.ua_value_rt

                self.r_rad_ow_iw = 1 / ((1 / self.r_rad_inner_ow) +
                                        (1 / self.r_rad_inner_win))
                if with_ground_floors:
                    self.r_rad_gf_iw = 1 / (1 / self.r_rad_inner_gf)
                if with_rooftops:
                    self.r_rad_rt_iw = 1 / (1 / self.r_rad_inner_rt)

                self.r_rest_ow = self.r_total_ow - self.r1_ow - \
                    1 / ((1 / self.r_conv_inner_ow) + (1 /
                                                       self.r_conv_inner_win) +
                         (1 / self.r_rad_ow_iw))
                if with_ground_floors:
                    self.r_rest_gf = self.r_total_gf - self.r1_gf - \
                        1 / (1 / self.r_conv_inner_gf + 1 / self.r_rad_gf_iw)
                if with_rooftops:
                    self.r_rest_rt = self.r_total_rt - self.r1_rt - \
                        1 / (1 / self.r_conv_inner_rt + 1 / self.r_rad_rt_iw)
                self.ir_emissivity_outer_ow = \
                    ((self.ir_emissivity_outer_ow * self.area_ow) +
                     (self.ir_emissivity_win * self.area_win)) / \
                    (self.area_ow + self.area_win)
                self.ir_emissivity_inner_ow = \
                    ((self.ir_emissivity_inner_ow * self.area_ow) +
                     (self.ir_emissivity_win * self.area_win)) / \
                    (self.area_ow + self.area_win)
                self.solar_absorp_ow = \
                    ((self.solar_absorp_ow * self.area_ow) +
                     (self.solar_absorp_win * self.area_win)) / \
                    (self.area_ow + self.area_win)

            else:
                warnings.warn("As no outer walls or no windows are defined\
                    lumped parameter cannot be calculated")

    def calc_chain_matrix(self, element_list, omega):
        """Matrix calculation.

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
        """

        for wall_count in range(len(element_list) - 1):

            if wall_count == 0:

                r1 = (element_list[wall_count].r1 *
                      element_list[wall_count].c1 ** 2 +
                      element_list[wall_count + 1].r1 *
                      element_list[wall_count + 1].c1 ** 2 + omega ** 2 *
                      element_list[wall_count].r1 *
                      element_list[wall_count + 1].r1 *
                      (element_list[wall_count].r1 +
                       element_list[wall_count + 1].r1) *
                      element_list[wall_count].c1 ** 2 *
                      element_list[wall_count + 1].c1 ** 2) / \
                     ((element_list[wall_count].c1 +
                       element_list[wall_count + 1].c1) ** 2 + omega ** 2 *
                      (element_list[wall_count].r1 +
                       element_list[wall_count + 1].r1) ** 2 *
                      element_list[wall_count].c1 ** 2 *
                      element_list[wall_count + 1].c1 ** 2)

                c1 = ((element_list[wall_count].c1 +
                       element_list[wall_count + 1].c1) ** 2 + omega ** 2 *
                      (element_list[wall_count].r1 +
                       element_list[wall_count + 1].r1) ** 2 *
                      element_list[wall_count].c1 ** 2 *
                      element_list[wall_count + 1].c1 ** 2) / \
                     (element_list[wall_count].c1 +
                      element_list[wall_count + 1].c1 + omega ** 2 *
                      (element_list[wall_count].r1 ** 2 *
                       element_list[wall_count].c1 +
                       element_list[wall_count + 1].r1 ** 2 *
                       element_list[wall_count + 1].c1) *
                      element_list[wall_count].c1 *
                      element_list[wall_count + 1].c1)
            else:
                r1x = r1
                c1x = c1
                r1 = (r1x * c1x ** 2 + element_list[wall_count + 1].r1 *
                      element_list[wall_count + 1].c1 ** 2 +
                      omega ** 2 * r1x * element_list[wall_count + 1].r1 *
                      (r1x + element_list[wall_count + 1].r1) *
                      c1x ** 2 * element_list[wall_count + 1].c1 ** 2) / \
                     ((c1x + element_list[wall_count + 1].c1) ** 2 +
                      omega ** 2 * (
                      r1x + element_list[wall_count + 1].r1) ** 2 *
                      c1x ** 2 * element_list[wall_count + 1].c1 ** 2)

                c1 = ((c1x + element_list[
                    wall_count + 1].c1) ** 2 + omega ** 2 *
                      (r1x + element_list[wall_count + 1].r1) ** 2 * c1x ** 2 *
                      element_list[wall_count + 1].c1 ** 2) / \
                    (c1x + element_list[wall_count + 1].c1 + omega ** 2 *
                        (r1x ** 2 * c1x + element_list[wall_count + 1].r1 **
                         2 * element_list[wall_count + 1].c1) * c1x *
                        element_list[wall_count + 1].c1)
        return r1, c1

    def sum_building_elements(self):
        """sums values of several building elements to zone based parameters

        Sums UA-Values, R-Values and area. Calculates the weighted coefficient
        of heat transfer for outer walls, inner walls, groundfloors, roofs and
        windows

        """
        # inner wall
        sum_r_conv_inner_iw = 0
        sum_r_rad_inner_iw = 0
        sum_r_comb_inner_iw = 0
        sum_r_conv_outer_iw = 0
        sum_r_rad_outer_iw = 0
        sum_r_comb_outer_iw = 0
        # outer wall
        sum_r_conv_inner_ow = 0
        sum_r_rad_inner_ow = 0
        sum_r_comb_inner_ow = 0
        sum_r_conv_outer_ow = 0
        sum_r_rad_outer_ow = 0
        sum_r_comb_outer_ow = 0
        sum_ir_emissivity_outer_ow = 0.0
        sum_ir_emissivity_inner_ow = 0.0
        sum_solar_absorp_ow = 0.0
        # ground floor
        sum_r_conv_inner_gf = 0
        sum_r_rad_inner_gf = 0
        sum_r_comb_inner_gf = 0
        sum_r_conv_outer_gf = 0
        sum_r_rad_outer_gf = 0
        sum_r_comb_outer_gf = 0
        sum_ir_emissivity_inner_gf = 0.0
        sum_solar_absorp_gf = 0.0
        # rooftop
        sum_r_conv_inner_rt = 0
        sum_r_rad_inner_rt = 0
        sum_r_comb_inner_rt = 0
        sum_r_conv_outer_rt = 0
        sum_r_rad_outer_rt = 0
        sum_r_comb_outer_rt = 0
        sum_ir_emissivity_outer_rt = 0.0
        sum_ir_emissivity_inner_rt = 0.0
        sum_solar_absorp_rt = 0.0
        # window
        sum_r_conv_inner_win = 0
        sum_r_rad_inner_win = 0
        sum_r_comb_inner_win = 0
        sum_r_conv_outer_win = 0
        sum_r_rad_outer_win = 0
        sum_r_comb_outer_win = 0
        sum_g_value = 0
        sum_solar_absorp_win = 0
        sum_ir_emissivity_win = 0

        for in_wall in self.inner_walls:
            self.ua_value_iw += in_wall.ua_value
            self.area_iw += in_wall.area
            sum_r_conv_inner_iw += 1 / in_wall.r_inner_conv
            sum_r_rad_inner_iw += 1 / in_wall.r_inner_rad
            sum_r_comb_inner_iw += 1 / in_wall.r_inner_comb
            # sum_r_conv_outer_iw += 1 / in_wall.r_outer_conv
            # sum_r_rad_outer_iw += 1 / in_wall.r_outer_rad
            # sum_r_comb_outer_iw += 1 / in_wall.r_outer_comb

        self.r_conv_inner_iw = 1 / sum_r_conv_inner_iw
        self.r_rad_inner_iw = 1 / sum_r_rad_inner_iw
        self.r_comb_inner_iw = 1 / sum_r_comb_inner_iw
        # self.r_conv_outer_iw = 1 / sum_r_conv_outer_iw
        # self.r_rad_outer_iw = 1 / sum_r_rad_outer_iw
        # self.r_comb_outer_iw = 1 / sum_r_comb_outer_iw

        self.alpha_conv_inner_iw = 1/(self.r_conv_inner_iw * self.area_iw)
        self.alpha_rad_inner_iw = 1/(self.r_rad_inner_iw * self.area_iw)
        self.alpha_comb_inner_iw = 1/(self.r_comb_inner_iw * self.area_iw)

        for out_wall in self.outer_walls:
            if type(out_wall).__name__ == "OuterWall":
                self.ua_value_ow += out_wall.ua_value
                self.area_ow += out_wall.area
                sum_r_conv_inner_ow += 1 / out_wall.r_inner_conv
                sum_r_rad_inner_ow += 1 / out_wall.r_inner_rad
                sum_r_comb_inner_ow += 1 / out_wall.r_inner_comb
                sum_r_conv_outer_ow += 1 / out_wall.r_outer_conv
                sum_r_rad_outer_ow += 1 / out_wall.r_outer_rad
                sum_r_comb_outer_ow += 1 / out_wall.r_outer_comb
                sum_ir_emissivity_outer_ow += \
                    out_wall.layer[-1].material.ir_emissivity * out_wall.area
                sum_ir_emissivity_inner_ow += \
                    out_wall.layer[0].material.ir_emissivity * out_wall.area
                sum_solar_absorp_ow += \
                    out_wall.layer[-1].material.solar_absorp * out_wall.area
            elif type(out_wall).__name__ == "Rooftop":
                self.ua_value_rt += out_wall.ua_value
                self.area_rt += out_wall.area
                sum_r_conv_inner_rt += 1 / out_wall.r_inner_conv
                sum_r_rad_inner_rt += 1 / out_wall.r_inner_rad
                sum_r_comb_inner_rt += 1 / out_wall.r_inner_comb
                sum_r_conv_outer_rt += 1 / out_wall.r_outer_conv
                sum_r_rad_outer_rt += 1 / out_wall.r_outer_rad
                sum_r_comb_outer_rt += 1 / out_wall.r_outer_comb
                sum_ir_emissivity_outer_rt += \
                    out_wall.layer[-1].material.ir_emissivity * out_wall.area
                sum_ir_emissivity_inner_rt += \
                    out_wall.layer[0].material.ir_emissivity * out_wall.area
                sum_solar_absorp_rt += \
                    out_wall.layer[-1].material.solar_absorp * out_wall.area
            elif type(out_wall).__name__ == "GroundFloor":
                self.ua_value_gf += out_wall.ua_value
                self.area_gf += out_wall.area
                sum_r_conv_inner_gf += 1 / out_wall.r_inner_conv
                sum_r_rad_inner_gf += 1 / out_wall.r_inner_rad
                sum_r_comb_inner_gf += 1 / out_wall.r_inner_comb
                sum_ir_emissivity_inner_gf += \
                    out_wall.layer[0].material.ir_emissivity * out_wall.area
                sum_solar_absorp_gf += \
                    out_wall.layer[-1].material.solar_absorp * out_wall.area
                # sum_r_conv_outer_gf += 1 / out_wall.r_outer_conv
                # sum_r_rad_outer_gf += 1 / out_wall.r_outer_rad
                # sum_r_comb_outer_gf += 1 / out_wall.r_outer_comb

        if [sum_r_comb_inner_ow, sum_r_comb_outer_ow] != 0:
            self.r_conv_inner_ow = 1 / sum_r_conv_inner_ow
            self.r_rad_inner_ow = 1 / sum_r_rad_inner_ow
            self.r_comb_inner_ow = 1 / sum_r_comb_inner_ow
            self.r_conv_outer_ow = 1 / sum_r_conv_outer_ow
            self.r_rad_outer_ow = 1 / sum_r_rad_outer_ow
            self.r_comb_outer_ow = 1 / sum_r_comb_outer_ow
            self.alpha_conv_inner_ow = (
                1 / (self.r_conv_inner_ow * self.area_ow))
            self.alpha_rad_inner_ow = (
                1 / (self.r_rad_inner_ow * self.area_ow))
            self.alpha_comb_inner_ow = (
                1 / (self.r_comb_inner_ow * self.area_ow))
            self.alpha_conv_outer_ow = (
                1 / (self.r_conv_outer_ow * self.area_ow))
            self.alpha_rad_outer_ow = (
                1 / (self.r_rad_outer_ow * self.area_ow))
            self.alpha_comb_outer_ow = (
                1 / (self.r_comb_outer_ow * self.area_ow))
            self.ir_emissivity_outer_ow = \
                sum_ir_emissivity_outer_ow / self.area_ow
            self.ir_emissivity_inner_ow = \
                sum_ir_emissivity_inner_ow / self.area_ow
            self.solar_absorp_ow = \
                sum_solar_absorp_ow / self.area_ow

        if sum_r_comb_inner_rt != 0:
            self.r_conv_inner_rt = 1 / sum_r_conv_inner_rt
            self.r_rad_inner_rt = 1 / sum_r_rad_inner_rt
            self.r_comb_inner_rt = 1 / sum_r_comb_inner_rt
            self.r_conv_outer_rt = 1 / sum_r_conv_outer_rt
            self.r_rad_outer_rt = 1 / sum_r_rad_outer_rt
            self.r_comb_outer_rt = 1 / sum_r_comb_outer_rt
            self.alpha_conv_inner_rt = (
                1 / (self.r_conv_inner_rt * self.area_rt))
            self.alpha_rad_inner_rt = (
                1 / (self.r_rad_inner_rt * self.area_rt))
            self.alpha_comb_inner_rt = (
                1 / (self.r_comb_inner_rt * self.area_rt))
            self.alpha_conv_outer_rt = (
                1 / (self.r_conv_outer_rt * self.area_rt))
            self.alpha_rad_outer_rt = (
                1 / (self.r_rad_outer_rt * self.area_rt))
            self.alpha_comb_outer_rt = (
                1 / (self.r_comb_outer_rt * self.area_rt))
            self.ir_emissivity_outer_rt = \
                sum_ir_emissivity_outer_rt / self.area_rt
            self.ir_emissivity_inner_rt = \
                sum_ir_emissivity_inner_rt / self.area_rt
            self.solar_absorp_rt = \
                sum_solar_absorp_rt / self.area_rt
        if sum_r_comb_inner_gf != 0:
            self.r_conv_inner_gf = 1 / sum_r_conv_inner_gf
            self.r_rad_inner_gf = 1 / sum_r_rad_inner_gf
            self.r_comb_inner_gf = 1 / sum_r_comb_inner_gf
            self.alpha_conv_inner_gf = (
                1 / (self.r_conv_inner_gf * self.area_gf))
            self.alpha_rad_inner_gf = (
                1 / (self.r_rad_inner_gf * self.area_gf))
            self.alpha_comb_inner_gf = (
                1 / (self.r_comb_inner_gf * self.area_gf))
            self.ir_emissivity_inner_gf = \
                sum_ir_emissivity_inner_gf / self.area_gf
            self.solar_absorp_gf = \
                sum_solar_absorp_gf / self.area_gf

        for win in self.windows:
            self.ua_value_win += win.ua_value
            self.area_win += win.area
            sum_r_conv_inner_win += 1 / win.r_inner_conv
            sum_r_rad_inner_win += 1 / win.r_inner_rad
            sum_r_comb_inner_win += 1 / win.r_inner_comb
            sum_r_conv_outer_win += 1 / win.r_outer_conv
            sum_r_rad_outer_win += 1 / win.r_outer_rad
            sum_r_comb_outer_win += 1 / win.r_outer_comb
            sum_g_value += win.g_value * win.area
            sum_solar_absorp_win += win.layer[-1].material.solar_absorp * \
                win.area
            sum_ir_emissivity_win += win.layer[-1].material.ir_emissivity * \
                win.area

        self.r_conv_inner_win = 1 / sum_r_conv_inner_win
        self.r_rad_inner_win = 1 / sum_r_rad_inner_win
        self.r_comb_inner_win = 1 / sum_r_comb_inner_win
        self.r_conv_outer_win = 1 / sum_r_conv_outer_win
        self.r_rad_outer_win = 1 / sum_r_rad_outer_win
        self.r_comb_outer_win = 1 / sum_r_comb_outer_win
        self.weighted_g_value = sum_g_value / self.area_win
        self.alpha_conv_inner_win = (
            1 / (self.r_conv_inner_win * self.area_win))
        self.alpha_rad_inner_win = (1 / (self.r_rad_inner_win * self.area_win))
        self.alpha_comb_inner_win = (
            1 / (self.r_comb_inner_win * self.area_win))
        self.alpha_conv_outer_win = (
            1 / (self.r_conv_outer_win * self.area_win))
        self.alpha_rad_outer_win = (1 / (self.r_rad_outer_win * self.area_win))
        self.alpha_comb_outer_win = (
            1 / (self.r_comb_outer_win * self.area_win))
        self.solar_absorp_win = sum_solar_absorp_win / self.area_win
        self.ir_emissivity_win = sum_ir_emissivity_win / self.area_win

    def calc_wf_one_element(self, merge_windows):
        pass

    def calc_wf_two_element(self, merge_windows):
        """Calculation of weightfactors.

        Calculates the weightfactors of the outer walls, including ground and
        windows.

        Parameters
        ----------
        merge_windows : bool
            True for merging the windows into the outer walls, False for
            separate resistance for window, default is False
        """

        if merge_windows is True:

            for wall in self.outer_walls:
                wall.wf_out = wall.ua_value / (
                    self.ua_value_ow + self.ua_value_win)

            for win in self.windows:
                win.wf_out = win.ua_value / (
                    self.ua_value_ow + self.ua_value_win)

        elif merge_windows is False:

            for wall in self.outer_walls:
                wall.wf_out = wall.ua_value / self.ua_value_ow

            for win in self.windows:
                win.wf_out = win.ua_value / self.ua_value_win

        else:
            raise ValueError("specify calculation method correctly")

    def calc_wf_three_element(self, merge_windows):
        """Calculation of weightfactors.

        Calculates the weightfactors of the outer walls (with rooftops) and
        ground with possibility to merge windows into outer walls

        Parameters
        ----------
        merge_windows : bool
            True for merging the windows into the outer walls, False for
            separate resistance for window, default is False
        """
        if merge_windows is True:

            for wall in self.outer_walls_help:
                wall.wf_out = wall.ua_value / (
                    self.ua_value_ow + self.ua_value_win)

            for win in self.windows:
                win.wf_out = win.ua_value / (
                    self.ua_value_ow + self.ua_value_win)

        elif merge_windows is False:

            for wall in self.outer_walls_help:
                wall.wf_out = wall.ua_value / self.ua_value_ow

            for win in self.windows:
                win.wf_out = win.ua_value / self.ua_value_win

        for wall in self.ground_floors:
            wall.wf_out = wall.ua_value / self.ua_value_gf

    def calc_wf_four_element(self, merge_windows):
        """Calculation of weightfactors.

        Calculates the weightfactors of the outer walls, rooftops and ground
        with possibility to merge windows into outer walls

        Parameters
        ----------
        merge_windows : bool
            True for merging the windows into the outer walls, False for
            separate resistance for window, default is False
        """
        if merge_windows is True:

            for wall in self.outer_walls_help:
                wall.wf_out = wall.ua_value / (
                    self.ua_value_ow + self.ua_value_win)

            for win in self.windows:
                win.wf_out = win.ua_value / (
                    self.ua_value_ow + self.ua_value_win)

        elif merge_windows is False:

            for wall in self.outer_walls_help:
                wall.wf_out = wall.ua_value / self.ua_value_ow

            for win in self.windows:
                win.wf_out = win.ua_value / self.ua_value_win

        for wall in self.ground_floors:
            wall.wf_out = wall.ua_value / self.ua_value_gf

        for wall in self.rooftops:
            wall.wf_out = wall.ua_value / self.ua_value_rt

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

        for wall in self.inner_walls:
            if type(wall).__name__ == "Ceiling" \
                    or type(wall).__name__ == "Floor":

                wall.area = ((self.parent.number_of_floors - 1) /
                             self.parent.number_of_floors) * self.area
            else:
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
            self.heating_load = ((self.ua_value_ow + self.ua_value_win) +
                                 self.volume * self.infiltration_rate / 3.6 *
                                 _heat_capac_air * _density_air) * \
                                (self.t_inside - self.t_outside)
        elif number_of_elements == 3:
            self.heating_load = ((self.ua_value_ow + self.ua_value_gf +
                                  self.ua_value_win) +
                                 self.volume * self.infiltration_rate / 3.6 *
                                 _heat_capac_air * _density_air) * \
                                 (self.t_inside - self.t_outside)
        elif number_of_elements == 4:
            self.heating_load = ((self.ua_value_ow + self.ua_value_gf +
                                  self.ua_value_rt + self.ua_value_win) +
                                 self.volume * self.infiltration_rate / 3.6 *
                                 _heat_capac_air*_density_air) * \
                                (self.t_inside - self.t_outside)

    def retrofit_zone(self, window_type=None, material=None):
        """Retrofits all walls and windows in the zone.
        """

        for wall_count in self.outer_walls:
            wall_count.retrofit_wall(self.parent.year_of_retrofit, material)
        for win_count in self.windows:
            win_count.replace_window(self.parent.year_of_retrofit, window_type)

    def set_calc_default(self):
        """sets default calculation parameters
        """
        self.outer_walls_help = []
        self.rooftops = []
        self.ground_floors = []

        self.r1_ow = 0.0
        self.c1_ow = 0.0
        self.r_rest_ow = 0.0
        self.r_total_ow = 0.0

        self.weightfactor_ow = []
        self.weightfactor_ground = []
        self.tilt_wall = []
        self.orientation_wall = []
        self.outer_walls_areas = []

        self.ua_value_ow = 0.0
        self.r_conv_inner_ow = 0.0
        self.r_rad_inner_ow = 0.0
        self.r_comb_inner_ow = 0.0
        self.r_conv_outer_ow = 0.0
        self.r_rad_outer_ow = 0.0
        self.r_comb_outer_ow = 0.0
        self.area_ow = 0.0

        self.alpha_conv_inner_ow = 0.0
        self.alpha_rad_inner_ow = 0.0
        self.alpha_comb_inner_ow = 0.0

        self.alpha_conv_outer_ow = 0.0
        self.alpha_rad_outer_ow = 0.0
        self.alpha_comb_outer_ow = 0.0

        self.r_rad_ow_iw = 0.0

        self.r1_iw = 0.0
        self.c1_iw = 0.0
        self.ua_value_iw = 0.0
        self.r_conv_iw = 0.0
        self.r_rad_iw = 0.0
        self.r_comb_iw = 0.0
        self.area_iw = 0.0
        self.r_conv_inner_iw = 0.0
        self.r_rad_inner_iw = 0.0
        self.r_comb_inner_iw = 0.0
        self.r_conv_outer_iw = 0.0
        self.r_rad_outer_iw = 0.0
        self.r_comb_outer_iw = 0.0

        self.alpha_conv_inner_iw = 0.0
        self.alpha_rad_inner_iw = 0.0
        self.alpha_comb_inner_iw = 0.0

        self.alpha_conv_outer_iw = 0.0
        self.alpha_rad_outer_iw = 0.0
        self.alpha_comb_outer_iw = 0.0

        self.r1_rt = 0.0
        self.c1_rt = 0.0
        self.r_rest_rt = 0.0
        self.r_total_rt = 0.0
        self.weightfactor_rt = []
        self.tilt_rt = []
        self.orientation_rt = []
        self.ua_value_rt = 0.0
        self.r_conv_inner_rt = 0.0
        self.r_rad_inner_rt = 0.0
        self.r_comb_inner_rt = 0.0
        self.r_conv_outer_rt = 0.0
        self.r_rad_outer_rt = 0.0
        self.r_comb_outer_rt = 0.0
        self.area_rt = 0.0

        self.alpha_conv_inner_rt = 0.0
        self.alpha_rad_inner_rt = 0.0
        self.alpha_comb_inner_rt = 0.0

        self.alpha_conv_outer_rt = 0.0
        self.alpha_rad_outer_rt = 0.0
        self.alpha_comb_outer_rt = 0.0

        self.r_rad_rt_iw = 0.0

        # Calculated values for GroundFlor for each Zone
        self.r1_gf = 0.0
        self.c1_gf = 0.0
        self.r_rest_gf = 0.0
        self.r_total_gf = 0.0
        self.weightfactor_gf = []
        self.tilt_gf = []
        self.orientation_gf = []
        self.ua_value_gf = 0.0
        self.r_conv_inner_gf = 0.0
        self.r_rad_inner_gf = 0.0
        self.r_comb_inner_gf = 0.0
        self.r_conv_outer_gf = 0.0
        self.r_rad_outer_gf = 0.0
        self.r_comb_outer_gf = 0.0
        self.area_gf = 0.0

        self.alpha_conv_inner_gf = 0.0
        self.alpha_rad_inner_gf = 0.0
        self.alpha_comb_inner_gf = 0.0

        self.alpha_conv_outer_gf = 0.0
        self.alpha_rad_outer_gf = 0.0
        self.alpha_comb_outer_gf = 0.0

        self.r_rad_gf_iw = 0.0

        # Calculated values for windows for each Zone
        self.r1_win = 0.0
        self.weightfactor_win = []
        self.g_sunblind_list = []
        self.window_area_list = []
        self.window_areas = []
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
        self.alpha_rad_inner_win = 0.0
        self.alpha_comb_inner_win = 0.0

        self.alpha_conv_outer_win = 0.0
        self.alpha_rad_outer_win = 0.0
        self.alpha_comb_outer_win = 0.0

        self.weighted_g_value = 0.0
        self.heating_load = 0.0
        self.cooling_load = 0.0

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
                       "Ceiling() or "
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
