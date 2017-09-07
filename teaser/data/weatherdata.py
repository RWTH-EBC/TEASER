"""Module contains a class to load and store weather data from TRY"""
import teaser.logic.utilities as utils
import os


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

    air_temp : np.array (or pd.series)
        Dry bulb air temperature at 2 m height.
    direct_radiation : np.array (or pd.series)
        Direct horizontal radiation.
    ...

    """

    def __init__(
            self,
            path=utils.get_full_path(
            os.path.join(
                'data', 'input', 'weatherdata', 'TRY2010_05_Jahr.dat'))):

        self.path = path
        self.air_temp = None
        self.direct_radiation = None

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

        self.path = path
        self.air_temp = None
        self.direct_radiation = None
