#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
VDI 6007 low order model TEASER implementation
"""

import numpy as np


def _to_hourly(vals, ts=60):
    val = np.array([np.mean(vals[i * ts:(i + 1) * ts]) for i in range(24)])

    return val


def _calc_splitfactors(cols, A_array, A_ext, A_win):
    """
    This is a direct translation from RC --> BaseClasses --> splitFacVal
    
    Parameters
    ----------
    cols : int
        Number of orientations
    A_array : list
        [ATotExt, ATotWin]
    A_ext : list
        Vector of exterior wall areas
    A_win : list
        Vector of window areas
    
    Example
    -------
    >>> # Define areas
    >>> A_ext = [10.5]
    >>> A_win = [0]
    >>> A_int = 75.5
    >>> A_ar = [sum(A_ext), sum(A_win), A_int]
    >>> # Calculate split factors for inner walls and outside walls
    >>> splitFac_IW = _calc_splitfactors(dim, 1, A_ar, [0], [0])
    >>> splitFac_OW = _calc_splitfactors(dim, len(A_ext), A_ar, A_ext, A_win)
    """

    A_tot = sum(A_array)  # total area

    rows = sum([1 if A > 0 else 0 for A in A_array])
    rows = len(A_array)

    # Counters
    i = 0  # A_array
    j = 0  # Row
    k = 0  # Column

    result = np.zeros((rows, cols))

    for A in A_array:
        if A > 0:
            k = 0
            if i == 0:
                for A_wall in A_ext:
                    result[j, k] = (A - A_wall) / (A_tot - A_wall - A_win[k])
                    k += 1
            elif i == 1:
                for A_wall in A_ext:
                    result[j, k] = (A - A_win[k]) / (A_tot - A_wall - A_win[k])
                    k += 1
            else:
                for A_wall in A_ext:
                    result[j, k] = A / (A_tot - A_wall - A_win[k])
                    k += 1
            j += 1
        i += 1

    return result


def reducedOrderModelVDI(houseData, weatherTemperature, solarRad_in,
                         equalAirTemp, alphaRad, ventRate,
                         Q_ig, source_igRad, krad,
                         t_set_heating, t_set_cooling,
                         heater_limit=[1e10, 1e10, 1e10],
                         cooler_limit=[-1e10, -1e10, -1e10],
                         heater_order=np.array([1, 2, 3]),
                         cooler_order=np.array([1, 2, 3]), dt=3600,
                         T_air_init=295.15, T_iw_init=295.15,
                         T_ow_init=295.15):
    """
    Compute indoor air temperature and necessary (convective) heat gains from
    an ideal heater/cooler based on the VDI 6007-1 model.
    
    Parameters
    ----------
    houseData: dict
        Dictionary describing the building physics. The following entries are
        required:
        
        - withInnerwalls : Boolean
            True if inner walls are considered, False if not
        - R1i : Float
            Heat resistance inner walls in K/W
        - C1i : Float
            Capacity of inner walls in ``Wh/K``
        - Ai : Float
            Surface area of inner walls in m2
        - RRest : Float
            Heat resistance between outer wall's capacity and environment in K/W
        - R1o : Float
            Heat resistance outer walls in K/W
        - C1o : Float
            Capacity of outer walls in ``Wh/K``
        - Ao : List of Floats
            Surface areas of outer walls in each direction in m2
        - Aw : List of Floats
            Window areas in each direction in m2
        - Vair : Float
            Room's indoor air volume in m3
        - rhoair : Float
            Density of air in kg/m3
        - cair : Float
            Specific heat capacity of air in Wh/kgK
        - splitfac : Float
            Factor for conv. part of rad. through windows (w/o unit)
        - g : Float
            Total energy transmittance of windows (w/o unit)
        - alphaiwi : Float
            Inner wall's coefficient of heat transfer (inner side) in W/m2K
        - alphaowi : Float
            Outer wall's coefficient of heat transfer (inner side) in W/m2K
    weatherTemperature : List of Float
        Environment temperatures in K
    solarRad_in : 2d-array (float)
        Solar radiation input on each external area in W/m2
    equalAirTemp : List of Float
        Equal air temperature based on VDI in K
    alphaRad : List of Float
        Radiative heat transfer coef. between inner and outer walls in W/m2K
    ventRate : List of Float
        Fresh air at temperature weatherTemperature in m3/s
    Q_ig : List of Float
        Internal convective gains in W
    source_igRad
    krad
    t_set_heating : List of Float
        Heating set temperatures. If the air temperature without heating drops
        below this temperature, a heating load that just fulfills this 
        temperature is computed
    t_set_cooling : List of Float
        Cooling set temperatures. If the air temperature without heating rises
        above this temperature, a cooling load that just fulfills this 
        temperature is computed
    dt : Float
        Length of one timestep in hours. Standard is 1 hour
    T_air_init : Float
        Initial air temperature in Kelvin
    T_iw_init : Float
        Initial temperature of the inner wall's capacity in Kelvin
    T_ow_init : Float
        Initial temperature of the outer wall's capacity  in Kelvin
    
    Returns
    -------
    T_air : Array of Float
        Indoor air temperature in Kelvin
    Q_HC : Array of Float
        Heating (positive) and cooling (negative) loads in Watt

    #  TODO: Add further return values and descriptions

    Current limitations
    -------------------
    1. Only written for thermal zones with windows, internal walls and 
       external walls
    """
    # %% partialReducedOrderModel
    # parameters

    timesteps = len(alphaRad)

    withInnerwalls = houseData["withInnerwalls"]  # If inner walls are existent
    #    withWindows     = houseData["withWindows"]      # If windows are existent
    #    withOuterwalls  = houseData["withOuterwalls"]   # If outer walls (including windows) are existent

    R1i = houseData["R1i"]  # Resistor 1 inner wall
    C1i = houseData["C1i"]  # Capacity 1 inner wall in Wh/K
    Ai = houseData["Ai"]  # Inner wall area
    RRest = houseData["RRest"]  # Resistor Rest outer wall
    R1o = houseData["R1o"]  # Resistor 1 outer wall
    C1o = houseData["C1o"]  # Capacity 1 outer wall in Wh/K
    Ao = houseData["Ao"]  # Outer wall area
    Aw = houseData["Aw"]  # Window area
    At = houseData["At"]  # Transmitting area

    Vair = houseData["Vair"]  # Volume of the air in the zone
    rhoair = houseData["rhoair"]  # Density of the air
    cair = houseData["cair"]  # Heat capacity of the air in Wh/KgK
    splitfac = houseData[
        "splitfac"]  # Factor for conv. part of rad. through windows

    g = houseData["g"]  # Total energy transmittance

    alphaiwi = houseData[
        "alphaiwi"]  # Coefficient of heat transfer for inner walls
    alphaowi = houseData[
        "alphaowi"]  # Outer wall's coefficient of heat transfer (inner side)
    alphaWall = houseData[
        "alphaWall"]  # Heat transfer between exterior wall and eq. air temp.

    A_win_tot = sum(Aw)
    Ao_tot = sum(Ao)
    A_ar = [Ao_tot, A_win_tot, Ai]

    # Adjust RRest to incorporate alphaWall
    RRest = RRest + 1 / alphaWall

    # %% Time variable inputs
    # convective heat entry from solar iradiation
    e_solar_conv = np.zeros((timesteps, len(At)))

    for i in range(len(At)):
        e_solar_conv[:, i] = solarRad_in[:, i] * splitfac * g * At[i]
    Q_solar_conv = np.sum(e_solar_conv, axis=1)

    # splitters:
    # on each splitter: one output goes to outer wall, one goes to inner wall
    # therefore dimension is 2 if inner walls exist => 2 outgoing signals
    splitFacSolar = _calc_splitfactors(len(Ao), A_ar, Ao, Aw)
    # therm. splitter solar radiative:
    e_solar_rad = np.zeros((timesteps, len(At)))
    for i in range(len(At)):
        e_solar_rad[:, i] = solarRad_in[:, i] * (splitfac - 1) * g * At[i]
    Q_solar_rad = np.zeros((timesteps, len(Ao), splitFacSolar.shape[0]))
    for i in range(len(Ao)):
        for j in range(splitFacSolar.shape[0]):
            Q_solar_rad[:, i, j] = -e_solar_rad[:, i] * splitFacSolar[j, i]

    Q_solarRadToInnerWall = np.sum(Q_solar_rad[:, :, 1], axis=1)
    Q_solarRadToOuterWalli = np.sum(Q_solar_rad[:, :, 0], axis=1)

    # therm. splitter loads radiative:
    Q_loads_rad = krad * source_igRad
    splitFacLoads = _calc_splitfactors(1, A_ar, [0], [0])

    Q_loadsToInnerWall = Q_loads_rad * splitFacLoads[1, 0]
    Q_loadsToOuterWalli = Q_loads_rad * splitFacLoads[0, 0]

    # %% Define system of linear equations:
    # A * x = rhs
    # x = [T_ow, T_owi, T_iw, T_iwi, T_air, Q_air, Q_HC_air, Q_HC_iw, Q_HC_ow] (all at time t)

    # Results' initialization
    T_ow = []
    T_owi = []
    T_iw = []
    T_iwi = []
    T_air = []
    Q_air = []
    Q_airHC = []
    Q_iwHC = []
    Q_owHC = []

    # Initial temperatures
    T_ow_prev = T_ow_init
    T_iw_prev = T_iw_init
    T_air_prev = T_air_init

    for t in range(timesteps):

        if t == 360:
            pass

        # Common equations
        A = np.zeros((9, 9))
        rhs = np.zeros(A.shape[0])

        # Fill matrix coefficients
        A[0, 0] = C1o / dt + 1 / RRest + 1 / R1o
        A[0, 1] = -1 / R1o
        A[1, 0] = 1 / R1o
        A[1, 1] = -min(Ao_tot, Ai) * alphaRad[t] - Ao_tot * alphaowi - 1 / R1o
        A[1, 3] = min(Ao_tot, Ai) * alphaRad[t]
        A[1, 4] = Ao_tot * alphaowi
        A[1, 8] = 1
        A[2, 2] = C1i / dt + 1 / R1i
        A[2, 3] = -1 / R1i
        A[3, 1] = min(Ao_tot, Ai) * alphaRad[t]
        A[3, 2] = 1 / R1i
        A[3, 3] = -min(Ao_tot, Ai) * alphaRad[t] - Ai * alphaiwi - 1 / R1i
        A[3, 4] = Ai * alphaiwi
        A[3, 7] = 1
        A[4, 1] = Ao_tot * alphaowi
        A[4, 3] = Ai * alphaiwi
        A[4, 4] = -Ao_tot * alphaowi - Ai * alphaiwi - ventRate[
                                                           t] * cair * rhoair
        A[4, 5] = -1
        A[4, 6] = 1
        A[5, 4] = Vair * cair * rhoair / dt
        A[5, 5] = -1

        # Fill right hand side
        rhs[0] = equalAirTemp[t] / RRest + C1o * T_ow_prev / dt
        rhs[1] = -Q_solarRadToOuterWalli[t] - Q_loadsToOuterWalli[t]
        rhs[2] = C1i * T_iw_prev / dt
        rhs[3] = -Q_solarRadToInnerWall[t] - Q_loadsToInnerWall[t]
        rhs[4] = -ventRate[t] * cair * rhoair * weatherTemperature[t] - \
                 Q_solar_conv[t] - Q_ig[t]
        rhs[5] = rhoair * cair * Vair * T_air_prev / dt

        # Calculate current time step
        x = _calc_timestep(A, rhs, t_set_heating[t], t_set_cooling[t],
                           heater_limit[t, :], cooler_limit[t, :],
                           heater_order, cooler_order)

        # Retrieve results
        T_ow.append(x[0])
        T_owi.append(x[1])
        T_iw.append(x[2])
        T_iwi.append(x[3])
        T_air.append(x[4])
        Q_air.append(x[5])
        Q_airHC.append(x[6])
        Q_iwHC.append(x[7])
        Q_owHC.append(x[8])

        # Update initial temperatures
        T_ow_prev = x[0]
        T_iw_prev = x[2]
        T_air_prev = x[4]

    return (
        np.array(T_air), np.array(Q_airHC), np.array(Q_iwHC), np.array(Q_owHC))


def _calc_timestep(A, rhs, t_set_heating=291.15, t_set_cooling=300.15,
                   heater_limit=[1e10, 1e10, 1e10],
                   cooler_limit=[-1e10, -1e10, -1e10],
                   heater_order=np.array([1, 2, 3]),
                   cooler_order=np.array([1, 2, 3])):
    """
    Calculate the temperatures and heat flow rate for the current time step.
    
    Parameters
    ----------
    A : 2d array of floats
        Coefficients describing the VDI model
    rhs : Array of floats
        Right hand side of these equations
    t_set_heating : Float
        Temperature below which heating demand is computed (in Kelvin)
    t_set_cooling : Float
        Temperature above which cooling demand is computed (in Kelvin)
    """
    # Calculate without further heat inputs to determine if heating 
    # or cooling is needed
    # x = [T_ow, T_owi, T_iw, T_iwi, T_air, Q_air, Q_HC]
    x_noHeat = _calc_temperatue(A, rhs, q_air_fix=0, q_iw_fix=0, q_ow_fix=0)

    if x_noHeat[4] < t_set_heating:
        # Indoor air temperature below heating set temperature

        # Use primary heater
        if np.argmax(heater_order == 1) == 0 and heater_limit[0] > 0:
            x_heating_1 = _calc_heatflow(A, rhs, t_air_set=t_set_heating,
                                         q_air_fix=None, q_iw_fix=0,
                                         q_ow_fix=0)
            if x_heating_1[6] > heater_limit[0]:
                x_maxheat_1 = _calc_temperatue(A, rhs,
                                               q_air_fix=heater_limit[0],
                                               q_iw_fix=0, q_ow_fix=0)

                if x_maxheat_1[4] < t_set_heating:
                    if np.argmax(heater_order == 2) == 1 and heater_limit[
                        1] > 0:
                        x_heating_2 = _calc_heatflow(A, rhs,
                                                     t_air_set=t_set_heating,
                                                     q_air_fix=heater_limit[0],
                                                     q_iw_fix=None, q_ow_fix=0)

                        if x_heating_2[7] > heater_limit[1]:
                            x_maxheat_2 = _calc_temperatue(A, rhs, q_air_fix=
                            heater_limit[0], q_iw_fix=heater_limit[1],
                                                           q_ow_fix=0)

                            if x_maxheat_2[4] < t_set_heating and heater_limit[
                                2] > 0:
                                x_heating_3 = _calc_heatflow(A, rhs,
                                                             t_air_set=t_set_heating,
                                                             q_air_fix=
                                                             heater_limit[0],
                                                             q_iw_fix=
                                                             heater_limit[1],
                                                             q_ow_fix=None)

                                if x_heating_3[8] > heater_limit[2]:
                                    return _calc_temperatue(A, rhs, q_air_fix=
                                    heater_limit[0], q_iw_fix=heater_limit[1],
                                                            q_ow_fix=
                                                            heater_limit[2])
                                else:
                                    return x_heating_3
                            else:
                                return x_maxheat_2
                        else:
                            return x_heating_2
                    elif np.argmax(heater_order == 2) == 2 and heater_limit[
                        2] > 0:
                        x_heating_2 = _calc_heatflow(A, rhs,
                                                     t_air_set=t_set_heating,
                                                     q_air_fix=heater_limit[0],
                                                     q_iw_fix=0, q_ow_fix=None)

                        if x_heating_2[8] > heater_limit[2]:
                            x_maxheat_2 = _calc_temperatue(A, rhs, q_air_fix=
                            heater_limit[0], q_iw_fix=0, q_ow_fix=heater_limit[
                                2])

                            if x_maxheat_2[4] < t_set_heating and heater_limit[
                                1] > 0:
                                x_heating_3 = _calc_heatflow(A, rhs,
                                                             t_air_set=t_set_heating,
                                                             q_air_fix=
                                                             heater_limit[0],
                                                             q_iw_fix=None,
                                                             q_ow_fix=
                                                             heater_limit[2])

                                if x_heating_3[7] > heater_limit[1]:
                                    return _calc_temperatue(A, rhs, q_air_fix=
                                    heater_limit[0], q_iw_fix=heater_limit[1],
                                                            q_ow_fix=
                                                            heater_limit[2])
                                else:
                                    return x_heating_3
                            else:
                                return x_maxheat_2
                        else:
                            return x_heating_2
                    else:
                        return x_maxheat_1
            else:
                return x_heating_1

        elif np.argmax(heater_order == 1) == 1 and heater_limit[1] > 0:
            x_heating_1 = _calc_heatflow(A, rhs, t_air_set=t_set_heating,
                                         q_air_fix=0, q_iw_fix=None,
                                         q_ow_fix=0)
            if x_heating_1[7] > heater_limit[1]:
                x_maxheat_1 = _calc_temperatue(A, rhs, q_air_fix=0,
                                               q_iw_fix=heater_limit[1],
                                               q_ow_fix=0)

                if x_maxheat_1[4] < t_set_heating:
                    if np.argmax(heater_order == 2) == 0 and heater_limit[
                        0] > 0:
                        x_heating_2 = _calc_heatflow(A, rhs,
                                                     t_air_set=t_set_heating,
                                                     q_air_fix=None,
                                                     q_iw_fix=heater_limit[1],
                                                     q_ow_fix=0)

                        if x_heating_2[6] > heater_limit[0]:
                            x_maxheat_2 = _calc_temperatue(A, rhs, q_air_fix=
                            heater_limit[0], q_iw_fix=heater_limit[1],
                                                           q_ow_fix=0)

                            if x_maxheat_2[4] < t_set_heating and heater_limit[
                                2] > 0:
                                x_heating_3 = _calc_heatflow(A, rhs,
                                                             t_air_set=t_set_heating,
                                                             q_air_fix=
                                                             heater_limit[0],
                                                             q_iw_fix=
                                                             heater_limit[1],
                                                             q_ow_fix=None)

                                if x_heating_3[8] > heater_limit[2]:
                                    return _calc_temperatue(A, rhs, q_air_fix=
                                    heater_limit[0], q_iw_fix=heater_limit[1],
                                                            q_ow_fix=
                                                            heater_limit[2])
                                else:
                                    return x_heating_3
                            else:
                                return x_maxheat_2
                        else:
                            return x_heating_2
                    elif np.argmax(heater_order == 2) == 2 and heater_limit[
                        2] > 0:
                        x_heating_2 = _calc_heatflow(A, rhs,
                                                     t_air_set=t_set_heating,
                                                     q_air_fix=0,
                                                     q_iw_fix=heater_limit[1],
                                                     q_ow_fix=None)

                        if x_heating_2[8] > heater_limit[2]:
                            x_maxheat_2 = _calc_temperatue(A, rhs, q_air_fix=0,
                                                           q_iw_fix=
                                                           heater_limit[1],
                                                           q_ow_fix=
                                                           heater_limit[2])

                            if x_maxheat_2[4] < t_set_heating and heater_limit[
                                0] > 0:
                                x_heating_3 = _calc_heatflow(A, rhs,
                                                             t_air_set=t_set_heating,
                                                             q_air_fix=None,
                                                             q_iw_fix=
                                                             heater_limit[1],
                                                             q_ow_fix=
                                                             heater_limit[2])

                                if x_heating_3[6] > heater_limit[0]:
                                    return _calc_temperatue(A, rhs, q_air_fix=
                                    heater_limit[0], q_iw_fix=heater_limit[1],
                                                            q_ow_fix=
                                                            heater_limit[2])
                                else:
                                    return x_heating_3
                            else:
                                return x_maxheat_2
                        else:
                            return x_heating_2
                    else:
                        return x_maxheat_1
            else:
                return x_heating_1
        elif np.argmax(heater_order == 1) == 2 and heater_limit[
            2] > 0:  # no else
            x_heating_1 = _calc_heatflow(A, rhs, t_air_set=t_set_heating,
                                         q_air_fix=0, q_iw_fix=0,
                                         q_ow_fix=None)
            if x_heating_1[8] > heater_limit[2]:
                x_maxheat_1 = _calc_temperatue(A, rhs, q_air_fix=0, q_iw_fix=0,
                                               q_ow_fix=heater_limit[2])

                if x_maxheat_1[4] < t_set_heating:
                    if np.argmax(heater_order == 2) == 0 and heater_limit[
                        0] > 0:
                        x_heating_2 = _calc_heatflow(A, rhs,
                                                     t_air_set=t_set_heating,
                                                     q_air_fix=None,
                                                     q_iw_fix=0,
                                                     q_ow_fix=heater_limit[2])

                        if x_heating_2[6] > heater_limit[0]:
                            x_maxheat_2 = _calc_temperatue(A, rhs, q_air_fix=
                            heater_limit[0], q_iw_fix=0, q_ow_fix=heater_limit[
                                1])

                            if x_maxheat_2[4] < t_set_heating and heater_limit[
                                1] > 0:
                                x_heating_3 = _calc_heatflow(A, rhs,
                                                             t_air_set=t_set_heating,
                                                             q_air_fix=
                                                             heater_limit[0],
                                                             q_iw_fix=None,
                                                             q_ow_fix=
                                                             heater_limit[2])

                                if x_heating_3[7] > heater_limit[1]:
                                    return _calc_temperatue(A, rhs, q_air_fix=
                                    heater_limit[0], q_iw_fix=heater_limit[1],
                                                            q_ow_fix=
                                                            heater_limit[2])
                                else:
                                    return x_heating_3
                            else:
                                return x_maxheat_2
                        else:
                            return x_heating_2
                    elif np.argmax(heater_order == 2) == 1 and heater_limit[
                        1] > 0:
                        x_heating_2 = _calc_heatflow(A, rhs,
                                                     t_air_set=t_set_heating,
                                                     q_air_fix=0,
                                                     q_iw_fix=None,
                                                     q_ow_fix=heater_limit[2])

                        if x_heating_2[7] > heater_limit[1]:
                            x_maxheat_2 = _calc_temperatue(A, rhs, q_air_fix=0,
                                                           q_iw_fix=
                                                           heater_limit[1],
                                                           q_ow_fix=
                                                           heater_limit[2])

                            if x_maxheat_2[4] < t_set_heating and heater_limit[
                                0] > 0:
                                x_heating_3 = _calc_heatflow(A, rhs,
                                                             t_air_set=t_set_heating,
                                                             q_air_fix=None,
                                                             q_iw_fix=
                                                             heater_limit[1],
                                                             q_ow_fix=
                                                             heater_limit[2])

                                if x_heating_3[6] > heater_limit[0]:
                                    return _calc_temperatue(A, rhs, q_air_fix=
                                    heater_limit[0], q_iw_fix=heater_limit[1],
                                                            q_ow_fix=
                                                            heater_limit[2])
                                else:
                                    return x_heating_3
                            else:
                                return x_maxheat_2
                        else:
                            return x_heating_2
                    else:
                        return x_maxheat_1
            else:
                return x_heating_1

    elif x_noHeat[4] > t_set_cooling:
        # Indoor air temperature above cooling set temperature

        if np.argmax(cooler_order == 1) == 0 and cooler_limit[0] < 0:
            x_cooling_1 = _calc_heatflow(A, rhs, t_air_set=t_set_cooling,
                                         q_air_fix=None, q_iw_fix=0,
                                         q_ow_fix=0)
            if x_cooling_1[6] < cooler_limit[0]:
                x_maxcool_1 = _calc_temperatue(A, rhs,
                                               q_air_fix=cooler_limit[0],
                                               q_iw_fix=0, q_ow_fix=0)

                if x_maxcool_1[4] > t_set_cooling:
                    if np.argmax(cooler_order == 2) == 1 and cooler_limit[
                        1] < 0:
                        x_cooling_2 = _calc_heatflow(A, rhs,
                                                     t_air_set=t_set_cooling,
                                                     q_air_fix=cooler_limit[0],
                                                     q_iw_fix=None, q_ow_fix=0)

                        if x_cooling_2[7] < cooler_limit[1]:
                            x_maxcool_2 = _calc_temperatue(A, rhs, q_air_fix=
                            cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                           q_ow_fix=0)

                            if x_maxcool_2[4] > t_set_cooling and cooler_limit[
                                2] < 0:
                                x_cooling_3 = _calc_heatflow(A, rhs,
                                                             t_air_set=t_set_cooling,
                                                             q_air_fix=
                                                             cooler_limit[0],
                                                             q_iw_fix=
                                                             cooler_limit[1],
                                                             q_ow_fix=None)

                                if x_cooling_3[8] < cooler_limit[2]:
                                    return _calc_temperatue(A, rhs, q_air_fix=
                                    cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                            q_ow_fix=
                                                            cooler_limit[2])
                                else:
                                    return x_cooling_3
                            else:
                                return x_maxcool_2
                        else:
                            return x_cooling_2
                    elif np.argmax(cooler_order == 2) == 2 and cooler_limit[
                        2] < 0:
                        x_cooling_2 = _calc_heatflow(A, rhs,
                                                     t_air_set=t_set_cooling,
                                                     q_air_fix=cooler_limit[0],
                                                     q_iw_fix=0, q_ow_fix=None)

                        if x_cooling_2[8] < cooler_limit[2]:
                            x_maxcool_2 = _calc_temperatue(A, rhs, q_air_fix=
                            cooler_limit[0], q_iw_fix=0, q_ow_fix=cooler_limit[
                                2])

                            if x_maxcool_2[4] > t_set_cooling and cooler_limit[
                                1] < 0:
                                x_cooling_3 = _calc_heatflow(A, rhs,
                                                             t_air_set=t_set_cooling,
                                                             q_air_fix=
                                                             cooler_limit[0],
                                                             q_iw_fix=None,
                                                             q_ow_fix=
                                                             cooler_limit[2])

                                if x_cooling_3[7] < cooler_limit[1]:
                                    return _calc_temperatue(A, rhs, q_air_fix=
                                    cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                            q_ow_fix=
                                                            cooler_limit[2])
                                else:
                                    return x_cooling_3
                            else:
                                return x_maxcool_2
                        else:
                            return x_cooling_2
                    else:
                        return x_maxcool_1
            else:
                return x_cooling_1
        elif np.argmax(cooler_order == 1) == 1 and cooler_limit[1] < 0:
            x_cooling_1 = _calc_heatflow(A, rhs, t_air_set=t_set_cooling,
                                         q_air_fix=0, q_iw_fix=None,
                                         q_ow_fix=0)
            if x_cooling_1[7] < cooler_limit[1]:
                x_maxcool_1 = _calc_temperatue(A, rhs, q_air_fix=0,
                                               q_iw_fix=cooler_limit[1],
                                               q_ow_fix=0)

                if x_maxcool_1[4] > t_set_cooling:
                    if np.argmax(cooler_order == 2) == 0 and cooler_limit[
                        0] < 0:
                        x_cooling_2 = _calc_heatflow(A, rhs,
                                                     t_air_set=t_set_cooling,
                                                     q_air_fix=None,
                                                     q_iw_fix=cooler_limit[1],
                                                     q_ow_fix=0)

                        if x_cooling_2[6] < cooler_limit[0]:
                            x_maxcool_2 = _calc_temperatue(A, rhs, q_air_fix=
                            cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                           q_ow_fix=0)

                            if x_maxcool_2[4] > t_set_cooling and cooler_limit[
                                2] < 0:
                                x_cooling_3 = _calc_heatflow(A, rhs,
                                                             t_air_set=t_set_cooling,
                                                             q_air_fix=
                                                             cooler_limit[0],
                                                             q_iw_fix=
                                                             cooler_limit[1],
                                                             q_ow_fix=None)

                                if x_cooling_3[8] < cooler_limit[2]:
                                    return _calc_temperatue(A, rhs, q_air_fix=
                                    cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                            q_ow_fix=
                                                            cooler_limit[2])
                                else:
                                    return x_cooling_3
                            else:
                                return x_maxcool_2
                        else:
                            return x_cooling_2
                    elif np.argmax(cooler_order == 2) == 2 and cooler_limit[
                        2] < 0:
                        x_cooling_2 = _calc_heatflow(A, rhs,
                                                     t_air_set=t_set_cooling,
                                                     q_air_fix=0,
                                                     q_iw_fix=cooler_limit[1],
                                                     q_ow_fix=None)

                        if x_cooling_2[8] < cooler_limit[2]:
                            x_maxcool_2 = _calc_temperatue(A, rhs, q_air_fix=0,
                                                           q_iw_fix=
                                                           cooler_limit[1],
                                                           q_ow_fix=
                                                           cooler_limit[2])

                            if x_maxcool_2[4] > t_set_cooling and cooler_limit[
                                0] < 0:
                                x_cooling_3 = _calc_heatflow(A, rhs,
                                                             t_air_set=t_set_cooling,
                                                             q_air_fix=None,
                                                             q_iw_fix=
                                                             cooler_limit[1],
                                                             q_ow_fix=
                                                             cooler_limit[2])

                                if x_cooling_3[6] < cooler_limit[0]:
                                    return _calc_temperatue(A, rhs, q_air_fix=
                                    cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                            q_ow_fix=
                                                            cooler_limit[2])
                                else:
                                    return x_cooling_3
                            else:
                                return x_maxcool_2
                        else:
                            return x_cooling_2
                    else:
                        return x_maxcool_1
            else:
                return x_cooling_1

        elif np.argmax(cooler_order == 1) == 2 and cooler_limit[2] < 0:
            x_cooling_1 = _calc_heatflow(A, rhs, t_air_set=t_set_cooling,
                                         q_air_fix=0, q_iw_fix=0,
                                         q_ow_fix=None)
            if x_cooling_1[8] < cooler_limit[2]:
                x_maxcool_1 = _calc_temperatue(A, rhs, q_air_fix=0, q_iw_fix=0,
                                               q_ow_fix=cooler_limit[2])

                if x_maxcool_1[4] > t_set_cooling:
                    if np.argmax(cooler_order == 2) == 0 and cooler_limit[
                        0] < 0:
                        x_cooling_2 = _calc_heatflow(A, rhs,
                                                     t_air_set=t_set_cooling,
                                                     q_air_fix=None,
                                                     q_iw_fix=0,
                                                     q_ow_fix=cooler_limit[2])

                        if x_cooling_2[6] < cooler_limit[0]:
                            x_maxcool_2 = _calc_temperatue(A, rhs, q_air_fix=
                            cooler_limit[0], q_iw_fix=0, q_ow_fix=cooler_limit[
                                2])

                            if x_maxcool_2[4] > t_set_cooling and cooler_limit[
                                1] < 0:
                                x_cooling_3 = _calc_heatflow(A, rhs,
                                                             t_air_set=t_set_cooling,
                                                             q_air_fix=
                                                             cooler_limit[0],
                                                             q_iw_fix=None,
                                                             q_ow_fix=
                                                             cooler_limit[2])

                                if x_cooling_3[7] < cooler_limit[1]:
                                    return _calc_temperatue(A, rhs, q_air_fix=
                                    cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                            q_ow_fix=
                                                            cooler_limit[2])
                                else:
                                    return x_cooling_3
                            else:
                                return x_maxcool_2
                        else:
                            return x_cooling_2
                    elif np.argmax(cooler_order == 2) == 1 and cooler_limit[
                        1] < 0:
                        x_cooling_2 = _calc_heatflow(A, rhs,
                                                     t_air_set=t_set_cooling,
                                                     q_air_fix=0,
                                                     q_iw_fix=None,
                                                     q_ow_fix=cooler_limit[2])

                        if x_cooling_2[7] < cooler_limit[1]:
                            x_maxcool_2 = _calc_temperatue(A, rhs, q_air_fix=0,
                                                           q_iw_fix=
                                                           cooler_limit[1],
                                                           q_ow_fix=
                                                           cooler_limit[2])

                            if x_maxcool_2[4] > t_set_cooling and cooler_limit[
                                0] < 0:
                                x_cooling_3 = _calc_heatflow(A, rhs,
                                                             t_air_set=t_set_cooling,
                                                             q_air_fix=None,
                                                             q_iw_fix=
                                                             cooler_limit[1],
                                                             q_ow_fix=
                                                             cooler_limit[2])

                                if x_cooling_3[6] < cooler_limit[0]:
                                    return _calc_temperatue(A, rhs, q_air_fix=
                                    cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                            q_ow_fix=
                                                            cooler_limit[2])
                                else:
                                    return x_cooling_3
                            else:
                                return x_maxcool_2
                        else:
                            return x_cooling_2
                    else:
                        return x_maxcool_1
            else:
                return x_cooling_1

    else:
        # Indoor air temperature between both set temperature -> no further 
        # action required
        return x_noHeat


def _calc_temperatue(A, rhs, q_air_fix=0, q_iw_fix=0, q_ow_fix=0):
    """
    Run the model with a fixed convective heating/cooling gain
    
    Parameters
    ----------
    A : 2d array of floats
        Coefficients describing the VDI model
    rhs : Array of floats
        Right hand side of these equations
    q_hc_fix : Float
        Heating/cooling input into the zone in Watt
    """

    # Delete all entries in the final three lines of A:
    A[6, :] = 0
    A[7, :] = 0
    A[8, :] = 0

    # Add Q_HC = q_hc_fix
    A[6, 6] = 1
    A[7, 7] = 1
    A[8, 8] = 1
    rhs[6] = q_air_fix
    rhs[7] = q_iw_fix
    rhs[8] = q_ow_fix

    # Solve updated model
    result = np.linalg.solve(A, rhs)

    # Return results
    return result


def _calc_heatflow(A, rhs, t_air_set=293.15, q_air_fix=None, q_iw_fix=None,
                   q_ow_fix=None):
    """
    Run the model with a fixed convective heating/cooling gain
    
    Parameters
    ----------
    A : 2d array of floats
        Coefficients describing the VDI model
    rhs : Array of floats
        Right hand side of these equations
    t_air_set : Float
        Zone's set temperature in Kelvin
    """

    # Delete all entries in the final three lines of A:
    A[6, :] = 0
    A[7, :] = 0
    A[8, :] = 0

    # Add T_air = t_air_set
    A[6, 4] = 1
    rhs[6] = t_air_set

    if q_air_fix == None:
        A[7, 7] = 1
        A[8, 8] = 1
        rhs[7] = q_iw_fix
        rhs[8] = q_ow_fix
    elif q_iw_fix == None:
        A[7, 6] = 1
        A[8, 8] = 1
        rhs[7] = q_air_fix
        rhs[8] = q_ow_fix
    elif q_ow_fix == None:
        A[7, 6] = 1
        A[8, 7] = 1
        rhs[7] = q_air_fix
        rhs[8] = q_iw_fix

    # Solve updated model
    result = np.linalg.solve(A, rhs)

    # Return results
    return result
