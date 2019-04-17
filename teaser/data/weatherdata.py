"""Module contains a class to load and store weather data from TRY"""
import teaser.logic.utilities as utils
import os
import numpy as np


class WeatherData(object):
    """Class for loading and storing weather data from TMY format.

    This class loads all necessary weather data (e.g. air temperature and solar
    radiation) and stores them into class attributes to be easy accessible.

    Parameters
    ----------

    path : str
        Path to the weather file.

    Attributes
    ----------

    air_temp : np.array (or pd.series) [degree C]
        Dry bulb air temperature in degree C at 2 m height.
    direct_radiation : np.array (or pd.series) [W/m2]
        Direct horizontal radiation.
    diffuse_radiation : np.array [W/m2]
        diffuse horizontal radiation
    sky_radiation : np.array [W/m2]
        radiation of the atmosphere downwards positive
    earth_radiation : np.array [W/m2]
        radiation of the earth upwards negative
    """

    def __init__(
            self,
            path=utils.get_full_path(
            os.path.join(
                'data', 'input', 'inputdata', 'weatherdata',
                'TRY2010_05_Jahr.dat'))):

        self.path = path
        self.air_temp = None
        self.direct_radiation = None
        self.diffuse_radiation = None
        self.sky_radiation = None
        self.earth_radiation = None

        self.load_weather(path=self.path)

    def load_weather(self, path):
        """This function loads weather data directly from TRY format.

        Sets class attributes with weather data as numpy array or pandas
        series.

        Parameters
        ----------
        path: string
            path of teaserXML file

        """

        weather_data = np.genfromtxt(
            path,
            skip_header=38,
            usecols=(8, 13, 14, 16, 17),
            encoding="ISO 8859-1")

        self.air_temp = weather_data[:, 0]
        self.direct_radiation = weather_data[:, 1]
        self.diffuse_radiation = weather_data[:, 2]
        self.sky_radiation = weather_data[:, 3]
        self.earth_radiation = weather_data[:, 4]
