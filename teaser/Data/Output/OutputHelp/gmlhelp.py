# created October 2015
# by TEASER4 Development Team
"""gmlhelp

This module contains function to instantiate and set citygml classes and
attributes
"""
import pyxb.binding as bd
import teaser.Data.SchemaBindings.opengis.raw as og
import teaser.Data.SchemaBindings.opengis.raw.gml as gml
import teaser.Data.SchemaBindings.opengis.citygml.raw.building as bldg
import teaser.Data.SchemaBindings.opengis.citygml.raw.energy as energy

def set_gml_building(teaser_building):
    """Creates an instance of a citygml Building with attributes

    creates a citygml.building.Building object. And fills the attributes of
    this instance with attributes of the TEASER buidling

    Parameters
    ----------

    teaser_building : Building Object of TEASER
        Instance of a TEASER object with set attributes

    Returns
    -------

    gml_bldg : citygml.building.Building() object
        Returns a citygml Building with attributes
    """
    gml_bldg = bldg.Building()

    gml_bldg.name = [og.gml.CodeType(teaser_building.name)]
    gml_bldg.function = [bldg.BuildingFunctionType(1120)]
    gml_bldg.yearOfConstruction =\
                                bd.datatypes.gYear(teaser_building.\
                                                   year_of_construction)
    gml_bldg.roofType = bldg.RoofTypeType(1000)
    gml_bldg.measuredHeight = gml.LengthType(teaser_building.number_of_floors *
                                             teaser_building.height_of_floors)
    gml_bldg.measuredHeight.uom = bd.datatypes.anyURI('m')
    gml_bldg.storeysAboveGround = teaser_building.number_of_floors
    gml_bldg.storeyHeightsAboveGround = gml.MeasureOrNullListType(
                                        [teaser_building.height_of_floors]*
                                        int(teaser_building.number_of_floors))
    gml_bldg.storeyHeightsAboveGround.uom = bd.datatypes.anyURI('m')

    #building attributes from energyADE we can in principle provide

    gml_bldg.GenericApplicationPropertyOfAbstractBuilding.append(
                    energy.atticType("None"))
    gml_bldg.GenericApplicationPropertyOfAbstractBuilding.append(
                    energy.basementType("None"))
#    gml_bldg.GenericApplicationPropertyOfAbstractBuilding.append(
#                    energy.constructionStyle(teaser_building.construction_type))
    gml_bldg.GenericApplicationPropertyOfAbstractBuilding.append(
                    energy.yearOfRefurbishment(
                    bd.datatypes.gYear(teaser_building.year_of_construction)))
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

    lod_2_solid.Solid = gml.Solid_()
    exterior_solid = gml.SurfacePropertyType()
    composite_surface = gml.CompositeSurface()

    bldg_center[0] = bldg_center[0]-length/2
    bldg_center[1] = bldg_center[1]-width/2

    # Ground surface
    coords = [[bldg_center[0], bldg_center[1], bldg_center[2]],
              [length + bldg_center[0], bldg_center[1], bldg_center[2]],
              [length + bldg_center[0], width + bldg_center[1], bldg_center[2]],
              [bldg_center[0], width + bldg_center[1], bldg_center[2]]]

    composite_surface = _add_surface(composite_surface, coords)
    composite_surface.surfaceMember[-1].Surface.id = gml_bldg.name[0].value()+"_ground"


    boundary_surface.append(bldg.BoundarySurfacePropertyType())
    boundary_surface[-1].BoundarySurface = bldg.FloorSurface()

    boundary_surface[-1].BoundarySurface = _add_gml_boundary(
                            boundary_surface[-1].BoundarySurface,
                            gml_bldg.name[0].value()+"_ground")


    # Roof surface
    coords = [[bldg_center[0], bldg_center[1], bldg_center[2]+height],
              [length + bldg_center[0], bldg_center[1], bldg_center[2]+height],
              [length + bldg_center[0], width + bldg_center[1],
                                                        bldg_center[2]+height],
              [bldg_center[0], width + bldg_center[1], bldg_center[2]+height]]

    composite_surface = _add_surface(composite_surface, coords)
    composite_surface.surfaceMember[-1].Surface.id = (gml_bldg.name[0].value()+
                                                      "_roof")

    boundary_surface.append(bldg.BoundarySurfacePropertyType())
    boundary_surface[-1].BoundarySurface = bldg.RoofSurface()

    boundary_surface[-1].BoundarySurface = _add_gml_boundary(
                            boundary_surface[-1].BoundarySurface,
                            gml_bldg.name[0].value()+"_roof")

    # Side a surface
    coords = [[bldg_center[0], bldg_center[1], bldg_center[2]],
              [length + bldg_center[0], bldg_center[1], bldg_center[2]],
              [length + bldg_center[0], bldg_center[1], bldg_center[2]+height],
              [bldg_center[0], bldg_center[1], bldg_center[2]+height]]

    composite_surface = _add_surface(composite_surface, coords)
    composite_surface.surfaceMember[-1].Surface.id = (gml_bldg.name[0].value()+
                                                      "_a")

    boundary_surface.append(bldg.BoundarySurfacePropertyType())
    boundary_surface[-1].BoundarySurface = bldg.WallSurface()

    boundary_surface[-1].BoundarySurface = _add_gml_boundary(
                            boundary_surface[-1].BoundarySurface,
                            gml_bldg.name[0].value()+"_a")

    # Side b surface

    coords = [[bldg_center[0], width + bldg_center[1], bldg_center[2]],
              [length + bldg_center[0], width + bldg_center[1],
                                                       bldg_center[2]],
              [length + bldg_center[0], width + bldg_center[1],
                                                       bldg_center[2]+height],
              [bldg_center[0], width + bldg_center[1], bldg_center[2]+height]]

    composite_surface = _add_surface(composite_surface, coords)
    composite_surface.surfaceMember[-1].Surface.id = (gml_bldg.name[0].value()+
                                                      "_b")

    boundary_surface.append(bldg.BoundarySurfacePropertyType())
    boundary_surface[-1].BoundarySurface = bldg.WallSurface()

    boundary_surface[-1].BoundarySurface = _add_gml_boundary(
                            boundary_surface[-1].BoundarySurface,
                            gml_bldg.name[0].value()+"_b")
    # Side c surface
    coords = [[bldg_center[0], bldg_center[1], bldg_center[2]],
              [bldg_center[0], width + bldg_center[1], bldg_center[2]],
              [bldg_center[0], width + bldg_center[1], bldg_center[2]+height],
              [bldg_center[0], bldg_center[1], bldg_center[2]+height]]
    composite_surface = _add_surface(composite_surface, coords)
    composite_surface.surfaceMember[-1].Surface.id = (gml_bldg.name[0].value()+
                                                      "_c")

    boundary_surface.append(bldg.BoundarySurfacePropertyType())
    boundary_surface[-1].BoundarySurface = bldg.WallSurface()

    boundary_surface[-1].BoundarySurface = _add_gml_boundary(
                            boundary_surface[-1].BoundarySurface,
                            gml_bldg.name[0].value()+"_c")
    # Side d surface
    coords = [[length + bldg_center[0], bldg_center[1], bldg_center[2]],
              [length + bldg_center[0], width + bldg_center[1],
                                                               bldg_center[2]],
              [length + bldg_center[0], width + bldg_center[1],
                                                        bldg_center[2]+height],
              [length + bldg_center[0], bldg_center[1], bldg_center[2]+height]]
    composite_surface = _add_surface(composite_surface, coords)
    composite_surface.surfaceMember[-1].Surface.id = (gml_bldg.name[0].value()+
                                                      "_d")

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
        
    linear_ring.posList = pos_list
    exterior_polygon.LinearRing = linear_ring
    polygon.exterior = exterior_polygon

    composite_surface.surfaceMember[-1].Surface = polygon

    return composite_surface

