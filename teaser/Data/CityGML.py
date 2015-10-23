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
import pyxb.bundles.opengis.citygml.generics as gen
import pyxb.bundles.opengis.citygml.vegetation as veg
import pyxb.bundles.opengis.citygml.waterBody as wtr
import pyxb.bundles.opengis.citygml.transportation as trans
import pyxb.bundles.opengis.citygml.appearance as app
import pyxb.bundles.opengis.citygml.cityFurniture as frn
import pyxb.bundles.opengis.citygml.cityObjectGroup as grp
import pyxb.bundles.opengis.citygml.building as bldg
import pyxb.bundles.opengis.citygml.landUse as luse
import pyxb.bundles.opengis.citygml.relief as dem
import pyxb.bundles.opengis.citygml.utility_core as network_core
import pyxb.bundles.opengis.citygml.utility_network_components as network_comp
import pyxb.bundles.opengis.citygml.energy as energy

from teaser.Project import Project
import teaser.Logic.Utilis as utilis

def save_gml(project, path):
    '''This function saves a project to a cityGML file 
    
    The function needs the Python Package PyXB. And the opengis bundle   

    Parameters
    ----------
    project: Project()
        Teaser instance of Project()
    path: string
        complete path to the output file
    '''
    
    new_path = path + ".gml"
    out_file = open(new_path, 'w')
    
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(citygml.Namespace, 'core')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(gml.Namespace, 'gml')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(bldg.Namespace, 'bldg')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(app.Namespace, 'app')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(energy.Namespace, 'energy')
    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(xlink.Namespace, 'xlink')
    
    gml_out = citygml.CityModel()
    gml_out.name = [og.gml.CodeType(project.name)]
    
    for bldg_count in project.list_of_buildings:
        
        gml_out.featureMember.append(citygml.cityObjectMember())
        
        gml_bldg = bldg.Building()
        gml_bldg.name = [og.gml.CodeType(bldg_count.name)]
        gml_bldg.yearOfConstruction = bd.datatypes.gYear(bldg_count.year_of_construction)
        
        
        for zone_count in bldg_count.thermal_zones:
            
            gml_zone = energy.thermalZones()
            gml_zone.ThermalZone = energy.ThermalZoneType()
            gml_zone.ThermalZone.heatedFloorArea = gml.AreaType(zone_count.area)
            gml_zone.ThermalZone.heatedFloorArea.uom = bd.datatypes.anyURI('m^2')
            
            for out_wall_count in zone_count.outer_walls:
                
                 gml_zone.ThermalZone.boundedBy_.append(energy.ThermalBoundarySurfacePropertyType())
                 gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface = energy.ThermalBoundarySurfaceType()
                 gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface.type = 'OuterWall' 
                 gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface.composedOf.append(energy.SurfaceComponentPropertyType())
                 
                 gml_surf_comp = energy.SurfaceComponent()
                 gml_surf_comp.area = gml.AreaType(out_wall_count.area)
                 gml_surf_comp.area.uom = bd.datatypes.anyURI('m^2')
                 gml_surf_comp.relates = gml.ReferenceType()
                 gml_surf_comp.relates.href = "asd"
                 gml_surf_comp.isSunExposed = bd.datatypes.boolean("true")
                 gml_surf_comp.isGroundCoupled = bd.datatypes.boolean("true")

                 gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface.composedOf[-1].SurfaceComponent = gml_surf_comp

            gml_bldg.GenericApplicationPropertyOfAbstractBuilding.append(gml_zone)
            
        gml_out.featureMember[-1].Feature = gml_bldg  
        
    
    out_file.write(gml_out.toDOM().toprettyxml())
           
    
"""
ef setEnergyBoundary(self, boundedBy_en, wallType ,href, area, areaWin,nrOfWall):
        '''
        sets the energy boundary surfaces
        arguments:
        ----------
        boundedBy_en: list of the walls that are bounding the building for energy (first call empty)
        wallType: wall Type defined in gml (OuterWall, FlatRoof, BasementFloor)
        href: connection to boundary of gml
        area: area of wall surface
        areaWin: area of window surface
        nrOfWall: counter of the number of wall of the building
        '''
        boundedBy_en.append(energy.ThermalBoundarySurfacePropertyType())
        boundedBy_en[nrOfWall].ThermalBoundarySurface = energy.ThermalBoundarySurfaceType()
        boundedBy_en[nrOfWall].ThermalBoundarySurface.type = wallType
        boundedBy_en[nrOfWall].ThermalBoundarySurface.composedOf.append(energy.SurfaceComponentPropertyType())
        
        wall = self.setSurfaceComponent(area, href, wallType)
        
        boundedBy_en[nrOfWall].ThermalBoundarySurface.composedOf[0].SurfaceComponent = wall
        
        boundedBy_en[nrOfWall].ThermalBoundarySurface.composedOf.append(energy.SurfaceComponentPropertyType())
        if wallType == "OuterWall":
            window = self.setSurfaceComponent(areaWin, href, "Window")
            boundedBy_en[nrOfWall].ThermalBoundarySurface.composedOf[1].SurfaceComponent = window
        else:
            pass
        return boundedBy_en
"""
    
prj = Project(True)
prj.type_bldg_office(name="TestBuilding",
                         year_of_construction=1988,
                         number_of_floors=7,
                         height_of_floors=1,
                         net_leased_area=1988 ,
                         office_layout=0,
                         window_layout=0,
                         construction_type="heavy")
prj.type_bldg_institute(name="TestBuilding1",
                         year_of_construction=1988,
                         number_of_floors=7,
                         height_of_floors=1,
                         net_leased_area=1988 ,
                         office_layout=0,
                         window_layout=0,
                         construction_type="heavy")
prj.type_bldg_institute4(name="TestBuilding2",
                         year_of_construction=1988,
                         number_of_floors=7,
                         height_of_floors=1,
                         net_leased_area=1988 ,
                         office_layout=0,
                         window_layout=0,
                         construction_type="heavy")
save_gml(prj, "Test")