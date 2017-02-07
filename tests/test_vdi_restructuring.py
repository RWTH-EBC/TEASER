#!/usr/bin/env python
# coding=utf-8
"""
Script to check functionality of VDI 6007 core after restructuring
(see issue #297)
"""

import os
import numpy as np

from teaser.project import Project
import teaser.logic.simulation.VDI_6007.weather as weat
import teaser.logic.simulation.VDI_6007.low_order_VDI as low_order_VDI
import teaser.logic.simulation.VDI_6007.equal_air_temperature as equ_air


class Test_VDI_Restructure(object):

    def test_sim_results(self):

        #  Generate project and add residential building

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
            net_leased_area=100,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=1,
            cellar=1,
            dormer=0,
            construction_type='heavy',
            number_of_apartments=None)

        #  Extract thermal_zone
        thermal_zone = prj.buildings[0].thermal_zones[0]

        #  Calculate beta angle
        beta = thermal_zone.model_attr.tilt_facade

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
                     "withInnerwalls": withInnerwalls,
                     "aowo": thermal_zone.model_attr.solar_absorp_ow,
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
        t_air, q_hc, q_iw, q_ow = \
            low_order_VDI.reducedOrderModelVDI(houseData=houseData,
                                               weatherTemperature=weatherTemperature,
                                               solarRad_in=solarRad_in,
                                               equalAirTemp=equalAirTemp,
                                               alphaRad=alphaRad,
                                               ventRate=ventRate,
                                               Q_ig=Q_ig,
                                               source_igRad=source_igRad,
                                               krad=krad,
                                               heater_order=np.array(
                                                   [1, 2, 3]),
                                               cooler_order=np.array(
                                                   [1, 2, 3]),
                                               t_set_heating=t_set_heating,
                                               t_set_cooling=t_set_cooling,
                                               heater_limit=heater_limit,
                                               cooler_limit=cooler_limit)

        #  Load reference values
        this_path = os.path.dirname(os.path.abspath(__file__))
        filename = 'res_unretrofited.txt'
        load_path = os.path.join(this_path, 'inputs', filename)

        load_array = np.genfromtxt(fname=load_path, delimiter='\t',
                                   skip_header=1)

        temp_ref = load_array[:, 0]
        q_hc_ref = load_array[:, 1]

        np.testing.assert_array_almost_equal(t_air, temp_ref, decimal=3)
        np.testing.assert_array_almost_equal(q_hc, q_hc_ref, decimal=3)

        #  Do retrofit of building
        prj.buildings[0].retrofit_building(year_of_retrofit=2014)

        # Calculate indoor air temperature with VDI model
        t_air2, q_hc2, q_iw, q_ow = \
            low_order_VDI.reducedOrderModelVDI(houseData=houseData,
                                               weatherTemperature=weatherTemperature,
                                               solarRad_in=solarRad_in,
                                               equalAirTemp=equalAirTemp,
                                               alphaRad=alphaRad,
                                               ventRate=ventRate,
                                               Q_ig=Q_ig,
                                               source_igRad=source_igRad,
                                               krad=krad,
                                               heater_order=np.array(
                                                   [1, 2, 3]),
                                               cooler_order=np.array(
                                                   [1, 2, 3]),
                                               t_set_heating=t_set_heating,
                                               t_set_cooling=t_set_cooling,
                                               heater_limit=heater_limit,
                                               cooler_limit=cooler_limit)

        #  Load reference values
        this_path = os.path.dirname(os.path.abspath(__file__))
        filename2 = 'res_retrofited.txt'
        load_path2 = os.path.join(this_path, 'inputs', filename2)

        load_array2 = np.genfromtxt(fname=load_path2, delimiter='\t',
                                    skip_header=1)

        temp_ref2 = load_array2[:, 0]
        q_hc_ref2 = load_array2[:, 1]

        np.testing.assert_array_almost_equal(t_air2, temp_ref2, decimal=3)
        np.testing.assert_array_almost_equal(q_hc2, q_hc_ref2, decimal=3)
