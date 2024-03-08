import datetime
import pandas as pd
from typing import Callable, Optional

import pytz

from ddmpc.modeling.plotting import Plotter
from ddmpc.data_handling import DataContainer
from ddmpc.systems.base_class import System
from ddmpc.modeling.main import Model
from ddmpc.systems.aedifion import AedifionClient, DataPoint, AedifionReadable
from ddmpc.weather.DWD import DWDClient
import pause
import numpy as np
from ddmpc.utils.pickle_handler import write_pkl
from ddmpc.utils.file_manager import file_manager


def round_time(
        dt:             datetime.datetime = None,
        date_delta:     datetime.timedelta = datetime.timedelta(minutes=1),
        to:             str = 'average',
):
    """
    Round a datetime object to a multiple of a timedelta
    dt : datetime.datetime object, default now.
    dateDelta : timedelta object, we round to a multiple of this, default 1 minute.
    """

    round_to = date_delta.total_seconds()
    if dt is None:
        dt = datetime.datetime.now(tz=Aedifion.tz)

    seconds = dt.timestamp()

    if seconds % round_to == 0 and dt.microsecond == 0:
        rounding = (seconds + round_to / 2) // round_to * round_to
    else:
        if to == 'up':
            # is a floor division, not a comment on following line (like in javascript):
            rounding = (seconds + dt.microsecond / 1000000 + round_to) // round_to * round_to
        elif to == 'down':
            rounding = seconds // round_to * round_to
        else:
            rounding = (seconds + round_to / 2) // round_to * round_to

    return dt + datetime.timedelta(0, rounding - seconds)


