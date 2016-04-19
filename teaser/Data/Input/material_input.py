'''
Created April 2016

@author: TEASER Development Team
'''

"""material_input.py

This module contains function to load material classes
"""

def load_material(material, mat_name):
    '''Material loader.

    Loads Material specified in the XML.

    Parameters
    ----------
    material : Material()
        instance of TEASERS Material class

    mat_name : str
        Code list for Material

    '''
    ass_error_1 = "You need to specify parents up to project"

    assert material.parent.parent.parent.parent.parent is not None, ass_error_1

    for mat in material.parent.parent.parent.parent.parent.\
            data.material_bind.Material:

        if mat.name == mat_name:

            material.name = mat.name
            material.density = mat.density
            material.thermal_conduc = float(mat.thermal_conduc)
            material.heat_capac = mat.heat_capac