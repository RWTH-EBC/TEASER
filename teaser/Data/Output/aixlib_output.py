# Created March 2016
# TEASER Development Team

"""Modelica_output

This module contains function to call Templates for Modelica model generation
"""

import teaser.Logic.Utilis as utilis
from mako.template import Template
import scipy.io
import teaser.Logic.Simulation.aixlib as aixlib

def export_aixlib(prj,
                  building_model="None",
                  zone_model="None",
                  corG=None,
                  internal_id=None,
                  path=None):
    '''Exports values to a record file for Modelica simulation

    The Export function for creating a AixLib LOM Multizone model

    Parameters
    ----------

    building_model : string
        setter of the used Aixlib building model (None, MultizoneEquipped,
        Multizone)
    zone_model : string
        setter of the used Aixlib zone model (ThermalZoneEquipped,
        ThermalZone)
    corG : boolean
        setter of the used g value calculation in the model
    internal_id : float
        setter of the used building which will be exported, if None then
        all buildings will be exported
    path : string
        if the Files should not be stored in OutputData, an alternative
        path can be specified as a full and absolute path

    '''

    #check the arguments
    assert building_model in ["None", "MultizoneEquipped", "Multizone"]
    assert zone_model in ["None", "ThermalZoneEquipped", "ThermalZone"]
    assert corG in [None, True, False]

    uses = ['Modelica(version = "3.2.1")',
            "AixLib(version=\"0.2.5\")"]

    # use the same zone templates for all exports
    zone_template = Template(
        filename=utilis.get_full_path(
            "Data\\Output\\ModelicaTemplate\\AixLib\\AixLib_zone"))
    model_template = Template(
        filename=utilis.get_full_path(
            "Data\\Output\\ModelicaTemplate\\AixLib\\AixLib_model"))
    zone_base_template = Template(
        filename=utilis.get_full_path(
            "Data\\Output\\ModelicaTemplate\\AixLib\\AixLib_base"))
    # list which contains exported buildings
    if internal_id is not None:
        exported_list_of_buildings = [bldg for bldg in
                                      prj.buildings if
                                      bldg.internal_id == internal_id]
    else:
        exported_list_of_buildings = prj.buildings

    # here we diff between zonerecord export and full model support
    if building_model != "None" and zone_model != "None" and\
        corG is not None:
        # full model support here
        print("full model support")

        _help_package(path, prj.name, uses)
        _help_package_order(path, exported_list_of_buildings)

        for bldg in exported_list_of_buildings:

            if bldg.merge_windows_calc is True:
                calc_method = 'vdi'
            elif bldg.merge_windows_calc is False:
                calc_method = 'ebc'

            bldg_path = path + "\\" + bldg.name + "\\"
            utilis.create_path(utilis.get_full_path(bldg_path))
            utilis.create_path(utilis.get_full_path
                               (bldg_path + bldg.name + "_DataBase"))
            aixlib.modelica_set_temp(bldg=bldg, path=path + "\\" + bldg.name)
            aixlib.modelica_AHU_boundary(bldg=bldg, path=path + "\\" + bldg.name)
            aixlib.modelica_gains_boundary(bldg=bldg, path=path + "\\" + bldg.name)

            _help_package(bldg_path, bldg.name)
            _help_package_order(bldg_path, [bldg], None,
                                     bldg.name + "_DataBase")

            out_file = open(utilis.get_full_path
                            (bldg_path + bldg.name + ".mo"), 'w')


            out_file.write(model_template.render_unicode(
                           bldg=bldg, mod_prj=prj.modelica_project,
                           weather=prj.weather_file_path,
                           weather_header=prj.weather_file_header,
                           model=building_model,
                           zone=zone_model,
                           physics=calc_method,
                           gFac=corG))
            out_file.close()

            for zone in bldg.thermal_zones:
                zone_path = bldg_path + bldg.name + "_DataBase" + "\\"

                out_file = open(utilis.get_full_path(
                    zone_path + "\\" + bldg.name + "_" +
                    zone.name.replace(" ", "") + ".mo"), 'w')
                out_file.write(zone_template.render_unicode(
                    bldg=bldg, zone=zone))
                out_file.close()

            _help_package(zone_path, bldg.name + "_DataBase")
            _help_package_order(
                zone_path, bldg.thermal_zones,
                bldg.name + "_", bldg.name + "_base")

            out_file = open(utilis.get_full_path
                            (zone_path + bldg.name + "_base.mo"),
                            'w')
            if bldg.central_ahu:
                out_file.write(zone_base_template.render_unicode(
                    bldg=bldg,
                    zone=zone,
                    mod_prj=prj.modelica_project,
                    central_ahu=bldg.central_ahu))
                out_file.close()
            else:
                out_file.write(zone_base_template.render_unicode(
                    bldg=bldg,
                    zone=zone,
                    mod_prj=prj.modelica_project))
                out_file.close()
        print("Exports can be found here:")
        print(path)

    elif building_model == "None" and zone_model == "None" and\
        corG is None:
        # only export the baserecords
        _help_package(path, prj.name, uses)
        _help_package_order(path, exported_list_of_buildings)
        for bldg in exported_list_of_buildings:

            bldg_path = path + "\\" + bldg.name + "\\"
            utilis.create_path(utilis.get_full_path(bldg_path))
            utilis.create_path(utilis.get_full_path
                               (bldg_path + bldg.name + "_DataBase"))

            _help_package(bldg_path, bldg.name)
            _help_package_order(bldg_path, [bldg], None,
                                     bldg.name + "_DataBase")
            for zone in bldg.thermal_zones:
                zone_path = bldg_path + bldg.name + "_DataBase" + "\\"

                out_file = open(utilis.get_full_path(
                    zone_path + "\\" + bldg.name + "_" +
                    zone.name.replace(" ", "") + ".mo"), 'w')
                out_file.write(zone_template.render_unicode(
                    bldg=bldg, zone=zone,
                    calc_core=bldg._calculation_method))

                out_file.close()
        print("Exports can be found here:")
        print(path)

    else:
        # not clearly specified
        print("please specify you export clearly")



def _help_package(path, name, uses=None):
    '''creates a package.mo file

    private function, do not call

    Parameters
    ----------

    path : string
        path of where the package.mo should be placed
    name : string
        name of the Modelica package

    '''

    package_template = Template(filename=utilis.get_full_path
                                ("Data\\Output\\ModelicaTemplate\\package"))
    out_file = open(
        utilis.get_full_path(path + "\\" + "package" + ".mo"), 'w')
    out_file.write(package_template.render_unicode(name=name, uses=uses))
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
    order_template = Template(filename=utilis.get_full_path
                              ("Data\\Output\\ModelicaTemplate\\package_order"))

    out_file = open(
        utilis.get_full_path(path + "\\" + "package" + ".order"), 'w')
    out_file.write(order_template.render_unicode
                   (list=package_list, addition=addition, extra=extra))
    out_file.close()