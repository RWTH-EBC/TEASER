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
import pyxb.bundles.opengis
import pyxb.bundles.common.raw.xlink as xlink
import pyxb.binding as bd
import pyxb.bundles.opengis.raw as og
import pyxb.bundles.opengis.raw.gml as gml
import pyxb.bundles.opengis.citygml
import pyxb.bundles.opengis.citygml.raw
import pyxb.bundles.opengis.citygml.base as citygml
import pyxb.bundles.opengis.citygml.appearance as app
import pyxb.bundles.opengis.citygml.building as bldg
import pyxb.bundles.opengis.citygml.energy as energy

import teaser.Data.DataHelp.gmlhelp as gmlhelp

def save_gml(project, path):
    '''This function saves a project to a cityGML file 
    
    The function needs the Python Package PyXB. And the opengis bundle for GML
    and CityGML.

    Parameters
    ----------
    project: Project()
        Teaser instance of Project()
    path: string
        complete path to the output file
    '''
    
    new_path = path + ".gml"
    out_file = open(new_path, 'w')
    
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        citygml.Namespace, 'core')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        gml.Namespace, 'gml')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        bldg.Namespace, 'bldg')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        app.Namespace, 'app')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        energy.Namespace, 'energy')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        xlink.Namespace, 'xlink')
    
    gml_out = citygml.CityModel()
    gml_out.name = [og.gml.CodeType(project.name)]

    
    #fixme: what kind of coordiantes we have to use e.g. for Aachen?    
    """    
    gml_out = gmlhelp.set_reference_boundary(gml_out,
                                             lower_coords=[458877,
                                                           5438353,
                                                           -0.2],
                                             upper_coords=[458889,
                                                           5438363,
                                                           6.317669])
    """                                                       
    for n,bldg_count in enumerate(project.list_of_buildings):
        
        gml_out.featureMember.append(citygml.cityObjectMember())
        
        gml_bldg = gmlhelp.set_gml_building(bldg_count)

        #unsolved problem with volume?
        #fixme what could be a method for placing the building 
        bldg_center = [n*80,0,0]  
        
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
                                                
            for i, out_wall_count in enumerate(zone_count.outer_walls):
                
                tb = gmlhelp.set_gml_thermal_boundary(gml_zone, out_wall_count)  
                
                for i, win_count in enumerate(zone_count.windows):
                    
                    if out_wall_count.orientation == win_count.orientation and\
                        out_wall_count.tilt == win_count.tilt:
                            
                        gmlhelp.set_gml_surface_component(tb, 
                                                          win_count, 
                                                          "true", 
                                                          "false")                   
            
            for i, in_wall_count in enumerate(zone_count.inner_walls):
                
                gmlhelp.set_gml_thermal_boundary(gml_zone, in_wall_count)

            gml_bldg.GenericApplicationPropertyOfAbstractBuilding.append(gml_zone)
        
        gml_out.featureMember[-1].Feature = gml_bldg 
        
    out_file.write(gml_out.toDOM().toprettyxml())
