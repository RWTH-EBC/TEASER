#Created April 2016
#TEASER 4 Development Team

"""material_output.py

This module contains function to save material classes
"""
import teaser.data.bindings.v_0_4.material_bind as mat_bind
import teaser.logic.utilities as utilitis


def save_material(material, data_class):
    """Material saver.

    Saves Material specified in the XML.

    Parameters
    ----------
    material : Material()
        instance of TEASERS Material class

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.

    """

    mat_pyxb = mat_bind.MaterialType()

    mat_pyxb.name = material.name
    mat_pyxb.density = material.density
    mat_pyxb.thermal_conduc = material.thermal_conduc
    mat_pyxb.heat_capac = material.heat_capac
    mat_pyxb.material_id = material.material_id

    mat_binding = data_class.material_bind
    mat_binding.Material.append(mat_pyxb)
    out_file = open(utilitis.get_full_path(data_class.path_mat), "w")

    out_file.write(mat_binding.toDOM().toprettyxml())
