#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import os
import numpy as np

from teaser.logic.simulation.vdi_core import VDICore
import teaser.examples.verification.vdi6007_testcases.vdi6007_case01 as vdic
from teaser.examples.verification.vdi6007_testcases.vdi6007shared import \
    prepare_thermal_zone, hourly_average, plot_result


def run_case11(plot_res=False):
    """
    Run test case 11

    Test Case 11 of the VDI 6007 Part 1:
    Calculation of heat load excited with a given radiative heat source and a setpoint
    profile for room version S. It is based on Test Case 7, but with a cooling ceiling
    for cooling purposes instead of a pure convective ideal cooler.

    Boundary conditions :
      - constant outdoor air temperature 22°C
      - no solar or short-wave radiation on the exterior wall
      - no solar or short-wave radiation through the windows
      - no long-wave radiation exchange between exterior wall, windows and ambient
        environment

    This test validates implementation of cooling ceiling or floor heating.

    Currently fails with:
    
        Deviations temperature in K:
        Max. deviation day 1: 2.6729828763453547
        Max. deviation day 10: 1.1678876692598514
        Max. deviation day 60: 1.1350803986407598
        Deviations heating/cooling in W:
        Max. deviation day 1: 90.12261852960904
        Max. deviation day 10: 267.87214370800694
        Max. deviation day 60: 274.8160896443969

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

    tz = prepare_thermal_zone(timesteps, room="S1")

    calc = VDICore(tz)
    calc.equal_air_temp = np.zeros(timesteps) + 295.15
    calc.solar_rad_in = np.zeros((timesteps, 1))

    t_set = np.zeros(timesteps_day) + 273.15 + 22
    for q in range(int(6 * timesteps_day / 24), int(18 * timesteps_day / 24)):
        t_set[q] = 273.15 + 27
    t_set = np.tile(t_set, 60)

    calc.t_set_heating = t_set
    calc.t_set_cooling = t_set

    calc.heater_limit = np.zeros((timesteps, 3))
    calc.heater_limit[:, 0] = 500
    calc.heater_order = np.array([1, 2, 3])
    calc.cooler_limit = np.zeros((timesteps, 3))
    calc.cooler_limit[:, 0] = - 500
    calc.cooler_order = [2, 1, 3]

    source_igRad = np.zeros(timesteps_day)
    for q in range(int(6 * timesteps_day / 24), int(18 * timesteps_day / 24)):
        source_igRad[q] = 1000
    source_igRad = np.tile(source_igRad, 60)

    calc.internal_gains_rad = source_igRad

    t_air, q_air_hc = calc.simulate()

    T_air_mean = hourly_average(data=t_air - 273.15, times_per_hour=times_per_hour)
    Q_hc_mean = hourly_average(data=q_air_hc, times_per_hour=times_per_hour)

    Q_hc_1 = Q_hc_mean[0:24]
    Q_hc_10 = Q_hc_mean[216:240]
    Q_hc_60 = Q_hc_mean[1416:1440]

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
    if plot_res:
        plot_result(T_air_1, T_air_ref_1, "Results temperatures day 1", "temperature")
        plot_result(
            T_air_10, T_air_ref_10, "Results temperatures day 10", "temperature"
        )
        plot_result(
            T_air_60, T_air_ref_60, "Results temperatures day 60", "temperature"
        )

        plot_result(
            Q_hc_1,
            Q_hc_ref_1,
            "Results heating/cooling day 1",
            "heat",
            res_raw=q_air_hc[:24*60]
        )
        plot_result(Q_hc_10, Q_hc_ref_10, "Results heating/cooling day 10", "heat")
        plot_result(Q_hc_60, Q_hc_ref_60, "Results heating/cooling day 60", "heat")

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
