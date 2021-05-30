import teaser.logic.utilities as utilities
import os
import warnings

import pandas as pd
import datetime
import json
import collections
import multiprocessing
import pickle

# helper scripts
import simulate as sim
import read_results as res

def generate_archetype():
    from teaser.project import Project

    prj = Project(load_data=True)
    prj.name = "Simulationsstudie"

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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

    # ----------------------------------------------

    # Project 2 includes all buildings of the building type 'multi family house'

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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

    # ----------------------------------------------

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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
        zone.heating_cooling_system.panel_heating_cooling(specific_power_heat=70.0, specific_power_cool=40.0)
        zone.use_conditions.heating_profile = [294.15]
        zone.use_conditions.cooling_profile = [298.15]

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

    return prj

def test_export_aixlib():
    prj = generate_archetype()

    prj.dir_reference_results = utilities.get_full_path(
        os.path.join(
            "examples",
            "../examplefiles",
            "ReferenceResults",
            "Dymola"))

    print(prj.dir_reference_results)

    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 2
    prj.weather_file_path = utilities.get_full_path(
        os.path.join(
            "data",
            "input",
            "inputdata",
            "weatherdata",
            "TRY2015_507755060854_Jahr_City_Aachen.mos"))

    prj.calc_all_buildings()

    path = prj.export_aixlib(
        internal_id=None,
        path=None)

    return path

if __name__ == '__main__':

    workspace = os.path.join("D:\\", "tbl-cwe", "Simulationsstudie_06_21")
    print("Your workspace is set to: ")
    print(workspace)
    sim_results_path = os.path.join(workspace, "sim_results")
    TEASER_output_path = os.path.join(workspace, "TEASEROutput")

    #DIR_SCRIPT = os.path.abspath(os.path.dirname(__file__))
    #DIR_TOP = os.path.abspath(DIR_SCRIPT)
    #random_name = random_choice()
    #index = pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H")
    #prj = Project(load_data=True)
    #prj.name = "Shamrock_Park_{}_{}".format("fbkk", "ref")
    #prj.name = "Shamrock_Park_{}_{}".format(random_name, "ref")
    #info_path = os.path.join(DIR_TOP, "shamrock_park")

    print("Generating archetypes...")
    prj = generate_archetype()
    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 2
    prj.calc_all_buildings()
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
    print("Your simulation results can be found in: ")
    print(sim_results_path)
    print("That's it! :)")

    """for bldg in prj.buildings:
        signals = [
            "multizone.PHeater[{}]".format(i + 1)
            for i in range(len(bldg.thermal_zones))
        ]
        signals += [
            "multizone.PCooler[{}]".format(i + 1)
            for i in range(len(bldg.thermal_zones))
        ]
        res.read_results(
            prj=prj,
            signals=signals,
            buildings=[bldg],
            index=index,
            results_path=os.path.join(RESULTS_PATH, prj.name),
            csv_path=os.path.join(RESULTS_PATH, prj.name, "demand_csv"),
        )
        """



