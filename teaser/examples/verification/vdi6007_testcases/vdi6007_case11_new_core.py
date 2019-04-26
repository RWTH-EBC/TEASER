#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import os
import numpy as np

from teaser.logic.simulation.vdi_core import VDICore
import teaser.examples.verification.vdi6007_testcases.vdi6007_case01 as vdic
from teaser.examples.verification.vdi6007_testcases.vdi6007shared import (
    prepare_thermal_zone,
    hourly_average,
    plot_result,
    prepare_internal_gains_rad,
    prepare_set_temperature,
)


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

    Originally fails with:
    
        Deviations temperature in K:
        Max. deviation day 1: 2.6729828763453547
        Max. deviation day 10: 1.1678876692598514
        Max. deviation day 60: 1.1350803986407598
        Deviations heating/cooling in W:
        Max. deviation day 1: 90.12261852960904
        Max. deviation day 10: 267.87214370800694
        Max. deviation day 60: 274.8160896443969

    Introducing `tz.model_attr.alpha_comb_inner_iw = 3` improves the results to

        Deviations temperature in K:
        Max. deviation day 1: 2.0026798505430357
        Max. deviation day 10: 0.8789041941994213
        Max. deviation day 60: 0.8721490045311029
        Deviations heating/cooling in W:
        Max. deviation day 1: 0.7602321051261924
        Max. deviation day 10: 242.07940042260856
        Max. deviation day 60: 244.90145685319482

    Setting `tz.model_attr.alpha_comb_outer_ow = 10.5 * 25` overall worsens results:

        Deviations temperature in K:
        Max. deviation day 1: 2.0135679444329675
        Max. deviation day 10: 0.9308007751085441
        Max. deviation day 60: 0.9244159549466211
        Deviations heating/cooling in W:
        Max. deviation day 1: 1.6933125877698672
        Max. deviation day 10: 229.33698430247819
        Max. deviation day 60: 232.01258145610353

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
    tz.volume = 0  # Seems to have no effect on results
    tz.model_attr.alpha_comb_inner_iw = 3  # Improvement, see doc-string
    # tz.model_attr.alpha_conv_outer_ow = 25  # No effect because only used in equalAirTemp
    # tz.model_attr.alpha_comb_outer_ow = 10.5 * 25  # Partial improvement, overall worse
    tz.model_attr.ratio_conv_rad_inner_win = 0  # No effect
    tz.infiltration_rate = 0  # No effect

    calc = VDICore(tz)
    calc.equal_air_temp = np.zeros(timesteps) + 295.15
    calc.solar_rad_in = np.zeros((timesteps, 1))

    calc.t_set_heating = prepare_set_temperature(timesteps_day)
    calc.t_set_cooling = prepare_set_temperature(timesteps_day)

    calc.heater_limit = np.zeros((timesteps, 3))
    calc.heater_limit[:, 0] = 500
    calc.heater_order = np.array([1, 2, 3])
    calc.cooler_limit = np.zeros((timesteps, 3))
    calc.cooler_limit[:, 0] = -500
    calc.cooler_order = [2, 1, 3]

    calc.internal_gains_rad = prepare_internal_gains_rad(timesteps_day)

    calc.debug = True
    t_air, q_air_hc, data_debug = calc.simulate()

    T_air_mean = hourly_average(data=t_air - 273.15, times_per_hour=times_per_hour)
    Q_hc_mean = hourly_average(data=q_air_hc, times_per_hour=times_per_hour)

    Q_hc_1 = Q_hc_mean[0:24]
    Q_hc_10 = Q_hc_mean[216:240]
    Q_hc_60 = Q_hc_mean[1416:1440]

    T_air_1 = T_air_mean[0:24]
    T_air_10 = T_air_mean[216:240]
    T_air_60 = T_air_mean[1416:1440]

    this_path = os.path.dirname(os.path.abspath(__file__))
    ref_file = "case11_res.csv"
    ref_path = os.path.join(this_path, "inputs", ref_file)

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
        # plot_result(T_air_1, T_air_ref_1, "Results temperatures day 1", "temperature")
        # plot_result(
        #     T_air_10, T_air_ref_10, "Results temperatures day 10", "temperature"
        # )
        # plot_result(
        #     T_air_60, T_air_ref_60, "Results temperatures day 60", "temperature"
        # )
        #
        # plot_result(
        #     Q_hc_1,
        #     Q_hc_ref_1,
        #     "Results heating/cooling day 1",
        #     "heat",
        #     res_raw=q_air_hc[: 24 * 60],
        # )
        # plot_result(Q_hc_10, Q_hc_ref_10, "Results heating/cooling day 10", "heat")
        # plot_result(Q_hc_60, Q_hc_ref_60, "Results heating/cooling day 60", "heat")
        #
        days = 2
        plot_result(Q_hc_mean[0:24*days], Q_hc_ref_1, f"Results heating/cooling {days} days", "heat")
        plot_result(T_air_mean[0:24*days], T_air_ref_1, f"Results temperature {days} days", "temperature")

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

    return (
        max_dev_1_temp,
        max_dev_10_temp,
        max_dev_60_temp,
        max_dev_1,
        max_dev_10,
        max_dev_60,
    )


if __name__ == "__main__":
    run_case11(plot_res=True)
