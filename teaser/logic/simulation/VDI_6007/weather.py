#!/usr/bin/env python
# coding=utf-8
"""
TEASER weather class for VDI 6007 calculation
"""

import os
import numpy as np
import math





def getIncidenceAngle(beta, gamma, phi, omega, delta):
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
    """
    # Compute incidence angle of beam radiation
    # Transform to radian
    betaR = math.radians(beta)
    phiR = math.radians(phi)
    gammaR = math.radians(gamma)
    deltaR = np.radians(delta)
    omegaR = np.radians(omega)

    # Introduce required abbreviations
    sinBeta = math.sin(betaR)
    cosBeta = math.cos(betaR)
    sinDelta = np.sin(deltaR)
    cosDelta = np.cos(deltaR)
    sinPhi = math.sin(phiR)
    cosPhi = math.cos(phiR)
    sinGamma = math.sin(gammaR)
    cosGamma = math.cos(gammaR)
    sinOmega = np.sin(omegaR)
    cosOmega = np.cos(omegaR)

    # Equation 1.6.2, page 14
    cosTheta = np.maximum(sinDelta * sinPhi * cosBeta -
                          sinDelta * cosPhi * sinBeta * cosGamma +
                          cosDelta * cosPhi * cosBeta * cosOmega +
                          cosDelta * sinPhi * sinBeta * cosGamma * cosOmega +
                          cosDelta * sinBeta * sinGamma * sinOmega, 0)
    thetaR = np.arccos(cosTheta)
    theta = np.rad2deg(thetaR)

    # Return incidence angle
    return (cosTheta, theta)


def getTotalRadiationTiltedSurface(theta, thetaZ,
                                   beamRadiation, diffuseRadiation,
                                   airmass, extraterrestrialIrradiance,
                                   beta, albedo):
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
    beamRadiation : array_like
        The solar radiation received from the sun without having been
        scattered by the atmosphere (also often named direct radiation)
    diffuseRadiation : array_like
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

    fCoefficients = np.array(
        [[-0.0083117, 0.5877285, -0.0620636, -0.0596012, 0.0721249,
          -0.0220216],
         [0.1299457, 0.6825954, -0.1513752, -0.0189325, 0.065965, -0.0288748],
         [0.3296958, 0.4868735, -0.2210958, 0.055414, -0.0639588, -0.0260542],
         [0.5682053, 0.1874525, -0.295129, 0.1088631, -0.1519229, -0.0139754],
         [0.873028, -0.3920403, -0.3616149, 0.2255647, -0.4620442, 0.0012448],
         [1.1326077, -1.2367284, -0.4118494, 0.2877813, -0.8230357, 0.0558651],
         [1.0601591, -1.5999137, -0.3589221, 0.2642124, -1.127234, 0.1310694],
         [0.677747, -0.3272588, -0.2504286, 0.1561313, -1.3765031, 0.2506212]
         ])

    # Compute a and b (page 281, below equation 9)
    thetaR = np.radians(theta)
    thetaZR = np.radians(thetaZ)
    cosThetaZ = np.cos(thetaZR)
    cosTheta = np.cos(thetaR)
    a = np.maximum(0, cosTheta)
    b = np.maximum(0.087, cosThetaZ)

    # Compute epsilon (the sky's clearness)
    # Introduce variables and compute third power of thetaZR
    kappa = 1.041
    thetaZRTo3 = np.power(thetaZR, 3)

    # Compute normal incidence direct irradiance
    I = beamRadiation / b
    # Prevent division by zero
    temp = np.zeros_like(theta)  # All inputs should have this length!
    temp[diffuseRadiation > 0] = (1.0 * I[diffuseRadiation > 0] /
                                  diffuseRadiation[diffuseRadiation > 0])
    # equation 1 on p. 273 in Perez et al - 1990
    epsilon = (1 + temp + kappa * thetaZRTo3) / (1 + kappa * thetaZRTo3)

    # Determine clear sky category
    # table 1 on page 273 in Perez et al - 1990
    # Note: As this value is used to get data from fCoefficients, the
    # implemented categories range from 0 to 7 instead from 1 to 8
    epsilonCategory = np.zeros_like(epsilon, dtype=int)
    epsilonCategory[(epsilon >= 1.065) & (epsilon < 1.23)] = 1
    epsilonCategory[(epsilon >= 1.230) & (epsilon < 1.50)] = 2
    epsilonCategory[(epsilon >= 1.500) & (epsilon < 1.95)] = 3
    epsilonCategory[(epsilon >= 1.950) & (epsilon < 2.80)] = 4
    epsilonCategory[(epsilon >= 2.800) & (epsilon < 4.50)] = 5
    epsilonCategory[(epsilon >= 4.500) & (epsilon < 6.20)] = 6
    epsilonCategory[epsilon >= 6.200] = 7

    # Compute Delta (the sky's brightness)
    # equation 2 on page 273 in Perez et al - 1990
    Delta = diffuseRadiation * airmass / extraterrestrialIrradiance

    # Compute F1 (circumsolar brightening coefficient) and F2 (horizon
    # brightening coefficient)
    # Below table 6 on page 282 in Perez et al - 1990
    # According to Duffie and Beckman (4th edition, page 94, equation 2.16.12),
    # F1 is supposed to be greater or equal to 0
    F1 = np.maximum(fCoefficients[epsilonCategory, 0] +
                    fCoefficients[epsilonCategory, 1] * Delta +
                    fCoefficients[epsilonCategory, 2] * thetaZR,
                    0)

    F2 = (fCoefficients[epsilonCategory, 3] +
          fCoefficients[epsilonCategory, 4] * Delta +
          fCoefficients[epsilonCategory, 5] * thetaZR)

    # Compute diffuse radiation on tilted surface
    # Equation 9 on page 281 in Perez et al - 1990
    betaR = math.radians(beta)
    cosBeta = math.cos(betaR)
    sinBeta = math.sin(betaR)
    diffuseRadTiltSurface = diffuseRadiation * ((1 - F1) * (1 + cosBeta) / 2 +
                                                F1 * a / b + F2 * sinBeta)

    # Compute the influence of beam radiation and reflected radiation
    # Equation 2.15.1 in Duffie and Beckman (4th edition, page 89)
    # Compute direct radiation on tilted surface
    # Equation 1.8.1 in Duffie and Beckman (4th edition, page 24)
    # We divide by b instead of cosThetaZ to prevent division by 0
    # Direct radiation on a tilted surface is always positive, therefore use
    # ``a`` instead of cosTheta
    directRadTiltSurface = beamRadiation * a / b

    # Compute reflected total radiation
    # Equation 2.15.1 in Duffie and Beckman (4th edition, page 89)
    # Notice: We changed the proposed nomenclature. rhoG is written as albedo.
    # Total solar radiation is computed as sum of beam and diffuse radiation.
    # See page 10 in Duffie and Beckman (4th edition)
    totalSolarRad = beamRadiation + diffuseRadiation
    reflectedRadTiltSurface = totalSolarRad * albedo * (1 - cosBeta) / 2

    totalRadTiltSurface = (diffuseRadTiltSurface +
                           directRadTiltSurface +
                           reflectedRadTiltSurface)

    # Return total radiation on a tilted surface
    return totalRadTiltSurface

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
        The number of calculated timesteps, default is 8760
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
        self.timesteps = 3600
        self.nb_timesteps = 365 * 24 * 3600 / self.timesteps
        self.time_zone = 1
        self.albedo = 0.2
        self.g_on = None
        self.omega = None
        self.airmass = None
        self.delta = None
        self.theta_z = None
        self.rad_on_tilted_surfaces = []

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
                    0,
                    self.timesteps - 1,
                    num=self.timesteps)) * time_discretization + initial_time)

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

    def _convert_orientation(self, orientation_teaser):
        """converts orientation from TEASER values to definition in sim

        Parameters
        ----------

        orientation_teaser : list [degree]
            TESAER orientation of all facades of thermal zone (win + wall)
            0 - 360
        Returns
        -------

        orientation_vdi : list [degree]
            VDI Simulation of all facedes of thermal zone (win + wall)
            -180 - 180

        """

        orientation_vdi = []

        for orient in orientation_teaser:
            if orient == -1 or orient == -2:
                orientation_vdi.append(0.0)
            else:
                orientation_vdi.append(orient - 180)

        return orientation_vdi

    def get_solar_gains(self):
        """computes solar gains on tilted surfaces"""

        gamma = self.convert_orientation(orientation_teaser=
            self.thermal_zone.parent.model_attr.orientation_facade)

        for i in range(len(gamma)):
            # compute incidence angle on each surface
            theta = getIncidenceAngle(
                self.thermal_zone.model_attr.tilt_facade[i],
                gamma[i],
                self.thermal_zone.parent.longitude,
                self.omega,
                self.delta)

            theta = theta[1]  # cosTheta is not required

            # compute radiation on tilted surface for each surface
            radiation = getTotalRadiationTiltedSurface(
                theta,
                self.theta_z,
                self.thermal_zone.parent.parent.data.weather['sun_dir'],
                self.thermal_zone.parent.parent.data.weather['sun_diff'],
                self.airmass,
                self.g_on,
                self.thermal_zone.model_attr.tilt_facade[i],
                self.albedo)
            self.rad_on_tilted_surfaces.append(radiation)

if __name__ == "__main__":

    weather_obj = Weather()

    print('Outdoor temperature in degree Celsius: ')
    print(weather_obj.temp)
