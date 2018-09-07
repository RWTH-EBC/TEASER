# Created March 2016
# TEASER Development Team

"""ibpsa_output

This module contains function to call Templates for AixLib model generation
"""

import os
import warnings
from mako.template import Template
from mako.lookup import TemplateLookup
import teaser.logic.utilities as utilities


def export_multizone(buildings, prj, path=None):
    """Exports models for AixLib library

    Exports a building for
    AixLib.ThermalZones.ReducedOrder.Multizone.MultizoneEquipped models
    using the ThermalZoneEquipped and supporting models, like tables and weather
    model. Depending on chosen calculation method the parameter set to 1,2,
    3 or 4 element model. By default it uses the  correction for solar
    glazing (corG) and decoupled heat conduction through windows (
    merge_windows=False). In contrast to versions < 0.5 TEASER now does not
    support any other model options, as we observed no need, since single
    ThermalZones are identical with IBPSA models. If you miss one of the
    old options please contact us.

    This function uses Mako Templates specified in
    data.output.modelicatemplates.AixLib

    Parameters
    ----------

    buildings : list of instances of Building
        list of TEASER instances of a Building that is exported to a AixLib
        MultizoneEquipped models. If you want to export a single building,
        please pass it over as a list containing only that building.
    prj : instance of Project
        Instance of TEASER Project object to access Project related
        information, e.g. name or version of used libraries
    path : string
        if the Files should not be stored in default output path of TEASER,
        an alternative path can be specified as a full path

    Attributes
    ----------

    lookup : TemplateLookup object
        Instance of mako.TemplateLookup to store general functions for templates
    zone_template_1 : Template object
        Template for ThermalZoneRecord using 1 element model
    zone_template_2 : Template object
        Template for ThermalZoneRecord using 2 element model
    zone_template_3 : Template object
        Template for ThermalZoneRecord using 3 element model
    zone_template_4 : Template object
        Template for ThermalZoneRecord using 4 element model
    model_template : Template object
        Template for MultiZone model
    """

    lookup = TemplateLookup(directories=[utilities.get_full_path(
        os.path.join('data', 'output', 'modelicatemplate'))])
    zone_template_1 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib"
            "/AixLib_ThermalZoneRecord_OneElement"),
        lookup=lookup)
    zone_template_2 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib"
            "/AixLib_ThermalZoneRecord_TwoElement"),
        lookup=lookup)
    zone_template_3 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib"
            "/AixLib_ThermalZoneRecord_ThreeElement"),
        lookup=lookup)
    zone_template_4 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib"
            "/AixLib_ThermalZoneRecord_FourElement"),
        lookup=lookup)
    model_template = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/AixLib/AixLib_Multizone"),
        lookup=lookup)

    uses = [
        'Modelica(version="' + prj.modelica_info.version + '")',
        'AixLib(version="' + prj.buildings[-1].library_attr.version + '")']
    _help_package(
        path=path,
        name=prj.name,
        uses=uses,
        within=None)
    _help_package_order(
        path=path,
        package_list=buildings,
        addition=None,
        extra=None)

    for i, bldg in enumerate(buildings):

        ass_error = "You chose IBPSA calculation, " \
                    "but want to export AixLib models, " \
                    "this is not possible"

        assert bldg.used_library_calc == 'AixLib', ass_error

        bldg_path = os.path.join(path, bldg.name)
        utilities.create_path(utilities.get_full_path(bldg_path))
        utilities.create_path(utilities.get_full_path(
            os.path.join(bldg_path,
                         bldg.name + "_DataBase")))
        bldg.library_attr.modelica_set_temp(path=bldg_path)
        bldg.library_attr.modelica_AHU_boundary(
            time_line=None,
            path=bldg_path)
        bldg.library_attr.modelica_gains_boundary(
            time_line=None,
            path=bldg_path)

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
                                               "number of the building in "
                                               "the project list.")
                bldg.building_id = i

        out_file = open(utilities.get_full_path
                        (os.path.join(bldg_path, bldg.name + ".mo")), 'w')

        out_file.write(model_template.render_unicode(
            bldg=bldg,
            weather=bldg.parent.weather_file_path,
            modelica_info=bldg.parent.modelica_info))
        out_file.close()

        zone_path = os.path.join(bldg_path, bldg.name + "_DataBase")

        for zone in bldg.thermal_zones:

            out_file = open(utilities.get_full_path(os.path.join(
                zone_path, bldg.name + '_' + zone.name + '.mo')), 'w')
            if type(zone.model_attr).__name__ == "OneElement":
                out_file.write(zone_template_1.render_unicode(zone=zone))
            elif type(zone.model_attr).__name__ == "TwoElement":
                out_file.write(zone_template_2.render_unicode(zone=zone))
            elif type(zone.model_attr).__name__ == "ThreeElement":
                out_file.write(zone_template_3.render_unicode(zone=zone))
            elif type(zone.model_attr).__name__ == "FourElement":
                out_file.write(zone_template_4.render_unicode(zone=zone))

            out_file.close()

        _help_package(
            path=zone_path,
            name=bldg.name + '_DataBase',
            within=prj.name + '.' + bldg.name)
        _help_package_order(
            path=zone_path,
            package_list=bldg.thermal_zones,
            addition=bldg.name + "_",
            extra=None)

    print("Exports can be found here:")
    print(path)


def _help_package(path, name, uses=None, within=None):
    """creates a package.mo file

    private function, do not call

    Parameters
    ----------

    path : string
        path of where the package.mo should be placed
    name : string
        name of the Modelica package
    within : string
        path of Modelica package containing this package

    """

    package_template = Template(filename=utilities.get_full_path(
        "data/output/modelicatemplate/package"))
    out_file = open(
        utilities.get_full_path(os.path.join(path, "package.mo")), 'w')
    out_file.write(package_template.render_unicode(
        name=name,
        within=within,
        uses=uses))
    out_file.close()


def _help_package_order(path, package_list, addition=None, extra=None):
    """creates a package.order file

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

    """

    order_template = Template(filename=utilities.get_full_path(
        "data/output/modelicatemplate/package_order"))

    out_file = open(
        utilities.get_full_path(path + "/" + "package" + ".order"), 'w')
    out_file.write(order_template.render_unicode
                   (list=package_list, addition=addition, extra=extra))
    out_file.close()
