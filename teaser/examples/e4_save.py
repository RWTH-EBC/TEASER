# Created January 2017
# TEASER Development Team

"""This module contains an example how to save buildings from a TEASER
project to various formats to save information.
"""

import teaser.examples.e1_generate_archetype as e1

def example_save():
    """"This function demonstrates different saving options of TEASER"""

    # In e1_generate_archetype we created a Project with three archetype
    # buildings to get this Project we rerun this example

    prj = e1.example_generate_archetype()

    # TEASERXML

    # pickle

    # probably do not include CityGML as we can't reload it


if __name__ == '__main__':
    example_save()
    
    print("Example 4: That's it! :)")