def _add_gml_boundary(boundary_surface, gml_id):
    """Adds a surface to the  LOD representation of the building

    Parameters
    ----------

    boundary_surface : bldg.BoundarySurfacePropertyType() object
        A boundary surface object (Roof, Wall, Floor) for one side of the bldg
    gml_id : str
        gmlID of the corresponding gml.Solid to reference the Surface

    Returns
    -------

    boundary_surface : gml.BoundarySurfacePropertyType() object
        Returns the modified boundary surface object

    """
    boundary_surface.id = "b_"+gml_id
    boundary_surface.lod2MultiSurface = gml.MultiSurfacePropertyType()
    boundary_surface.lod2MultiSurface.MultiSurface = gml.MultiSurfaceType()
    boundary_surface.lod2MultiSurface.MultiSurface.surfaceMember.append(
                                                    gml.SurfacePropertyType())
    boundary_surface.lod2MultiSurface.MultiSurface.surfaceMember[-1].href = gml_id

    boundary_surface.opening.append(bldg.OpeningPropertyType())
    boundary_surface.opening[-1].Opening = bldg.Window()
    boundary_surface.opening[-1].Opening.id = gml_id+"_win"

    return boundary_surface

def set_gml_thermal_zone(thermal_zone):
    """creates a citygml.energy instance of a thermal zone

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

def set_gml_thermal_boundary(gml_zone, wall):
    """Control function to add a thermal boundary surface to the thermal zone

    The thermal zone instance of citygml is modidified and thermal boundary
    surfaces are added. The thermal boundaries are chosen according to their
    type (OuterWall, InnerWall, Roof, etc.). For outer walls (including roof)
    the thermal boundary is returnd to add windows.

    Parameters
    ----------

    gml_zone : energy.thermalZones() object
        A thermalZone object, where energy is a reference to
        `pyxb.bundles.opengis.citygml.energy`.

    wall : TEASER isntance of Wall()
        Teaser instance of Wall of its inherited classes

    Returns
    ----------

    _current_tb : energy.ThermalBoundarySurface()
        A ThermalBoundarySurface object with semantic information
        (material etc.)

    """
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

        set_gml_surface_component(_current_tb,
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

        set_gml_surface_component(_current_tb,
                                  wall,
                                  sun_exp="true",
                                  grnd_coupled="true")

        return _current_tb

    elif type(wall).__name__ == "GroundFloor":

        gml_zone.ThermalZone.boundedBy_.append(
                            energy.ThermalBoundarySurfacePropertyType())
        gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface =\
                            energy.ThermalBoundarySurfaceType()

        _current_tb = gml_zone.ThermalZone.boundedBy_[-1].ThermalBoundarySurface
        _current_tb.type = 'BasementFloor'

        _current_tb.inclination = gml.AngleType(wall.tilt)
        _current_tb.inclination.uom = bd.datatypes.anyURI('deg')

        set_gml_surface_component(_current_tb,
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

        set_gml_surface_component(_current_tb,
                                  wall,
                                  sun_exp="false",
                                  grnd_coupled="false")

def set_gml_surface_component(thermal_boundary, element, sun_exp, grnd_coupled):
    """Adds a surface component to a citygml thermal_boundary

    A surface component is needed to store semantic information. This function
    adds a surface component to the layer. It does not return the surface.

    Parameters
    ----------

    thermal_boundary : energy.ThermalBoundarySurface()
        A ThermalBoundarySurface object
    element : TEASER BuildingElement
        Instance of BuilingElement or inherited classes
    sun_exp : str
        "true" if the surface is exposed to sun, else "false"
    grnd_coupled : str
        "true" if the surface is coupled to ground, else "false"

    """
    thermal_boundary.composedOf.append(energy.SurfaceComponentPropertyType())

    gml_surf_comp = energy.SurfaceComponent()
    gml_surf_comp.area = gml.AreaType(element.area)
    gml_surf_comp.area.uom = bd.datatypes.anyURI('m^2')
    gml_surf_comp.isSunExposed = bd.datatypes.boolean(sun_exp)
    gml_surf_comp.isGroundCoupled = bd.datatypes.boolean(grnd_coupled)

    _add_gml_layer(gml_surf_comp, element)

    thermal_boundary.composedOf[-1].SurfaceComponent = gml_surf_comp

def _add_gml_layer(gml_surf_comp, element):
    """Adds gml layer to a surface compomenent

    Adds all layer of the element to the gml surface component

    Parameters
    ----------

    gml_surf_comp : energy.SurfaceComponent()
        A SurfaceComponent object with basic data
    element : TEASER BuildingElement
        Instance of BuilingElement or inherited classes
    """
    construction = energy.construction()
    construction.Construction = energy.ConstructionType()
    construction.Construction.name = [og.gml.CodeType(element.name)]
    if type(element).__name__ == "Window":

        construction.Construction.transmittance.append(
                                        energy.TransmittancePropertyType())

        construction.Construction.transmittance[-1].Transmittance = \
                                        energy.Transmittance()
        _g_vlaue =  construction.Construction.transmittance[-1].Transmittance
        _g_vlaue.percentage = element.g_value
        _g_vlaue.wavelengthRange = energy.WavelengthRangeTypeType("Solar")

    for lay_count in element.layer:
        layer = energy.LayerPropertyType()
        layer.Layer = energy.LayerType()
        layer.Layer.layerComponent.append(energy.LayerComponentPropertyType())
        layer.Layer.layerComponent[-1].LayerComponent = \
                                          energy.LayerComponentType()

        _current_layer =  layer.Layer.layerComponent[-1].LayerComponent

        _current_layer.thickness = gml.LengthType(lay_count.thickness)
        _current_layer.thickness.uom = bd.datatypes.anyURI('m')


        if type(element).__name__ != "Window":

            _add_gml_opaque_material(_current_layer, lay_count)

            construction.Construction.layer.append(layer)

        else:

            gml_glazing_material(_current_layer, lay_count)

            construction.Construction.layer.append(layer)

    gml_surf_comp.GenericApplicationPropertyOfCityObject.append(construction)

def _add_gml_opaque_material(gml_layer, teaser_layer):
    """Adds gml opaque material to the given layer

    Adds a material to given layer and fills information with teaser
    information

    Parameters
    ----------

    gml_surf_comp : energy.LayerComponentType()
        A Layer object with basic data
    element : TEASER Layer
        Instance of Layer
    """
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
    """Adds gml glazing material to the given layer

    Adds a material to given layer and fills information with teaser

    Currently the EnergyADE is not able to store information like thermal
    conductivity for Glazing, this will change in the next release. As a
    shortcut we implement a OpaqueMaterial for now.

    Parameters
    ----------

    gml_surf_comp : energy.LayerComponentType()
        A Layer object with basic data
    element : TEASER Layer
        Instance of Layer
    """
    gml_layer.material = energy.AbstractMaterialPropertyType()
    gml_layer.material.AbstractMaterial = energy.OpaqueMaterial()

    _current_material = gml_layer.material.AbstractMaterial
    _current_material.name = [og.gml.CodeType(teaser_layer.material.name)]
    _current_material.conductivity = gml.MeasureType(
                                        teaser_layer.material.thermal_conduc)
    _current_material.conductivity.uom = bd.datatypes.anyURI('W/mK')
