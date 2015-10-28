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


def set_lod_1(gml_bldg, coords, height=6.51769):
    """Adds a LOD 1 representation of the building based on 4 coordinates

    Parameters
    ----------

    gml_bldg : bldg.Building() object
        A building object, where bldg is a reference to
        `pyxb.bundles.opengis.citygml.building`.
    coords : list
        A list that contains the coordinates of the 4 points defining the
        ground area of the building. Each of the 4 list elements should consist
        of a list with 3 ints or floats for the x, y, and z coordinates of one
        point.

    Returns
    -------

    gml_bldg : bldg.Building() object
        Returns the modified building object

    """
    assert len(coords) == 4, 'coords must contain 4 elements'
    for coord in coords:
        assert len(coord) == 3, 'Each coord list should contain 3 elements'

    lod_1_solid = gml.SolidPropertyType()

    lod_1_solid.arcrole = 'Test'
    lod_1_solid.Solid = gml.Solid_()
    exterior_solid = gml.SurfacePropertyType()
    composite_surface = gml.CompositeSurface()

    # Ground surface
    composite_surface = _add_surface(composite_surface, coords)

    # Roof surface
    new_coords = copy.deepcopy(coords)
    for coord in new_coords:
        coord[2] += height
    roof_coords = [new_coords[0], new_coords[3], new_coords[2], new_coords[1]]
    composite_surface = _add_surface(composite_surface, roof_coords)

    # Side a surface
    new_coords = copy.deepcopy(coords)
    side_a_coords = []
    side_a_coords.append(new_coords[0])
    next = copy.deepcopy(new_coords[0])
    next[2] += height
    side_a_coords.append(next)
    next = copy.deepcopy(new_coords[1])
    next[2] += height
    side_a_coords.append(next)
    side_a_coords.append(new_coords[1])
    composite_surface = _add_surface(composite_surface, side_a_coords)

    # Side b surface
    new_coords = copy.deepcopy(coords)
    side_b_coords = []
    side_b_coords.append(new_coords[1])
    next = copy.deepcopy(new_coords[1])
    next[2] += height
    side_b_coords.append(next)
    next = copy.deepcopy(new_coords[2])
    next[2] += height
    side_b_coords.append(next)
    side_b_coords.append(new_coords[2])
    composite_surface = _add_surface(composite_surface, side_b_coords)

    # Side c surface
    new_coords = copy.deepcopy(coords)
    side_c_coords = []
    side_c_coords.append(new_coords[2])
    next = copy.deepcopy(new_coords[2])
    next[2] += height
    side_c_coords.append(next)
    next = copy.deepcopy(new_coords[3])
    next[2] += height
    side_c_coords.append(next)
    side_c_coords.append(new_coords[3])
    composite_surface = _add_surface(composite_surface, side_c_coords)

    # Side d surface
    new_coords = copy.deepcopy(coords)
    side_d_coords = []
    side_d_coords.append(new_coords[3])
    next = copy.deepcopy(new_coords[3])
    next[2] += height
    side_d_coords.append(next)
    next = copy.deepcopy(new_coords[0])
    next[2] += height
    side_d_coords.append(next)
    side_d_coords.append(new_coords[0])
    composite_surface = _add_surface(composite_surface, side_d_coords)

    exterior_solid.Surface = composite_surface
    lod_1_solid.Solid.exterior = exterior_solid

    gml_bldg.lod1Solid = lod_1_solid

    return gml_bldg


