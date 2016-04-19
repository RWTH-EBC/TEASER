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
import teaser.Data.SchemaBindings.opengis
import teaser.Data.SchemaBindings.opengis.citygml.raw.base as citygml
import teaser.Data.SchemaBindings.opengis.citygml.raw.energy as energy
import teaser.Data.SchemaBindings.opengis.citygml.raw.building as bldg
import teaser.Data.SchemaBindings.opengis.citygml.raw.generics as gen
import teaser.Data.SchemaBindings.opengis.raw.gml as gml
import teaser.Data.SchemaBindings.opengis.raw._nsgroup as nsgroup
import teaser.Data.SchemaBindings.opengis.raw.smil20 as smil
import teaser.Data.SchemaBindings.opengis.misc.raw.xAL as xal

from teaser.Logic.BuildingObjects.Building import Building


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
                bldg = Building(parent=prj)
                _create_building_part(bldg=bldg, part=part)
                if part.function:
                    bldg.convert_bldg(part.function[0].value())
                    bldg.set_height_gml()



        else:
            bldg = Building(parent=prj)
            _create_building(bldg=bldg, city_object=city_object)
            if city_object.Feature.function:
                bldg.convert_bldg(city_object.Feature.function[0].value())
                bldg.set_height_gml()



def _create_building(bldg, city_object):
    #LOD2
    if city_object.Feature.boundedBy_:
        for bound_surf in city_object.Feature.boundedBy_:
            for comp_member in bound_surf.BoundarySurface.lod2MultiSurface.MultiSurface.surfaceMember:
                try: #modelling option 1
                    bldg.gml_surfaces.append(Surface_gml(
                        comp_member.Surface.exterior.Ring.posList.value()))
                except: #modelling option 2
                    for pos_list in comp_member.Surface.surfaceMember:
                        bldg.gml_surfaces.append(Surface_gml(
                            pos_list.Surface.exterior.Ring.posList.value()))
    #if a building Feature has no boundedBy_ but a lod1solid it is LOD1
    elif city_object.Feature.lod1Solid:
        for member in city_object.Feature.lod1Solid.Solid.exterior\
                .Surface.surfaceMember:
            bldg.gml_surfaces.append(Surface_gml(
                member.Surface.exterior.Ring.posList.value()))

def _create_building_part(bldg, part):
    if part.BuildingPart.boundedBy_:
        for bound_surf in part.BuildingPart.boundedBy_:
            for comp_member in bound_surf.BoundarySurface.lod2MultiSurface.MultiSurface.surfaceMember:
                try: #modelling option 1
                    bldg.gml_surfaces.append(Surface_gml(
                        comp_member.Surface.exterior.Ring.posList.value()))
                except: #modelling option 2
                    for pos_list in comp_member.Surface.surfaceMember:
                        bldg.gml_surfaces.append(Surface_gml(
                            pos_list.Surface.exterior.Ring.posList.value()))
    #if a building Feature has no boundedBy_ but a lod1solid it is LOD1
    elif part.BuildingPart.lod1Solid:
        for member in part.BuildingPart.lod1Solid.Solid.exterior\
                .Surface.surfaceMember:
            bldg.gml_surfaces.append(Surface_gml(
                member.Surface.exterior.Ring.posList.value()))



class Surface_gml(object):

    def __init__(self, gml_surface, boundary = None):
        self.gml_surface = gml_surface
        self.surface_area = None
        self.surface_orientation = None
        self.surface_tilt = None
        self.name = boundary

        self.surface_area = self.get_gml_area()
        self.surface_orientation = self.get_gml_orientation()
        self.surface_tilt = self.get_gml_tilt()


    def get_gml_area(self):
        '''calc the area of a gml_surface defined by 4 or 5 gml coordinates

        Surface needs to be planar

        Parameters
        ----------
        gml_surface : [float]
            list of gml coordinates that describe a planar surface

        Returns
        ----------
        surface_area : float
            returns the area of the surface
        '''
        gml_surface = np.array(self.gml_surface)

        gml1 = gml_surface[0:3]
        gml2 = gml_surface[3:6]
        gml3 = gml_surface[6:9]
        gml4 = gml_surface[9:12]

        vektor_1 = gml2-gml1
        vektor_2 = gml3-gml1
        normal_1 = np.cross(vektor_1, vektor_2)

        self.surface_area = LA.norm(normal_1)

        if len(gml_surface) > 15:
            vektor_3 = gml4-gml3
            normal_2 = np.cross(vektor_1, vektor_3)
            self.surface_area = 0.5*LA.norm(normal_2) + self.surface_area

        return self.surface_area

    def get_gml_tilt(self):
        '''calc the tilt of a gml_surface defined by 4 or 5 gml coordinates

        Surface needs to be planar

        Parameters
        ----------
        gml_surface : [float]
            list of gml coordinates that describe a planar surface

        Returns
        ----------
        surface_tilt : float
            returns the orientation of the surface
        '''

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

        return self.surface_tilt

    def get_gml_orientation(self):
        '''calc the orienation of a gml_surface defined by 4 or 5 gml
        coordinates

        Surface needs to be planar, the orientation returned is in TEASER
        coordinates

        Parameters
        ----------
        gml_surface : [float]
            list of gml coordinates that describe a planar surface

        Returns
        ----------
        surface_orientation : float
            returns the orientation of the surface
        '''

        gml_surface = np.array(self.gml_surface)
        gml1 = gml_surface[0:3]
        gml2 = gml_surface[3:6]
        gml3 = gml_surface[6:9]
        gml4 = gml_surface[9:12]

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
