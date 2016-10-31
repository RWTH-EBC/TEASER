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

    def __init__(self):
        '''Constructor of DataClass
        '''

        self.element_bind = None
        self.material_bind = None
        self.conditions_bind = None


        self.path_tb = utilitis.get_full_path(
            "data/input/inputdata/TypeBuildingElements.xml")
        self.path_uc = utilitis.get_full_path(
            "data/input/inputdata/UseConditions.xml")
        self.path_mat = utilitis.get_full_path(
            "data/input/inputdata/MaterialTemplates.xml")

        self.load_tb_binding()
        self.load_uc_binding()
        self.load_mat_binding()

    def load_tb_binding(self):
        """loads specified type building XML files into bindings

        """

        try:
            __xml_file_tb = open(self.path_tb, 'r+')
            version_parse = element_tree.parse(self.path_tb)
        except:
            __xml_file_tb = open(self.path_tb, 'w')
            version_parse = False

        if version_parse is False:
            import teaser.data.bindings.v_0_4.typeelement_bind as tb_bind
            self.element_bind = tb_bind.TypeBuildingElements()
        elif bool(version_parse.getroot().attrib) is False:
            warnings.warn(
                "You are using an old version of type building element data base XML file")
            import teaser.data.bindings.v_0_3_9.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(__xml_file_tb.read())
        elif version_parse.getroot().attrib['version'] == "0.3.9":
            warnings.warn(
                "You are using an old version of type building element data base XML file")
            import teaser.data.bindings.v_0_3_9.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(__xml_file_tb.read())
        elif version_parse.getroot().attrib['version'] == "0.4":
            import teaser.data.bindings.v_0_4.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(__xml_file_tb.read())

    def load_uc_binding(self):
        """loads specified use condition XML files into bindings

        """

        try:
            __xml_file_uc = open(self.path_uc, 'r+')
            version_parse = element_tree.parse(self.path_uc)
        except:
            __xml_file_uc = open(self.path_uc, 'w')
            version_parse = False

        if version_parse is False:
            import teaser.data.bindings.v_0_4.boundaryconditions_bind as uc_bind
            self.conditions_bind = uc_bind.UseConditions()
        elif bool(version_parse.getroot().attrib) is False:
            warnings.warn("You are using an old version of use condition data base XML file")
            import teaser.data.bindings.v_0_3_9.boundaryconditions_bind as uc_bind
            self.conditions_bind = uc_bind.CreateFromDocument(
                __xml_file_uc.read())
        elif version_parse.getroot().attrib['version'] == "0.3.9":
            warnings.warn("You are using an old version of use condition data base XML file")
            import teaser.data.bindings.v_0_3_9.boundaryconditions_bind as uc_bind
            self.conditions_bind = uc_bind.CreateFromDocument(
                __xml_file_uc.read())
        elif version_parse.getroot().attrib['version'] == "0.4":
            import teaser.data.bindings.v_0_4.boundaryconditions_bind as uc_bind
            self.conditions_bind = uc_bind.CreateFromDocument(
                __xml_file_uc.read())

    def load_mat_binding(self):
        """loads specified material XML files into bindings

        """
        try:
            __xml_file_mat = open(self.path_mat, 'r+')
            version_parse = element_tree.parse(self.path_tb)
        except:
            __xml_file_mat = open(self.path_mat, 'w')
            version_parse = False

        if version_parse is False:
            import teaser.data.bindings.v_0_4.material_bind as mat_bind
            self.material_bind = mat_bind.MaterialTemplates()
        elif bool(version_parse.getroot().attrib) is False:
            warnings.warn(
                "You are using an old version of material data base XML file")
            import teaser.data.bindings.v_0_3_9.material_bind as mat_bind
            self.material_bind = mat_bind.CreateFromDocument(
                __xml_file_mat.read())
        elif version_parse.getroot().attrib['version'] == "0.3.9":
            warnings.warn(
                "You are using an old version of material data base XML file")
            import teaser.data.bindings.v_0_3_9.material_bind as mat_bind
            self.material_bind = mat_bind.CreateFromDocument(
                __xml_file_mat.read())
        elif version_parse.getroot().attrib['version'] == "0.4":
            import teaser.data.bindings.v_0_4.material_bind as mat_bind
            self.material_bind = mat_bind.CreateFromDocument(
                __xml_file_mat.read())
