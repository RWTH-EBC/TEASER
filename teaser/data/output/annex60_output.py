# Created May 2016
# TEASER Development Team

"""annex60_output

This module contains function to call Templates for Annex60 model generation
"""

import teaser.data.output.aixlib_output as aixlib_output
import os.path
import teaser.logic.utilities as utilities
from mako.template import Template
from mako.lookup import TemplateLookup


def export_annex60(
        buildings,
        prj,
        path=None):
    """Exports models for Annex60 library

    Export a building to several models for
    Annex60.ThermalZones.ReducedOrder. Depending on the chosen calculation
    method models for 1, 2, 3, or 4 element model are exported. In addition
    you can specify if windows should be lumped into the walls, like it is
    done in VDI 6007 (merge_windows=True) or not. For each zone, one model is
    exported, if you want to combine all thermal zones into one model, consider
    using AixLib. The export includes internal gains from use conditions (
    calculated in teaser.logic.calculation.annex60) but does not include any
    heating or cooling equipment.


    Parameters
    ----------

    buildings : list of instances of Building
        list of TEASER instances of a Building that are exoirted If you want to
        export a single building, please pass it over as a list containing
        only that building.
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
    model_template_2 : Template object
        Template for ThermalZoneRecord using 2 element model
    zone_template_3 : Template object
        Template for ThermalZoneRecord using 4 element model
    zone_template_4 : Template object
        Template for ThermalZoneRecord using 5 element model

    """

    uses = uses = [
        'Modelica(version="' + prj.modelica_info.version + '")',
        'Annex60(version="' + prj.buildings[-1].library_attr.version + '")']

    lookup = TemplateLookup(directories=[utilities.get_full_path(
        "data/output/modelicatemplate/")])
    model_template_2 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/Annex60/Annex60_TwoElements"),
        lookup=lookup)
    model_template_3 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/Annex60/Annex60_ThreeElements"),
        lookup=lookup)
    model_template_4 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/Annex60/Annex60_FourElements"),
        lookup=lookup)

    aixlib_output._help_package(
        path=path,
        name=prj.name,
        uses=uses,
        within=None)
    aixlib_output._help_package_order(
        path=path,
        package_list=buildings,
        addition=None,
        extra=None)

    for i, bldg in enumerate(buildings):

        bldg_path = os.path.join(path, bldg.name)

        utilities.create_path(utilities.get_full_path(bldg_path))
        utilities.create_path(utilities.get_full_path(
            os.path.join(bldg_path, bldg.name + "_Models")))

        aixlib_output._help_package(
            path=bldg_path,
            name=bldg.name,
            within=bldg.parent.name)

        aixlib_output._help_package_order(
            path=bldg_path,
            package_list=[bldg],
            addition=None,
            extra=bldg.name + "_Models")

        for zone in bldg.thermal_zones:

            zone_path = os.path.join(
                bldg_path,
                bldg.name + "_Models")
            zone.parent.library_attr.file_internal_gains = 'InternalGains_' +\
                                                           bldg.name + \
                                                           zone.name + '.mat'
            bldg.library_attr.modelica_gains_boundary(
                time_line=None,
                path=zone_path)

            out_file = open(utilities.get_full_path(os.path.join(
                zone_path, bldg.name + '_' + zone.name + '.mo')), 'w')

            if type(zone.model_attr).__name__ == "OneElement":
                pass
            elif type(zone.model_attr).__name__ == "TwoElement":
                out_file.write(model_template_2.render_unicode(zone=zone))
            elif type(zone.model_attr).__name__ == "ThreeElement":
                out_file.write(model_template_2.render_unicode(zone=zone))
            elif type(zone.model_attr).__name__ == "FourElement":
                pass

            aixlib_output._help_package(zone_path,
                                        bldg.name + "_Models",
                                        within=prj.name + '.' + bldg.name)

            aixlib_output._help_package_order(zone_path,
                                              bldg.thermal_zones,
                                              (bldg.name + "_"))

            out_file.close()

    print("Exports can be found here:")
    print(path)
