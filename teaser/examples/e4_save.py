# Created January 2017
# TEASER Development Team

"""This module contains an example how to save buildings from a TEASER
project to XML and pickle in order to save information.
"""

import teaser.examples.e1_generate_archetype as e1
import teaser.logic.utilities as utilities
import os


def example_save():
    """"This function demonstrates different saving options of TEASER"""

    # In e1_generate_archetype we created a Project with three archetype
    # buildings to get this Project we rerun this example

    prj = e1.example_generate_archetype()

    # First option is to use TEASERs own XML format to save all relevant
    # data into a more or less human readable format. The corresponding
    # function is called Project().save_project() you can specify a file name
    #  and a save path. If both are non (as in this case) it will use the
    # projects name and default path in your home folder.

    prj.save_project(file_name=None, path=None)

    # Second option is to use pickle from Python Standard Library ,
    # which will save the whole Python classes and all attributes into a
    # binary file. There is no specific API function for this, but you can
    # simply create an empty file with open() and then use pickle.dump().
    # Make sure you specify your path correctly. In this case we want to use
    # the default path of TEASERs output.

    import pickle

    pickle_file = os.path.join(
        utilities.get_default_path(),
        'teaser_pickle.p')

    pickle.dump(prj, open(pickle_file, "wb"))


if __name__ == '__main__':
    example_save()

    print("Example 4: That's it! :)")
