'''
Created on 05.05.2015

@author: pre
'''
import copy

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

def set_bldg_elements(gml_bldg, bldg_count):
    
    
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
    return gml_bldg                    
                    
def set_reference_boundary(gml_out, lower_coords, upper_coords):
    """Adds a reference coordinate system with `Envelope`'s corners

    The gml file includes a reference coordinate system defined in the 
    `boundedBy` object, within which the `Envelope` object contains both a
    `lowerCorner` and an `upperCorner`. Both corners extend 
    `gml.DirectPositionType`. This method sets all necessary parts of the
    `boundedBy` in a given gml file.

    Parameters
    ----------

    gml_out : citygml.CityModel() object
        A CityModel object, where citygml is a reference to 
        `pyxb.bundles.opengis.citygml.base`. The reference coordinate system
        will be added to this object.
    lower_coords : list
        A list that contains the coordinates of the point for the 
        `lowerCorner` definition. It should contain 3 ints or floats for 
        x, y, and z coordinates of the point.
    upper_coords : list
        A list that contains the coordinates of the point for the 
        `upperCorner` definition. It should contain 3 ints or floats for 
        x, y, and z coordinates of the point.

    Returns
    -------

    gml_out : citygml.CityModel() object
        Returns the modified CityModel object
    """
    assert len(lower_coords) == 3, 'lower_coords must contain 3 elements'
    assert len(upper_coords) == 3, 'lower_coords must contain 3 elements'

    reference_bound = gml.boundedBy()

    reference_envelope = gml.Envelope()
    reference_envelope.srsDimension = 3
    reference_envelope.srsName = 'urn:adv:crs:ETRS89_UTM32'

    lower_corner = gml.DirectPositionType(lower_coords)
    lower_corner.srsDimension = 3
    reference_envelope.lowerCorner = lower_corner
    upper_corner = gml.DirectPositionType(upper_coords)
    upper_corner.srsDimension = 3
    reference_envelope.upperCorner = upper_corner

    reference_bound.Envelope = reference_envelope
    gml_out.boundedBy = reference_bound

    return gml_out

