import math
from typing import Callable, Optional

import numpy as np
import casadi as ca
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, RBF, WhiteKernel

from ddmpc.modeling.process_models.main import Predictor
from ddmpc.utils.pickle_handler import *
from ddmpc.data_handling.processing_data import TrainingData
from ddmpc.utils.file_manager import file_manager
from ddmpc.data_handling.reduction import InducingPoints


class GaussianProcess(Predictor):
    """ Gaussian Process Regression using casadi Functions """

    constant_value_bounds:  tuple = (1e-4, 1e5)
    length_scale_bounds:    tuple = (1e-4, 1e5)
    noise_level_bounds:     tuple = (1e-4, 1e5)
    noise_level:            float = 1.0

    def __init__(
            self,
            normalize:  bool = True,
    ):

        super(GaussianProcess, self).__init__()

        # data
        self.x_train = None
        self.y_train = None

        # normalization
        self.normalize = normalize
        self.mean = None
        self.std = None

        # hyper parameters
        self.alpha = None
        self.constant_value = None
        self.length_scale = None
        self.theta = None

    def fit(self, training_data: TrainingData):
        """ fits the Hyper-parameters to the data """

        # set new Inputs, Output and step_size
        self.inputs = training_data.inputs
        self.output = training_data.output
        self.step_size = training_data.step_size

        x_train = training_data.xTrain
        y_train = training_data.yTrain

        x_train = self._normalize(x_train, update=True)

        kernel = \
            ConstantKernel(constant_value_bounds=self.constant_value_bounds) * \
            RBF(length_scale_bounds=self.length_scale_bounds) + \
            WhiteKernel(noise_level=self.noise_level, noise_level_bounds=self.noise_level_bounds)

        # use sklearn gaussian process regression
        gpr = GaussianProcessRegressor(
            kernel=kernel,
            copy_X_train=False,
        )
        gpr.fit(X=x_train, y=training_data.yTrain)

        # save the data
        self.x_train = x_train
        self.y_train = y_train

        # extract hyper parameters
        self.alpha = gpr.alpha_
        self.constant_value = gpr.kernel_.k1.k1.constant_value
        self.length_scale = gpr.kernel_.k1.k2.length_scale
        self.theta = gpr.kernel_.k2.theta

    def test(
            self,
            training_data: TrainingData,
            metric: Optional[Callable] = None,
            show_plot: Optional[bool] = True,
            save_plot: Optional[bool] = False,
            save_data: Optional[bool] = False,
    ):
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

    def predict(self, x: Union[list, ca.MX, ca.DM, np.ndarray]) -> ca.MX:
        """
        Return a prediction on the given input x using casadi.

        shape(x) = (n_samples, n_features)
        """

        if isinstance(x, list):
            x = ca.vertcat(*x).T

        x = self._normalize(x)
        k_star = self._kernel(x)

        if isinstance(x, ca.MX):
            f_mean = ca.mtimes(k_star.T, self.alpha)

        else:
            f_mean = np.matmul(k_star.T, self.alpha, dtype=float)

        return f_mean

    def std(self, x: Union[ca.MX, np.ndarray]) -> ca.MX:

        assert x.shape[0] == 1

        x = self._normalize(x)

        x_train = self.x_train
        x_test = x

        K = self._kernel(x_train, x_train)
        K_s = self._kernel(x_test, x_train)
        K_ss = self._kernel(x_test, x_test)

        L = np.linalg.cholesky(K + 0.0000001 * np.eye(len(x_train)))
        Lk = np.linalg.solve(L, K_s)

        var = np.diag(K_ss) - np.sum(Lk ** 2, axis=0)

        return ca.sqrt(var)

    @staticmethod
    def reset_bounds():

        GaussianProcess.constant_value_bounds = (1e-5, 1e5)
        GaussianProcess.length_scale_bounds = (1e-5, 1e5)
        GaussianProcess.noise_level_bounds = (1e-5, 1e5)

    def _square_distance(self, x_test: Union[ca.MX, np.ndarray], x_train: Union[ca.MX, np.ndarray] = None):
        """
        Calculates the square distance from x_train to x_test.

        shape(x_test)  = (n_test_samples, n_features)
        shape(x_train) = (n_train_samples, n_features)
        """

        if x_train is None:
            x_train = self.x_train

        self._check_shapes(x_test, x_train)

        if x_test.shape[0] == 1:
            a = ca.sum2(x_test**2)
        else:
            a = np.sum(x_test ** 2, axis=1, dtype=float)

        b = np.sum(x_train ** 2, axis=1, dtype=float).reshape(-1, 1)

        if isinstance(x_test, ca.MX):
            c = - 2 * ca.mtimes(x_train, x_test.T)

        else:
            c = - 2 * np.matmul(x_train, x_test.T, dtype=float)

        return a + b + c

    def _kernel(self, x_test: Union[ca.MX, np.ndarray], x_train: Union[ca.MX, np.ndarray] = None) -> ca.MX:
        """
        Calculates the kernel with regard to mpc and testing data.
        If x_train is None the internal mpc data is used.

        shape(x_test)  = (n_samples, n_features)
        shape(x_train) = (n_samples, n_features)
        """

        square_distance = self._square_distance(x_test, x_train)

        return np.exp((- square_distance / (2 * self.length_scale ** 2))) * self.constant_value

    def _check_shapes(self, x_test: Union[ca.MX, np.ndarray], x_train: Union[ca.MX, np.ndarray]):

        if x_train is not None:
            assert x_test.shape[1] == x_train.shape[1],\
                f'The shape of x_test {x_test.shape}[1] and x_train {x_train.shape}[1] must match.'
        else:
            assert x_test.shape[1] == self.x_train.shape[1]

    def _normalize(self, x, update: bool = False):

        # do nothing if x should not be normalized
        if not self.normalize:
            return x

        # update the normal and the mean if update is True
        if update:
            self.mean = x.mean(axis=0, dtype=float)
            self.std = x.std(axis=0, dtype=float)

            for idx, val in enumerate(self.std):
                if val == 0:
                    print('Encountered zero while normalizing. Continuing with a std of one for this Input.')
                    self.std[idx] = 1.0

        assert self.mean is not None or self.std is None, 'Please update std and mean.'

        if isinstance(x, ca.MX):
            return (x - ca.DM(self.mean).T) / ca.DM(self.std).T

        # normalize x and return
        return (x - self.mean) / self.std

    @staticmethod
    def find_best_GPR(
            training_data:  TrainingData,
            iterations:     int = 100,
            normalize:      bool = False,
            reducer:        InducingPoints = None,
    ):
        """ to overcome randomness in the mpc process this function trains multiple GPR Models to the data """

        if training_data.validSampleCount > 0:
            print('The training data contains no validation data. For GaussianProcess only Train & Test data is required!')

        if training_data.testSampleCount == 0:
            raise ValueError('The training data contains no test data.')

        best_score = math.inf
        best_idx = 0
        best_gp = None

        for i in range(iterations):

            training_data.shuffle()
            if reducer:
                training_data = training_data.reduce(inducing_points=reducer, inplace=False)

            gp = GaussianProcess(normalize=normalize)
            gp.fit(training_data=training_data)
            score = gp.test(training_data=training_data, show_plot=False, save_plot=False)
            score = score[2] * 0.5 + score[3] * 0.5

            if score < best_score:
                best_score = score
                best_idx = i
                best_gp = gp

            print(f'\rnew best score: {best_score.__round__(6)} on iteration {best_idx+1} | {i+1} / {iterations}', end='', )

        print()

        return best_gp

    def print_coefficients(self):

        print('GaussianProcess:')
        print(f'\tConstant Value:   {self.constant_value}')
        print(f'\tLength Scale:     {self.length_scale}')
        print(f'\tTheta:            {self.theta}')


def load_GaussianProcess(filename: str, folder: str = None) -> GaussianProcess:

    directory = file_manager.predictors_dir(folder=folder)

    gp = read_pkl(filename, directory=directory)
    assert isinstance(gp, GaussianProcess), 'Wrong type loaded!'
    return gp
