#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example script for VDI 6007 simulation usage

This example is currently not working
"""

import numpy as np

from teaser.project import Project
from teaser.logic.simulation.vdi_core import VDICore

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
        year_of_construction=2015,
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


def vdi_example_6007(thermal_zone):
    """
    Example function to perform VDI 6007 calculation with thermal_zone

    Parameters
    ----------
    thermal_zone : object
        TEASER thermal zone object

    Returns
    -------
    res_tuple : tuple (of np.arrays)
        Result tuple.
        First entry:
        t_indoor : np.array
            Indoor air temperature in degree Celsius per timestep
        Second entry:
        q_heat_cool : np.array
            Array with heating/cooling values in Watt (positiv: heating;
            negative: cooling)
    """

    #  Generate vdi calculation core instance
    vdi_calc = VDICore(thermal_zone=thermal_zone)

    (t_indoor, q_heat_cool) = vdi_calc.simulate()

    return (t_indoor, q_heat_cool)


if __name__ == '__main__':

    import teaser.data.weatherdata as weatherdata

    #  Get TEASER project with residential type building
    prj = gen_res_type_example_building()

    #  Pointer to building object
    building = prj.buildings[0]

    #  Extract thermal_zone
    thermal_zone = prj.buildings[0].thermal_zones[0]

    weather = weatherdata.WeatherData()
    prj.weather_data = weather

    print('UA value before retrofiting:')
    print(prj.buildings[0].thermal_zones[0].outer_walls[0].ua_value)
    print('Inner resistance (VDI 6007) of thermal zone before retrofit:')
    print(thermal_zone.model_attr.r1_ow)
    print()

    #  Perform simulation for unretrofited model
    (t_indoor, q_heat_cool_1) = vdi_example_6007(thermal_zone)

    q_heat1 = np.zeros(len(q_heat_cool_1))
    q_cool1 = np.zeros(len(q_heat_cool_1))
    for i in range(len(q_heat_cool_1)):
        if q_heat_cool_1[i] > 0:
            q_heat1[i] = q_heat_cool_1[i]
        elif q_heat_cool_1[i] < 0:
            q_cool1[i] = q_heat_cool_1[i]

    print('Sum of heating energy in kWh:')
    print(sum(q_heat1) / 1000)

    print('Sum of cooling energy in kWh:')
    print(-sum(q_cool1) / 1000)

    import matplotlib.pyplot as plt

    fig = plt.figure()
    fig.add_subplot(411)
    plt.plot(weather.air_temp)
    plt.ylabel('Outdoor air\ntemperature in\ndegree Celsius')
    fig.add_subplot(412)
    plt.plot(weather.direct_radiation)
    plt.ylabel('Direct radiation in W/m2')
    fig.add_subplot(413)
    plt.plot(t_indoor - 273.15)
    plt.ylabel('Indoor air\ntemperature in\ndegree Celsius')
    fig.add_subplot(414)
    plt.plot(q_heat_cool_1 / 1000)

    plt.ylabel('Heating/cooling\npower (+/-)\nin kW')
    plt.xlabel('Time in hours')
    plt.show()
