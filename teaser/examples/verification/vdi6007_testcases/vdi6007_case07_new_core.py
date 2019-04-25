#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import os
import numpy as np

from teaser.logic.simulation.vdi_core import VDICore
import teaser.examples.verification.vdi6007_testcases.vdi6007_case01 as vdic
from teaser.examples.verification.vdi6007_testcases.vdi6007shared import \
    prepare_thermal_zone, hourly_average, plot_result, prepare_internal_gains_rad


def run_case7(plot_res=False):
    """
    Run test case 7

    Parameters
    ----------
    plot_res : bool, optional
        Defines, if results should be plotted (default: False)

    Returns
    -------
    result_tuple : tuple (of floats)
        Results tuple with maximal power deviations
        (max_dev_1, max_dev_10, max_dev_60)
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
    calc.cooler_limit = np.zeros((timesteps, 3))
    calc.cooler_limit[:, 0] = - 500

    calc.internal_gains_rad = prepare_internal_gains_rad(timesteps_day)

    t_air, q_air_hc = calc.simulate()

    Q_hc_mean = hourly_average(data=q_air_hc, times_per_hour=times_per_hour)

    Q_hc_1 = Q_hc_mean[0:24]
    Q_hc_10 = Q_hc_mean[216:240]
    Q_hc_60 = Q_hc_mean[1416:1440]

    this_path = os.path.dirname(os.path.abspath(__file__))
    ref_file = 'case07_res.csv'
    ref_path = os.path.join(this_path, 'inputs', ref_file)

    # Load reference results
    (Q_hc_ref_1, Q_hc_ref_10, Q_hc_ref_60) = vdic.load_res(ref_path)
    Q_hc_ref_1 = Q_hc_ref_1[:, 0]
    Q_hc_ref_10 = Q_hc_ref_10[:, 0]
    Q_hc_ref_60 = Q_hc_ref_60[:, 0]

    if plot_res:
        plot_result(Q_hc_1, Q_hc_ref_1, "Results day 1", "heat")
        plot_result(Q_hc_10, Q_hc_ref_10, "Results day 10", "heat")
        plot_result(Q_hc_60, Q_hc_ref_60, "Results day 60", "heat")

    max_dev_1 = np.max(np.abs(Q_hc_1 - Q_hc_ref_1))
    max_dev_10 = np.max(np.abs(Q_hc_10 - Q_hc_ref_10))
    max_dev_60 = np.max(np.abs(Q_hc_60 - Q_hc_ref_60))

    print("Max. deviation day 1: " + str(max_dev_1))
    print("Max. deviation day 10: " + str(max_dev_10))
    print("Max. deviation day 60: " + str(max_dev_60))

    return (max_dev_1, max_dev_10, max_dev_60)


if __name__ == '__main__':
    run_case7(plot_res=True)
