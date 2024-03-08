import numpy as np

from pyod.models.abod import ABOD
from pyod.models.ocsvm import OCSVM
from pyod.models.iforest import IForest
from pyod.models.mcd import MCD
from pyod.models.knn import KNN

from sklearn.neighbors import KernelDensity
from sklearn.mixture import GaussianMixture
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from sklearn.exceptions import ConvergenceWarning
from sklearn.utils._testing import ignore_warnings


class Detector:

    def __init__(self):
        self.min = None
        self.max = None
        self.clf = None

    def train_percentage(self, x_train, train_error, percentage):
        x_train_c = x_train.copy()
        train_error_c = train_error.copy()

        train_error_c = train_error_c.reshape(len(train_error_c), 1)
        data = np.concatenate([train_error_c, x_train_c], axis=1)
        data = data[data[:, 0].argsort()]
        length = len(data)
        x_train_c = data[:int(percentage * length), 1:]
        self.train(x_train_c)

    def train(self, x_train):
        x_train_c = x_train.copy()

        x_train_c = self.norm(x_train_c, init=True)

        self.clf.fit(x_train_c)

    def norm(self, x_t, init=False):
        x_t_c = x_t.copy()
        x_t_n = np.zeros(x_t_c.shape)
        nc = len(x_t_c[0])
        if init:
            self.min = np.zeros(nc)
            self.max = np.zeros(nc)
        for c in range(0, nc):
            if init:
                self.min[c] = np.amin(x_t_c[:, c])
                self.max[c] = np.amax(x_t_c[:, c])
            x_t_n[:, c] = (x_t_c[:, c] - self.min[c]) / (self.max[c] - self.min[c])
        # x_test_c[:,1] = x_test_c[:,1] * 10
        return x_t_n

    def predict(self, x_test):
        scores = self.score(x_test)
        classification = np.zeros(len(x_test))
        classification[scores > self.threshold] = 1
        return classification

    def score(self, x_test):
        x_test_c = self.norm(x_test)
        return self.clf.decision_function(x_test_c)

    def get_decision_scores(self):
        return self.clf.decision_scores_

    @property
    def threshold(self):
        return self.threshold

    @threshold.setter
    def threshold(self, threshold):
        self.threshold = threshold

    @property
    def info(self) -> dict:
        return {}


class D_OCSVM(Detector):
    def __init__(self, contamination=0.01, nu=0.15, kernel='rbf', gamma=10):
        super(D_OCSVM).__init__()
        self.nu = nu
        self.kernel = kernel
        self.gamma = gamma
        self.contamination = contamination
        self.clf = OCSVM(nu=self.nu, kernel=self.kernel, gamma=self.gamma, contamination=contamination)

    @property
    def info(self) -> dict:
        return {'Gamma': self.gamma, 'NoveltyThreshold': self.threshold}


class D_IF(Detector):
    def __init__(self, contamination=0.01, random_state=None):
        super(D_IF).__init__()
        self.contamination = contamination
        if random_state is not None:
            self.random_state = random_state
            self.clf = IForest(contamination=contamination, random_state=random_state)
        else:
            self.clf = IForest(contamination=contamination)

    @property
    def info(self) -> dict:
        return {'Seed': self.clf.random_state, 'NoveltyThreshold': self.threshold}


class D_MCD(Detector):
    def __init__(self, contamination=0.01):
        super(D_MCD).__init__()
        self.contamination = contamination
        self.clf = MCD(contamination=contamination)


class D_KNN(Detector):
    def __init__(self, contamination=0.01, n_neighbors=5, method='largest', p=2):
        super(D_KNN).__init__()
        self.contamination = contamination
        self.n_neighbors = n_neighbors
        self.method = method
        self.p = p
        self.clf = KNN(contamination=contamination, n_neighbors=n_neighbors, method=method, p=p)

    @property
    def info(self) -> dict:
        return {'K': self.n_neighbors, 'p': self.p, 'Method': self.method, 'NoveltyThreshold': self.threshold}


