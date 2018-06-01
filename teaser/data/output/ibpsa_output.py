# Created May 2016
# TEASER Development Team

"""ibpsa_output

This module contains function to call Templates for IBPSA model generation
"""

import teaser.data.output.aixlib_output as ibpsa_output
import os.path
import teaser.logic.utilities as utilities
from mako.template import Template
from mako.lookup import TemplateLookup


def export_ibpsa(
        buildings,
        prj,
        path=None,
        library='AixLib'):
    """Exports models for IBPSA library

    Export a building to several models for
    IBPSA.ThermalZones.ReducedOrder. Depending on the chosen calculation
    method models for 1, 2, 3, or 4 element model are exported. In addition
    you can specify if windows should be lumped into the walls, like it is
    done in VDI 6007 (merge_windows=True) or not. For each zone, one model is
    exported, if you want to combine all thermal zones into one model, consider
    using AixLib. The export includes internal gains from use conditions (
    calculated in teaser.logic.calculation.ibpsa) but does not include any
    heating or cooling equipment.


    Parameters
    ----------

    buildings : list of instances of Building
        list of TEASER instances of a Building that are exported If you
        want to
        export a single building, please pass it over as a list containing
        only that building.
    prj : instance of Project
        Instance of TEASER Project object to access Project related
        information, e.g. name or version of used libraries
    path : string
        if the Files should not be stored in default output path of TEASER,
        an alternative path can be specified as a full path
    library : str
        Used library within the framework of IBPSA library. The
        models are identical in each library, but IBPSA Modelica library is
        just a core set of models and should not be used standalone.
        Valid values are 'AixLib' (default), 'Buildings',
        'BuildingSystems' and 'IDEAS'.

     Attributes
    ----------

    lookup : TemplateLookup object
        Instance of mako.TemplateLookup to store general functions for templates
    model_template_1 : Template object
        Template for ThermalZoneRecord using 1 element model
    model_template_2 : Template object
        Template for ThermalZoneRecord using 2 element model
    model_template_3 : Template object
        Template for ThermalZoneRecord using 3 element model
    model_template_4 : Template object
        Template for ThermalZoneRecord using 4 element model

    """

    uses = uses = [
        'Modelica(version="' + prj.modelica_info.version + '")',
        library + '(version="' + prj.buildings[-1].library_attr.version[
            library] + '")']

    lookup = TemplateLookup(directories=[utilities.get_full_path(
        os.path.join('data', 'output', 'modelicatemplate'))])
    model_template_1 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/IBPSA/IBPSA_OneElement"),
        lookup=lookup)
    model_template_2 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/IBPSA/IBPSA_TwoElements"),
        lookup=lookup)
    model_template_3 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/IBPSA/IBPSA_ThreeElements"),
        lookup=lookup)
    model_template_4 = Template(
        filename=utilities.get_full_path(
            "data/output/modelicatemplate/IBPSA/IBPSA_FourElements"),
        lookup=lookup)

    ibpsa_output._help_package(
        path=path,
        name=prj.name,
        uses=uses,
        within=None)
    ibpsa_output._help_package_order(
        path=path,
        package_list=buildings,
        addition=None,
        extra=None)

    for i, bldg in enumerate(buildings):

        ass_error = "You chose AixLib calculation, " \
                    "but want to export IBPSA models, " \
                    "this is not possible"

        assert bldg.used_library_calc == 'IBPSA', ass_error

        bldg_path = os.path.join(path, bldg.name)

        utilities.create_path(utilities.get_full_path(bldg_path))
        utilities.create_path(utilities.get_full_path(
            os.path.join(bldg_path, bldg.name + "_Models")))

        ibpsa_output._help_package(
            path=bldg_path,
            name=bldg.name,
            within=bldg.parent.name)

        ibpsa_output._help_package_order(
            path=bldg_path,
            package_list=[],
            addition=None,
            extra=bldg.name + "_Models")

        zone_path = os.path.join(
            bldg_path,
            bldg.name + "_Models")

        for zone in bldg.thermal_zones:

            zone.parent.library_attr.file_internal_gains = \
                'InternalGains_' + bldg.name + zone.name + '.mat'
            bldg.library_attr.modelica_gains_boundary(
                zone=zone,
                time_line=None,
                path=zone_path)

            out_file = open(utilities.get_full_path(os.path.join(
                zone_path, bldg.name + '_' + zone.name + '.mo')), 'w')

            if type(zone.model_attr).__name__ == "OneElement":
                out_file.write(model_template_1.render_unicode(zone=zone,
                                                               library=library))
            elif type(zone.model_attr).__name__ == "TwoElement":
                out_file.write(model_template_2.render_unicode(zone=zone,
                                                               library=library))
            elif type(zone.model_attr).__name__ == "ThreeElement":
                out_file.write(model_template_3.render_unicode(zone=zone,
                                                               library=library))
            elif type(zone.model_attr).__name__ == "FourElement":
                out_file.write(model_template_4.render_unicode(zone=zone,
                                                               library=library))

            out_file.close()

        ibpsa_output._help_package(
            path=zone_path,
            name=bldg.name + "_Models",
            within=prj.name + '.' + bldg.name)

        ibpsa_output._help_package_order(
            path=zone_path,
            package_list=bldg.thermal_zones,
            addition=bldg.name + "_")

    print("Exports can be found here:")
    print(path)
