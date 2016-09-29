# created June 2015
# by TEASER4 Development Team

"""This module includes the Project class, which serves as base class and API
"""


import warnings
import os
import teaser.logic.utilities as utilitis
import teaser.data.input.teaserxml_input as txml_in
import teaser.data.output.teaserxml_output as txml_out
import teaser.data.output.aixlib_output as aixlib_output
import teaser.data.output.annex60_output as annex60_output
import teaser.data.output.text_output as text_out
from teaser.data.dataclass import DataClass
from teaser.logic.archetypebuildings.bmvbs.office import Office
from teaser.logic.archetypebuildings.bmvbs.custom.institute import Institute
from teaser.logic.archetypebuildings.bmvbs.custom.institute4 import Institute4
from teaser.logic.archetypebuildings.bmvbs.custom.institute8 import Institute8
from teaser.logic.archetypebuildings.urbanrenet.est1a import EST1a
from teaser.logic.archetypebuildings.urbanrenet.est1b import EST1b
from teaser.logic.archetypebuildings.urbanrenet.est4b import EST4b
from teaser.logic.archetypebuildings.urbanrenet.est7 import EST7
from teaser.logic.archetypebuildings.bmvbs.singlefamilydwelling import SingleFamilyDwelling
from teaser.logic.simulation.modelicainfo import ModelicaInfo

try:
    import teaser.data.output.citygml_output as citygml_out
    import teaser.data.input.citygml_input as citygml_in
