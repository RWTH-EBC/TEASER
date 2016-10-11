#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from __future__ import division

import numpy as np


def equal_air_temp(HSol, TBlaSky, TDryBul, sunblind, params):
    """
    Inputs:
    HSol - solar radiation per unit area
    TBlaSky - black-body sky temperature
    TDryBul - dry bulb temperature
    sunblind - opening factor of sunblinds for each direction (0 = open to 1 = closed)
    params - misc. constant input parameters
    ----------------------------------------
    Outputs:
    TEqAir - equivalent air temperature
    
    """
    # Read parameters to improve readability in the equations
    eExt = params[
        "eExt"]  # coefficient of emission of exterior walls (outdoor)
    aExt = params[
        "aExt"]  # coefficient of absorption of exterior walls (outdoor)
    alphaRadWall = params["alpha_rad_wall"]
    alphaWallOut = params["alpha_wall_out"]
    wfWall = params["wfWall"]  # weight factors of the walls
    wfWin = params["wfWin"]  # weight factors of the windows
    wfGro = params[
        "wfGro"]  # weight factor of the ground (0 if not considered)
    TGro = params["T_Gro"]  #
    n = len(wfWall)

    # Compute equivalent long wave and short wave temperatures
    delTEqLW = (TBlaSky - TDryBul) * (
    eExt * alphaRadWall / (alphaRadWall + alphaWallOut * 0.93))
    delTEqSW = HSol * aExt / (alphaRadWall + alphaWallOut)

    # Compute equivalent window and wall temperatures
    if params["withLongwave"]:
        TEqWin = np.array(
            [TDryBul + delTEqLW * (1 - sunblind[:, i]) for i in range(n)]).T
        TEqWall = np.array(
            [TDryBul + delTEqLW[:, i] + delTEqSW[:, i] for i in range(n)]).T
    else:
        TEqWin = np.array([TDryBul for i in range(n)]).T
        TEqWall = np.array([TDryBul + delTEqSW[:, i] for i in range(n)]).T

    # Compute equivalent air temperature
    TEqAir = np.dot(TEqWall, wfWall) + np.dot(TEqWin, wfWin) + TGro * wfGro

    # Return result
    return TEqAir


if __name__ == "__main__":
    times_per_hour = 60
    no_tile = 60

    t_outside_raw = np.loadtxt("inputs/case08_t_amb.csv", delimiter=",")
    t_outside = np.array([t_outside_raw[2 * i, 1] for i in range(24)])
    t_outside_adj = np.repeat(t_outside, times_per_hour)
    t_outside_tiled = np.tile(t_outside_adj, no_tile)

    q_sol_rad_win_raw = np.loadtxt("inputs/case08_q_sol_win.csv",
                                   usecols=(1, 2))
    solarRad_win = q_sol_rad_win_raw[0:24, :]

    sunblind_in = np.zeros_like(solarRad_win)
    sunblind_in[solarRad_win > 100] = 0.85
    sunblind_in_adj = np.repeat(sunblind_in, times_per_hour, axis=0)

    q_sol_rad_wall_raw = np.loadtxt("inputs/case08_q_sol_wall.csv",
                                    usecols=(1, 2))
    solarRad_wall = q_sol_rad_wall_raw[0:24, :]
    solarRad_wall_adj = np.repeat(solarRad_wall, times_per_hour, axis=0)
    solarRad_wall_tiled = np.tile(solarRad_wall_adj.T, no_tile).T

    t_black_sky = np.zeros_like(t_outside) + 273.15

    params = {"aExt": 0.7,
              "eExt": 0.9,
              "wfWall": [0.05796831135677373, 0.13249899738691134],
              "wfWin": [0.4047663456281575, 0.4047663456281575],
              "wfGro": 0,
              "T_Gro": 273.15 + 12,
              "alpha_wall_out": 20,
              "alpha_rad_wall": 5,
              "withLongwave": False}

    t_equal_air = equal_air_temp(solarRad_wall, t_black_sky, t_outside,
                                 sunblind_in, params)
