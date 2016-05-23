# Created March 2016
# TEASER Development Team

"""Text_output

This module contains function to call Templates for textual output
"""
import teaser.Logic.utilities as utilitis
from mako.template import Template

def export_parameters_txt(prj, path):
    '''Exports parameters of all buildings in a readable text file

    Parameters
    ----------

    path : string
        if the Files should not be stored in OutputData, an alternative
        can be specified
    '''
    if path is None:
        path = "OutputData\\"+prj.name
    else:
        path = path+"\\"+prj.name

    for bldg in prj.buildings:
        bldg_path = path + "\\" + bldg.name + "\\"
        utilitis.create_path(utilitis.get_full_path(bldg_path))
        readable_template = Template(
            filename=utilitis.get_full_path(
                "Data\\Output\\TextTemplate\\ReadableBuilding"))

        out_file = open(utilitis.get_full_path
                        (bldg_path+"ReadableOutput.txt"), 'w')
        out_file.write(readable_template.render_unicode
                       (bldg=bldg, prj=prj))
        out_file.close()
