# Created October 2015
# TEASER 4 Development Team

"""CityGML

This module contains function to save and load Projects in the non proprietary
CityGML file format .gml
"""
import pyxb
import pyxb.utils
import pyxb.namespace
import pyxb.bundles
import teaser.Data.SchemaBindings.opengis
import pyxb.bundles.common.raw.xlink as xlink
import teaser.Data.SchemaBindings.opengis.raw as og
import teaser.Data.SchemaBindings.opengis.raw.gml as gml
import teaser.Data.SchemaBindings.opengis.citygml
import teaser.Data.SchemaBindings.opengis.citygml.raw
import teaser.Data.SchemaBindings.opengis.citygml.raw.base as citygml
import teaser.Data.SchemaBindings.opengis.citygml.raw.building as bldg
import teaser.Data.SchemaBindings.opengis.citygml.raw.energy as energy

import teaser.Data.DataHelp.gmlhelp as gmlhelp

def save_gml(project, path, ref_coordinates=None):
    '''This function saves a project to a cityGML file

    The function needs the Python Package PyXB. And the opengis bundle for GML
    and CityGML.

    Parameters
    ----------
    project: Project()
        Teaser instance of Project()
    path: string
        complete path to the output file
    ref_coordinates: list
        list with  lower and one upper reference coordinates. Each coordiante
        should contain 3 ints or floats for x, y, and z coordinates of the 
        point. e.g: [[458877,,5438353, -0.2], [458889,5438363,6.317669]]
    '''
    
    if path.endswith("gml"):
        out_file = open(path, 'w')
    else:
        out_file = open(path + ".gml", 'w')

    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        citygml.Namespace, 'core')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        gml.Namespace, 'gml')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        bldg.Namespace, 'bldg')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        energy.Namespace, 'energy')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        xlink.Namespace, 'xlink')

    gml_out = citygml.CityModel()
    gml_out.name = [og.gml.CodeType(project.name)]

    if ref_coordinates != None:
        
        gml_out = gmlhelp.set_reference_boundary(gml_out,
                                                 ref_coordinates[0],
                                                 ref_coordinates[1])
    else: 
        bldg_center = [0,0,0]
        pass

    for i, bldg_count in enumerate(project.buildings):

        gml_out.featureMember.append(citygml.cityObjectMember())

        gml_bldg = gmlhelp.set_gml_building(bldg_count)
        
        bldg_center = [i*80, 0, 0]
        building_length = None
        building_width = None
        building_height = None
        if type(bldg_count).__name__ == "Residential":
            building_length = (bldg_count.thermal_zones[0].area /
                               bldg_count.thermal_zones[0].typical_width)
            building_width = bldg_count.thermal_zones[0].typical_width
            building_height = (bldg_count.number_of_floors *
                               bldg_count.height_of_floors)

        else:
            building_width = 0.05 * (bldg_count.net_leased_area /
                                     bldg_count.number_of_floors)
            building_length = (bldg_count.net_leased_area /
                               bldg_count.number_of_floors) / building_width
            building_height = (bldg_count.number_of_floors *
                               bldg_count.height_of_floors)

        gml_bldg = gmlhelp.set_lod_2(gml_bldg,
                                     building_length,
                                     building_width,
                                     building_height,
                                     bldg_center)

        for zone_count in bldg_count.thermal_zones:

            gml_zone = gmlhelp.set_gml_thermal_zone(zone_count)

            for out_wall_count in zone_count.outer_walls:

                outer_bound = gmlhelp.set_gml_thermal_boundary(gml_zone,
                                                               out_wall_count)

                for win_count in zone_count.windows:

                    if out_wall_count.orientation == win_count.orientation and\
                        out_wall_count.tilt == win_count.tilt:

                        gmlhelp.set_gml_surface_component(outer_bound,
                                                          win_count,
                                                          "true",
                                                          "false")

            for in_wall_count in zone_count.inner_walls:

                gmlhelp.set_gml_thermal_boundary(gml_zone, in_wall_count)

            gml_bldg.GenericApplicationPropertyOfAbstractBuilding.append(
                gml_zone)

        gml_out.featureMember[-1].Feature = gml_bldg

    out_file.write(gml_out.toDOM().toprettyxml())
