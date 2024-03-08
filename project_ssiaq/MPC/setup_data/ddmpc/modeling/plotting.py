import locale
import math
import datetime
from typing import Optional, Iterator, Callable

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as dates
from matplotlib import colors
from matplotlib.axes._axes import _log
import numpy as np
import pandas as pd
from matplotlib.ticker import FuncFormatter

from ddmpc.utils.time import *
import ddmpc.utils.formatting as fmt
from ddmpc.modeling.variables.features import Feature, Controlled, Constructed

_log.setLevel('ERROR')


class SubPlot:
    """ A SubPlot takes a tuple of sources """

    def __init__(
            self,
            features:           list[Feature],
            y_label:            Optional[str] = None,
            y_label_right:      Optional[str] = None,
            legend:             Optional[bool] = True,
            legend_col:         int = 1,
            step:               Optional[bool] = False,
            where:              Optional[str] = 'post',
            unit_format_left:   Optional[tuple[str, str]] = None,
            unit_format_right:  Optional[tuple[str, str]] = None,
            lb:                 Optional[float] = None,
            ub:                 Optional[float] = None,
            factor:             Optional[float] = 1,
            shift:              Optional[float] = 0,
            normalize:          Optional[bool] = False,
            rolling:            Optional[int] = False,
            grid:               Optional[bool] = False,
            ratio:              Optional[float] = 1,
    ):

        self.features:      list[Feature] = features

        if unit_format_right or y_label_right or any([f.variable.plt_opts.second_axis for f in self.features]):
            self.enable_right_axis = True
        else:
            self.enable_right_axis = False

        self.y_label_left:  str = y_label
        self.y_label_right: str = y_label_right

        self.unit_format_left: Optional[Callable] = unit_format_left
        if unit_format_left:
            def format_left(x, pos):
                unit, str_f = unit_format_left
                return f'{str_f.format(x)} {unit}'

            self.unit_format_left: Callable = format_left

        self.unit_format_right: Optional[Callable] = unit_format_right
        if unit_format_right:
            def format_right(x, pos):
                unit, str_f = unit_format_right
                return f'{str_f.format(x)} {unit}'

            self.unit_format_right: Callable = format_right

        self.legend:        bool = legend
        self.legend_col:    int = legend_col
        self.step:          int = step
        self.where:         str = where
        self.lb:            float = lb
        self.ub:            float = ub

        self.factor:        float = factor
        self.shift:         float = shift
        self.normalize:     float = normalize
        self.rolling:       int = rolling
        self.grid:          bool = grid
        self.ratio:         float = ratio

    def convert(self, values: pd.Series):

        if self.normalize:
            values = (values - values.min()) / (values.max() - values.min())

        values = values * self.factor - self.shift

        if self.rolling:
            values = values.rolling(window=self.rolling, center=True).mean()

        return values

    def __str__(self):
        return f"SubPlot(features={self.features}, y_label={self.y_label_left})"

    def __repr__(self):
        return f"SubPlot(features={self.features}, y_label={self.y_label_left})"

    def __len__(self):
        return len(self.features)


