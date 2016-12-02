# created December 2016

from __future__ import division
import math
import random
import warnings
import re


class TwoElement(object):
    """This class contains attributes and functions for two element model

    This model distinguishes between internal thermal masses and exterior walls.
    While exterior walls contribute to heat transfer to the ambient, adiabatic
    conditions apply to interior walls. This approach allows considering the
    dynamic behaviour induced by internal heat storage. This class calculates
    and holds all attributes given in documentation.

    It treats Rooftops, GroundFloors and OuterWalls as one type of outer
    walls and computes one RC-combination for these types.

    Depending on the chosen method it will consider an extra resistance for
    windows or merge all windows into the RC-Combination for outer walls.

    Parameters
    ----------
    thermal_zone: ThermalZone()
        TEASER instance of ThermalZone
    merge_windows : boolean
        True for merging the windows into the outer wall's RC-combination,
        False for separate resistance for window, default is False
    t_bt : int
        Time constant according to VDI 6007 (default t_bt = 5)

    Attributes
    ----------
    Interior Walls

    area_iw : float [m2]
        Area of all interior walls.
    alpha_conv_inner_iw : float [W/(m2K)]
        Area-weighted convective coefficient of heat transfer of interior
        walls facing the inside of this thermal zone.
    alpha_rad_inner_iw : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of interior
        walls facing the inside of this thermal zone.
    alpha_comb_inner_iw : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of interior walls
        facing the inside of this thermal zone.
    alpha_conv_outer_iw : float [W/(m2K)]
        Area-weighted convective coefficient of heat transfer of interior
        walls facing the adjacent thermal zone.
    alpha_rad_outer_iw : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of interior
        walls facing the adjacent thermal zone.
    alpha_comb_outer_iw : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of interior walls
        facing the adjacent thermal zone.
    ua_value_iw : float [W/(m2K)]
        U-Value times interior wall area.
    r_conv_inner_iw : float [K/W]
        Sum of convective resistances for all interior walls
        facing the inside of this thermal zone.
    r_rad_inner_iw : float [K/W]
        Sum of radiative resistances for all interior walls facing the
        inside of this thermal zone
    r_comb_inner_iw : float [K/W]
        Sum of combined resistances for all interior walls facing the
        inside of this thermal zone
    r1_iw : float [K/W]
        Lumped resistance of interior walls
    c1_iw : float [J/K]
        Lumped capacity of interior walls

    Outer Walls (OuterWall, Rooftop, GroundFloor)

    area_ow : float [m2]
        Area of all outer walls.
    alpha_conv_inner_ow : float [W/(m2K)]
        Area-weighted convective coefficient of heat transfer of outer walls
        facing the inside of this thermal zone.
    alpha_rad_inner_ow : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of outer walls
        facing the inside of this thermal zone.
    alpha_comb_inner_ow : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of outer walls
        facing the inside of this thermal zone.
    alpha_conv_outer_ow : float [W/(m2K)]
        Area-weighted convective coefficient of heat transfer of outer walls
        facing the ambient.
    alpha_rad_outer_ow : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of outer walls
        facing the ambient.
    alpha_comb_outer_ow : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of outer walls
        facing the ambient.
    ua_value_ow : float [W/(m2K)]
        U-Value times outer wall area.
    r_conv_inner_ow : float [K/W]
        Sum of convective resistances for all outer walls facing the
        inside of this thermal zone.
    r_rad_inner_ow : float [K/W]
        Sum of radiative resistances for all outer walls facing the
        inside of this thermal zone.
    r_comb_inner_ow : float [K/W]
        Sum of combined resistances for all outer walls facing the
        inside of this thermal zone.
    r_conv_outer_ow : float [K/W]
        Sum of convective resistances for all outer walls facing the
        ambient.
    r_rad_outer_ow : float [K/W]
        Sum of radiative resistances for all outer walls facing the
        ambient.
    r_comb_outer_ow : float [K/W]
        Sum of combined resistances for all outer walls facing the
        ambient.
    r1_ow : float [K/W]
        Lumped resistance of outer walls.
    r_rest_ow : float [K/W]
        Lumped remaining resistance of outer walls between r1_ow and c1_ow.
    c1_ow : float [J/K]
        Lumped capacity of outer walls.
    weightfactor_ow : list of floats
        Weightfactors of outer walls (UA-Value of walls with same orientation
        and tilt divided by ua_value_ow)
    weightfactor_ground : list of floats
        Weightfactors of groundfloors (UA-Value of groundfloor divided by
        ua_value_ow).
    tilt_wall : list of floats [degree]
        Tilt of outer walls against the horizontal.
    orientation_wall : list of floats [degree]
        Orientation of outer walls (Azimuth).
        0 - North
        90 - East
        180 - South
        270 - West
    outer_walls_areas : list of floats [m2]
        Area of all outer walls in one list.
    r_rad_ow_iw : float [K/W]
        Resistance for radiative heat transfer between walls.
        TODO: needs to be checked
    ir_emissivity_outer_ow : float
        Area-weighted ir emissivity of outer wall facing the ambient.
    ir_emissivity_inner_ow : float
        Area-weighted ir emissivity of outer walls facing the thermal zone.
    solar_absorp_ow : float
        Area-weighted solar absorption of outer walls facing the ambient.

    Windows

    area_win : float [m2]
        Area of all windows.
    alpha_conv_inner_win : float [W/(m2K)]
        Area-weighted convective coefficient of heat transfer of windows
        facing the inside of this thermal zone.
    alpha_rad_inner_win : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of windows
        facing the inside of this thermal zone.
    alpha_comb_inner_win : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of windows facing
        the inside of this thermal zone.
    alpha_conv_outer_win : float [W/(m2K)]
        Area-weighted convective coefficient of heat transfer of windows
        facing the ambient.
    alpha_rad_outer_win : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of windows
        facing the ambient.
    alpha_comb_outer_win : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of windows facing
        the ambient.
    ua_value_win : float [W/(m2K)]
        U-Value times outer wall area.
    r_conv_inner_win : float [K/W]
        Sum of convective resistances for all windows facing the
        inside of this thermal zone.
    r_rad_inner_win : float [K/W]
        Sum of radiative resistances for all windows facing the
        inside of this thermal zone.
    r_comb_inner_win : float [K/W]
        Sum of combined resistances for all windows facing the
        inside of this thermal zone.
    r_conv_outer_win : float [K/W]
        Sum of convective resistances for all windows facing the
        ambient.
    r_rad_outer_win : float [K/W]
        Sum of radiative resistances for all windows facing the
        ambient.
    r_comb_outer_win : float [K/W]
        Sum of combined resistances for all windows facing the
        ambient.
    r1_win : float [K/W]
        Lumped resistance of windows.
    r_rest_win : float [K/W]
        Lumped remaining resistance of windows between r1_win and c1_win.
    c1_win : float [J/K]
        Lumped capacity of windows.
    weightfactor_win : list of floats
        Weightfactors of windows (UA-Value of windows with same orientation
        and tilt divided by ua_value_win or ua_value_win+ua_value_ow,
        depending if windows is lumped/merged into the walls or not)
    tilt_win : list of floats [degree]
        Tilt of windows against the horizontal.
    orientation_win : list of floats [degree]
        Orientation of windows (Azimuth).
        0 - North
        90 - East
        180 - South
        270 - West
    window_areas : list of floats [m2]
        Area of all windows in one list.
    solar_absorp_win : float
        Area-weighted solar absorption for windows. (typically 0.0)
    ir_emissivity_win : float
        Area-weighted ir_emissivity for windows. Can be used for windows
        facing the thermal zone and the ambient.
    weighted_g_value : float
        Area-weighted g-Value of all windows.

    """

    def __init__(self, thermal_zone, merge_windows, t_bt):
        """Constructor for TwoElement"""

        self.internal_id = random.random()

        self.thermal_zone = thermal_zone
        self.merge_windows = merge_windows
        self.t_bt = t_bt

        # Attributes of inner walls
        self.area_iw = 0.0

        # coefficient of heat transfer facing the inside of this thermal zone
        self.alpha_conv_inner_iw = 0.0
        self.alpha_rad_inner_iw = 0.0
        self.alpha_comb_inner_iw = 0.0
        # coefficient of heat transfer facing the adjacent thermal zone
        self.alpha_conv_outer_iw = 0.0
        self.alpha_rad_outer_iw = 0.0
        self.alpha_comb_outer_iw = 0.0

        # UA-Value
        self.ua_value_iw = 0.0

        # resistances for heat transfer facing the inside of this thermal zone
        self.r_conv_inner_iw = 0.0
        self.r_rad_inner_iw = 0.0
        self.r_comb_inner_iw = 0.0
        self.r_conv_outer_iw = 0.0
        self.r_rad_outer_iw = 0.0
        self.r_comb_outer_iw = 0.0

        # lumped resistance/capacity
        self.r1_iw = 0.0
        self.c1_iw = 0.0

        # Attributes for outer walls (OuterWall, Rooftop, GroundFloor)
        self.area_ow = 0.0

        # coefficient of heat transfer facing the inside of this thermal zone
        self.alpha_conv_inner_ow = 0.0
        self.alpha_rad_inner_ow = 0.0
        self.alpha_comb_inner_ow = 0.0

        # coefficient of heat transfer facing the ambient
        self.alpha_conv_outer_ow = 0.0
        self.alpha_rad_outer_ow = 0.0
        self.alpha_comb_outer_ow = 0.0

        # UA-Value
        self.ua_value_ow = 0.0

        # resistances for heat transfer facing the inside of this thermal zone
        self.r_conv_inner_ow = 0.0
        self.r_rad_inner_ow = 0.0
        self.r_comb_inner_ow = 0.0

        # resistances for heat transfer facing the ambient
        self.r_conv_outer_ow = 0.0
        self.r_rad_outer_ow = 0.0
        self.r_comb_outer_ow = 0.0

        # lumped resistances/capacity
        self.r1_ow = 0.0
        self.r_rest_ow = 0.0
        self.c1_ow = 0.0
        self.r_total_ow = 0.0

        # Optical properties
        self.ir_emissivity_outer_ow = 0.0
        self.ir_emissivity_inner_ow = 0.0
        self.solar_absorp_ow = 0.0

        # Additional attributes
        self.weightfactor_ow = []
        self.weightfactor_ground = []
        self.tilt_wall = []
        self.orientation_wall = []
        self.outer_walls_areas = []

        # TODO: check this value
        self.r_rad_ow_iw = 0.0

        # Attributes for windows
        self.area_win = 0.0

        # coefficient of heat transfer facing the inside of this thermal zone
        self.alpha_conv_inner_win = 0.0
        self.alpha_rad_inner_win = 0.0
        self.alpha_comb_inner_win = 0.0

        # coefficient of heat transfer facing the ambient
        self.alpha_conv_outer_win = 0.0
        self.alpha_rad_outer_win = 0.0
        self.alpha_comb_outer_win = 0.0

        # UA-Value
        self.ua_value_win = 0.0

        # resistances for heat transfer facing the inside of this thermal zone
        self.r_conv_inner_win = 0.0
        self.r_rad_inner_win = 0.0
        self.r_comb_inner_win = 0.0

        # resistances for heat transfer facing the ambient
        self.r_conv_outer_win = 0.0
        self.r_rad_outer_win = 0.0
        self.r_comb_outer_win = 0.0

        # lumped resistances/capacity
        self.r1_win = 0.0

        # Optical properties
        self.ir_emissivity_outer_win = 0.0
        self.ir_emissivity_inner_win = 0.0
        self.solar_absorp_win = 0.0

        # Additional attributes
        self.weightfactor_win = []
        self.tilt_win = []
        self.orientation_win = []
        self.window_areas = []
        self.g_sunblind_list = []
        self.weighted_g_value = 0.0

    def sum_building_elements(self):
        """Sum attributes of several building elements

        This function sums and computes the area-weighted values,
        where necessary (the class doc string) for coefficients of heat
        transfer, resistances, areas and UA-Values.

        For TwoElement model it treats Rooftops, Groundfloor and OuterWalls
        as one kind of wall type.

        """
        # treat all outer wall types identical

        outer_walls = self.thermal_zone.outer_walls + \
                      self.thermal_zone.rooftops + \
                      self.thermal_zone.ground_floors

        # temporary attributes for outer walls
        _sum_r_conv_inner_ow = 0
        _sum_r_rad_inner_ow = 0
        _sum_r_comb_inner_ow = 0
        _sum_r_conv_outer_ow = 0
        _sum_r_rad_outer_ow = 0
        _sum_r_comb_outer_ow = 0
        _sum_ir_emissivity_outer_ow = 0.0
        _sum_ir_emissivity_inner_ow = 0.0
        _sum_solar_absorp_ow = 0.0



        # temporary attributes for inner walls

        sum_r_conv_inner_iw = 0
        sum_r_rad_inner_iw = 0
        sum_r_comb_inner_iw = 0

        # temporary attributes for windows

        sum_r_conv_inner_win = 0
        sum_r_rad_inner_win = 0
        sum_r_comb_inner_win = 0
        sum_r_conv_outer_win = 0
        sum_r_rad_outer_win = 0
        sum_r_comb_outer_win = 0
        sum_g_value = 0
        sum_solar_absorp_win = 0
        sum_ir_emissivity_win = 0

        self.ua_value_ow = sum(out_wall.ua_value for out_wall in outer_walls)
        self.area_ow = sum(out_wall.ua_value for out_wall in outer_walls)
        self.r_conv_inner_ow = 1 / sum(1 / (sum(out_wall.r_inner_conv for out_wall in outer_walls)))

        for out_wall in outer_walls:

            self.ua_value_ow += out_wall.ua_value
            self.area_ow += out_wall.area
            _sum_r_conv_inner_ow += 1 / out_wall.r_inner_conv
            _sum_r_rad_inner_ow += 1 / out_wall.r_inner_rad
            _sum_r_comb_inner_ow += 1 / out_wall.r_inner_comb
            _sum_r_conv_outer_ow += 1 / out_wall.r_outer_conv
            _sum_r_rad_outer_ow += 1 / out_wall.r_outer_rad
            _sum_r_comb_outer_ow += 1 / out_wall.r_outer_comb
            _sum_ir_emissivity_outer_ow += \
                out_wall.layer[-1].material.ir_emissivity * out_wall.area
            _sum_ir_emissivity_inner_ow += \
                out_wall.layer[0].material.ir_emissivity * out_wall.area
            _sum_solar_absorp_ow += \
                out_wall.layer[-1].material.solar_absorp * out_wall.area

        if [_sum_r_comb_inner_ow, _sum_r_comb_outer_ow] != 0:
            self.r_conv_inner_ow = 1 / _sum_r_conv_inner_ow
            self.r_rad_inner_ow = 1 / _sum_r_rad_inner_ow
            self.r_comb_inner_ow = 1 / _sum_r_comb_inner_ow
            self.r_conv_outer_ow = 1 / _sum_r_conv_outer_ow
            self.r_rad_outer_ow = 1 / _sum_r_rad_outer_ow
            self.r_comb_outer_ow = 1 / _sum_r_comb_outer_ow
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
                _sum_ir_emissivity_outer_ow / self.area_ow
            self.ir_emissivity_inner_ow = \
                _sum_ir_emissivity_inner_ow / self.area_ow
            self.solar_absorp_ow = \
                _sum_solar_absorp_ow / self.area_ow

        for in_wall in self.thermal_zone.inner_walls:
            self.ua_value_iw += in_wall.ua_value
            self.area_iw += in_wall.area
            sum_r_conv_inner_iw += 1 / in_wall.r_inner_conv
            sum_r_rad_inner_iw += 1 / in_wall.r_inner_rad
            sum_r_comb_inner_iw += 1 / in_wall.r_inner_comb

        if sum_r_comb_inner_iw != 0:
            self.r_conv_inner_iw = 1 / sum_r_conv_inner_iw
            self.r_rad_inner_iw = 1 / sum_r_rad_inner_iw
            self.r_comb_inner_iw = 1 / sum_r_comb_inner_iw

            self.alpha_conv_inner_iw = 1/(self.r_conv_inner_iw * self.area_iw)
            self.alpha_rad_inner_iw = 1/(self.r_rad_inner_iw * self.area_iw)
            self.alpha_comb_inner_iw = 1/(self.r_comb_inner_iw * self.area_iw)

        for win in self.thermal_zone.windows:
            self.ua_value_win += win.ua_value
            self.area_win += win.area
            sum_r_conv_inner_win += 1 / win.r_inner_conv
            sum_r_rad_inner_win += 1 / win.r_inner_rad
            sum_r_comb_inner_win += 1 / win.r_inner_comb
            sum_r_conv_outer_win += 1 / win.r_outer_conv
            sum_r_rad_outer_win += 1 / win.r_outer_rad
            sum_r_comb_outer_win += 1 / win.r_outer_comb
            sum_g_value += win.g_value * win.area
            sum_solar_absorp_win += win.layer[-1].material.solar_absorp
            sum_ir_emissivity_win += win.layer[-1].material.ir_emissivity

        if [sum_r_comb_inner_win, sum_r_comb_outer_win] != 0:
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