class D_ABOD(Detector):
    def __init__(self, contamination=0.01, n_neigbors=5):
        super(D_ABOD).__init__()
        self.contamination = contamination
        self.n_neigbors = n_neigbors
        self.clf = ABOD(contamination=contamination, n_neighbors=n_neigbors)

    def score(self, x_test):
        scores = super().score(x_test)
        return -np.log(scores * -1)

    def get_decision_scores(self):
        return -np.log(self.clf.decision_scores_ * -1)


class Detector_SKLearn(Detector):

    def __init__(self):
        super(Detector_SKLearn).__init__()
        self.decision_scores_ = None
        self.x_train_UnNormalized = None

    def train(self, x_train):
        self.x_train_UnNormalized = x_train
        super().train(x_train)

    def get_decision_scores(self):
        if self.decision_scores_ is None:
            self.decision_scores_ = self.score(self.x_train_UnNormalized)
        return self.decision_scores_

    def score(self, x_test):
        x_test_c = self.norm(x_test)
        return self.clf.score_samples(x_test_c)

    def fit(self, x_train):
        self.train(x_train)

    def decision_function(self, x_test):
        return self.score(x_test)


class D_ParzenWindow(Detector_SKLearn):
    def __init__(self, contamination=0.01, bandwith=0.1, kernel='gaussian'):
        super(D_ParzenWindow).__init__()
        self.bandwith = bandwith
        self.kernel = kernel
        self.contamination = contamination
        self.decision_scores_ = None
        self.clf = KernelDensity(kernel=kernel, bandwidth=bandwith)

    def score(self, x_test):
        scores = super().score(x_test)
        return -np.exp(scores)

    @property
    def info(self) -> dict:
        return {'Bandwith': self.bandwith, 'NoveltyThreshold': self.threshold}


class D_GGM(Detector_SKLearn):
    def __init__(self, contamination=0.01, n_components=5):
        super(D_GGM).__init__()
        self.n_components = n_components
        self.contamination = contamination
        self.decision_scores_ = None
        self.clf = GaussianMixture(n_components=n_components)

    def score(self, x_test):
        scores = super().score(x_test)
        return -np.exp(scores)


class NoveltyDetectionGPR(GaussianProcessRegressor):

    @ignore_warnings(category=ConvergenceWarning)
    def fit(self, x_train):
        y_train = np.ones((x_train.shape[0], 1))
        super().fit(x_train, y_train)


class D_GP(Detector):

    def __init__(self, contamination=0.01, kernel=1.0 * RBF(length_scale=1.0, length_scale_bounds=(1e-1, 10.0))):
        super(D_GP).__init__()
        self.contamination = contamination
        self.decision_scores_ = None
        self.kernel = kernel
        self.clf = NoveltyDetectionGPR(kernel=kernel, random_state=0)
        self.x_train_UnNormalized = None

    def train(self, x_train):
        self.x_train_UnNormalized = x_train
        super().train(x_train)

    def get_decision_scores(self):
        if self.decision_scores_ is None:
            self.decision_scores_ = self.score(self.x_train_UnNormalized)
        return self.decision_scores_

    def score(self, x_test):
        x_test_c = self.norm(x_test)
        y_mean, y_std = self.clf.predict(x_test_c, return_std=True)
        return y_std

    def fit(self, x_train):
        self.train(x_train)

    def decision_function(self, x_test):
        return self.score(x_test)

    @property
    def info(self) -> dict:
        return {'LengthScale': self.clf.kernel.k2.length_scale, 'NoveltyThreshold': self.threshold}


class D_None(Detector):

    def __init__(self):
        super(D_None).__init__()
        self.decision_scores_ = None
        self.threshold = 0

    def train_percentage(self, x_train, train_error, percentage):
        self.train(x_train)

    def train(self, x_train):
        self.decision_scores_ = -1 * np.ones(len(x_train))

    def norm(self, x_t, init=False):
        return

    def predict(self, x_test):
        classification = np.zeros(len(x_test))
        return classification

    def score(self, x_test):
        scores = -1 * np.ones(len(x_test))
        return scores

    def get_decision_scores(self):
        return self.decision_scores_
