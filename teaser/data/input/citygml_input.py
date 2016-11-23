# Created April 2016
# TEASER Development Team

"""CityGML

This module contains function to load Buildings in the non proprietary
CityGML file format .gml
"""
import numpy as np
from numpy import linalg as LA
import pyxb
import pyxb.utils
import pyxb.namespace
import pyxb.bundles
import pyxb.bundles.common.raw.xlink as xlink
import teaser.data.bindings.opengis
import teaser.data.bindings.opengis.citygml.raw.base as citygml
import teaser.data.bindings.opengis.citygml.raw.energy as energy
import teaser.data.bindings.opengis.citygml.raw.building as bldg
import teaser.data.bindings.opengis.citygml.raw.generics as gen
import teaser.data.bindings.opengis.raw.gml as gml
import teaser.data.bindings.opengis.raw._nsgroup as nsgroup
import teaser.data.bindings.opengis.raw.smil20 as smil
import teaser.data.bindings.opengis.misc.raw.xAL as xal

from teaser.logic.archetypebuildings.bmvbs.singlefamilydwelling \
                            import SingleFamilyDwelling
from teaser.logic.archetypebuildings.bmvbs.office import Office
from teaser.logic.buildingobjects.building import Building


def load_gml(path, prj):
    '''This function loads buildings from a CityGML file

    Parameters
    ----------
    path: string
        path of CityGML file

    prj: Project()
        Teaser instance of Project()
    '''
    xml_file = open(path, 'r')
    gml_bind = citygml.CreateFromDocument(xml_file.read())

    for i, city_object in enumerate(gml_bind.featureMember):
        if city_object.Feature.consistsOfBuildingPart:
            for part in city_object.Feature.consistsOfBuildingPart:
                if part.BuildingPart.function:
                    if part.BuildingPart.function[0].value() == "1000":
                        bldg = SingleFamilyDwelling(parent=prj,
                                                    name=part.BuildingPart.id)
                    elif part.BuildingPart.function[0].value() == "1120":
                        bldg = Office(parent=prj,
                                      name=part.BuildingPart.id)
                    else:
                        bldg = Building(parent=prj,
                                        name=part.BuildingPart.id)

                else:
                    bldg = Building(parent=prj,
                                    name=part.BuildingPart.id)
                _create_building_part(bldg=bldg, part=part)
                _set_attributes(bldg=bldg, gml_bldg=part.BuildingPart)
                bldg.set_height_gml()
        else:

            if city_object.Feature.function:
                if city_object.Feature.function[0].value() == "1000":
                    bldg = SingleFamilyDwelling(parent=prj,
                                                name=city_object.Feature.id)

                elif city_object.Feature.function[0].value() == "1120":
                    bldg = Office(parent=prj,
                                    name=city_object.Feature.id)
                else:
                    bldg = Building(parent=prj,
                                    name=city_object.Feature.id)
            else:

                bldg = Building(parent=prj,
                                name=city_object.Feature.id)

            _create_building(bldg=bldg, city_object=city_object)
            _set_attributes(bldg=bldg, gml_bldg=city_object.Feature)
            bldg.set_height_gml()
            try:
                bldg.set_gml_attributes()
            except:
                pass
            try:
                bldg.generate_from_gml()
            except:
                pass


def _set_attributes(bldg, gml_bldg):
    """tries to set attributes for type building generation
    """
    try:
        bldg.name = gml_bldg.name[0].value()
    except:
        pass
    try:
        bldg.number_of_floors = gml_bldg.storeysAboveGround
    except:
        pass
    try:
        bldg.height_of_floors = gml_bldg.storeyHeightsAboveGround.value()[0]
    except:
        pass
    try:
        bldg.year_of_construction = gml_bldg.yearOfConstruction.year
    except:
        pass
    try:
        bldg.bldg_height = gml_bldg.measuredHeight.value()
    except:
        pass


