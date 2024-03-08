from datetime import datetime

import lxml.etree
import pandas as pd
import pytz
from lxml import etree


class MOSMIXParser:

    tags: dict[dict] = {
        'T5cm':
            {'name': 'weather_temperature_5cm', 'func': lambda x: x - 273.15},   # Temperature 5cm above surface in K
        'TTT':
            {'name': 'weather_temperature', 'func': lambda x: x - 273.15},  # Temperature 2m above surface in K
        'Rad1h':
            {'name': 'weather_radiation', 'func': lambda x: x / 3.6},       # Global Irradiance in Kj/m²
        'N':
            {'name': 'weather_clouds', 'func': lambda x: x},                # Total cloud cover in %
        'Neff':
            {'name': 'weather_clouds_eff', 'func': lambda x: x},            # Effective cloud cover in %
        'Td':
            {'name': 'weather_dewpoint', 'func': lambda x: x - 273.15},     # Dewpoint 2m above surface in K
        'RRS1c':
            {'name': 'weather_rain', 'func': lambda x: x},          # Snow-Rain-Equivalent during the last hour in kg/m²
    }

    def __init__(self, kml_file):

        self.tree = etree.parse(kml_file)

    def get_element_by_name(self, name: str):
        return self.tree.xpath(f'////*[name()="{name}"]')[0]

    def get_description(self):
        return self.get_element_by_name('kml:description').text

    def get_issue_time(self):
        return datetime.strptime(self.get_element_by_name('dwd:IssueTime').text, '%Y-%m-%dT%H:%M:%S.000Z')

    def get_date_time_index(self) -> pd.DatetimeIndex:

        time_steps = [timeslot.text for timeslot in self.get_element_by_name('dwd:ForecastTimeSteps').getchildren()]
        time_steps = [datetime.strptime(str_time, '%Y-%m-%dT%H:%M:%S.000Z') for str_time in time_steps]

        datetime_index = pd.DatetimeIndex(time_steps)
        datetime_index = datetime_index.tz_localize(pytz.timezone('Europe/Berlin'), ambiguous=True, nonexistent='shift_forward')

        return datetime_index

    def save_tree_as_txt(self):

        self.tree.write('pretty_etree.txt', pretty_print=True)


class SParser(MOSMIXParser):

    def get_df(self, station_name: str) -> pd.DataFrame:

        station_node = self.tree.xpath(f'////*[name()="kml:description" and .="{station_name}"]')[0]

        # element: lxml.etree._Element
        # print('text:', element.text, 'prefix:', element.prefix)

        next_element = station_node.getnext()
        # next_element: lxml.etree._Element

        forecast_dict = dict()
        for tag, dct in self.tags.items():

            node = next_element.xpath(f'./*[name()="dwd:Forecast" and @*[name()="dwd:elementName" and .="{tag}"]]')[0]

            # split string
            lst = node.getchildren()[0].text.split()

            try:
                # convert to float and apply function
                lst = [dct['func'](float(i)) for i in lst]

            except ValueError:
                pass

            # save to dict
            forecast_dict[dct['name']] = lst

        return pd.DataFrame(
            data=forecast_dict,
            index=self.get_date_time_index(),
        )


class LParser(MOSMIXParser):

    def get_df(self) -> pd.DataFrame:

        forecast_dict = dict()

        for tag, dct in self.tags.items():

            search_string = f'////*[name()="dwd:Forecast" and @*[name()="dwd:elementName" and .="{tag}"]]'

            path = self.tree.xpath(search_string)

            text = path[0].getchildren()[0].text

            # split string
            lst = text.split()

            try:
                # convert to float and apply function
                lst = [dct['func'](float(i)) for i in lst]

            except ValueError:
                pass

            forecast_dict[dct['name']] = lst

        return pd.DataFrame(
            data=forecast_dict,
            index=self.get_date_time_index(),
        )
