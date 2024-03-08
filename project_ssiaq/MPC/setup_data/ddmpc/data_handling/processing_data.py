""" processing_data.py: Contains methods to apply Inducing Points to Training Data. """
import copy
import random

import matplotlib.ticker as plticker
from matplotlib.colors import LinearSegmentedColormap
from scipy.spatial.distance import cdist
from sklearn.neighbors import NearestNeighbors

from ddmpc.data_handling.storing_data import *
from ddmpc.modeling.process_models.main import Inputs, Output
from ddmpc.data_handling.data_reduction import *
from ddmpc.modeling.variables.main import Constructed, Variable


class TrainingData:
    """
    Training data for supervised machine learning.
    This Class supports basic operations like shuffling, splitting and reducing the data.
    """

    def __init__(
            self,
            inputs:     Inputs,
            output:     Output,
            step_size:  int,
            raw_data:   Union[None, DataContainer, DataHandler, list[DataContainer]] = None,
    ):

        self.inputs:    Inputs = inputs
        self.output:    Output = output

        self.step_size: int = step_size

        N = inputs.totalLag

        self.xTrain:    Optional[np.ndarray] = np.empty(shape=(0, N), dtype=float)
        self.yTrain:    Optional[np.ndarray] = np.empty(shape=(0, 1), dtype=float)
        self.xValid:    Optional[np.ndarray] = np.empty(shape=(0, N), dtype=float)
        self.yValid:    Optional[np.ndarray] = np.empty(shape=(0, 1), dtype=float)
        self.xTest:     Optional[np.ndarray] = np.empty(shape=(0, N), dtype=float)
        self.yTest:     Optional[np.ndarray] = np.empty(shape=(0, 1), dtype=float)

        self.xClipped:  Optional[np.ndarray] = np.empty(shape=(0, N), dtype=float)
        self.yClipped:  Optional[np.ndarray] = np.empty(shape=(0, 1), dtype=float)

        self.add(raw_data)

    def __str__(self):
        return f'{self.__class__.__name__}' \
               f'(training={self.trainSampleCount}, ' \
               f'testing={self.testSampleCount}, ' \
               f'validation={self.validSampleCount})'

    def __repr__(self):
        return f'{self.__class__.__name__}(totalSampleCount={self.totalSampleCount}, shares={self.sampleShares})'

    @property
    def trainData(self) -> tuple[np.ndarray, np.ndarray]:
        return self.xTrain, self.yTrain

    @property
    def validData(self) -> tuple[np.ndarray, np.ndarray]:
        return self.xValid, self.yValid

    @property
    def testData(self) -> tuple[np.ndarray, np.ndarray]:
        return self.xTest, self.yTest

    @property
    def clippedData(self) -> tuple[np.ndarray, np.ndarray]:
        return self.xClipped, self.yClipped

    @property
    def totalSampleCount(self) -> int:
        return self.trainSampleCount + self.validSampleCount + self.testSampleCount

    @property
    def trainSampleCount(self) -> int:
        """ returns the mpc sample count"""

        return self.xTrain.shape[0]

    @property
    def validSampleCount(self) -> int:
        """ returns the validation sample count"""

        return self.xValid.shape[0]

    @property
    def testSampleCount(self) -> int:
        """ returns the test sample count"""

        return self.xTest.shape[0]

    @property
    def sampleShares(self) -> tuple[float, float, float]:
        """ returns the mpc, validating and testing share """

        n_samples = self.totalSampleCount
        assert n_samples > 0, 'There are no samples in the mpc data.'

        return self.trainSampleCount / n_samples, self.validSampleCount / n_samples, self.testSampleCount / n_samples

    @property
    def allSamples(self) -> tuple[np.ndarray, np.ndarray]:
        """ returns all samples as a tuple of x and y """

        x = np.concatenate([self.xTrain, self.xValid, self.xTest], axis=0)
        y = np.concatenate([self.yTrain, self.yValid, self.yTest], axis=0)

        return x, y

    def add(self, raw_data: Union[DataContainer, DataHandler, list[DataContainer]]):
        """ adds raw data to the data handler """

        dh = to_DataHandler(raw_data)

        if dh.empty:
            return

        x = [self.xTrain]
        y = [self.yTrain]

        for container in dh:

            single_x, single_y = self._process(container.df)

            x.append(single_x)
            y.append(single_y)

        self.xTrain = np.concatenate(x, axis=0, dtype=float)
        self.yTrain = np.concatenate(y, axis=0, dtype=float)

    def clear(self):
        """ clears all data """

        N = self.inputs.totalLag

        self.xTrain:    Optional[np.ndarray] = np.empty(shape=(0, N), dtype=float)
        self.yTrain:    Optional[np.ndarray] = np.empty(shape=(0, 1), dtype=float)
        self.xValid:    Optional[np.ndarray] = np.empty(shape=(0, N), dtype=float)
        self.yValid:    Optional[np.ndarray] = np.empty(shape=(0, 1), dtype=float)
        self.xTest:     Optional[np.ndarray] = np.empty(shape=(0, N), dtype=float)
        self.yTest:     Optional[np.ndarray] = np.empty(shape=(0, 1), dtype=float)

    def shuffle(self, seed: int = None):
        """ shuffles all data samples while keeping the mpc, validating and testing shares """

        if seed is not None:
            np.random.seed(seed)

        # save the original sample shares
        trainShare, validShare, testShare = self.sampleShares

        # shuffle all samples
        x, y = self.allSamples
        x, y = self._shuffle(x, y)

        # split the shuffled samples back in the saved sample shares
        self.xTrain, self.yTrain, self.xValid, self.yValid, self.xTest, self.yTest =\
            self._split(x, y, trainShare, validShare, testShare)

    def split(self, trainShare: float, validShare: float, testShare: float):
        """ splits the data into the desired mpc, testing and validation split """

        x, y = self.allSamples

        self.xTrain, self.yTrain, self.xValid, self.yValid, self.xTest, self.yTest =\
            self._split(x, y, trainShare, validShare, testShare)

    def reduce(self, inducing_points: InducingPoints, only_training_data: bool = True, inplace: bool = True):
        """ reduces the data to the desired inducing points while keeping the sample shares """

        if only_training_data:
            xTrain, yTrain = inducing_points.reduce(self.xTrain, self.yTrain)
            xValid, yValid = self.validData
            xTest, yTest = self.testData

        else:

            trainShare, validShare, testShare = self.sampleShares

            x, y = self.allSamples
            x, y = inducing_points.reduce(x, y)

            xTrain, yTrain, xValid, yValid, xTest, yTest = self._split(x, y, trainShare, validShare, testShare)

        if inplace:

            self.xTrain, self.yTrain, self.xValid, self.yValid, self.xTest, self.yTest = \
                xTrain, yTrain, xValid, yValid, xTest, yTest

            return self

        else:
            copy_of_self = copy.copy(self)

            copy_of_self.xTrain, copy_of_self.yTrain, copy_of_self.xValid, copy_of_self.yValid, copy_of_self.xTest, copy_of_self.yTest = \
                xTrain, yTrain, xValid, yValid, xTest, yTest

            return copy_of_self

    def hopkins_statistic(self):

        def hopkins(X):

            d = X.shape[1]

            n = len(X)
            m = int(0.1 * n)
            nbrs = NearestNeighbors(n_neighbors=1).fit(X)

            rand_X = random.sample(range(0, n), m)

            ujd = []
            wjd = []
            for j in rand_X:
                u_dist, _ = nbrs.kneighbors(
                    X=np.random.uniform(np.amin(X, axis=0), np.amax(X, axis=0), d).reshape(1, -1),
                    n_neighbors=2,
                    return_distance=True,
                )
                ujd.append(u_dist[0][1])

                w_dist, _ = nbrs.kneighbors(X[j].reshape(1, -1), 2, return_distance=True)
                wjd.append(w_dist[0][1])

            H = sum(ujd) / (sum(ujd) + sum(wjd))

            if np.isnan(H):
                print(ujd, wjd)
                H = 0

            return H

        x, y = self.allSamples

        print(hopkins(x))
        print(hopkins(x))
        print(hopkins(x))
        print(hopkins(x))

        exit()

    def eval_quality(self, labels: list[str] = None, bins: int = None):

        mask = [0]
        for inp in self.inputs[:-1]:
            mask.append(mask[-1] + inp.lag)

        x, y = self.allSamples

        x_mean = np.mean(x, axis=0)
        x_std = np.std(x, axis=0)
        x_standardized = (x - x_mean) / x_std

        y_mean = np.mean(y)
        y_std = np.std(y)
        y_standardized = (y - y_mean) / y_std

        concat = np.concatenate([x_standardized[:, mask], y_standardized], axis=1)

        if labels is None:
            labels = [str(f.variable.name) for f in self.inputs]
            labels.append(self.output.variable.name)

        assert len(labels) == concat.shape[1]

        # hist
        if bins is None:
            bins = int(np.sqrt(x.shape[0]))

        bins = np.linspace(np.min(concat), np.max(concat), num=bins)

        hist = list()
        for i in mask:
            hist.append(np.histogram(x_standardized[:, i], bins=bins)[0])
        hist.append(np.histogram(y_standardized, bins=bins)[0])

        hist = np.array(hist)
        hist = (hist.T / np.max(hist, axis=1)).T
        # hist = np.sqrt(hist)

        fig, ax = plt.subplots(figsize=(5, 0.2 + 0.3 * concat.shape[1]))

        ax.set_yticks(np.arange(len(labels)), labels=labels)

        x_labels = (bins[1:] + bins[:-1]) / 2
        ax.set_xticks(np.arange(x_labels.shape[0]), x_labels.astype(int))

        ax.xaxis.set_major_locator(plticker.LinearLocator())


        cmap = LinearSegmentedColormap.from_list(name='cmap', colors=[fmt.white, fmt.grey, fmt.red])
        plt.imshow(
            X=hist,
            cmap=cmap,
            vmin=0,
            vmax=1,
            aspect='auto',
        )

        plt.colorbar(fraction=0.046, pad=0.04)
        plt.tight_layout()
        plt.show()

        fig, ax = plt.subplots(figsize=(5, 0.2 + 0.3 * concat.shape[1]))
        plt.boxplot(
            concat,
            vert=False,
            labels=labels,
            notch=False,
            # sym='.',
            whis=2,
            medianprops=dict(linestyle='-.', linewidth=2, color=fmt.red),
            boxprops=dict(linestyle=fmt.line_solid, linewidth=1, color=fmt.black),
            flierprops=dict(marker='o', markeredgecolor=fmt.red, markerfacecolor=fmt.white, markersize=2),
        )
        plt.tight_layout()
        plt.show()

    def eval(self):

        def standardize(vec: np.ndarray):
            return (vec - vec.mean()) / vec.std()

        def remove_outliers(vec: np.ndarray, m: float = 1.5):

            d = np.abs(vec - np.median(vec))
            mdev = np.median(d)
            s = d / mdev if mdev else np.zeros(shape=(len(d), ))
            return vec[s < m]

        def calc_score(vec: np.ndarray):

            vec = np.sort(vec)

            distances = vec[1:] - vec[:-1]

            n = distances.shape[0]

            # distance between two points if the space between every point is equal
            norm = np.sum(distances) / n ** 2 * n
            sq = np.sum(distances ** 2)

            with np.errstate(divide='ignore', invalid='ignore'):
                score = np.nan_to_num(norm / sq)

            return score

        x, _ = self.allSamples

        idx: int = 0
        results: list = list()
        for inp in self.inputs:

            vector = x[:, idx]

            vector = standardize(vector)
            n_before = len(vector)
            vector = remove_outliers(vector)
            n_after = len(vector)
            score = calc_score(vector)
            results.append(score)

            print(f'{inp} has a score of {score} with reduction from {n_before} to {n_after} samples.')

            idx += inp.lag

        return results

    def clip(self, lb: float, ub: float):

        train_mask = (lb < self.yTrain) & (self.yTrain < ub)
        train_mask = train_mask.flatten()

        test_mask = (lb < self.yTest) & (self.yTest < ub)
        test_mask = test_mask.flatten()

        valid_mask = (lb < self.yValid) & (self.yValid < ub)
        valid_mask = valid_mask.flatten()

        self.xClipped = np.concatenate([
            self.xTrain[np.invert(train_mask)],
            self.xTest[np.invert(test_mask)],
            self.xValid[np.invert(valid_mask)],
        ])

        self.yClipped = np.concatenate([
            self.yTrain[np.invert(train_mask)],
            self.yTest[np.invert(test_mask)],
            self.yValid[np.invert(valid_mask)],
        ])

        self.xTrain = self.xTrain[train_mask]
        self.yTrain = self.yTrain[train_mask]

        self.xTest = self.xTest[test_mask]
        self.yTest = self.yTest[test_mask]

        self.xValid = self.xValid[valid_mask]
        self.yValid = self.yValid[valid_mask]

    def remove_clipped(self):

        N = self.inputs.totalLag
        self.xClipped:  Optional[np.ndarray] = np.empty(shape=(0, N), dtype=float)
        self.yClipped:  Optional[np.ndarray] = np.empty(shape=(0, 1), dtype=float)

    @property
    def average_distance(self) -> float:

        dist_train_valid = float(np.mean(cdist(self.xTrain, self.xValid)))
        dist_train_test = float(np.mean(cdist(self.xTrain, self.xTest)))
        dist_valid_test = float(np.mean(cdist(self.xValid, self.xTest)))

        share_train_valid = self.trainSampleCount + self.validSampleCount
        share_train_test = self.trainSampleCount + self.testSampleCount
        share_valid_test = self.validSampleCount + self.testSampleCount

        total = dist_train_valid * share_train_valid + dist_train_test * share_train_test + dist_valid_test * share_valid_test

        total = total / (self.totalSampleCount * 2)

        return total

    @staticmethod
    def _split(x: np.ndarray, y: np.ndarray, trainShare: float, validShare: float, testShare:  float):
        """ splits the samples into mpc, validating and testing sets """

        assert 0.99 < trainShare + validShare + testShare < 1.01, f'Check shares {trainShare} {validShare} {testShare}'

        # calculate the sample count and shares
        N = x.shape[0]
        n_training = int(trainShare * N)
        n_validation = n_training + int(validShare * N)

        # split the data
        return \
            x[0:n_training], y[0:n_training],\
            x[n_training:n_validation], y[n_training:n_validation],\
            x[n_validation:], y[n_validation:]

    @staticmethod
    def _shuffle(x: np.ndarray, y: np.ndarray):
        """ shuffles the data samples """

        assert len(x) == len(y)
        p = np.random.permutation(len(x))

        return x[p], y[p]

    def _process(self, df: pd.DataFrame) -> tuple[np.ndarray, np.ndarray]:
        """
        Takes raw data in form of a Pandas DataFrame, processes it and
        returns the batched mpc data in the form of numpy arrays.
        """

        def create_lag(data_frame: pd.DataFrame) -> pd.DataFrame:

            ret_df = pd.DataFrame(dtype=float)

            # inputs
            for i in self.inputs:

                if i.variable.col_name not in data_frame.columns:

                    # try to construct the source if it is not included in the data_frame
                    try:
                        data_frame = i.variable.process(data_frame)
                    except AttributeError:
                        f'Please make sure {i.variable.col_name} is contained in {data_frame.columns}.'

                for k in range(0, i.lag):

                    ret_df[i.col_name(k)] = data_frame[i.variable.col_name].shift(k)

            # output
            if not self.output.variable.col_name in data_frame.columns:
                if isinstance(self.output.variable, Constructed):
                    data_frame = self.output.variable.process(data_frame.copy())

            try:
                ret_df[self.output.col_name()] = data_frame[self.output.variable.col_name].shift(-1)
            except AttributeError:
                f'Please make sure {self.output.variable.col_name} is contained in {data_frame.columns}.'

            # drop na
            ret_df = ret_df.dropna(axis=0)

            return ret_df

        def reduce_step_size(data_frame: pd.DataFrame) -> pd.DataFrame:
            return data_frame[(data_frame['SimTime'] - data_frame['SimTime'].iloc[0]) % self.step_size == 0]

        assert self.step_size % self.step_size == 0, \
            f'Make sure the step_size of the NetworkTrainer {self.step_size} ist ' \
            f'a multiple of the step_size of the FMU {self.step_size}.'

        # reduces the step size to the desired size
        df = reduce_step_size(df)

        # create all inputs
        df = create_lag(df)

        # batch
        input_col_names = [i.col_name(k) for i in self.inputs for k in range(0, i.lag)]
        output_col_name = [self.output.col_name()]

        return df[input_col_names].values.astype(dtype=float), df[output_col_name].values.astype(dtype=float)

    def summary(self):

        print('TrainingData:')
        print(f'\tInputs:           {self.inputs}')
        print(f'\tOutput:           {self.output}')
        print(f'\tTotalSamples:     {self.totalSampleCount}')
        print(f'\tshares:           {self.sampleShares}')


