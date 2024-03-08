from typing import Union, Callable, Optional

from sklearn import linear_model
import casadi as ca
import numpy as np

from ddmpc.modeling.process_models.main import Predictor
from ddmpc.data_handling.processing_data import TrainingData
from ddmpc.utils import file_manager
from ddmpc.utils.pickle_handler import read_pkl
import ddmpc.utils.formatting as fmt


class LinearRegression(Predictor):

    def __init__(self):

        super(LinearRegression, self).__init__()
        self.linear_model = linear_model.LinearRegression()

    def fit(self, training_data: TrainingData):
        """ fits the Hyper-parameters to the data """

        # set new Inputs, Output and step_size
        self.inputs = training_data.inputs
        self.output = training_data.output
        self.step_size = training_data.step_size

        x_train, y_train = training_data.trainData

        self.linear_model.fit(X=x_train, y=y_train)

    def test(
            self,
            training_data: TrainingData,
            metric: Optional[Callable] = None,
            show_plot: Optional[bool] = True,
            save_plot: Optional[bool] = False,
            save_data: Optional[bool] = False,
    ) -> tuple[float, float, float, float]:
        """ tests the Hyper-parameters to the data """

        return self._test(
            train_set=training_data.trainData,
            valid_set=training_data.validData,
            test_set=training_data.testData,
            clipped_set=training_data.clippedData,
            metric=metric,
            show_plot=show_plot,
            save_plot=save_plot,
            save_data=save_data,
        )

    def predict(self, input_values: Union[list, ca.MX, ca.DM, np.ndarray]) -> Union[ca.MX, ca.DM, np.ndarray]:

        if isinstance(input_values, list):

            s = [v * c for v, c in zip(input_values, self.linear_model.coef_[0])]

            return self.linear_model.intercept_ + ca.sum1(ca.vertcat(*s))

        elif isinstance(input_values, np.ndarray):

            if input_values.ndim == 1:
                return self.linear_model.intercept_ + np.sum(input_values * self.linear_model.coef_)

            elif input_values.ndim == 2:
                return self.linear_model.intercept_ + input_values @ self.linear_model.coef_.T

            return self.linear_model.intercept_ + input_values * self.linear_model.predict(input_values)

        elif isinstance(input_values, ca.MX):

            return self.linear_model.intercept_ + input_values * self.linear_model.predict(input_values)

        else:
            raise ValueError("input_values has to be either a list, np.ndarray or ca.MX")

    def print_coefficients(self):

        print('Coefficients for the Linear Regression:')

        table = list()

        total_i = 0
        for f in self.inputs:

            table.append([])
            cum_sum = 0
            table.append(['\t', f.variable.name, 'i   ', 'lag ', 'cum_sum'])

            for i in range(0, f.lag):
                val = self.linear_model.coef_[0][total_i]
                cum_sum += val
                table.append(['\t', '', total_i, i, '{0:+4f}'.format(val), '{0:+4f}'.format(cum_sum)])
                total_i += 1

        fmt.print_table(table)


def load_LinearRegression(filename: str, folder: str = None) -> LinearRegression:

    lr = read_pkl(filename, file_manager.predictors_dir(folder=folder))

    assert isinstance(lr, LinearRegression), 'Wrong type loaded!'

    return lr

