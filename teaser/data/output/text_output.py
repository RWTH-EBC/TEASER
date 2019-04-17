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

    prj : TEASER project
        Project to export
    path : string
        if the Files should not be stored in OutputData, an alternative
        can be specified
    """

    lookup = TemplateLookup(directories=[utilities.get_full_path(
        os.path.join('data', 'output', 'modelicatemplate'))])

    model_template_1 = Template(
        filename=utilities.get_full_path(
            os.path.join(
                'data',
                'output',
                'texttemplate',
                'ReadableBuilding_OneElement')),
        lookup=lookup)
    model_template_2 = Template(
        filename=utilities.get_full_path(
            os.path.join(
                'data',
                'output',
                'texttemplate',
                'ReadableBuilding_TwoElement')),
        lookup=lookup)
    model_template_3 = Template(
        filename=utilities.get_full_path(
            os.path.join(
                'data',
                'output',
                'texttemplate',
                'ReadableBuilding_ThreeElement')),
        lookup=lookup)
    model_template_4 = Template(
        filename=utilities.get_full_path(
            os.path.join(
                'data',
                'output',
                'texttemplate',
                'ReadableBuilding_FourElement')),
        lookup=lookup)

    for bldg in prj.buildings:
        bldg_path = os.path.join(
            path,
            bldg.name + "_txtOutput")
        utilities.create_path(bldg_path)
        out_file = open(os.path.join(bldg_path, bldg.name + ".txt"), 'w')

        if type(bldg.thermal_zones[0].model_attr).__name__ == "OneElement":
            out_file.write(model_template_1.render_unicode(bldg=bldg))
        elif type(bldg.thermal_zones[0].model_attr).__name__ == "TwoElement":
            out_file.write(model_template_2.render_unicode(bldg=bldg))
        elif type(bldg.thermal_zones[0].model_attr).__name__ == "ThreeElement":
            out_file.write(model_template_3.render_unicode(bldg=bldg))
        elif type(bldg.thermal_zones[0].model_attr).__name__ == "FourElement":
            out_file.write(model_template_4.render_unicode(bldg=bldg))

        out_file.close()
