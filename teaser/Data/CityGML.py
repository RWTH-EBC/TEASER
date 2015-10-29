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

from teaser.Project import Project
import teaser.Data.DataHelp.gmlhelp as gmlhelp

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
    for i,bldg_count in enumerate(project.list_of_buildings):
        
        gml_out.featureMember.append(citygml.cityObjectMember())
        
        gml_bldg = bldg.Building()
        
        '''set general attributes of the building, as far as they are known and
        are defined in cityGML'''
        gml_bldg.name = [og.gml.CodeType(bldg_count.name)]
        gml_bldg.function = [bldg.BuildingFunctionType(1120)]
        gml_bldg.yearOfConstruction = bd.datatypes.gYear(
                                            bldg_count.year_of_construction)
        gml_bldg.roofType = bldg.RoofTypeType(1000)
        gml_bldg.measuredHeight = gml.LengthType(bldg_count.number_of_floors * 
                                                bldg_count.height_of_floors)
        gml_bldg.measuredHeight.uom = bd.datatypes.anyURI('m')
        gml_bldg.storeysAboveGround = bldg_count.number_of_floors
        gml_bldg.storeyHeightsAboveGround = gml.MeasureOrNullListType(
            [bldg_count.height_of_floors]*int(bldg_count.number_of_floors))
        gml_bldg.storeyHeightsAboveGround.uom = bd.datatypes.anyURI('m')
        
        #building attributes from energyADE we can in principle provide
        
        gml_bldg.GenericApplicationPropertyOfAbstractBuilding.append(
                        energy.atticType("None"))
        gml_bldg.GenericApplicationPropertyOfAbstractBuilding.append(
                        energy.basementType("None"))
        gml_bldg.GenericApplicationPropertyOfAbstractBuilding.append(
                        energy.constructionStyle(bldg_count.construction_type))       
        gml_bldg.GenericApplicationPropertyOfAbstractBuilding.append(
                        energy.yearOfRefurbishment(
                        bd.datatypes.gYear(bldg_count.year_of_construction)))
        #unsolved problem with volume?
        #fixme what could be a method for placing the building 
        bldg_center = [i*100,0,0]     
                        
        building_length = bldg_count._est_length
        building_width = bldg_count._est_width
        building_height = (bldg_count.number_of_floors * 
                            bldg_count.height_of_floors)

        gml_bldg = gmlhelp.set_lod_2(gml_bldg, 
                                     building_length, 
                                     building_width, 
                                     building_height,
                                     bldg_center)
                                     
                                     
        """
        for zone_count in bldg_count.thermal_zones:
            
            gml_zone = energy.thermalZones()
            gml_zone.ThermalZone = energy.ThermalZoneType()
            gml_zone.ThermalZone.heatedFloorArea = gml.AreaType(
                                                            zone_count.area)
            gml_zone.ThermalZone.heatedFloorArea.uom = bd.datatypes.anyURI(
                                                                        'm^2')
            
            for out_wall_count in zone_count.outer_walls:
                
                 gml_zone.ThermalZone.boundedBy_.append(
                     energy.ThermalBoundarySurfacePropertyType())
                 gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface =\
                     energy.ThermalBoundarySurfaceType()
                 gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface.type =\
                     'OuterWall' 
                 gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface.\
                     composedOf.append(energy.SurfaceComponentPropertyType())
                 
                 gml_surf_comp = energy.SurfaceComponent()
                 gml_surf_comp.area = gml.AreaType(out_wall_count.area)
                 gml_surf_comp.area.uom = bd.datatypes.anyURI('m^2')
                 gml_surf_comp.relates = gml.ReferenceType()
                 gml_surf_comp.relates.href = "asd"
                 gml_surf_comp.isSunExposed = bd.datatypes.boolean("true")
                 gml_surf_comp.isGroundCoupled = bd.datatypes.boolean("true")

                 gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface.composedOf[-1].SurfaceComponent = gml_surf_comp

            gml_bldg.GenericApplicationPropertyOfAbstractBuilding.append(gml_zone)
        """
        gml_out.featureMember[-1].Feature = gml_bldg  
        
    
    out_file.write(gml_out.toDOM().toprettyxml())
           
    
"""
def setEnergyBoundary(self, boundedBy_en, wallType ,href, area, areaWin,nrOfWall):
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
                         number_of_floors=2,
                         height_of_floors=3,
                         net_leased_area=500 ,
                         office_layout=0,
                         window_layout=0,
                         construction_type="heavy")

prj.type_bldg_office(name="TestBuisdfsdfsdflding",
                         year_of_construction=1988,
                         number_of_floors=2,
                         height_of_floors=3,
                         net_leased_area=500 ,
                         office_layout=0,
                         window_layout=0,
                         construction_type="heavy")                      

save_gml(prj, "Test")
print("ahhasd")
