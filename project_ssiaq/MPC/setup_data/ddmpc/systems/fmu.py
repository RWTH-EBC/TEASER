from typing import Optional, Union
import shutil
import fmpy
import fmpy.fmi2
import pandas as pd
from os.path import isfile
from pathlib import Path
from ddmpc.modeling.main import Model, Readable
from ddmpc.systems.base_class import System
from ddmpc.utils.pickle_handler import write_pkl, read_pkl


class FMU(System):
    """
    This FMU class implements functionalities to interact with FMUs
    """

    def __init__(
            self,
            model:      Model,
            step_size:  int,
            name:       str,
            directory:  Path = Path('stored_data', 'FMUs'),
    ):
        """
        initialize FMU System class
        :param model:           Model Ontology
        :param step_size:       time step size of the fmu
        :param fmu_name:        name of the fmu (must match with stored name)
        :param directory:       directory where the fmu file is stored
        """

        # initialize parent class
        super().__init__(
            model=model,
            name=name,
            step_size=step_size,
        )

        # fmu instance
        self.fmu:           Optional[FMU] = None
        self.directory:     Union[Path, str] = directory

        # description and variables
        self.description:   fmpy.model_description.ModelDescription  = self._get_description()
        self.variable_dict: dict[str] = self._get_variable_dict()

        # check variables
        # self._check_variables()

        # disturbances
        self.disturbances: pd.DataFrame | None = None

        try:
            self.load_disturbances()

        except FileNotFoundError:
            self.simulate_disturbances()

    def setup(
            self,
            start_time:     int,
            instance_name:  str = 'fmu',
            sim_tolerance:  float = 0.0001,

    ):
        """
        Set up the FMU environment for a given start time
        :param start_time:  Time at which the simulation is started (in s of the year)
        :param instance_name: Name of the fmu instance
        :param sim_tolerance: Simulation tolerance
        """

        # start time
        assert start_time >= 0, 'Please make sure the start time is greater or equal to zero.'
        assert self.fmu is None, 'Please make sure the simulation was closed'

        self.time = start_time

        # create a slave
        self.fmu = fmpy.fmi2.FMU2Slave(
            guid=self.description.guid,
            unzipDirectory=fmpy.extract(self.fmu_path),
            modelIdentifier=self.description.coSimulation.modelIdentifier,
            instanceName=instance_name
        )
        self.fmu.instantiate()
        self.fmu.reset()
        self.fmu.setupExperiment(
            startTime=start_time,
            tolerance=sim_tolerance
        )
        self.fmu.enterInitializationMode()
        self.fmu.exitInitializationMode()

    def close(self):
        """ Closes the simulation and clears the fmu object """

        self.fmu.terminate()
        self.fmu.freeInstance()
        shutil.rmtree(fmpy.extract(self.fmu_path))

        del self.fmu
        self.fmu = None

        del self.last_df
        self.last_df = pd.DataFrame()

    def do_step(self):
        """ Simulates one step """

        self.fmu.doStep(
            currentCommunicationPoint=self.time,
            communicationStepSize=self.step_size
        )

        # increment system time
        self.time += self.step_size

    # -------------------- utility -------------------

    def summary(self):
        """ prints the summary of the FMU """

        fmpy.dump(str(self.fmu_path))

    def _check_variables(self):
        """ checks if the BaseVariables from the Model are really included in the fmu before running """

        for base_var in self.model.readable:

            assert base_var.read_name in self.variable_dict, \
                f'The BaseVariable {base_var} is not included in the FMU. ' \
                f'Please call summary to get an overview of all Variables.'

    # ------------ disturbances handling  ------------

    def _get_forecast(self, length: int) -> pd.DataFrame:
        """ Returns forecast for the current prediction horizon """

        return self.disturbances[
            (self.time <= self.disturbances['SimTime']) &
            (self.disturbances['SimTime'] <= (self.time + length))
            ].copy()

    @property
    def disturbances_filepath(self) -> str:
        """ The filepath where the disturbances are stored """

        return f'{self.directory}//{self.name}_disturbances_{self.step_size}.pkl'

    def load_disturbances(self):
        """ Loads the disturbances DataFrame from the disc """

        # check if the disturbances already exist.
        if isfile(self.disturbances_filepath):
            self.disturbances = read_pkl(filename=self.disturbances_filepath)
        else:
            raise FileNotFoundError(f'Disturbances missing at "{self.disturbances_filepath}".')

    def simulate_disturbances(self, start_time: int = 0, stop_time: int = 3600 * 24 * 380, controllers: list = None):
        """
        Simulates the fmu file and extracts only the disturbances from it.
        Afterwards the DataFrame is stored at self.disturbances_filepath.

        :param controllers:             Tuple with all controllers
        :param start_time:              Start of the disturbances DataFrame
        :param stop_time:               End of the disturbances DataFrame
        """

        if controllers is None:
            controllers = tuple()

        self.setup(start_time=start_time)

        try:
            df = self.run(duration=stop_time - start_time, controllers=controllers).df

        except fmpy.fmi2.FMICallException:

            print('Simulating the disturbances failed due to an FMICallException. Continuing anyway...')

            self.close()

        else:

            df = df[['SimTime'] + [d.variable.col_name for d in self.model.disturbances]]

            # save as pickle
            write_pkl(df, self.disturbances_filepath, override=True)

            # save to df
            self.disturbances = df

        finally:
            # close the fmu
            self.close()

    # ------------ internal use only ------------

    @property
    def fmu_path(self) -> Path:
        return Path(self.directory, self.name)

    def _get_description(self) -> fmpy.model_description.ModelDescription:
        """
        Read the description of the given fmu file
        :return: model_description
        """

        # open fmu file
        if self.fmu_path.is_file():
            file = open(self.fmu_path)

        else:
            raise AttributeError(f'FMU file with path "{self.fmu_path}" does not exist.')

        # read model description
        model_description = fmpy.read_model_description(self.fmu_path.as_posix())

        # close fmu file
        file.close()

        # return model  description
        return model_description

    def _get_variable_dict(self) -> dict:
        """
        Returns a dict with all variables included in the fmu.
        """

        assert self.description is not None, 'Please make sure to read model description first.'

        # collect all variables
        variables = dict()
        for variable in self.description.modelVariables:
            variables[variable.name] = variable

        return variables

    # ------------ fmu interaction ------------

    def read_values(self) -> dict:
        """ Reads current variable values and returns them as a dict """

        res = dict()
        for var_name in self._readable_columns:
            res[var_name] = self._read_value(var_name)

        # add current time to results
        res['SimTime'] = self.time
        return res

    def _read_value(self, var_name: str):
        """
        Read a single variable.
        """

        variable = self.variable_dict[var_name]
        vr = [variable.valueReference]

        if variable.type == 'Real':
            return self.fmu.getReal(vr)[0]
        elif variable.type in ['Integer', 'Enumeration']:
            return self.fmu.getInteger(vr)[0]
        elif variable.type == 'Boolean':
            value = self.fmu.getBoolean(vr)[0]
            return value != 0
        else:
            raise Exception("Unsupported type: %s" % variable.type)

    def write_values(self, control_dict: dict):
        """
        Writes Values of control dict to fmu
        :param control_dict:
        :return:
        """
        if control_dict:
            for var_name, value in control_dict.items():
                self._write_value(var_name, value)
        else:
            self._write_default_controls()

    def _write_value(self, var_name: str, value):
        """
        Write a single control value
        :param var_name: Name of the variable to write
        :param value:  value to be written
        :return:
        """

        variable = self.variable_dict[var_name]
        vr = [variable.valueReference]

        if variable.type == 'Real':
            self.fmu.setReal(vr, [float(value)])
        elif variable.type in ['Integer', 'Enumeration']:
            self.fmu.setInteger(vr, [int(value)])
        elif variable.type == 'Boolean':
            self.fmu.setBoolean(vr, [value == 1.0 or value == True or value == "True"])
        else:
            raise Exception("Unsupported type: %s" % variable.type)
