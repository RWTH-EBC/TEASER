#Created April 2016
#TEASER 4 Development Team

"""material_input.py

This module contains function to load material classes
"""

def load_material(material, mat_name, binding=None):
    '''Material loader.

    Loads Material specified in the XML.

    Parameters
    ----------
    material : Material()
        instance of TEASERS Material class

    mat_name : str
        Code list for Material

    binding : pyxb Material binding
        If binding is none, the Project binding will be used, otherwise you
        can use a specific XML binding for your own purpose

    '''
    if binding is None:
        ass_error_1 = "You need to specify parents up to project"

        assert material.parent.parent.parent.parent.parent is not None, ass_error_1
        binding = material.parent.parent.parent.parent.parent.data.material_bind
    else:
        pass

    for mat in binding.Material:

        if mat.name == mat_name:

            material.name = mat.name
            material.density = mat.density
            material.thermal_conduc = float(mat.thermal_conduc)
            material.heat_capac = mat.heat_capac

def load_material_id(material, mat_id, binding):
    """Material loader by id.

    Loads Material specified in the XML by given material_id.

    Parameters
    ----------
    material : Material()
        instance of TEASERS Material class

    mat_id : name
        id of material from XML

    binding : pyxb Material binding
        If binding is none, the Project binding will be used, otherwise you
        can use a specific XML binding for your own purpose
    """
    if binding is None:
        ass_error_1 = "You need to specify parents up to project"

        assert material.parent.parent.parent.parent.parent is not None, ass_error_1
        binding = material.parent.parent.parent.parent.parent.data.material_bind
    else:
        pass

    for mat in binding.Material:

        if mat.material_id == mat_id:

            material.material_id = mat.material_id
            material.name = mat.name
            material.density = mat.density
            material.thermal_conduc = float(mat.thermal_conduc)
            material.heat_capac = mat.heat_capac