def _create_building(bldg, city_object):
    #LOD2
    if city_object.Feature.boundedBy_:
        for bound_surf in city_object.Feature.boundedBy_:
            for comp_member in bound_surf.BoundarySurface.lod2MultiSurface.MultiSurface.surfaceMember:
                try: #modelling option 1
                    bldg.gml_surfaces.append(SurfaceGML(
                        comp_member.Surface.exterior.Ring.posList.value()))
                except: #modelling option 2
                    for pos_list in comp_member.Surface.surfaceMember:
                        bldg.gml_surfaces.append(SurfaceGML(
                            pos_list.Surface.exterior.Ring.posList.value()))
    #if a building Feature has no boundedBy_ but a lod1solid it is LOD1
    elif city_object.Feature.lod1Solid:
        for member in city_object.Feature.lod1Solid.Solid.exterior\
                .Surface.surfaceMember:
            bldg.gml_surfaces.append(SurfaceGML(
                member.Surface.exterior.Ring.posList.value()))


def _create_building_part(bldg, part):
    if part.BuildingPart.boundedBy_:
        for bound_surf in part.BuildingPart.boundedBy_:
            for comp_member in bound_surf.BoundarySurface.lod2MultiSurface.MultiSurface.surfaceMember:
                try: #modelling option 1
                    bldg.gml_surfaces.append(SurfaceGML(
                        comp_member.Surface.exterior.Ring.posList.value()))
                except: #modelling option 2
                    for pos_list in comp_member.Surface.surfaceMember:
                        bldg.gml_surfaces.append(SurfaceGML(
                            pos_list.Surface.exterior.Ring.posList.value()))
    #if a building Feature has no boundedBy_ but a lod1solid it is LOD1
    elif part.BuildingPart.lod1Solid:
        for member in part.BuildingPart.lod1Solid.Solid.exterior\
                .Surface.surfaceMember:
            bldg.gml_surfaces.append(SurfaceGML(
                member.Surface.exterior.Ring.posList.value()))

def _convert_bldg(bldg, function):
    """converts the instance to a specific archetype building

    DANGEROUS function, should only be used in combination with CityGML
    and if you know what you are doing

    Parameters
    ----------

    bldg : Building()
        TEASER instance of a building

    function : str
        function from CityGML code list 1000 is residential 1120 is office
    """
    parent_help = bldg.parent
    name_help = bldg.name
    gml_surfaces_help = bldg.gml_surfaces
    year_of_construction_help = bldg.year_of_construction
    bldg_height_help = bldg.bldg_height

    if function == "1000":
        from teaser.logic.archetypebuildings.bmvbs.singlefamilydwelling \
            import SingleFamilyDwelling
        bldg.__class__ = SingleFamilyDwelling
    elif function == "1120":
        from teaser.logic.archetypebuildings.bmvbs.office import Office
        bldg.__class__ = Office

    bldg.__init__(parent=None)
    bldg.gml_surfaces = gml_surfaces_help
    bldg.parent = parent_help
    bldg.name = name_help
    bldg.year_of_construction = year_of_construction_help
    bldg.bldg_height = bldg_height_help

    bldg.set_gml_attributes()
    bldg.generate_from_gml()

