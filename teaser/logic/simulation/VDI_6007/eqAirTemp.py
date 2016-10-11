#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""

import math
import parser_buildings
import numpy as np
import re


def eqAirTemp(weatherData, houseData, solarRad_in, method="vdi"):
    # %% partialEqAirTemp 
    aowo = houseData["aowo"]  # Coefficient of absorption of the outer walls
    # TODO: is this the correct key word for the emission parameter?
    eowo = houseData["epso"]  # Coefficient of emission   of the outer walls
    n = len(houseData[
                "orientationswallshorizontal"])  # Number of orientations (without ground)
    T_ground = houseData[
        "temperatureground"]  # Temperature of the ground in contact with ground slab
    withLongwave = True  # If longwave radiation exchange is considered
    #    withInnerwalls  = houseData["withInnerwalls"]   # If inner walls are existent
    #    withOuterwalls  = houseData["withOuterwalls"]   # If outer walls (including windows) are existent
    #    withWindows     = houseData["withWindows"]      # If windows are existent

    wf_wall = houseData["weightfactorswall"]  # Weight factors of the walls
    wf_win = houseData["weightfactorswindow"]  # Weight factors of the windows
    wf_ground = houseData[
        "weightfactorground"]  # Weight factor of the ground (0 if not considered)

    unitvec = [1.0] * n

    T_air = weatherData[0]  # outdoor air temperature
    E_sky = weatherData[1]  # Iradiation from sky
    E_earth = weatherData[2]  # Iradiation from land surface

    I_max = houseData["Imax"]  # Intensity at which the sunblind closes
    gsunblind = houseData[
        "gsunblind"]  # Total energy transmittances if sunblind is closed

    sunblindsig = [0] * n
    for i in range(n):
        if solarRad_in[i] > I_max:
            sunblindsig[i] = 1 - gsunblind[i]
        else:
            sunblindsig[i] = 0

    T_eqLW = [0] * n
    T_eqSW = [0] * n
    T_eqWin = [0] * n
    T_eqWall = [0] * n

    if method == "vdi":
        # %% EqAirTempVDI
        alphaowo = houseData[
            "alphaowo"]  # Outer wall's coefficient of heat transfer (outer side)
        orientationswallshorizontal = houseData[
            "orientationswallshorizontal"]  # orientations of the walls against the vertical (wall,roof)    

        # scalars
        T_earth = ((-E_earth / (0.93 * 5.67)) ** 0.25) * 100  # -273.15
        T_sky = ((E_sky / (0.93 * 5.67)) ** 0.25) * 100  # -273.15    

        if abs(E_sky + E_earth) < 0.1:
            alpharad = 5.0
        else:
            alpharad = (E_sky + (E_earth / 0.93)) / (T_sky - T_earth)

        phiprivate = [0] * n
        for i in range(n):
            phiprivate[i] = (unitvec[i] + math.cos(
                orientationswallshorizontal[i] * math.pi / 180)) / 2

        for i in range(n):
            T_eqLW[i] = ((T_earth - T_air) * (unitvec[i] - phiprivate[i]) + (
                T_sky - T_air) * phiprivate[i]) * (eowo * alpharad / alphaowo)
            T_eqSW[i] = solarRad_in[i] * aowo / (alphaowo)

        for i in range(n):
            if withLongwave == True:
                T_eqWin[i] = T_air * unitvec[i] + T_eqLW[i] * abs(
                    sunblindsig[i] - unitvec[i])
                T_eqWall[i] = T_air * unitvec[i] + T_eqLW[i] + T_eqSW[i]
            else:
                T_eqWin[i] = T_air * unitvec[i]
                T_eqWall[i] = T_air * unitvec[i] + T_eqSW[i]

        # scalar products        
        temp = [T_eqWin[i] * wf_win[i] + T_eqWall[i] * wf_wall[i] for i in
                range(n)]
        equalAirTemp = sum(
            temp[i] for i in range(len(temp))) + T_ground * wf_ground

        return equalAirTemp

    elif method == "ebcMod":
        # %% EqAirTempEBCMod
        orientationswallshorizontal = houseData[
            "orientationswallshorizontal"]  # orientations of the walls against the vertical (wall,roof)
        # TODO: which parameters in the houseData??
        alphaconv_wall = houseData[
            ""]  # Outer walls coefficient of heat transfer (outerside)
        alphaconv_win = houseData[
            ""]  # Outer walls coefficient of heat transfer (outerside)
        awin = houseData["awin"]  # Coefficient of absorption of the window

        # scalars
        T_earth = ((-E_earth / (0.93 * 5.67)) ** 0.25) * 100  # -273.15
        T_sky = ((E_sky / (5.67)) ** 0.25) * 100  # -273.15        

        if abs(E_sky + E_earth) < 0.1:
            alpharad = 5.0
        else:
            alpharad = (E_sky + (E_earth / 0.93)) / (T_sky - T_earth)

        phiprivate = [0] * n
        for i in range(n):
            phiprivate[i] = (unitvec[i] + math.cos(
                orientationswallshorizontal[i] * math.pi / 180)) / 2

        T_eqLW_win = [0] * n
        T_eqSW_win = [0] * n
        for i in range(n):
            T_eqLW[i] = ((T_earth - T_air) * (unitvec[i] - phiprivate[i]) +
                         (T_sky - T_air) * phiprivate[i]) * (
                            eowo * alpharad / (alpharad + alphaconv_wall))
            T_eqLW_win[i] = ((T_earth - T_air) * (unitvec[i] - phiprivate[i]) +
                             (T_sky - T_air) * phiprivate[i]) * (
                                eowo * alpharad / (
                                    alpharad + alphaconv_win)) * abs(
                sunblindsig[i] - unitvec[i])
            T_eqSW[i] = solarRad_in[i] * aowo / (alpharad + alphaconv_wall);
            T_eqSW_win[i] = solarRad_in[i] * awin / (alpharad + alphaconv_win)

        for i in range(n):
            if withLongwave == True:
                T_eqWin[i] = T_air * unitvec[i] + T_eqLW_win[i] + T_eqSW_win[i]
                T_eqWall[i] = T_air * unitvec[i] + T_eqLW[i] + T_eqSW[i]
            else:
                T_eqWin[i] = T_air * unitvec[i] + T_eqSW_win[i]
                T_eqWall[i] = T_air * unitvec[i] + T_eqSW[i]

        # scalar products
        temp = [T_eqWall[i] * wf_wall[i] for i in range(n)]
        equalAirTemp = sum(
            temp[i] for i in range(len(temp))) + T_ground * wf_ground
        temp = [T_eqWin[i] * wf_win for i in range(n)]
        equalAirTempWindow = sum(temp[i] for i in range(len(temp)))

        return equalAirTemp, equalAirTempWindow

    elif method == "simple":
        # %% EqAirTempSimple
        alphaowo = houseData[
            "alphaowo"]  # Outer wall's coefficient of heat transfer (outer side)
        phiprivate = 0.5

        T_earth = ((-E_earth / (0.93 * 5.67)) ** 0.25) * 100  # -273.15
        T_sky = ((E_sky / (0.93 * 5.67)) ** 0.25) * 100  # -273.15

        if abs(E_sky + E_earth) < 0.1:
            alpharad = 5.0
        else:
            alpharad = (E_sky + (E_earth / 0.93)) / (T_sky - T_earth)

        # scalar
        T_eqLWs = ((T_earth - T_air) * (1 - phiprivate) + (
            T_sky - T_air) * phiprivate) * (
                  eowo * alpharad / (alphaowo * 0.93))

        for i in range(n):
            T_eqLW[i] = T_eqLWs * abs(sunblindsig[i] - unitvec[i])
            T_eqSW[i] = solarRad_in[i] * aowo / alphaowo

        for i in range(n):
            if withLongwave == True:
                T_eqWin[i] = (T_air * unitvec[i]) + T_eqLW[i]
                T_eqWall[i] = (T_air + T_eqLWs) * unitvec[i] + T_eqSW[i]
            else:
                T_eqWin[i] = T_air * unitvec[i]
                T_eqWall[i] = T_air * unitvec[i] + T_eqSW[i]

        # scalar products        
        temp = [T_eqWin[i] * wf_win[i] + T_eqWall[i] * wf_wall[i] for i in
                range(n)]
        equalAirTemp = sum(
            temp[i] for i in range(len(temp))) + T_ground * wf_ground

        return equalAirTemp
    else:
        pass


