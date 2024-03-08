""" mpc.py: Model Predictive Controller, Objectives and Constraints"""
import datetime
import time
import os
import glob

from ddmpc.controller.conventional import Controller
from ddmpc.modeling import *
from ddmpc.controller.model_predictive.nlp import NLP, NLPSolution
from ddmpc.utils.file_manager import file_manager
from ddmpc.utils.pickle_handler import read_pkl, write_pkl


class ModelPredictive(Controller):
    """ model predictive controller that can handel multiple Objective's, Constraint's and Predictor's """

    def __init__(
            self,
            nlp:                NLP,
            step_size:          int,
            forecast_callback:  Callable,
            solution_plotter:   Optional[Plotter] = None,
            show_solution_plot: bool = False,
            save_solution_plot: bool = True,
            save_solution_data: bool = True,
    ):
        """ Model Predictive Controller """

        super(ModelPredictive, self).__init__(step_size=step_size)

        self.nlp:                   NLP = nlp
        self._forecast_callback:    Callable = forecast_callback

        self._solution_plotter:     Plotter = solution_plotter

        self.show_solution_plot: bool = show_solution_plot
        self.save_solution_plot: bool = save_solution_plot
        self.save_solution_data: bool = save_solution_data

    def __str__(self):
        return f'ModelPredictive()'

    def __call__(self, past: pd.DataFrame) -> tuple[dict, dict]:

        if len(past) <= self.nlp.max_lag:
            return {}, {}

        current_time = past['SimTime'].iloc[-1]

        # get the forecast and past data
        forecast = self._forecast_callback(length=60*60*24*8)

        # solve the nlp
        par_vals: list[float] = self._get_par_vals(past, forecast, current_time)
        solution: NLPSolution = self.nlp.solve(par_vals)

        # retrieve the optimal controls
        controls: dict[str, float] = solution.optimal_controls

        additional_info: dict[str, float] = {'success': solution.success, 'runtime': solution.runtime}

        # append the solution to the solutions and save them to the disc
        self._save_solution(solution.df, current_time)

        # plot the solution
        self._plot_solution(solution.df, current_time)

        return controls, additional_info

    def _plot_solution(self, df: pd.DataFrame, current_time: int):

        if self._solution_plotter is None:
            return

        # add the SimTime column to the DataFrame
        df['SimTime'] = current_time + df.index * self.step_size

        self._solution_plotter.plot(
            df,
            save_plot=self.save_solution_plot,
            show_plot=self.show_solution_plot,
            current_time=current_time,
            filepath=file_manager.plot_filepath(name='mpc_solution', sub_folder='solutions', include_time=True)
        )

    def _get_par_vals(self, past: pd.DataFrame, forecast: pd.DataFrame, current_time: int) -> list[float]:
        """ calculates the input list for the nlp """

        par_vars = list()

        # iterate over all par vars
        for nlp_var in self.nlp._par_vars:

            t = current_time + self.step_size * nlp_var.k

            # if k <= 0 use the past DataFrame
            if nlp_var.k <= 0:
                value = past.loc[past['SimTime'] == t, nlp_var.col_name].values

                if len(value) != 1:
                    print(f'Error occurred while getting par var {nlp_var}')
                    print('k =', nlp_var.k)
                    print('SimTime =', int(t), datetime.datetime.fromtimestamp(t))
                    print('current_time=', int(current_time), datetime.datetime.fromtimestamp(current_time))
                    print(nlp_var.col_name)

                    past['t'] = past['SimTime'].apply(func=datetime.datetime.fromtimestamp)
                    pd.set_option('display.float_format', lambda x: '%.2f' % x)

                    print(past.tail(n=self.nlp.max_lag).to_string())

                    raise ValueError('Error occurred, while getting par vars')

            # if k > 0 use the forecast DataFrame
            else:

                if nlp_var.col_name not in forecast.columns:
                    forecast = nlp_var.feature.variable.process(forecast)

                try:
                    value = forecast.loc[forecast['SimTime'] == t, nlp_var.col_name].values
                    assert len(value) == 1,\
                        f'{nlp_var} with col_name={nlp_var.col_name} at t={t} was not found in: \n {forecast.to_string()}'

                except KeyError:
                    raise KeyError(f'{nlp_var} with col_name={nlp_var.col_name} was not found in {forecast.columns}.')

            assert len(value) == 1
            assert value[0] is not None
            assert value[0] != np.nan, f'Detected nan for {nlp_var}'

            par_vars.append(float(value))

        return par_vars

    def _save_solution(self, df: pd.DataFrame, current_time: int):

        if not self.save_solution_data:
            return

        filename: str = 'solutions_0'
        directory: str = file_manager.data_dir()

        counter = 0
        filesize = 0
        # read old solutions and generate new file, if filesize is bigger than threshold
        try:
            for solution_file in glob.glob('solutions_*.pkl',root_dir=directory):
                filename =solution_file
                filesize = os.path.getsize(directory.joinpath(filename))
                counter += 1
            if filesize < 20000000: # filesize in bytes
                solutions = read_pkl(filename=filename, directory=directory)
            else:
                filename = 'solutions_'+str(counter)
                solutions = dict()
        except (FileNotFoundError, EOFError):
            solutions = dict()

        # add the SimTime column to the DataFrame
        df['SimTime'] = current_time + df.index * self.step_size
        solutions[current_time] = df

        # save solutions
        write_pkl(solutions, filename=filename, directory=directory, override=True)