class SurfaceGML(object):
    """Class for calculating attributes of CityGML surfaces

    this class automatically calculates surface area using an algorithm for
    polygons with arbitrary number of points. The Surface orientation by
    analysing the normal vector (caution: the orientations are then set to
    TEASER orientation). The Surface tilt by analysing the normal vector.

    Parameters
    ----------

    gml_surface : list
        list of gml points with srsDimension=3 the first 3 and the last 3
        entries must describe the same point in CityGML

    boundary : str
        Name of the boundary surface

    """

    def __init__(self,
                 gml_surface,
                 boundary=None):
        self.gml_surface = gml_surface
        self.name = boundary
        self.surface_area = None
        self.surface_orientation = None
        self.surface_tilt = None

        self.surface_area = self.get_gml_area()
        self.surface_orientation = self.get_gml_orientation()
        self.surface_tilt = self.get_gml_tilt()

    def get_gml_area(self):
        """calc the area of a gml_surface defined by gml coordinates

        Surface needs to be planar

        Returns
        ----------
        surface_area : float
            returns the area of the surface
        """

        split_surface = list(zip(*[iter(self.gml_surface)]*3))
        self.surface_area = self.poly_area(poly=split_surface)

        return self.surface_area

    def get_gml_tilt(self):
        """calc the tilt of a gml_surface defined by 4 or 5 gml coordinates

        Surface needs to be planar

        Returns
        ----------
        surface_tilt : float
            returns the orientation of the surface
        """

        gml_surface = np.array(self.gml_surface)
        gml1 = gml_surface[0:3]
        gml2 = gml_surface[3:6]
        gml3 = gml_surface[6:9]
        gml4 = gml_surface[9:12]

        vektor_1 = gml2-gml1
        vektor_2 = gml3-gml1

        normal_1 = np.cross(vektor_1, vektor_2)
        z_axis = np.array([0,0,1])

        self.surface_tilt = np.arccos(np.dot(normal_1, z_axis)/(LA.norm(
            z_axis)*LA.norm(normal_1)))*360/(2*np.pi)

        if self.surface_tilt == 180:
            self.surface_tilt = 0.0
        elif str(self.surface_tilt) == "nan":
            self.surface_tilt = None
        return self.surface_tilt

    def get_gml_orientation(self):
        """calc the orientation of a gml_surface defined by 4 or 5 gml
        coordinates

        Surface needs to be planar, the orientation returned is in TEASER
        coordinates

        Returns
        ----------
        surface_orientation : float
            returns the orientation of the surface
        """

        gml_surface = np.array(self.gml_surface)
        gml1 = gml_surface[0:3]
        gml2 = gml_surface[3:6]
        gml3 = gml_surface[6:9]
        gml4 = gml_surface[9:12]
        if len(gml_surface) > 12:
            vektor_1 = gml2-gml1
            vektor_2 = gml4-gml1
        else:
            vektor_1 = gml2-gml1
            vektor_2 = gml3-gml1

        normal_1 = np.cross(vektor_1, vektor_2)
        normal_uni = normal_1/LA.norm(normal_1)
        phi = None
        if normal_uni[0] > 0:
            phi = np.arctan(normal_uni[1]/normal_uni[0])
        elif normal_uni[0] < 0 <= normal_uni[1]:
            phi = np.arctan(normal_uni[1]/normal_uni[0]) + np.pi
        elif normal_uni[0] < 0 > normal_uni[1]:
            phi = np.arctan(normal_uni[1]/normal_uni[0]) - np.pi
        elif normal_uni[0] == 0 < normal_uni[1]:
            phi = np.pi/2
        elif normal_uni[0] == 0 > normal_uni[1]:
            phi = -np.pi/2

        if phi is None:
            pass
        elif phi < 0:
            self.surface_orientation = (phi+2*np.pi)*360/(2*np.pi)
        else:
            self.surface_orientation = (phi)*360/(2*np.pi)

        if self.surface_orientation is None:
            pass
        elif 0 <= self.surface_orientation <= 90:
            self.surface_orientation = 90 - self.surface_orientation
        else:
            self.surface_orientation = 450 - self.surface_orientation

        if normal_uni[2] == -1:
            self.surface_orientation = -2
        elif normal_uni[2] == 1:
            self.surface_orientation = -1

        return self.surface_orientation

    def unit_normal(self, a, b, c):
        """calculates the unit normal vector of a surface described by 3 points

        Parameters
        ----------

        a : float
            point 1
        b : float
            point 2
        c : float
            point 3

        Returns
        ----------

        unit_normal : list
            unit normal vector as a list

        """

        x = np.linalg.det([[1,a[1],a[2]],
             [1,b[1],b[2]],
             [1,c[1],c[2]]])
        y = np.linalg.det([[a[0],1,a[2]],
             [b[0],1,b[2]],
             [c[0],1,c[2]]])
        z = np.linalg.det([[a[0],a[1],1],
             [b[0],b[1],1],
             [c[0],c[1],1]])
        magnitude = (x**2 + y**2 + z**2)**.5
        return (x/magnitude, y/magnitude, z/magnitude)

    def poly_area(self, poly):
        """calculates the area of a polygon with arbitrary points

        Parameters
        ----------

        poly : list
            polygon as a list in srsDimension = 3

        Returns
        ----------

        area : float
            returns the area of a polygon
        """

        if len(poly) < 3: # not a plane - no area
            return 0
        total = [0, 0, 0]
        length = len(poly)
        for i in range(length):
            vi1 = poly[i]
            vi2 = poly[(i+1) % length]
            prod = np.cross(vi1, vi2)
            total[0] += prod[0]
            total[1] += prod[1]
            total[2] += prod[2]
        result = np.dot(total, self.unit_normal(poly[0], poly[1], poly[2]))
        return abs(result/2)
