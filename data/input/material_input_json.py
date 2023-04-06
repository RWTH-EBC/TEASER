"""This module contains function to load material classes."""


def load_material(material, mat_name, data_class):
    """Material loader with name as identification.

    Loads Material specified in the JSON. Sources are
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

    for id, mat in binding.items():
        if id != "version":
            if mat["name"] == mat_name:

                material.material_id = id
                material.name = mat["name"]
                material.density = mat["density"]
                material.thermal_conduc = mat["thermal_conduc"]
                material.heat_capac = mat["heat_capac"]
                material.solar_absorp = mat["solar_absorp"]
                material.thickness_default = mat["thickness_default"]
                material.thickness_list = mat["thickness_list"]


def load_material_id(material, mat_id, data_class):
    """Material loader with id as identification.

    Loads Material specified in the JSON by given material_id.

    Parameters
    ----------
    material : Material()
        instance of TEASERS Material class

    mat_id : name
        id of material from JSON

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.

    """
    binding = data_class.material_bind

    for id, mat in binding.items():
        if id != "version":
            if id == mat_id:

                material.material_id = id
                material.name = mat["name"]
                material.density = mat["density"]
                material.thermal_conduc = mat["thermal_conduc"]
                material.heat_capac = mat["heat_capac"]
                material.solar_absorp = mat["solar_absorp"]
                material.thickness_default = mat["thickness_default"]
                material.thickness_list = mat["thickness_list"]
