#!/usr/bin/env python
# coding=utf-8
"""
Run VDI 6007 test case 2
"""

import os
import numpy as np

from teaser.logic.simulation.vdi_core import VDICore
import teaser.examples.verification.vdi6007_testcases.vdi6007_case01 as vdic
from teaser.examples.verification.vdi6007_testcases.vdi6007shared import \
    prepare_thermal_zone


def run_case2(plot_res=False):
    """
    Run test case 2

    Parameters
    ----------
    plot_res : bool, optional
        Defines, if results should be plotted (default: False)
    Returns
    -------
    result_tuple : tuple (of floats)
        Results tuple with maximal temperature deviations
        (max_dev_1, max_dev_10, max_dev_60)
    """

    # Definition of time horizon
    times_per_hour = 60
    timesteps = 24 * 60 * times_per_hour  # 60 days
    timesteps_day = int(24 * times_per_hour)

    tz = prepare_thermal_zone(timesteps, room="S")

    calc = VDICore(tz)
    calc.equal_air_temp = np.zeros(timesteps) + 295.15
    calc.solar_rad_in = np.zeros((timesteps, 1))

    calc.t_set_heating = np.zeros(timesteps)  # in Kelvin
    calc.t_set_cooling = np.zeros(timesteps) + 600  # in Kelvin

    calc.heater_limit = np.zeros((timesteps, 3)) + 1e10
    calc.cooler_limit = np.zeros((timesteps, 3)) - 1e10

    source_igRad = np.zeros(timesteps_day)
    for q in range(int(6 * timesteps_day / 24), int(18 * timesteps_day / 24)):
        source_igRad[q] = 1000
    source_igRad = np.tile(source_igRad, 60)

    calc.internal_gains_rad = source_igRad

    t_air, q_air_hc = calc.simulate()

    T_air_c = t_air - 273.15
    T_air_mean = np.array(
        [np.mean(T_air_c[i * times_per_hour:(i + 1) * times_per_hour]) for i in
         range(24 * 60)])

    T_air_1 = T_air_mean[0:24]
    T_air_10 = T_air_mean[216:240]
    T_air_60 = T_air_mean[1416:1440]

    this_path = os.path.dirname(os.path.abspath(__file__))
    ref_file = 'case02_res.csv'
    ref_path = os.path.join(this_path, 'inputs', ref_file)

    # Load reference results
    (T_air_ref_1, T_air_ref_10, T_air_ref_60) = vdic.load_res(ref_path)
    T_air_ref_1 = T_air_ref_1[:, 0]
    T_air_ref_10 = T_air_ref_10[:, 0]
    T_air_ref_60 = T_air_ref_60[:, 0]

    # Plot comparisons
    def plot_result(res, ref, title="Results day 1"):

        import matplotlib.pyplot as plt

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

    max_dev_1 = np.max(np.abs(T_air_1 - T_air_ref_1))
    max_dev_10 = np.max(np.abs(T_air_10 - T_air_ref_10))
    max_dev_60 = np.max(np.abs(T_air_60 - T_air_ref_60))

    print("Max. deviation day 1: " + str(max_dev_1))
    print("Max. deviation day 10: " + str(max_dev_10))
    print("Max. deviation day 60: " + str(max_dev_60))

    return (max_dev_1, max_dev_10, max_dev_60)


if __name__ == '__main__':

    run_case2(plot_res=True)
