# Created May 2016
# TEASER Development Team

"""annex60_output

This module contains function to call Templates for Annex60 model generation
"""
import teaser.data.output.aixlib_output as aixlib_output
import os.path
import teaser.logic.utilities as utilitis
from mako.template import Template


def export_annex60(prj,
                   number_of_elements=2,
                   merge_windows=False,
                   internal_id=None,
                   path=None):
    """Exports values to a record file for Annex60 simulation

    The Export function for creating a Annex60 example model

    Parameters
    ----------

    number_of_elements : int
            defines the number of elements, that area aggregated, between 1
            and 4, default is 2
    merge_windows : bool
            True for merging the windows into the outer walls, False for
            separate resistance for window, default is False
    internal_id : float
        setter of the used building which will be exported, if None then
        all buildings will be exported
    path : string
        if the Files should not be stored in OutputData, an alternative
        path can be specified as a full and absolute path

    """

    uses = ['Modelica(version = "3.2.2")',
            'Annex60(version="0.1")']

    if internal_id is not None:
        exported_list_of_buildings = [bldg for bldg in
                                      prj.buildings if
                                      bldg.internal_id == internal_id]
    else:
        exported_list_of_buildings = prj.buildings

    aixlib_output._help_package(path, prj.name, uses, within=None)
    aixlib_output._help_package_order(path, exported_list_of_buildings)

    if number_of_elements == 1:
        pass
    elif number_of_elements == 2:
        zone_template = Template(filename=utilitis.get_full_path(
            "data/output/modelicatemplate/Annex60/Annex60_TwoElements"))
    elif number_of_elements == 3:
        zone_template = Template(filename=utilitis.get_full_path(
            "data/output/modelicatemplate/Annex60/Annex60_ThreeElements"))
    elif number_of_elements == 4:
        zone_template = Template(filename=utilitis.get_full_path(
            "data/output/modelicatemplate/Annex60/Annex60_FourElements"))

    for bldg in exported_list_of_buildings:
        bldg_path = os.path.join(path,
                                 bldg.name)
        utilitis.create_path(utilitis.get_full_path(bldg_path))
        utilitis.create_path(utilitis.get_full_path(bldg_path+ "/" + bldg.name + \
                                                     "_Models"))
        aixlib_output._help_package(bldg_path, bldg.name, within=prj.name)
        aixlib_output._help_package_order(bldg_path,
                                          [bldg],
                                          None,
                                          bldg.name + "_Models")
        for zone in bldg.thermal_zones:
            zone_path = os.path.join(bldg_path,
                                     bldg.name+"_Models")

            out_file = open(utilitis.get_full_path(
                    zone_path + "/" + bldg.name + "_" +
                    zone.name.replace(" ", "") + ".mo"), 'w')
            out_file.write(zone_template.render_unicode(bldg=bldg,
                                                        zone=zone,
                                                        merge_windows=merge_windows,
                                                        within=(prj.name +
                                                                '.' +
                                                                bldg.name +
                                                                '.' +
                                                                bldg.name +
                                                                "_Models"),
                                                        modelica_info=prj.modelica_info,
                                                        weather=prj.weather_file_path))

            aixlib_output._help_package(zone_path,
                                        bldg.name + "_Models",
                                        within=prj.name + '.' + bldg.name)

            aixlib_output._help_package_order(zone_path,
                                              bldg.thermal_zones,
                                              (bldg.name + "_"))

            out_file.close()

    print("Exports can be found here:")
    print(path)
