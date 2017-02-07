#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import os
import numpy as np
import matplotlib.pyplot as plt

import teaser.logic.simulation.VDI_6007.low_order_VDI as low_order_VDI
import teaser.examples.verification.vdi6007_testcases.vdi6007_case01 as vdic
import teaser.logic.simulation.VDI_6007.equal_air_temperature as eq_air_temp


def run_case9(plot_res=False):
    """
    Run test case 9

    Parameters
    ----------
    plot_res : bool, optional
        Defines, if results should be plotted (default: False)
    """

    # Definition of time horizon
    times_per_hour = 60
    timesteps = 24 * 60 * times_per_hour  # 60 days
    timesteps_day = int(24 * times_per_hour)

    # Zero inputs
    ventRate = np.zeros(timesteps)

    # Constant inputs
    alphaRad = np.zeros(timesteps) + 5

    # Variable inputs
    Q_ig = np.zeros(timesteps_day)
    source_igRad = np.zeros(timesteps_day)
    for q in range(int(7 * timesteps_day / 24), int(17 * timesteps_day / 24)):
        Q_ig[q] = 200 + 80
        source_igRad[q] = 80
    Q_ig = np.tile(Q_ig, 60)
    source_igRad = np.tile(source_igRad, 60)

    this_path = os.path.dirname(os.path.abspath(__file__))
    ref_file = 'case09_q_sol_win.csv'
    ref_path = os.path.join(this_path, 'inputs', ref_file)

    q_sol_rad_win_raw = np.loadtxt(ref_path, usecols=(1, 2))
    solarRad_win = q_sol_rad_win_raw[0:24, :]
    solarRad_win[solarRad_win > 100] = solarRad_win[solarRad_win > 100] * 0.15
    solarRad_win_adj = np.repeat(solarRad_win, times_per_hour, axis=0)
    solarRad_win_in = np.tile(solarRad_win_adj.T, 60).T

    sunblind_in = np.zeros_like(solarRad_win)
    sunblind_in[solarRad_win > 100] = 0.85
    sunblind_in_adj = np.repeat(sunblind_in, times_per_hour, axis=0)
    sunblind_in_tiled = np.tile(sunblind_in_adj.T, 60).T

    ref_file = 'case09_q_sol_wall.csv'
    ref_path = os.path.join(this_path, 'inputs', ref_file)

    q_sol_rad_wall_raw = np.loadtxt(ref_path, usecols=(1, 2))
    solarRad_wall = q_sol_rad_wall_raw[0:24, :]
    solarRad_wall_adj = np.repeat(solarRad_wall, times_per_hour, axis=0)
    solarRad_wall_tiled = np.tile(solarRad_wall_adj.T, 60).T

    ref_file = 'case09_t_amb.csv'
    ref_path = os.path.join(this_path, 'inputs', ref_file)

    t_outside_raw = np.loadtxt(ref_path, delimiter=",")
    t_outside = ([t_outside_raw[2 * i, 1] for i in range(24)])
    t_outside_adj = np.repeat(t_outside, times_per_hour)
    weatherTemperature = np.tile(t_outside_adj, 60)

    ref_file = 'case09_h_sky.csv'
    ref_path = os.path.join(this_path, 'inputs', ref_file)

    H_sky_raw = np.loadtxt(ref_path, usecols=(1,))
    H_sky = H_sky_raw[0:24]
    t_black_sky_in = 65.99081593 * (H_sky ** 0.25)
    t_black_sky_adj = np.repeat(t_black_sky_in, times_per_hour)
    t_black_sky = np.tile(t_black_sky_adj, 60)

    eq_air_params = {"aExt": 0.7,
                     "eExt": 0.9,
                     "wfWall": [0.05796831135677373, 0.13249899738691134],
                     "wfWin": [0.4047663456281575, 0.4047663456281575],
                     "wfGro": 0,
                     "T_Gro": 273.15 + 12,
                     "alpha_wall_out": 20,
                     "alpha_rad_wall": 5,
                     "withLongwave": False}

    equalAirTemp = eq_air_temp.equal_air_temp(HSol=solarRad_wall_tiled,
                                              TBlaSky=t_black_sky,
                                              TDryBul=weatherTemperature,
                                              sunblind=sunblind_in_tiled,
                                              params=eq_air_params)

    # Load constant house parameters
    houseData = {"R1i": 0.000668895639141,
                 "C1i": 12391363.8631,
                 "Ai": 60.5,
                 "RRest": 0.01913729904,
                 "R1o": 0.0017362530106,
                 "C1o": 5259932.23,
                 "Ao": [10.5, 15],
                 "Aw": np.zeros(2),
                 "At": [7, 7],
                 "Vair": 52.5,
                 "rhoair": 1.19,
                 "cair": 0,
                 "splitfac": 0.09,
                 "g": 1,
                 "alphaiwi": 2.12,
                 "alphaowi": 2.7,
                 "alphaWall": 25 * 25.5,  # 25 * sum(Ao)
                 "withInnerwalls": True}

    krad = 1

    # Define set points (prevent heating or cooling!)
    t_set_heating = np.zeros(timesteps)  # in Kelvin
    t_set_cooling = np.zeros(timesteps) + 600  # in Kelvin

    heater_limit = np.zeros((timesteps, 3)) + 1e10
    cooler_limit = np.zeros((timesteps, 3)) - 1e10

    # Calculate indoor air temperature
    T_air, Q_hc, Q_iw, Q_ow = \
        low_order_VDI.reducedOrderModelVDI(houseData,
                                           weatherTemperature,
                                           solarRad_win_in,
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
                                               [1, 2,
                                                3]),
                                           dt=int(
                                               3600 / times_per_hour))

    # Compute averaged results
    T_air_c = T_air - 273.15
    T_air_mean = np.array(
        [np.mean(T_air_c[i * times_per_hour:(i + 1) * times_per_hour]) for i in
         range(24 * 60)])

    T_air_1 = T_air_mean[0:24]
    T_air_10 = T_air_mean[216:240]
    T_air_60 = T_air_mean[1416:1440]

    ref_file = 'case09_res.csv'
    ref_path = os.path.join(this_path, 'inputs', ref_file)

    # Load reference results
    (T_air_ref_1, T_air_ref_10, T_air_ref_60) = vdic.load_res(ref_path)
    T_air_ref_1 = T_air_ref_1[:, 0]
    T_air_ref_10 = T_air_ref_10[:, 0]
    T_air_ref_60 = T_air_ref_60[:, 0]

    # Plot comparisons
    def plot_result(res, ref, title="Results day 1"):
        plt.figure()
        ax_top = plt.subplot(211)
        plt.plot(res, label="Reference", color="black", linestyle="--")
        plt.plot(ref, label="Simulation", color="blue", linestyle="-")
        plt.legend()
        plt.ylabel("Temperature in degC")

        plt.title(title)

        plt.subplot(212, sharex=ax_top)
        plt.plot(res - ref, label="Ref. - Sim.")
        plt.legend()
        plt.ylabel("Temperature difference in K")
        plt.xticks([4 * i for i in range(7)])
        plt.xlim([1, 24])
        plt.xlabel("Time in h")

        plt.show()

    if plot_res:
        plot_result(T_air_1, T_air_ref_1, "Results day 1")
        plot_result(T_air_10, T_air_ref_10, "Results day 10")
        plot_result(T_air_60, T_air_ref_60, "Results day 60")

    print(
        "Max. deviation day 1: " + str(np.max(np.abs(T_air_1 - T_air_ref_1))))
    print("Max. deviation day 10: " + str(
        np.max(np.abs(T_air_10 - T_air_ref_10))))
    print("Max. deviation day 60: " + str(
        np.max(np.abs(T_air_60 - T_air_ref_60))))


if __name__ == '__main__':
    run_case9(plot_res=True)
