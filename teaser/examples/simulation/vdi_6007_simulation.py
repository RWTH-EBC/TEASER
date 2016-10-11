#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example script for VDI 6007 simulation usage
"""

import numpy as np

import teaser.logic.simulation.VDI_6007.low_order_VDI as low_order_VDI


def vdi_example_6007():
    # Definition of time horizon
    times_per_hour = 60
    timesteps = 24 * 60 * times_per_hour  # 60 days
    timesteps_day = int(24 * times_per_hour)

    # Ventilation rate
    #  TODO: Substitute with TEASER call
    ventRate = np.zeros(timesteps)

    #  Solar radiation
    #  TODO: Substitute with TEASER call
    solarRad_in = np.zeros((timesteps, 1))
    source_igRad = np.zeros(timesteps)

    # Constant inputs
    #  TODO: Substitute with TEASER call
    alphaRad = np.zeros(timesteps) + 5

    #  TODO: Calculate with function call
    equalAirTemp = np.zeros(timesteps) + 295.15  # all temperatures in K
    weatherTemperature = np.zeros(timesteps) + 295.15  # in K

    # Variable inputs
    #  TODO: Substitute with TEASER boundary conditions
    Q_ig = np.zeros(timesteps_day)
    for q in range(int(6 * timesteps_day / 24), int(18 * timesteps_day / 24)):
        Q_ig[q] = 1000
    Q_ig = np.tile(Q_ig, 60)

    #  TODO: Substitute with TEASER type building call
    # Load constant house parameters
    houseData = {"R1i": 0.000595693407511,
                 "C1i": 14836354.6282,
                 "Ai": 75.5,
                 "RRest": 0.03895919557,
                 "R1o": 0.00436791293674,
                 "C1o": 1600848.94,
                 "Ao": [10.5],
                 "Aw": np.zeros(1),
                 "At": np.zeros(1),
                 "Vair": 52.5,
                 "rhoair": 1.19,
                 "cair": 0,
                 "splitfac": 0.09,
                 "g": 1,
                 "alphaiwi": 2.24,
                 "alphaowi": 2.7,
                 "alphaWall": 25 * 10.5,  # 25 * sum(Ao)
                 "withInnerwalls": True}

    #  TODO: What is krad?
    krad = 1

    # Define set points (prevent heating or cooling!)
    #  TODO: Calculate with function call
    t_set_heating = np.zeros(timesteps)  # in Kelvin
    t_set_cooling = np.zeros(timesteps) + 600  # in Kelvin

    heater_limit = np.zeros((timesteps, 3)) + 1e10
    cooler_limit = np.zeros((timesteps, 3)) - 1e10

    # Calculate indoor air temperature
    T_air, Q_hc, Q_iw, Q_ow = low_order_VDI.reducedOrderModelVDI(houseData,
                                                                 weatherTemperature,
                                                                 solarRad_in,
                                                                 equalAirTemp,
                                                                 alphaRad,
                                                                 ventRate,
                                                                 Q_ig,
                                                                 source_igRad,
                                                                 krad,
                                                                 t_set_heating,
                                                                 t_set_cooling,
                                                                 heater_limit,
                                                                 cooler_limit,
                                                                 heater_order=np.array(
                                                                     [1, 2,
                                                                      3]),
                                                                 cooler_order=np.array(
                                                                     [1, 2,
                                                                      3]),
                                                                 dt=int(
                                                                     3600 / times_per_hour))

    print('Indoor air temperature in Kelvin:')
    print(T_air)
    print()


if __name__ == '__main__':
    vdi_example_6007()
