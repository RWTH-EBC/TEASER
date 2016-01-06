# created June 2015
# by TEASER4 Development Team

"""This module includes the Project class, which serves as base class and API
"""
import warnings
import teaser.Data.TeaserXML as txml
try:
    import teaser.Data.CityGML as citygml
except:
    warnings.warn("No CityGML module found, no CityGML import/export")    
import teaser.Data.DataHelp.OldTeaser as old_teaser
from teaser.Data.DataClass import DataClass
from mako.template import Template
import teaser.Logic.Utilis as utilis
import shutil
from teaser.Logic.BuildingObjects.TypeBuildings.Office import Office
from teaser.Logic.BuildingObjects.TypeBuildings.Institute import Institute
from teaser.Logic.BuildingObjects.TypeBuildings.Institute4 import Institute4
from teaser.Logic.BuildingObjects.TypeBuildings.Institute8 import Institute8
from teaser.Logic.BuildingObjects.TypeBuildings.Residential import Residential
from teaser.Logic.Simulation.ModelicaInfo import ModelicaInfo


class Project(object):

    '''Base class for each project, serves also as API

        The Project class is the root class for each action in TEASER and
        should be instantiated only once for each project. It also contains
        all API function to use main functionality of TEASER4

        Parameters
        ----------
        load_data : boolean
            boolean if data bindings for type elements and use conditions
            should be loaded (default = True)

        Attributes
        ----------

        list_of_buildings : list
            list of all buildings in one project, instances of Building()
        data : list
            instance of Data containing the XML binding classes, instance of
            DataClass()
        modelica_project : str
            name of the Modelica Project used in type building creation
            (default: self.name)
        weather_file_name : str
            name of the weather file used for Modelica simulation
            (default: "TRY_5_Essen.txt")
        calculation_method : str
            specifier for the calculation method for building parameters,
            codelist (ebc or vdi), (default: "vdi")

    '''

    def __init__(self, load_data=True):
        '''Constructor of Project Class.

        '''
        self.name = "Project"
        self.modelica_info = ModelicaInfo()

        self.modelica_project = self.name
        self.weather_file_name = "TRY_5_Essen.txt"
        self.list_of_buildings = []
        self._calculation_method = "vdi"

        self.load_data = load_data
        self._type_element_file = None

        if load_data is True:
            self.data = self.instantiate_data_class()
        else:
            self.data = None

    def instantiate_data_class(self, type_element_file=None):
        '''Initialization of DataClass

        Parameters
        ----------

        type_element_files: str
            Name of project specific file (if needed). (default = None)

        Returns
        ----------

        DataClass : Instance of DataClass()

        '''
        return DataClass(type_element_file)

    def load_weather_file(self, weather_path, file_name):
        '''Loads an arbitrary weather file into the InputData Folder

        Load your own weather data into the project
        Needs to be loaded before the type building is created and the record
        is exported

        Parameters
        ----------

        weather_path : string
            Path to the folder where new weather file is stored
        file_name : string
            name of the weather file

        '''
        self.weather_file_name = file_name
        weather_file = weather_path + file_name
        output_path = (utilis.get_full_path("InputData\\Boundaries \
                                            TypeBuilding\\") +
                                            file_name)

        try:
            shutil.copyfile(weather_file, output_path)
        except:
            pass
        else:
            pass

    def calc_all_buildings(self, calculation_core):
        '''Calculates values for all project buildings

        Parameters
        ----------

        calculation_core : string
            setter of the used calculation core ('vdi' or 'ebc'), default:'vdi'

        '''

        if calculation_core == self.calculation_method:
            pass
        else:
            self.calculation_method = calculation_core

        for bldg in self.list_of_buildings:

            bldg.calc_building_parameter(calculation_core)

    def retrofit_all_buildings(self, year_of_retrofit,
                               window_type=None,
                               material=None):
        ''' Retrofits all buildings in the project

        All Buildings in the project are retrofitted in the following manner:

        - replace all windows of the building to retrofitted window according
          to the year of retrofit.
        - add an additional insulation layer to all outer walls
          (including roof, and ground floor).
          The thickness of the insulation layer is calculated
          that the U-Value of the wall corresponds to the retrofit standard of
          the year of retrofit.

        The needed parameters for the Modelica Model are calculated
        automatically, using the calculation_method specified in the
        first scenario.

        Note: To Calculate U-Value, the standard TEASER coefficients for outer
        and inner heat transfer are used.

        Parameters
        ----------

        year_of_retrofit : int
            the year the buildings are retrofitted
        window_type : str
            Default: EnEv 2014
        material : str
            Default: EPS035

        '''

        for bldg in self.list_of_buildings:
            bldg.year_of_retrofit = year_of_retrofit
            bldg.retrofit_building()

    def type_bldg_office(self,
                         name,
                         year_of_construction,
                         number_of_floors,
                         height_of_floors,
                         net_leased_area,
                         office_layout=None,
                         window_layout=None,
                         construction_type=None):
        '''Create and calculate an office building

        Parameters
        ----------

        name : str
            individual name
        year_of_construction : int
            year of first construction
        number_of_floors : int
            number of floors above ground
        height_of_floors : float
            average height of the floors
        net_leased_area : float
            total net leased area of building
        office_layout : int
            type of floor plan (default = 0)

            0: use default values
            1: elongated 1 floor
            2: elongated 2 floors
            3: compact
        window_layout : int
            type of window layout (default = 0)

            0: use default values
            1: punctuated facade
            2: banner facade
            3: full glazing
        construction_type : str
            construction type (default = "heavy")

            heavy: heavy construction
            light: light construction

        Returns
        ----------

        type_bldg : Instance of Office()

        '''

        type_bldg = Office(self,
                           name,
                           year_of_construction,
                           number_of_floors,
                           height_of_floors,
                           net_leased_area,
                           office_layout,
                           window_layout,
                           construction_type)

        type_bldg.generate_office()
        type_bldg.calc_building_parameter(self.calculation_method)
        return type_bldg

    def type_bldg_institute(self,
                            name,
                            year_of_construction,
                            number_of_floors,
                            height_of_floors,
                            net_leased_area,
                            office_layout=None,
                            window_layout=None,
                            construction_type=None):
        '''Create and calculate an institute building

        Parameters
        ----------

        name : str
            individual name
        year_of_construction : int
            year of first construction
        number_of_floors : int
            number of floors above ground
        height_of_floors : float
            average height of the floors
        net_leased_area : float
            total net leased area of building
        office_layout : int
            type of floor plan (default = 0)

            0: use default values
            1: elongated 1 floor
            2: elongated 2 floors
            3: compact
        window_layout : int
            type of window layout (default = 0)

            0: use default values
            1: punctuated facade
            2: banner facade
            3: full glazing
        construction_type : str (default = "heavy")
            construction type

            heavy: heavy construction
            light: light construction

        Returns
        ----------

        type_bldg : Instance of Institute()

        '''
        type_bldg = Institute(self,
                              name,
                              year_of_construction,
                              number_of_floors,
                              height_of_floors,
                              net_leased_area,
                              office_layout,
                              window_layout,
                              construction_type)

        type_bldg.generate_office()
        type_bldg.calc_building_parameter(self.calculation_method)
        return type_bldg

    def type_bldg_institute4(self,
                             name,
                             year_of_construction,
                             number_of_floors,
                             height_of_floors,
                             net_leased_area,
                             office_layout=None,
                             window_layout=None,
                             construction_type=None):
        '''Create and calculate an institute4 building

        Parameters
        ----------

        name : str
            individual name
        year_of_construction : int
            year of first construction
        number_of_floors : int
            number of floors above ground
        height_of_floors : float
            average height of the floors
        net_leased_area : float
            total net leased area of building
        office_layout : int
            type of floor plan (default = 0)

            0: use default values
            1: elongated 1 floor
            2: elongated 2 floors
            3: compact
        window_layout : int
            type of window layout (default = 0)

            0: use default values
            1: punctuated facade
            2: banner facade
            3: full glazing
        construction_type : str (default = "heavy")
            construction type

            heavy: heavy construction
            light: light construction

        Returns
        ----------

        type_bldg : Instance of Institute4()

        '''
        type_bldg = Institute4(self,
                               name,
                               year_of_construction,
                               number_of_floors,
                               height_of_floors,
                               net_leased_area,
                               office_layout,
                               window_layout,
                               construction_type)

        type_bldg.generate_office()
        type_bldg.calc_building_parameter(self.calculation_method)
        return type_bldg

    def type_bldg_institute8(self,
                             name,
                             year_of_construction,
                             number_of_floors,
                             height_of_floors,
                             net_leased_area,
                             office_layout=None,
                             window_layout=None,
                             construction_type=None):
        '''Create and calculate an institute8 building

        Parameters
        ----------

        name : str
            individual name
        year_of_construction : int
            year of first construction
        number_of_floors : int
            number of floors above ground
        height_of_floors : float
            average height of the floors
        net_leased_area : float
            total net leased area of building
        office_layout : int
            type of floor plan (default = 0)

            0: use default values
            1: elongated 1 floor
            2: elongated 2 floors
            3: compact
        window_layout : int
            type of window layout (default = 0)

            0: use default values
            1: punctuated facade
            2: banner facade
            3: full glazing
        construction_type : str (default = "heavy")
            construction type

            heavy: heavy construction
            light: light construction

        Returns
        ----------

        type_bldg : Instance of Institute8()

        '''
        type_bldg = Institute8(self,
                               name,
                               year_of_construction,
                               number_of_floors,
                               height_of_floors,
                               net_leased_area,
                               office_layout,
                               window_layout,
                               construction_type)

        type_bldg.generate_office()
        type_bldg.calc_building_parameter(self.calculation_method)
        return type_bldg

    def type_bldg_residential(self,
                              name,
                              year_of_construction,
                              number_of_floors,
                              height_of_floors,
                              net_leased_area,
                              residential_layout=None,
                              neighbour_buildings=None,
                              attic=None,
                              cellar=None,
                              dormer=None,
                              construction_type=None):
        '''Create and calculate an residential building

        Parameters
        ----------

        name : str
            individual name
        year_of_construction : int
            year of first construction
        number_of_floors : int
            number of floors above ground
        height_of_floors : float
            average height of the floors
        net_leased_area : float
            total net leased area of building
        residential_layout : int
            type of floor plan (default = 0)

            0: compact
            1: elongated/complex
        neighbour_buildings : int
            neighbour (default = 0)

            0: no neighbour
            1: one neighbour
            2: two neighbours
        attic : int
            type of attic (default = 0)

            0: flat roof
            1: non heated attic
            2: partly heated attic
            3: heated attic
        cellar : int
            type of cellar (default = 0)

            0: no cellar
            1: non heated cellar
            2: partly heated cellar
            3: heated cellar
        construction_type : str
            construction type (default = "heavy")

            heavy: heavy construction
            light: light construction
        dormer : str
            construction type

            0: no dormer
            1: dormer

        Returns
        ----------

        type_bldg : Instance of Residential()
        '''
        type_bldg = Residential(self,
                                name,
                                year_of_construction,
                                number_of_floors,
                                height_of_floors,
                                net_leased_area,
                                residential_layout,
                                neighbour_buildings,
                                attic,
                                cellar,
                                dormer,
                                construction_type)

        type_bldg.generate_residential()
        type_bldg.calc_building_parameter(self.calculation_method)
        return type_bldg

    def save_project(self, file_name=None, path=None):
        '''Saves the project to a tXML file

        calls the function save_teaser_xml in Data.TeaserXML.py

        Parameters
        ----------

        file_name : string
            name of the new file
        path : string
            if the Files should not be stored in OutputData, an alternative
            can be specified

        '''
        if file_name is None:
            name = self.name
        else:
            name = file_name

        if path is None:
            new_path = utilis.get_full_path("OutputData") + "\\" + name
        else:
            new_path = path + "\\" + name
            utilis.create_path(utilis.get_full_path(path))

        txml.save_teaser_xml(new_path, self)

    def load_project(self, path):
        '''Loads the project from a teaserXML file (new format)

        calls the function load_teaser_xml in Data.TeaserXML.py

        Parameters
        ----------
        path : string
            full path to a teaserXML file

        '''

        txml.load_teaser_xml(path, self)

    def load_old_teaser(self, path):
        '''Loads the project from an old TEASER xml file

        calls the function load_teaser_xml in Data.DataHelp.OldTeaser.py


        Parameters
        ----------
        path : string
            full path to a teaserXML file

        '''

        old_teaser.load_teaser_xml(path, self)

    def save_citygml(self, file_name=None, path=None):
        '''Saves the project to a citygml file

        calls the function save_gml in Data.CityGML we make use of CityGML core
        and EnergyADE to store semantic information


        Parameters
        ----------

        file_name : string
            name of the new file
        path : string
            if the Files should not be stored in OutputData, an alternative
            can be specified

        '''
        if file_name is None:
            name = self.name
        else:
            name = file_name

        if path is None:
            new_path = utilis.get_full_path("OutputData") + "\\" + name
        else:
            new_path = path + "\\" + name
            utilis.create_path(utilis.get_full_path(path))

        citygml.save_gml(self, new_path)


    def export_record(self, model_type, path=None, buildingID=None):
        '''Exports values to a record file for Modelica simulation


        Parameters
        ----------

        model_type : string
            setter of the used Modelica model (AixLib or CitiesRWin)
        path : string
            if the Files should not be stored in OutputData, an alternative
            path can be specified

        '''
        if path is None:
            path = "OutputData\\" + self.name
        else:
            path = path + "\\" + self.name

        utilis.create_path(utilis.get_full_path(path))

        input_path = utilis.get_full_path("InputData\\BoundariesTypeBuilding")

        try:
            shutil.copytree(
                input_path, utilis.get_full_path(path) + "\\Tables")
        except:
            pass
        else:
            pass

        if model_type == "CitiesRWin":

            uses = ['BaseLib (version="2.4")',
                    'DataBase (version="2.4")',
                    'Building (version="2.4")',
                    'HVAC (version="2.4")',
                    'Cities (version="2.4")',
                    'Modelica (version="3.2.1")',
                    'AixLib(version="0.1.0")']

            for bldg in self.list_of_buildings:
                assert bldg._calculation_method == "ebc", ("CitiesRWin needs \
                calculation core ebc")

            zone_template = Template(
                filename=utilis.get_full_path(
                    "InputData\\RecordTemplate\\CitiesRWin\\CitiesRWin_zone"))
            zone_base_template = Template(
                filename=utilis.get_full_path(
                    "InputData\\RecordTemplate\\CitiesRWin\\CitiesRWin_base"))
            building_template = Template(
                filename=utilis.get_full_path(
                    "InputData\\RecordTemplate\\CitiesRWin\\CitiesRWin_bldg"))

            self._help_package(path, self.name)
            self._help_package_order(path, self.list_of_buildings)

        elif model_type == "AixLib":

            uses = ['Modelica(version = "3.2.1")',
                    "AixLib(version=\"0.1.0\")"]

            for bldg in self.list_of_buildings:
                assert bldg._calculation_method == "vdi", ("AixLib needs \
                calculation core vdi")

            zone_template = Template(
                filename=utilis.get_full_path(
                    "InputData\\RecordTemplate\\AixLib\\AixLib_zone"))

            self._help_package(path, self.name, uses)
            self._help_package_order(path, self.list_of_buildings)

        elif model_type == "CitiesType_old":

            uses = ['BaseLib (version="2.2")',
                    'DataBase (version="2.2")',
                    'Building (version="2.2")',
                    'HVAC (version="2.2")',
                    'Cities (version="2.2")',
                    'Modelica (version="3.2.1")']

            for bldg in self.list_of_buildings:
                assert bldg._calculation_method == "vdi", ("CitiesType_old \
                    needs calculation core vdi")

            zone_template = Template(
                filename=utilis.get_full_path(
                    "InputData\\RecordTemplate\\CitiesType\\CitiesType_zone"))
            zone_base_template = Template(
                filename=utilis.get_full_path(
                    "InputData\\RecordTemplate\\CitiesType\\CitiesType_base"))
            building_template = Template(
                filename=utilis.get_full_path(
                    "InputData\\RecordTemplate\\CitiesType\\CitiesType_bldg"))

            self._help_package(path, self.name, uses)
            self._help_package_order(path, self.list_of_buildings)

        else:

            raise ValueError("specify calculation method correctly")

        for bldg in self.list_of_buildings:

            bldg_path = path + "\\" + bldg.name + "\\"
            utilis.create_path(utilis.get_full_path(bldg_path))
            utilis.create_path(utilis.get_full_path
                               (bldg_path + bldg.name + "_DataBase"))

            self._help_package(bldg_path, bldg.name)
            self._help_package_order(bldg_path, [bldg], None,
                                     bldg.name + "_DataBase")

            if model_type == "CitiesRWin" or model_type == "CitiesType_old":
                out_file = open(utilis.get_full_path
                                (bldg_path + bldg.name + ".mo"), 'w')
                out_file.write(building_template.render_unicode
                               (bldg=bldg, mod_prj=self.modelica_project))
                out_file.close()

            for zone in bldg.thermal_zones:
                zone_path = bldg_path + bldg.name + "_DataBase" + "\\"

                out_file = open(utilis.get_full_path(
                    zone_path + "\\" + bldg.name + "_" + zone.name + ".mo"),
                                                                           'w')
                out_file.write(zone_template.render_unicode(
                    bldg=bldg, zone=zone))
                out_file.close()

                if model_type == "CitiesRWin" or\
                        model_type == "CitiesType_old":
                    self._help_package(zone_path, bldg.name + "_DataBase")
                    self._help_package_order(
                        zone_path, bldg.thermal_zones, bldg.name + "_",
                        bldg.name + "_base")

                    out_file = open(utilis.get_full_path
                                    (zone_path + bldg.name + "_base.mo"), 'w')
                    out_file.write(zone_base_template.render_unicode(
                        bldg=bldg, zone=zone, mod_prj=self.modelica_project))
                    out_file.close()
                else:
                    pass

    def export_parameters_txt(self, path=None):
        '''Exports parameters of all buildings in a readable text file

        Parameters
        ----------

        path : string
            if the Files should not be stored in OutputData, an alternative
            can be specified
        '''
        if path is None:
            path = "OutputData\\"+self.name
        else:
            path = path+"\\"+self.name

        for bldg in self.list_of_buildings:
            bldg_path = path + "\\" + bldg.name + "\\"
            utilis.create_path(utilis.get_full_path(bldg_path))
            readable_template = Template(
                filename=utilis.get_full_path(
                    "InputData\\ReadableOutputTemplate\\ReadableBuilding"))

            out_file = open(utilis.get_full_path
                            (bldg_path+"ReadableOutput.txt"), 'w')
            out_file.write(readable_template.render_unicode
                           (bldg=bldg, prj=self))
            out_file.close()

    def _help_package(self, path, name, uses=None):
        '''creates a package.mo file

        private function, do not call

        Parameters
        ----------

        path : string
            path of where the package.mo should be placed
        name : string
            name of the Modelica package

        '''

        package_template = Template(filename=utilis.get_full_path
                                    ("InputData\\RecordTemplate\\package"))

        out_file = open(
            utilis.get_full_path(path + "\\" + "package" + ".mo"), 'w')
        out_file.write(package_template.render_unicode(name=name, uses=uses))
        out_file.close()

    def _help_package_order(self, path, package_list,
                            addition=None, extra=None):
        '''creates a package.order file

        private function, do not call

        Parameters
        ----------

        path : string
            path of where the package.mo should be placed
        package_list : [string]
            name of all models or packages contained in the package
        addition : string
            if there should be a suffix in front of package_list.string it can
            be specified
        extra : string
            an extra package or model not contained in package_list can be
            specified

        '''
        order_template = Template(filename=utilis.get_full_path
                                  ("InputData\\RecordTemplate\\package_order"))

        out_file = open(
            utilis.get_full_path(path + "\\" + "package" + ".order"), 'w')
        out_file.write(order_template.render_unicode
                       (list=package_list, addition=addition, extra=extra))
        out_file.close()

    def set_default(self):
        '''sets all attributes except self.data to default

        '''

        self.name = "Project"

        self.modelica_project = self.name
        self.weather_file_name = "TRY_5_Essen.txt"
        self.list_of_buildings = []
        self.calculation_method = "vdi"

        self._type_element_file = None

    @property
    def type_element_file(self):
        return self._type_element_file

    @type_element_file.setter
    def type_element_file(self, value):
        self._type_element_file = value
        self.instantiate_data_class(value)

    @property
    def calculation_method(self):
        return self._calculation_method

    @calculation_method.setter
    def calculation_method(self, value):

        ass_error_1 = "calculation_method has to be vdi or ebc"

        assert value != "ebc" or value != "vdi", ass_error_1

        self._calculation_method = value