def _add_surface(composite_surface, coords):
    """Adds a surface to the  LOD 1 representation of the building 

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
    pos_list.srsDimension = 3

    linear_ring.posList = pos_list
    exterior_polygon.LinearRing = linear_ring
    polygon.exterior = exterior_polygon
    composite_surface.surfaceMember[-1].Surface = polygon

    return composite_surface

#     def setLOD2Composite(self):
#         '''
#         sets a LOD2 CompositeSurface
#         arguments:
#         ----------
#
#         '''
#         lod2Composite = gml.SolidPropertyType()
#         lod2Composite.Solid = gml.Solid_()
#         lod2Composite.Solid.exterior = gml.SurfacePropertyType()
#         lod2Composite.Solid.exterior.Surface = gml.CompositeSurface()
#
#         return lod2Composite
#
#     def setLOD2Surface(self, lod2Composite, gmlID, posList, nrOfWall):
#         '''
#         sets a LOD2 Composite Surface Member
#         arguments:
#         ----------
#         lod2Composite : from def setLOD2Composite
#         gmlID: gmlID of Surface
#         posList: coordinates of surface in gml coordinates
#         nrOfWall: counter of the number of wall of the building
#         '''
#
#         lod2Composite.Solid.exterior.Surface.surfaceMember.append(
#             gml.SurfacePropertyType())
#         lod2Composite.Solid.exterior.Surface.surfaceMember[
#             nrOfWall].Surface = gml.Polygon()
#         lod2Composite.Solid.exterior.Surface.surfaceMember[
#             nrOfWall].Surface.id = gmlID
#         ring = gml.LinearRing()
#         ring.posList = (gml.DirectPositionListType(posList))
#         lod2Composite.Solid.exterior.Surface.surfaceMember[
#             nrOfWall].Surface.exterior = gml.AbstractRingPropertyType(ring)
#
#         lod2Solid = lod2Composite
#         return lod2Solid
#
#     def setGMLBoundary(self, boundedBy_, wallType, gmlID, href, nrOfWall):
#         '''
#         sets the gml boundary surfaces
#         arguments:
#         ----------
#         boundedBy_: list of the walls that are bounding the building for gml (first call empty)
#         wallType: wall Type defined in gml (OuterWall, FlatRoof, BasementFloor)
#         gmlID --- unique gmlID for surface
#         href --- connection to LOD2Surface
#         nrOfWall: counter of the number of wall of the building
#         '''
#
#         boundedBy_.append(bldg.BoundarySurfacePropertyType())
#         if wallType == "OuterWall":
#             boundedBy_[nrOfWall].BoundarySurface = bldg.WallSurface()
#
#             boundedBy_[nrOfWall].BoundarySurface.id = gmlID
#             boundedBy_[
#                 nrOfWall].BoundarySurface.lod2MultiSurface = gml.MultiSurfacePropertyType()
#             boundedBy_[
#                 nrOfWall].BoundarySurface.lod2MultiSurface.MultiSurface = gml.MultiSurfaceType()
#             boundedBy_[nrOfWall].BoundarySurface.lod2MultiSurface.MultiSurface.surfaceMember.append(
#                 gml.SurfacePropertyType())
#             boundedBy_[nrOfWall].BoundarySurface.lod2MultiSurface.MultiSurface.surfaceMember[
#                 0].href = href
#
#             boundedBy_[nrOfWall].BoundarySurface.opening.append(
#                 bldg.OpeningPropertyType())
#             boundedBy_[nrOfWall].BoundarySurface.opening[
#                 0].Opening = bldg.Window()
#             boundedBy_[nrOfWall].BoundarySurface.opening[
#                 0].Opening.id = gmlID + "_win"
#
#         elif wallType == "FlatRoof":
#             boundedBy_[nrOfWall].BoundarySurface = bldg.RoofSurface()
#             boundedBy_[nrOfWall].BoundarySurface.id = gmlID
#             boundedBy_[
#                 nrOfWall].BoundarySurface.lod2MultiSurface = gml.MultiSurfacePropertyType()
#             boundedBy_[
#                 nrOfWall].BoundarySurface.lod2MultiSurface.MultiSurface = gml.MultiSurfaceType()
#             boundedBy_[nrOfWall].BoundarySurface.lod2MultiSurface.MultiSurface.surfaceMember.append(
#                 gml.SurfacePropertyType())
#             boundedBy_[nrOfWall].BoundarySurface.lod2MultiSurface.MultiSurface.surfaceMember[
#                 0].href = href
#         elif wallType == "BasementFloor":
#             boundedBy_[nrOfWall].BoundarySurface = bldg.FloorSurface()
#             boundedBy_[nrOfWall].BoundarySurface.id = gmlID
#             boundedBy_[
#                 nrOfWall].BoundarySurface.lod2MultiSurface = gml.MultiSurfacePropertyType()
#             boundedBy_[
#                 nrOfWall].BoundarySurface.lod2MultiSurface.MultiSurface = gml.MultiSurfaceType()
#             boundedBy_[nrOfWall].BoundarySurface.lod2MultiSurface.MultiSurface.surfaceMember.append(
#                 gml.SurfacePropertyType())
#             boundedBy_[nrOfWall].BoundarySurface.lod2MultiSurface.MultiSurface.surfaceMember[
#                 0].href = href
#
#         return boundedBy_
#
#     def setEnergyBoundary(self, boundedBy_en, wallType, href, area, areaWin, nrOfWall):
#         '''
#         sets the energy boundary surfaces
#         arguments:
#         ----------
#         boundedBy_en: list of the walls that are bounding the building for energy (first call empty)
#         wallType: wall Type defined in gml (OuterWall, FlatRoof, BasementFloor)
#         href: connection to boundary of gml
#         area: area of wall surface
#         areaWin: area of window surface
#         nrOfWall: counter of the number of wall of the building
#         '''
#         boundedBy_en.append(energy.ThermalBoundarySurfacePropertyType())
#         boundedBy_en[
#             nrOfWall].ThermalBoundarySurface = energy.ThermalBoundarySurfaceType()
#         boundedBy_en[nrOfWall].ThermalBoundarySurface.type = wallType
#         boundedBy_en[nrOfWall].ThermalBoundarySurface.composedOf.append(
#             energy.SurfaceComponentPropertyType())
#
#         wall = self.setSurfaceComponent(area, href, wallType)
#
#         boundedBy_en[nrOfWall].ThermalBoundarySurface.composedOf[
#             0].SurfaceComponent = wall
#
#         boundedBy_en[nrOfWall].ThermalBoundarySurface.composedOf.append(
#             energy.SurfaceComponentPropertyType())
#         if wallType == "OuterWall":
#             window = self.setSurfaceComponent(areaWin, href, "Window")
#             boundedBy_en[nrOfWall].ThermalBoundarySurface.composedOf[
#                 1].SurfaceComponent = window
#         else:
#             pass
#         return boundedBy_en
#
#     def setSurfaceComponent(self, area, href, wallType):
#         '''
#         sets the energy boundary surface component according to type
#         arguments:
#         ----------
#         area -- area of surface component
#         href -- reference to boundary of gml
#         wallType -- wall type defined in gml
#         '''
#         surfaceComponent = energy.SurfaceComponent()
#         surfaceComponent.area = gml.AreaType(area)
#         surfaceComponent.area.uom = bd.datatypes.anyURI('m^2')
#         surfaceComponent.relates = gml.ReferenceType()
#
#         if wallType == "OuterWall":
#             surfaceComponent.relates.href = href
#             surfaceComponent.isSunExposed = bd.datatypes.boolean("true")
#             surfaceComponent.isGroundCoupled = bd.datatypes.boolean("true")
#         elif wallType == "FlatRoof":
#             surfaceComponent.relates.href = href
#             surfaceComponent.isSunExposed = bd.datatypes.boolean("true")
#             surfaceComponent.isGroundCoupled = bd.datatypes.boolean("false")
#         elif wallType == "BasementFloor":
#             surfaceComponent.relates.href = href
#             surfaceComponent.isSunExposed = bd.datatypes.boolean("true")
#             surfaceComponent.isGroundCoupled = bd.datatypes.boolean("true")
#         elif wallType == "Window":
#             surfaceComponent.relates.href = href + "_win"
#             surfaceComponent.isSunExposed = bd.datatypes.boolean("true")
#             surfaceComponent.isGroundCoupled = bd.datatypes.boolean("true")
#
#         return surfaceComponent
#
#     def setMaterialProperties(self, outerWall, nrOfWall, wallType=0):
#         '''
#         sets the material properties of a energy wall
#         arguments:
#         ----------
#         outerWall -- outerWall object of building in Teaser
#         nrOfWall -- wall counter of gml
#         wallType -- wall type defined in gml
#         '''
#         construction = energy.construction()
#         construction.Construction = energy.ConstructionType()
#         construction.Construction.id = outerWall.id
#
#         if not wallType == "BasementFloor":
#             absorp = energy.AbsorptancePropertyType()
#             absorp.Absorptance = energy.Absorptance()
#             absorp.Absorptance.percentage = outerWall.layer[
#                 0].material.solarAbsorp
#             absorp.Absorptance.surface = "Outside"
#             absorp.Absorptance.wavelengthRange = "Solar"
#             construction.Construction.absorptance.append(absorp)
#
#         layer = energy.LayerPropertyType()
#         layer.Layer = energy.LayerType()
#         layer.Layer.layerComponent.append(energy.LayerComponentPropertyType())
#         layer.Layer.layerComponent.append(energy.LayerComponentPropertyType())
#         layer.Layer.layerComponent.append(energy.LayerComponentPropertyType())
#
#         i = 0
#         for lay in outerWall.layer:
#
#             component = energy.LayerComponentType()
#
#             thickness = gml.LengthType(lay.thickness)
#             thickness.uom = bd.datatypes.anyURI('m')
#
#             component.thickness = thickness
#
#             component.material = energy.AbstractMaterialPropertyType()
#             component.material.AbstractMaterial = energy.OpaqueMaterial()
#
#             conductivity = gml.MeasureType(lay.material.thermalConduc)
#             conductivity.uom = bd.datatypes.anyURI('W/mK')
#
#             density = gml.MeasureType(lay.material.density)
#             density.uom = bd.datatypes.anyURI('kg/m^3')
#
#             specificHeat = gml.MeasureType(lay.material.heatCapac)
#             specificHeat.uom = bd.datatypes.anyURI('kJ/kg')
#
#             component.material.AbstractMaterial.conductivity = conductivity
#             component.material.AbstractMaterial.density = density
#             component.material.AbstractMaterial.specificHeat = specificHeat
#
#             layer.Layer.layerComponent[i].LayerComponent = component
#
#             i += 1
#         construction.Construction.layer.append(layer)
#         return construction
#
#     def setMaterialPropertiesWin(self, win, nrOfWall):
#         '''
#         sets the material properties of a energy window
#         arguments:
#         ----------
#         win -- window object of building in Teaser
#         nrOfWall -- wall counter in gml
#         '''
#         construction = energy.construction()
#         construction.Construction = energy.ConstructionType()
#         construction.Construction.id = win.id
#
#         layer = energy.LayerPropertyType()
#         layer.Layer = energy.LayerType()
#         layer.Layer.layerComponent.append(energy.LayerComponentPropertyType())
#
#         i = 0
#         for lay in win.layer:
#
#             component = energy.LayerComponentType()
#
#             thickness = gml.LengthType(lay.thickness)
#             thickness.uom = bd.datatypes.anyURI('m')
#
#             component.thickness = thickness
#
#             component.material = energy.AbstractMaterialPropertyType()
#             component.material.AbstractMaterial = energy.Glazing()
#
#             transmittance = energy.TransmittancePropertyType()
#             transmittance.Transmittance = energy.Transmittance()
#             transmittance.Transmittance.percentage = 0.8
#             transmittance.Transmittance.wavelengthRange = energy.WavelengthRangeTypeType(
#                 'Solar')
#
# component.material.AbstractMaterial.normalIncidenceTransmittance = [energy.Transmittance()]
#             component.material.AbstractMaterial.normalIncidenceTransmittance = transmittance
#
#             layer.Layer.layerComponent[i].LayerComponent = component
#
#             i += 1
#         construction.Construction.layer.append(layer)
#         return construction
#
#     def setPosList(self, nrOfWall, nrOfBuild):
#         '''
#         to do
#         '''
#         multi = nrOfBuild * 15
#
#         if nrOfWall == 0:
#             posList = [0.0 + multi, 0.0, 0.0, 10.0 + multi, 0.0, 0.0, 10.0 +
#                        multi, 0.0, 3.0, 0.0 + multi, 0.0, 3.0, 0.0 + multi, 0.0, 0.0]
#         elif nrOfWall == 1:
#             posList = [0.0 + multi, 20.0, 0.0, 10.0 + multi, 20.0, 0.0, 10.0 +
#                        multi, 20.0, 3.0, 0.0 + multi, 20.0, 3.0, 0.0 + multi, 20.0, 0.0]
#         elif nrOfWall == 2:
#             posList = [0.0 + multi, 0.0, 3.0, 10.0 + multi, 0.0, 3.0, 10.0 +
#                        multi, 20.0, 3.0, 0.0 + multi, 20.0, 3.0, 0.0 + multi, 0.0, 3.0]
#         elif nrOfWall == 3:
#             posList = [10.0 + multi, 0.0, 0.0, 10.0 + multi, 20.0, 0.0, 10.0 +
#                        multi, 20.0, 3.0, 10.0 + multi, 0.0, 3.0, 10.0 + multi, 0.0, 0.0]
#         elif nrOfWall == 4:
#             posList = [0.0 + multi, 0.0, 0.0, 10.0 + multi, 0.0, 0.0, 10.0 +
#                        multi, 20.0, 0.0, 0.0 + multi, 20.0, 0.0, 0.0 + multi, 0.0, 0.0]
#         elif nrOfWall == 5:
#             posList = [0.0 + multi, 0.0, 0.0, 0.0 + multi, 20.0, 0.0, 0.0 +
#                        multi, 20.0, 3.0, 0.0 + multi, 0.0, 3.0, 0.0 + multi, 0.0, 0.0]
#         elif nrOfWall == 6:
#             posList = [0.0 + multi, 20.0, 0.0, 10.0 + multi, 20.0, 0.0, 10.0 +
#                        multi, 20.0, 3.0, 0.0 + multi, 20.0, 3.0, 0.0 + multi, 20.0, 0.0]
#
#         return posList
