# Created July 2015
# TEASER 4 Development Team

"""This module holds file paths and bindings for XML data
"""

import warnings
import xml.etree.ElementTree as et
import os
import sys
import teaser.logic.utilities as utils

v = sys.version_info
if v >= (2, 7):
    try:
        FileNotFoundError
    except NameError:
        FileNotFoundError = IOError


class DataClass(object):
    """Class for XML data bindings

    This class loads all XML files with statistic or template data needed
    for statistical data enrichment. It creates the binding classes
    automatically with instantiation. The binding needs the Python Package PyXB.

    Parameters
    ----------

    used_statistics : str
        This parameter indicates which statistical data about building
        elements should be used. Use 'iwu' or 'tabula_de'.

    Attributes
    ----------

    element_bind : instance of PyXB TypeBuilding elements
        PyXB instance of the TypeBuildingElements binding
    path_tb : str
        Full path to TypeBuildingElements XML file (XML needs to be compliant
        with XSD schema). Default is
        teaser/data/input/inputdata/TypeBuildingElements.xml
    material_bind : instance of PyXB Material
        PyXB instance of the Material binding
    path_mat : str
        Full path to MaterialTemplates XML file (XML needs to be compliant
        with XSD schema). Default is
        teaser/data/input/inputdata/MaterialTemplates.xml
    conditions_bind : instance of PyXB UseConditions
        PyXB instance of the UseConditions binding
    path_uc : str
        Full path to UseConditions XML file (XML needs to be compliant
        with XSD schema). Default is
        teaser/data/input/inputdata/UseConditions.xml
    """

    def __init__(
            self,
            used_statistic='iwu'):
        """Constructor of DataClass
        """
        self.used_statistic = used_statistic
        self.element_bind = None
        if self.used_statistic == 'iwu':
            self.path_tb = utils.get_full_path(
                "data/input/inputdata/TypeBuildingElements.xml")
            self.load_tb_binding()
        elif self.used_statistic == 'tabula_de':
            self.path_tb = utils.get_full_path(
                os.path.join(
                    'data',
                    'input',
                    'inputdata',
                    'TypeElements_TABULA_DE.xml'))
            self.load_tb_binding()
        elif self.used_statistic is None:
            pass
        self.material_bind = None
        self.path_mat = utils.get_full_path(
            "data/input/inputdata/MaterialTemplates.xml")
        self.conditions_bind = None
        self.path_uc = utils.get_full_path(
            "data/input/inputdata/UseConditions.xml")

        self.load_uc_binding()
        self.load_mat_binding()

    def load_tb_binding(self):
        """Loads TypeBuildingElement XML into binding classes
        """

        try:
            __xml_file_tb = open(self.path_tb, 'r+')
            version_parse = et.parse(self.path_tb)
        except et.ParseError:
            __xml_file_tb = open(self.path_tb, 'w')
            version_parse = False
        except FileNotFoundError:
            __xml_file_tb = open(self.path_tb, 'w+')
            version_parse = False

        if version_parse is False:
            import teaser.data.bindings.v_0_6.typeelement_bind as tb_bind
            self.element_bind = tb_bind.TypeBuildingElements()
        elif bool(version_parse.getroot().attrib) is False:
            warnings.warn(
                "You are using an old version of type building element data "
                "base XML file")
            import teaser.data.bindings.v_0_3_9.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(
                __xml_file_tb.read())
        elif version_parse.getroot().attrib['version'] == "0.3.9":
            warnings.warn(
                "You are using an old version of type building element data "
                "base XML file")
            import teaser.data.bindings.v_0_3_9.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(
                __xml_file_tb.read())
        elif version_parse.getroot().attrib['version'] == "0.4":
            warnings.warn(
                "You are using an old version of type building element data "
                "base XML file")
            import teaser.data.bindings.v_0_4.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(
                __xml_file_tb.read())
        elif version_parse.getroot().attrib['version'] == "0.6":
            import teaser.data.bindings.v_0_6.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(
                __xml_file_tb.read())

    def load_uc_binding(self):
        """Loads UseConditions XML into binding classes
        """

        try:
            __xml_file_uc = open(self.path_uc, 'r+')
            version_parse = et.parse(self.path_uc)
        except:
            __xml_file_uc = open(self.path_uc, 'w')
            version_parse = False

        if version_parse is False:
            import teaser.data.bindings.v_0_6.boundaryconditions_bind as uc_bind
            self.conditions_bind = uc_bind.UseConditions()
        elif bool(version_parse.getroot().attrib) is False:
            warnings.warn("You are using an old version of use condition data "
                          "base XML file")
            import teaser.data.bindings.v_0_3_9.boundaryconditions_bind as uc_bind
            self.conditions_bind = uc_bind.CreateFromDocument(
                __xml_file_uc.read())
        elif version_parse.getroot().attrib['version'] == "0.3.9":
            warnings.warn("You are using an old version of use condition data "
                          "base XML file")
            import teaser.data.bindings.v_0_3_9.boundaryconditions_bind as uc_bind
            self.conditions_bind = uc_bind.CreateFromDocument(
                __xml_file_uc.read())
        elif version_parse.getroot().attrib['version'] == "0.4":
            warnings.warn("You are using an old version of use condition data "
                          "base XML file")
            import teaser.data.bindings.v_0_4.boundaryconditions_bind as uc_bind
            self.conditions_bind = uc_bind.CreateFromDocument(
                __xml_file_uc.read())
        elif version_parse.getroot().attrib['version'] == "0.6":
            import teaser.data.bindings.v_0_6.boundaryconditions_bind as uc_bind
            self.conditions_bind = uc_bind.CreateFromDocument(
                __xml_file_uc.read())

    def load_mat_binding(self):
        """Loads MaterialTemplates XML into binding classes
        """
        try:
            __xml_file_mat = open(self.path_mat, 'r+')
            version_parse = et.parse(self.path_mat)
        except:
            __xml_file_mat = open(self.path_mat, 'w')
            version_parse = False

        if version_parse is False:
            import teaser.data.bindings.v_0_6.material_bind as mat_bind
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
            warnings.warn(
                "You are using an old version of material data base XML file")
            import teaser.data.bindings.v_0_4.material_bind as mat_bind
            self.material_bind = mat_bind.CreateFromDocument(
                __xml_file_mat.read())
        elif version_parse.getroot().attrib['version'] == "0.6":
            import teaser.data.bindings.v_0_6.material_bind as mat_bind
            self.material_bind = mat_bind.CreateFromDocument(
                __xml_file_mat.read())
