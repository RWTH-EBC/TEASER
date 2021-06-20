import multiprocessing
import os
import pickle
import pandas as pd
import datetime
from dymola.dymola_interface import DymolaInterface


# helper scripts
import simulate as sim
import teaser.logic.utilities as utilities

"""
Use this script to generate and simulate multiple buildings at once.
1. Define buildings in generate_archetype() similar to teaser/examples/e1_generate_archetype.py
2. Choose a heating/cooling system setup from teaser/logic/buildingobjects/buildingsystems/heatingcooling.py
3. Set your workspace and weather file in the main routine

"""

def generate_archetype():
    from teaser.project import Project

    prj = Project(load_data=True)
    prj.name = "Referenz"

    heating_profile_night_reduction = [292.15,
                                       292.15,
                                       292.15,
                                       292.15,
                                       292.15,
                                       292.15,
                                       292.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       294.15,
                                       292.15]
    cooling_profile_night_reduction = [301.15,
                                       301.15,
                                       301.15,
                                       301.15,
                                       301.15,
                                       298.15,
                                       298.15,
                                       298.15,
                                       298.15,
                                       298.15,
                                       298.15,
                                       298.15,
                                       298.15,
                                       298.15,
                                       298.15,
                                       298.15,
                                       298.15,
                                       298.15,
                                       301.15,
                                       301.15,
                                       301.15,
                                       301.15,
                                       301.15,
                                       301.15]

    # Project 1 includes all buildings of the building type 'single family house'

    # -----EFH radiator-----
    """
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHradiator1990heavy100",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    """
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHradiator1990heavy200",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    """
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHradiator1990light100",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    """
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHradiator1990light200",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    """
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHradiator2010heavy100",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHradiator2010heavy200",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHradiator2010light100",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHradiator2010light200",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    
    # ------EFH panel-----

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanel1990heavy100",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanel1990heavy200",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanel1990light100",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanel1990light200",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanel2010heavy100",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanel2010heavy200",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanel2010light100",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHpanel2010light200",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    
    # -----EFH tabs plus air-----
    
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair1990heavy100",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair1990heavy200",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair1990light100",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair1990light200",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair2010heavy100",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair2010heavy200",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair2010light100",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHtabsplusair2010light200",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=200.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    # -----convective-----

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvective1990heavy100",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvective1990light100",
        year_of_construction=1990,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvective2010heavy100",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="EFHconvective2010light100",
        year_of_construction=2010,
        number_of_floors=2,
        height_of_floors=2.8,
        net_leased_area=100.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    # ----------------------------------------------
    
    # Project 2 includes all buildings of the building type 'multi family house'
    """
    # -----MFH radiator-----

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHradiator1990heavy1000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    """
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHradiator1990heavy2000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=2000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    """
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHradiator1990light1000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    """
    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHradiator1990light2000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=2000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHradiator2010heavy1000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHradiator2010heavy2000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=2000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHradiator2010light1000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHradiator2010light2000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=2000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    
    # ------MFH panel-----

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHpanel1990heavy1000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHpanel1990heavy2000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=2000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHpanel1990light1000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHpanel1990light2000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=2000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHpanel2010heavy1000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHpanel2010heavy2000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=2000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHpanel2010light1000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHpanel2010light2000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=2000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    # -----MFH tabs plus air-----

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHtabsplusair1990heavy1000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHtabsplusair1990heavy2000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=2000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHtabsplusair1990light1000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHtabsplusair1990light2000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=2000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHtabsplusair2010heavy1000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHtabsplusair2010heavy2000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=2000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHtabsplusair2010light1000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHtabsplusair2010light2000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=2000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    # -----MFH convective-----

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHconvective1990heavy1000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHconvective1990light1000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHconvective2010heavy1000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="MFHconvective2010light1000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=2.8,
        net_leased_area=1000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    # ----------------------------------------------
    """
    # Project 3 includes all buildings of the building type 'office'

    # -----Office radiator-----

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officeradiator1990heavy3000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    """
    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officeradiator1990heavy5000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=5000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    """
    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officeradiator1990light3000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    """
    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officeradiator1990light5000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=5000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officeradiator2010heavy3000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officeradiator2010heavy5000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=5000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officeradiator2010light3000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officeradiator2010light5000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=5000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.radiator_heating()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    
    # ------Office panel-----

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officepanel1990heavy3000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officepanel1990heavy5000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=5000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officepanel1990light3000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officepanel1990light5000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=5000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officepanel2010heavy3000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officepanel2010heavy5000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=5000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officepanel2010light3000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officepanel2010light5000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=5000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.test_panel_heating_cooling(specific_power_heat=100.0, specific_power_cool=40.0, KR=1, TN=17.5)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    # -----Office tabs plus air-----

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officetabsplusair1990heavy3000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officetabsplusair1990heavy5000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=5000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officetabsplusair1990light3000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officetabsplusair1990light5000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=5000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officetabsplusair2010heavy3000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officetabsplusair2010heavy5000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=5000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officetabsplusair2010light3000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officetabsplusair2010light5000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=5000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.tabs_plus_air_heating_cooling(specific_power_heat=30.0, specific_power_cool=30.0,
                                                                  room_temp_control=True)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    # -----Office convective-----

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officeconvective1990heavy3000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officeconvective1990light3000",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officeconvective2010heavy3000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="heavy")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]

    prj.add_non_residential(
        method="bmvbs",
        usage="office",
        name="Officeconvective2010light3000",
        year_of_construction=2010,
        number_of_floors=5,
        height_of_floors=3.0,
        net_leased_area=3000.0,
        construction_type="light")

    bldg = prj.buildings[-1]  # can be replaced with specific building

    for zone in bldg.thermal_zones:
        zone.heating_cooling_system.convective_heating_cooling()
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]
        zone.use_conditions.max_user_infiltration = 0.5
        zone.use_conditions.max_overheating_infiltration = [0.1, 0.1]
        zone.use_conditions.max_summer_infiltration = [0.0, 273.15 + 10, 273.15 + 17]
        zone.use_conditions.winter_reduction_infiltration = [0.2, 273.15, 273.15 + 10]
        if "ICT" in zone.name:
            zone.use_conditions.infiltration_rate = 6.0
            zone.use_conditions.max_user_infiltration = 0.0
            zone.use_conditions.winter_reduction_infiltration = [1.0, 273.15, 273.15 + 10]
    """
    return prj

def read_results(
        buildings,
        signals,
        index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
        index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
        results_path=None,
        csv_path=None,
):
    """Read simulation data from .mat file and save them into csv.

    Reads Dymola result files and saves them as time series in csv. It assumes that all
    thermal_zones are a MultiZone (TEASER Export) in Modelica.

    Parameters
    ----------
    buildings : list
        List of TEASER bldgs
    signals : list
        List of signals to be read from the results file.
    index : Pandas date_range
        Pandas date range of the simulation data. Must fit the length of
        simulation data. (Beware of leap years! every 4 years, e.g. 2020) (default: hourly for year 2019)
    index_res : Pandas date_range
        Pandas date range  if slice should be picked e. g. only january of the simulation data. Must fit the length of
        simulation data. (default: hourly for year 2015)
    results_path : str
        Path where Dymola results are  stored.
    csv_path : str
        Path where csv results should be stored.

    """

    if not os.path.exists(csv_path):
        os.makedirs(csv_path)
    dymola = DymolaInterface()

    for bldg in buildings:
        print("reading building {}".format(bldg))
        # bldg.name # bldg
        #if not (bldg + "_heat.csv") in os.listdir(csv_path):
        try:
            #print(os.path.join(results_path, bldg + ".mat"))
            dym_res = dymola.readTrajectory(
                fileName=os.path.join(results_path, bldg + ".mat"),
                signals=signals,
                rows=dymola.readTrajectorySize(
                    fileName=os.path.join(results_path, bldg + ".mat")
                ),
            )
            results = pd.DataFrame().from_records(dym_res).T
            results = results.rename(
                columns=dict(zip(results.columns.values, signals))
            )
        except BaseException:
            # Dymola has strange exceptions
            print(
                "Reading results of building {} failed, "
                "please check result file".format(bldg)
            )
            # raise Exception("Results Error!")
            continue
        try:
            results.index = index
        except ValueError:
            print(
                "Simulation results of building {} are most likely "
                "faulty (series is shorter then one year), please check "
                "result file".format(bldg)
            )
            # raise Exception("Completion Error!")
            continue

        heat = pd.DataFrame(
            data=results.filter(like="PHeat").sum(axis=1)[
                 index_res[0]: index_res[-1]
                 ],
            columns=[bldg + " PHeat"],
        )

        cool = pd.DataFrame(
            data=results.filter(like="PCool")
                     .abs()
                     .sum(axis=1)[
                 index_res[0]: index_res[-1]
                 ],
            columns=[bldg + " PCool"],
        )

        heat.to_csv(os.path.join(csv_path, bldg + "_heat.csv"))
        cool.to_csv(os.path.join(csv_path, bldg + "_cool.csv"))

    dymola.close()

if __name__ == '__main__':

    # set your workspace to your desired path here
    workspace = os.path.join("D:\\", "tbl-cwe", "Simulation", "Netzismulation", "Referenz")
    sim_results_path = os.path.join(workspace, "sim_results")
    TEASER_output_path = os.path.join(workspace, "TEASEROutput")
    """
    print("Generating archetypes...")
    prj = generate_archetype()
    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 2
    prj.calc_all_buildings()

    # set your desired weather file here
    prj.weather_file_path = utilities.get_full_path(
        os.path.join(
            "data",
            "input",
            "inputdata",
            "weatherdata",
            "TRY2015_507755060854_Jahr_City_Aachen.mos"))

    print("Exporting buildings...")
    prj.export_aixlib(path=TEASER_output_path)

    # Save project in pickle file for later use
    pickle_file = os.path.join(workspace, "building_simulation_pickle.p")
    pickle.dump(prj, open(pickle_file, "wb"))

    print("Starting simulation")
    sim.queue_simulation(
        sim_function=sim.simulate,
        prj=prj,
        model_path=TEASER_output_path,
        results_path=sim_results_path,
        number_of_workers=multiprocessing.cpu_count() - 3,
    )
    print("Your simulation results can be found in: " + sim_results_path)
    print("That's it! :)")
    """

    load_pickle = os.path.join(workspace, "building_simulation_pickle.p")
    pickle_prj = pickle.load(open(load_pickle, "rb"))

    sim_results_path = os.path.join(workspace, "sim_results", pickle_prj.name)
    print("Your Dymola Results are stored in: " + sim_results_path)

    csv_results_path = os.path.join(workspace, "csv_results")
    print("Your .csv files are stored in: " + csv_results_path)
    print("##########")
    """
    for bldg in pickle_prj.buildings:
        if "radiator" in bldg.name:
            signals = ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]

            read_results(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )
        else:
            signals = ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.PCooler[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]

            read_results(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )

    print("That's it! :)")
    """
    for bldg in pickle_prj.buildings:
        ma = pd.DataFrame()
        ma_bldg = pd.DataFrame()
        ma = pd.read_csv(os.path.join(csv_results_path, bldg.name + "_heat.csv"))

        i = 0

        for column in ma.columns[1:]:
            ma.to_csv(os.path.join(csv_results_path, column + "_ma.txt"))
            ma.index = [i * 3600 for i in range(8760)]
            ma_bldg = ma[column]

            ma_bldg = ma_bldg.drop(ma_bldg.index[0:24])
            ma_bldg.to_csv(os.path.join(csv_results_path, column + "_ma.txt"), header=False)

            with open(os.path.join(csv_results_path, column + "_ma.txt")) as f:
                lines = f.readlines()

            lines.insert(0, "#1\n")
            lines.insert(1, 'double heat(8736,2)\n')

            with open(os.path.join(csv_results_path, column + "_ma.txt"), "w") as f:
                f.writelines(lines)

            f.close()



