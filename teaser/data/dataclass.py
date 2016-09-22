#Created July 2015
#TEASER 4 Development Team

"""DataClass

This module holds file pathes and bindings for XML data
"""

import teaser.logic.utilities as utilitis
import teaser.data.bindings.typeelement_bind as tb_bind
import teaser.data.bindings.boundaryconditions_bind as uc_bind
import teaser.data.bindings.material_bind as mat_bind
import codecs
import xml.etree.ElementTree as element_tree

class DataClass(object):
    '''Class for XML data bindings

    This class loads all XML files with statistic or template data needed
    for statistical data enrichment. It creates the binding automatically.
    The binding needs the Python Package PyXB.

    Parameters
    ----------

    type_element_file : string
        name of the XML file with the project specific type elements
        default: TypeBuildingElements.xml for general investigation,
        this file can be exchanged to project specific files.

    Attributes
    ----------

    element_bind : instance of PyXB TypeBuilding elements
        PyXB instance of the TypeBuildingElements binding
    conditions_bind : instance of PyXB UseConditions
        PyXB instance of the UseConditions binding
    material_bind : instance of PyXB Material
        PyXB instance of the Material binding

    '''

    def __init__(self, type_element_file=None):
        '''Constructor of DataClass

        '''
        if type_element_file is None:
            self.path_tb = utilitis.get_full_path(
                "data/input/inputdata/TypeBuildingElements.xml")
        else:
            self.path_tb = utilitis.get_full_path("data/input/inputdata/"+str(
                type_element_file))

        version_parse = element_tree.parse(self.path_tb)
        if version_parse.getroot().attrib['version'] == "ASD":
            print("asd")
        __xml_file_tb = open(self.path_tb, 'r')
        self.element_bind = tb_bind.CreateFromDocument(__xml_file_tb.read())
        self.path_uc = utilitis.get_full_path(
            "data/input/inputdata/UseConditions.xml")
        __xml_file_uc = open(self.path_uc, 'r')
        self.conditions_bind = uc_bind.CreateFromDocument(__xml_file_uc.read())

        __path_mat = utilitis.get_full_path(
            "data/input/inputdata/MaterialTemplates.xml")
        __xml_file_mat = codecs.open(__path_mat, 'r', encoding='utf-8')
        self.material_bind = mat_bind.CreateFromDocument(__xml_file_mat.read())
