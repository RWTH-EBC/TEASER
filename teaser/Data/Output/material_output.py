'''
Created April 2016

@author: TEASER Development Team
'''

"""material_output.py

This module contains function to save material classes
"""
import teaser.Data.SchemaBindings.MaterialBind as mat_bind
import teaser.Logic.Utilis as utilis

def save_material(material):
    '''Material saver.

    Saves Material specified in the XML.
    
    Parameters
    ----------
    material : Material()
        instance of TEASERS Material class

    '''

    mat_pyxb = mat_bind.MaterialType()
    mat_pyxb.name = material.name
    mat_pyxb.density = material.density
    mat_pyxb.thermal_conduc = material.thermal_conduc
    mat_pyxb.heat_capac = material.heat_capac

    path = utilis.get_full_path("InputData/MaterialTemplates.xml")
    xml_file = open(path, 'r')

    xml_parse = mat_bind.CreateFromDocument(xml_file.read())
    xml_parse.Material.append(mat_pyxb)
    out_file = open(path, 'w')

    out_file.write(xml_parse.toDOM().toprettyxml())