def set_lod_2(gml_bldg, length, width, height, bldg_center):
    """Adds a LOD 2 representation of the building based on building length, 
    width and height

    alternative way to handle building position

    Parameters
    ----------

    gml_bldg : bldg.Building() object
        A building object, where bldg is a reference to
        `pyxb.bundles.opengis.citygml.building`.
    length : float
        length of the building
    width : float
        width of the building
    height : float
        height of the building
    bldg_center : list
        coordinates in the reference system of the building center

    Returns
    -------

    gml_bldg : bldg.Building() object
        Returns the modified building object

    """
    boundary_surface = []
    lod_2_solid = gml.SolidPropertyType()
    
    #fixme what is arcrole?
    #lod_2_solid.arcrole = 'Test'
    
    lod_2_solid.Solid = gml.Solid_()
    exterior_solid = gml.SurfacePropertyType()
    composite_surface = gml.CompositeSurface()
    
    bldg_center[0] = bldg_center[0]-length/2
    bldg_center[1] = bldg_center[1]-width/2
    
    # Ground surface   
    coords = [[bldg_center[0],bldg_center[1],bldg_center[2]],
              [length + bldg_center[0],bldg_center[1],bldg_center[2]],
              [length + bldg_center[0],width + bldg_center[1],bldg_center[2]],
              [bldg_center[0],width + bldg_center[1],bldg_center[2]]]
              
    composite_surface = _add_surface(composite_surface, coords)
    composite_surface.surfaceMember[-1].Surface.id = gml_bldg.name[0].value()+"_ground"
    
    
    boundary_surface.append(bldg.BoundarySurfacePropertyType())
    boundary_surface[-1].BoundarySurface = bldg.FloorSurface()
    
    boundary_surface[-1].BoundarySurface = _add_gml_boundary(
                            boundary_surface[-1].BoundarySurface, 
                            gml_bldg.name[0].value()+"_ground")
    
    
    # Roof surface
    coords = [[bldg_center[0],bldg_center[1],bldg_center[2]+height],
              [length + bldg_center[0],bldg_center[1],bldg_center[2]+height],
              [length + bldg_center[0],width + bldg_center[1],bldg_center[2]+height],
              [bldg_center[0],width + bldg_center[1],bldg_center[2]+height]]
              
    composite_surface = _add_surface(composite_surface, coords)
    composite_surface.surfaceMember[-1].Surface.id = gml_bldg.name[0].value()+"_roof"


    boundary_surface.append(bldg.BoundarySurfacePropertyType())
    boundary_surface[-1].BoundarySurface = bldg.RoofSurface()
    
    boundary_surface[-1].BoundarySurface = _add_gml_boundary(
                            boundary_surface[-1].BoundarySurface, 
                            gml_bldg.name[0].value()+"_roof")

    # Side a surface
    coords = [[bldg_center[0],bldg_center[1],bldg_center[2]],
              [length + bldg_center[0],bldg_center[1],bldg_center[2]],
              [length + bldg_center[0],bldg_center[1],bldg_center[2]+height],
              [bldg_center[0],bldg_center[1],bldg_center[2]+height]]
              
    composite_surface = _add_surface(composite_surface, coords)
    composite_surface.surfaceMember[-1].Surface.id = gml_bldg.name[0].value()+"_a"
    
    boundary_surface.append(bldg.BoundarySurfacePropertyType())
    boundary_surface[-1].BoundarySurface = bldg.WallSurface()
    
    boundary_surface[-1].BoundarySurface = _add_gml_boundary(
                            boundary_surface[-1].BoundarySurface, 
                            gml_bldg.name[0].value()+"_a")    
    
    # Side b surface
    
    coords = [[bldg_center[0],width + bldg_center[1],bldg_center[2]],
              [length + bldg_center[0],width + bldg_center[1],bldg_center[2]],
              [length + bldg_center[0],width + bldg_center[1],bldg_center[2]+height],
              [bldg_center[0],width + bldg_center[1],bldg_center[2]+height]]
    composite_surface = _add_surface(composite_surface, coords)
    composite_surface.surfaceMember[-1].Surface.id = gml_bldg.name[0].value()+"_b"
    
    boundary_surface.append(bldg.BoundarySurfacePropertyType())
    boundary_surface[-1].BoundarySurface = bldg.WallSurface()
    
    boundary_surface[-1].BoundarySurface = _add_gml_boundary(
                            boundary_surface[-1].BoundarySurface, 
                            gml_bldg.name[0].value()+"_b")       
    # Side c surface
    coords = [[bldg_center[0],bldg_center[1],bldg_center[2]],
              [bldg_center[0],width + bldg_center[1],bldg_center[2]],
              [bldg_center[0],width + bldg_center[1],bldg_center[2]+height],
              [bldg_center[0],bldg_center[1],bldg_center[2]+height]]
    composite_surface = _add_surface(composite_surface, coords)
    composite_surface.surfaceMember[-1].Surface.id = gml_bldg.name[0].value()+"_c"
    
    boundary_surface.append(bldg.BoundarySurfacePropertyType())
    boundary_surface[-1].BoundarySurface = bldg.WallSurface()
    
    boundary_surface[-1].BoundarySurface = _add_gml_boundary(
                            boundary_surface[-1].BoundarySurface, 
                            gml_bldg.name[0].value()+"_c")     
    # Side d surface
    coords = [[length + bldg_center[0],bldg_center[1],bldg_center[2]],
              [length + bldg_center[0],width + bldg_center[1],bldg_center[2]],
              [length + bldg_center[0],width + bldg_center[1],bldg_center[2]+height],
              [length + bldg_center[0],bldg_center[1],bldg_center[2]+height]]
    composite_surface = _add_surface(composite_surface, coords)
    composite_surface.surfaceMember[-1].Surface.id = gml_bldg.name[0].value()+"_d"
    
    boundary_surface.append(bldg.BoundarySurfacePropertyType())
    
    boundary_surface[-1].BoundarySurface = bldg.WallSurface()
    
    boundary_surface[-1].BoundarySurface = _add_gml_boundary(
                            boundary_surface[-1].BoundarySurface, 
                            gml_bldg.name[0].value()+"_d")       
    
    exterior_solid.Surface = composite_surface
    lod_2_solid.Solid.exterior = exterior_solid

    gml_bldg.lod2Solid = lod_2_solid
    gml_bldg.boundedBy_ = boundary_surface
    return gml_bldg
   
def _add_surface(composite_surface, coords):
    """Adds a surface to the  LOD representation of the building 

    Parameters
    ----------

    composite_surface : gml.CompositeSurface() object
        A surface object object for one side of the building
    coords : list
        A list that contains the coordinates of the 4 points defining the
        ground area of the building. Each of the 4 list elements should consist
        of a list with 3 ints or floats for the x, y, and z coordinates of one
        point.

    Returns
    -------

    composite_surface : gml.CompositeSurface() object
        Returns the modified composite surface object

    """
    assert len(coords) == 4, 'coords must contain 4 elements'
    for coord in coords:
        assert len(coord) == 3, 'Each coord list should contain 3 elements'

    composite_surface.surfaceMember.append(gml.SurfacePropertyType())
    polygon = gml.Polygon()
    linear_ring = gml.LinearRing()
    exterior_polygon = gml.AbstractRingPropertyType(linear_ring)

    input_list = []
    for coord in coords:
        for value in coord:
            input_list.append(value)
    for value in coords[0]:
        input_list.append(value)
    
    pos_list = gml.posList(input_list)
    """
    fixme what is srsDimension
    pos_list.srsDimension = 3
    """
    linear_ring.posList = pos_list
    exterior_polygon.LinearRing = linear_ring
    polygon.exterior = exterior_polygon
    
    composite_surface.surfaceMember[-1].Surface = polygon
    
    return composite_surface
    
