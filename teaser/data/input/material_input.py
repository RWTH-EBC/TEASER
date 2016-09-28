#Created April 2016
#TEASER 4 Development Team

"""material_input.py

This module contains function to load material classes
"""


def load_material(material, mat_name, data_class):
    '''Material loader.

    Loads Material specified in the XML.

    Parameters
    ----------

    material : Material()
        instance of TEASERS Material class

    mat_name : str
        Code list for Material

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.
    '''

    binding = data_class.material_bind

    for mat in binding.Material:

        if mat.name == mat_name:

            material.material_id = mat.material_id
            material.name = mat.name
            material.density = mat.density
            material.thermal_conduc = float(mat.thermal_conduc)
            material.heat_capac = mat.heat_capac


def load_material_id(material, mat_id, data_class):
    """Material loader by id.

    Loads Material specified in the XML by given material_id.

    Parameters
    ----------

    material : Material()
        instance of TEASERS Material class

    mat_id : name
        id of material from XML

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.
    """

    binding = data_class.material_bind

    for mat in binding.Material:

        if mat.material_id == mat_id:

            material.material_id = mat.material_id
            material.name = mat.name
            material.density = mat.density
            material.thermal_conduc = float(mat.thermal_conduc)
            material.heat_capac = mat.heat_capac

