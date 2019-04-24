#!/usr/bin/env python
# coding=utf-8
"""
Shared code for all VDI 6007 test cases
"""

import numpy as np

from teaser.project import Project
from teaser.logic.buildingobjects.building import Building
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.calculation.two_element import TwoElement
from teaser.data.weatherdata import WeatherData


def prepare_thermal_zone(timesteps):
    """Prepare the thermal zone for running VDI test case

    Parameters
    ----------
    timesteps : int
        Number of time steps

    Returns
    -------
    tz : teaser.logic.buildingobjects.thermalzone.ThermalZone
        Thermal zone object with setup for test case
    """

    weather = WeatherData()
    weather.air_temp = np.zeros(timesteps) + 295.15

    prj = Project()
    prj.weather_data = weather

    bldg = Building(prj)
    tz = ThermalZone(bldg)

    model_data = TwoElement(tz, merge_windows=False, t_bt=5)

    # Building parameters
    model_data.r1_iw = 0.000595693407511
    model_data.c1_iw = 14836354.6282
    model_data.area_iw = 75.5
    model_data.r_rest_ow = 0.03895919557
    model_data.r1_ow = 0.00436791293674
    model_data.c1_ow = 1600848.94
    model_data.area_ow = 10.5
    model_data.outer_wall_areas = [10.5]
    model_data.window_areas = np.zeros(1)
    model_data.transparent_areas = np.zeros(1)
    tz.volume = 52.5
    tz.density_air = 1.19
    tz.heat_capac_air = 0
    model_data.ratio_conv_rad_inner_win = 0.09
    model_data.weighted_g_value = 1
    model_data.alpha_comb_inner_iw = 2.24
    model_data.alpha_comb_inner_ow = 2.7
    model_data.alpha_conv_outer_ow = 20
    model_data.alpha_rad_outer_ow = 5
    model_data.alpha_comb_outer_ow = 25
    model_data.alpha_rad_inner_mean = 5

    tz.model_attr = model_data

    return tz

