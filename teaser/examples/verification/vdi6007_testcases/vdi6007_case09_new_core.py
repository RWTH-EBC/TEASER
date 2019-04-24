#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
import os
import numpy as np

from teaser.project import Project
from teaser.logic.buildingobjects.building import Building
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.calculation.two_element import TwoElement
from teaser.logic.simulation.vdi_core import VDICore

# import customized weather class
from teaser.data.weatherdata import WeatherData

import teaser.examples.verification.vdi6007_testcases.vdi6007_case01 as vdic


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

    prj = Project()
    prj.weather_data = weather

    bldg = Building(prj)

    tz = ThermalZone(bldg)

    model_data = TwoElement(tz, merge_windows=True, t_bt=5)

    #  Store building parameters for testcase 1
    model_data.r1_iw = 0.000668895639141
    model_data.c1_iw = 12391363.8631
    model_data.area_iw = 60.5
    model_data.r_rest_ow = 0.01913729904
    model_data.r1_ow = 0.0017362530106
    model_data.c1_ow = 5259932.23
    model_data.area_ow = 25.5
    model_data.outer_wall_areas = [10.5, 15]
    model_data.window_areas = [0, 0]
    model_data.transparent_areas = [7, 7]
    tz.volume = 52.5
    tz.density_air = 1.19
    tz.heat_capac_air = 0
    tz.t_ground = 285.15
    model_data.ratio_conv_rad_inner_win = 0.09
    model_data.weighted_g_value = 1
    model_data.alpha_comb_inner_iw = 2.12
    model_data.alpha_comb_inner_ow = 2.7
    model_data.alpha_conv_outer_ow = 20
    model_data.alpha_rad_outer_ow = 5
    model_data.alpha_comb_outer_ow = 25
    model_data.alpha_rad_inner_mean = 5

    model_data.solar_absorp_ow = 0.7
    model_data.ir_emissivity_outer_ow = 0.9
    model_data.weightfactor_ow = [0.05796831135677373, 0.13249899738691134]
    model_data.weightfactor_win = [0.4047663456281575, 0.4047663456281575]
    model_data.weightfactor_ground = 0

    tz.model_attr = model_data

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

    T_air_c = t_air - 273.15
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
    run_case9(plot_res=True)
