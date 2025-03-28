# created January 2017

from __future__ import division
import math
import numpy as np
import random
import warnings


class FiveElement(object):
    """This class contains attributes and functions for five element model

    This model adds new elements for borders with neighboured zones. Doing so,
    borders to the same zone are lumped, but those to different zones are not.
    As a consequence, the final model may have more than five elements.

    It treats OuterWalls, Rooftops and GroundFloors separate resulting in three
    RC-combination for these, and one additional RC combination per bordered
    neighboured zone.
    Depending on the chosen method it will consider an extra resistance for
    windows or merge all windows into the RC-Combination for outer walls.

    Parameters
    ----------
    thermal_zone: ThermalZone()
        TEASER instance of ThermalZone
    merge_windows : boolean
        True for merging windows into the outer wall's RC-combination,
        False for separate resistance for window, default is False. (Only
        supported for IBPSA)
    t_bt : float [d]
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
        walls facing the adjacent thermal zone. (Currently not supported)
    alpha_rad_outer_iw : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of interior
        walls facing the adjacent thermal zone. (Currently not supported)
    alpha_comb_outer_iw : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of interior walls
        facing the adjacent thermal zone. (Currently not supported)
    ua_value_iw : float [W/K]
        U-Value times interior wall area. (Does not take adjacent thermal
        zones into account)
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
        Lumped resistance of interior walls no heat transfer coefficients for
        convection and radiation are accounted in this resistance.
    c1_iw : float [J/K]
        Lumped capacity of interior walls

    Outer Walls

    area_ow : float [m2]
        Area of all outer walls .
    alpha_conv_inner_ow : float [W/(m2K)]
        Area-weighted convective coefficient of heat transfer of outer walls
        facing the inside of this thermal zone .
    alpha_rad_inner_ow : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of outer walls
        facing the inside of this thermal zone .
    alpha_comb_inner_ow : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of outer walls
        facing the inside of this thermal zone .
    alpha_conv_outer_ow : float [W/(m2K)]
        Area-weighted convective coefficient of heat transfer of outer walls
        facing the ambient.
    alpha_rad_outer_ow : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of outer walls
        facing the ambient .
    alpha_comb_outer_ow : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of outer walls
        facing the ambient.
    ua_value_ow : float [W/K]
        U-Value times outer wall area.
    r_conv_inner_ow : float [K/W]
        Sum of convective resistances for all outer walls facing the
        inside of this thermal zone .
    r_rad_inner_ow : float [K/W]
        Sum of radiative resistances for all outer walls facing the
        inside of this thermal zone .
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
        Lumped capacity of outer walls .
    weightfactor_ow : list of floats
        Weightfactors of outer walls (UA-Value of walls with same orientation
        and tilt divided by ua_value_ow)
    outer_wall_areas : list of floats [m2]
        Area of all outer walls in one list.
    ir_emissivity_outer_ow : float
        Area-weighted ir emissivity of outer wall facing the ambient.
    ir_emissivity_inner_ow : float
        Area-weighted ir emissivity of outer walls facing the thermal zone.
    solar_absorp_ow : float
        Area-weighted solar absorption of outer walls facing the ambient.

    Ground Floors

    area_gf : float [m2]
        Area of all ground floors.
    alpha_conv_inner_gf : float [W/(m2K)]
        Area-weighted convective coefficient of heat transfer of ground floors
        facing the inside of this thermal zone.
    alpha_rad_inner_gf : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of ground floors
        facing the inside of this thermal zone.
    alpha_comb_inner_gf : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of ground floors
        facing the inside of this thermal zone.
    ua_value_gf : float [W/K]
        U-Value times ground floor area.
    r_conv_inner_gf : float [K/W]
        Sum of convective resistances for all ground floors facing the
        inside of this thermal zone.
    r_rad_inner_gf : float [K/W]
        Sum of radiative resistances for all ground floors facing the
        inside of this thermal zone.
    r_comb_inner_gf : float [K/W]
        Sum of combined resistances for all ground floors facing the
        inside of this thermal zone.
    r1_gf : float [K/W]
        Lumped resistance of ground floors no heat transfer coefficients for
        convection and radiation are accounted in this resistance.
    r_rest_gf : float [K/W]
        Lumped remaining resistance of ground floors between r1_gf and c1_gf no
        heat transfer coefficients for convection and radiation are accounted
        in this resistance.
    c1_gf : float [J/K]
        Lumped capacity of ground floors.
    weightfactor_gf : float
        Weightfactor of ground floors (UA-Value of walls with same orientation
        and tilt divided by ua_value_gf)
    ground_floor_area : float [m2]
        Area of all ground floors.
    r_rad_gf_iw : float [K/W]
        Resistance for radiative heat transfer between walls.
        TODO: needs to be checked
    ir_emissivity_inner_gf : float
        Area-weighted ir emissivity of ground floors facing the thermal zone.

    Rooftops

    area_rt : float [m2]
        Area of all rooftops .
    alpha_conv_inner_rt : float [W/(m2K)]
        Area-weighted convective coefficient of heat transfer of rooftops
        facing the inside of this thermal zone .
    alpha_rad_inner_rt : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of rooftops
        facing the inside of this thermal zone .
    alpha_comb_inner_rt : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of rooftops
        facing the inside of this thermal zone .
    alpha_conv_outer_rt : float [W/(m2K)]
        Area-weighted convective coefficient of heat transfer of rooftops
        facing the ambient.
    alpha_rad_outer_rt : float [W/(m2K)]
        Area-weighted radiative coefficient of heat transfer of rooftops
        facing the ambient .
    alpha_comb_outer_rt : float [W/(m2K)]
        Area-weighted combined coefficient of heat transfer of rooftops
        facing the ambient.
    ua_value_rt : float [W/K]
        U-Value times outer wall area.
    r_conv_inner_rt : float [K/W]
        Sum of convective resistances for all rooftops facing the
        inside of this thermal zone .
    r_rad_inner_rt : float [K/W]
        Sum of radiative resistances for all rooftops facing the
        inside of this thermal zone .
    r_comb_inner_rt : float [K/W]
        Sum of combined resistances for all rooftops facing the
        inside of this thermal zone.
    r_conv_outer_rt : float [K/W]
        Sum of convective resistances for all rooftops facing the
        ambient.
    r_rad_outer_rt : float [K/W]
        Sum of radiative resistances for all rooftops facing the
        ambient.
    r_comb_outer_rt : float [K/W]
        Sum of combined resistances for all rooftops facing the
        ambient.
    r1_rt : float [K/W]
        Lumped resistance of rooftops no heat transfer coefficients for
        convection and radiation are accounted in this resistance.
    r_rest_rt : float [K/W]
        Lumped remaining resistance of rooftops between r1_rt and c1_rt no
        heat transfer coefficients for convection and radiation are accounted
        in this resistance.
    c1_rt : float [J/K]
        Lumped capacity of rooftops .
    weightfactor_rt : list of floats
        Weightfactors of rooftops (UA-Value of walls with same orientation
        and tilt divided by ua_value_rt)
    weightfactor_win_rt : list of floats
        Weightfactors of windows in rooftop. CAUTION: this will be always a
        list full of zeors, as windows are always calculated separatly.
    outer_wall_areas : list of floats [m2]
        Area of all rooftops in one list.
    r_rad_rt_iw : float [K/W]
        Resistance for radiative heat transfer between walls.
        TODO: needs to be checked
    ir_emissivity_outer_rt : float
        Area-weighted ir emissivity of outer wall facing the ambient.
    ir_emissivity_inner_rt : float
        Area-weighted ir emissivity of rooftops facing the thermal zone.
    solar_absorp_rt : float
        Area-weighted solar absorption of rooftops facing the ambient.
    tilt_rt : list of floats [degree]
        Tilt of rooftops against the horizontal.
    orientation_rt : list of floats [degree]
        Orientation of rooftops (Azimuth).
        0 - North
        90 - East
        180 - South
        270 - West

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
        U-Value times outer wall area.
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
    shading_max_irr : list of float [W/m2]
        Threshold value above which the sunblind becomes active for the whole zone.
        Threshold regards to the incoming irradiation level with the window direction.
        This value does not account for heat flux due to the outside temperature.
    shading_g_total : list of float
        Factor representing how much of the actual solar irradiation goes through
        the sunblind and enters the window element, for the case, that the sunblind is
        activated. Defaults to 1, i.e. no shading is active.

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
        orientation, windows and outer walls
    n_rt : int
        Number of total facades with different combination of tilt and
        orientation, Rooftops
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
        """Constructor for FourElement"""

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

        # Attributes for outer walls
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

        # Attributes for GroundFloor
        self.area_gf = 0.0

        # coefficient of heat transfer facing the inside of this thermal zone
        self.alpha_conv_inner_gf = 0.0
        self.alpha_rad_inner_gf = 0.0
        self.alpha_comb_inner_gf = 0.0

        # UA-Value
        self.ua_value_gf = 0.0

        # resistances for heat transfer facing the inside of this thermal zone
        self.r_conv_inner_gf = 0.0
        self.r_rad_inner_gf = 0.0
        self.r_comb_inner_gf = 0.0

        # lumped resistances/capacity
        self.r1_gf = 0.0
        self.r_rest_gf = 0.0
        self.c1_gf = 0.0
        self.r_total_gf = 0.0

        # Optical properties
        self.ir_emissivity_inner_gf = 0.0

        # Additional attributes

        self.weightfactor_ground = 0.0

        # Attributes for rooftops
        self.area_rt = 0.0

        # coefficient of heat transfer facing the inside of this thermal zone
        self.alpha_conv_inner_rt = 0.0
        self.alpha_rad_inner_rt = 0.0
        self.alpha_comb_inner_rt = 0.0

        # coefficient of heat transfer facing the ambient
        self.alpha_conv_outer_rt = 0.0
        self.alpha_rad_outer_rt = 0.0
        self.alpha_comb_outer_rt = 0.0

        # UA-Value
        self.ua_value_rt = 0.0

        # resistances for heat transfer facing the inside of this thermal zone
        self.r_conv_inner_rt = 0.0
        self.r_rad_inner_rt = 0.0
        self.r_comb_inner_rt = 0.0

        # resistances for heat transfer facing the ambient
        self.r_conv_outer_rt = 0.0
        self.r_rad_outer_rt = 0.0
        self.r_comb_outer_rt = 0.0

        # lumped resistances/capacity
        self.r1_rt = 0.0
        self.r_rest_rt = 0.0
        self.c1_rt = 0.0
        self.r_total_rt = 0.0

        # Optical properties
        self.ir_emissivity_outer_rt = 0.0
        self.ir_emissivity_inner_rt = 0.0
        self.solar_absorp_rt = 0.0

        # Additional attributes
        self.weightfactor_rt = []
        self.weightfactor_win_rt = []
        self.rooftop_areas = []
        self.tilt_rt = []
        self.orientation_rt = []

        # TODO: check this value
        self.r_rad_rt_iw = 0.0

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
        self.shading_g_total = []
        self.shading_max_irr = []
        self.weighted_g_value = 0.0

        # Attributes for neighboured zones (vectorized - one element per other
        # zone)
        self.area_nzb = []

        # coefficient of heat transfer facing the inside of this thermal zone
        self.alpha_conv_inner_nzb = []
        self.alpha_rad_inner_nzb = []
        self.alpha_comb_inner_nzb = []

        # coefficient of heat transfer facing the other thermal zone
        self.alpha_conv_outer_nzb = []
        self.alpha_rad_outer_nzb = []
        self.alpha_comb_outer_nzb = []

        # UA-Value
        self.ua_value_nzb = []

        # resistances for heat transfer facing the inside of this thermal zone
        self.r_conv_inner_nzb = []
        self.r_rad_inner_nzb = []
        self.r_comb_inner_nzb = []

        # resistances for heat transfer facing the ambient
        self.r_conv_outer_nzb = []
        self.r_rad_outer_nzb = []
        self.r_comb_outer_nzb = []

        # lumped resistances/capacity
        self.r1_nzb = []
        self.r_rest_nzb = []
        self.c1_nzb = []
        self.r_total_nzb = []

        # Optical properties
        self.ir_emissivity_outer_nzb = []
        self.ir_emissivity_inner_nzb = []

        # Additional parameters
        self.nz_index = []
        self.other_nz_indexes = []
        self.nzbs_per_nz = []

        # Misc values
        self.n_outer = 0
        self.all_tilts = []
        self.all_orientations = []
        self.alpha_rad_inner_mean = 0.0
        self.alpha_rad_outer_mean = 0.0
        self.heat_load = 0.0
        self.cool_load = 0.0

        # Misc values

        self.alpha_rad_inner_mean = 0.0
        self.alpha_rad_outer_mean = 0.0
        self.n_outer = 0
        self.n_rt = 0
        self.facade_areas = []
        self.tilt_facade = []
        self.orientation_facade = []
        self.heat_load = 0.0
        self.cool_load = 0.0

    def calc_attributes(self):
        """Calls all necessary function to calculate model attributes"""

        for out_wall in self.thermal_zone.outer_walls:
            out_wall.calc_equivalent_res()
            out_wall.calc_ua_value()
        for rt in self.thermal_zone.rooftops:
            rt.calc_equivalent_res()
            rt.calc_ua_value()
        for gf in self.thermal_zone.ground_floors:
            gf.calc_equivalent_res()
            gf.calc_ua_value()
        for nzb in self.thermal_zone.interzonal_elements:
            nzb.calc_equivalent_res()
            nzb.calc_ua_value()
        for win in self.thermal_zone.windows:
            win.calc_equivalent_res()
            win.calc_ua_value()
        for inner_wall in (
            self.thermal_zone.inner_walls
            + self.thermal_zone.floors
            + self.thermal_zone.ceilings
        ):
            inner_wall.calc_equivalent_res()
            inner_wall.calc_ua_value()

        self.set_calc_default()
        if len(self.thermal_zone.outer_walls) < 1:
            warnings.warn(
                "No walls are defined as outer walls for thermal "
                + "zone "
                + self.thermal_zone.name
                + " in building "
                + self.thermal_zone.parent.name
                + ", please be careful with results. In addition "
                + "this might lead to RunTimeErrors"
            )
        else:
            self._sum_outer_wall_elements()
        if (
            len(
                self.thermal_zone.inner_walls
                + self.thermal_zone.floors
                + self.thermal_zone.ceilings
                + self.nzbs_for_iw
            )
            < 1
        ):
            warnings.warn(
                "For thermal zone "
                + self.thermal_zone.name
                + " in building "
                + self.thermal_zone.parent.name
                + ", no inner walls have been defined."
            )
        else:
            self._sum_inner_wall_elements()
            self._calc_inner_elements()
        if (
            len(self.thermal_zone.find_izes_outer(add_reversed=True))
            < 1
        ):
            warnings.warn(
                "For thermal zone "
                + self.thermal_zone.name
                + " in building "
                + self.thermal_zone.parent.name
                + ", no interzonal elements have been defined."
            )
        else:
            self._sum_interzonal_elements()
            self._calc_interzonal_elements()
        if len(self.thermal_zone.windows) < 1:
            warnings.warn(
                "For thermal zone "
                + self.thermal_zone.name
                + " in building "
                + self.thermal_zone.parent.name
                + ", no windows have been defined."
            )
        else:
            self._sum_window_elements()
        if len(self.thermal_zone.ground_floors) < 1:
            warnings.warn(
                "For thermal zone "
                + self.thermal_zone.name
                + " in building "
                + self.thermal_zone.parent.name
                + ", no ground floors have been defined."
            )
        else:
            self._sum_ground_floor_elements()
            self._calc_ground_floor_elements()
        if len(self.thermal_zone.rooftops) < 1:
            warnings.warn(
                "For thermal zone "
                + self.thermal_zone.name
                + " in building "
                + self.thermal_zone.parent.name
                + ", no rooftops have been defined."
            )
        else:
            self._sum_rooftop_elements()
            self._calc_rooftop_elements()
        if (
            len(self.thermal_zone.outer_walls) >= 1
            or len(self.thermal_zone.windows) >= 1
        ):
            self._calc_outer_elements()
            self._calc_wf()
            self._calc_mean_values()
        if self.nzbs_for_iw:
            warnings.warn(
                "For thermal zone "
                + self.thermal_zone.name
                + " in building "
                + self.thermal_zone.parent.name
                + ", interzonal elements have been defined that are treated as "
                + "inner elements based on your settings to them or the project"
                + " parameter 'method_interzonal_export'."
            )
        self._calc_number_of_elements()
        self._fill_zone_lists()
        self._calc_heat_load()
        self.cool_load = -self.heat_load

        return True

    @staticmethod
    def _calc_parallel_connection(element_list, omega, mode='iw'):
        """Parallel connection of walls according to VDI 6007

        Calculates the parallel connection of wall elements according to VDI
        6007, resulting in R1 and C1 (equation 23, 24).

        Parameters
        ----------
        element_list : list
            List of inner or outer walls
        omega : float
            VDI 6007 frequency
        mode : str
            'ow' uses r1 and c1_korr
            'iw' uses r1 and c1 (function falls back here for other strings)
            'izw_backwards' uses r2 and c1_korr because heat flow goes towards
                this thermal zone (instead of away from it) for interzonal
                elements between heated and unheated zones

        Returns
        ----------
        r1 : float [K/W]
            VDI 6007 resistance for all inner or outer walls
        c1 : float [K/W]
            VDI 6007 capacity all for inner or outer walls
        """

        for wall_count in range(len(element_list) - 1):

            if wall_count == 0:
                if mode == 'izw_backwards':
                    r1_before = element_list[wall_count].r2
                else:
                    r1_before = element_list[wall_count].r1
                if mode == 'ow' or mode == 'izw_backwards':
                    c1_before = element_list[wall_count].c1_korr
                else:
                    c1_before = element_list[wall_count].c1
            else:
                r1_before = r1
                c1_before = c1
            if mode == 'izw_backwards':
                r1_add = element_list[wall_count + 1].r2
            else:
                r1_add = element_list[wall_count + 1].r1
            if mode == 'ow' or mode == 'izw_backwards':
                c1_add = element_list[wall_count + 1].c1_korr
            else:
                c1_add = element_list[wall_count + 1].c1

            r1 = (r1_before * c1_before ** 2 + r1_add * c1_add ** 2
                  + omega ** 2 * r1_before * r1_add * (r1_before + r1_add)
                  * c1_before ** 2 * c1_add ** 2) \
                 / ((c1_before + c1_add) ** 2
                    + omega ** 2 * (r1_before + r1_add) ** 2 * c1_before ** 2
                    * c1_add ** 2)

            c1 = ((c1_before + c1_add) ** 2
                  + omega ** 2 * (r1_before + r1_add) ** 2 * c1_before ** 2
                  * c1_add ** 2) \
                 / (c1_before + c1_add
                    + omega ** 2
                    * (r1_before ** 2 * c1_before + r1_add ** 2 * c1_add)
                    * c1_before
                    * c1_add)

        return r1, c1

    def _sum_outer_wall_elements(self):
        """Sum attributes for outer wall elements

        This function sums and computes the area-weighted values,
        where necessary  for coefficients of heat
        transfer, resistances, areas and UA-Values.

        For ThreeElement model it treats rooftops and outer walls
        as one kind of wall type.

        """

        self.area_ow = sum(out_wall.area for out_wall in self.thermal_zone.outer_walls)

        self.ua_value_ow = sum(
            out_wall.ua_value for out_wall in self.thermal_zone.outer_walls
        )

        self.r_total_ow = 1 / self.ua_value_ow

        # values facing the inside of the thermal zone

        self.r_conv_inner_ow = 1 / (
            sum(1 / out_wall.r_inner_conv for out_wall in self.thermal_zone.outer_walls)
        )

        self.r_rad_inner_ow = 1 / (
            sum(1 / out_wall.r_inner_rad for out_wall in self.thermal_zone.outer_walls)
        )

        self.r_comb_inner_ow = 1 / (
            sum(1 / out_wall.r_inner_comb for out_wall in self.thermal_zone.outer_walls)
        )

        self.ir_emissivity_inner_ow = (
            sum(
                out_wall.layer[0].material.ir_emissivity * out_wall.area
                for out_wall in self.thermal_zone.outer_walls
            )
        ) / self.area_ow

        self.alpha_conv_inner_ow = 1 / (self.r_conv_inner_ow * self.area_ow)
        self.alpha_rad_inner_ow = 1 / (self.r_rad_inner_ow * self.area_ow)
        self.alpha_comb_inner_ow = 1 / (self.r_comb_inner_ow * self.area_ow)

        # values facing the ambient
        # ground floor does not have any coefficients on ambient side

        self.r_conv_outer_ow = 1 / (
            sum(1 / out_wall.r_outer_conv for out_wall in self.thermal_zone.outer_walls)
        )
        self.r_rad_outer_ow = 1 / (
            sum(1 / out_wall.r_outer_rad for out_wall in self.thermal_zone.outer_walls)
        )
        self.r_comb_outer_ow = 1 / (
            sum(1 / out_wall.r_outer_comb for out_wall in self.thermal_zone.outer_walls)
        )

        self.ir_emissivity_outer_ow = (
            (
                sum(
                    out_wall.layer[-1].material.ir_emissivity * out_wall.area
                    for out_wall in self.thermal_zone.outer_walls
                )
            )
        ) / self.area_ow

        self.solar_absorp_ow = (
            (
                sum(
                    out_wall.layer[-1].material.solar_absorp * out_wall.area
                    for out_wall in self.thermal_zone.outer_walls
                )
            )
        ) / self.area_ow

        self.alpha_conv_outer_ow = 1 / (self.r_conv_outer_ow * self.area_ow)
        self.alpha_rad_outer_ow = 1 / (self.r_rad_outer_ow * self.area_ow)
        self.alpha_comb_outer_ow = 1 / (self.r_comb_outer_ow * self.area_ow)

    def _sum_ground_floor_elements(self):
        """Sum attributes for ground floor elements

        This function sums and computes the area-weighted values,
        where necessary (the class doc string) for coefficients of heat
        transfer, resistances, areas and UA-Values.

        """

        self.area_gf = sum(ground.area for ground in self.thermal_zone.ground_floors)

        self.ua_value_gf = sum(
            ground.ua_value for ground in self.thermal_zone.ground_floors
        )

        self.r_total_gf = 1 / self.ua_value_gf

        # values facing the inside of the thermal zone

        self.r_conv_inner_gf = 1 / sum(
            1 / ground.r_inner_conv for ground in self.thermal_zone.ground_floors
        )

        self.r_rad_inner_gf = 1 / sum(
            1 / ground.r_inner_rad for ground in self.thermal_zone.ground_floors
        )

        self.r_comb_inner_gf = 1 / sum(
            1 / ground.r_inner_comb for ground in self.thermal_zone.ground_floors
        )

        self.ir_emissivity_inner_gf = (
            sum(
                ground.layer[0].material.ir_emissivity * ground.area
                for ground in self.thermal_zone.ground_floors
            )
            / self.area_gf
        )

        self.alpha_conv_inner_gf = 1 / (self.r_conv_inner_gf * self.area_gf)
        self.alpha_rad_inner_gf = 1 / (self.r_rad_inner_gf * self.area_gf)
        self.alpha_comb_inner_gf = 1 / (self.r_comb_inner_gf * self.area_gf)

    def _sum_rooftop_elements(self):
        """Sum attributes for rooftop elements

        This function sums and computes the area-weighted values,
        where necessary  for coefficients of heat
        transfer, resistances, areas and UA-Values.

        For ThreeElement model it treats rooftops and outer walls
        as one kind of wall type.

        """

        self.area_rt = sum(roof.area for roof in self.thermal_zone.rooftops)

        self.ua_value_rt = sum(roof.ua_value for roof in self.thermal_zone.rooftops)

        self.r_total_rt = 1 / self.ua_value_rt

        # values facing the inside of the thermal zone

        self.r_conv_inner_rt = 1 / sum(
            1 / roof.r_inner_conv for roof in self.thermal_zone.rooftops
        )

        self.r_rad_inner_rt = 1 / sum(
            1 / roof.r_inner_rad for roof in self.thermal_zone.rooftops
        )

        self.r_comb_inner_rt = 1 / sum(
            1 / roof.r_inner_comb for roof in self.thermal_zone.rooftops
        )

        self.ir_emissivity_inner_rt = (
            sum(
                roof.layer[0].material.ir_emissivity * roof.area
                for roof in self.thermal_zone.rooftops
            )
            / self.area_rt
        )

        self.alpha_conv_inner_rt = 1 / (self.r_conv_inner_rt * self.area_rt)
        self.alpha_rad_inner_rt = 1 / (self.r_rad_inner_rt * self.area_rt)
        self.alpha_comb_inner_rt = 1 / (self.r_comb_inner_rt * self.area_rt)

        # values facing the ambient
        # ground floor does not have any coefficients on ambient side

        self.r_conv_outer_rt = 1 / sum(
            1 / roof.r_outer_conv for roof in self.thermal_zone.rooftops
        )
        self.r_rad_outer_rt = 1 / sum(
            1 / roof.r_outer_rad for roof in self.thermal_zone.rooftops
        )
        self.r_comb_outer_rt = 1 / sum(
            1 / roof.r_outer_comb for roof in self.thermal_zone.rooftops
        )

        self.ir_emissivity_outer_rt = (
            sum(
                roof.layer[-1].material.ir_emissivity * roof.area
                for roof in self.thermal_zone.rooftops
            )
            / self.area_rt
        )

        self.solar_absorp_rt = (
            sum(
                roof.layer[-1].material.solar_absorp * roof.area
                for roof in self.thermal_zone.rooftops
            )
            / self.area_rt
        )

        self.alpha_conv_outer_rt = 1 / (self.r_conv_outer_rt * self.area_rt)
        self.alpha_rad_outer_rt = 1 / (self.r_rad_outer_rt * self.area_rt)
        self.alpha_comb_outer_rt = 1 / (self.r_comb_outer_rt * self.area_rt)

    def _sum_inner_wall_elements(self):
        """Sum attributes for interior elements

        This function sums and computes the area-weighted values,
        where necessary (the class doc string) for coefficients of heat
        transfer, resistances, areas and UA-Values.

        It treats all inner walls identical.

        Function is identical for TwoElement, ThreeElement and FourElement.

        Calculation of adjacent thermal zones and thus these attributes are
        currently not supported.

        """
        self.area_iw = (
            sum(in_wall.area for in_wall in self.thermal_zone.inner_walls)
            + sum(floor.area for floor in self.thermal_zone.floors)
            + sum(ceiling.area for ceiling in self.thermal_zone.ceilings)
            + sum(nzb.area for nzb in self.nzbs_for_iw)
        )

        self.ua_value_iw = (
            sum(in_wall.ua_value for in_wall in self.thermal_zone.inner_walls)
            + sum(floor.ua_value for floor in self.thermal_zone.floors)
            + sum(ceiling.ua_value for ceiling in self.thermal_zone.ceilings)
            + sum(nzb.ua_value for nzb in self.nzbs_for_iw)
        )

        # values facing the inside of the thermal zone

        self.r_conv_inner_iw = 1 / (
            sum(1 / in_wall.r_inner_conv for in_wall in self.thermal_zone.inner_walls)
            + sum(1 / floor.r_inner_conv for floor in self.thermal_zone.floors)
            + sum(1 / ceiling.r_inner_conv for ceiling in self.thermal_zone.ceilings)
            + sum(1 / nzb.r_inner_conv for nzb in self.nzbs_for_iw)
        )

        self.r_rad_inner_iw = 1 / (
            sum(1 / in_wall.r_inner_rad for in_wall in self.thermal_zone.inner_walls)
            + sum(1 / floor.r_inner_rad for floor in self.thermal_zone.floors)
            + sum(1 / ceiling.r_inner_rad for ceiling in self.thermal_zone.ceilings)
            + sum(1 / nzb.r_inner_rad for nzb in self.nzbs_for_iw)
        )

        self.r_comb_inner_iw = 1 / (
            sum(1 / in_wall.r_inner_comb for in_wall in self.thermal_zone.inner_walls)
            + sum(1 / floor.r_inner_comb for floor in self.thermal_zone.floors)
            + sum(1 / ceiling.r_inner_comb for ceiling in self.thermal_zone.ceilings)
            + sum(1 / nzb.r_inner_comb for nzb in self.nzbs_for_iw)
        )

        self.ir_emissivity_inner_iw = (
            sum(
                in_wall.layer[0].material.ir_emissivity * in_wall.area
                for in_wall in self.thermal_zone.inner_walls
            )
            + sum(
                floor.layer[0].material.ir_emissivity * floor.area
                for floor in self.thermal_zone.floors
            )
            + sum(
                ceiling.layer[0].material.ir_emissivity * ceiling.area
                for ceiling in self.thermal_zone.ceilings
            )
            + sum(
                nzb.layer[0].material.ir_emissivity * nzb.area
                for nzb in self.nzbs_for_iw
            )
        ) / self.area_iw

        self.alpha_conv_inner_iw = 1 / (self.r_conv_inner_iw * self.area_iw)
        self.alpha_rad_inner_iw = 1 / (self.r_rad_inner_iw * self.area_iw)
        self.alpha_comb_inner_iw = 1 / (self.r_comb_inner_iw * self.area_iw)

    def _sum_window_elements(self):
        """Sum attributes for window elements

        This function sums and computes the area-weighted values,
        where necessary (the class doc string) for coefficients of heat
        transfer, resistances, areas and UA-Values.

        Function is identical for TwoElement, ThreeElement, FourElement and
        FiveElement.
        """

        self.area_win = sum(win.area for win in self.thermal_zone.windows)
        self.ua_value_win = sum(win.ua_value for win in self.thermal_zone.windows)
        self.u_value_win = self.ua_value_win / self.area_win

        # values facing the inside of the thermal zone

        self.r_conv_inner_win = 1 / (
            sum(1 / win.r_inner_conv for win in self.thermal_zone.windows)
        )

        self.r_rad_inner_win = 1 / (
            sum(1 / win.r_inner_rad for win in self.thermal_zone.windows)
        )

        self.r_comb_inner_win = 1 / (
            sum(1 / win.r_inner_comb for win in self.thermal_zone.windows)
        )

        self.ir_emissivity_inner_win = (
            sum(
                win.layer[0].material.ir_emissivity * win.area
                for win in self.thermal_zone.windows
            )
            / self.area_win
        )

        self.alpha_conv_inner_win = 1 / (self.r_conv_inner_win * self.area_win)
        self.alpha_rad_inner_win = 1 / (self.r_rad_inner_win * self.area_win)
        self.alpha_comb_inner_win = 1 / (self.r_comb_inner_win * self.area_win)
        self.ratio_conv_rad_inner_win = (
            sum(win.a_conv * win.area for win in self.thermal_zone.windows)
            / self.area_win
        )

        # values facing the ambient

        self.r_conv_outer_win = 1 / (
            sum(1 / win.r_outer_conv for win in self.thermal_zone.windows)
        )

        self.r_rad_outer_win = 1 / (
            sum(1 / win.r_outer_rad for win in self.thermal_zone.windows)
        )

        self.r_comb_outer_win = 1 / (
            sum(1 / win.r_outer_comb for win in self.thermal_zone.windows)
        )

        self.ir_emissivity_win = (
            sum(
                win.layer[-1].material.ir_emissivity * win.area
                for win in self.thermal_zone.windows
            )
            / self.area_win
        )

        self.solar_absorp_win = (
            sum(
                win.layer[-1].material.solar_absorp * win.area
                for win in self.thermal_zone.windows
            )
            / self.area_win
        )

        self.weighted_g_value = (
            sum(win.g_value * win.area for win in self.thermal_zone.windows)
            / self.area_win
        )

        self.alpha_conv_outer_win = 1 / (self.r_conv_outer_win * self.area_win)
        self.alpha_rad_outer_win = 1 / (self.r_rad_outer_win * self.area_win)
        self.alpha_comb_outer_win = 1 / (self.r_comb_outer_win * self.area_win)

    def _sum_interzonal_elements(self):
        """Sum attributes for neighboured zone border elements

        This function sums and computes the area-weighted values,
        where necessary (the class doc string) for coefficients of heat
        transfer, resistances, areas and UA-Values.

        """
        other_nz_indexes = set()
        for nz_border in self.thermal_zone.find_izes_outer(add_reversed=True):
            other_nz_indexes.add(self.thermal_zone.parent.thermal_zones.index(
                nz_border.other_side
            ))
        self.other_nz_indexes = list(other_nz_indexes)
        self.nzbs_per_nz = []
        for nz_index in self.other_nz_indexes:
            other_nz = self.thermal_zone.parent.thermal_zones[nz_index]
            self.nzbs_per_nz.append([])
            for nz_border \
                    in self.thermal_zone.find_izes_outer(add_reversed=True):
                if nz_border.other_side is other_nz:
                    self.nzbs_per_nz[-1].append(nz_border)
                    nz_border.idx_orientation = nz_index

        self.area_nzb = _lump_sum(self.nzbs_per_nz, 'area')

        self.ua_value_nzb = _lump_sum(self.nzbs_per_nz, 'ua_value')

        self.r_total_nzb = [1 / ua for ua in self.ua_value_nzb]

        # values facing the inside of the thermal zone

        self.r_conv_inner_nzb = _lump_inverse_sum(self.nzbs_per_nz,
                                                  'r_inner_conv')

        self.r_rad_inner_nzb = _lump_inverse_sum(self.nzbs_per_nz,
                                                 'r_inner_rad')

        self.r_comb_inner_nzb = _lump_inverse_sum(self.nzbs_per_nz,
                                                  'r_inner_comb')

        self.ir_emissivity_inner_nzb = [
            sum(el.layer[0].material.ir_emissivity * el.area for el in els) / a
            for els, a in zip(self.nzbs_per_nz, self.area_nzb)
        ]

        self.alpha_conv_inner_nzb = [
            1 / (rci * a)
            for rci, a in zip(self.r_conv_inner_nzb, self.area_nzb)
        ]
        self.alpha_rad_inner_nzb = [
            1 / (rri * a)
            for rri, a in zip(self.r_rad_inner_nzb, self.area_nzb)
        ]
        self.alpha_comb_inner_nzb = [
            1 / (rci * a)
            for rci, a in zip(self.r_comb_inner_nzb, self.area_nzb)
        ]

        # values facing the other zone

        self.r_conv_outer_nzb = _lump_inverse_sum(self.nzbs_per_nz,
                                                  'r_outer_conv')
        self.r_rad_outer_nzb = _lump_inverse_sum(self.nzbs_per_nz,
                                                 'r_outer_rad')
        self.r_comb_outer_nzb = _lump_inverse_sum(self.nzbs_per_nz,
                                                  'r_outer_comb')

        self.ir_emissivity_outer_nzb = [
            sum(el.layer[-1].material.ir_emissivity * el.area for el in els) / a
            for els, a in zip(self.nzbs_per_nz, self.area_nzb)
        ]

        self.alpha_conv_outer_nzb = [
            1 / (rco * a)
            for rco, a in zip(self.r_conv_outer_nzb, self.area_nzb)]
        self.alpha_rad_outer_nzb = [
            1 / (rro * a)
            for rro, a in zip(self.r_rad_outer_nzb, self.area_nzb)]
        self.alpha_comb_outer_nzb = [
            1 / (rco * a)
            for rco, a in zip(self.r_comb_outer_nzb, self.area_nzb)
        ]

    def _calc_outer_elements(self):
        """Lumped parameter for outer wall elements

        Calculates all necessary parameters for outer walls. This includes
        OuterWalls and Rooftops.

        Attributes
        ----------
        omega : float [1/s]
            angular frequency with given time period.
        outer_walls : list
            List containing all TEASER Wall instances that are treated as same
            outer wall type. In case of TwoElement model OuterWalls, Rooftops
        """

        omega = 2 * math.pi / 86400 / self.t_bt

        outer_walls = self.thermal_zone.outer_walls

        if 0 < len(outer_walls) <= 1:
            # only one outer wall, no need to calculate chain matrix
            self.r1_ow = outer_walls[0].r1
            self.c1_ow = outer_walls[0].c1_korr
        elif len(outer_walls) > 1:
            # more than one outer wall, calculate chain matrix
            self.r1_ow, self.c1_ow = self._calc_parallel_connection(
                outer_walls, omega, mode='ow'
            )
        else:
            warnings.warn(
                "No walls are defined as outer walls, please be "
                "careful with results. In addition this might lead "
                "to RunTimeErrors"
            )

        if self.merge_windows is False:
            try:

                if len(self.thermal_zone.windows) > 0:
                    self.r1_win = 1 / sum(
                        (1 / win.r1) for win in self.thermal_zone.windows
                    )
                if len(self.thermal_zone.outer_walls) > 0:
                    conduction = 1 / sum(
                        (1 / element.r_conduc) for element in outer_walls
                    )

                    self.r_rest_ow = conduction - self.r1_ow

            except RuntimeError:
                print(
                    "As no outer walls or no windows are defined lumped "
                    "parameter cannot be calculated"
                )

        if self.merge_windows is True:

            try:
                if (
                    len(self.thermal_zone.windows) > 0
                    and len(self.thermal_zone.outer_walls) > 0
                ):
                    self.r1_win = 1 / sum(
                        1 / (win.r1 / 6) for win in self.thermal_zone.windows
                    )

                    self.r1_ow = 1 / (1 / self.r1_ow + 1 / self.r1_win)

                    self.r_total_ow = 1 / (self.ua_value_ow + self.ua_value_win)
                    self.r_rest_ow = (
                        self.r_total_ow
                        - self.r1_ow
                        - 1
                        / (
                            (
                                (1 / self.r_conv_inner_ow)
                                + (1 / self.r_conv_inner_win)
                                + (1 / self.r_rad_inner_ow)
                                + (1 / self.r_rad_inner_win)
                            )
                        )
                    ) - 1 / (self.alpha_comb_outer_ow * self.area_ow)

                self.ir_emissivity_inner_ow = (
                    self.ir_emissivity_inner_ow * self.area_ow
                    + self.ir_emissivity_inner_win * self.area_win
                ) / (self.area_ow + self.area_win)

                self.ir_emissivity_outer_ow = (
                    self.ir_emissivity_outer_ow * self.area_ow
                    + self.ir_emissivity_win * self.area_win
                ) / (self.area_ow + self.area_win)

                self.solar_absorp_ow = (
                    self.solar_absorp_ow * self.area_ow
                    + self.solar_absorp_win * self.area_win
                ) / (self.area_ow + self.area_win)

            except RuntimeError:
                print(
                    "As no outer walls or no windows are defined lumped "
                    "parameter cannot be calculated"
                )

    def _calc_ground_floor_elements(self):
        """Lumped parameter for ground floor elements

        Calculates lumped parameters for ground floors. No windows in ground
        floor allowed.

        Attributes
        ----------
        omega : float [1/s]
            angular frequency with given time period.
        """
        omega = 2 * math.pi / 86400 / self.t_bt

        if 0 < len(self.thermal_zone.ground_floors) <= 1:
            # only one outer wall, no need to calculate chain matrix
            self.r1_gf = self.thermal_zone.ground_floors[0].r1
            self.c1_gf = self.thermal_zone.ground_floors[0].c1_korr
        elif len(self.thermal_zone.ground_floors) > 1:
            # more than one outer wall, calculate chain matrix
            self.r1_gf, self.c1_gf = self._calc_parallel_connection(
                self.thermal_zone.ground_floors, omega, mode='ow'
            )
        else:
            warnings.warn(
                "No walls are defined as ground floors, please be "
                "careful with results. In addition this might lead "
                "to RunTimeErrors"
            )
        try:
            conduction = 1 / sum(
                (1 / element.r_conduc) for element in self.thermal_zone.ground_floors
            )

            self.r_rest_gf = conduction - self.r1_gf
        except RuntimeError:
            print(
                "As no ground floors are defined lumped "
                "parameter cannot be calculated"
            )

    def _calc_rooftop_elements(self):
        """Lumped parameter for rooftop elements

        Calculates lumped parameters for rooftops. Windows are considered in
        outer wall calculation. This results in an error concerning the
        interior radiation distribution. But currently there is no other option.

        Attributes
        ----------
        omega : float [1/s]
            angular frequency with given time period.
        """

        omega = 2 * math.pi / 86400 / self.t_bt

        if 0 < len(self.thermal_zone.rooftops) <= 1:
            # only one outer wall, no need to calculate chain matrix
            self.r1_rt = self.thermal_zone.rooftops[0].r1
            self.c1_rt = self.thermal_zone.rooftops[0].c1_korr
        elif len(self.thermal_zone.rooftops) > 1:
            # more than one outer wall, calculate chain matrix
            self.r1_rt, self.c1_rt = self._calc_parallel_connection(
                self.thermal_zone.rooftops, omega, mode='ow'
            )
        else:
            warnings.warn(
                "No walls are defined as ground floors, please be "
                "careful with results. In addition this might lead "
                "to RunTimeErrors"
            )
        try:
            conduction = 1 / sum(
                (1 / element.r_conduc) for element in self.thermal_zone.rooftops
            )

            self.r_rest_rt = conduction - self.r1_rt
        except RuntimeError:
            print("As no rooftops are defined lumped " "parameter cannot be calculated")

    def _calc_inner_elements(self):
        """Lumped parameter for inner wall elements

        Calculates all necessary parameters for inner walls. This includes
        InnerWalls, Ceilings and Floors.

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

        inner_walls = (
            self.thermal_zone.inner_walls
            + self.thermal_zone.floors
            + self.thermal_zone.ceilings
        )

        for in_wall in inner_walls:
            in_wall.calc_equivalent_res()
            in_wall.calc_ua_value()

        if 0 < len(inner_walls) <= 1:
            # only one inner wall, no need to calculate chain matrix
            self.r1_iw = inner_walls[0].r1
            self.c1_iw = inner_walls[0].c1_korr
        elif len(inner_walls) > 1:
            # more than one inner wall, calculate chain matrix
            self.r1_iw, self.c1_iw = self._calc_parallel_connection(
                inner_walls, omega, mode='iw'
            )
        else:
            warnings.warn(
                "No walls are defined as inner walls, please be "
                "careful with results. In addition this might lead "
                "to RunTimeErrors"
            )

    def _calc_interzonal_elements(self):
        """Lumped parameter for neighboured zone border elements

        Calculates lumped parameters for borders to
        neighboured zones. No windows allowed.

        Attributes
        ----------
        omega : float [1/s]
            angular frequency with given time period.
        """

        omega = 2 * math.pi / 86400 / self.t_bt

        any_nzb = False
        self.r1_nzb = []
        self.c1_nzb = []
        for nz_borders in self.nzbs_per_nz:
            if 0 < len(nz_borders) <= 1:
                # only one nz border, no need to calculate chain matrix
                self.c1_nzb.append(nz_borders[0].c1_korr)
                conduction = nz_borders[0].r_conduc
                if nz_borders[0].interzonal_type_export == 'outer_reversed':
                    self.r_rest_nzb.append(nz_borders[0].r2)
                    self.r1_nzb.append(conduction - self.r_rest_nzb[-1])
                else:
                    self.r1_nzb.append(nz_borders[0].r1)
                    self.r_rest_nzb.append(conduction - self.r1_nzb[-1])
            elif len(nz_borders) > 1:
                # more than one nz border, calculate chain matrix
                if nz_borders[0].interzonal_type_export == 'outer_reversed':
                    parallel_mode = 'izw_backwards'
                else:
                    parallel_mode = 'ow'
                r1_nzb, c1_nzb = self._calc_parallel_connection(
                    nz_borders, omega, mode=parallel_mode
                )
                conduction = 1 / sum(1 / nzb.r_conduc for nzb in nz_borders)
                if nz_borders[0].interzonal_type_export == 'outer_reversed':
                    self.r_rest_nzb.append(r1_nzb)
                    self.r1_nzb.append(conduction - self.r_rest_nzb[-1])
                else:
                    self.r1_nzb.append(r1_nzb)
                    self.r_rest_nzb.append(conduction - self.r1_nzb[-1])
                self.c1_nzb.append(c1_nzb)

    def _calc_wf(self):
        """Weightfactors for outer elements(walls, roof, ground floor, windows)

        Calculates the weightfactors of outer walls, rooftops, including
        ground and windows.

        """

        self.weightfactor_ground = 0.0

        if self.merge_windows is True:

            for wall in self.thermal_zone.outer_walls:
                wall.wf_out = wall.ua_value / (self.ua_value_ow + self.ua_value_win)

            for win in self.thermal_zone.windows:
                win.wf_out = win.ua_value / (self.ua_value_ow + self.ua_value_win)

            for rt in self.thermal_zone.rooftops:
                rt.wf_out = rt.ua_value / self.ua_value_rt

        elif self.merge_windows is False:

            for wall in self.thermal_zone.outer_walls:
                wall.wf_out = wall.ua_value / self.ua_value_ow

            for win in self.thermal_zone.windows:
                win.wf_out = win.ua_value / self.ua_value_win

            for rt in self.thermal_zone.rooftops:
                rt.wf_out = rt.ua_value / self.ua_value_rt

        else:
            raise ValueError("specify merge window method correctly")

    def _calc_mean_values(self):
        """Calculates mean values for inner and outer elements

        This function calculates mean values inside the thermal zone (e.g.
        the mean value for coefficient of radiative heat transfer between
        inner and outer walls
        """

        self.alpha_rad_inner_mean = (
            self.area_ow * self.alpha_rad_inner_ow
            + self.area_win * self.alpha_rad_inner_win
            + self.area_gf * self.alpha_rad_inner_gf
            + self.area_rt * self.alpha_rad_inner_rt
            + np.dot(self.area_nzb, self.alpha_rad_inner_nzb)
            + self.area_iw * self.alpha_rad_inner_iw
        ) / (self.area_ow + self.area_win + self.area_iw + self.area_gf + self.area_rt)
        self.alpha_rad_outer_mean = (
            self.area_ow * self.alpha_rad_outer_ow
            + self.area_rt * self.alpha_rad_outer_rt
            + self.area_win * self.alpha_rad_outer_win
        ) / (self.area_ow + self.area_rt + self.area_win)

    def _calc_number_of_elements(self):
        """Calculates the number of facade elements with different tilt/orient

        This function calculates the number of outer elements with a
        different combination of orientation and tilt, this includes the
        outer walls, rooftops and windows.
        """

        outer_elements = self.thermal_zone.outer_walls + self.thermal_zone.windows

        tilt_orient = []
        for element in outer_elements:
            tilt_orient.append((element.orientation, element.tilt))
        self.n_outer = len(list(set(tilt_orient)))

        tilt_orient_rt = []
        for roof in self.thermal_zone.rooftops:
            tilt_orient_rt.append((roof.orientation, roof.tilt))
        self.n_rt = len(list(set(tilt_orient_rt)))

    def _fill_zone_lists(self):
        """Fills lists like weightfactors and tilt, orientation

        Fills the lists of a zone  according to orientation and tilt of the
        zone. Therefore it compares orientation and tilt of all outer
        elements and then creates lists for zone weightfactors, orientation,
        tilt, ares and sunblinds."""

        outer_elements = self.thermal_zone.outer_walls + self.thermal_zone.windows

        tilt_orient = []
        for element in outer_elements:
            tilt_orient.append((element.orientation, element.tilt))
        tilt_orient = list(set(tilt_orient))

        for i in tilt_orient:
            walls = self.thermal_zone.find_walls(i[0], i[1])
            wins = self.thermal_zone.find_wins(i[0], i[1])

            if self.merge_windows is True:
                self.facade_areas.append(
                    sum([element.area for element in (walls + wins)])
                )
            else:
                self.facade_areas.append(sum([element.area for element in (walls)]))

            self.orientation_facade.append(i[0])
            self.tilt_facade.append(i[1])

            if not walls:
                self.weightfactor_ow.append(0.0)
                self.outer_wall_areas.append(0.0)
            else:
                self.weightfactor_ow.append(sum([wall.wf_out for wall in walls]))
                self.outer_wall_areas.append(sum([wall.area for wall in walls]))

            if not wins:
                self.weightfactor_win.append(0.0)
                self.shading_g_total.append(1.0)
                self.window_areas.append(0.0)
                self.transparent_areas.append(0.0)
                self.shading_max_irr.append(9999.9)
            else:
                self.weightfactor_win.append(sum([win.wf_out for win in wins]))

                if self.merge_windows is False:
                    self.window_areas.append(sum([win.area for win in wins]))
                    self.transparent_areas.append(sum([win.area for win in wins]))

                else:
                    self.window_areas.append(0)
                    self.transparent_areas.append(sum([win.area for win in wins]))
                self.shading_g_total.append(
                    sum(
                        [
                            win.shading_g_total * win.area / sum([w.area for w in wins])
                            for win in wins
                        ]
                    )
                )
                self.shading_max_irr.append(
                    sum(
                        [
                            win.shading_max_irr * win.area / sum([w.area for w in wins])
                            for win in wins
                        ]
                    )
                )

        tilt_orient_rt = []
        for roof in self.thermal_zone.rooftops:
            tilt_orient_rt.append((roof.orientation, roof.tilt))
        tilt_orient_rt = list(set(tilt_orient_rt))

        for i in tilt_orient_rt:
            rts = self.thermal_zone.find_rts(i[0], i[1])

            self.orientation_rt.append(i[0])
            self.tilt_rt.append(i[1])
            self.weightfactor_win_rt.append(0)
            if not rts:
                self.weightfactor_rt.append(0.0)
                self.rooftop_areas.append(0.0)
            else:
                self.weightfactor_rt.append(sum([rt.wf_out for rt in rts]))
                self.rooftop_areas.append(sum([rt.area for rt in rts]))

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

        if self.thermal_zone.parent.parent.t_soil_mode == 2:
            t_ground = self.thermal_zone.t_ground \
                       - self.thermal_zone.t_ground_amplitude
        else:
            t_ground = self.thermal_zone.t_ground

        ua_value_ow_temp = self.ua_value_rt + self.ua_value_ow

        ua_value_nzb_temp = 0.0
        if self.thermal_zone.use_conditions.with_heating:
            for other_zone_index, ua_value_izw in zip(self.other_nz_indexes,
                                                      self.ua_value_nzb):
                if not self.thermal_zone.parent.thermal_zones[
                        other_zone_index
                ].use_conditions.with_heating:
                    ua_value_nzb_temp += ua_value_izw

        self.heat_load_outside_factor = (
            (ua_value_ow_temp + self.ua_value_win + ua_value_nzb_temp)
            + self.thermal_zone.volume
            * self.thermal_zone.use_conditions.infiltration_rate
            * 1
            / 3600
            * self.thermal_zone.heat_capac_air
            * self.thermal_zone.density_air
        )
        self.heat_load_ground_factor = self.ua_value_gf
        self.heat_load = \
            self.heat_load_outside_factor \
            * (self.thermal_zone.t_inside - self.thermal_zone.t_outside) \
            + self.heat_load_ground_factor \
            * (self.thermal_zone.t_inside - t_ground)

    def set_calc_default(self):
        """sets default calculation parameters
        """

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

        # Attributes for outer walls
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

        # Attributes for GroundFloor
        self.area_gf = 0.0

        # coefficient of heat transfer facing the inside of this thermal zone
        self.alpha_conv_inner_gf = 0.0
        self.alpha_rad_inner_gf = 0.0
        self.alpha_comb_inner_gf = 0.0

        # UA-Value
        self.ua_value_gf = 0.0

        # resistances for heat transfer facing the inside of this thermal zone
        self.r_conv_inner_gf = 0.0
        self.r_rad_inner_gf = 0.0
        self.r_comb_inner_gf = 0.0

        # lumped resistances/capacity
        self.r1_gf = 0.0
        self.r_rest_gf = 0.0
        self.c1_gf = 0.0
        self.r_total_gf = 0.0

        # Optical properties
        self.ir_emissivity_inner_gf = 0.0

        # Additional attributes

        self.weightfactor_ground = 0.0

        # Attributes for rooftops
        self.area_rt = 0.0

        # coefficient of heat transfer facing the inside of this thermal zone
        self.alpha_conv_inner_rt = 0.0
        self.alpha_rad_inner_rt = 0.0
        self.alpha_comb_inner_rt = 0.0

        # coefficient of heat transfer facing the ambient
        self.alpha_conv_outer_rt = 0.0
        self.alpha_rad_outer_rt = 0.0
        self.alpha_comb_outer_rt = 0.0

        # UA-Value
        self.ua_value_rt = 0.0

        # resistances for heat transfer facing the inside of this thermal zone
        self.r_conv_inner_rt = 0.0
        self.r_rad_inner_rt = 0.0
        self.r_comb_inner_rt = 0.0

        # resistances for heat transfer facing the ambient
        self.r_conv_outer_rt = 0.0
        self.r_rad_outer_rt = 0.0
        self.r_comb_outer_rt = 0.0

        # lumped resistances/capacity
        self.r1_rt = 0.0
        self.r_rest_rt = 0.0
        self.c1_rt = 0.0
        self.r_total_rt = 0.0

        # Optical properties
        self.ir_emissivity_outer_rt = 0.0
        self.ir_emissivity_inner_rt = 0.0
        self.solar_absorp_rt = 0.0

        # Additional attributes
        self.weightfactor_rt = []
        self.rooftop_areas = []
        self.tilt_rt = []
        self.orientation_rt = []

        # TODO: check this value
        self.r_rad_rt_iw = 0.0

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
        self.shading_g_total = []
        self.shading_max_irr = []
        self.weighted_g_value = 0.0

        # Attributes for neighboured zones (vectorized - one element per other
        # zone)
        self.area_nzb = []

        # coefficient of heat transfer facing the inside of this thermal zone
        self.alpha_conv_inner_nzb = []
        self.alpha_rad_inner_nzb = []
        self.alpha_comb_inner_nzb = []

        # coefficient of heat transfer facing the other thermal zone
        self.alpha_conv_outer_nzb = []
        self.alpha_rad_outer_nzb = []
        self.alpha_comb_outer_nzb = []

        # UA-Value
        self.ua_value_nzb = []

        # resistances for heat transfer facing the inside of this thermal zone
        self.r_conv_inner_nzb = []
        self.r_rad_inner_nzb = []
        self.r_comb_inner_nzb = []

        # resistances for heat transfer facing the ambient
        self.r_conv_outer_nzb = []
        self.r_rad_outer_nzb = []
        self.r_comb_outer_nzb = []

        # lumped resistances/capacity
        self.r1_nzb = []
        self.r_rest_nzb = []
        self.c1_nzb = []
        self.r_total_nzb = []

        # Optical properties
        self.ir_emissivity_outer_nzb = []
        self.ir_emissivity_inner_nzb = []

        # Additional parameters
        self.nz_index = []
        self.other_nz_indexes = []
        self.nzbs_per_nz = []

        # Misc values

        self.alpha_rad_inner_mean = 0.0
        self.n_outer = 0
        self.n_rt = 0
        self.facade_areas = []
        self.tilt_facade = []
        self.orientation_facade = []
        self.heat_load = 0.0
        self.cool_load = 0.0

    @property
    def nzbs_for_iw(self):
        """returns borders to neighboured zones to be considered as inner walls

        Returns
        -------
        value : list
            list of those interzonal elements that are to be treated as
            'inner' depending on their 'interzonal_type_export' attribute

        """
        elements = []
        for i in self.thermal_zone.interzonal_elements:
            if i.interzonal_type_export == 'inner':
                elements.append(i)
            else:
                pass
        return elements


def _lump_sum(elements, parameter):
    """calculates sums of the parameter of 2nd-level entries in a 2-level list

    Parameters
    ----------
    elements : list
        list of lists with building elements
    parameter : str
        parameter to lump

    Returns
    -------
    lumped_sum : list
        list of sums for each sub-list of elements
    """
    return [sum(eval('el.{}'.format(parameter)) for el in els)
            for els in elements]


def _lump_inverse_sum(elements, parameter):
    """inverse sums of the parameter of 2nd-level entries in a 2-level list

    Parameters
    ----------
    elements : list
        list of lists with building elements
    parameter : str
        parameter to lump

    Returns
    -------
    lumped_sum : list
        list of sums of inverse entries for each sub-list of elements
    """
    return [1 / sum(1 / eval('el.{}'.format(parameter)) for el in els)
            for els in elements]
