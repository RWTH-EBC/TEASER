import time

import pandas as pd

import ddmpc.utils.formatting
from ddmpc.modeling.main import Model
from ddmpc.systems.base_class import System
from urllib.parse import urljoin
import requests
import json


class BopTest(System):

    def __init__(
            self,
            model: Model,
            step_size: int,
            url: str,
            name: str,
            forecast_mapping: dict = None,
    ):

        super(BopTest, self).__init__(
            name=name,
            step_size=step_size,
            model=model,
        )

        self.url = url
        self.controls = dict()
        self.measurements = dict()

        self.inputs = requests.get(url=urljoin(url, 'inputs')).json()
        self.outputs = requests.get(url=urljoin(url, 'measurements')).json()

        # forecast
        forecast_params = requests.get(url=urljoin(self.url, 'forecast_parameters')).json()
        self.forecast_horizon = forecast_params['horizon']
        self.forecast_interval = forecast_params['interval']
        self.forecast_mapping = forecast_mapping

    def setup(
            self,
            start_time:             int,
            warmup_period:          int = 0,
            scenario:               dict = None,
            active_control_layers:  dict = None,
    ):

        # start time
        assert start_time >= 0, 'Please make sure the start time is greater or equal to zero.'

        # set step size
        requests.put(url=urljoin(self.url, 'step'), data={'step': self.step_size})

        # initialization
        init_params = {'start_time': start_time, 'warmup_period': warmup_period}
        self.measurements = requests.put(url=urljoin(self.url, 'initialize'), data=init_params).json()

        # update all time variables
        self.measurements['SimTime'] = self.measurements['time']
        self.time = self.measurements['time']

        if scenario is not None:
            self.measurements = requests.put(urljoin(self.url, 'scenario'), data=scenario).json()

        self.controls.clear()
        if active_control_layers is not None:
            self.controls.update(active_control_layers)

        # set the forecast horizon to a small value so the
        self._set_forecast_parameter()

    @property
    def scenario(self):
        return requests.get(url=urljoin(self.url, 'scenario')).json()

    def do_step(self):

        def advance():
            """ advances the simulation by one step """

            url_advance = urljoin(self.url, 'advance')
            raw_measurements = requests.post(url_advance, self.controls)

            try:
                self.measurements.update(
                    raw_measurements.json()
                )

            except json.decoder.JSONDecodeError:

                # if the Response is empty manually advance the simulation time by one
                self.measurements['time'] = self.measurements['time'] + self.step_size

                print('Failed to convert Response to json at t=', self.measurements['time'])
                print('Continuing with the last measurements.')

        advance()

        # update all time variables
        self.measurements['SimTime'] = self.measurements['time']
        self.time = self.measurements['time']

    def close(self):
        pass

    def read_values(self) -> dict:

        for var_name in self._readable_columns:
            assert var_name in self.measurements.keys(),\
                f'The feature with var_name: "{var_name}" can not be read. Measurements: {self.measurements}'

        return {var_name: self.measurements[var_name] for var_name in ['SimTime'] + self._readable_columns}

    def write_values(self, control_dict: dict):
        """ Updates the control dict with new inputs """

        self.controls.update(control_dict)

    def _get_forecast(self, length: int) -> pd.DataFrame:

        if length != self.forecast_interval:
            requests.put(url=urljoin(self.url, 'forecast_parameters'), data={'horizon': length})

        def request_forecast() -> pd.DataFrame:

            try:
                return pd.DataFrame(requests.get(urljoin(self.url, 'forecast')).json())

            except json.decoder.JSONDecodeError:

                print('Requesting forecast failed. Trying again...')

                return request_forecast()

        forecast = request_forecast()
        forecast.rename(columns={'time': 'SimTime'}, inplace=True)

        if self.forecast_mapping is not None:
            forecast.rename(columns=self.forecast_mapping, inplace=True)

        return forecast

    def _set_forecast_parameter(self, horizon: int = 60*60*24):

        requests.put(
            url=urljoin(self.url, 'forecast_parameters'),
            data={'interval': self.step_size, 'horizon': horizon}
        )

    def summary(self):

        print('----------------------- BopTest Summary -----------------------')
        print(f'Name:           {self.name}')
        print(f'URL:            {self.url}')
        print(f'Scenario:            {self.url}')
        print(self.scenario)

        print(f'Inputs:')
        rows = [['', 'Name', 'Minimum', 'Maximum', 'Unit', 'Description']]
        for name, i in self.inputs.items():
            row = ['', name, i['Minimum'], i['Maximum'], i['Unit'], i['Description']]
            rows.append(row)

        rows.append(['Outputs:'])
        rows.append(['', 'Name', 'Minimum', 'Maximum', 'Unit', 'Description'])
        for name, i in self.outputs.items():
            row = ['', name, i['Minimum'], i['Maximum'], i['Unit'], i['Description']]
            rows.append(row)

        ddmpc.utils.formatting.print_table(rows=rows)
        print()