def _add_gml_boundary(boundary_surface, id):
    """Adds a surface to the  LOD representation of the building 

    Parameters
    ----------

    boundary_surface : bldg.BoundarySurfacePropertyType() object
        A boundary surface object (Roof, Wall, Floor) for one side of the bldg
    id : str
        gmlID of the corresponding gml.Solid to reference the Surface

    Returns
    -------

    boundary_surface : gml.BoundarySurfacePropertyType() object
        Returns the modified boundary surface object

    """
    boundary_surface.id = "b_"+id
    boundary_surface.lod2MultiSurface = gml.MultiSurfacePropertyType()
    boundary_surface.lod2MultiSurface.MultiSurface = gml.MultiSurfaceType()
    boundary_surface.lod2MultiSurface.MultiSurface.surfaceMember.append(
                                                    gml.SurfacePropertyType())
    boundary_surface.lod2MultiSurface.MultiSurface.surfaceMember[-1].href = id
    
    boundary_surface.opening.append(bldg.OpeningPropertyType())
    boundary_surface.opening[-1].Opening = bldg.Window()
    boundary_surface.opening[-1].Opening.id =id+"_win"    
    
    return boundary_surface
    
def gml_thermal_zone(thermal_zone):
    """creates a gml instance of a thermal zone
    
    EnergyADE includes information of a thermal zone, these values are set in
    this class.    

    Parameters
    ----------

    thermal_zone : ThermalZone() object
        A ThermalZone object, from TEASER

    Returns
    -------

    gml_zone : energy.thermalZones() object
        A thermalZone object, where energy is a reference to 
        `pyxb.bundles.opengis.citygml.energy`.
    """
    gml_zone = energy.thermalZones()
    gml_zone.ThermalZone = energy.ThermalZoneType()
    gml_zone.ThermalZone.heatedFloorArea = gml.AreaType(thermal_zone.area)
    gml_zone.ThermalZone.heatedFloorArea.uom = bd.datatypes.anyURI('m^2')
    gml_zone.ThermalZone.infiltrationRate = gml.MeasureType(
                                        thermal_zone.infiltration_rate)
    gml_zone.ThermalZone.infiltrationRate.uom = bd.datatypes.anyURI('1/h')
    
    return gml_zone                                                            

def gml_thermal_boundary(gml_zone, wall):
    _current_tb = None
    
    if type(wall).__name__ == "OuterWall":
        
        gml_zone.ThermalZone.boundedBy_.append(
                            energy.ThermalBoundarySurfacePropertyType())
        gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface =\
                            energy.ThermalBoundarySurfaceType()
                            
        _current_tb = gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface
        _current_tb.type = 'OuterWall' 
        _current_tb.azimuth = gml.AngleType(wall.orientation)
        _current_tb.azimuth.uom = bd.datatypes.anyURI('deg')
        _current_tb.inclination = gml.AngleType(wall.tilt)
        _current_tb.inclination.uom = bd.datatypes.anyURI('deg')

        gml_surface_component(_current_tb, 
                              wall, 
                              sun_exp="true", 
                              grnd_coupled="true")  
        return _current_tb
        
    elif type(wall).__name__ == "Rooftop":
        
        gml_zone.ThermalZone.boundedBy_.append(
                            energy.ThermalBoundarySurfacePropertyType())
        gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface =\
                            energy.ThermalBoundarySurfaceType()
                            
        _current_tb = gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface
        _current_tb.type = 'FlatRoof' 

        _current_tb.inclination = gml.AngleType(wall.tilt)
        _current_tb.inclination.uom = bd.datatypes.anyURI('deg')

        gml_surface_component(_current_tb, 
                              wall, 
                              sun_exp="true", 
                              grnd_coupled="true")

    elif type(wall).__name__ == "GroundFloor":
        
        gml_zone.ThermalZone.boundedBy_.append(
                            energy.ThermalBoundarySurfacePropertyType())
        gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface =\
                            energy.ThermalBoundarySurfaceType()
                            
        _current_tb = gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface
        _current_tb.type = 'BasementFloor' 

        _current_tb.inclination = gml.AngleType(wall.tilt)
        _current_tb.inclination.uom = bd.datatypes.anyURI('deg')      
        
        gml_surface_component(_current_tb, 
                              wall, 
                              sun_exp="false", 
                              grnd_coupled="true")
    
    elif type(wall).__name__ == "InnerWall" \
    or type(wall).__name__ == "Ceiling"\
    or type(wall).__name__ == "Floor":
        
        gml_zone.ThermalZone.boundedBy_.append(
                            energy.ThermalBoundarySurfacePropertyType())
        gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface =\
                            energy.ThermalBoundarySurfaceType()
                            
        _current_tb = gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface
        _current_tb.type = 'SharedWall' 
        _current_tb.inclination = gml.AngleType(wall.tilt)
        _current_tb.inclination.uom = bd.datatypes.anyURI('deg')
        _current_tb.inclination = gml.AngleType(wall.tilt)
        _current_tb.inclination.uom = bd.datatypes.anyURI('deg')      
        
        gml_surface_component(_current_tb, 
                              wall, 
                              sun_exp="false", 
                              grnd_coupled="false")

