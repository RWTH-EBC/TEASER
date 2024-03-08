""" data_reduction.py: Contains methods to apply Inducing Points to Training Data. """

from abc import ABC, abstractmethod
import numpy as np
from typing import Callable
from ddmpc.utils.formatting import print_progress
import matplotlib.pyplot as plt


class InducingPoints(ABC):
    """
    The idea is to reduce the effective number of input data points x to the GP
    from n to m, with m<n, where the set of m points are called inducing points.
     Since this makes the effective covariance matrix K smaller,
     many inducing point approaches reduce the computational complexity from O(n3) to O(nm2).
     The smaller m is, the bigger the speed up.

     Source: https://bwengals.github.io/inducing-point-methods-to-speed-up-gps.html
    """

    def __init__(
            self,
            remaining_count: int,
    ):
        self.remaining_count = remaining_count

    def reduce(self, x: np.ndarray, y: np.ndarray, plot_distance_matrix: bool = True) -> tuple[np.ndarray, np.ndarray]:
        """ This function is called to reduce the sample size of x and y """

        assert x.shape[0] == y.shape[0]
        sample_count = x.shape[0]

        # if there are fewer samples in x and y than the remaining count, return the original data
        if self.remaining_count > sample_count:
            print('Inducing Points Error: Remaining count > Sample count!')
            return x, y

        if plot_distance_matrix:
            self.plot_distance_matrix(self.distance_matrix(x, y, normalize=True))

        # do the actual reduction
        x, y = self._reduce(x, y)

        if plot_distance_matrix:
            self.plot_distance_matrix(self.distance_matrix(x, y, normalize=True))

        # return the reduced data
        return x, y

    @abstractmethod
    def _reduce(self, x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        pass

    @staticmethod
    def argmin(_m: np.ndarray) -> tuple[int, int]:
        """ returns the indices of the two samples with the lowest distance between each other """

        pos = np.nanargmin(_m)
        N = _m.shape[0]

        _i = pos // N
        _j = pos % N

        return _i, _j

    @staticmethod
    def distance_matrix(*samples: np.ndarray, normalize: bool = False) -> np.ndarray:
        """ returns the distance matrix for all samples """

        # get all samples and combine the x and y-axis
        points = np.concatenate(samples, axis=1)

        # normalize the feature axis
        if normalize:

            if all(points.std(axis=0)):
                points = (points - points.mean(axis=0)) / points.std(axis=0)

            else:
                print(f'Reducer Error: Normalizing failed')

        from scipy.spatial.distance import cdist

        return cdist(XA=points, XB=points)

    @staticmethod
    def plot_distance_matrix(dist: np.ndarray):
        """ plots the distance matrix """

        # sort by the mean of the columns
        dist = np.sort(dist, axis=0)
        dist = np.sort(dist, axis=1)
        # dist = dist[np.nanmean(dist, axis=1).argsort(axis=0)]

        fig = plt.gcf()
        fig.set_size_inches(10, 10)

        plt.matshow(dist, fignum=1)
        plt.colorbar()
        plt.show()


class SimpleReducer(InducingPoints):
    """
    The simple reducer picks the two samples with the lowest distance to each other.
    Then calculates the minimum distance to every other sample for both points.
    The point with the lower minimum distance is removed.
    This process is repeated until the desired number of samples is reached.
    """

    def __init__(
            self,
            remaining_count: int,
            metric: Callable = np.nanmin,
            normalize: bool = False,
    ):
        super(SimpleReducer, self).__init__(
            remaining_count=remaining_count
        )
        self.metric = metric
        self.normalize = normalize

    def _reduce(self, x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

        m = self.distance_matrix(x, y, normalize=self.normalize)

        sample_count = x.shape[0]
        remove_count = sample_count - self.remaining_count

        for i in range(remove_count):

            print_progress(i, remove_count, 'Simple Reducing: ')

            i, j = self.argmin(m)

            i_score = self.metric(np.delete(m[i], j))
            j_score = self.metric(np.delete(m[j], i))

            if i_score > j_score:
                index_to_delete = j
            else:
                index_to_delete = i

            m = np.delete(m, index_to_delete, axis=0)
            m = np.delete(m, index_to_delete, axis=1)

            x = np.delete(x, index_to_delete, axis=0)
            y = np.delete(y, index_to_delete, axis=0)

        print()

        return x, y


class HeuristicReducer(InducingPoints):
    """
    Idea from:
    Porumbel, D.C., Hao, JK. & Glover, F.
    A simple and effective algorithm for the MaxMin diversity problem.
    """

    def __init__(
            self,
            remaining_count: int,
            iterations: int,
    ):

        super(HeuristicReducer, self).__init__(
            remaining_count=remaining_count
        )
        self.m = None
        self.X = None
        self.h = 0
        self.iter = dict()

        self.tabu_list = list()

        self.iterations = iterations

    def _reduce(self, x: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:

        self.m = np.ma.array(self.distance_matrix(x, y), dtype=float, mask=True)

        self._initial_guess()
        self._tabu_search()

        indices = np.where(self.X)[0]
        x, y = x[indices], y[indices]

        self.distance_matrix(x, y)

        return x, y

    def _add(self, x: int):

        self.X[x] = True

        for j, v in enumerate(np.invert(self.X)):
            if v:
                self.m.mask[x, j] = False
        self.m.mask[:, x] = True

        self.iter[x] = self.h

        self.h += 1

    def _drop(self, x: int):

        self.X[x] = False

        for j, v in enumerate(self.X):
            if v:
                self.m.mask[j, x] = False
        self.m.mask[x, :] = True

        self.h += 1

    def _max_min_distance(self) -> int:

        col_min = np.min(self.m, axis=0)
        return int(np.argmax(col_min))

    def _initial_guess(self):

        N = self.m.shape[0]
        self.X = np.zeros(shape=(N,), dtype=bool)

        for i in range(N):
            self.iter[i] = 0

        self.m.mask = False
        x = int(np.argmax(np.sum(self.m, axis=1)))
        self.m.mask = True

        self._add(x)

        self.h = 1
        while self.h < self.remaining_count:

            print_progress(self.h, self.remaining_count, 'Initial guess')

            x = self._max_min_distance()

            self._add(x)

        print()

    def _tabu_search(self):

        for i in range(self.iterations):

            print_progress(i+1, self.iterations, 'Tabu Search  ')

            drop_idx = np.random.choice(np.where(self.X)[0])
            self._drop(drop_idx)

            add_idx = self._max_min_distance()
            self._add(add_idx)

            self.tabu_list.append({'drop': drop_idx})
            self.tabu_list.append({'add': add_idx})

        print()


if __name__ == '__main__':

    import matplotlib.pyplot as plt

    np.random.seed(10)
    xtrain = np.random.normal(size=(1000, 2))
    ytrain = np.zeros(shape=(xtrain.shape[0], 1))

    hr = HeuristicReducer(remaining_count=100, iterations=1000)
    xguess, yguess = hr.reduce(xtrain, ytrain)

    plt.scatter(xtrain.T[0], xtrain.T[1], c='blue')
    plt.scatter(xguess.T[0], xguess.T[1], c='red', s=10)
    plt.show()

    sr = SimpleReducer(remaining_count=100)
    xguess, yguess = sr.reduce(xtrain, ytrain)

    plt.scatter(xtrain.T[0], xtrain.T[1], c='blue')
    plt.scatter(xguess.T[0], xguess.T[1], c='red', s=10)
    plt.show()

