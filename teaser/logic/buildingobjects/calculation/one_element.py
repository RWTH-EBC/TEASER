# created January 2017

from __future__ import division
import math
import random
import warnings


class OneElement(object):
    """This class contains attributes and functions for one element model

    his model merges all thermal masses into one element, parameterized by the
    length of the RC-chain nExt, the vector of the capacities CExt[nExt] that
    is connected via the vector of resistances RExt[nExt] and RExtRem to the
    ambient and indoor air. By default, the model neglects all internal thermal
    masses that are not directly connected to the ambient.

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
        False for separate resistance for window, default is False. (Only
        supported for IBPSA)
    t_bt : float [d]
        Time constant according to VDI 6007 (default t_bt = 5)

    Attributes
    ----------

    Outer Walls (OuterWall, Rooftop, GroundFloor)

    area_ow : float [m2]
        Area of all outer walls.
    n_outer : int
        Number of total outer walls with different combination of tilt and
        orientation, including Rooftops and GroundFloors
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
    ua_value_ow : float [W/K]
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
        Lumped resistance of outer walls no heat transfer coefficients for
        convection and radiation are accounted in this resistance.
    r_rest_ow : float [K/W]
        Lumped remaining resistance of outer walls between r1_ow and c1_ow no
        heat transfer coefficients for convection and radiation are accounted
        in this resistance.
    c1_ow : float [J/K]
        Lumped capacity of outer walls.
    weightfactor_ow : list of floats
        Weightfactors of outer walls (UA-Value of walls with same orientation
        and tilt divided by ua_value_ow)
    weightfactor_ground : list of floats
        Weightfactors of groundfloors (UA-Value of groundfloor divided by
        ua_value_ow).
    tilt_facade : list of floats [degree]
        Tilt of outer walls against the horizontal.
    orientation_facade : list of floats [degree]
        Orientation of outer walls (Azimuth).
        0 - North
        90 - East
        180 - South
        270 - West
    outer_wall_areas : list of floats [m2]
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
    ratio_conv_rad_inner_win : float [-]
        Ratio for windows between convective and radiative heat emission,
        given in VDI 6007-3
    alpha_conv_outer_win : float [W/(m2K)]
        Area-weighted convective coefficient of heat transfer of windows
        facing the ambient.
    alpha_rad_outer_win : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of windows
        facing the ambient.
    alpha_comb_outer_win : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of windows facing
        the ambient.
    ua_value_win : float [W/K]
        U-Value times window wall area.
    u_value_win : float [W/(m2K)]
        Area weighted U-Value of windows.
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
        Lumped resistance of windows, no heat transfer coefficients for
        convection and radiation are accounted in this resistance.
    weightfactor_win : list of floats
        Weightfactors of windows (UA-Value of windows with same orientation
        and tilt divided by ua_value_win or ua_value_win+ua_value_ow,
        depending if windows is lumped/merged into the walls or not)
    window_areas : list of floats [m2]
        Area of all windows in one list, if the windows are merged into the
        outer wall this list will be full of zeros
    transparent_areas : list of floats [m2]
        Area of all transparent elements (most likely windows) in one list,
        this list will be always filled with the areas, independent if
        windows are merged into walls or not.
    solar_absorp_win : float
        Area-weighted solar absorption for windows. (typically 0.0)
    ir_emissivity_win : float
        Area-weighted ir_emissivity for windows. Can be used for windows
        facing the thermal zone and the ambient.
    weighted_g_value : float
        Area-weighted g-Value of all windows.
    g_sunblind : list of floats
        G-Value of all sunblinds of each window in a list

    Misc values:

    alpha_rad_inner_mean : float [W/(m2K)]
        Area-weighted radiative coefficient of all surfaces facing the
        inside of this thermal zone (OuterWalls, Windows, InnerWalls, ...).
    alpha_rad_outer_mean : float [W/(m2K)]
        Area-weighted radiative coefficient of all surfaces facing the
        ambient (OuterWalls, Windows, ...).
    heat_load : [W]
        Static heat load of the thermal zone.
    facade_areas : list of floats [m2]
        List containing the area of each facade (with same tilt and
        orientation) this includes also roofs and ground floors and windows.
    n_outer : int
        Number of total facades with different combination of tilt and
        orientation, including Rooftops and GroundFloors
    tilt_facade : list of floats [degree]
        Tilt of facades against the horizontal.
    orientation_facade : list of floats [degree]
        Orientation of facades (Azimuth).
        0 - North
        90 - East
        180 - South
        270 - West

    """

    def __init__(self, thermal_zone, merge_windows, t_bt):
        """Constructor for TwoElement"""

        self.internal_id = random.random()

        self.thermal_zone = thermal_zone
        self.merge_windows = merge_windows
        self.t_bt = t_bt

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
        self.weightfactor_ground = 0.0
        self.outer_wall_areas = []

        # Attributes for windows
        self.area_win = 0.0

        # coefficient of heat transfer facing the inside of this thermal zone
        self.alpha_conv_inner_win = 0.0
        self.alpha_rad_inner_win = 0.0
        self.alpha_comb_inner_win = 0.0
        self.ratio_conv_rad_inner_win = 0.0

        # coefficient of heat transfer facing the ambient
        self.alpha_conv_outer_win = 0.0
        self.alpha_rad_outer_win = 0.0
        self.alpha_comb_outer_win = 0.0

        # UA-Value
        self.ua_value_win = 0.0
        self.u_value_win = 0.0

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
        self.ir_emissivity_win = 0.0
        self.ir_emissivity_inner_win = 0.0
        self.solar_absorp_win = 0.0

        # Additional attributes
        self.weightfactor_win = []
        self.window_areas = []
        self.transparent_areas = []
        self.g_sunblind = []
        self.weighted_g_value = 0.0

        # Misc values

        self.alpha_rad_inner_mean = 0.0
        self.alpha_rad_outer_mean = 0.0
        self.n_outer = 0
        self.facade_areas = []
        self.tilt_facade = []
        self.orientation_facade = []
        self.heat_load = 0.0
        self.cool_load = 0.0

    def calc_attributes(self):
        """Calls all necessary function to calculate model attributes"""

        outer_walls = (self.thermal_zone.outer_walls +
                       self.thermal_zone.ground_floors +
                       self.thermal_zone.rooftops)

        for out_wall in outer_walls:
            out_wall.calc_equivalent_res()
            out_wall.calc_ua_value()
        for win in self.thermal_zone.windows:
            win.calc_equivalent_res()
            win.calc_ua_value()
        for inner_wall in (self.thermal_zone.inner_walls +
                           self.thermal_zone.floors +
                           self.thermal_zone.ceilings):
            inner_wall.calc_equivalent_res()
            inner_wall.calc_ua_value()

        self.set_calc_default()
        if len(outer_walls) < 1:
            warnings.warn("No walls are defined as outer walls for thermal " +
                          "zone " + self.thermal_zone.name + " in building " +
                          self.thermal_zone.parent.name +
                          ", please be careful with results. In addition " +
                          "this might lead to RunTimeErrors")
        else:
            self._sum_outer_wall_elements()
        if len(self.thermal_zone.windows) < 1:
            warnings.warn('For thermal zone ' + self.thermal_zone.name +
                          ' in building ' + self.thermal_zone.parent.name +
                          ', no windows have been defined.')
        else:
            self._sum_window_elements()
        if len(outer_walls) >= 1 or len(self.thermal_zone.windows) >= 1:
            self._calc_outer_elements()
            self._calc_wf()
            self._calc_mean_values()
        self._calc_number_of_elements()
        self._fill_zone_lists()
        self._calc_heat_load()

    @staticmethod
    def _calc_parallel_connection(element_list, omega):
        """Parallel connection of walls according to VDI 6007

        Calculates the parallel connection of wall elements according to VDI
        6007, resulting in R1 and C1 (equation 23, 24).

        Parameters
        ----------
        element_list : list
            List of inner or outer walls
        omega : float
            VDI 6007 frequency

        Returns
        ----------
        r1 : float [K/W]
            VDI 6007 resistance for all inner or outer walls
        c1 : float [K/W]
            VDI 6007 capacity all for inner or outer walls
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

    def _sum_outer_wall_elements(self):
        """Sum attributes for outer wall elements

        This function sums and computes the area-weighted values,
        where necessary (the class doc string) for coefficients of heat
        transfer, resistances, areas and UA-Values.

        For TwoElement model it treats rooftops, ground floor and outer walls
        as one kind of wall type.

        """
        # treat all outer wall types identical

        self.area_ow = \
            (sum(out_wall.area for out_wall in
                 self.thermal_zone.outer_walls)
             + sum(ground.area for ground in
                   self.thermal_zone.ground_floors)
             + sum(roof.area for roof in
                   self.thermal_zone.rooftops))

        self.ua_value_ow = \
            (sum(out_wall.ua_value for out_wall in
                 self.thermal_zone.outer_walls)
             + sum(ground.ua_value for ground in
                   self.thermal_zone.ground_floors)
             + sum(roof.ua_value for roof in
                   self.thermal_zone.rooftops))

        self.r_total_ow = 1 / self.ua_value_ow

        # values facing the inside of the thermal zone

        self.r_conv_inner_ow = (1 /
                                (sum(1 / out_wall.r_inner_conv for out_wall in
                                     self.thermal_zone.outer_walls)
                                 + sum(1 / ground.r_inner_conv for ground in
                                       self.thermal_zone.ground_floors)
                                 + sum(1 / roof.r_inner_conv for roof in
                                       self.thermal_zone.rooftops)))

        self.r_rad_inner_ow = (1 /
                               (sum(1 / out_wall.r_inner_rad for out_wall in
                                    self.thermal_zone.outer_walls)
                                + sum(1 / ground.r_inner_rad for ground in
                                      self.thermal_zone.ground_floors)
                                + sum(1 / roof.r_inner_rad for roof in
                                      self.thermal_zone.rooftops)))

        self.r_comb_inner_ow = (1 /
                                (sum(1 / out_wall.r_inner_comb for out_wall in
                                     self.thermal_zone.outer_walls)
                                 + sum(1 / ground.r_inner_comb for ground in
                                       self.thermal_zone.ground_floors)
                                 + sum(1 / roof.r_inner_comb for roof in
                                       self.thermal_zone.rooftops)))

        self.ir_emissivity_inner_ow = (
            (sum(out_wall.layer[0].material.ir_emissivity * out_wall.area for
                 out_wall in self.thermal_zone.outer_walls)
             + sum(ground.layer[0].material.ir_emissivity * ground.area for
                   ground in self.thermal_zone.ground_floors)
             + sum(roof.layer[0].material.ir_emissivity * roof.area for
                   roof in self.thermal_zone.rooftops)) / self.area_ow)

        self.alpha_conv_inner_ow = (
            1 / (self.r_conv_inner_ow * self.area_ow))
        self.alpha_rad_inner_ow = (
            1 / (self.r_rad_inner_ow * self.area_ow))
        self.alpha_comb_inner_ow = (
            1 / (self.r_comb_inner_ow * self.area_ow))

        # values facing the ambient
        # ground floor does not have any coefficients on ambient side

        _area_ow_rt = (sum(out_wall.area for out_wall in
                           self.thermal_zone.outer_walls)
                       + sum(roof.area for roof in
                             self.thermal_zone.rooftops))

        self.r_conv_outer_ow = (1 /
                                (sum(1 / out_wall.r_outer_conv for out_wall in
                                     self.thermal_zone.outer_walls)
                                 + sum(1 / roof.r_outer_conv for roof in
                                       self.thermal_zone.rooftops)))
        self.r_rad_outer_ow = (1 /
                               (sum(1 / out_wall.r_outer_rad for out_wall in
                                    self.thermal_zone.outer_walls)
                                + sum(1 / roof.r_outer_rad for roof in
                                      self.thermal_zone.rooftops)))
        self.r_comb_outer_ow = (1 /
                                (sum(1 / out_wall.r_outer_comb for out_wall in
                                     self.thermal_zone.outer_walls)
                                 + sum(1 / roof.r_outer_comb for roof in
                                       self.thermal_zone.rooftops)))

        self.ir_emissivity_outer_ow = (
            (sum(out_wall.layer[-1].material.ir_emissivity * out_wall.area for
                 out_wall in self.thermal_zone.outer_walls)
             + sum(roof.layer[-1].material.ir_emissivity * roof.area for
                   roof in self.thermal_zone.rooftops)) / _area_ow_rt)

        self.solar_absorp_ow = (
            (sum(out_wall.layer[-1].material.solar_absorp * out_wall.area for
                 out_wall in self.thermal_zone.outer_walls)
             + sum(roof.layer[-1].material.solar_absorp * roof.area for
                   roof in self.thermal_zone.rooftops)) / _area_ow_rt)

        self.alpha_conv_outer_ow = (
            1 / (self.r_conv_outer_ow * _area_ow_rt))
        self.alpha_rad_outer_ow = (
            1 / (self.r_rad_outer_ow * _area_ow_rt))
        self.alpha_comb_outer_ow = (
            1 / (self.r_comb_outer_ow * _area_ow_rt))

    def _sum_window_elements(self):
        """Sum attributes for window elements

        This function sums and computes the area-weighted values,
        where necessary (the class doc string) for coefficients of heat
        transfer, resistances, areas and UA-Values.

        Function is identical for TwoElement, ThreeElement and FourElement.
        """

        self.area_win = sum(win.area for win in self.thermal_zone.windows)
        self.ua_value_win = sum(
            win.ua_value for win in self.thermal_zone.windows)
        self.u_value_win = self.ua_value_win / self.area_win

        self.r_total_win = 1 / self.ua_value_win
        # values facing the inside of the thermal zone

        self.r_conv_inner_win = (1 / (sum(1 / win.r_inner_conv for win in
                                          self.thermal_zone.windows)))

        self.r_rad_inner_win = (1 / (sum(1 / win.r_inner_rad for win in
                                         self.thermal_zone.windows)))

        self.r_comb_inner_win = (1 / (sum(1 / win.r_inner_comb for win in
                                          self.thermal_zone.windows)))

        self.ir_emissivity_inner_win = sum(
            win.layer[0].material.ir_emissivity * win.area for win in
            self.thermal_zone.windows) / self.area_win

        self.alpha_conv_inner_win = (
            1 / (self.r_conv_inner_win * self.area_win))
        self.alpha_rad_inner_win = (
            1 / (self.r_rad_inner_win * self.area_win))
        self.alpha_comb_inner_win = (
            1 / (self.r_comb_inner_win * self.area_win))
        self.ratio_conv_rad_inner_win = sum(win.a_conv * win.area for win in
                                            self.thermal_zone.windows) / \
            self.area_win

        # values facing the ambient

        self.r_conv_outer_win = (1 / (sum(1 / win.r_outer_conv for win in
                                          self.thermal_zone.windows)))

        self.r_rad_outer_win = (1 / (sum(1 / win.r_outer_rad for win in
                                         self.thermal_zone.windows)))

        self.r_comb_outer_win = (1 / (sum(1 / win.r_outer_comb for win in
                                          self.thermal_zone.windows)))

        self.ir_emissivity_win = sum(win.layer[-1].material.ir_emissivity
                                     * win.area for win in
                                     self.thermal_zone.windows) / self.area_win

        self.solar_absorp_win = sum(win.layer[-1].material.solar_absorp
                                    * win.area for win in
                                    self.thermal_zone.windows) / self.area_win

        self.weighted_g_value = sum(win.g_value * win.area for win in
                                    self.thermal_zone.windows) / self.area_win

        self.alpha_conv_outer_win = (
            1 / (self.r_conv_outer_win * self.area_win))
        self.alpha_rad_outer_win = (
            1 / (self.r_rad_outer_win * self.area_win))
        self.alpha_comb_outer_win = (
            1 / (self.r_comb_outer_win * self.area_win))

    def _calc_outer_elements(self):
        """Lumped parameter for outer wall elements

        Calculates all necessary parameters for outer walls. This includes
        OuterWalls, GroundFloors and Rooftops.
        Attributes
        ----------
        omega : float [1/s]
            angular frequency with given time period.
        outer_walls : list
            List containing all TEASER Wall instances that are treated as same
            outer wall type. In case of TwoElement model OuterWalls,
            GroundFloors, Rooftops
        """

        omega = 2 * math.pi / 86400 / self.t_bt

        outer_walls = (self.thermal_zone.outer_walls +
                       self.thermal_zone.ground_floors +
                       self.thermal_zone.rooftops)

        if 0 < len(outer_walls) <= 1:
            # only one outer wall, no need to calculate chain matrix
            self.r1_ow = outer_walls[0].r1
            self.c1_ow = outer_walls[0].c1_korr
        elif len(outer_walls) > 1:
            # more than one outer wall, calculate chain matrix
            self.r1_ow, self.c1_ow = self._calc_parallel_connection(outer_walls,
                                                                    omega)

        if self.merge_windows is False:
            try:

                if len(self.thermal_zone.windows) > 0:
                    self.r1_win = (1 / sum((1 / win.r1) for win in
                                           self.thermal_zone.windows))
                if len(self.thermal_zone.outer_walls) > 0:
                    conduction = (1 / sum((1 / element.r_conduc) for element in
                                  outer_walls))

                    self.r_rest_ow = (conduction - self.r1_ow)

            except RuntimeError:
                print("As no outer walls or no windows are defined lumped "
                      "parameter cannot be calculated")

        if self.merge_windows is True:

            try:

                if len(self.thermal_zone.windows) > 0 and  \
                   len(self.thermal_zone.outer_walls) > 0:
                    self.r1_win = 1 / sum(1 / (win.r1 / 6) for win in
                                          self.thermal_zone.windows)

                    self.r1_ow = 1 / (1 / self.r1_ow + 1 / self.r1_win)

                    self.r_total_ow = 1 / (self.ua_value_ow +
                                           self.ua_value_win)
                    self.r_rest_ow = (self.r_total_ow - self.r1_ow - 1 / (
                        ((1 / self.r_conv_inner_ow)
                         + (1 / self.r_conv_inner_win)
                         + (1 / self.r_rad_inner_ow)
                         + (1 / self.r_rad_inner_win)))) - 1 / (
                        self.alpha_comb_outer_ow * self.area_ow)

                self.ir_emissivity_inner_ow = (
                    (self.ir_emissivity_inner_ow * self.area_ow
                     + self.ir_emissivity_inner_win * self.area_win)
                    / (self.area_ow + self.area_win))

                self.ir_emissivity_outer_ow = (
                    (self.ir_emissivity_outer_ow * self.area_ow
                     + self.ir_emissivity_win * self.area_win)
                    / (self.area_ow + self.area_win))

                self.solar_absorp_ow = (
                    (self.solar_absorp_ow * self.area_ow
                     + self.solar_absorp_win * self.area_win)
                    / (self.area_ow + self.area_win))

            except RuntimeError:
                print("As no outer walls or no windows are defined lumped "
                      "parameter cannot be calculated")

    def _calc_wf(self):
        """Weightfactors for outer elements(walls, roof, ground floor, windows)

        Calculates the weightfactors of the outer walls, including ground and
        windows.

        Parameters
        ----------
        outer_walls : list
            List containing all TEASER Wall instances that are treated as same
            outer wall type. In case of TwoElement model OuterWalls,
            GroundFloors, Rooftops
        """

        outer_walls = (self.thermal_zone.outer_walls +
                       self.thermal_zone.ground_floors +
                       self.thermal_zone.rooftops)

        if self.merge_windows is True:

            for wall in outer_walls:
                wall.wf_out = wall.ua_value / (
                    self.ua_value_ow + self.ua_value_win)

            for win in self.thermal_zone.windows:
                win.wf_out = win.ua_value / (
                    self.ua_value_ow + self.ua_value_win)

            self.weightfactor_ground = sum(gf.wf_out for gf in
                                           self.thermal_zone.ground_floors)

        elif self.merge_windows is False:

            for wall in outer_walls:
                wall.wf_out = wall.ua_value / self.ua_value_ow

            for win in self.thermal_zone.windows:
                win.wf_out = win.ua_value / self.ua_value_win

            self.weightfactor_ground = sum(gf.wf_out for gf in
                                           self.thermal_zone.ground_floors)

        else:
            raise ValueError("specify merge window method correctly")

    def _calc_mean_values(self):
        """Calculates mean values for inner and outer elements

        This function calculates mean values inside the thermal zone (e.g.
        the mean value for coefficient of radiative heat transfer between
        inner and outer walls
        """

        self.alpha_rad_inner_mean = (self.area_ow * self.alpha_rad_inner_ow +
                                     self.area_win * self.alpha_rad_inner_win
                                     ) / (self.area_ow + self.area_win)
        self.alpha_rad_outer_mean = (self.area_ow * self.alpha_rad_outer_ow +
                                     self.area_win * self.alpha_rad_outer_win) \
            / (self.area_ow + self.area_win)

    def _calc_number_of_elements(self):
        """Calculates the number of outer elements with different tilt/orient

        This function calculates the number of outer elements with a
        different combination of orientation and tilt, this includes the
        rooftops and ground floors.
        """

        outer_elements = (
            self.thermal_zone.outer_walls +
            self.thermal_zone.ground_floors +
            self.thermal_zone.rooftops +
            self.thermal_zone.windows)

        tilt_orient = []
        for element in outer_elements:
            tilt_orient.append((element.orientation, element.tilt))
        self.n_outer = len(list(set(tilt_orient)))

    def _fill_zone_lists(self):
        """Fills lists like weightfactors and tilt, orientation

        Fills the lists of a zone  according to orientation and tilt of the
        zone. Therefore it compares orientation and tilt of all outer
        elements and then creates lists for zone weightfactors, orientation,
        tilt, ares and sunblinds."""

        outer_elements = (
            self.thermal_zone.outer_walls +
            self.thermal_zone.rooftops +
            self.thermal_zone.windows +
            self.thermal_zone.ground_floors)

        tilt_orient = []
        for element in outer_elements:
            tilt_orient.append((element.orientation, element.tilt))
        tilt_orient = list(set(tilt_orient))

        for i in tilt_orient:
            wall_rt = \
                self.thermal_zone.find_walls(i[0], i[1]) + \
                self.thermal_zone.find_rts(i[0], i[1])
            wins = self.thermal_zone.find_wins(i[0], i[1])
            gf = self.thermal_zone.find_gfs(i[0], i[1])

            if self.merge_windows is True:
                self.facade_areas.append(sum([element.area for element in (
                    wall_rt + wins + gf)]))
            else:
                self.facade_areas.append(sum([element.area for element in (
                    wall_rt + gf)]))

            self.orientation_facade.append(i[0])
            self.tilt_facade.append(i[1])

            if not wall_rt:

                if not gf:
                    self.weightfactor_ow.append(0.0)
                    self.outer_wall_areas.append(0.0)
                else:
                    self.weightfactor_ow.append(0.0)
                    self.outer_wall_areas.append((sum([element.area for element
                                                       in gf])))
            else:
                self.weightfactor_ow.append(
                    sum([wall.wf_out for wall in wall_rt]))
                self.outer_wall_areas.append(sum([wall.area for wall in
                                                  wall_rt]))

            if not wins:
                self.weightfactor_win.append(0.0)
                self.g_sunblind.append(0.0)
                self.window_areas.append(0.0)
                self.transparent_areas.append(0.0)
            else:
                self.weightfactor_win.append(
                    sum([win.wf_out for win in wins]))
                self.g_sunblind.append(
                    sum([win.shading_g_total for win in wins]))

                if self.merge_windows is False:
                    self.window_areas.append(
                        sum([win.area for win in wins]))
                    self.transparent_areas.append(
                        sum([win.area for win in wins]))

                else:
                    self.window_areas.append(0)
                    self.transparent_areas.append(
                        sum([win.area for win in wins]))

    def _calc_heat_load(self):
        """Static heat load calculation

        This function calculates the static heat load of the thermal zone by
        multiplying the UA-Value of the elements with the given Temperature
        difference of t_inside and t_outside. And takes heat losses through
        infiltration into account.

        Attributes
        ----------
        ua_value_ow_temp : float [W/(m2*K)]
            UA Value without GroundFloors
        ua_value_gf_temp : float [W/(m2*K)]
            UA Value of all GroundFloors
        """
        self.heat_load = 0.0
        ua_value_gf_temp = sum(
            ground.ua_value for ground in self.thermal_zone.ground_floors)
        ua_value_ow_temp = self.ua_value_ow - ua_value_gf_temp
        self.heat_load = \
            ((((ua_value_ow_temp + self.ua_value_win) +
               self.thermal_zone.volume *
               self.thermal_zone.use_conditions.infiltration_rate * 1 / 3600 *
               self.thermal_zone.heat_capac_air *
               self.thermal_zone.density_air) * (self.thermal_zone.t_inside -
                                                 self.thermal_zone.t_outside))
             + (ua_value_gf_temp * (self.thermal_zone.t_inside -
                                    self.thermal_zone.t_ground)))

    def set_calc_default(self):
        """sets default calculation parameters
        """

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
        self.weightfactor_ground = 0.0
        self.outer_wall_areas = []

        # TODO: check this value
        self.r_rad_ow_iw = 0.0

        # Attributes for windows
        self.area_win = 0.0

        # coefficient of heat transfer facing the inside of this thermal zone
        self.alpha_conv_inner_win = 0.0
        self.alpha_rad_inner_win = 0.0
        self.alpha_comb_inner_win = 0.0
        self.ratio_conv_rad_inner_win = 0.0

        # coefficient of heat transfer facing the ambient
        self.alpha_conv_outer_win = 0.0
        self.alpha_rad_outer_win = 0.0
        self.alpha_comb_outer_win = 0.0

        # UA-Value
        self.ua_value_win = 0.0
        self.u_value_win = 0.0

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
        self.ir_emissivity_win = 0.0
        self.solar_absorp_win = 0.0

        # Additional attributes
        self.weightfactor_win = []
        self.window_areas = []
        self.transparent_areas = []
        self.g_sunblind = []
        self.weighted_g_value = 0.0

        # Misc values

        self.alpha_rad_inner_mean = 0.0
        self.n_outer = 0
        self.facade_areas = []
        self.tilt_facade = []
        self.orientation_facade = []
        self.heat_load = 0.0
        self.cool_load = 0.0
