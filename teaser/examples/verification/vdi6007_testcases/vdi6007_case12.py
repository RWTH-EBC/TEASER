#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from __future__ import division
import os
import numpy as np

import teaser.logic.simulation.VDI_6007.low_order_VDI as low_order_VDI
import teaser.examples.verification.vdi6007_testcases.vdi6007_case01 as vdic


def run_case12(plot_res=False):
    """
    Run test case 12

    Parameters
    ----------
    plot_res : bool, optional
        Defines, if results should be plotted (default: False)
    """

    # Definition of time horizon
    times_per_hour = 60
    timesteps = 24 * 60 * times_per_hour # 60 days
    timesteps_day = int(24 * times_per_hour)

    # Constant inputs
    alphaRad = np.zeros(timesteps) + 5

    # Variable inputs
    Q_ig = np.zeros(timesteps_day)
    source_igRad = np.zeros(timesteps_day)
    for q in range(int(7*timesteps_day/24), int(17*timesteps_day/24)):
        Q_ig[q] = 200 + 80
        source_igRad[q] = 80
    Q_ig = np.tile(Q_ig, 60)
    source_igRad = np.tile(source_igRad, 60)

    this_path = os.path.dirname(os.path.abspath(__file__))
    ref_file = 'case12_q_sol.csv'
    ref_path = os.path.join(this_path, 'inputs', ref_file)

    solarRad_raw = np.loadtxt(ref_path, usecols=(1,))
    solarRad = solarRad_raw[0:24]
    solarRad[solarRad > 100] = solarRad[solarRad > 100] * 0.15
    solarRad_adj = np.repeat(solarRad, times_per_hour)
    solarRad_in = np.array([np.tile(solarRad_adj, 60)]).T

    ref_file = 'case12_t_amb.csv'
    ref_path = os.path.join(this_path, 'inputs', ref_file)

    t_outside_raw = np.loadtxt(ref_path, delimiter=",")
    t_outside = ([t_outside_raw[2*i,1] for i in range(24)])
    t_outside_adj = np.repeat(t_outside, times_per_hour)
    weatherTemperature = np.tile(t_outside_adj, 60)

    equalAirTemp = weatherTemperature

    # VentRate --> incoming volume flow rate in m3/s
    ventRate = np.zeros(timesteps_day) + 100 / 3600
    for q in range(int(7*timesteps_day/24), int(17*timesteps_day/24)):
        ventRate[q] = 50 / 3600
    ventRate = np.tile(ventRate, 60)

    # Load constant house parameters
    houseData = {"R1i": 0.000595693407511,
                "C1i": 14836354.6282,
                "Ai": 75.5,
                "RRest": 0.03895919557,
                "R1o": 0.00436791293674,
                "C1o": 1600848.94,
                "Ao": [10.5],
                "Aw": np.zeros(1),
                "At": [7],
                "Vair": 0,
                "rhoair": 1.19,
                "cair": 1007,
                "splitfac": 0.09,
                "g": 1,
                "alphaiwi": 2.24,
                "alphaowi": 2.7,
                "alphaWall": 25 * 10.5, # 25 * sum(Ao)
                "withInnerwalls": True}

    krad = 1

    # Define set points (prevent heating or cooling!)
    t_set_heating = np.zeros(timesteps)        # in Kelvin
    t_set_cooling = np.zeros(timesteps) + 600  # in Kelvin

    heater_limit = np.zeros((timesteps,3)) + 1e10
    cooler_limit = np.zeros((timesteps,3)) - 1e10

    # Calculate indoor air temperature
    T_air, Q_hc, Q_iw, Q_ow = low_order_VDI.reducedOrderModelVDI(houseData, weatherTemperature, solarRad_in,
                                       equalAirTemp, alphaRad, ventRate, Q_ig, source_igRad, krad,
                                       t_set_heating, t_set_cooling, heater_limit, cooler_limit,
                                       heater_order=np.array([1,2,3]), cooler_order=np.array([1,2,3]),
                                       dt=int(3600/times_per_hour))

    # Compute averaged results
    T_air_c = T_air - 273.15
    T_air_mean = np.array([np.mean(T_air_c[i*times_per_hour:(i+1)*times_per_hour]) for i in range(24*60)])

    T_air_1 = T_air_mean[0:24]
    T_air_10 = T_air_mean[216:240]
    T_air_60 = T_air_mean[1416:1440]

    ref_file = 'case12_res.csv'
    ref_path = os.path.join(this_path, 'inputs', ref_file)

    # Load reference results
    (T_air_ref_1, T_air_ref_10, T_air_ref_60) = vdic.load_res(ref_path)
    T_air_ref_1 = T_air_ref_1[:,0]
    T_air_ref_10 = T_air_ref_10[:,0]
    T_air_ref_60 = T_air_ref_60[:,0]


    # Plot comparisons
    def plot_result(res, ref, title="Results day 1"):

        import matplotlib.pyplot as plt

        plt.figure()
        ax_top = plt.subplot(211)
        plt.plot(ref, label="Reference", color="black", linestyle="--")
        plt.plot(res, label="Simulation", color="blue", linestyle="-")
        plt.legend()
        plt.ylabel("Temperature in degC")

        plt.title(title)

        plt.subplot(212, sharex=ax_top)
        plt.plot(res-ref, label="Ref. - Sim.")
        plt.legend()
        plt.ylabel("Temperature difference in K")
        plt.xticks([4*i for i in range(7)])
        plt.xlim([1,24])
        plt.xlabel("Time in h")

        plt.show()

    if plot_res:
        plot_result(T_air_1, T_air_ref_1, "Results day 1")
        plot_result(T_air_10, T_air_ref_10, "Results day 10")
        plot_result(T_air_60, T_air_ref_60, "Results day 60")

    max_dev_1 = np.max(np.abs(T_air_1 - T_air_ref_1))
    max_dev_10 = np.max(np.abs(T_air_10 - T_air_ref_10))
    max_dev_60 = np.max(np.abs(T_air_60 - T_air_ref_60))

    print("Max. deviation day 1: " + str(max_dev_1))
    print("Max. deviation day 10: " + str(max_dev_10))
    print("Max. deviation day 60: " + str(max_dev_60))

    return (max_dev_1, max_dev_10, max_dev_60)

if __name__ == '__main__':
    run_case12(plot_res=True)