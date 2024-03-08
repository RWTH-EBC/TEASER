import datetime
from os import listdir
from os.path import isfile, join
from typing import Optional

import ddmpc.utils.formatting
from ddmpc.weather.parser import MOSMIXParser, SParser, LParser

from ddmpc.utils.pickle_handler import read_pkl, write_pkl
import urllib.request
import matplotlib.pyplot as plt
from io import BytesIO
from zipfile import ZipFile
import pandas as pd
import urllib.error


stations = {
    "clu": {
        "AACHEN": 99808,
        "AACHEN-ORSBACH": 99809,
    },
    "id": {
        "AACHEN": 10501,
        "AACHEN-ORSBACH": 10505,
    }
}


class Forecast:
    """
    List of all elements available: https://www.mikrocontroller.net/attachment/454587/mosmix_elemente.pdf
    List of parameters, that should be extracted from the kml file.
    """

    def __init__(
            self,
            description: str,
            issue_time: datetime.datetime,
            df: pd.DataFrame,
            station_name: str,
    ):

        self.description = description
        self.issue_time = issue_time
        self.df = df
        self.station_name = station_name

    def __str__(self):
        return f'Forecast(station_name={self.station_name}, start={self.start}, length={self.length})'

    def __repr__(self):
        return 'Forecast'

    @property
    def start(self):
        return self.df.index[0]

    @property
    def stop(self):
        return self.df.index[-1]

    @property
    def length(self):
        return self.df.index[-1] - self.df.index[0]

    def shorten(self, length: datetime.timedelta):

        self.df = self.df.truncate(after=self.start + length)

    def plot(self):

        for col in self.df.columns:
            plt.title(col)
            plt.plot(self.df[col])
            plt.show()

    def save(self, directory: str = 'stored_data\\forecasts', override: bool = True):
        filename = f'{self.station_name}-{self.issue_time.strftime("%m%d%Y%H")}'
        write_pkl(self, filename=filename, directory=directory, override=override)


class DWDClient:

    def __init__(self, station_name: str):

        self.station_name = station_name

        try:
            self.station_id = stations['id'][station_name]
            self.station_clu = stations['clu'][station_name]
        except KeyError:
            raise KeyError(f'Make sure station {station_name} is included in stations.json')

    @staticmethod
    def download_kml(url: str):

        # download the kmz file
        response = urllib.request.urlopen(url)

        # create a zip file from the kmz
        zip_file = ZipFile(BytesIO(response.read()))

        # read the first name from the zip
        filename = zip_file.namelist()[0]

        # extract the file
        return zip_file.open(name=filename)

    @property
    def url_forecast_S(self):
        return 'https://opendata.dwd.de/weather/local_forecasts/mos/MOSMIX_S/all_stations/kml/MOSMIX_S_LATEST_240.kmz'

    @property
    def url_forecast_L(self):
        return 'https://opendata.dwd.de/weather/local_forecasts/mos/MOSMIX_L/single_stations/' \
               f'{self.station_id}/kml/MOSMIX_L_LATEST_{self.station_id}.kmz'

    def get_forecast_S(self, url: str = None):

        if url is None:
            url = self.url_forecast_S

        klm_file = self.download_kml(url)

        parser = SParser(kml_file=klm_file)

        description = parser.get_description()
        issue_time = parser.get_issue_time()

        df = parser.get_df(station_name=self.station_name)

        return Forecast(
            description=description,
            issue_time=issue_time,
            df=df,
            station_name=self.station_name
        )

    def get_forecast_L(self, url: str = None):

        if url is None:
            url = self.url_forecast_L

        klm_file = self.download_kml(url)

        parser = LParser(kml_file=klm_file)

        return Forecast(
            description=parser.get_description(),
            issue_time=parser.get_issue_time(),
            df=parser.get_df(),
            station_name=self.station_name,
        )

    def download_latest_forecasts_S(self):

        base_url = 'https://opendata.dwd.de/weather/local_forecasts/mos/MOSMIX_S/all_stations/kml/'

        now = datetime.datetime.now()

        # the dwd saves forecasts for 50 hours on their site
        for i in range(50):

            ddmpc.utils.formatting.print_progress(i, 50, text='downloading forcasts...')

            t = now - datetime.timedelta(hours=i)
            str_time = self.datetime_to_str(t)

            url = f'{base_url}MOSMIX_S_{str_time}_240.kmz'

            try:
                forecast = self.get_forecast_S(url=url)
                forecast.save()

            except urllib.error.URLError:
                pass

    @staticmethod
    def datetime_to_str(time: datetime.datetime):
        return time.strftime('%Y%m%d%H')


def load_Forecast(
        filename: str,
        directory: str = 'stored_data\\forecasts',
) -> Forecast:

    dc = read_pkl(filename, directory)

    assert isinstance(dc, Forecast), 'Wrong type loaded!'

    return dc


def load_Forecasts(
        directory:  str = 'stored_data\\forecasts',
        station:    str = None,
        start:      Optional[datetime.datetime] = None,
        end:        Optional[datetime.datetime] = None,
) -> list[Forecast]:

    forecasts = list()

    for filename in listdir(directory):
        if isfile(join(directory, filename)):

            forecast = read_pkl(filename, directory)
            assert isinstance(forecast, Forecast), 'Wrong type loaded!'

            start_match = start is None or start < forecast.issue_time
            end_match = end is None or forecast.issue_time < end
            station_match = station is None or forecast.station_name == station

            if start_match and end_match and station_match:
                forecasts.append(forecast)

    return forecasts


if __name__ == '__main__':

    c = DWDClient(station_name='AACHEN-ORSBACH')

    f = c.get_forecast_L()
    print(f.length)
    print(f.df.head(10).to_string())

    f = c.get_forecast_S()
    print(f.length)
    print(f.df.head(10).to_string())

