# Created July 2015
# TEASER Development Team

"""This module contains an example that shows how to retrofit all buildings
in a TEASER project with different setups
"""

import teaser.examples.e1_generate_archetype as e1


def example_create_building():
    """"This function demonstrates retrofit options of TEASER API"""

    # In e1_generate_archetype we created a Project with three archetype
    # buildings to get this Project we rerun this example

    prj = e1.example_generate_archetype()

    # To apply simplified retrofit for all buildings in the project we can
    # use Project.retrofit_all_buildings() function. This will retrofit all
    # building in the project in following manner:
    # 1. Replace all window with a new window (default is EnEv window with
    # U-Value of XYZ
    # 2. Add an additional insulation layer to all outer walls (including,
    # roof and ground floor). Set the thickness that it corresponds to the
    # retrofit standard od the year of retrofit.
    # The year of retrofit has to be specified. In addition, we can set
    # the used window_type and the type of insulation material used.

    prj.retrofit_all_buildings(
        year_of_retrofit=2015,
        window_type='Alu- oder Stahlfenster, Isolierverglasung',
        material='EPS035')


if __name__ == '__main__':
    example_create_building()
    print("Example 7: That's it :)")
