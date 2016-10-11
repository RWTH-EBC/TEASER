#!/usr/bin/env python
# coding=utf-8
"""
TEASER weather class for VDI 6007 calculation
"""

import os
import numpy as np

import teaser.logic.simulation.VDI_6007.sun as sun


def get_weather(filepath):
    """

    Parameters
    ----------
    filepath : str
            Path to weather file

    Returns
    -------
    weather_data : numpy array
        nd numpy array with weather data
    """

    return np.loadtxt(filepath, skiprows=38, usecols=(8, 13, 14, 16, 17))


class Weather(object):
    """
    Weather class of TEASER
    """

    def __init__(self, beta, gamma, weather_path=None, albedo=0.2, timeZone=1,
                 altitude=0, location=(49.5, 8.5)):
        """
        Constructor of weather object

        Parameters
        ----------
        beta
        gamma
        weather_path : str, optional
            Path to weather file (default: None)
            If set to None, loads weather set TRY 2010, region 12
        albedo
        timeZone
        altitude
        location
        """

        if weather_path is None:
            #  If None, use default weather path

            wfile = 'TRY2010_12_Jahr.dat'
            this_path = os.path.dirname(os.path.abspath(__file__))
            weather_path = os.path.join(this_path, 'input_weather', wfile)

        # Load weather data
        weather_data = get_weather(weather_path)

        self.temp = weather_data[:, 0]  # Outdoor temperature in degree C
        self.sun_dir = weather_data[:, 1]  # Direct radiation
        self.sun_diff = weather_data[:, 2]  # Diffuse radiation
        self.rad_sky = weather_data[:, 3]
        self.rad_earth = weather_data[:, 4]

        # Sun radiation on surfaces
        self.sun_rad = sun.getSolarGains(0, 3600, weather_data.shape[0],
                                         timeZone=timeZone,
                                         location=location,
                                         altitude=altitude,
                                         beta=beta,
                                         gamma=gamma,
                                         beam=self.sun_dir,
                                         diffuse=self.sun_diff,
                                         albedo=albedo)


if __name__ == "__main__":
    beta = [45, 90, 90, 45, 90, 90]
    gamma = -np.array([0, 0, 90, 0, 180, 270])

    weather_obj = Weather(beta=beta, gamma=gamma)

    print('Outdoor temperature in degree Celsius: ')
    print(weather_obj.temp)
