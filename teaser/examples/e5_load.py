# Created January 2017
# TEASER Development Team

"""This module contains an example how to import TEASER projects from
*.teaserXML and pickle in order to reuse data.
"""

import teaser.logic.utilities as utilities
import os


def example_save():
    """"This function demonstrates different loading options of TEASER"""

    # In example e4_save we saved two TEASER projects using *.teaserXML and
    # Python package pickle. This example shows how to import these
    # information into your python environment again.

    # To load data from *.teaserXML we can use a simple API function. So
    # first we need to instantiate our API (similar to example
    # e1_generate_archetype). The XML file is called
    # `ArchetypeExample.teaserXML` and saved in the default path.

    from teaser.project import Project

    prj = Project()

    load_xml =  pickle_file = os.path.join(
        utilities.get_default_path(),
        'ArchetypeExample.teaserXML')

    prj.load_project(
        path=load_xml)

    # To reload data from a pickle file, we do not need to instantiate an
    # API, as pickle will automatically instantiate all classes as they have
    # been saved. The saved file from example e4 is called ´teaser_pickle.p´

    import pickle

    load_pickle = pickle_file = os.path.join(
        utilities.get_default_path(),
        'teaser_pickle.p')

    pickle_prj = pickle.load(open(load_pickle, "rb"))

if __name__ == '__main__':
    example_save()

    print("Example 5: That's it! :)")
