#Created April 2016
#TEASER 4 Development Team

"""material_output.py

This module contains function to save material classes
"""
import teaser.data.bindings.v_0_4.material_bind as mat_bind
import teaser.logic.utilities as utilitis
import warnings
import pyxb

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
    mat_binding = data_class.material_bind
    add_to_xml = True
    mat_binding.version = "0.4"
    warning_text = ("Material with same name and same properties already "
                    "exists in XML, consider this material or revising your "
                    "properties")

    pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        mat_bind.Namespace, 'materials')

    for check in mat_binding.Material:
        if check.name == material.name and \
                check.density == material.density and \
                check.thermal_conduc == material.thermal_conduc and \
                check.heat_capac == material.heat_capac:
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

        mat_binding.Material.append(mat_pyxb)
        out_file = open(utilitis.get_full_path(data_class.path_mat), "w")

        out_file.write(mat_binding.toDOM().toprettyxml())