def gml_surface_component(thermal_boundary, wall, sun_exp, grnd_coupled):   

    thermal_boundary.composedOf.append(energy.SurfaceComponentPropertyType())

    gml_surf_comp = energy.SurfaceComponent()
    gml_surf_comp.area = gml.AreaType(wall.area)
    gml_surf_comp.area.uom = bd.datatypes.anyURI('m^2')
    #fixme: how to relate to corresponding boundarySurface
    gml_surf_comp.relates = gml.ReferenceType()
    #gml_surf_comp.relates.href = "asd"
    gml_surf_comp.isSunExposed = bd.datatypes.boolean(sun_exp)
    gml_surf_comp.isGroundCoupled = bd.datatypes.boolean(grnd_coupled)
    
    gml_layer(gml_surf_comp, wall)    
    
    thermal_boundary.composedOf[-1].SurfaceComponent = gml_surf_comp
    
def gml_layer(gml_surf_comp, wall):

    construction = energy.construction()
    construction.Construction = energy.ConstructionType() 
    construction.Construction.name = [og.gml.CodeType(wall.name)]
    if type(wall).__name__ == "Window":
        
        construction.Construction.transmittance.append(energy.TransmittancePropertyType())
        construction.Construction.transmittance[-1].Transmittance = energy.Transmittance() 
        construction.Construction.transmittance[-1].Transmittance.percentage = wall.g_value
        construction.Construction.transmittance[-1].Transmittance.wavelengthRange = energy.WavelengthRangeTypeType("Solar")
    
    for lay_count in wall.layer:
        layer = energy.LayerPropertyType()
        layer.Layer = energy.LayerType()
        layer.Layer.layerComponent.append(energy.LayerComponentPropertyType())         
        layer.Layer.layerComponent[-1].LayerComponent = energy.LayerComponentType()
    
        _current_layer =  layer.Layer.layerComponent[-1].LayerComponent       
        
        _current_layer.thickness = gml.LengthType(lay_count.thickness) 
        _current_layer.thickness.uom = bd.datatypes.anyURI('m')
         
        
        if type(wall).__name__ != "Window":
            
            gml_opaque_material(_current_layer, lay_count)
            
            construction.Construction.layer.append(layer)  
            
        else:
            
            
            gml_glazing_material(_current_layer, lay_count)
    
            construction.Construction.layer.append(layer)                    
    
    gml_surf_comp.GenericApplicationPropertyOfCityObject.append(construction)
    
    
def gml_opaque_material(gml_layer, teaser_layer):
    
    gml_layer.material = energy.AbstractMaterialPropertyType()
    gml_layer.material.AbstractMaterial = energy.OpaqueMaterial()
            
    _current_material = gml_layer.material.AbstractMaterial
    _current_material.name = [og.gml.CodeType(teaser_layer.material.name)]
    _current_material.conductivity = gml.MeasureType(
                                        teaser_layer.material.thermal_conduc)
    _current_material.conductivity.uom = bd.datatypes.anyURI('W/mK') 
    _current_material.density = gml.MeasureType(teaser_layer.material.density)
    _current_material.density.uom = bd.datatypes.anyURI('kg/m^3') 
    _current_material.specificHeat = gml.MeasureType(
                                        teaser_layer.material.heat_capac)
    _current_material.specificHeat.uom = bd.datatypes.anyURI('kJ/kg')
    
def gml_glazing_material(gml_layer, teaser_layer):
    
    gml_layer.material = energy.AbstractMaterialPropertyType()
    gml_layer.material.AbstractMaterial = energy.OpaqueMaterial()
            
    _current_material = gml_layer.material.AbstractMaterial
    _current_material.name = [og.gml.CodeType(teaser_layer.material.name)]
    _current_material.conductivity = gml.MeasureType(
                                        teaser_layer.material.thermal_conduc)
    _current_material.conductivity.uom = bd.datatypes.anyURI('W/mK') 
    
