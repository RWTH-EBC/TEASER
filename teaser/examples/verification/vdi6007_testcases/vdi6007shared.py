#!/usr/bin/env python
# coding=utf-8
"""
Shared code for all VDI 6007 test cases
"""

import matplotlib.pyplot as plt
import numpy as np

from teaser.project import Project
from teaser.logic.buildingobjects.building import Building
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.calculation.two_element import TwoElement
from teaser.data.weatherdata import WeatherData


def prepare_thermal_zone(timesteps, room, weather=None):
    """Prepare the thermal zone for running VDI test case

    Parameters
    ----------
    timesteps : int
        Number of time steps
    room : str
        Type of room {"S1", "S2", "L"}; "S" indicates "small", "L" indicates "large";
        the numbers 1 and 2 indicate the number of exterior walls
    weather : numpy.array
        Optional weather input

    Returns
    -------
    tz : teaser.logic.buildingobjects.thermalzone.ThermalZone
        Thermal zone object with setup for test case
    """

    if weather is None:
        weather = WeatherData()
        weather.air_temp = np.zeros(timesteps) + 295.15

    prj = Project()
    prj.weather_data = weather

    bldg = Building(prj)
    tz = ThermalZone(bldg)

    model_data = TwoElement(tz, merge_windows=False, t_bt=5)

    if room == "S1":
        model_data.r1_iw = 0.000595693407511
        model_data.c1_iw = 14836354.6282
        model_data.area_iw = 75.5
        model_data.r_rest_ow = 0.03895919557
        model_data.r1_ow = 0.00436791293674
        model_data.c1_ow = 1600848.94
    elif room == "S2":
        model_data.r1_iw = 0.000668895639141
        model_data.c1_iw = 12391363.8631
        model_data.area_iw = 60.5
        model_data.r_rest_ow = 0.01913729904
        model_data.r1_ow = 0.0017362530106
        model_data.c1_ow = 5259932.23
    elif room == "L":
        model_data.r1_iw = 0.003237138
        model_data.c1_iw = 7297100
        model_data.area_iw = 75.5
        model_data.r_rest_ow = 0.039330865
        model_data.r1_ow = 0.00404935160802
        model_data.c1_ow = 47900
    else:
        raise LookupError("Unknown room type selected. Choose from {'S1', 'S2', 'L'}")

    if room == "S2":
        model_data.area_ow = 25.5
        model_data.outer_wall_areas = [10.5, 15]
        model_data.window_areas = [0, 0]
        model_data.transparent_areas = [7, 7]
    else:
        model_data.area_ow = 10.5
        model_data.outer_wall_areas = [10.5]
        model_data.window_areas = np.zeros(1)
        model_data.transparent_areas = np.zeros(1)

    tz.volume = 52.5
    tz.density_air = 1.19
    tz.heat_capac_air = 0

    model_data.ratio_conv_rad_inner_win = 0.09
    model_data.weighted_g_value = 1
    if room == "S2":
        model_data.alpha_comb_inner_iw = 2.12
    else:
        model_data.alpha_comb_inner_iw = 2.24
    model_data.alpha_comb_inner_ow = 2.7
    model_data.alpha_conv_outer_ow = 20
    model_data.alpha_rad_outer_ow = 5
    model_data.alpha_comb_outer_ow = 25
    model_data.alpha_rad_inner_mean = 5

    tz.model_attr = model_data

    return tz


def hourly_average(data, times_per_hour):
    """Calculate the hourly average of the data in smaller time steps

    Parameters
    ----------
    data : numpy.array
        Input data in small time steps
    times_per_hour : int
        Number of time steps per hour (usually 60: 1 for each minute)

    Returns
    -------
    result : numpy.array
        Output data in hourly averages
    """

    result = np.array(
        [
            np.mean(data[i * times_per_hour : (i + 1) * times_per_hour])
            for i in range(24 * 60)
        ]
    )

    return result


def plot_result(res, ref, title, temperature_or_heat, res_raw=None):
    """Plot result comparison to reference values

    Parameters
    ----------
    res : numpy.array
        Simulation result (averaged values)
    ref : numpy.array
        Reference values
    title : str
        Title of the plot
    temperature_or_heat : str
        Decide between {"temperature", "heat"}
    """

    if temperature_or_heat == "temperature":
        y_label_top = "Temperature in °C"
        y_label_bottom = "Temperature difference in K"
    elif temperature_or_heat == "heat":
        y_label_top = "Heat load in W"
        y_label_bottom = "Heat load difference in W"
    else:
        raise LookupError("Unknown plot type. Must be 'temperature' or 'heat'")

    plt.figure()
    ax_top = plt.subplot(211)
    plt.plot(ref, label="Reference", color="black", linestyle="--")
    plt.plot(res, label="Simulation", color="blue", linestyle="-")
    plt.scatter(range(len(ref)), ref, color="black", marker="x")
    plt.scatter(range(len(res)), res, color="blue", marker="o")
    if res_raw is not None:
        plt.plot(
            [x / 60 for x in range(len(res_raw))],
            res_raw,
            color="red",
            linestyle="dotted",
            alpha=0.5,
            label="Simulation raw output"
        )

    plt.legend()
    plt.ylabel(y_label_top)

    plt.title(title)

    plt.subplot(212, sharex=ax_top)
    plt.plot(res - ref, label="Ref. - Sim.")
    plt.legend()
    plt.ylabel(y_label_bottom)
    plt.xticks([4 * i for i in range(7)])
    plt.xlim([1, 24])
    plt.xlabel("Time in h")

    plt.show()


def prepare_internal_gains_rad(timesteps_day):
    """Prepare a time series of prescribed internal radiative gains

    Parameters
    ----------
    timesteps_day : int
        Number of time steps in a day

    Returns
    -------
    result : numpy.array
        Time series of prescribed internal radiative gains
    """
    result = np.zeros(timesteps_day)
    for q in range(int(6 * timesteps_day / 24), int(18 * timesteps_day / 24)):
        result[q] = 1000
    result = np.tile(result, 60)

    return result