# %%
def getTRYData(houseData):
    rad_sky = []
    rad_earth = []
    temp = []
    sun_dir = []
    sun_diff = []

    # Parse all lines 
    with open("TRY2010_12_Jahr.dat") as f:
        # Read all lines at once
        all_lines = f.readlines()

        # Skip the first 38 lines
        for i in range(38, len(all_lines)):
            s = all_lines[i].split()

            rad_sky.append(float(s[16]))
            rad_earth.append(float(s[17]))
            temp.append(float(s[8]))
            sun_dir.append(float(s[13]))
            sun_diff.append(float(s[14]))

        # get location data
        if re.match("Lage", all_lines[2]) != None:
            i = all_lines[2].replace("<- B.", "").replace("<- L.", "").replace(
                " ", "").split("N")
            j = filter(None, re.split("[° \']+", i[0].replace("Lage:", "")))
            latitude = float(j[0]) + float(j[1]) / 60
            i = i[1].split("O")
            j = filter(None, re.split("[° \']+", i[0]))
            longitude = float(j[0]) + float(j[1]) / 60
            altitude = float(i[1].replace("Meter\xfcber", ""))

        location = (latitude, longitude)

        # calculate orientation depending iradiation
        import sun
        timeZone = 1
        albedo = 0.2

        beta = houseData["orientationswallshorizontal"]
        n = len(beta)
        gamma = [0, 90, 180, 270]
        if n == 4:
            pass
        elif n == 5:
            gamma.append(0)
        elif n == 6:
            # in the current Teaser data file: beta = [45,90,90,45,90,90]
            gamma = [0, 0, 90, 0, 180, 270]

        # Sun radiation on surfaces
        SunRad = sun.getSolarGains(0, 3600, 8760,
                                   timeZone=timeZone,
                                   location=location,
                                   altitude=altitude,
                                   beta=beta,
                                   gamma=gamma,
                                   beam=np.array(sun_dir),
                                   diffuse=np.array(sun_diff),
                                   albedo=albedo)

    return rad_sky, rad_earth, temp, SunRad


# %%       
if __name__ == "__main__":

    # get building inputs
    filename = "TEASER4_meine_Geo.mo"
    houseData = parser_buildings.parse_record(filename)

    # get weather inputs
    raw_inputs = {}

    (raw_inputs["solar_irrad_sky"],
     raw_inputs["solar_irrad_earth"],
     raw_inputs["temperature"], solarRad_in) = getTRYData(houseData)

    # results
    t_equiv = []

    method = "vdi"
    for i in range(len(raw_inputs["temperature"])):
        if method == "ebcMod":
            equalAirTemp, equalAirTempWindow = eqAirTemp(
                [raw_inputs["temperature"][i],
                 raw_inputs["solar_irrad_sky"][i],
                 raw_inputs["solar_irrad_earth"][i]],
                houseData,
                solarRad_in[:, i],
                method=method)
            t_equiv.append((equalAirTemp, equalAirTempWindow))
        else:
            equalAirTemp = eqAirTemp([raw_inputs["temperature"][i],
                                      raw_inputs["solar_irrad_sky"][i],
                                      raw_inputs["solar_irrad_earth"][i]],
                                     houseData,
                                     solarRad_in[:, i],
                                     method=method)
            t_equiv.append(equalAirTemp)
