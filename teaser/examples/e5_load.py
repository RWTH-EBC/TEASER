# Created January 2017
# TEASER Development Team

"""This module contains an example how to import TEASER projects from
*.teaserjson and pickle in order to reuse data.
"""

import teaser.logic.utilities as utilities
import os


def example_load():
    """"This function demonstrates different loading options of TEASER"""

    # In example e4_save we saved two TEASER projects using *.teaserjson and
    # Python package pickle. This example shows how to import these
    # information into your python environment again.

    # To load data from *.teaserjson we can use a simple API function. So
    # first we need to instantiate our API (similar to example
    # e1_generate_archetype). The json file is called
    # `ArchetypeExample.teaserjson` and saved in the default path. You need to
    #  run e4 first before you can load this example file.

    from teaser.project import Project

    prj = Project()

    load_json = os.path.join(utilities.get_default_path(), "ArchetypeExample.json")

    prj.load_project(path=load_json)

    prj = Project()
    prj.load_project(utilities.get_full_path("examples/examplefiles/unitTest.json"))
    prj.save_project(file_name="unitTest", path=None)

    # To reload data from a pickle file, we do not need to instantiate an
    # API, as pickle will automatically instantiate all classes as they have
    # been saved. The saved file from example e4 is called ´teaser_pickle.p´

    import pickle

    load_pickle = os.path.join(utilities.get_default_path(), "teaser_pickle.p")

    pickle_prj = pickle.load(open(load_pickle, "rb"))
    print(pickle_prj)

    # After you imported your teaser project one or another way into you
    # python environment you can access variables and functions.


if __name__ == "__main__":
    example_load()

    print("Example 5: That's it! :)")
