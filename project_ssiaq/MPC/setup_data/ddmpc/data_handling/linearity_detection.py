import math

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.ticker as plticker
#
from ddmpc.data_handling.storing_data import *
from ddmpc.modeling.variables.features import *


def _features_to_sources(inputs):

    res = list()

    for inp in inputs:
        if isinstance(inp, Feature):
            res.append(inp.variable)
        else:
            res.append(inp)

    return res


def generate_changes(inputs: list[Union[Feature, Variable]]) -> list[Variable]:
    return [Change(inp) for inp in inputs]


def generate_running_means(inputs: list[Union[Feature, Variable]], n_start=2, n_stop=10) -> list[Variable]:

    res = list()

    for inp in inputs:

        for i in range(n_start, n_stop):

            rm = RunningMean(
                base=inp,
                n=i,
            )
            res.append(rm)

    return res


def generate_running_shifts(inputs: list[Union[Feature, Variable]], n_start=2, n_stop=10) -> list[Variable]:

    res = list()

    for inp in inputs:

        for i in range(n_start, n_stop):

            rm = Shift(
                base=inp,
                n=i,
            )
            res.append(rm)

    return res


class LinearityDetector:

    def __init__(self, data, output: Feature):

        self.data: DataHandler = to_DataHandler(data)

        if isinstance(output, Feature):
            output = output.variable

        self.output: Variable = output

    def _generate_columns(self, inputs: list[Union[Feature, Variable]]):

        import warnings

        warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

        data_handler = DataHandler()

        for dc in self.data.containers:

            df = dc.df

            for f in inputs:

                if not isinstance(f, Constructed):
                    continue

                if f.col_name in df.columns:
                    continue

                f.process(df)

            data_handler.add(dc)

        return data_handler

    def eval(self, inputs: list[Union[Feature, Variable]], plot: bool = False) -> pd.Series:

        inputs: list[Variable] = _features_to_sources(inputs)

        data = self._generate_columns(inputs)

        res: dict[Variable, float] = dict()

        for i in inputs:
            scores = list()

            for dc in data:

                input_col = dc.df[i.col_name]
                output_col = dc.df[self.output.col_name].shift(-1)

                correlation = output_col.corr(input_col)

                # print(f'{i.name} x {self.output.name} = {correlation}, {type(correlation)}')
                if not math.isnan(correlation):
                    scores.append(correlation)

                if plot:
                    plt.title(i.__str__())
                    plt.scatter(input_col, output_col)

                    df = pd.concat((input_col, output_col), axis=1)
                    df.dropna(inplace=True)

                    z = np.polyfit(df[input_col.name], df[output_col.name], 1)
                    p = np.poly1d(z)
                    plt.plot(input_col, p(input_col), "r--")

                    plt.show()

            # scores = [score for score in scores if isinstance(score)]
            res[i] = sum(scores) / len(scores)

        return pd.Series(res)

    def plot_correlation(
            self,
            features,
            labels,
            step_size: int,
            vmin: float,
            vmax: float,
            mark_highest: bool = False,
            title: str = None,
            save: bool = False,
            filepath: str = None,
    ):

        data = np.array([self.eval(inputs=i).values for i in features])


        # Normalize array by rows
        """
        row_mins = data.min(axis=1)
        row_maxes = data.max(axis=1)
        row_range = row_maxes - row_mins
        data = (data - row_mins[:, np.newaxis]) / row_range[:, np.newaxis]
        """

        # mask max value of every row
        if mark_highest:
            maxes = np.apply_along_axis(max, axis=1, arr=data)
            mask = np.isin(data, maxes)
            data = np.ma.masked_where(mask, data)

        fig, ax = plt.subplots(figsize=(4, len(labels) * 0.4))

        ax.set_yticks(np.arange(len(labels)), labels=labels)
        ax.set_xticks(
            np.arange(len(data[0])),
            labels=[f'{int((n + 1) * step_size / (60 * 60))}h'for n in range(len(data[0]))],
        )

        loc = plticker.MultipleLocator(base=int(60 * 60 / step_size))
        ax.xaxis.set_major_locator(loc)

        cmap = LinearSegmentedColormap.from_list(name='cmap', colors=[fmt.blue, fmt.white, fmt.red])
        cmap.set_bad(color=fmt.black)
        plt.imshow(
            data,
            cmap=cmap,
            interpolation='nearest',
            aspect='auto',
            vmin=vmin,
            vmax=vmax,
        )
        plt.colorbar()
        if title:
            plt.title(title)

        fig.tight_layout()

        if save:

            if filepath is None:
                raise ValueError('You must provide a name for the plot to save it.')

            plt.savefig(filepath)

        plt.show()


