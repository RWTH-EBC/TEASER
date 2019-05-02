# Created April 2016
# TEASER 4 Development Team

"""material_input.py

This module contains function to load material classes
"""


def load_material(material, mat_name, data_class):
    """Material loader.

    Loads Material specified in the XML. Sources are
    :cite:`DeutschesInstitutfurNormung.Juli2000`,
    DeutschesInstitutfurNormung.Februar2013, :cite:`Schramek.2009` and
    :cite:`VereinDeutscherIngenieure.2015c`.

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
    """

    binding = data_class.material_bind

    for mat in binding.Material:

        if mat.name == mat_name:

            material.material_id = mat.material_id
            material.name = mat.name
            material.density = mat.density
            material.thermal_conduc = float(mat.thermal_conduc)
            material.heat_capac = mat.heat_capac
            material.solar_absorp = mat.solar_absorp
            material.ir_emissivity = mat.ir_emissivity
            if float(data_class.material_bind.version) >= 0.6:
                try:
                    material.thickness_default = mat.thickness_default
                    material.thickness_list = mat.thickness_list
                except AttributeError:
                    pass


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
            material.solar_absorp = mat.solar_absorp
            material.ir_emissivity = mat.ir_emissivity
            if float(data_class.material_bind.version) >= 0.6:
                try:
                    material.thickness_default = mat.thickness_default
                    material.thickness_list = mat.thickness_list
                except AttributeError:
                    pass