class Plotter:
    """
    This class is used to plot the simulated data.
    The SubPlots are stacked vertically.
    """

    scale_y = 1.1
    scale_x = 1.3

    major_locator = None
    major_formatter = None
    minor_locator = None
    minor_formatter = None

    def __init__(
            self,
            *sub_plots:         SubPlot,
            size_x:             Optional[float] = None,
            size_y:             Optional[float] = None,
            title:              Optional[str] = None,
    ):

        # SubPlots
        self.sub_plots: tuple[SubPlot] = sub_plots

        # settings
        self.size_x: float = size_x
        self.size_y: float = size_y
        self.title: Optional[str] = title

        # setup plot
        self.setup()

    def __str__(self):
        return f'Plotter'

    def __repr__(self):
        return f'Plotter'

    def __len__(self):
        return len(self.sub_plots)

    def __iter__(self) -> Iterator[SubPlot]:
        return iter(self.sub_plots)

    def plot(
            self,
            df: pd.DataFrame,
            show_plot:      bool = True,
            current_time:   int = None,
            save_plot:      bool = False,
            filepath:       str = None,
    ):

        # build plot
        self._build(df, current_time)

        # save plot
        if save_plot:

            if filepath is None:
                raise ValueError('You must provide a filepath when saving the plot')

            plt.savefig(filepath)

        # show plot
        if show_plot:
            plt.show(block=False)

        plt.clf()
        plt.close('all')

    @staticmethod
    def setup():

        locale.setlocale(locale.LC_ALL, 'deu_deu')

        matplotlib.rcParams['mathtext.fontset'] = 'custom'
        matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
        matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
        matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'

        matplotlib.rcParams['mathtext.fontset'] = 'stix'
        matplotlib.rcParams['font.family'] = 'STIXGeneral'

        matplotlib.rcParams['savefig.dpi'] = 200
        matplotlib.rcParams['figure.dpi'] = 200

    def _build(self, df: pd.DataFrame, current_time: int):

        ratios = [subplot.ratio for subplot in self.sub_plots]

        fig, axs = plt.subplots(len(self), sharex='all', gridspec_kw={'height_ratios': ratios})

        df = df.copy(deep=True).round(5)

        assert 'SimTime' in df.columns

        if self.title:
            fig.suptitle(self.title)

        # timescale
        step_size = int(df['SimTime'].iloc[1] - df['SimTime'].iloc[0])
        duration = abs(int(df['SimTime'].iloc[-1] - df['SimTime'].iloc[0]))
        start_date = datetime.datetime.fromtimestamp(int(df['SimTime'].iloc[0]))
        date_list = [start_date + datetime.timedelta(seconds=step_size) * rows for rows in range(0, len(df.index))]

        if current_time is not None:
            ct = datetime.datetime.fromtimestamp(current_time)
            for ax in axs:
                ax.axvline(x=ct, color=fmt.grey, linestyle=fmt.line_dashed)

        # iterate over all sub_plots
        for ax_left, sub_plot in zip(axs, self.sub_plots):

            ax_right = None

            if sub_plot.enable_right_axis:
                ax_right = ax_left.twinx()

            if sub_plot.y_label_left:
                ax_left.set_ylabel(sub_plot.y_label_left)

            if sub_plot.y_label_right:
                ax_right.set_ylabel(sub_plot.y_label_right)

            if sub_plot.unit_format_left:
                major_formatter = FuncFormatter(sub_plot.unit_format_left)
                ax_left.yaxis.set_major_formatter(major_formatter)
                ax_left.yaxis.set_label_coords(-0.10, 0.5)

            else:
                ax_left.yaxis.set_label_coords(-0.08, 0.5)

            if sub_plot.unit_format_right:
                major_formatter = FuncFormatter(sub_plot.unit_format_right)
                ax_right.yaxis.set_major_formatter(major_formatter)
                # set the right edge of the plot a bit to the left
                plt.subplots_adjust(right=0.88)

            if sub_plot.unit_format_left and sub_plot.unit_format_right:
                ax_left.yaxis.set_label_coords(-0.11, 0.5)

            if sub_plot.lb:
                ax_left.set_ylim(bottom=sub_plot.lb - 0.4)

            if sub_plot.ub:
                ax_left.set_ylim(top=sub_plot.ub + 0.4)

            lns = list()
            labels = list()

            # iterate over all features
            for feature in sub_plot.features:

                plt_opt = feature.variable.plt_opts

                if feature.variable.col_name not in df.columns and isinstance(feature.variable, Constructed):
                    try:
                        df = feature.variable.process(df)
                    except KeyError:
                        print(f'Could not process {feature}, continuing...')

                try:
                    values = sub_plot.convert(df[feature.variable.col_name])

                except KeyError:

                    print(f'Plotting error! Feature with col_name {feature.variable.col_name} not in df. Continuing...')
                    continue

                # second axis
                if plt_opt.second_axis:

                    _ax = ax_right
                else:
                    _ax = ax_left

                # actual plot
                if sub_plot.step:
                    plot, = _ax.step(
                        date_list,
                        values,
                        label=plt_opt.label,
                        color=plt_opt.color,
                        linestyle=plt_opt.line,
                        where=sub_plot.where,
                    )

                else:
                    plot, = _ax.plot(
                        date_list,
                        values,
                        label=plt_opt.label,
                        color=plt_opt.color,
                        linestyle=plt_opt.line,
                    )

                if plt_opt.label:
                    lns.append(plot)
                    labels.append(plt_opt.label)

                # lower and upper bound
                if isinstance(feature, Controlled):

                    if feature.col_name_lb not in df.columns:
                        continue

                    lb = sub_plot.convert(df[feature.col_name_lb])

                    _ax.step(
                        date_list,
                        lb,
                        label='',
                        color='black',
                        linestyle='-',
                        where='post',
                    )
                if isinstance(feature, Controlled):

                    if feature.col_name_ub not in df.columns:
                        continue

                    ub = sub_plot.convert(df[feature.col_name_ub])
                    _ax.step(
                        date_list,
                        ub,
                        label='',
                        color='black',
                        linestyle='-',
                        where='post',
                    )
                if isinstance(feature, Controlled):
                    if feature.col_name_target not in df.columns:
                        continue

                    target = sub_plot.convert(df[feature.col_name_target])
                    _ax.step(
                        date_list,
                        target,
                        label='',
                        color='grey',
                        linestyle='--',
                        where='post',
                    )

            # legend
            if sub_plot.legend:
                ax_left.legend(lns, labels, loc='upper right', ncol=sub_plot.legend_col)

            if sub_plot.grid:
                ax_left.grid(visible=True, which='both', axis='y', color=fmt.light_grey, linestyle=fmt.line_solid)

        self._set_size(duration, fig)
        self._set_locator_and_formatter(duration=duration, axs=axs)

    def plot_solutions(
            self,
            real:       pd.DataFrame,
            solutions:  dict[float, pd.DataFrame],
            length:     int = 60*60*24,
            plot_upper_bound: bool = True,
            end:        datetime.datetime = None,
            start:      datetime.datetime = None,
            save_plot:  bool = False,
            filepath:   str = None,
    ):

        # timescale
        try:
            step_size = int(real['SimTime'].iloc[1] - real['SimTime'].iloc[0])
        except IndexError:
            raise ValueError(f'real only contains {len(real.index)} rows')

        len_n = int(length / step_size)

        ratios = [subplot.ratio for subplot in self.sub_plots]
        fig, axs = plt.subplots(len(self), sharex='all', gridspec_kw={'height_ratios': ratios})

        if not isinstance(axs, np.ndarray):
            axs = (axs, )
        else:
            axs = axs.tolist()

        color_map = [fmt.light_red, fmt.dark_grey, fmt.light_grey]

        for i, (calculation_time, df) in enumerate(solutions.items()):

            n = len(list(solutions.keys()))
            i = i / n

            grey = fmt.interpolate_colors(i, color_map)

            df = df[df['SimTime'] >= calculation_time]

            if end is not None:
                df = df[df['SimTime'] <= end.timestamp()]

            if start is not None:
                df = df[start.timestamp() <= df['SimTime']]

            df = df.iloc[:len_n]

            # offset = datetime.datetime.fromtimestamp(Mode.time_offset)
            try:
                start_date = datetime.datetime.fromtimestamp(int(df['SimTime'].iloc[0]))
            except IndexError:
                print('Empty DataFrame warning!')
                continue

            date_list = [start_date + datetime.timedelta(seconds=step_size) * rows for rows in range(0, len(df.index))]

            # iterate over all sub_plots
            for ax, sub_plot in zip(axs, self.sub_plots):

                if sub_plot.y_label_left:
                    ax.set_ylabel(sub_plot.y_label_left)

                if sub_plot.unit_format_left:
                    major_formatter = FuncFormatter(sub_plot.unit_format_left)
                    ax.yaxis.set_major_formatter(major_formatter)
                    ax.yaxis.set_label_coords(-0.10, 0.5)

                else:
                    ax.yaxis.set_label_coords(-0.08, 0.5)

                if sub_plot.lb:
                    ax.set_ylim(bottom=sub_plot.lb - 0.4)

                if sub_plot.ub:
                    ax.set_ylim(top=sub_plot.ub + 0.4)

                # iterate over all features
                for feature in sub_plot.features:
                    try:
                        values = sub_plot.convert(df[feature.variable.col_name])
                    except KeyError:
                        continue

                    # actual plot
                    if sub_plot.step:
                        ax.step(
                            date_list,
                            values,
                            label=feature.variable.plt_opts.label,
                            color=grey,
                            linestyle=fmt.line_solid,
                            where=sub_plot.where,
                        )

                    else:
                        ax.plot(
                            date_list,
                            values,
                            label=feature.variable.plt_opts.label,
                            color=grey,
                            linestyle=fmt.line_solid,
                        )

                    # lower and upper bound
                    if isinstance(feature, Controlled):

                        try:
                            if plot_upper_bound:
                                ub = sub_plot.convert(df[feature.col_name_ub])
                                ax.step(date_list, ub, label='', color='black', linestyle='-', where='post')

                            lb = sub_plot.convert(df[feature.col_name_lb])
                            ax.step(date_list, lb, label='', color='black', linestyle='-', where='post')

                        except Exception:
                            pass

                        if feature.col_name_lb not in df.columns or feature.col_name_ub not in df.columns:
                            continue

                        """
                        lb = sub_plot.convert(df[feature.col_name_lb])
                        ax.step(date_list, lb, label='', color='black', linestyle='-', where='post')
                    
                        if plot_upper_bound:
                            ub = sub_plot.convert(df[feature.col_name_ub])                        
                            ax.step(date_list, ub, label='', color='black', linestyle='-', where='post')
                        """

        # iterate over all sub_plots
        start_date = datetime.datetime.fromtimestamp(int(real['SimTime'].iloc[0]))
        date_list = [start_date + datetime.timedelta(seconds=step_size) * rows for rows in range(0, len(real.index))]

        for ax, sub_plot in zip(axs, self.sub_plots):

            # iterate over all features
            for feature in sub_plot.features:
                if feature.variable.col_name not in real.columns:
                    feature.process(real, inplace=True)

                values = sub_plot.convert(real[feature.variable.col_name])

                # actual plot
                if sub_plot.step:
                    ax.step(
                        date_list,
                        values,
                        label=feature.variable.plt_opts.label,
                        color=fmt.red,
                        linestyle=fmt.line_solid,
                        where=sub_plot.where,
                    )

                else:
                    ax.plot(
                        date_list,
                        values,
                        label=feature.variable.plt_opts.label,
                        color=fmt.red,
                        linestyle=fmt.line_solid,
                    )

                """
                # lower and upper bound
                if isinstance(feature, Controlled):

                    if feature.col_name_lb not in real.columns:
                        continue

                    lb = sub_plot.convert(real[feature.col_name_lb])

                    ax.step(
                        date_list,
                        lb,
                        label='',
                        color='black',
                        linestyle='-',
                        where='post',
                    )

                    if feature.col_name_ub not in real.columns:
                        continue

                    if plot_upper_bound:
                        ub = sub_plot.convert(real[feature.col_name_ub])
                        ax.step(
                            date_list,
                            ub,
                            label='',
                            color='black',
                            linestyle='-',
                            where='post',
                        )
                """

        plt.xlim(left=start_date)

        if end is not None:
            plt.xlim(right=end)

        first_df = list(solutions.values())[0]
        last_df = list(solutions.values())[-1]
        duration = abs(int(last_df['SimTime'].iloc[-1] - first_df['SimTime'].iloc[0]))
        self._set_size(duration, fig=fig)
        self._set_locator_and_formatter(duration, axs=axs)

        # save plot
        if save_plot:
            plt.savefig(filepath)

        plt.show()
        plt.clf()
        plt.close('all')

    def _set_size(self, duration: int, fig):

        if self.size_x:
            size_x = self.size_x
        else:
            size_x = 5 + self.scale_x * math.sqrt(duration / one_day)

        if self.size_y:
            size_y = self.size_y
        else:
            size_y = self.scale_y * len(self)

        fig.set_size_inches(size_x, size_y)

    def _set_locator_and_formatter(self, duration: int, axs):

        # major and minor locator
        if duration <= one_day:
            major_locator = dates.DayLocator()
            major_formatter = dates.DateFormatter('%a')
            minor_locator = dates.HourLocator(byhour=[4, 8, 12, 16, 20])
            minor_formatter = dates.DateFormatter('%H:%M')

        elif duration <= one_day * 2:
            major_locator = dates.DayLocator()
            major_formatter = dates.DateFormatter('%a')
            minor_locator = dates.HourLocator(byhour=[8, 16])
            minor_formatter = dates.DateFormatter('%H:%M')

        elif duration <= one_day * 4:
            major_locator = dates.DayLocator()
            major_formatter = dates.DateFormatter('%a')
            minor_locator = dates.HourLocator(byhour=[8, 16])
            minor_formatter = dates.DateFormatter('%H:%M')

        elif duration <= one_week:
            major_locator = dates.MonthLocator()
            major_formatter = dates.DateFormatter('%b')

            minor_locator = dates.DayLocator()
            minor_formatter = dates.DateFormatter('%a')

        elif duration <= one_week * 2:
            major_locator = dates.MonthLocator()
            major_formatter = dates.DateFormatter('%b')

            minor_locator = dates.DayLocator()
            minor_formatter = dates.DateFormatter('%d')

        elif duration <= one_month:
            major_locator = dates.MonthLocator()
            major_formatter = dates.DateFormatter('%b')

            minor_locator = dates.DayLocator(interval=2)
            minor_formatter = dates.DateFormatter('%d.')

        else:
            major_locator = dates.YearLocator()
            major_formatter = dates.DateFormatter('%Y')
            minor_locator = dates.MonthLocator()
            minor_formatter = dates.DateFormatter('%b')

        if self.major_locator is None:
            axs[-1].xaxis.set_major_locator(major_locator)
        else:
            axs[-1].xaxis.set_major_locator(self.major_locator)

        if self.major_formatter is None:
            axs[-1].xaxis.set_major_formatter(major_formatter)
        else:
            axs[-1].xaxis.set_major_formatter(self.major_formatter)

        if self.minor_locator is None:
            axs[-1].xaxis.set_minor_locator(minor_locator)
        else:
            axs[-1].xaxis.set_minor_locator(self.minor_locator)

        if self.minor_formatter is None:
            axs[-1].xaxis.set_minor_formatter(minor_formatter)
        else:
            axs[-1].xaxis.set_minor_formatter(self.minor_formatter)
