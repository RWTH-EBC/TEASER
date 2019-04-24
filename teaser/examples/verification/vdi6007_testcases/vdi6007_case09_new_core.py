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
from teaser.data.weatherdata import WeatherData


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

    weather = WeatherData()
    weather.air_temp = weatherTemperature

    tz = prepare_thermal_zone(timesteps, room="S2", weather=weather)

    # Adjust settings for this test case
    tz.t_ground = 285.15
    tz.model_attr.solar_absorp_ow = 0.7
    tz.model_attr.ir_emissivity_outer_ow = 0.9
    tz.model_attr.weightfactor_ow = [0.05796831135677373, 0.13249899738691134]
    tz.model_attr.weightfactor_win = [0.4047663456281575, 0.4047663456281575]
    tz.model_attr.weightfactor_ground = 0

    calc = VDICore(tz)

    calc.t_set_heating = np.zeros(timesteps)  # in Kelvin
    calc.t_set_cooling = np.zeros(timesteps) + 600  # in Kelvin

    calc.heater_limit = np.zeros((timesteps, 3)) + 1e10
    calc.cooler_limit = np.zeros((timesteps, 3)) - 1e10

    calc.internal_gains_rad = source_igRad
    calc.internal_gains = Q_ig

    calc.solar_rad_in = solarRad_win_in

    calc.equal_air_temp = calc._eq_air_temp(
        h_sol=solarRad_wall_tiled,
        t_black_sky=t_black_sky)

    t_air, q_air_hc = calc.simulate()

    T_air_mean = hourly_average(data=t_air-273.15, times_per_hour=times_per_hour)

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

    if plot_res:
        plot_result(T_air_1, T_air_ref_1, "Results day 1", "temperature")
        plot_result(T_air_10, T_air_ref_10, "Results day 10", "temperature")
        plot_result(T_air_60, T_air_ref_60, "Results day 60", "temperature")

    max_dev_1 = np.max(np.abs(T_air_1 - T_air_ref_1))
    max_dev_10 = np.max(np.abs(T_air_10 - T_air_ref_10))
    max_dev_60 = np.max(np.abs(T_air_60 - T_air_ref_60))

    print("Max. deviation day 1: " + str(max_dev_1))
    print("Max. deviation day 10: " + str(max_dev_10))
    print("Max. deviation day 60: " + str(max_dev_60))

    return (max_dev_1, max_dev_10, max_dev_60)


if __name__ == '__main__':
    run_case9(plot_res=True)
