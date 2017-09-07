# -*- coding: utf-8 -*-
"""Module contains class to calculate a thermal zone with VDI core"""
from __future__ import division

import math
import numpy as np


class VDICore(object):
    """Class to handle VDI 6007 simulation directly in Python.

    Contains function and classes to simulate according to VDI core directly in
    python.

    Parameters
    ----------
    thermal_zone: instance of ThermalZone
        TEASER instance of ThermalZone
    weather_data:  instance of WeatherData class
        TEASER isntance of WeatherData class containing TRY weather data.
    building: instance of Building
        TEASER instance of Building
    room_air_temperature: np.array or pd.series
        simulation results for room air temperature in degree Celsius
    heat_load: np.array
        simulation results for heating load in Watt
    cooling_load: np.array
        simulation results for cooling load in Watt
    heater_limit: list (of floats)
        List with heater limit values in Watt
    cooler_limit: list (of floats)
        List with cooler limit values in Watt
    initial_air_temp : float
        Initial indoor air temperature in Kelvin
    initial_inner_wall_temp : float
        Initial inner wall temperature in Kelvin
    initial_outer_wall_temp : float
        Initial outer wall temperature in Kelvin
    heater_order : np.array (of int)
        describes in which order the different heating devices are turned on
    cooler_order : np.array (of int)
        describes in which order the different cooling devices are turned on
    """

    def __init__(
            self,
            thermal_zone):
        """Constructor of DataClass

        Parameters
        ----------
        thermal_zone: instance of ThermalZone
            TEASER instance of ThermalZone
        """
        self.thermal_zone = thermal_zone
        self.weather_data = self.thermal_zone.parent.parent.weather_data
        self.building = self.thermal_zone.parent
        self.room_air_temperature = None

        #  Todo: Get heater limits from thermal_zone
        self.heater_limit = [1e10, 1e10, 1e10]
        self.cooler_limit = [-1e10, -1e10, -1e10]

        self.initial_air_temp = 295.15
        self.initial_inner_wall_temp = 295.15
        self.initial_outer_wall_temp = 295.15

        self.heater_order = np.array([1, 2, 3])
        self.cooler_order = np.array([1, 2, 3])

    def _eq_air_temp(self, h_sol, sunblind, params):
        """Calculates equal air temperature

        corresponds to function eqAirTemp from eqAirTemp

        h_sol - solar radiation per unit area
        sunblind - opening factor of sunblinds for each direction
        (0 = open to
        1 = closed)
        params - misc. constant input parameters
        ----------------------------------------
        Outputs:
        TEqAir - equivalent air temperature

        """
        #  Todo: Cleanup docstring

        timesteps = 365 * 24

        #  Todo: Where to store t_balck_sky?
        t_black_sky = np.zeros(timesteps) + 273.15
        t_dry_bulb = self.weather_data.air_temp + 273.15  # in Kelvin

        # Read parameters to improve readability in the equations
        eExt = params[
            "eExt"]  # coefficient of emission of exterior walls (outdoor)
        aExt = params[
            "aExt"]  # coefficient of absorption of exterior walls (outdoor)
        alphaRadWall = params["alpha_rad_wall"]
        alphaWallOut = params["alpha_wall_out"]
        wfWall = params["wfWall"]  # weight factors of the walls
        wfWin = params["wfWin"]  # weight factors of the windows
        wfGro = params[
            "wfGro"]  # weight factor of the ground (0 if not considered)
        TGro = params["T_Gro"]  #
        n = len(wfWall)

        # Compute equivalent long wave and short wave temperatures
        delTEqLW = (t_black_sky - t_dry_bulb) * (
            eExt * alphaRadWall / (alphaRadWall + alphaWallOut * 0.93))
        delTEqSW = h_sol * aExt / (alphaRadWall + alphaWallOut)

        # Compute equivalent window and wall temperatures
        if params["withLongwave"]:
            TEqWin = np.array(
                [t_dry_bulb + delTEqLW * (1 - sunblind[:, i]) for i in
                 range(n)]).T
            TEqWall = np.array(
                [t_dry_bulb + delTEqLW[:, i] + delTEqSW[:, i] for i in
                 range(n)]).T
        else:
            TEqWin = np.array([t_dry_bulb for i in range(n)]).T
            TEqWall = np.array([t_dry_bulb + delTEqSW[:, i] for i in range(n)]).T

        # Compute equivalent air temperature
        TEqAir = np.dot(TEqWall, wfWall) + np.dot(TEqWin, wfWin) + TGro * wfGro

        # Return result
        return TEqAir

    def _solar_radiation(self, beta=[90, 90, 90, 90, 0],
                         gamma=[-180, -90, 0, 90, 0],
                         albedo=0.2, time_zone=1,
                         altitude=0, location=(49.5, 8.5)):
        """
        Calculates solar radiation on tilted surface

        corresponds to function calc_sun_rad from weather

        Parameters
        ----------
        beta
        gamma
        albedo
        time_zone
        altitude
        location

        Returns
        -------

        """
        #  FIXME: Deal with input values (to weather / project?)
        timesteps = 365 * 24
        dt = 3600
        initial_time = 0

        #  Get weather data
        #  TODO: Check weather
        direct_rad = self.weather_data.direct_radiation
        diffuse_rad = self.weather_data.diffuse_radiation

        geometry = self.get_geometry(initial_time=initial_time,
                                     dt=dt,
                                     timesteps=timesteps,
                                     time_zone=time_zone,
                                     location=location,
                                     altitude=altitude)

        #  Extract geometry values
        (omega, delta, theta_z, airmass, gon) = geometry

        # iterate over all surfaces (given in beta/gamma)
        results = []
        for i in range(len(gamma)):
            # compute incidence angle on each surface
            theta = self.get_incidence_angle(beta=beta[i],
                                             gamma=gamma[i],
                                             phi=location[0],
                                             omega=omega,
                                             delta=delta)
            theta = theta[1]  # cos_theta is not required

            # compute radiation on tilted surface for each surface
            radiation = self.get_rad_on_tilted_surface(theta=theta,
                                                       theta_z=theta_z,
                                                       beam_rad=direct_rad,
                                                       diffuse_rad=diffuse_rad,
                                                       airmass=airmass,
                                                       extra_terr_irr=gon,
                                                       beta=beta[i],
                                                       albedo=albedo)

            results.append(radiation)

        # return radiation on each surface
        return np.array(results)

    def get_geometry(self, initial_time, dt, timesteps,
                     time_zone=1,
                     location=(50.76, 6.07), altitude=0):
        """
        This function computes hour angle, declination, zenith angle of the sun
        and solar azimuth angle for a given location and time.

        The implemented equations can be found in:
        Duffie, Beckman - Solar Engineering of Thermal Processes, 2013 (4th ed.)

        Parameters
        ----------
        initial_time : integer
            Time passed since January 1st, 00:00:00 in seconds
        dt : integer
            Time between two consecutive time steps in seconds
        timesteps : integer
            Number of investigated / requested time steps
        time_zone : integer, optional
            Shift between the location's time and GMT in hours. CET would be 1.
        location : tuple, optional
            (latitude, longitude) of the simulated system's position. Standard
            values (50.76, 6.07) represent Aachen, Germany.
        altitude : float, optional
            The locations altitude in meters

        Returns
        -------
        omega : array_like
            Hour angle. The angular displacement of the sun east or west of the
            local meridian due to rotation of the earth on its axis at 15 degrees
            per hour; morning negative, afternoon positive
        delta : array_like
            Declination. The angular position of the sun at solar noon (i.e., when
            the sun is on the local meridian) with respect to the plane of the
            equator, north positive; −23.45 <= delta <= 23.45
        theta_z : array_like
            Zenith angle. The angle between the vertical and the line to the sun,
            that is, the angle of incidence of beam radiation on a horizontal
            surface; 0 <= theta_z <= 90
        airmass
        gon
        """
        #  TODO: Add missing explanations to docstring

        # Define pi
        pi = math.pi

        # Notice:
        # All inputs and outputs are given/expected in degrees. For the
        # computation, radians are required. Angles are converted from degrees to
        # radians via np.radians(angle). The resulting radian value is noted with
        # an R-suffix. Converting radian values to degrees is done via
        # np.rad2deg(angleR).
        # This conversion can also be done by multiplying/dividing with 180°/pi

        # Split location into latitude (phi) and longitude (lambda).
        (latitude, longitude) = location

        # Create time array
        time = ((np.linspace(0, timesteps - 1, num=timesteps)) * dt
                + initial_time)

        #  Determine the day's number and standard time 
        #  (neglect daylight saving)
        number_day = time / (3600 * 24)
        standard_time = time / 3600 - np.floor(number_day) * 24

        # Equation 1.4.2, page 9
        b_param = 360 / 365.26 * number_day
        br_param = np.radians(b_param)
        #  Compute abbreviations for e_param and extraterrestrial irradiation 
        #  (gon)
        cos_b = np.cos(br_param)
        sin_b = np.sin(br_param)
        cos_b_2 = np.cos(2 * br_param)
        sin_b_2 = np.sin(2 * br_param)

        # Convert local time into solar time
        # Equation 1.5.3, page 11
        e_param = 229.2 / 60 * (0.000075 +
                                0.001868 * cos_b -
                                0.032077 * sin_b -
                                0.014615 * cos_b_2 -
                                0.040890 * sin_b_2)

        # Compute standard meridian
        # Footnote 5 of chapter 1. Can be found on page 11.
        lambda_standard = time_zone * 15

        # Compute solar time
        # Equation 1.5.2, page 11 (conversion to hours instead of minutes)
        solar_time = (standard_time + 4 * (
            longitude - lambda_standard) / 60 + e_param) - 0.5

        # Hour angle
        # The angular displacement of the sun east or west of the local meridian
        # due to rotation of the earth on its axis at 15 degrees per hour; morning
        # negative, afternoon positive
        # Confirm page 13
        omega = 360 / 24 * (solar_time - 12)
        # Ensure: -180 <= omega <= 180
        omega[omega < -180] = omega[omega < -180] + 360
        omega[omega > 180] = omega[omega > 180] - 360
        omega_r = np.radians(omega)

        # Declination
        # The angular position of the sun at solar noon (i.e., when the sun is on
        # the local meridian) with respect to the plane of the equator, north
        # positive; −23.45 <= delta <= 23.45
        # Equation 1.6.1a, page 13
        delta = 23.45 * np.sin((284 + number_day) / 365 * 2 * pi)
        delta_r = np.radians(delta)

        # Zenith angle
        # The angle between the vertical and the line to the sun, that is, the
        # angle of incidence of beam radiation on a horizontal surface;
        # 0 <= theta_z <= 90. If theta_z > 90, the sun is below the horizon.
        # Equation 1.6.5 on page 15

        # Introduce abbreviations to improve readability
        latitude_r = math.radians(latitude)
        cos_phi = math.cos(latitude_r)
        sin_phi = math.sin(latitude_r)
        cos_delta = np.cos(delta_r)
        sin_delta = np.sin(delta_r)
        cos_omega = np.cos(omega_r)
        costheta_z = np.maximum(0,
                                cos_phi * cos_delta * cos_omega + sin_delta
                                * sin_phi)
        theta_zr = np.arccos(costheta_z)
        theta_z = np.rad2deg(theta_zr)

        # Compute airmass
        # Footnote 3 on page 10
        airmass = (math.exp(-0.0001184 * altitude) /
                   (costheta_z + 0.5057 * np.power(96.08 - theta_z, -1.634)))

        # Compute extraterrestrial irradiance (gon)
        # Extraterrestrial radiation incident on the plane normal to the radiation
        # on the nth day of the year.
        # Solar constant. Page 6
        gsc = 1367  # W/m2
        # Equation 1.4.1b
        gon = gsc * (1.000110 +
                     0.034221 * cos_b +
                     0.001280 * sin_b +
                     0.000719 * cos_b_2 +
                     0.000077 * sin_b_2)

        # Return results
        return (omega, delta, theta_z, airmass, gon)

    def get_incidence_angle(self, beta, gamma, phi, omega, delta):
        """
        Compute the incidence angle on a tilted surface.

        All inputs/outputs are supposed to be in degrees!

        Parameters
        ----------
        beta : float
            Slope, the angle (in degree) between the plane of the surface in
            question and the horizontal. 0 <= beta <= 180. If beta > 90, the
            surface faces downwards.
        gamma : float
            Surface azimuth angle. The deviation of the projection on a horizontal
            plane of the normal to the surface from the local meridian, with zero
            due south, east negative, and west positive.
            -180 <= gamma <= 180
        phi : float
            Latitude. North is positive, south negative. -90 <= phi <= 90
        omega : array_like
            Hour angle. The angular displacement of the sun east or west of the
            local meridian due to rotation of the earth on its axis at 15 degrees
            per hour; morning negative, afternoon positive
        delta : array_like
            Declination. The angular position of the sun at solar noon (i.e., when
            the sun is on the local meridian) with respect to the plane of the
            equator, north positive; −23.45 <= delta <= 23.45

        Returns
        -------
        cos_theta
        theta
        """
        #  Todo: Add missing explanations to docstring

        # Compute incidence angle of beam radiation
        # Transform to radian
        beta_r = math.radians(beta)
        phi_r = math.radians(phi)
        gamma_r = math.radians(gamma)
        delta_r = np.radians(delta)
        omega_r = np.radians(omega)

        # Introduce required abbreviations
        sin_beta = math.sin(beta_r)
        cos_beta = math.cos(beta_r)
        sin_delta = np.sin(delta_r)
        cos_delta = np.cos(delta_r)
        sin_phi = math.sin(phi_r)
        cos_phi = math.cos(phi_r)
        sin_gamma = math.sin(gamma_r)
        cos_gamma = math.cos(gamma_r)
        sin_omega = np.sin(omega_r)
        cos_omega = np.cos(omega_r)

        # Equation 1.6.2, page 14
        cos_theta = np.maximum(sin_delta * sin_phi * cos_beta -
                               sin_delta * cos_phi * sin_beta * cos_gamma +
                               cos_delta * cos_phi * cos_beta * cos_omega +
                               cos_delta * sin_phi * sin_beta * cos_gamma *
                               cos_omega +
                               cos_delta * sin_beta * sin_gamma * sin_omega, 0)
        theta_r = np.arccos(cos_theta)
        theta = np.rad2deg(theta_r)

        # Return incidence angle
        return (cos_theta, theta)

    def get_rad_on_tilted_surface(self, theta, theta_z,
                                  beam_rad, diffuse_rad,
                                  airmass, extra_terr_irr,
                                  beta, albedo):
        """
        Compute the total radiation on a tilted surface.

        Parameters
        ----------
        theta : array_like
            Incidence angle.
        theta_z : array_like
            Zenith angle. The angle between the vertical and the line to the sun,
            that is, the angle of incidence of beam radiation on a horizontal
            surface; 0 <= theta_z <= 90
        beam_rad : array_like
            The solar radiation received from the sun without having been
            scattered by the atmosphere (also often named direct radiation)
        diffuse_rad : array_like
            The solar radiation received from the sun after its direction has been
            changed by scattering by the atmosphere.
        airmass : array_like
            The ratio of the mass of atmosphere through which beam radiation
            passes to the mass it would pass through if the sun were at the zenith.
            Thus at sea level ``m=1`` when the sun is at the zenith and ``m=2``
            for a zenith angle ``theta_z=60`` degrees.
        extra_terr_irr : array_like
            Extraterrestrial radiation incident on the plane normal to the
            radiation on the nth day of the year.
        beta : float
            Slope, the angle (in degree) between the plane of the surface in
            question and the horizontal. 0 <= beta <= 180. If beta > 90, the
            surface faces downwards.
        albedo : float
            Ground reflectance. 0 <= albedo <= 1
        """
        # Model coefficients
        # Table 6, in Perez et al - 1990 - Modeling daylight availability and
        # irradiance components from direct and global irradiance.
        # Solar Energy, Vol. 44, No. 5, pp. 271-289
        # Values with increased accuracy can be found in the EnergyPlus
        # engineering reference (Table 22, Fij Factors as a Function of Sky
        # Clearness Range, page 147)

        f_coeff = np.array(
            [[-0.0083117, 0.5877285, -0.0620636, -0.0596012, 0.0721249,
              -0.0220216],
             [0.1299457, 0.6825954, -0.1513752, -0.0189325, 0.065965,
              -0.0288748],
             [0.3296958, 0.4868735, -0.2210958, 0.055414, -0.0639588,
              -0.0260542],
             [0.5682053, 0.1874525, -0.295129, 0.1088631, -0.1519229,
              -0.0139754],
             [0.873028, -0.3920403, -0.3616149, 0.2255647, -0.4620442,
              0.0012448],
             [1.1326077, -1.2367284, -0.4118494, 0.2877813, -0.8230357,
              0.0558651],
             [1.0601591, -1.5999137, -0.3589221, 0.2642124, -1.127234,
              0.1310694],
             [0.677747, -0.3272588, -0.2504286, 0.1561313, -1.3765031,
              0.2506212]
             ])

        # Compute a and b (page 281, below equation 9)
        theta_r = np.radians(theta)
        theta_zr = np.radians(theta_z)
        costheta_z = np.cos(theta_zr)
        cos_theta = np.cos(theta_r)
        a = np.maximum(0, cos_theta)
        b = np.maximum(0.087, costheta_z)

        # Compute epsilon (the sky's clearness)
        # Introduce variables and compute third power of theta_zr
        kappa = 1.041
        theta_zrto3 = np.power(theta_zr, 3)

        # Compute normal incidence direct irradiance
        irr = beam_rad / b
        # Prevent division by zero
        temp = np.zeros_like(theta)  # All inputs should have this length!
        temp[diffuse_rad > 0] = (1.0 * irr[diffuse_rad > 0] /
                                 diffuse_rad[diffuse_rad > 0])
        # equation 1 on p. 273 in Perez et al - 1990
        epsilon = (1 + temp + kappa * theta_zrto3) / (1 + kappa * theta_zrto3)

        # Determine clear sky category
        # table 1 on page 273 in Perez et al - 1990
        # Note: As this value is used to get data from f_coeff, the
        # implemented categories range from 0 to 7 instead from 1 to 8
        eps_category = np.zeros_like(epsilon, dtype=int)
        eps_category[(epsilon >= 1.065) & (epsilon < 1.23)] = 1
        eps_category[(epsilon >= 1.230) & (epsilon < 1.50)] = 2
        eps_category[(epsilon >= 1.500) & (epsilon < 1.95)] = 3
        eps_category[(epsilon >= 1.950) & (epsilon < 2.80)] = 4
        eps_category[(epsilon >= 2.800) & (epsilon < 4.50)] = 5
        eps_category[(epsilon >= 4.500) & (epsilon < 6.20)] = 6
        eps_category[epsilon >= 6.200] = 7

        # Compute delta (the sky's brightness)
        # equation 2 on page 273 in Perez et al - 1990
        delta = diffuse_rad * airmass / extra_terr_irr

        # Compute f1_par (circumsolar brightening coefficient) and f2_par (horizon
        # brightening coefficient)
        # Below table 6 on page 282 in Perez et al - 1990
        # According to Duffie and Beckman (4th edition, page 94, equation 2.16.12),
        # f1_par is supposed to be greater or equal to 0
        f1_par = np.maximum(f_coeff[eps_category, 0] +
                            f_coeff[eps_category, 1] * delta +
                            f_coeff[eps_category, 2] * theta_zr,
                            0)

        f2_par = (f_coeff[eps_category, 3] +
                  f_coeff[eps_category, 4] * delta +
                  f_coeff[eps_category, 5] * theta_zr)

        # Compute diffuse radiation on tilted surface
        # Equation 9 on page 281 in Perez et al - 1990
        beta_r = math.radians(beta)
        cos_beta = math.cos(beta_r)
        sin_beta = math.sin(beta_r)
        diff_rad_tilt_surface = diffuse_rad * (
            (1 - f1_par) * (1 + cos_beta) / 2 +
            f1_par * a / b + f2_par * sin_beta)

        # Compute the influence of beam radiation and reflected radiation
        # Equation 2.15.1 in Duffie and Beckman (4th edition, page 89)
        # Compute direct radiation on tilted surface
        # Equation 1.8.1 in Duffie and Beckman (4th edition, page 24)
        # We divide by b instead of costheta_z to prevent division by 0
        # Direct radiation on a tilted surface is always positive, therefore use
        # ``a`` instead of cos_theta
        dir_rad_tilt_surface = beam_rad * a / b

        # Compute reflected total radiation
        # Equation 2.15.1 in Duffie and Beckman (4th edition, page 89)
        # Notice: We changed the proposed nomenclature. rhoG is written as albedo.
        # Total solar radiation is computed as sum of beam and diffuse radiation.
        # See page 10 in Duffie and Beckman (4th edition)
        total_sol_rad = beam_rad + diffuse_rad
        refl_rad_tilt_surface = total_sol_rad * albedo * (1 - cos_beta) / 2

        total_rad_tilt_surface = (diff_rad_tilt_surface +
                                  dir_rad_tilt_surface +
                                  refl_rad_tilt_surface)

        # Return total radiation on a tilted surface
        return total_rad_tilt_surface

    def simulate(self):
        """Simulates VDI 6007 with hourly timestep for given thermal_zone

        corresponds to function: calc_reduced_order_model from
        simulation_vdi_6007 """

        #  Fix number of timesteps
        timesteps = 365 * 24
        dt = 3600

        #  Get building parameters
        r1_iw = self.thermal_zone.model_attr.r1_iw
        c1_iw = self.thermal_zone.model_attr.c1_iw
        area_iw = self.thermal_zone.model_attr.area_iw
        r_rest_ow = self.thermal_zone.model_attr.r_rest_ow
        r1_ow = self.thermal_zone.model_attr.r1_ow
        c1_ow = self.thermal_zone.model_attr.c1_ow
        area_ow = [self.thermal_zone.model_attr.area_ow]
        window_areas = self.thermal_zone.model_attr.window_areas
        transparent_areas = self.thermal_zone.model_attr.transparent_areas
        volume = self.thermal_zone.volume
        density_air = self.thermal_zone.density_air
        heat_capac_air = self.thermal_zone.heat_capac_air
        ratio_conv_rad_inner_win = \
            self.thermal_zone.model_attr.ratio_conv_rad_inner_win
        weighted_g_value = self.thermal_zone.model_attr.weighted_g_value
        alpha_comb_inner_iw = self.thermal_zone.model_attr.alpha_comb_inner_iw
        alpha_comb_inner_ow = self.thermal_zone.model_attr.alpha_comb_inner_ow
        alpha_wall = self.thermal_zone.model_attr.alpha_comb_outer_ow * \
                     self.thermal_zone.model_attr.area_ow

        area_win_tot = sum(window_areas)
        area_o_tot = sum(area_ow)
        area_ar = [area_o_tot, area_win_tot, area_iw]

        r_rest_ow = r_rest_ow + 1 / alpha_wall

        #  Get weather temperature of weather in Kelvin
        air_temp = self.weather_data.air_temp

        #  Get weather direct_radiation
        direct_radiation = self.weather_data.direct_radiation
        diffuse_ratiation = self.weather_data.diffuse_radiation

        #  Calculate solar_rad_in with weather
        #  Todo: Set further inputs for _solar_radiation()?
        solar_rad_in = np.transpose(self._solar_radiation())

        # Max. irradiation
        #  Todo: Where to store max irradiation value?
        i_max = 100

        list_window_areas = []
        list_sunblind = []
        for window in self.thermal_zone.windows:
            list_window_areas.append(window.area)
            list_sunblind.append(0.0)

        sunblind_in = np.zeros_like(solar_rad_in)
        sunblind_in[solar_rad_in > i_max] = 0.85

        #  Calculate equal_air_temp
        equal_air_temp = self._eq_air_temp(h_sol=solar_rad_in,
                                           t_black_sky=t_black_sky,
                                           sunblind=sunblind_in,
                                           params)
        #  Todo: Replace params input with single thermal zone inputs

        e_solar_conv = np.zeros((timesteps, len(transparent_areas)))

        for i in range(len(transparent_areas)):
            e_solar_conv[:, i] = solar_rad_in[:, i] * \
                                 ratio_conv_rad_inner_win * weighted_g_value * \
                                 transparent_areas[i]
        q_solar_conv = np.sum(e_solar_conv, axis=1)

        # splitters:
        # on each splitter: one output goes to outer wall, one goes to inner
        # wall therefore dimension is 2 if inner walls exist => 2 outgoing
        # signals
        split_fac_solar = self.calc_splitfactors(
            len(area_ow), area_ar, area_ow, window_areas)

        # therm. splitter solar radiative:
        e_solar_rad = np.zeros((timesteps, len(transparent_areas)))
        for i in range(len(transparent_areas)):
            e_solar_rad[:, i] = solar_rad_in[:, i] * (
                ratio_conv_rad_inner_win - 1) * weighted_g_value * \
                                transparent_areas[i]
        q_solar_rad = np.zeros((
            timesteps,
            len(area_ow),
            split_fac_solar.shape[0]))
        for i in range(len(area_ow)):
            for j in range(split_fac_solar.shape[0]):
                q_solar_rad[:, i, j] = -e_solar_rad[:, i] * split_fac_solar[
                    j, i]

        q_solarRadToInnerWall = np.sum(q_solar_rad[:, :, 1], axis=1)
        q_solarRadToOuterWalli = np.sum(q_solar_rad[:, :, 0], axis=1)

        # Results' initialization
        t_ow = []
        t_owi = []
        t_iw = []
        t_iwi = []
        t_air = []
        q_air = []
        q_air_hc = []
        q_iw_hc = []
        q_ow_hc = []

        # Initial temperatures
        t_ow_prev = self.initial_outer_wall_temp
        t_iw_prev = self.initial_inner_wall_temp
        t_air_prev = self.initial_air_temp

        for t in range(timesteps):
            # Common equations
            A = np.zeros((9, 9))
            rhs = np.zeros(A.shape[0])

            # Fill matrix coefficients
            A[0, 0] = c1_ow / dt + 1 / r_rest_ow + 1 / r1_ow
            A[0, 1] = -1 / r1_ow
            A[1, 0] = 1 / r1_ow
            A[1, 1] = - min(area_o_tot, area_iw) * alphaRad[t] - area_o_tot * \
                                                             alpha_comb_inner_ow - 1 / r1_ow
            A[1, 3] = min(area_o_tot, area_iw) * alphaRad[t]
            A[1, 4] = area_o_tot * alpha_comb_inner_ow
            A[1, 8] = 1
            A[2, 2] = c1_iw / dt + 1 / r1_iw
            A[2, 3] = -1 / r1_iw
            A[3, 1] = min(area_o_tot, area_iw) * alphaRad[t]
            A[3, 2] = 1 / r1_iw
            A[3, 3] = -min(area_o_tot, area_iw) * alphaRad[t] - area_iw * \
                                                            alpha_comb_inner_iw - 1 / r1_iw
            A[3, 4] = area_iw * alpha_comb_inner_iw
            A[3, 7] = 1
            A[4, 1] = area_o_tot * alpha_comb_inner_ow
            A[4, 3] = area_iw * alpha_comb_inner_iw
            A[4, 4] = -area_o_tot * alpha_comb_inner_ow - area_iw * \
                                                      alpha_comb_inner_iw - \
                      ventRate[t] * heat_capac_air * \
                      density_air
            A[4, 5] = -1
            A[4, 6] = 1
            A[5, 4] = volume * heat_capac_air * density_air / dt
            A[5, 5] = -1

            # Fill right hand side
            rhs[0] = equalAirTemp[t] / r_rest_ow + c1_ow * t_ow_prev / dt
            rhs[1] = -q_solarRadToOuterWalli[t] - Q_loadsToOuterWalli[t]
            rhs[2] = c1_iw * t_iw_prev / dt
            rhs[3] = -q_solarRadToInnerWall[t] - Q_loadsToInnerWall[t]
            rhs[4] = -ventRate[t] * heat_capac_air * density_air * \
                     weatherTemperature[t] - q_solar_conv[t] - Q_ig[t]
            rhs[5] = density_air * heat_capac_air * volume * t_air_prev / dt

            # Calculate current time step
            x = self.calc_timestep(
                A,
                rhs,
                t_set_heating[t],
                t_set_cooling[t],
                heater_limit[t, :],
                cooler_limit[t, :],
                heater_order,
                cooler_order)

            # Retrieve results
            t_ow.append(x[0])
            t_owi.append(x[1])
            t_iw.append(x[2])
            t_iwi.append(x[3])
            t_air.append(x[4])
            q_air.append(x[5])
            q_air_hc.append(x[6])
            q_iw_hc.append(x[7])
            q_ow_hc.append(x[8])

            # Update initial temperatures
            t_ow_prev = x[0]
            t_iw_prev = x[2]
            t_air_prev = x[4]

            self.indoor_air_temperature = np.array(t_air)
            self.q_flow_heater_cooler = np.array(q_air_hc)

        return (np.array(t_air), np.array(q_air_hc))

    def calc_splitfactors(cols, a_array, a_ext, a_win):
        """
        This function calculates the split factors

        Parameters
        ----------
        cols : int
            Number of orientations
        a_array : list
            [ATotExt, ATotWin]
        a_ext : list
            Vector of exterior wall areas
        a_win : list
            Vector of window areas

        Example
        -------
        >>> # Define areas
        >>> a_ext = [10.5]
        >>> a_win = [0]
        >>> A_int = 75.5
        >>> area_ar = [sum(a_ext), sum(a_win), A_int]
        >>> # Calculate split factors for inner walls and outside walls
        >>> splitFac_IW = _calc_splitfactors(dim, 1, area_ar, [0], [0])
        >>> splitFac_OW = _calc_splitfactors(dim, len(a_ext), area_ar, a_ext,
        a_win)
        """

        a_tot = sum(a_array)  # total area

        rows = sum([1 if a > 0 else 0 for a in a_array])
        rows = len(a_array)

        # Counters
        i = 0  # a_array
        j = 0  # Row
        k = 0  # Column

        result = np.zeros((rows, cols))

        for a in a_array:
            if a > 0:
                k = 0
                if i == 0:
                    for a_wall in a_ext:
                        result[j, k] = (a - a_wall) / (
                            a_tot - a_wall - a_win[k])
                        k += 1
                elif i == 1:
                    for a_wall in a_ext:
                        result[j, k] = (a - a_win[k]) / (
                            a_tot - a_wall - a_win[k])
                        k += 1
                else:
                    for a_wall in a_ext:
                        result[j, k] = a / (a_tot - a_wall - a_win[k])
                        k += 1
                j += 1
            i += 1

        return result

    def calc_timestep(
            A,
            rhs,
            t_set_heating=291.15,
            t_set_cooling=300.15,
            heater_order=np.array([1, 2, 3]),
            cooler_order=np.array([1, 2, 3])):

        """
        Calculate the temperatures and heat flow rate for the current time step

        Parameters
        ----------
        A : 2d array of floats
            Coefficients describing the VDI model
        rhs : Array of floats
            Right hand side of these equations
        t_set_heating : Float (Move to Init?)
            Temperature below which heating demand is computed (in Kelvin)
        t_set_cooling : Float (Move to Init?)
            Temperature above which cooling demand is computed (in Kelvin)
        """
        # Calculate without further heat inputs to determine if heating
        # or cooling is needed
        # x = [T_ow, T_owi, T_iw, T_iwi, T_air, Q_air, Q_HC]
        x_noHeat = _calc_temperatue(
            A, rhs, q_air_fix=0, q_iw_fix=0, q_ow_fix=0)

        if x_noHeat[4] < t_set_heating:
            # Indoor air temperature below heating set temperature

            # Use primary heater
            if np.argmax(heater_order == 1) == 0 and heater_limit[0] > 0:
                x_heating_1 = _calc_heatflow(
                    A,
                    rhs,
                    t_air_set=t_set_heating,
                    q_air_fix=None,
                    q_iw_fix=0,
                    q_ow_fix=0)

                if x_heating_1[6] > heater_limit[0]:
                    x_maxheat_1 = _calc_temperatue(
                        A,
                        rhs,
                        q_air_fix=heater_limit[0],
                        q_iw_fix=0,
                        q_ow_fix=0)

                    if x_maxheat_1[4] < t_set_heating:
                        if np.argmax(heater_order == 2) == 1 and \
                                        heater_limit[1] > 0:
                            x_heating_2 = _calc_heatflow(
                                A, rhs,
                                t_air_set=t_set_heating,
                                q_air_fix=heater_limit[0],
                                q_iw_fix=None, q_ow_fix=0)

                            if x_heating_2[7] > heater_limit[1]:
                                x_maxheat_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=heater_limit[0],
                                    q_iw_fix=heater_limit[1],
                                    q_ow_fix=0)

                                if x_maxheat_2[4] < t_set_heating and \
                                                heater_limit[2] > 0:
                                    x_heating_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_heating,
                                        q_air_fix=heater_limit[0],
                                        q_iw_fix=heater_limit[1],
                                        q_ow_fix=None)

                                    if x_heating_3[8] > heater_limit[2]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=heater_limit[0],
                                            q_iw_fix=heater_limit[1],
                                            q_ow_fix=heater_limit[2])
                                    else:
                                        return x_heating_3
                                else:
                                    return x_maxheat_2
                            else:
                                return x_heating_2
                        elif np.argmax(heater_order == 2) == 2 and \
                                        heater_limit[2] > 0:
                            x_heating_2 = _calc_heatflow(
                                A,
                                rhs,
                                t_air_set=t_set_heating,
                                q_air_fix=heater_limit[0],
                                q_iw_fix=0, q_ow_fix=None)

                            if x_heating_2[8] > heater_limit[2]:
                                x_maxheat_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=heater_limit[0],
                                    q_iw_fix=0,
                                    q_ow_fix=heater_limit[2])

                                if x_maxheat_2[4] < t_set_heating and \
                                                heater_limit[1] > 0:
                                    x_heating_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_heating,
                                        q_air_fix=heater_limit[0],
                                        q_iw_fix=None,
                                        q_ow_fix=heater_limit[2])

                                    if x_heating_3[7] > heater_limit[1]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=heater_limit[0],
                                            q_iw_fix=heater_limit[1],
                                            q_ow_fix=heater_limit[2])
                                    else:
                                        return x_heating_3
                                else:
                                    return x_maxheat_2
                            else:
                                return x_heating_2
                        else:
                            return x_maxheat_1
                else:
                    return x_heating_1
            elif np.argmax(heater_order == 1) == 1 and heater_limit[1] > 0:
                x_heating_1 = _calc_heatflow(
                    A,
                    rhs,
                    t_air_set=t_set_heating,
                    q_air_fix=0,
                    q_iw_fix=None,
                    q_ow_fix=0)

                if x_heating_1[7] > heater_limit[1]:
                    x_maxheat_1 = _calc_temperatue(
                        A,
                        rhs,
                        q_air_fix=0,
                        q_iw_fix=heater_limit[1],
                        q_ow_fix=0)

                    if x_maxheat_1[4] < t_set_heating:
                        if np.argmax(heater_order == 2) == 0 and \
                                        heater_limit[0] > 0:
                            x_heating_2 = _calc_heatflow(
                                A,
                                rhs,
                                t_air_set=t_set_heating,
                                q_air_fix=None,
                                q_iw_fix=heater_limit[1],
                                q_ow_fix=0)

                            if x_heating_2[6] > heater_limit[0]:
                                x_maxheat_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=heater_limit[0],
                                    q_iw_fix=heater_limit[1],
                                    q_ow_fix=0)

                                if x_maxheat_2[4] < t_set_heating and \
                                                heater_limit[2] > 0:
                                    x_heating_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_heating,
                                        q_air_fix=heater_limit[0],
                                        q_iw_fix=heater_limit[1],
                                        q_ow_fix=None)

                                    if x_heating_3[8] > heater_limit[2]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=heater_limit[0],
                                            q_iw_fix=heater_limit[1],
                                            q_ow_fix=heater_limit[2])
                                    else:
                                        return x_heating_3
                                else:
                                    return x_maxheat_2
                            else:
                                return x_heating_2
                        elif np.argmax(heater_order == 2) == 2 and \
                                        heater_limit[2] > 0:
                            x_heating_2 = _calc_heatflow(
                                A,
                                rhs,
                                t_air_set=t_set_heating,
                                q_air_fix=0,
                                q_iw_fix=heater_limit[1],
                                q_ow_fix=None)

                            if x_heating_2[8] > heater_limit[2]:
                                x_maxheat_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=0,
                                    q_iw_fix=heater_limit[1],
                                    q_ow_fix=heater_limit[2])

                                if x_maxheat_2[4] < t_set_heating and \
                                                heater_limit[0] > 0:
                                    x_heating_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_heating,
                                        q_air_fix=None,
                                        q_iw_fix=heater_limit[1],
                                        q_ow_fix=heater_limit[2])

                                    if x_heating_3[6] > heater_limit[0]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=heater_limit[0],
                                            q_iw_fix=heater_limit[1],
                                            q_ow_fix=heater_limit[2])
                                    else:
                                        return x_heating_3
                                else:
                                    return x_maxheat_2
                            else:
                                return x_heating_2
                        else:
                            return x_maxheat_1
                else:
                    return x_heating_1
            elif np.argmax(heater_order == 1) == 2 and \
                            heater_limit[2] > 0:  # no else
                x_heating_1 = _calc_heatflow(
                    A,
                    rhs,
                    t_air_set=t_set_heating,
                    q_air_fix=0,
                    q_iw_fix=0,
                    q_ow_fix=None)

                if x_heating_1[8] > heater_limit[2]:
                    x_maxheat_1 = _calc_temperatue(
                        A,
                        rhs,
                        q_air_fix=0,
                        q_iw_fix=0,
                        q_ow_fix=heater_limit[2])

                    if x_maxheat_1[4] < t_set_heating:
                        if np.argmax(heater_order == 2) == 0 and \
                                        heater_limit[0] > 0:
                            x_heating_2 = _calc_heatflow(
                                A,
                                rhs,
                                t_air_set=t_set_heating,
                                q_air_fix=None,
                                q_iw_fix=0,
                                q_ow_fix=heater_limit[2])

                            if x_heating_2[6] > heater_limit[0]:
                                x_maxheat_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=heater_limit[0],
                                    q_iw_fix=0,
                                    q_ow_fix=heater_limit[1])

                                if x_maxheat_2[4] < t_set_heating and \
                                                heater_limit[1] > 0:
                                    x_heating_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_heating,
                                        q_air_fix=heater_limit[0],
                                        q_iw_fix=None,
                                        q_ow_fix=heater_limit[2])

                                    if x_heating_3[7] > heater_limit[1]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=heater_limit[0],
                                            q_iw_fix=heater_limit[1],
                                            q_ow_fix=heater_limit[2])
                                    else:
                                        return x_heating_3
                                else:
                                    return x_maxheat_2
                            else:
                                return x_heating_2
                        elif np.argmax(heater_order == 2) == 1 and \
                                        heater_limit[1] > 0:
                            x_heating_2 = _calc_heatflow(
                                A,
                                rhs,
                                t_air_set=t_set_heating,
                                q_air_fix=0,
                                q_iw_fix=None,
                                q_ow_fix=heater_limit[2])

                            if x_heating_2[7] > heater_limit[1]:
                                x_maxheat_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=0,
                                    q_iw_fix=heater_limit[1],
                                    q_ow_fix=heater_limit[2])

                                if x_maxheat_2[4] < t_set_heating and \
                                                heater_limit[0] > 0:
                                    x_heating_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_heating,
                                        q_air_fix=None,
                                        q_iw_fix=heater_limit[1],
                                        q_ow_fix=heater_limit[2])

                                    if x_heating_3[6] > heater_limit[0]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=heater_limit[0],
                                            q_iw_fix=heater_limit[1],
                                            q_ow_fix=heater_limit[2])
                                    else:
                                        return x_heating_3
                                else:
                                    return x_maxheat_2
                            else:
                                return x_heating_2
                        else:
                            return x_maxheat_1
                else:
                    return x_heating_1

        elif x_noHeat[4] > t_set_cooling:
            # Indoor air temperature above cooling set temperature

            if np.argmax(cooler_order == 1) == 0 and cooler_limit[0] < 0:
                x_cooling_1 = _calc_heatflow(
                    A,
                    rhs,
                    t_air_set=t_set_cooling,
                    q_air_fix=None,
                    q_iw_fix=0,
                    q_ow_fix=0)

                if x_cooling_1[6] < cooler_limit[0]:
                    x_maxcool_1 = _calc_temperatue(
                        A,
                        rhs,
                        q_air_fix=cooler_limit[0],
                        q_iw_fix=0,
                        q_ow_fix=0)

                    if x_maxcool_1[4] > t_set_cooling:
                        if np.argmax(cooler_order == 2) == 1 and \
                                        cooler_limit[1] < 0:
                            x_cooling_2 = _calc_heatflow(
                                A,
                                rhs,
                                t_air_set=t_set_cooling,
                                q_air_fix=cooler_limit[0],
                                q_iw_fix=None,
                                q_ow_fix=0)

                            if x_cooling_2[7] < cooler_limit[1]:
                                x_maxcool_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=cooler_limit[0],
                                    q_iw_fix=cooler_limit[1],
                                    q_ow_fix=0)

                                if x_maxcool_2[4] > t_set_cooling and \
                                                cooler_limit[2] < 0:
                                    x_cooling_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_cooling,
                                        q_air_fix=cooler_limit[0],
                                        q_iw_fix=cooler_limit[1],
                                        q_ow_fix=None)

                                    if x_cooling_3[8] < cooler_limit[2]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=cooler_limit[0],
                                            q_iw_fix=cooler_limit[1],
                                            q_ow_fix=cooler_limit[2])
                                    else:
                                        return x_cooling_3
                                else:
                                    return x_maxcool_2
                            else:
                                return x_cooling_2
                        elif np.argmax(cooler_order == 2) == 2 and \
                                        cooler_limit[2] < 0:
                            x_cooling_2 = _calc_heatflow(
                                A,
                                rhs,
                                t_air_set=t_set_cooling,
                                q_air_fix=cooler_limit[0],
                                q_iw_fix=0,
                                q_ow_fix=None)

                            if x_cooling_2[8] < cooler_limit[2]:
                                x_maxcool_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=cooler_limit[0],
                                    q_iw_fix=0,
                                    q_ow_fix=cooler_limit[2])

                                if x_maxcool_2[4] > t_set_cooling and \
                                                cooler_limit[1] < 0:
                                    x_cooling_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_cooling,
                                        q_air_fix=cooler_limit[0],
                                        q_iw_fix=None,
                                        q_ow_fix=cooler_limit[2])

                                    if x_cooling_3[7] < cooler_limit[1]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=cooler_limit[0],
                                            q_iw_fix=cooler_limit[1],
                                            q_ow_fix=cooler_limit[2])
                                    else:
                                        return x_cooling_3
                                else:
                                    return x_maxcool_2
                            else:
                                return x_cooling_2
                        else:
                            return x_maxcool_1
                else:
                    return x_cooling_1

            elif np.argmax(cooler_order == 1) == 1 and cooler_limit[1] < 0:
                x_cooling_1 = _calc_heatflow(
                    A,
                    rhs,
                    t_air_set=t_set_cooling,
                    q_air_fix=0,
                    q_iw_fix=None,
                    q_ow_fix=0)

                if x_cooling_1[7] < cooler_limit[1]:
                    x_maxcool_1 = _calc_temperatue(
                        A,
                        rhs,
                        q_air_fix=0,
                        q_iw_fix=cooler_limit[1],
                        q_ow_fix=0)

                    if x_maxcool_1[4] > t_set_cooling:
                        if np.argmax(cooler_order == 2) == 0 and \
                                        cooler_limit[0] < 0:
                            x_cooling_2 = _calc_heatflow(
                                A,
                                rhs,
                                t_air_set=t_set_cooling,
                                q_air_fix=None,
                                q_iw_fix=cooler_limit[1],
                                q_ow_fix=0)

                            if x_cooling_2[6] < cooler_limit[0]:
                                x_maxcool_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=cooler_limit[0],
                                    q_iw_fix=cooler_limit[1],
                                    q_ow_fix=0)

                                if x_maxcool_2[4] > t_set_cooling and \
                                                cooler_limit[2] < 0:
                                    x_cooling_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_cooling,
                                        q_air_fix=cooler_limit[0],
                                        q_iw_fix=cooler_limit[1],
                                        q_ow_fix=None)

                                    if x_cooling_3[8] < cooler_limit[2]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=cooler_limit[0],
                                            q_iw_fix=cooler_limit[1],
                                            q_ow_fix=cooler_limit[2])
                                    else:
                                        return x_cooling_3
                                else:
                                    return x_maxcool_2
                            else:
                                return x_cooling_2
                        elif np.argmax(cooler_order == 2) == 2 and \
                                        cooler_limit[2] < 0:
                            x_cooling_2 = _calc_heatflow(
                                A,
                                rhs,
                                t_air_set=t_set_cooling,
                                q_air_fix=0,
                                q_iw_fix=cooler_limit[1],
                                q_ow_fix=None)

                            if x_cooling_2[8] < cooler_limit[2]:
                                x_maxcool_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=0,
                                    q_iw_fix=cooler_limit[1],
                                    q_ow_fix=cooler_limit[2])

                                if x_maxcool_2[4] > t_set_cooling and \
                                                cooler_limit[0] < 0:
                                    x_cooling_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_cooling,
                                        q_air_fix=None,
                                        q_iw_fix=cooler_limit[1],
                                        q_ow_fix=cooler_limit[2])

                                    if x_cooling_3[6] < cooler_limit[0]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=cooler_limit[0],
                                            q_iw_fix=cooler_limit[1],
                                            q_ow_fix=cooler_limit[2])
                                    else:
                                        return x_cooling_3
                                else:
                                    return x_maxcool_2
                            else:
                                return x_cooling_2
                        else:
                            return x_maxcool_1
                else:
                    return x_cooling_1

            elif np.argmax(cooler_order == 1) == 2 and cooler_limit[2] < 0:
                x_cooling_1 = _calc_heatflow(
                    A,
                    rhs,
                    t_air_set=t_set_cooling,
                    q_air_fix=0,
                    q_iw_fix=0,
                    q_ow_fix=None)
                if x_cooling_1[8] < cooler_limit[2]:
                    x_maxcool_1 = _calc_temperatue(
                        A,
                        rhs,
                        q_air_fix=0,
                        q_iw_fix=0,
                        q_ow_fix=cooler_limit[2])

                    if x_maxcool_1[4] > t_set_cooling:
                        if np.argmax(cooler_order == 2) == 0 and \
                                        cooler_limit[0] < 0:
                            x_cooling_2 = _calc_heatflow(
                                A,
                                rhs,
                                t_air_set=t_set_cooling,
                                q_air_fix=None,
                                q_iw_fix=0,
                                q_ow_fix=cooler_limit[2])

                            if x_cooling_2[6] < cooler_limit[0]:
                                x_maxcool_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=cooler_limit[0],
                                    q_iw_fix=0,
                                    q_ow_fix=cooler_limit[2])

                                if x_maxcool_2[4] > t_set_cooling and \
                                                cooler_limit[1] < 0:
                                    x_cooling_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_cooling,
                                        q_air_fix=cooler_limit[0],
                                        q_iw_fix=None,
                                        q_ow_fix=cooler_limit[2])

                                    if x_cooling_3[7] < cooler_limit[1]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=cooler_limit[0],
                                            q_iw_fix=cooler_limit[1],
                                            q_ow_fix=cooler_limit[2])
                                    else:
                                        return x_cooling_3
                                else:
                                    return x_maxcool_2
                            else:
                                return x_cooling_2
                        elif np.argmax(cooler_order == 2) == 1 and \
                                        cooler_limit[1] < 0:
                            x_cooling_2 = _calc_heatflow(
                                A,
                                rhs,
                                t_air_set=t_set_cooling,
                                q_air_fix=0,
                                q_iw_fix=None,
                                q_ow_fix=cooler_limit[2])

                            if x_cooling_2[7] < cooler_limit[1]:
                                x_maxcool_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=0,
                                    q_iw_fix=cooler_limit[1],
                                    q_ow_fix=cooler_limit[2])

                                if x_maxcool_2[4] > t_set_cooling and \
                                                cooler_limit[0] < 0:
                                    x_cooling_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_cooling,
                                        q_air_fix=None,
                                        q_iw_fix=cooler_limit[1],
                                        q_ow_fix=cooler_limit[2])

                                    if x_cooling_3[6] < cooler_limit[0]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=cooler_limit[0],
                                            q_iw_fix=cooler_limit[1],
                                            q_ow_fix=cooler_limit[2])
                                    else:
                                        return x_cooling_3
                                else:
                                    return x_maxcool_2
                            else:
                                return x_cooling_2
                        else:
                            return x_maxcool_1
                else:
                    return x_cooling_1
        else:
            # Indoor air temperature between both set temperature -> no further
            # action required
            return x_noHeat
