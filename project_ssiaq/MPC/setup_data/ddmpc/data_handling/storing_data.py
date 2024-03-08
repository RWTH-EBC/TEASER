""" data_handling.py: Classes to manage simulated data using Pandas DataFrames """
import datetime

import numpy as np
import pandas as pd
from typing import Union, Optional

from ddmpc.utils.pickle_handler import write_pkl, read_pkl
from ddmpc.modeling.plotting import Plotter
from ddmpc.modeling.variables.features import Controlled, Feature
import ddmpc.utils.formatting as fmt
from ddmpc.utils.file_manager import file_manager


class DataContainer:
    """ stores mpc data and additional information """

    def __init__(
            self,
            df:         pd.DataFrame,
    ):

        assert len(df) >= 1, 'The DataFrame must contain cant be empty.'

        self.df:            pd.DataFrame = df
        self.predictions:   Optional[pd.DataFrame] = None

    def __str__(self):
        return f'DataContainer({self.info})'

    def __repr__(self):
        return f'DataContainer({self.info})'

    def __get__(self, instance, owner):
        """ returns the DataFrame """

        return self.df

    def __set__(self, instance, value):

        self.df = value

    @property
    def info(self):
        return f"From {int(self.start_time/(60*60*24))} to {int(self.stop_time/(60*60*24))} - " \
               f"Duration {int(self.duration / (60 * 60 * 24))}"

    @property
    def start_time(self):
        return self.df['SimTime'].iloc[0]

    @property
    def stop_time(self):
        return self.df['SimTime'].iloc[-1]

    @property
    def duration(self):
        return self.stop_time - self.start_time

    @property
    def step_size(self):
        return self.df['SimTime'].iloc[1] - self.df['SimTime'].iloc[0]

    def split(self, shares: tuple[float]) -> list:
        """
        Splits a single DataContainer into new DataContainers.
        """

        assert sum(shares) == 1, \
            'Make sure mpc, testing and validation split add up to one.'

        # assign to new DataFrames
        split_containers = list()

        last_split = 0
        for share in shares:

            new_split = int(share * len(self.df))

            split_containers.append(
                DataContainer(
                    df=self.df.iloc[last_split:last_split+new_split]
                )
            )

            last_split += new_split

        return split_containers

    @staticmethod
    def merge(containers: list) -> list:
        """ merges all stored DataContainers together """

        # make sure stop and start time do match
        def merge(lst: list, new):

            if len(lst) == 0:
                lst.append(new)

                return lst

            if not lst[-1].stop_time == new.start_time - new.step_size:
                lst.append(new)

                return lst

            merged_df = pd.concat([lst[-1].df, new.df])
            merged_df = merged_df.reset_index(drop=True)

            lst[-1] = DataContainer(df=merged_df)

            return lst

        merged_lst = list()
        for next_df in containers:
            merged_lst = merge(merged_lst, next_df)

        return merged_lst

    def shorten(
            self,
            start_time: Union[int, datetime.datetime] = None,
            stop_time:  Union[int, datetime.datetime] = None,
    ):

        if isinstance(start_time, datetime.datetime):
            start_time = start_time.timestamp()

        if isinstance(stop_time, datetime.datetime):
            stop_time = stop_time.timestamp()

        if start_time is not None:
            self.df = self.df[start_time <= self.df['SimTime']]

        if stop_time is not None:
            self.df = self.df[self.df['SimTime'] <= stop_time]

    def plot(
            self,
            plotter:    Plotter,
            start_time: int = None,
            stop_time:  int = None,
            show_plot:  bool = True,
            save_plot:  bool = False,
            filepath:   str = None,
    ):
        """
        Plots the DataFrame.
        """

        df = self.df

        if start_time is not None:
            df = df[start_time <= df['SimTime']]

        if stop_time is not None:
            df = df[df['SimTime'] <= stop_time]

        plotter.plot(df=df, save_plot=save_plot, show_plot=show_plot, filepath=filepath)

    def mean(self, feature: Feature):

        return self.df[feature.variable.col_name].mean()

    def mse(self, feature: Controlled) -> pd.Series:
        """ returns the mean squared error for a given feature """

        return self.df[feature.col_name_error] ** 2

    def mae(self, feature: Controlled) -> pd.Series:
        """ returns the mean squared error for a given feature """

        return self.df[feature.col_name_error].abs()

    def corr(self, feature1: Feature, feature2: Feature):

        return self.df[feature1.variable.col_name].corr(self.df[feature2.variable.col_name])

    def add_solving_times(self, solving_times: dict):

        self.df['solving_times'] = self.df['SimTime'].map(solving_times)

    def save(self, filename: str, folder: str = None, override: bool = False):

        directory = file_manager.data_dir(folder=folder, mkdir=True)

        write_pkl(self, filename, directory=directory, override=override)