def delete_repetitions(
        data:                   Union[DataContainer, DataHandler, list[DataContainer]],
        bases:                  list[Union[Variable, Feature]],
        max_repetition_length:  int,
        min_data_frame_length:  int,
        value:                  float = None,
        allowed_change:         float = None,
) -> DataHandler:

    sources: list[Variable] = list()
    for base in bases:
        if isinstance(base, Feature):
            sources.append(base.variable)
        elif isinstance(base, Variable):
            sources.append(base)
        else:
            raise ValueError('Please only pass a list of Sources for Features!')

    data_containers = list()
    for data_container in to_DataHandler(data):

        # checking for sensor errors
        max_repetitions = int(max_repetition_length / data_container.step_size)
        min_rows = int(min_data_frame_length / data_container.step_size)

        col_names = [s.col_name for s in sources]

        condition = (data_container.df[col_names] == data_container.df[col_names].shift())

        if allowed_change is not None:

            c1 = data_container.df[col_names] - allowed_change <= data_container.df[col_names].shift()
            c2 = data_container.df[col_names].shift() <= data_container.df[col_names] + allowed_change
            condition = c1 & c2

        if value is not None:
            condition = (data_container.df[col_names] == value)

        repetitions = np.where(condition, 1, 0).any(axis=1)
        repetitions = np.array(repetitions).astype(int)

        for i in range(1, len(repetitions)):
            if repetitions[i]:
                repetitions[i] += repetitions[i - 1]

        data_container.df = data_container.df[repetitions <= max_repetitions]

        repetitions = [i for i in repetitions if i <= max_repetitions]

        last_idx = 0
        for idx, rep in enumerate(repetitions):
            # print('idx:', idx, 'rep:', rep, 'last_idx:', last_idx, 'max_rep:', max_repetitions)

            if rep == max_repetitions:
                # print('NEW DF:', last_idx, '-', idx - max_repetitions)
                # only append data frame if length is more than min_n
                if min_rows < (idx - max_repetitions) - last_idx:
                    data_containers.append(
                        DataContainer(data_container.df[last_idx:idx - max_repetitions])
                    )

                last_idx = idx + 1

        if min_rows < len(repetitions) - last_idx:
            data_containers.append(
                DataContainer(data_container.df[last_idx:len(repetitions)])
            )

    return DataHandler(data=data_containers)


