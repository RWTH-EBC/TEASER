#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example script for VDI 6007 simulation usage
"""

import numpy as np

from teaser.project import Project
import teaser.logic.simulation.VDI_6007.weather as weat
import teaser.logic.simulation.VDI_6007.low_order_VDI as low_order_VDI
import teaser.logic.simulation.VDI_6007.equal_air_temperature as equ_air


def gen_res_type_example_building():
    """
    Generate example residential type building for VDI 6007 calculation

    Returns
    -------
    prj : object
        TEASER project instance
    """

    prj = Project(load_data=True)
    prj.name = "ArchetypeBuildings"
    prj.merge_windows_calc = True

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name='Test_res_building',
        year_of_construction=1962,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200,
        with_ahu=False,
        residential_layout=None,
        neighbour_buildings=None,
        attic=None,
        cellar=None,
        dormer=None,
        construction_type=None,
        number_of_apartments=None)

    return prj


def vdi_example_6007(thermal_zone, weather):
    """
    Example function to perform VDI 6007 calculation with thermal_zone

    Parameters
    ----------
    thermal_zone : object
        TEASER thermal zone object
    weather : object
        Weather object of TEASER
    """

    timesteps = 365 * 24

    # Load constant house parameters
    if len(thermal_zone.inner_walls) != 0:
        withInnerwalls = True
    else:
        withInnerwalls = False

    # Max. irradiation
    i_max = 100

    list_window_areas = []
    list_sunblind = []
    for window in thermal_zone.windows:
        list_window_areas.append(window.area)
        list_sunblind.append(0.0)

    # Convert into house data dictionary
    #  #-------------------------------------------------------
    houseData = {"R1i": thermal_zone.model_attr.r1_iw,
                 "C1i": thermal_zone.model_attr.c1_iw,
                 "Ai": thermal_zone.model_attr.area_iw,
                 "RRest": thermal_zone.model_attr.r_rest_ow,
                 "R1o": thermal_zone.model_attr.r1_ow,
                 "C1o": thermal_zone.model_attr.c1_ow,
                 "Ao": [thermal_zone.model_attr.area_ow],
                 "Aw": thermal_zone.model_attr.window_areas,
                 "At": thermal_zone.model_attr.transparent_areas,
                 "Vair": thermal_zone.volume,
                 "rhoair": thermal_zone.density_air,
                 "cair": thermal_zone.heat_capac_air,
                 "splitfac": thermal_zone.model_attr.ratio_conv_rad_inner_win,
                 "g": thermal_zone.model_attr.weighted_g_value,
                 "alphaiwi": thermal_zone.model_attr.alpha_comb_inner_iw,
                 "alphaowi": thermal_zone.model_attr.alpha_comb_inner_ow,
                 "alphaWall": thermal_zone.model_attr.alpha_comb_outer_ow * thermal_zone.model_attr.area_ow,
                 #"alphaowo": 25.0,
                 # TODO: Substitute with TEASER call (misc or outer walls)
                 "withInnerwalls": withInnerwalls,
                 "aowo": thermal_zone.model_attr.solar_absorp_ow,
                 #"epso": thermal_zone.model_attr.ir_emissivity_inner_ow,
                 #"orientationswallshorizontal": [90, 90, 90, 90, 0],
                 "temperatureground": thermal_zone.t_ground,
                 "weightfactorswall": thermal_zone.model_attr.weightfactor_ow,
                 "weightfactorswindow": thermal_zone.model_attr.weightfactor_win,
                 "weightfactorground": thermal_zone.model_attr.weightfactor_ground,
                 "gsunblind": thermal_zone.model_attr.g_sunblind,
                 "Imax": i_max}

    #  Solar radiation input on each external area in W/m2
    #  #-------------------------------------------------------
    # solarRad_in = np.zeros((timesteps, 5))
    solarRad_in = np.transpose(weather.sun_rad)

    source_igRad = np.zeros(timesteps)

    krad = 1

    #  Equal air temperature based on VDI in K
    #  #-------------------------------------------------------
    # #  equalAirTemp = np.zeros(timesteps) + 273.15 + 10
    # equalAirTemp = weather.temp + 0.5 + 273.15

    t_black_sky = np.zeros(timesteps) + 273.15

    sunblind_in = np.zeros_like(solarRad_in)
    sunblind_in[solarRad_in > i_max] = 0.85

    eq_air_params = {"aExt": thermal_zone.model_attr.solar_absorp_ow,
                     # coefficient of absorption of exterior walls (outdoor)
                     "eExt": thermal_zone.model_attr.ir_emissivity_outer_ow,
                     # coefficient of emission of exterior walls (outdoor)
                     "wfWall": thermal_zone.model_attr.weightfactor_ow,
                     # weight factors of the walls
                     "wfWin": thermal_zone.model_attr.weightfactor_win,
                     # weight factors of the windows
                     "wfGro": thermal_zone.model_attr.weightfactor_ground,
                     # weight factor of the ground (0 if not considered)
                     "T_Gro": thermal_zone.t_ground,
                     "alpha_wall_out": thermal_zone.model_attr.alpha_conv_outer_ow,
                     "alpha_rad_wall": thermal_zone.model_attr.alpha_rad_outer_ow,
                     "withLongwave": False}

    t_dry_bulb = weather.temp + 273.15

    equalAirTemp = equ_air.equal_air_temp(HSol=solarRad_in,
                                          TBlaSky=t_black_sky,
                                          TDryBul=t_dry_bulb,
                                          sunblind=sunblind_in,
                                          params=eq_air_params)

    #  Environment temperatures in K
    #  #-------------------------------------------------------
    # weatherTemperature = np.zeros(timesteps) + 273.15 + 10  # in K
    weatherTemperature = weather.temp + 273.15

    #  Ventilation rate: Fresh air at temperature weatherTemperature in m3/s
    #  #-------------------------------------------------------
    # ventRate = np.zeros(timesteps)
    ventRate = np.zeros(timesteps) + (thermal_zone.volume *
                                      thermal_zone.infiltration_rate / 3600)

    #  Internal convective gains in W
    #  #-------------------------------------------------------
    #  TODO: Substitute with TEASER boundary conditions
    #  logic/buildingobjects/boundaryconditions/boundaryconditions.py
    #  Living (18599) / SIA for occupancy
    Q_ig = np.zeros(timesteps) + 200

    # Radiative heat transfer coef. between inner and outer walls in W/m2K
    alphaRad = np.zeros(timesteps) + \
               thermal_zone.model_attr.alpha_rad_inner_mean

    # Define set points for heating
    #  #-------------------------------------------------------
    #  TODO: Calculate with function call (depending on occupancy)
    # t_set_heating = np.zeros(timesteps) + 273.15 + 21  # in Kelvin
    t_set_heat_day = \
        np.array([18, 18, 18, 18, 18, 18, 21, 21, 21, 21, 21, 21,
                  21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 18]) + 273.15
    t_set_heating = np.tile(t_set_heat_day, 365)

    # Define set points for cooling (cooling is disabled for high values)
    #  #-------------------------------------------------------
    t_set_cooling = np.zeros(timesteps) + 273.15 + 1000  # in Kelvin

    heater_limit = np.zeros((timesteps, 3)) + 1e10
    cooler_limit = np.zeros((timesteps, 3)) - 1e10

    # Calculate indoor air temperature with VDI model
    T_air, Q_hc, Q_iw, Q_ow = \
        low_order_VDI.reducedOrderModelVDI(houseData=houseData,
                                           weatherTemperature=weatherTemperature,
                                           solarRad_in=solarRad_in,
                                           equalAirTemp=equalAirTemp,
                                           alphaRad=alphaRad,
                                           ventRate=ventRate,
                                           Q_ig=Q_ig,
                                           source_igRad=source_igRad,
                                           krad=krad,
                                           heater_order=np.array([1, 2, 3]),
                                           cooler_order=np.array([1, 2, 3]),
                                           t_set_heating=t_set_heating,
                                           t_set_cooling=t_set_cooling,
                                           heater_limit=heater_limit,
                                           cooler_limit=cooler_limit)

    return (T_air, Q_hc, Q_iw, Q_ow)


if __name__ == '__main__':

    #  Get TEASER project with residential type building
    prj = gen_res_type_example_building()

    #  Pointer to building object
    building = prj.buildings[0]

    #  Extract thermal_zone
    thermal_zone = prj.buildings[0].thermal_zones[0]

    #  Calculate beta angle
    beta = thermal_zone.model_attr.tilt_facade

    #  Calculate gamma angle
    #  TEASER definition
    #  orientation_facade: list of floats[degree]
    #         Orientation of facades(Azimuth).
    #         0 - North
    #         90 - East
    #         180 - South
    #         270 - West
    #   TEASER: [180.0, -1, 0.0, -2, 90.0, 270.0]
    #   South, horizontal, North, ground, east, west
    #  VDI: [-180, -90, 0, 90, 0, 0],  # north, east, south, west, horizontal
    gamma = thermal_zone.model_attr.orientation_facade

    #  Recalculate to VDI core azimuth usage
    for i in range(len(gamma)):
        angle = gamma[i]
        if angle == -1 or angle == -2:
            gamma[i] = 0.0
        else:
            gamma[i] = angle - 180

    weather = weat.Weather(
        beta=beta,
        gamma=gamma,
        weather_path=None,
        albedo=0.2,
        timeZone=1,
        altitude=0,
        location=(49.5, 8.5),
        timestep=3600,
        do_sun_rad=True)

    print('UA value before retrofiting:')
    print(prj.buildings[0].thermal_zones[0].outer_walls[0].ua_value)
    print('Inner resistance (VDI 6007) of thermal zone before retrofit:')
    print(thermal_zone.model_attr.r1_ow)
    print()

    #  Perform simulation for unretrofited model
    (T_air, Q_hc1, Q_iw, Q_ow) = vdi_example_6007(thermal_zone,
                                                  weather=weather)

    q_heat1 = np.zeros(len(Q_hc1))
    q_cool1 = np.zeros(len(Q_hc1))
    for i in range(len(Q_hc1)):
        if Q_hc1[i] > 0:
            q_heat1[i] = Q_hc1[i]
        elif Q_hc1[i] < 0:
            q_cool1[i] = Q_hc1[i]

    print('Sum of heating energy in kWh:')
    print(sum(q_heat1) / 1000)

    print('Sum of cooling energy in kWh:')
    print(-sum(q_cool1) / 1000)

    #  Do retrofit of building
    building.retrofit_building(year_of_retrofit=2014)

    print('UA value after retrofiting:')
    print(prj.buildings[0].thermal_zones[0].outer_walls[0].ua_value)
    print('Inner resistance (VDI 6007) of thermal zone after retrofit:')
    print(thermal_zone.model_attr.r1_ow)
    # print()
    thermal_zone = prj.buildings[0].thermal_zones[0]

    #  Rund VDI 6007 example with thermal zone
    (T_air, Q_hc, Q_iw, Q_ow) = vdi_example_6007(thermal_zone, weather=weather)

    print('Indoor air temperature in Kelvin:')
    print(T_air)
    print()

    print('Heating(+) / cooling(-) load in Watt:')
    print(Q_hc)
    print()

    q_heat = np.zeros(len(Q_hc))
    q_cool = np.zeros(len(Q_hc))
    for i in range(len(Q_hc)):
        if Q_hc[i] > 0:
            q_heat[i] = Q_hc[i]
        elif Q_hc[i] < 0:
            q_cool[i] = Q_hc[i]

    print('Sum of heating energy in kWh (after retrofit):')
    print(sum(q_heat) / 1000)

    print('Sum of cooling energy in kWh (after retrofit):')
    print(-sum(q_cool) / 1000)

    import matplotlib.pyplot as plt

    fig = plt.figure()
    fig.add_subplot(411)
    plt.plot(weather.temp)
    plt.ylabel('Outdoor air\ntemperature in\ndegree Celsius')
    fig.add_subplot(412)
    plt.plot(weather.sun_rad[0])
    plt.ylabel('Sun radiation\non surface 0')  # TODO: Add unit
    fig.add_subplot(413)
    plt.plot(T_air - 273.15)
    plt.ylabel('Indoor air\ntemperature in\ndegree Celsius')
    fig.add_subplot(414)
    plt.plot(Q_hc1 / 1000, color="Red")
    plt.plot(Q_hc / 1000)

    plt.ylabel('Heating/cooling\npower (+/-)\nin kW')
    plt.xlabel('Time in hours')
    plt.show()