class DataHandler:
    """ stores a list of DataContainers and has useful functions to manage them """

    def __init__(
            self,
            data:       Union[DataContainer, list[DataContainer], 'DataHandler'] = None,
    ):

        # containers
        self.containers: list[DataContainer] = list()
        self.add(data)

    def __str__(self) -> str:

        total_duration = int(sum(dc.duration for dc in self) / (60*60*24))

        return f"DataHandler({total_duration} Days in {len(self)} DataContainer's)"

    def __iter__(self):
        """ iterates over all stored DataContainer's """

        return iter(self.containers)

    def __len__(self):
        """ returns the count of DataContainers stored """

        return len(self.containers)

    def __getitem__(self, i):
        """ returns the DataContainer at position i """

        return self.containers[i]

    def __delitem__(self, i: int):
        """ removes the DataContainer at position i """

        del self.containers[i]

    def __setitem__(self, key, value):
        """ sets the DataContainer at position i """

        if isinstance(value, DataContainer):
            self.containers[key] = value

        raise ValueError('Please make sure to pass a DataContainer.')

    def __bool__(self):
        return bool(self.containers)

    @property
    def empty(self) -> bool:
        return len(self.containers) == 0

    def add(self, data: Union[DataContainer, list[DataContainer], 'DataHandler']):
        """
        Add data to the DataHandler. Allowed types are: NoneType, DataContainer, list[DataContainer] and DataHandler.
        """

        if data is None:
            return

        if isinstance(data, DataContainer):
            self.containers.append(data)

        elif isinstance(data, DataHandler):
            self.containers.extend(data.containers)

        elif all([type(i) == DataContainer for i in data]):
            self.containers.extend(data)

        else:
            raise ValueError("Please pass a list of DataContainer's, a DataContainer or a DataHandler ")

    def summary(self):

        print(f'{fmt.BOLD}DataHandler:{fmt.ENDC}')

        if len(self.containers) == 0:
            print('\tNone')
            return

        for container in self.containers:
            print(f'\t{container}')

    def clear(self):
        """
        Clears the list with the DataContainers.
        """
        del self.containers
        self.containers = list()

    def merge(self):
        """ merges DataContainers in the DataHandler together if possible """

        self.containers = DataContainer.merge(self.containers)

    def add_solving_times(self, solving_times: dict):

        for c in self.containers:
            c.add_solving_times(solving_times)

    def plot(self, plotter: Plotter):

        for dc in self:
            dc.plot(plotter)

    def save(self, filename: str, folder: str = None, override: bool = False):

        directory = file_manager.data_dir(folder=folder, mkdir=True)

        write_pkl(self, filename, directory=directory, override=override)


def to_DataHandler(data: Union[DataContainer, DataHandler, list[DataContainer]]) -> DataHandler:
    """ converts data to a DataHandler """

    if isinstance(data, DataContainer):
        return DataHandler(data)

    if isinstance(data, DataHandler):
        return data

    if isinstance(data, list):
        return DataHandler(data)

    if data is None:
        return DataHandler(data=data)

    raise TypeError(f'Please provide a DataContainer, DataHandler or list of DataContainers not {type(data)}')


def load_DataContainer(filename: str, folder: str = None) -> DataContainer:

    directory = file_manager.data_dir(folder=folder, mkdir=False)
    dc = read_pkl(filename, directory)

    assert isinstance(dc, DataContainer), 'Wrong type loaded!'

    return dc


def load_DataHandler(filename: str, folder: str = None) -> DataHandler:

    directory = file_manager.data_dir(folder=folder, mkdir=False)

    dh = read_pkl(filename, directory)

    assert isinstance(dh, DataHandler), 'Wrong type loaded!'

    return dh
