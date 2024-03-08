import time
from pathlib import Path
from typing import Optional
import pandas as pd


class FileManager(str):

    def __init__(
            self,
            base_directory: str = 'stored_data',
    ):

        self.base:          str = base_directory
        self.experiment:    Optional[str] = None
        self.folder:        Optional[str] = None

    @property
    def current_time(self) -> str:
        return time.strftime("%d.%m.%Y - %Hh %Mm %Ss", time.localtime())

    @staticmethod
    def _build_path(*elements, mkdir: bool = False) -> Path:

        path = []
        for element in elements:
            if element:
                path.append(element)

        path = Path(*path)

        if not path.exists() and mkdir:
            path.mkdir(parents=True)

        return path

    @property
    def experiment_dir(self) -> Path:

        return self._build_path(self.base, self.experiment)

    def plots_dir(self, folder: str = None, mkdir: bool = False) -> Path:

        if not folder:
            folder = self.folder

        return self._build_path(self.experiment_dir, 'plots', folder, mkdir=mkdir)

    def data_dir(self, folder: str = None, mkdir: bool = False) -> Path:

        if not folder:
            folder = self.folder

        return self._build_path(self.experiment_dir, 'data', folder, mkdir=mkdir)

    def data_filepath(self, name: str, folder: str = None,  mkdir: bool = False) -> Path:

        if not folder:
            folder = self.folder

        return Path(self._build_path(self.experiment_dir, 'data', folder, mkdir=mkdir), name)

    def solution_filepath(self, folder: str = None, mkdir: bool = False) -> Path:

        return self._build_path(self.data_dir(folder), 'solutions', mkdir=mkdir)

    def predictors_dir(self, folder: str = None, mkdir: bool = False) -> Path:

        if not folder:
            folder = self.folder

        return self._build_path(self.experiment_dir, 'predictors', folder, mkdir=mkdir)

    def keras_model_filepath(self, folder: str, name: str, mkdir: bool = False) -> Path:

        if not folder:
            folder = self.folder

        return self._build_path(self.experiment_dir, 'predictors', folder, 'keras_models', name, mkdir=mkdir)

    def plot_filepath(self, name: str, folder: str = None, sub_folder: str = None, include_time: bool = False) -> Path:

        directory = self._build_path(self.plots_dir(folder, mkdir=True), sub_folder, mkdir=True)

        if include_time:
            filename = f'{self.current_time} - {name}.svg'
        else:
            filename = f'{name}.svg'

        return Path(directory, filename)

    def summary(self):

        print('FileManager:')
        print(f'\tbase:         {self.base}')
        print(f'\texperiment:   {self.experiment}')
        print(f'\tdirectories:')
        print(f'\t\texperiment_dir: {self.experiment_dir}')
        print(f'\t\tdata_dir:       {self.data_dir}')
        print(f'\t\tplots_dir:      {self.plots_dir}')
        print(f'\t\tpredictors_dir: {self.predictors_dir}')


file_manager = FileManager()
