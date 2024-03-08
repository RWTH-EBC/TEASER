import numpy as np
from sklearn import kernel_approximation
from abc import ABC, abstractmethod
from sklearn.gaussian_process.kernels import Kernel, RBF


class InducingPoints(ABC):
    """
    The idea is to reduce the effective number of input data points x to the GP
    from n to m, with m<n, where the set of m points are called inducing points.
     Since this makes the effective covariance matrix K smaller,
     many inducing point approaches reduce the computational complexity from O(n3) to O(nm2).
     The smaller m is, the bigger the speed up.

     Source: https://bwengals.github.io/inducing-point-methods-to-speed-up-gps.html
    """

    def __init__(self):

        pass

    @abstractmethod
    def reduce(
            self,
            x:                      np.ndarray,
            y:                      np.ndarray,
            plot_distance_matrix:   bool = True,
    ) -> tuple[np.ndarray, np.ndarray]:

        pass


class NystroemReducer(InducingPoints):

    def __init__(self, n_components: int, kernel: Kernel = None):

        super(NystroemReducer, self).__init__()

        if kernel is None:
            kernel = RBF()

        self.nystroem = kernel_approximation.Nystroem(kernel=kernel, n_components=n_components)

    def reduce(
            self,
            x:                      np.ndarray,
            y:                      np.ndarray,
            plot_distance_matrix:   bool = True,
    ) -> tuple[np.ndarray, np.ndarray]:

        self.nystroem.fit(x, y)

        return self.nystroem.components_, y[self.nystroem.component_indices_]


if __name__ == '__main__':

    from sklearn.gaussian_process import GaussianProcessRegressor
    import matplotlib.pyplot as plt

    n_components = 25

    def f(x):
        'some more or less complex output function'

        return x[:, 0] * 2 + x[:, 1] * x[:, 0] + x[:, 1] * 3 + 1 / x[:, 1] * x[:, 1]

    def get_score(x, y, x_test, y_test, message):

        gpr = GaussianProcessRegressor(RBF(), normalize_y=True)
        gpr.fit(x, y)
        s = gpr.score(x_test, y_test)

        print(message, s, 'samples:', x.shape, y.shape)

        return s

    scores = list()

    for i in range(2):

        np.random.seed(i)

        x_train = np.random.normal(size=(800, 2), loc=0, scale=10)
        y_train = f(x_train)

        x_test = np.random.normal(size=(200, 2), loc=0, scale=10)
        y_test = f(x_test)

        x_red, y_red = NystroemReducer(n_components=n_components).reduce(x_train, y_train)

        score_before = get_score(x_train, y_train, x_test, y_test, 'before')
        score_after = get_score(x_red, y_red, x_test, y_test, 'after')

        plt.scatter(x_train.T[0], x_train.T[1], c=y_train)
        plt.scatter(x_red.T[0], x_red.T[1], c='black', label='reduced_data')
        plt.legend()
        plt.title(f'score_before: {round(score_before, 4)}, score_after: {round(score_after, 4)}\n n_components: {n_components}')
        plt.show()

