#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import os
import numpy as np
import matplotlib.pyplot as plt

import teaser.logic.simulation.VDI_6007.low_order_VDI as low_order_VDI
import teaser.examples.verification.vdi6007_testcases.vdi6007_case01 as vdic


def run_case11(plot_res=False):
    """
    Run test case 11

    Parameters
    ----------
    plot_res : bool, optional
        Defines, if results should be plotted (default: False)

    Returns
    -------
    res_tuple : tuple (of floats)
        Results tuple with maximal deviations for temperatures and power
        values
        (max_dev_1_temp, max_dev_10_temp, max_dev_60_temp, max_dev_1,
            max_dev_10, max_dev_60)
    """

    # Definition of time horizon
    times_per_hour = 60
    timesteps = 24 * 60 * times_per_hour  # 60 days
    timesteps_day = int(24 * times_per_hour)

    # Zero inputs
    ventRate = np.zeros(timesteps)
    solarRad_in = np.zeros((timesteps, 1))
    Q_ig = np.zeros(timesteps)

    # Constant inputs
    alphaRad = np.zeros(timesteps) + 5
    equalAirTemp = np.zeros(timesteps) + 295.15  # all temperatures in K
    weatherTemperature = np.zeros(timesteps) + 295.15  # in K

    # Variable inputs
    source_igRad = np.zeros(timesteps_day)
    for q in range(int(6 * timesteps_day / 24), int(18 * timesteps_day / 24)):
        source_igRad[q] = 1000
    source_igRad = np.tile(source_igRad, 60)

    # Load constant house parameters
    houseData = {"R1i": 0.000595693407511,
                 "C1i": 14836354.6282,
                 "Ai": 75.5,
                 "RRest": 0.03895919557,
                 "R1o": 0.00436791293674,
                 "C1o": 1600848.94,
                 "Ao": [10.5],
                 "Aw": np.zeros(1),
                 "At": [0],
                 "Vair": 0,
                 "rhoair": 1.19,
                 "cair": 1007,
                 "splitfac": 0.09,
                 "g": 1,
                 "alphaiwi": 3,
                 "alphaowi": 2.7,
                 "alphaWall": 25 * 10.5,  # 25 * sum(Ao)
                 "withInnerwalls": True}

    krad = 1

    # Define set points
    t_set = np.zeros(timesteps_day) + 273.15 + 22
    for q in range(int(6 * timesteps_day / 24), int(18 * timesteps_day / 24)):
        t_set[q] = 273.15 + 27
    t_set = np.tile(t_set, 60)
    t_set_heating = t_set
    t_set_cooling = t_set

    heater_limit = np.zeros((timesteps, 3))
    cooler_limit = np.zeros((timesteps, 3))
    heater_limit[:, 0] = 500
    cooler_limit[:, 1] = -500

    # Calculate indoor air temperature
    T_air, Q_hc, Q_iw, Q_ow = \
        low_order_VDI.reducedOrderModelVDI(houseData,
                                           weatherTemperature,
                                           solarRad_in,
                                           equalAirTemp,
                                           alphaRad,
                                           ventRate,
                                           Q_ig,
                                           source_igRad,
                                           krad,
                                           t_set_heating,
                                           t_set_cooling,
                                           heater_limit,
                                           cooler_limit,
                                           heater_order=np.array(
                                               [1, 2,
                                                3]),
                                           cooler_order=np.array(
                                               [2, 1,
                                                3]),
                                           dt=int(
                                               3600 / times_per_hour))

    # Compute averaged results
    Q_hc_mean = np.array(
        [np.mean(Q_hc[i * times_per_hour:(i + 1) * times_per_hour]) for i in
         range(24 * 60)])
    Q_iw_mean = np.array(
        [np.mean(Q_iw[i * times_per_hour:(i + 1) * times_per_hour]) for i in
         range(24 * 60)])
    Q_ow_mean = np.array(
        [np.mean(Q_ow[i * times_per_hour:(i + 1) * times_per_hour]) for i in
         range(24 * 60)])

    Q_hc_1 = Q_hc_mean[0:24] + Q_iw_mean[0:24] + Q_ow_mean[0:24]
    Q_hc_10 = Q_hc_mean[216:240] + Q_iw_mean[216:240] + Q_ow_mean[216:240]
    Q_hc_60 = Q_hc_mean[1416:1440] + Q_iw_mean[1416:1440] + Q_ow_mean[
                                                            1416:1440]

    T_air_c = T_air - 273.15
    T_air_mean = np.array(
        [np.mean(T_air_c[i * times_per_hour:(i + 1) * times_per_hour]) for i in
         range(24 * 60)])

    T_air_1 = T_air_mean[0:24]
    T_air_10 = T_air_mean[216:240]
    T_air_60 = T_air_mean[1416:1440]

    this_path = os.path.dirname(os.path.abspath(__file__))
    ref_file = 'case11_res.csv'
    ref_path = os.path.join(this_path, 'inputs', ref_file)

    # Load reference results
    (load_res_1, load_res_10, load_res_60) = vdic.load_res(ref_path)
    Q_hc_ref_1 = load_res_1[:, 1]
    Q_hc_ref_10 = load_res_10[:, 1]
    Q_hc_ref_60 = load_res_60[:, 1]

    T_air_ref_1 = load_res_1[:, 0]
    T_air_ref_10 = load_res_10[:, 0]
    T_air_ref_60 = load_res_60[:, 0]

    # Plot comparisons
    def plot_result(res, ref, title="Results day 1"):
        plt.figure()
        ax_top = plt.subplot(211)
        plt.plot(ref, label="Reference", color="black", linestyle="--")
        plt.plot(res, label="Simulation", color="blue", linestyle="-")
        plt.legend()
        plt.ylabel("Heat load in W")

        plt.title(title)

        plt.subplot(212, sharex=ax_top)
        plt.plot(res - ref, label="Ref. - Sim.")
        plt.legend()
        plt.ylabel("Heat load difference in W")
        plt.xticks([4 * i for i in range(7)])
        plt.xlim([1, 24])
        plt.xlabel("Time in h")

        plt.show()

    if plot_res:
        plot_result(T_air_1, T_air_ref_1, "Results temperatures day 1")
        plot_result(T_air_10, T_air_ref_10, "Results temperatures day 10")
        plot_result(T_air_60, T_air_ref_60, "Results temperatures day 60")

        plot_result(Q_hc_1, Q_hc_ref_1, "Results heating/cooling day 1")
        plot_result(Q_hc_10, Q_hc_ref_10, "Results heating/cooling day 10")
        plot_result(Q_hc_60, Q_hc_ref_60, "Results heating/cooling day 60")

    max_dev_1_temp = np.max(np.abs(T_air_1 - T_air_ref_1))
    max_dev_10_temp = np.max(np.abs(T_air_10 - T_air_ref_10))
    max_dev_60_temp = np.max(np.abs(T_air_60 - T_air_ref_60))

    print("Deviations temperature in K:")
    print("Max. deviation day 1: " + str(max_dev_1_temp))
    print("Max. deviation day 10: " + str(max_dev_10_temp))
    print("Max. deviation day 60: " + str(max_dev_60_temp))

    max_dev_1 = np.max(np.abs(Q_hc_1 - Q_hc_ref_1))
    max_dev_10 = np.max(np.abs(Q_hc_10 - Q_hc_ref_10))
    max_dev_60 = np.max(np.abs(Q_hc_60 - Q_hc_ref_60))

    print("Deviations heating/cooling in W:")
    print("Max. deviation day 1: " + str(max_dev_1))
    print("Max. deviation day 10: " + str(max_dev_10))
    print("Max. deviation day 60: " + str(max_dev_60))

    return (max_dev_1_temp, max_dev_10_temp, max_dev_60_temp, max_dev_1,
            max_dev_10, max_dev_60)

if __name__ == '__main__':
    run_case11(plot_res=True)
