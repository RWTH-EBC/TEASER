# Created July 2015
# TEASER 4 Development Team

"""This module holds file paths and bindings for XML data
"""

import teaser.logic.utilities as utils
import warnings
import xml.etree.ElementTree as et
import os
import numpy as np
import math

class DataClass(object):
    """Class for XML data bindings

    This class loads all XML files with statistic or template data needed
    for statistical data enrichment. It creates the binding classes
    automatically with instantiation. The binding needs the Python Package PyXB.

    If VDI Simulation in Python is used, this class loads and stores weather
    data from TRY in a dictionary.

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

    weather_data : dict
        Dictionary containing relevant weather data from Test Reference Year
        (TRY) in following form:
        'air_temp' : np.array - Air temperature
        'sun_dir' : np.array - direct horizontal solar radiation
        'sun_diff' : np.array - diffuse horizontal solar radiation
        'rad_sky' : np.array - longwave sky radiation
        'rad_earth' : np.array - longwave earth radiation
    """

    def __init__(self):
        """Constructor of DataClass
        """

        self.element_bind = None
        self.path_tb = utils.get_full_path(
            "data/input/inputdata/TypeBuildingElements.xml")
        self.material_bind = None
        self.path_mat = utils.get_full_path(
            "data/input/inputdata/MaterialTemplates.xml")
        self.conditions_bind = None
        self.path_uc = utils.get_full_path(
            "data/input/inputdata/UseConditions.xml")

        self.load_tb_binding()
        self.load_uc_binding()
        self.load_mat_binding()

        self.weather_data = {
            'air_temp': None,
            'sun_dir': None,
            'sun_diff': None,
            'rad_sky': None,
            'rad_earth': None}

    def load_tb_binding(self):
        """Loads TypeBuildingElement XML into binding classes
        """

        try:
            __xml_file_tb = open(self.path_tb, 'r+')
            version_parse = et.parse(self.path_tb)
        except:
            __xml_file_tb = open(self.path_tb, 'w')
            version_parse = False

        if version_parse is False:
            import teaser.data.bindings.v_0_4.typeelement_bind as tb_bind
            self.element_bind = tb_bind.TypeBuildingElements()
        elif bool(version_parse.getroot().attrib) is False:
            warnings.warn(
                "You are using an old version of type building element data "
                "base XML file")
            import teaser.data.bindings.v_0_3_9.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(__xml_file_tb.read())
        elif version_parse.getroot().attrib['version'] == "0.3.9":
            warnings.warn(
                "You are using an old version of type building element data "
                "base XML file")
            import teaser.data.bindings.v_0_3_9.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(__xml_file_tb.read())
        elif version_parse.getroot().attrib['version'] == "0.4":
            import teaser.data.bindings.v_0_4.typeelement_bind as tb_bind
            self.element_bind = tb_bind.CreateFromDocument(__xml_file_tb.read())

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
            import teaser.data.bindings.v_0_4.boundaryconditions_bind as uc_bind
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
            import teaser.data.bindings.v_0_4.boundaryconditions_bind as uc_bind
            self.conditions_bind = uc_bind.CreateFromDocument(
                __xml_file_uc.read())

    def load_mat_binding(self):
        """Loads MaterialTemplates XML into binding classes
        """
        try:
            __xml_file_mat = open(self.path_mat, 'r+')
            version_parse = et.parse(self.path_tb)
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

    def load_weather(self, path):
        """Loads Weather time series from TRY .dat file into dict

        Parameters
        ----------

        path : str
            Full path to TRY .dat file

        """

        wea_data = np.genfromtxt(
            path,
            skip_header=38,
            usecols=(8, 13, 14, 16, 17))

        self.weather_data['air_temp'] = wea_data[:, 0]
        self.weather_data['sun_dir'] = wea_data[:, 1]
        self.weather_data['sun_diff'] = wea_data[:, 2]
        self.weather_data['rad_sky'] = wea_data[:, 3]
        self.weather_data['rad_earth'] = wea_data[:, 4]
