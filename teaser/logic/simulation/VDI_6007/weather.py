#!/usr/bin/env python
# coding=utf-8
"""
TEASER weather class for VDI 6007 calculation
"""

import os
import numpy as np
import math

class Weather(object):
    """Computes weather data like solar radiation

    Weather class of TEASER

    Attributes
    ----------
    time_zone : int
        Shift between the location's time and GMT in hours. CET would be 1.
    timestep : int [s]
        duration of one timestep in sec. default is 3600
    nb_timesteps : int
        The number of calculated timestep, default is 8760
    omega : array_like
        Hour angle. The angular displacement of the sun east or west of the
        local meridian due to rotation of the earth on its axis at 15 degrees
        per hour; morning negative, afternoon positive
    delta : array_like
        Declination. The angular position of the sun at solar noon (i.e., when
        the sun is on the local meridian) with respect to the plane of the
        equator, north positive; −23.45 <= delta <= 23.45
    thetaZ : array_like
        Zenith angle. The angle between the vertical and the line to the sun,
        that is, the angle of incidence of beam radiation on a horizontal
        surface; 0 <= thetaZ <= 90
    albedo : float
        Ground reflectance. 0 <= albedo <= 1
    g_on : array like
        extraterrestrial irradiance
    airmass : array like
        airmass


    """

    def __init__(self, thermal_zone):
        """
        Constructor of weather object
        """
        self.thermal_zone = thermal_zone
        self.timestep = 3600
        self.nb_timesteps = 365 * 24 * 3600 / self.timestep
        self.time_zone = 1
        self.albedo = 0.2
        self.g_on = None
        self.omega = None
        self.airmass = None
        self.delta = None
        self.theta_z = None
        self.rad_on_tilted_surfaces = []

    def get_solar_gains(self):
        """computes solar gains on tilted surfaces"""

        self.get_sun_geometry(initial_time=0, time_discretization=self.timestep)

        gamma = self._convert_orientation(orientation_teaser=
            self.thermal_zone.model_attr.orientation_facade)

        for i in range(len(gamma)):
            # compute incidence angle on each surface
            theta = self._get_incidence_angle(
                self.thermal_zone.model_attr.tilt_facade[i],
                gamma[i],
                self.thermal_zone.parent.longitude,
                self.omega,
                self.delta)

            theta = theta[1]  # cosTheta is not required

            # compute radiation on tilted surface for each surface
            radiation = self._get_total_radiation_tilted_surface(
                theta=theta,
                beta=self.thermal_zone.model_attr.tilt_facade[i])
            self.rad_on_tilted_surfaces.append(radiation)

    def get_sun_geometry(self, initial_time, time_discretization):
        """Computes suns geometry for a certain location and time

        This function computes hour angle, declination, zenith angle of the sun
        and solar azimuth angle for a given location and time.

        Notice:
        All inputs and outputs are given/expected in degrees. For the
        computation, radians are required. Angles are converted from degrees to
        radians via np.radians(angle). The resulting radian value is noted with
        an r-suffix. Converting radian values to degrees is done via
        np.rad2deg(angle_r).
        This conversion can also be done by multiplying/dividing with 180°/pi

        The implemented equations can be found in:
        Duffie, Beckman - Solar Engineering of Thermal Processes, 2013 (4th ed.)

        Parameters
        ----------
        initial_time : integer
            Time passed since January 1st, 00:00:00 in seconds
        time_discretization : integer
            Time between two consecutive time steps in seconds

        """

        pi = math.pi

        # Create time array
        time = ((np.linspace(
                    0, self.timestep - 1, num=self.timestep)) *
                time_discretization + initial_time)

        # Determine the day's number and standard time (neglect daylight saving)
        day_nr = time / (3600 * 24)
        std_time = time / 3600 - np.floor(day_nr) * 24

        # Equation 1.4.2, page 9
        b = 360 / 365.26 * day_nr
        b_r = np.radians(b)
        # Compute abbreviations for E and extraterrestrial irradiation (Gon)
        cos_b = np.cos(b_r)
        sin_b = np.sin(b_r)
        cos2_b = np.cos(2 * b_r)
        sin2_b = np.sin(2 * b_r)

        # Convert local time into solar time
        # Equation 1.5.3, page 11
        e = 229.2 / 60 * (
            0.000075 +
            0.001868 * cos_b -
            0.032077 * sin_b -
            0.014615 * cos2_b -
            0.040890 * sin2_b)

        # Compute standard meridian
        # Footnote 5 of chapter 1. Can be found on page 11.
        lambda_std = self.time_zone * 15

        # Compute solar time
        # Equation 1.5.2, page 11 (conversion to hours instead of minutes)
        solar_time = (std_time + 4 * (
            self.thermal_zone.parent.longitude - lambda_std) / 60 + e) - 0.5

        # Hour angle
        # The angular displacement of the sun east or west of the local meridian
        # due to rotation of the earth on its axis at 15 degrees per hour;
        # morning negative, afternoon positive
        # Confirm page 13
        self.omega = 360 / 24 * (solar_time - 12)
        # Ensure: -180 <= omega <= 180
        self.omega[self.omega < -180] += 360
        self.omega[self.omega > 180] -= 360
        omega_r = np.radians(self.omega)

        # Declination
        # The angular position of the sun at solar noon (i.e., when the sun is on
        # the local meridian) with respect to the plane of the equator, north
        # positive; −23.45 <= delta <= 23.45
        # Equation 1.6.1a, page 13
        self.delta = 23.45 * np.sin((284 + day_nr) / 365 * 2 * pi)
        delta_r = np.radians(self.delta)

        # Zenith angle
        # The angle between the vertical and the line to the sun, that is, the
        # angle of incidence of beam radiation on a horizontal surface;
        # 0 <= thetaZ <= 90. If thetaZ > 90, the sun is below the horizon.
        # Equation 1.6.5 on page 15

        # Introduce abbreviations to improve readability
        latitude_r = math.radians(self.thermal_zone.parent.latitude)
        cos_phi = math.cos(latitude_r)
        sin_phi = math.sin(latitude_r)
        cos_delta = np.cos(delta_r)
        sin_delta = np.sin(delta_r)
        cos_omega = np.cos(omega_r)
        cos_theta_z = np.maximum(
            0,
            cos_phi * cos_delta * cos_omega + sin_delta * sin_phi)
        theta_z_r = np.arccos(cos_theta_z)
        self.theta_z = np.rad2deg(theta_z_r)

        # Compute airmass
        # Footnote 3 on page 10
        self.airmass = (math.exp(-0.0001184 *
                                self.thermal_zone.parent.altitude) / (
            cos_theta_z + 0.5057 * np.power(96.08 - self.theta_z, -1.634)))

        # Compute extraterrestrial irradiance (Gon)
        # Extraterrestrial radiation incident on the plane normal to the radiation
        # on the nth day of the year.
        # Solar constant. Page 6
        g_sc = 1367  # W/m2
        # Equation 1.4.1b
        self.g_on = g_sc * (
            1.000110 +
            0.034221 * cos_b +
            0.001280 * sin_b +
            0.000719 * cos2_b +
            0.000077 * sin2_b)

    @staticmethod
    def _convert_orientation(orientation_teaser):
        """converts orientation from TEASER values to definition in sim

        Parameters
        ----------

        orientation_teaser : list [degree]
            TESAER orientation of all facades of thermal zone (win + wall)
            0 - 360
        Returns
        -------

        orientation_vdi : list [degree]
            VDI Simulation of all facades of thermal zone (win + wall)
            -180 - 180
        """

        orientation_vdi = []

        for orient in orientation_teaser:
            if orient == -1 or orient == -2:
                orientation_vdi.append(0.0)
            else:
                orientation_vdi.append(orient - 180)

        return orientation_vdi

    @staticmethod
    def _get_incidence_angle(beta, gamma, phi, omega, delta):
        """Computes the incidence angle on a tilted surface.

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
        """

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
        cos_theta = np.maximum(
            sin_delta * sin_phi * cos_beta -
            sin_delta * cos_phi * sin_beta * cos_gamma +
            cos_delta * cos_phi * cos_beta * cos_omega +
            cos_delta * sin_phi * sin_beta * cos_gamma * cos_omega +
            cos_delta * sin_beta * sin_gamma * sin_omega, 0)
        theta_r = np.arccos(cos_theta)
        theta = np.rad2deg(theta_r)

        # Return incidence angle
        return cos_theta, theta

    def _get_total_radiation_tilted_surface(
            self,
            theta,
            beta):
        """
        Compute the total radiation on a tilted surface.

        Parameters
        ----------
        theta : array_like
            Incidence angle.
        thetaZ : array_like
            Zenith angle. The angle between the vertical and the line to the sun,
            that is, the angle of incidence of beam radiation on a horizontal
            surface; 0 <= thetaZ <= 90
        beam_radiation : array_like
            The solar radiation received from the sun without having been
            scattered by the atmosphere (also often named direct radiation)
        diffuse_radiation : array_like
            The solar radiation received from the sun after its direction has been
            changed by scattering by the atmosphere.
        airmass : array_like
            The ratio of the mass of atmosphere through which beam radiation
            passes to the mass it would pass through if the sun were at the zenith.
            Thus at sea level ``m=1`` when the sun is at the zenith and ``m=2``
            for a zenith angle ``thetaZ=60`` degrees.
        extraterrestrialIrradiance : array_like
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

        beam_radiation = self.thermal_zone.parent.parent.data.weather_data['sun_dir']
        diffuse_radiation = self.thermal_zone.parent.parent.data.weather_data['sun_diff']

        f_coefficients = np.array(
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
        theta_z_r = np.radians(self.theta_z)
        cos_theta_z = np.cos(theta_z_r)
        cos_theta = np.cos(theta_r)
        a = np.maximum(0, cos_theta)
        b = np.maximum(0.087, cos_theta_z)

        # Compute epsilon (the sky's clearness)
        # Introduce variables and compute third power of theta_z_r
        kappa = 1.041
        theta_z_r_to3 = np.power(theta_z_r, 3)

        # Compute normal incidence direct irradiance
        i = beam_radiation / b
        # Prevent division by zero
        temp = np.zeros_like(theta)  # All inputs should have this length!
        temp[diffuse_radiation > 0] = (1.0 * i[diffuse_radiation > 0] /
                                       diffuse_radiation[diffuse_radiation > 0])
        # equation 1 on p. 273 in Perez et al - 1990
        epsilon = (1 + temp + kappa * theta_z_r_to3) / (1 + kappa * theta_z_r_to3)

        # Determine clear sky category
        # table 1 on page 273 in Perez et al - 1990
        # Note: As this value is used to get data from f_coefficients, the
        # implemented categories range from 0 to 7 instead from 1 to 8
        epsilon_category = np.zeros_like(epsilon, dtype=int)
        epsilon_category[(epsilon >= 1.065) & (epsilon < 1.23)] = 1
        epsilon_category[(epsilon >= 1.230) & (epsilon < 1.50)] = 2
        epsilon_category[(epsilon >= 1.500) & (epsilon < 1.95)] = 3
        epsilon_category[(epsilon >= 1.950) & (epsilon < 2.80)] = 4
        epsilon_category[(epsilon >= 2.800) & (epsilon < 4.50)] = 5
        epsilon_category[(epsilon >= 4.500) & (epsilon < 6.20)] = 6
        epsilon_category[epsilon >= 6.200] = 7

        # Compute delta (the sky's brightness)
        # equation 2 on page 273 in Perez et al - 1990
        delta = diffuse_radiation * self.airmass / self.g_on

        # Compute f1 (circumsolar brightening coefficient) and f2 (horizon
        # brightening coefficient)
        # Below table 6 on page 282 in Perez et al - 1990
        # According to Duffie and Beckman (4th edition, page 94, equation 2.16.12),
        # f1 is supposed to be greater or equal to 0
        f1 = np.maximum(f_coefficients[epsilon_category, 0] +
                        f_coefficients[epsilon_category, 1] * delta +
                        f_coefficients[epsilon_category, 2] * theta_z_r,
                        0)

        f2 = (f_coefficients[epsilon_category, 3] +
              f_coefficients[epsilon_category, 4] * delta +
              f_coefficients[epsilon_category, 5] * theta_z_r)

        # Compute diffuse radiation on tilted surface
        # Equation 9 on page 281 in Perez et al - 1990
        beta_r = math.radians(beta)
        cos_beta = math.cos(beta_r)
        sin_beta = math.sin(beta_r)
        diffuse_rad_tilt_surface = diffuse_radiation * (
            (1 - f1) * (1 + cos_beta) / 2 + f1 * a / b + f2 * sin_beta)

        # Compute the influence of beam radiation and reflected radiation
        # Equation 2.15.1 in Duffie and Beckman (4th edition, page 89)
        # Compute direct radiation on tilted surface
        # Equation 1.8.1 in Duffie and Beckman (4th edition, page 24)
        # We divide by b instead of cos_theta_z to prevent division by 0
        # Direct radiation on a tilted surface is always positive, therefore use
        # ``a`` instead of cos_theta
        direct_rad_tilt_surface = beam_radiation * a / b

        # Compute reflected total radiation
        # Equation 2.15.1 in Duffie and Beckman (4th edition, page 89)
        # Notice: We changed the proposed nomenclature. rhoG is written as albedo.
        # Total solar radiation is computed as sum of beam and diffuse radiation.
        # See page 10 in Duffie and Beckman (4th edition)
        total_solar_rad = beam_radiation + diffuse_radiation
        reflected_rad_tilt_surface = total_solar_rad * self.albedo * \
                                     (1 - cos_beta) / 2

        total_rad_tilt_surface = (diffuse_rad_tilt_surface +
                                  direct_rad_tilt_surface +
                                  reflected_rad_tilt_surface)

        # Return total radiation on a tilted surface
        return total_rad_tilt_surface


if __name__ == "__main__":

    weather_obj = Weather()

    print('Outdoor temperature in degree Celsius: ')
    print(weather_obj.temp)
