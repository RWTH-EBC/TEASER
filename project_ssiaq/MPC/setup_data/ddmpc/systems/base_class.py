import datetime
import pandas as pd
from abc import ABC, abstractmethod

from ddmpc.data_handling.storing_data import DataContainer, DataHandler
from ddmpc.modeling import Model, Constructed
from ddmpc.modeling.plotting import Plotter
from typing import Optional


class System(ABC):
    """
    Implements abstract system class to allow a modular access to the controller developement
    Contains the relevant functions to interact with a system. The controller should be passed in the simulator class.
    """

    display_time:           bool = True
    display_time_format:    str = '%m.%d.%Y - %H:%M'
    display_time_interval:  int = 60 * 60 * 4
    display_time_offset:    int = 1640995200

    def __init__(
            self,
            name:    str,
            step_size:      int,
            model:          Model,
    ):
        """
        Initialize System, e.g. load relevant information
        :param system_name: Identifier of the System
        :param directory: Directory to load
        :param step_size: Step_size of the system
        :param model: Ontology of the system, passed as model class
        """

        # system settings
        self.name:   str = name
        self.step_size:     int = step_size

        # model and plotter
        self.model:         Model = model

        # simulation
        self.time:   Optional[int] = None
        self.last_df:       pd.DataFrame = pd.DataFrame()

        # colum names
        self._readable_columns: list[str] = [f.read_name for f in self.model.readable]

    def __str__(self):
        return f'{self.__class__}(step_size={self.step_size}s, system_name={self.name})'

    def __repr__(self):
        return f'{self.__class__}(step_size={self.step_size}s, system_name={self.name})'

    @abstractmethod
    def setup(self, start_time: int, **kwargs):
        """ Set up the system at a given start time """
        ...

    @abstractmethod
    def close(self):
        """ Closes the system """

    @abstractmethod
    def do_step(self):
        """ In this method on simulation step is performed and the system time is updated """
        ...

    @abstractmethod
    def read_values(self) -> dict:
        """ Reads multiple values from System and returns them as dict """
        ...

    @abstractmethod
    def write_values(self, control_dict: dict):
        """
        Write control values to system
        :return:
        """
        ...

    def get_forecast(self, length: int) -> pd.DataFrame:
        """
        Returns a DataFrame with the disturbance forecast (weather etc.)
        :param length:  Length of the forecast in seconds
        """

        # get the forecast from the system
        forecast = self._get_forecast(length)

        # rename to known name
        for d in self.model.disturbances:

            if d.forecast_name is None:
                continue

            forecast.rename(columns={d.forecast_name: d.variable.col_name}, inplace=True)

        # add bounds to the DataFrame
        for x in self.model.controlled:
            # print(forecast.columns)
            forecast = x._process(forecast)

        return forecast

    @abstractmethod
    def _get_forecast(self, length: int) -> pd.DataFrame:
        """
        Returns a DataFrame with the disturbance forecast (weather etc.)
        :param length:  Length of the forecast in seconds
        """
        ...

    @abstractmethod
    def summary(self):
        pass

    def run(self, duration: int, controllers: Optional[list] = None) -> DataContainer:
        """ Runs the simulation using the passed controllers """

        if controllers is None:
            controllers = list()

        # update start and stop time
        start_time = self.time
        stop_time = start_time + duration

        assert start_time % self.step_size == 0 and stop_time % self.step_size == 0, \
            f'Please make sure the start ({start_time}) and stop ({stop_time})' \
            f' time are multiples of the step_size ({self.step_size})'

        for controller in controllers:
            assert self.step_size <= controller.step_size, \
                f'Please make sure the step_size of the controller (step_size={controller.step_size})' \
                f' is greater or equal to the step_size of the fmu (step_size={self.step_size}).'
            assert controller.step_size % self.step_size == 0, \
                f'The step_size of the controller (step_size={controller.step_size}) ' \
                f'must be multiple of the step_size of the fmu (step_size={self.step_size}).'

        # Initialize a pandas DataFrame by calculating the length of the DataFrame and all column names
        index = range(0, int((stop_time - start_time) / self.step_size))

        df = pd.DataFrame(
            index=index,
            dtype=float,
        )

        # If the system was already in use initialize concat the new, empty data frame with the old one
        if not self.last_df.empty:
            df = pd.concat([self.last_df, df], ignore_index=True)
            skip_rows = len(self.last_df)
        else:
            skip_rows = 0

        # write default controls to system
        self._write_default_controls()

        # ------------------ simulation loop ------------------

        for idx in df.index[skip_rows:]:

            def update(dct: dict):
                """ function to update the DataFrame in the current row with a hash map """

                for col in dct:
                    df.loc[idx, col] = dct[col]

            if self.time % self.step_size == 0:

                # display the current time
                self._display_time()

                # update the data frame with the current values so the controller can access them
                update(self.read_values())

                # update the current row by the helping variables of the Controlled Features (eg. LowerBound)
                self.model.update(df=df, idx=idx)

                # calculate the controls and write them
                for controller in controllers:

                    if self.time % controller.step_size == 0:

                        # calculate the controls
                        controls, additional_columns = controller(df.loc[df.index <= idx])

                        # write controls to the system
                        self.write_values(controls)

                        # update current row by controls
                        update(controls)

                        # update the additional columns as Predictions or solver call times
                        update(additional_columns)

            # advance simulation
            self.do_step()

        # ------------------ simulation loop ------------------

        # last df
        self.last_df = df[skip_rows:].copy(deep=True)

        # create DataContainer
        dc = DataContainer(df=df[skip_rows:])

        return dc

    def _write_default_controls(self):
        """ Writes the default controls to the System """

        default_controls = {u.variable.col_name: u.default for u in self.model.controls}

        self.write_values(default_controls)

    def _display_time(self):
        """ Displays the System time """

        if not self.display_time:
            return

        if not self.time % self.display_time_interval == 0:
            return

        time = datetime.datetime.fromtimestamp(self.time + self.display_time_offset)

        print(time.strftime(self.display_time_format))

