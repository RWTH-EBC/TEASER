# Created April 2016
# TEASER Development Team

"""material_output.py

This module contains function to save material classes
"""
import warnings

import pyxb

import teaser.data.bindings.v_0_6.material_bind as mat_bind
import teaser.logic.utilities as utilities


def save_material(material, data_class):
    """Material saver.

    Saves material and their properties the XML file for type building
    elements. If the Project parent is set, it automatically saves it to
    the file given in Project.data. Alternatively you can specify a path to
    a file with Materials. If this file does not exist, a new file is created.

    Parameters
    ----------
    material : Material()
        instance of TEASERS Material class

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.

    """
    mat_binding = data_class.material_bind
    add_to_xml = True
    mat_binding.version = "0.6"
    warning_text = ("Material with same name and same properties already "
                    "exists in XML, consider this material or revising your "
                    "properties")

    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        mat_bind.Namespace, 'materials')

    for check in mat_binding.Material:
        if check.name == material.name and \
                check.density == material.density and \
                check.thermal_conduc == material.thermal_conduc and \
                check.heat_capac == material.heat_capac and \
                check.thickness_default == material.thickness_default and \
                check.thickness_list == material.thickness_list:
            warnings.warn(warning_text)
            add_to_xml = False
            break

    if add_to_xml is True:
        mat_pyxb = mat_bind.MaterialType()

        mat_pyxb.name = material.name
        mat_pyxb.density = material.density
        mat_pyxb.thermal_conduc = material.thermal_conduc
        mat_pyxb.heat_capac = material.heat_capac
        mat_pyxb.material_id = material.material_id
        mat_pyxb.thickness_default = material.thickness_default
        mat_pyxb.thickness_list = material.thickness_list
        mat_pyxb.solar_absorp = material.solar_absorp

        mat_binding.Material.append(mat_pyxb)
        out_file = open(utilities.get_full_path(data_class.path_mat), "w")

        out_file.write(mat_binding.toDOM().toprettyxml())


def modify_material(material, data_class):
    """Material modifier.

    Modifies material and their properties the XML file for type building
    elements. If the Project parent is set, it automatically modifies it to
    the file given in Project.data.

    Parameters
    ----------
    material : Material()
        instance of TEASERS Material class

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.

    """

    mat_binding = data_class.material_bind

    for mat in mat_binding.Material:
        if mat.material_id == material.material_id:
            # mat_binding.Material.remove(mat)
            mat.material_id = material.material_id
            mat.name = material.name
            mat.density = material.density
            mat.thermal_conduc = material.thermal_conduc
            mat.heat_capac = material.heat_capac
            # mat_binding.Material.append(mat)"""
            break

    out_file = open(utilities.get_full_path(data_class.path_mat), "w")
    out_file.write(mat_binding.toDOM().toprettyxml())
