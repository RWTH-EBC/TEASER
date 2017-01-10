# Created March 2016
# TEASER Development Team

"""Text_output

This module contains function to call Templates for textual output
"""
import teaser.logic.utilities as utilities
from mako.template import Template
from mako.lookup import TemplateLookup
import os


def export_parameters_txt(prj, path):
    """Exports parameters of all buildings in a readable text file

    Parameters
    ----------

    path : string
        if the Files should not be stored in OutputData, an alternative
        can be specified
    """

    if path is None:
        path = os.path.join(os.path.expanduser('~'), "TEASEROutput/", prj.name)
    else:
        path = os.path.join(path, prj.name)

    lookup = TemplateLookup(directories=[utilities.get_full_path(
        os.path.join('data', 'output', 'modelicatemplate'))])

    for bldg in prj.buildings:
        bldg_path = os.path.join(
            path,
            bldg.name + "_txtOutput")
        utilities.create_path(bldg_path)
        readable_template = Template(
            filename=utilities.get_full_path(
                os.path.join(
                    'data',
                    'output',
                    'texttemplate',
                    'ReadableBuilding')),
            lookup=lookup)

        out_file = open((bldg_path + "ReadableOutput.txt"), 'w')
        out_file.write(readable_template.render_unicode
                       (bldg=bldg, prj=prj))
        out_file.close()
