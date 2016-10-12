#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example script for VDI 6007 simulation usage
"""

import numpy as np

import teaser.logic.simulation.VDI_6007.low_order_VDI as low_order_VDI
"""
        self.internal_id = random.random()

        self.parent = parent
        self.name = name
        self.building_id = None
        self.street_name = ""
        self.city = ""

        self.type_of_building = type(self).__name__

        self.year_of_construction = year_of_construction
        self._central_ahu = None
        self.with_ahu = with_ahu

        if with_ahu is True:
            self.central_ahu = BuildingAHU(self)

        self.number_of_floors = None
        self.height_of_floors = None
        self.net_leased_area = net_leased_area
        self.bldg_height = None

        self._year_of_retrofit = None

        self._thermal_zones = []
        self._outer_area = {}
        self._window_area = {}

        self.gml_surfaces = []

        self.volume = 0
        self.sum_heating_load = 0
        self.sum_cooling_load = 0

        #additional simulation parameters
        self.longitude = None
        self.latitude = None

        self.file_ahu = None
        self.file_internal_gains = None
        self.file_set_t = None
        self.file_weather = None

        self.orientation_bldg = []
        self.tilt_bldg = []
        self.orient_tilt = []
        self._number_of_elements_calc = 2
        self._merge_windows_calc = False
        self._used_library_calc = "AixLib"
"""


def vdi_example_6007(thermal_zone):
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
    if len(thermal_zone.inner_walls)!= 0:
        withInnerwalls="true"
    else:
        withInnerwalls="false"


    houseData = {"R1i": thermal_zone.r1_iw,
                 "C1i": thermal_zone.c1_iw,
                 "Ai": thermal_zone.area_iw,
                 "RRest": thermal_zone.r_rest_ow,
                 "R1o": thermal_zone.r1_ow,
                 "C1o": thermal_zone.c1_ow,
                 "Ao": thermal_zone.area_ow,
                 "Aw": thermal_zone.window_area_list,
                 #"At": thermal_zone., #TODO
                 "Vair": thermal_zone.volume,
                 "rhoair": thermal_zone.density_air,
                 "cair": thermal_zone.heat_capac_air,
                 "splitfac": thermal_zone.windows[0].a_conv,
                 "g": thermal_zone.weighted_g_value,
                 "alphaiwi": thermal_zone.alpha_comb_iw,
                 "alphaowi": thermal_zone.alpha_comb_inner_ow,
                 #"alphaWall": thermal_zone.,  # 25 * sum(Ao)#TODO
                 "withInnerwalls": withInnerwalls} #TODO is this correct?

    print(houseData)

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

    from teaser.project import Project
    prj = Project(load_data=True)
    prj.name = "ArchetypeBuildings"
    prj.type_bldg_residential(name="ResidentialBuilding",
                              year_of_construction=1988,
                              number_of_floors=2,
                              height_of_floors=3.5,
                              net_leased_area=100,
                              with_ahu=True,
                              residential_layout=1,
                              neighbour_buildings=1,
                              attic=1,
                              cellar=1,
                              construction_type="heavy",
                              dormer=1)

    prj.type_bldg_office(name="Office1",
                         year_of_construction=1988,
                         number_of_floors=2,
                         height_of_floors=3.5,
                         net_leased_area=100,
                         office_layout=1,
                         window_layout=1,
                         with_ahu=True,
                         construction_type="heavy")




    for i in range(len(prj.buildings)-1):
        for j in range(len(prj.buildings[i].thermal_zones)-1):
            thermal_zone=prj.buildings[i].thermal_zones[j]
            vdi_example_6007(thermal_zone)

    vdi_example_6007(prj.buildings[0].thermal_zones[0])