def delete_nan(
        data:                   Union[DataContainer, DataHandler, list[DataContainer]],
        bases:                  list[Union[Variable, Feature]],
        min_data_frame_length:  int,
) -> DataHandler:

    sources: list[Variable] = list()
    for base in bases:
        if isinstance(base, Feature):
            sources.append(base.variable)
        elif isinstance(base, Variable):
            sources.append(base)
        else:
            raise ValueError('Please only pass a list of Sources for Features!')

    data_containers = list()

    for data_container in to_DataHandler(data):

        min_rows = int(min_data_frame_length / data_container.step_size)

        col_names = [f.col_name for f in sources]
        events = data_container.df[col_names].isna().any(axis=1)

        last_event = False
        last_idx = 0
        for idx, this_event in enumerate(events):

            # print('last_idx:', last_idx, 'last_event:',  last_event, 'this_event:', this_event, 'idx:', idx)

            if last_event is False and this_event is True:

                if min_rows < idx - last_idx:
                    data_containers.append(
                        DataContainer(data_container.df[last_idx:idx])
                    )

            if last_event is True and this_event is False:
                last_idx = idx + 1

            last_event = this_event

        data_containers.append(
            DataContainer(data_container.df[last_idx:])
        )

    return DataHandler(data_containers)


def delete_by_condition(
        data:                   Union[DataContainer, DataHandler, list[DataContainer]],
        conditions:             list[dict],
        connection,
        min_data_frame_length:  int,
) -> DataHandler:

    data_containers = list()
    for data_container in to_DataHandler(data):

        # checking for sensor errors
        min_rows = int(min_data_frame_length / data_container.step_size)
        df = data_container.df

        c = None

        for condition in conditions:
            left = condition['left']
            right = condition['right']
            op = condition['operator']

            if isinstance(left, Feature):
                left = left.variable

            if isinstance(right, Feature):
                right = right.variable

            if isinstance(left, Variable):
                left = df[left.col_name]

            if isinstance(right, Variable):
                left = df[right.col_name]

            if c is None:
                c = op(left, right)
            else:
                c = connection(op(left, right), c)

        repetitions = np.where(c, 1, 0)
        repetitions = np.array(repetitions).astype(int)

        for i in range(1, len(repetitions)):
            if repetitions[i]:
                repetitions[i] += repetitions[i - 1]

        data_container.df = data_container.df[repetitions <= 1]

        repetitions = [i for i in repetitions if i <= 1]

        last_idx = 0
        for idx, rep in enumerate(repetitions):
            # print('idx:', idx, 'rep:', rep, 'last_idx:', last_idx, 'max_rep:', max_repetitions)

            if rep == 1:
                # print('NEW DF:', last_idx, '-', idx - max_repetitions)
                # only append data frame if length is more than min_n
                if min_rows < (idx - 1) - last_idx:
                    data_containers.append(
                        DataContainer(data_container.df[last_idx:idx - 1])
                    )

                last_idx = idx + 1

        if min_rows < len(repetitions) - last_idx:
            data_containers.append(
                DataContainer(data_container.df[last_idx:len(repetitions)])
            )

    return DataHandler(data=data_containers)

