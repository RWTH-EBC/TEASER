# Created January 2017
# TEASER Development Team

"""This module contains an example how to use TEASERS own simulation class
"""

import teaser.examples.e1_generate_archetype as e1
import teaser.logic.utilities as utilities
import os

def simulate_vdi():
    """"This function demonstrates the export to Modelica library AixLib using
    the API function of TEASER"""

    # In e1_generate_archetype we created a Project with three archetype
    # buildings to get this Project we rerun this example

    prj = e1.example_generate_archetype()

    prj.data.load_weather()

    from teaser.logic.simulation.VDI_6007.weather import Weather

    test = Weather(prj.buildings[0].thermal_zones[0])
    test.get_solar_gains()
    None

if __name__ == '__main__':
    simulate_vdi()

    print("Example 9: That's it! :)")
