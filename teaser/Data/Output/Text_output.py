# Created March 2016
# TEASER Development Team

"""Text_output

This module contains function to call Templates for textual output
"""
import teaser.Logic.Utilis as utilis

def export_parameters_txt(prj, path=None):
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

    for bldg in prj.list_of_buildings:
        bldg_path = path + "\\" + bldg.name + "\\"
        utilis.create_path(utilis.get_full_path(bldg_path))
        readable_template = Template(
            filename=utilis.get_full_path(
                "InputData\\ReadableOutputTemplate\\ReadableBuilding"))

        out_file = open(utilis.get_full_path
                        (bldg_path+"ReadableOutput.txt"), 'w')
        out_file.write(readable_template.render_unicode
                       (bldg=bldg, prj=prj))
        out_file.close()