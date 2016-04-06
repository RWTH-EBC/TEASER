# Created April 2016
# TEASER Development Team

"""CityGML

This module contains function to load Buildings in the non proprietary
CityGML file format .gml
"""
import pyxb
import pyxb.binding as bd
import pyxb.utils
import pyxb.namespace
import pyxb.bundles
import teaser.Data.SchemaBindings.opengis
import pyxb.bundles.common.raw.xlink as xlink
import numpy as np
from numpy import linalg as LA
import teaser.Data.SchemaBindings.opengis.raw as og
import teaser.Data.SchemaBindings.opengis.raw.gml as gml
import teaser.Data.SchemaBindings.opengis.citygml.raw.base as citygml
import teaser.Data.SchemaBindings.opengis.citygml.raw.building as bldg
import teaser.Data.SchemaBindings.opengis.citygml.raw.energy as energy
import teaser.Data.SchemaBindings.opengis.citygml.raw.generics as generics
from teaser.Logic.BuildingObjects.Building import Building

def load_gml(path, prj):
    '''This function loads a project from CityGML file

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
        #for LOD2 we check if boundary surfaces are described
        if city_object.Feature.boundedBy_:
            bldg = Building(parent=prj)
            for bound_surf in city_object.Feature.boundedBy_:
                for comp_member in  bound_surf.BoundarySurface.lod2MultiSurface.MultiSurface.surfaceMember:
                    try: #modelling option 1
                        _identify_area(bldg,comp_member.Surface.exterior.Ring.posList.value())
                    except: #modelling option 2
                        for pos_list in comp_member.Surface.surfaceMember:
                            _identify_area(bldg, pos_list.Surface.exterior.Ring.posList.value())



def _identify_area(teaser_bldg, pos_list):

    print(_get_gml_tilt(pos_list=pos_list))


def _get_gml_tilt(pos_list):
    '''calc the tilt of a gml_surface defined by 4 or 5 gml coordinates

    Surface needs to be planar

    Parameters
    ----------
    pos_list : [float]
        list of gml coordinates that describe a planar surface

    Returns
    ----------
    surface_tilt : float
        returns the orientation of the surface
    '''

    gml_surface = np.array(pos_list)
    gml1 = gml_surface[0:3]
    gml2 = gml_surface[3:6]
    gml3 = gml_surface[6:9]
    vector_1 = gml2-gml1
    vector_2 = gml3-gml1

    normal_1 = np.cross(vector_1, vector_2)
    z_axis = np.array([0,0,1])

    surface_tilt = np.arccos(np.dot(normal_1, z_axis)/(LA.norm(z_axis)*LA.norm(normal_1)))*360/(2*np.pi)

    if surface_tilt == 180:
        surface_tilt = 0.0

    return surface_tilt