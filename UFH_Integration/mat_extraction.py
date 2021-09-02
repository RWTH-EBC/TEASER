"""
Goals of this part of the examples:
1. Learn how to use `TimeSeriesData`
2. Understand why we use `TimeSeriesData`
3. Get to know the different processing functions
"""
# Start by importing all relevant packages
import math
import pathlib
import numpy as np
import matplotlib.pyplot as plt
# Imports from ebcpy
from ebcpy import TimeSeriesData


def main(with_plot=True):
    """
    Arguments of this example:

    :param bool with_plot:
        Show the plot at the end of the script. Default is True.
    """
    # First get the path with relevant input files:
    basepath = pathlib.Path(__file__).parents[3].joinpath("Dymola")

    # Now a simulation result file (.mat)
    tsd_mat = TimeSeriesData(basepath.joinpath('SimpleBuildingint_tabs_comparison.mat'))
    # print(tsd_mat)
    # for tag in tsd_mat.get_tags(variable="multizone.zone[1].ROM.intGainsConv.T")[::-1]:
    #     plt.plot(tsd_mat.loc[:, ("multizone.zone[1].ROM.intGainsConv.T", tag)], label=tag)
    # plt.show()
    # plt.legend()

    plt.figure()
    fig, axs = plt.subplots(2)

    axs[0].plot(tsd_mat.loc[:, ("multizone.zone[2].ROM.intGainsConv.T", "raw")], label="as Walls", color="blue")
    axs[0].plot(tsd_mat.loc[:, ("multizone.zone[1].ROM.intGainsConv.T", "raw")], label="as Tabs", color="red")
    axs[0].legend()

    # RMS test
    x = tsd_mat.to_df()
    x["RMS_test"] = abs(x["multizone.zone[1].ROM.intGainsConv.T"] - x["multizone.zone[2].ROM.intGainsConv.T"])/x["multizone.zone[1].ROM.intGainsConv.T"]*100
    axs[1].plot(x["RMS_test"], label="Percentage", color="blue")
    axs[1].legend()
    plt.show()
    print()
    # ######################### Processing TimeSeriesData ##########################
    # Index changing:
    # print(tsd_hdf.index)
    # tsd_hdf.to_float_index(offset=0)
    # print(tsd_hdf.index)
    # tsd_hdf.to_datetime_index(unit_of_index="s")
    # print(tsd_hdf.index)
    # # Some filter options
    # tsd_hdf.low_pass_filter(crit_freq=0.1, filter_order=2,
    #                         variable="measured_T", new_tag="lowPass2")
    # print(tsd_hdf)
    # tsd_hdf.moving_average(window=50, variable="measured_T",
    #                        tag="raw", new_tag="MovingAverage")
    # print(tsd_hdf)
    # for tag in tsd_hdf.get_tags(variable="measured_T")[::-1]:
    #     plt.plot(tsd_hdf.loc[:, ("measured_T", tag)], label=tag)
    # plt.legend()
    #
    # # How-to re-sample your data:
    # tsd_hdf_ref = tsd_hdf.copy()  # Create a savecopy to later reference the change.
    # # Call the function. Desired frequency is a string (s: seconds), 60: 60 seconds.
    # # Play around with this value to see what happens.
    # tsd_hdf.clean_and_space_equally(desired_freq="60s")
    # plt.figure()
    # plt.plot(tsd_hdf_ref.loc[:, ("measured_T", "raw")], label="Reference", color="blue")
    # plt.plot(tsd_hdf.loc[:, ("measured_T", "raw")], label="Resampled", color="red")
    # plt.legend()
    # if with_plot:
    #     plt.show()


if __name__ == '__main__':
    main()