class Aedifion(System):

    tz = pytz.timezone('Europe/Berlin')

    def __init__(
            self,
            name:                   str,
            step_size:              int,
            model:                  Model,
            weather_station_name:   str = 'AACHEN-ORSBACH',
            forecast_mapping:       dict = None,
            write_callback:         Callable = None,
            control_buffer:         datetime.timedelta = datetime.timedelta(minutes=5),
    ):

        assert step_size % 60*60 == 0, 'The step size must be a multiple of one hour.'

        super().__init__(
            name=name,
            step_size=step_size,
            model=model,
        )

        self.dwd_client: DWDClient = DWDClient(
            station_name=weather_station_name,
        )

        self.aedifion_client: AedifionClient = AedifionClient(
            dataPoints=[feature.variable for feature in model.features if isinstance(feature.variable, DataPoint)],
        )

        self.forecast_mapping: dict = forecast_mapping

        self._constructed_columns: list = [c.col_name for c in self.model.constructed]

        self.write_callback: Callable = write_callback

        self.control_buffer: datetime.timedelta = control_buffer

        self.last_values: dict = dict()

    @property
    def last_step(self) -> datetime.datetime:
        """ The next datetime at which the  controls are applied"""

        return round_time(
            dt=datetime.datetime.now(tz=self.tz),
            date_delta=datetime.timedelta(seconds=self.step_size),
            to='down',
        )

    @property
    def next_step(self) -> datetime.datetime:
        """ The next datetime at which the  controls are applied"""

        return round_time(

            dt=datetime.datetime.now(tz=self.tz),
            date_delta=datetime.timedelta(seconds=self.step_size),
            to='up',
        )

    @property
    def next_mpc_call(self) -> datetime.datetime:
        """ Five minutes before the controls are passed to the system the mpc is called """

        return self.next_step - self.control_buffer

    @property
    def now(self) -> datetime.datetime:
        return datetime.datetime.now(tz=self.tz)

    def setup(self, start_date: datetime.datetime = None, **kwargs):
        """
        1. waits until the start_date
        2. downloads the

        """

        if start_date is None:
            # if no start date is provided, start now
            start_date = self.now

        # the start time must be in the future
        # if a start date is give wait until ten minutes before this date
        if self.now <= start_date:
            print(f'Starting at {start_date.strftime("%d.%m.%Y, %H:%M")}')
            pause.until(start_date - datetime.timedelta(minutes=10))

        # set the system time to the start date
        self.system_time = start_date

        # load the data from the last day
        start = self.last_step - datetime.timedelta(days=1)
        end = self.last_step

        last_day = self.aedifion_client.getTimeSeries(
            samplerate=self.step_size,
            start=start,
            end=end,
        )

        # convert index to SimTime as unix timestamp by converting from nanoseconds to seconds
        last_day['SimTime'] = last_day.index.astype(np.int64) // 10**9
        last_day.reset_index(inplace=True, drop=True)

        self.model.process(last_day)

        self.last_df = last_day

    def do_step(self) -> (pd.DataFrame, pd.DataFrame):
        raise NotImplementedError()

    def close(self):

        for u in self.model.controls:

            assert isinstance(u.variable, DataPoint)

            res = u.variable.postSetPoint(
                value="null",
            )

            print(res.json())

    def read_values(self) -> dict:
        """ Reads the past values"""
        try:
            values = self.aedifion_client.getLastValues()
        except ValueError as e:
            print(e)
            values = self.last_values

        values['SimTime'] = self.next_step.timestamp()

        return values

    def _get_forecast(self, length: int) -> pd.DataFrame:

        forecast = self.dwd_client.get_forecast_S().df

        forecast = forecast.reindex(pd.date_range(
            start=forecast.index.min(),
            end=forecast.index.max(),
            freq=f'{self.step_size}s'),
        )

        forecast.interpolate(method='linear', inplace=True)

        # convert index to SimTime as unix timestamp by converting from nanoseconds to seconds
        forecast['SimTime'] = forecast.index.astype(np.int64) // 10**9
        forecast.reset_index(inplace=True, drop=True)

        if self.forecast_mapping is None:
            return forecast

        # map the names
        df = forecast.rename(columns=self.forecast_mapping)

        return df

    def plan_run(
            self,
            end_date:   datetime.datetime,
            start_date: Optional[datetime.datetime] = None,
            controller: list = None,
    ):
        now = datetime.datetime.now()

        if start_date is None:
            start_date = now

        if start_date < now:
            start_date = now

        print(f'Running MPC from {start_date.strftime("%d.%m.%Y, %H:%M")} to {end_date.strftime("%d.%m.%Y, %H:%M")}')

        pause.until(start_date)

        return self.run(
            duration=int((end_date - start_date).total_seconds()),
            controller=controller,
        )

    def run(
            self,
            duration: int,
            controller=None,
    ) -> DataContainer:
        """ Runs the simulation using the passed controllers """

        assert controller is not None, 'A controller must be passed to run the aedifion System'
        assert controller.step_size == self.step_size, f'Make sure the controller has a step size of {self.step_size}s.'

        # Initialize a pandas DataFrame by calculating the length of the DataFrame and all column names
        new_rows = int(duration / self.step_size)
        skip_rows = len(self.last_df)

        df = self.last_df.reindex(range(0, skip_rows + new_rows))

        # ------------------ control loop ------------------

        for idx in df.index[skip_rows:]:

            def update(dct: dict):
                """ function to update the DataFrame in the current row with a hash map """

                for col in dct:
                    df.loc[idx, col] = dct[col]

            # update the data frame with the current values so the controller can access them
            values = self.read_values()
            update(values)

            # update the current row by the helping variables
            self.model.update(df=df, idx=idx)

            controls = dict()

            if controller is not None:

                try:

                    # calculate the controls
                    controls, additional_data = controller(df.loc[df.index <= idx])

                    # update current row by controls and additional data
                    update(controls)
                    update(additional_data)

                except Exception as e:

                    print('Error occurred while running the MPC:', e)

            # write the current progress to the disc in form of df
            write_pkl(df[:idx+1], filename=f'progress', directory=file_manager.data_dir(), override=True)

            # wait until the next step then write the controls
            print(f'Waiting unitl {self.next_step.strftime("%d.%m.%Y, %H:%M")} to write controls:')
            for k, v in controls.items():
                print(f'\t{k}: {" " * (50 - len(k))}{v}')
            print()

            try:
                pause.until(self.next_step)
            except KeyboardInterrupt:
                exit()

            try:
                self.write_values(controls)
            except Exception as e:
                print('Error occurred while writing the controls:', e)

            # wait until next mpc call then start over again
            print(f'Waiting until: {self.next_mpc_call.strftime("%d.%m.%Y, %H:%M")} to call the mpc.')

            try:
                pause.until(self.next_mpc_call)
            except KeyboardInterrupt:
                exit()

        # ------------------ control loop ------------------

        return DataContainer(df=df[skip_rows:])

    def get_historic_data(self, start: datetime.datetime, end: datetime.datetime) -> DataContainer:

        history = self.aedifion_client.getTimeSeries(
            samplerate=self.step_size,
            start=start,
            end=end,
        )

        history['SimTime'] = history.index.astype(np.int64) // 10**9
        history.reset_index(inplace=True, drop=True)

        # process constructed Features
        history = self.model.process(history)

        return DataContainer(df=history)

    def write_values(self, control_dict: dict):

        print(f'Writing controls: {control_dict}')

        # if the write callback is not None call it and then return
        if self.write_callback is not None:
            self.write_callback(control_dict)
            return

    def get_system_time(self) -> int:
        """ This method returns the Systems time """
        return int(self.next_step.timestamp())

    def summary(self):

        print('aedifion System:')

