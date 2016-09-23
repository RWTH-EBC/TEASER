#Created July 2015
#TEASER 4 Development Team

"""DataClass

This module holds file pathes and bindings for XML data
"""

import teaser.logic.utilities as utilitis
import warnings
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
        __xml_file_tb = open(self.path_tb, 'r', encoding='utf-8')

        if bool(version_parse.getroot().attrib) is False:
            warnings.warn("You are using an old version of type building element data base XML file")
            import teaser.data.bindings.v_0_3_9.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(__xml_file_tb.read())
        elif version_parse.getroot().attrib['version'] == "0.3.9":
            import teaser.data.bindings.v_0_3_9.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(__xml_file_tb.read())
        elif version_parse.getroot().attrib['version'] == "0.4":
            import teaser.data.bindings.v_0_4.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(__xml_file_tb.read())


        self.path_uc = utilitis.get_full_path(
            "data/input/inputdata/UseConditions.xml")
        version_parse = element_tree.parse(self.path_uc)
        __xml_file_uc = open(self.path_uc, 'r', encoding='utf-8')

        if bool(version_parse.getroot().attrib) is False:
            warnings.warn("You are using an old version of use condition data base XML file")
            import teaser.data.bindings.v_0_3_9.boundaryconditions_bind as uc_bind
            self.conditions_bind = uc_bind.CreateFromDocument(
                __xml_file_uc.read())
        elif version_parse.getroot().attrib['version'] == "0.3.9":
            import teaser.data.bindings.v_0_3_9.boundaryconditions_bind as uc_bind
            self.conditions_bind = uc_bind.CreateFromDocument(__xml_file_uc.read())

        self.path_mat = utilitis.get_full_path(
            "data/input/inputdata/MaterialTemplates.xml")
        version_parse = element_tree.parse(self.path_mat)
        __xml_file_mat = codecs.open(self.path_mat, 'r', encoding='utf-8')

        if bool(version_parse.getroot().attrib) is False:
            warnings.warn("You are using an old version of material data base XML file")
            import teaser.data.bindings.v_0_3_9.material_bind as mat_bind
            self.material_bind = mat_bind.CreateFromDocument(
                __xml_file_mat.read())
        elif version_parse.getroot().attrib['version'] == "0.3.9":
            import teaser.data.bindings.v_0_3_9.material_bind as mat_bind
            self.material_bind = mat_bind.CreateFromDocument(__xml_file_mat.read())
        elif version_parse.getroot().attrib['version'] == "0.4":
            import teaser.data.bindings.v_0_4.material_bind as mat_bind
            self.material_bind = mat_bind.CreateFromDocument(__xml_file_mat.read())

