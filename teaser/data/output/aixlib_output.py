# Created March 2016
# TEASER Development Team

"""aixlib_output

This module contains function to call Templates for AixLib model generation
"""

import os
import warnings
from mako.template import Template
import teaser.logic.utilities as utilities


def export_aixlib(buildings,
                  path=None):
    """Exports values to a model file for library AixLib

    Exports a building for
    AixLib.ThermalZones.ReducedOrder.Multizone.MultizoneEquipped models
    using the ThermalZoneEquipped model with a correction of g-value (
    double pane glazing) and supporting models, like tables and weather
    model. In contrast to versions < 0.5 TEASER now does not
    support any model options, as we observed no need, since single
    ThermalZones are identically with Annex60 models. If you miss one of
    the old options please contact us.

    This function uses Mako Templates specified in
    data.output.modelicatemplates.AixLib

    Parameters
    ----------

    buildings : list of instances of Building
        list of TEASER instances of a Building that is exported to a AixLib
        MultizoneEquipped models. If you want to export a single building,
        please pass it over as a list containing only that building.
    path : string
        if the Files should not be stored in default output path of TEASER,
        an alternative path can be specified as a full path
    """

    zone_template = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib/AixLib_ThermalZoneRecord"))
    model_template = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib/AixLib_Multizone"))

    for i, bldg in enumerate(buildings):

        bldg_path = os.path.join(path, bldg.name)
        utilities.create_path(utilities.get_full_path(bldg_path))
        utilities.create_path(utilities.get_full_path
                       (os.path.join(bldg_path,
                                      bldg.name + "_DataBase")))
        bldg.library_atrr.modelica_set_temp(path=os.path.join(
                                                        bldg_path,
                                                        bldg.name))
        bldg.library_atrr.modelica_AHU_boundary(
            time_line=None,
            path=os.path.join(bldg_path, bldg.name))
        bldg.library_atrr.modelica_gains_boundary(
            time_line=None,
            path=os.path.join(bldg_path, bldg.name))

        _help_package(path=bldg_path, name=bldg.name, within=bldg.parent.name)

        _help_package_order(
            path=bldg_path,
            package_list=[bldg],
            addition=None,
            extra=bldg.name + "_DataBase")

        if bldg.building_id is None:
            bldg.building_id = i
        else:
            try:
                bldg.building_id = int(bldg.building_id)
            except UserWarning:
                warnings.warn("Cannot convert building_id to integer, "
                              "is set to ", i, "which is the enumeration "
                              "number of the building in the project list.")
                bldg.building_id = i

        out_file = open(utilities.get_full_path
                    (os.path.join(bldg_path, bldg.name + ".mo")), 'w')

        out_file.write(model_template.render_unicode(
                       bldg=bldg,
                       weather=bldg.parent.weather_file_path,
                       modelica_info=bldg.parent.modelica_info))
    out_file.close()

    for zone in bldg.thermal_zones:
        zone_path = bldg_path + bldg.name + "_DataBase" + "/"

        out_file = open(utilities.get_full_path(
            zone_path + "/" + bldg.name + "_" +
            zone.name.replace(" ", "") + ".mo"), 'w')
        out_file.write(zone_template.render_unicode(
            bldg=bldg,
            zone=zone,
            mod_prj=prj.modelica_project,
            number_of_elements=number_of_elements))
        out_file.close()

    _help_package(zone_path,
                  bldg.name + "_DataBase",
                  within=prj.name + '.' + bldg.name)
    _help_package_order(zone_path,
                        bldg.thermal_zones,
                            bldg.name + "_")
    print("Exports can be found here:")
    print(path)

    elif building_model == "None" and zone_model == "None" and\
        corG is None:
        # only export the baserecords
        _help_package(path, prj.name, uses)
        _help_package_order(path, exported_list_of_buildings)
        for bldg in exported_list_of_buildings:

            bldg_path = path + "/" + bldg.name + "/"
            utilities.create_path(utilities.get_full_path(bldg_path))
            utilities.create_path(utilities.get_full_path
                               (bldg_path + bldg.name + "_DataBase"))

            _help_package(bldg_path, bldg.name, within=prj.name)
            _help_package_order(bldg_path, [bldg], None,
                                     bldg.name + "_DataBase")

            for zone in bldg.thermal_zones:
                zone_path = bldg_path + bldg.name + "_DataBase" + "/"

                out_file = open(utilities.get_full_path(
                    zone_path + "/" + bldg.name + "_" +
                    zone.name.replace(" ", "") + ".mo"), 'w')
                out_file.write(zone_template.render_unicode(
                    bldg=bldg,
                    zone=zone,
                    calc_core=bldg._calculation_method,
                    mod_prj=prj.modelica_project,
                    number_of_elements=number_of_elements))

                out_file.close()

            _help_package(zone_path,
                          bldg.name + "_DataBase",
                          within=prj.name + '.' + bldg.name)
            _help_package_order(zone_path,
                                bldg.thermal_zones,
                                bldg.name + "_")

        print("Exports can be found here:")
        print(path)

    else:
        # not clearly specified
        print("please specify you export clearly")



def _help_package(path, name, uses=None, within=None):
    '''creates a package.mo file

    private function, do not call

    Parameters
    ----------

    path : string
        path of where the package.mo should be placed
    name : string
        name of the Modelica package
    within : string
        path of Modelica package containing this package

    '''

    package_template = Template(filename=utilities.get_full_path
                                ("data/output/modelicatemplate/package"))
    out_file = open(
        utilities.get_full_path(path + "/" + "package" + ".mo"), 'w')
    out_file.write(package_template.render_unicode(name=name,
                                                   within=within,
                                                   uses=uses))
    out_file.close()

def _help_package_order(path, package_list, addition=None, extra=None):
    '''creates a package.order file

    private function, do not call

    Parameters
    ----------

    path : string
        path of where the package.order should be placed
    package_list : [string]
        name of all models or packages contained in the package
    addition : string
        if there should be a suffix in front of package_list.string it can
        be specified
    extra : string
        an extra package or model not contained in package_list can be
        specified

    '''
    order_template = Template(filename=utilities.get_full_path
                              ("data/output/modelicatemplate/package_order"))

    out_file = open(
        utilities.get_full_path(path + "/" + "package" + ".order"), 'w')
    out_file.write(order_template.render_unicode
                   (list=package_list, addition=addition, extra=extra))
    out_file.close()