except:
    warnings.warn("No CityGML module found, no CityGML import/export")

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

        buildings : list
            list of all buildings in one project, instances of Building()
        data : list
            instance of Data containing the XML binding classes, instance of
            DataClass()
        modelica_project : str
            name of the Modelica Project used in type building creation
            (default: self.name)
        weather_file_header : str
            header of weather file used for Modelica simulation
        weather_file_path : str
            path to weather file used for Modelica simulation
            (default: "TRY_5_Essen.txt")
        number_of_elements_calc : int
            defines the number of elements, that area aggregated, between 1
            and 4, default is 2
        merge_windows_calc : bool
            True for merging the windows into the outer walls, False for
            separate resistance for window, default is False
        used_library_calc : str
            used library (AixLib and Annex60 are supported)

    '''

    def __init__(self, load_data=True):
        '''Constructor of Project Class.

        '''
        self._name = "Project"
        self.modelica_info = ModelicaInfo()

        self.modelica_project = self.name
        self.weather_file_header = "wetter"
        self.weather_file_path = "modelica://AixLib/Resources/WeatherData/" \
                                 "TRY2010_12_Jahr_Modelica-Library.txt"
        self.buildings = []

        self._calculation_method = "vdi"

        self.load_data = load_data
        self._type_element_file = None

        self._number_of_elements_calc = 2
        self._merge_windows_calc = False
        self._used_library_calc = "AixLib"

        if load_data is True:
            self.data = self.instantiate_data_class()
        else:
            self.data = None

    def instantiate_data_class(self):
        '''Initialization of DataClass

        Returns
        ----------

        DataClass : Instance of DataClass()

        '''
        return DataClass()

    def calc_all_buildings(self, raise_errors=False):
        '''Calculates values for all project buildings

        You need to set the following parameters in the Project class.

        number_of_elements_calc : int
            defines the number of elements, that area aggregated, between 1
            and 4, default is 2
            For AixLib you should always use 2 elements!!!

        merge_windows_calc : bool
            True for merging the windows into the outer walls, False for
            separate resistance for window, default is False
            For AixLib vdi calculation is True, ebc calculation is False

        used_library_calc : str
            used library (AixLib and Annex60 are supported)

        '''
        if raise_errors is True:
            for bldg in reversed(self.buildings):
                bldg.calc_building_parameter(
                    number_of_elements=self._number_of_elements_calc,
                    merge_windows=self._merge_windows_calc,
                    used_library=self._used_library_calc)
        else:
            for bldg in reversed(self.buildings):
                try:
                    bldg.calc_building_parameter(
                        number_of_elements=self._number_of_elements_calc,
                        merge_windows=self._merge_windows_calc,
                        used_library=self._used_library_calc)
                except:
                    print("Following building can't be calculated:", bldg.name)
                    print("raise_errors=True to get python errors")
                    self.buildings.remove(bldg)

    def retrofit_all_buildings(self,
                               year_of_retrofit,
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

        for bldg in self.buildings:
            bldg.retrofit_building(year_of_retrofit, window_type, material)

    def type_bldg_office(self,
                         name,
                         year_of_construction,
                         number_of_floors,
                         height_of_floors,
                         net_leased_area,
                         with_ahu=True,
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
        with_ahu : boolean
            if building has a central AHU or not
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
                           with_ahu,
                           office_layout,
                           window_layout,
                           construction_type)

        type_bldg.generate_archetype()
        type_bldg.calc_building_parameter(
            number_of_elements=self._number_of_elements_calc,
            merge_windows=self._merge_windows_calc,
            used_library=self._used_library_calc)
        return type_bldg

    def type_bldg_institute(self,
                            name,
                            year_of_construction,
                            number_of_floors,
                            height_of_floors,
                            net_leased_area,
                            with_ahu=True,
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
        with_ahu : boolean
            if building has a central AHU or not
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
                              with_ahu,
                              office_layout,
                              window_layout,
                              construction_type)

        type_bldg.generate_archetype()
        type_bldg.calc_building_parameter(
                number_of_elements=self._number_of_elements_calc,
                merge_windows=self._merge_windows_calc,
                used_library=self._used_library_calc)
        return type_bldg

    def type_bldg_institute4(self,
                             name,
                             year_of_construction,
                             number_of_floors,
                             height_of_floors,
                             net_leased_area,
                             with_ahu=True,
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
        with_ahu : boolean
            if building has a central AHU or not
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
                               with_ahu,
                               office_layout,
                               window_layout,
                               construction_type)

        type_bldg.generate_archetype()
        type_bldg.calc_building_parameter(
                number_of_elements=self._number_of_elements_calc,
                merge_windows=self._merge_windows_calc,
                used_library=self._used_library_calc)
        return type_bldg

    def type_bldg_institute8(self,
                             name,
                             year_of_construction,
                             number_of_floors,
                             height_of_floors,
                             net_leased_area,
                             with_ahu=True,
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
        with_ahu : boolean
            if building has a central AHU or not
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
                               with_ahu,
                               office_layout,
                               window_layout,
                               construction_type)

        type_bldg.generate_archetype()
        type_bldg.calc_building_parameter(
                number_of_elements=self._number_of_elements_calc,
                merge_windows=self._merge_windows_calc,
                used_library=self._used_library_calc)
        return type_bldg

    def type_bldg_est1a(self,
                             name,
                             year_of_construction,
                             number_of_floors,
                             height_of_floors,
                             net_leased_area,
                             with_ahu=False,
                             neighbour_buildings=None,
                             construction_type=None):
        '''Create and calculate an est1a building

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
        with_ahu : boolean
            if building has a central AHU or not
        neighbour_buildings : int
            neighbour (default = 0)

            0: no neighbour
            1: one neighbour
            2: two neighbours
        construction_type : str (default = "heavy")
            construction type

            heavy: heavy construction
            light: light construction

        Returns
        ----------

        type_bldg : Instance of EST1a()

        '''
        type_bldg = EST1a(self,
                               name,
                               year_of_construction,
                               number_of_floors,
                               height_of_floors,
                               net_leased_area,
                               with_ahu,
                               neighbour_buildings,
                               construction_type)

        type_bldg.generate_archetype()
        type_bldg.calc_building_parameter(
                number_of_elements=self._number_of_elements_calc,
                merge_windows=self._merge_windows_calc,
                used_library=self._used_library_calc)
        return type_bldg

    def type_bldg_est1b(self,
                             name,
                             year_of_construction,
                             number_of_floors,
                             height_of_floors,
                             net_leased_area,
                             with_ahu=False,
                             neighbour_buildings=None,
                             construction_type=None,
                             number_of_apartments=None):
        '''Create and calculate an est1a building

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
        with_ahu : boolean
            if building has a central AHU or not
        neighbour_buildings : int
            neighbour (default = 0)

            0: no neighbour
            1: one neighbour
            2: two neighbours
        construction_type : str (default = "heavy")
            construction type

            heavy: heavy construction
            light: light construction

        Returns
        ----------

        type_bldg : Instance of EST1a()

        '''
        type_bldg = EST1b(self,
                               name,
                               year_of_construction,
                               number_of_floors,
                               height_of_floors,
                               net_leased_area,
                               with_ahu,
                               neighbour_buildings,
                               construction_type,
                               number_of_apartments)

        type_bldg.generate_archetype()
        type_bldg.calc_building_parameter(
                number_of_elements=self._number_of_elements_calc,
                merge_windows=self._merge_windows_calc,
                used_library=self._used_library_calc)
        return type_bldg

    def type_bldg_est4b(self,
                             name,
                             year_of_construction,
                             number_of_floors,
                             height_of_floors,
                             net_leased_area,
                             with_ahu=False,
                             neighbour_buildings=None,
                             construction_type=None,
                             number_of_apartments=None):
        '''Create and calculate an est1a building

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
        with_ahu : boolean
            if building has a central AHU or not
        neighbour_buildings : int
            neighbour (default = 0)

            0: no neighbour
            1: one neighbour
            2: two neighbours
        construction_type : str (default = "heavy")
            construction type

            heavy: heavy construction
            light: light construction

        Returns
        ----------

        type_bldg : Instance of EST1a()

        '''
        type_bldg = EST4b(self,
                               name,
                               year_of_construction,
                               number_of_floors,
                               height_of_floors,
                               net_leased_area,
                               with_ahu,
                               neighbour_buildings,
                               construction_type,
                               number_of_apartments)

        type_bldg.generate_archetype()
        type_bldg.calc_building_parameter(
                number_of_elements=self._number_of_elements_calc,
                merge_windows=self._merge_windows_calc,
                used_library=self._used_library_calc)
        return type_bldg

    def type_bldg_est7(self,
                             name,
                             year_of_construction,
                             number_of_floors,
                             height_of_floors,
                             net_leased_area,
                             with_ahu=False,
                             neighbour_buildings=None,
                             construction_type=None,
                             number_of_apartments=None):
        '''Create and calculate an est1a building

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
        with_ahu : boolean
            if building has a central AHU or not
        neighbour_buildings : int
            neighbour (default = 0)

            0: no neighbour
            1: one neighbour
            2: two neighbours
        construction_type : str (default = "heavy")
            construction type

            heavy: heavy construction
            light: light construction

        Returns
        ----------

        type_bldg : Instance of EST1a()

        '''
        type_bldg = EST7(self,
                               name,
                               year_of_construction,
                               number_of_floors,
                               height_of_floors,
                               net_leased_area,
                               with_ahu,
                               neighbour_buildings,
                               construction_type,
                               number_of_apartments)

        type_bldg.generate_archetype()
        type_bldg.calc_building_parameter(
                number_of_elements=self._number_of_elements_calc,
                merge_windows=self._merge_windows_calc,
                used_library=self._used_library_calc)
        return type_bldg

    def type_bldg_residential(self,
                              name,
                              year_of_construction,
                              number_of_floors,
                              height_of_floors,
                              net_leased_area,
                              with_ahu=False,
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
        with_ahu : boolean
            if building has a central AHU or not
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

        type_bldg : Instance of SingleFamilyDwelling()
        '''
        type_bldg = SingleFamilyDwelling(self,
                                         name,
                                         year_of_construction,
                                         number_of_floors,
                                         height_of_floors,
                                         net_leased_area,
                                         with_ahu,
                                         residential_layout,
                                         neighbour_buildings,
                                         attic,
                                         cellar,
                                         dormer,
                                         construction_type)

        type_bldg.generate_archetype()
        type_bldg.calc_building_parameter(
                number_of_elements=self._number_of_elements_calc,
                merge_windows=self._merge_windows_calc,
                used_library=self._used_library_calc)
        return type_bldg

    def save_project(self, file_name=None, path=None):
        '''Saves the project to a tXML file

        calls the function save_teaser_xml in data.TeaserXML.py

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
            new_path = os.path.join(utilitis.get_default_path(), name)
        else:
            new_path = path + "/" + name
            utilitis.create_path(utilitis.get_full_path(path))

        txml_out.save_teaser_xml(new_path, self)

    def load_project(self, path):
        '''Loads the project from a teaserXML file (new format)

        calls the function load_teaser_xml in data.TeaserXML.py

        Parameters
        ----------
        path : string
            full path to a teaserXML file

        '''

        txml_in.load_teaser_xml(path, self)


    def save_citygml(self, file_name=None, path=None):
        '''Saves the project to a citygml file

        calls the function save_gml in data.CityGML we make use of CityGML core
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
            new_path = os.path.join(utilitis.get_default_path(), name)
        else:
            new_path = path + "/" + name
            utilitis.create_path(utilitis.get_full_path(path))

        citygml_out.save_gml(self, new_path)

    def load_citygml(self,
                     path=None):
        '''Loads buildings from a citygml file

        calls the function load_gml in data.CityGML we make use of CityGML core
        and possibly not all kinds of CityGML modelling techniques are
        supported.

        If the fucntion of the building is given as Residential (1000) or
        Office (1120) the importer directly converts the building to
        archetype buildings. If not only the citygml geometry is imported and
        you need take care of either the material properties and zoning or you
        may use the _convert_bldg fucntion in citygml_input module. 


        Parameters
        ----------

        path : string
            full path to a CityGML file

        '''

        citygml_in.load_gml(path, self)

    def export_aixlib(self,
                      building_model="None",
                      zone_model="None",
                      corG=None,
                      internal_id=None,
                      path=None):
        """Exports values to a record file for Modelica simulation

        Parameters
        ----------

        building_model : string
            setter of the used Aixlib building model (None, MultizoneEquipped,
            Multizone)
        zone_model : string
            setter of the used Aixlib zone model (ThermalZoneEquipped,
            ThermalZone)
        corG : boolean
            setter of the used g value calculation in the model
        internal_id : float
            setter of the used building which will be exported, if None then
            all buildings will be exported
        path : string
            if the Files should not be stored in OutputData, an alternative
            path can be specified as a full and absolute path
        """

        if path is None:
            path = utilitis.get_default_path() + "/" + self.name
        else:
            path = path + "/" + self.name

        utilitis.create_path(path)

        aixlib_output.export_aixlib(prj=self,
                                    building_model=building_model,
                                    zone_model=zone_model,
                                    corG=corG,
                                    internal_id=internal_id,
                                    path=path)

    def export_annex(self,
                     internal_id=None,
                     path=None):
        """Exports values to a record file for Modelica simulation

        Parameters
        ----------

        internal_id : float
            setter of the used building which will be exported, if None then
            all buildings will be exported
        path : string
            if the Files should not be stored in OutputData, an alternative
            path can be specified as a full and absolute path
        """

        if path is None:
            path = utilitis.get_default_path() + "/" + self.name
        else:
            path = path + "/" + self.name

        utilitis.create_path(path)

        annex60_output.export_annex60(prj=self,
                                      number_of_elements=self.number_of_elements_calc,
                                      merge_windows=self.merge_windows_calc,
                                      internal_id=internal_id,
                                      path=path)

    def export_parameters_txt(self, path=None):
        '''Exports parameters of all buildings in a readable text file

        Parameters
        ----------

        path : string
            if the Files should not be stored in OutputData, an alternative
            can be specified
        '''

        if path is None:
            path = os.path.join(utilitis.get_default_path(), self.name)
        else:
            path = path+"/"+self.name

        text_out.export_parameters_txt(prj=self,
                                       path=path)

    def set_default(self):
        '''sets all attributes except self.data to default
        '''

        self.name = "Project"

        self.modelica_project = self.name
        self.weather_file_header = "wetter"
        self.weather_file_path = "modelica://AixLib/Resources/WeatherData/" \
                                 "TRY2010_12_Jahr_Modelica-Library.txt"
        self.buildings = []
        self._number_of_elements_calc = 2
        self._merge_windows_calc = False
        self._used_library_calc = "AixLib"


        self._type_element_file = None

    @property
    def type_element_file(self):
        return self._type_element_file

    @type_element_file.setter
    def type_element_file(self, value):
        self._type_element_file = value
        self.instantiate_data_class(value)

    @property
    def number_of_elements_calc(self):
        return self._number_of_elements_calc

    @number_of_elements_calc.setter
    def number_of_elements_calc(self, value):

        ass_error_1 = "calculation_method has to be 1,2,3 or 4"

        assert value != [1, 2, 3, 4], ass_error_1

        self._number_of_elements_calc = value

        for bldg in self.buildings:
            bldg.number_of_elements_calc = value

    @property
    def merge_windows_calc(self):
        return self._merge_windows_calc

    @merge_windows_calc.setter
    def merge_windows_calc(self, value):

        ass_error_1 = "merge windows needs to be True or False"

        assert value != [True, False], ass_error_1

        self._merge_windows_calc = value

        for bldg in self.buildings:
            bldg.merge_windows_calc = value

    @property
    def used_library_calc(self):
        return self._used_library_calc

    @used_library_calc.setter
    def used_library_calc(self, value):

        ass_error_1 = "used library needs to be AixLib or Annex60"

        assert value != ["AixLib", "Annex60"], ass_error_1

        self._used_library_calc = value

        for bldg in self.buildings:
            bldg.used_library_calc = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):

        self._name = value
        self.modelica_project = value
