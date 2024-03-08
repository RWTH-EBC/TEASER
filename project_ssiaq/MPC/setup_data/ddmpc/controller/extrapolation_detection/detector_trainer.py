from abc import abstractmethod, ABC

import numpy as np
import math

from ddmpc.controller.extrapolation_detection.detector import D_None
from ddmpc.controller.extrapolation_detection.hyper_opt import Hyper_Threshold, HyperOpt
from ddmpc.data_handling.processing_data import TrainingData
from ddmpc.modeling.process_models.main import Predictor


class DetectorTrainer(ABC):

    def __init__(self):
        self.clf = None

    @abstractmethod
    def train(self, training_data: TrainingData):
        pass

    @abstractmethod
    def retrain(self, training_data: TrainingData):
        pass

    @property
    def detector(self):
        return self.clf

    @abstractmethod
    def additional_info(self) -> dict:
        pass

    @property
    def info(self) -> dict:
        info = self.clf.info()
        info.update(self.additional_info())
        return info


class NoClf(DetectorTrainer):

    def __init__(self):
        super(NoClf, self).__init__()
        self.clf = D_None()

    def train(self, training_data: TrainingData):
        pass

    def retrain(self, training_data: TrainingData):
        pass

    def additional_info(self) -> dict:
        return {}


class HyperOptTrainer(DetectorTrainer, ABC):

    def __init__(self,
                 predictor: Predictor,
                 hyper_opt: HyperOpt,
                 outlier_fraction: float = 0.05,
                 update_error_threshold: bool = False,
                 error_threshold: float = None,
                 beta: float = 1):
        super(HyperOptTrainer, self).__init__()
        self.predictor = predictor
        self.hyper_opt = hyper_opt
        self.outlier_fraction = outlier_fraction
        self.hyper_threshold = Hyper_Threshold(beta=beta)
        self.update_error_threshold = update_error_threshold
        self.error_threshold = error_threshold

        self.x_train = None
        self.x_val = None
        self.groundtruth = None

    def train(self, training_data: TrainingData):
        self.rearrange_training_data(training_data)
        self.clf = self.hyper_opt.get_clf(self.x_train, self.x_val, self.groundtruth)
        self.clf.train(self.x_train)

    def retrain(self, training_data: TrainingData):
        if self.update_error_threshold:
            self.error_threshold = None
        else:
            self.outlier_fraction = None
        self.train(training_data)

    def additional_info(self) -> dict:
        return {'ErrorThreshold': self.error_threshold, 'OutlierFraction': self.outlier_fraction}

    def rearrange_training_data(self, training_data: TrainingData):
        train_errors = self.predictor.prediction_error(training_data.xTrain, training_data.yTrain, abs)
        val_errors = self.predictor.prediction_error(training_data.xValid, training_data.yValid, abs)
        test_errors = self.predictor.prediction_error(training_data.xTest, training_data.yTest, abs)

        tvt_error = np.concatenate((val_errors, test_errors, train_errors))
        if self.error_threshold is None:
            tvt_error_sorted = np.sort(tvt_error, axis=0)
            error_threshold = tvt_error_sorted[math.floor((1 - self.outlier_fraction) * len(tvt_error_sorted))]
            self.error_threshold = error_threshold
        else:
            ground_truth = np.zeros((len(tvt_error), 1))
            ground_truth[tvt_error > self.error_threshold] = 1
            self.outlier_fraction = np.sum(ground_truth) / len(tvt_error)

        self.x_train = training_data.xTrain[(train_errors <= self.error_threshold).flatten(), :]
        x_train_out = training_data.xTrain[(train_errors > self.error_threshold).flatten(), :]
        self.x_val = np.concatenate((x_train_out, training_data.xValid, training_data.xTest))

        train_errors_in = train_errors[(train_errors <= self.error_threshold).flatten()]
        train_errors_out = train_errors[(train_errors > self.error_threshold).flatten()]
        train_groundtruth = np.zeros(len(train_errors_in))
        val_errors = np.concatenate((train_errors_out, val_errors, test_errors))
        val_groundtruth = np.zeros(len(val_errors))
        val_groundtruth[(val_errors > self.error_threshold).flatten()] = 1
        self.groundtruth = np.concatenate((train_groundtruth, val_groundtruth))

