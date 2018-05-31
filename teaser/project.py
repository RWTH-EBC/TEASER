# created June 2015
# by TEASER4 Development Team

"""This module includes the Project class, which is the API for TEASER.
"""

import warnings
import os
import re
import teaser.logic.utilities as utilities
import teaser.data.input.teaserxml_input as txml_in
import teaser.data.output.teaserxml_output as txml_out
import teaser.data.output.aixlib_output as aixlib_output
import teaser.data.output.ibpsa_output as ibpsa_output
import teaser.data.output.text_output as text_out
from teaser.data.dataclass import DataClass
from teaser.logic.archetypebuildings.bmvbs.office import Office
from teaser.logic.archetypebuildings.bmvbs.custom.institute import Institute
from teaser.logic.archetypebuildings.bmvbs.custom.institute4 import Institute4
from teaser.logic.archetypebuildings.bmvbs.custom.institute8 import Institute8
from teaser.logic.archetypebuildings.urbanrenet.est1a import EST1a
from teaser.logic.archetypebuildings.urbanrenet.est1b import EST1b
from teaser.logic.archetypebuildings.urbanrenet.est2 import EST2
from teaser.logic.archetypebuildings.urbanrenet.est3 import EST3
from teaser.logic.archetypebuildings.urbanrenet.est4a import EST4a
from teaser.logic.archetypebuildings.urbanrenet.est4b import EST4b
from teaser.logic.archetypebuildings.urbanrenet.est5 import EST5
from teaser.logic.archetypebuildings.urbanrenet.est6 import EST6
from teaser.logic.archetypebuildings.urbanrenet.est7 import EST7
from teaser.logic.archetypebuildings.urbanrenet.est8a import EST8a
from teaser.logic.archetypebuildings.urbanrenet.est8b import EST8b
from teaser.logic.archetypebuildings.tabula.de.singlefamilyhouse import \
    SingleFamilyHouse
from teaser.logic.archetypebuildings.tabula.de.terracedhouse import \
    TerracedHouse
from teaser.logic.archetypebuildings.tabula.de.multifamilyhouse import \
    MultiFamilyHouse
from teaser.logic.archetypebuildings.tabula.de.apartmentblock import \
    ApartmentBlock
from teaser.logic.archetypebuildings.bmvbs.singlefamilydwelling import \
    SingleFamilyDwelling
from teaser.logic.simulation.modelicainfo import ModelicaInfo
import teaser.data.output.citygml_output as citygml_out
import teaser.data.input.citygml_input as citygml_in


class Project(object):
    """Top class for TEASER projects it serves as an API

    The Project class is the top class for all TEASER projects and serves as an
    API for script based interface. It is highly recommended to always
    instantiate the Project class before starting to work with TEASER. It
    contains functions to generate archetype buildings, to export models and to
    save information for later use.

    Parameters
    ----------
    load_data : boolean
        boolean if data bases for materials, type elements and use conditions
        should be loaded. default = False but will be automatically loaded
        once you add a archetype building. For building generation from
        scratch, set to True

    Attributes
    ----------

    name : str
        Name of the Project (default is 'Project')
    modelica_info : instance of ModelicaInfo
        TEASER instance of ModelicaInfo to store Modelica related
        information, like used compiler, runtime, etc.
    buildings : list
        List of all buildings in one project, instances of Building()
    data : instance of DataClass
        TEASER instance of DataClass containing XML binding classes
    weather_file_path : str
        Absolute path to weather file used for Modelica simulation. Default
        weather file can be find in inputdata/weatherdata.
    number_of_elements_calc : int
        Defines the number of elements, that are aggregated (1, 2, 3 or 4),
        default is 2
    merge_windows_calc : bool
        True for merging the windows into the outer walls, False for
        separate resistance for window, default is False (only supported for
        IBPSA)
    used_library_calc : str
        used library (AixLib and IBPSA are supported)
    """

    def __init__(self, load_data=False):
        """Constructor of Project Class.
        """
        self._name = "Project"
        self.modelica_info = ModelicaInfo()

        self.weather_file_path = utilities.get_full_path(
            os.path.join(
                "data",
                "input",
                "inputdata",
                "weatherdata",
                "DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos"))

        self.buildings = []

        self.load_data = load_data

        self._number_of_elements_calc = 2
        self._merge_windows_calc = False
        self._used_library_calc = "AixLib"

        if load_data is True:
            self.data = self.instantiate_data_class()
        else:
            self.data = None

    @staticmethod
    def instantiate_data_class():
        """Initialization of DataClass

        Returns
        ----------

        DataClass : Instance of DataClass()

        """
        return DataClass()

    def calc_all_buildings(self, raise_errors=False):
        """Calculates values for all project buildings

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
            used library (AixLib and IBPSA are supported)

        """
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
                except (ZeroDivisionError, TypeError):
                    warnings.warn(
                        "Following building can't be calculated and is "
                        "removed from buildings list. Use raise_errors=True "
                        "to get python errors and stop TEASER from deleting "
                        "this building:" + bldg.name)
                    self.buildings.remove(bldg)

    def retrofit_all_buildings(
            self,
            year_of_retrofit=None,
            type_of_retrofit=None,
            window_type=None,
            material=None):
        """Retrofits all buildings in the project.

        Depending on the used Archetype approach this function will retrofit
        the building. If you have archetypes of both typologies (tabula and
        iwu/BMBVS) you need to pass all keywords (see also Parameters section).

        If TABULA approach is used, it will replace the current construction
        with the construction specified in 'type_of_retrofit',
        where 'retrofit' and 'adv_retrofit' are allowed.

        'iwu' or 'BMVBS' Buildings in the project are retrofitted in the
        following manner:

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
            the year the buildings are retrofitted, only 'iwu'/'bmbvs'
            archetype approach.
        type_of_retrofit : str
            The classification of retrofit, if the archetype building
            approach of TABULA is used.
        window_type : str
            Default: EnEv 2014, only 'iwu'/'bmbvs' archetype approach.
        material : str
            Default: EPS035, only 'iwu'/'bmbvs' archetype approach.

        """
        ass_error_type = "only 'retrofit' and 'adv_retrofit' are valid "
        assert type_of_retrofit in [None, 'adv_retrofit', 'retrofit'], \
            ass_error_type
        tabula_buildings = []
        iwu_buildings = []

        for bldg in self.buildings:
            if isinstance(bldg, SingleFamilyHouse):
                if type_of_retrofit is None:
                    raise ValueError("you need to set type_of_retrofit for "
                                     "TABULA retrofit")
                tabula_buildings.append(bldg)
            else:
                if year_of_retrofit is None:
                    raise ValueError("you need to set year_of_retrofit for "
                                     "retrofit")
                iwu_buildings.append(bldg)

        if self.data.used_statistic == 'iwu':
            for bld_iwu in iwu_buildings:
                bld_iwu.retrofit_building(
                    year_of_retrofit=year_of_retrofit,
                    window_type=window_type,
                    material=material)
            self.data = DataClass(used_statistic='tabula_de')
            for bld_tabula in tabula_buildings:
                bld_tabula.retrofit_building(
                    type_of_retrofit=type_of_retrofit)

        else:
            for bld_tabula in tabula_buildings:
                bld_tabula.retrofit_building(
                    type_of_retrofit=type_of_retrofit)
            self.data = DataClass(used_statistic='iwu')
            for bld_iwu in iwu_buildings:
                bld_iwu.retrofit_building(
                    year_of_retrofit=year_of_retrofit,
                    window_type=window_type,
                    material=material)

    def add_non_residential(
            self,
            method,
            usage,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu=True,
            office_layout=None,
            window_layout=None,
            construction_type=None):
        """Add a non-residential building to the TEASER project.

        This function adds a non-residential archetype building to the TEASER
        project. You need to specify the method of the archetype generation.
        Currently TEASER supports only method according to Lichtmess and BMVBS
        for non-residential buildings. Further the type of usage needs to be
        specified. Currently TEASER supports four different types of
        non-residential buildings ('office', 'institute', 'institute4',
        'institute8'). For more information on specific archetype buildings and
        methods, please read the docs of archetype classes.

        This function also calculates the parameters of the buildings directly
        with the settings set in the project (e.g. used_library_calc or
        number_of_elements_calc).

        Parameters
        ----------
        method : str
            Used archetype method, currently only 'bmvbs' is supported
        usage : str
            Main usage of the obtained building, currently only 'office',
            'institute', 'institute4', institute8' are supported
        name : str
            Individual name
        year_of_construction : int
            Year of first construction
        height_of_floors : float [m]
            Average height of the buildings' floors
        number_of_floors : int
            Number of building's floors above ground
        net_leased_area : float [m2]
            Total net leased area of building. This is area is NOT the
            footprint
            of a building
        with_ahu : Boolean
            If set to True, an empty instance of BuildingAHU is instantiated
            and
            assigned to attribute central_ahu. This instance holds information
            for central Air Handling units. Default is False.
        office_layout : int
            Structure of the floor plan of office buildings, default is 1,
            which is representative for one elongated floor.
                1: elongated 1 floor
                2: elongated 2 floors
                3: compact (e.g. for a square base building)
        window_layout : int
            Structure of the window facade type, default is 1, which is
            representative for a punctuated facade.
                1: punctuated facade (individual windows)
                2: banner facade (continuous windows)
                3: full glazing
        construction_type : str
            Construction type of used wall constructions default is "heavy")
                heavy: heavy construction
                light: light construction

        Returns
        ----------
        type_bldg : Instance of Office()

        """
        ass_error_method = "only 'bmvbs' is a valid method for " \
                           "non-residential archetype generation"

        assert method in ['bmvbs'], ass_error_method

        ass_error_usage = "only 'office', 'institute', 'institute4', " \
                          "'institute8' are valid usages for archetype " \
                          "generation"

        assert usage in ['office', 'institute', 'institute4',
                         'institute8'], ass_error_usage

        if self.data is None:
            self.data = DataClass(used_statistic='iwu')
        elif self.data.used_statistic != 'iwu':
            self.data = DataClass(used_statistic='iwu')

        if usage == 'office':

            type_bldg = Office(
                self,
                name,
                year_of_construction,
                number_of_floors,
                height_of_floors,
                net_leased_area,
                with_ahu,
                office_layout,
                window_layout,
                construction_type)

        elif usage == 'institute':

            type_bldg = Institute(
                self,
                name,
                year_of_construction,
                number_of_floors,
                height_of_floors,
                net_leased_area,
                with_ahu,
                office_layout,
                window_layout,
                construction_type)

        elif usage == 'institute4':

            type_bldg = Institute4(
                self,
                name,
                year_of_construction,
                number_of_floors,
                height_of_floors,
                net_leased_area,
                with_ahu,
                office_layout,
                window_layout,
                construction_type)

        elif usage == 'institute8':

            type_bldg = Institute8(
                self,
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

    def add_residential(
            self,
            method,
            usage,
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
            construction_type=None,
            number_of_apartments=None):
        """Add a residential building to the TEASER project.

        This function adds a residential archetype building to the TEASER
        project. You need to specify the method of the archetype generation.
        Currently TEASER supports only method according 'iwu' and 'urbanrenet'
        for residential buildings ('tabula_de' to follow soon). Further the
        type
        of usage needs to be specified. Currently TEASER supports one type of
        residential building for 'iwu' and eleven types for 'urbanrenet'. For
        more information on specific archetype buildings and methods, please
        read the docs of archetype classes.
        This function also calculates the parameters of the buildings directly
        with the settings set in the project (e.g. used_library_calc or
        number_of_elements_calc).

        Parameters
        ----------
        method : str
            Used archetype method, currently only 'iwu' or 'urbanrenet' are
            supported, 'tabula_de' to follow soon
        usage : str
            Main usage of the obtained building, currently only
            'single_family_dwelling' is supported for iwu and 'est1a', 'est1b',
            'est2', 'est3', 'est4a', 'est4b', 'est5' 'est6', 'est7', 'est8a',
            'est8b' for urbanrenet.
        name : str
            Individual name
        year_of_construction : int
            Year of first construction
        height_of_floors : float [m]
            Average height of the buildings' floors
        number_of_floors : int
            Number of building's floors above ground
        net_leased_area : float [m2]
            Total net leased area of building. This is area is NOT the
            footprint
            of a building
        with_ahu : Boolean
            If set to True, an empty instance of BuildingAHU is instantiated
            and
            assigned to attribute central_ahu. This instance holds information
            for central Air Handling units. Default is False.
        residential_layout : int
            Structure of floor plan (default = 0) CAUTION only used for iwu
                0: compact
                1: elongated/complex
        neighbour_buildings : int
            Number of neighbour buildings. CAUTION: this will not change
            the orientation of the buildings wall, but just the overall
            exterior wall and window area(!) (default = 0)
                0: no neighbour
                1: one neighbour
                2: two neighbours
        attic : int
            Design of the attic. CAUTION: this will not change the orientation
            or tilt of the roof instances, but just adapt the roof area(!) (
            default = 0) CAUTION only used for iwu
                0: flat roof
                1: non heated attic
                2: partly heated attic
                3: heated attic
        cellar : int
            Design of the of cellar CAUTION: this will not change the
            orientation, tilt of GroundFloor instances, nor the number or area
            of ThermalZones, but will change GroundFloor area(!) (default = 0)
            CAUTION only used for iwu
                0: no cellar
                1: non heated cellar
                2: partly heated cellar
                3: heated cellar
        dormer : str
            Is a dormer attached to the roof? CAUTION: this will not
            change roof or window orientation or tilt, but just adapt the roof
            area(!) (default = 0) CAUTION only used for iwu
                0: no dormer
                1: dormer
        construction_type : str
            Construction type of used wall constructions default is "heavy")
                heavy: heavy construction
                light: light construction
        number_of_apartments : int
            number of apartments inside Building (default = 1). CAUTION only
            used for urbanrenet

        Returns
        ----------
        type_bldg : Instance of Archetype Building

        """
        ass_error_method = "only'tabula_de', 'iwu' and 'urbanrenet' " \
                           "are valid methods for residential archetype " \
                           "generation"

        assert method in ['tabula_de', 'iwu', 'urbanrenet'], ass_error_method

        ass_error_apart = (
            "The keyword number_of_apartments does not have any "
            "effect on archetype generation for 'iwu' or"
            "'tabula_de', see docs for more information")

        if method in ['iwu', 'tabula_de'] and number_of_apartments is not None:
            warnings.warn(ass_error_apart)

        if method == 'tabula_de':

            if self.data is None:
                self.data = DataClass(used_statistic=method)
            elif self.data.used_statistic != 'tabula_de':
                self.data = DataClass(used_statistic=method)

            ass_error_usage_tabula = "only 'single_family_house',"
            "'terraced_house', 'multi_family_house', 'apartment_block' are"
            "valid usages for iwu archetype method"
            assert usage in ['single_family_house', 'terraced_house',
                             'multi_family_house', 'apartment_block'], \
                ass_error_usage_tabula

            if usage == 'single_family_house':

                type_bldg = SingleFamilyHouse(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    construction_type)
                type_bldg.generate_archetype()
                return type_bldg

            elif usage == 'terraced_house':

                type_bldg = TerracedHouse(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    construction_type)
                type_bldg.generate_archetype()
                return type_bldg

            elif usage == 'multi_family_house':

                type_bldg = MultiFamilyHouse(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    construction_type)
                type_bldg.generate_archetype()
                return type_bldg

            elif usage == 'apartment_block':

                type_bldg = ApartmentBlock(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    construction_type)

                type_bldg.generate_archetype()
                return type_bldg

        elif method == 'iwu':

            if self.data is None:
                self.data = DataClass(used_statistic=method)
            elif self.data.used_statistic != 'iwu':
                self.data = DataClass(used_statistic=method)

            ass_error_usage_iwu = "only 'single_family_dwelling' is a valid " \
                                  "usage for iwu archetype method"
            assert usage in ['single_family_dwelling'], ass_error_usage_iwu

            if usage == 'single_family_dwelling':

                type_bldg = SingleFamilyDwelling(
                    self,
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

        elif method == 'urbanrenet':

            if self.data is None:
                self.data = DataClass(used_statistic='iwu')
            elif self.data.used_statistic != 'iwu':
                self.data = DataClass(used_statistic='iwu')

            ass_error_usage_urn = "only 'est1a', 'est1b', 'est2', 'est3', " \
                                  "'est4a', 'est4b', 'est5' 'est6', 'est7', " \
                                  "'est8a','est8b' is are valid usages for " \
                                  "urbanrenet archetype method"
            assert usage in ['est1a', 'est1b', 'est2', 'est3', 'est4a',
                             'est4b', 'est5', 'est6', 'est7', 'est8a',
                             'est8b'], ass_error_usage_urn
            if usage == 'est1a':

                type_bldg = EST1a(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    neighbour_buildings,
                    construction_type)

            elif usage == 'est1b':

                type_bldg = EST1b(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    neighbour_buildings,
                    construction_type,
                    number_of_apartments)

            elif usage == 'est2':

                type_bldg = EST2(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    neighbour_buildings,
                    construction_type,
                    number_of_apartments)

            elif usage == 'est3':

                type_bldg = EST3(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    neighbour_buildings,
                    construction_type,
                    number_of_apartments)

            elif usage == 'est4a':

                type_bldg = EST4a(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    neighbour_buildings,
                    construction_type,
                    number_of_apartments)

            elif usage == 'est4b':

                type_bldg = EST4b(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    neighbour_buildings,
                    construction_type,
                    number_of_apartments)

            elif usage == 'est5':

                type_bldg = EST5(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    neighbour_buildings,
                    construction_type,
                    number_of_apartments)

            elif usage == 'est6':

                type_bldg = EST6(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    neighbour_buildings,
                    construction_type,
                    number_of_apartments)

            elif usage == 'est7':

                type_bldg = EST7(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    neighbour_buildings,
                    construction_type,
                    number_of_apartments)

            elif usage == 'est8a':

                type_bldg = EST8a(
                    self,
                    name,
                    year_of_construction,
                    number_of_floors,
                    height_of_floors,
                    net_leased_area,
                    with_ahu,
                    neighbour_buildings,
                    construction_type,
                    number_of_apartments)

            elif usage == 'est8b':

                type_bldg = EST8b(
                    self,
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

    def type_bldg_office(
            self,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu=True,
            office_layout=None,
            window_layout=None,
            construction_type=None):
        """Old function, consider rewriting your code

        This is an old function for archetype generation, consider rewriting
        your code to use Project.add_non_residential(). This function will be
        eliminated within the next versions
        """

        warnings.warn("You are using an old function for archetype "
                      "generation, consider rewriting you code to use "
                      "Project.add_non_residential(). This function will be "
                      "eliminated within the next versions")

        type_bldg = Office(
            self,
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

    def type_bldg_institute(
            self,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu=True,
            office_layout=None,
            window_layout=None,
            construction_type=None):
        """Old function, consider rewriting your code

        This is an old function for archetype generation, consider rewriting
        your code to use Project.add_non_residential(). This function will be
        eliminated within the next versions
        """

        warnings.warn("You are using an old function for archetype "
                      "generation, consider rewriting you code to use "
                      "Project.add_non_residential(). This function will be "
                      "eliminated within the next versions")
        type_bldg = Institute(
            self,
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

    def type_bldg_institute4(
            self,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu=True,
            office_layout=None,
            window_layout=None,
            construction_type=None):
        """Old function, consider rewriting your code

        This is an old function for archetype generation, consider rewriting
        your code to use Project.add_non_residential(). This function will be
        eliminated within the next versions
        """

        warnings.warn("You are using an old function for archetype "
                      "generation, consider rewriting you code to use "
                      "Project.add_non_residential(). This function will be "
                      "eliminated within the next versions")

        type_bldg = Institute4(
            self,
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

    def type_bldg_institute8(
            self,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu=True,
            office_layout=None,
            window_layout=None,
            construction_type=None):
        """Old function, consider rewriting your code

        This is an old function for archetype generation, consider rewriting
        your code to use Project.add_non_residential(). This function will be
        eliminated within the next versions
        """

        warnings.warn("You are using an old function for archetype "
                      "generation, consider rewriting you code to use "
                      "Project.add_non_residential(). This function will be "
                      "eliminated within the next versions")
        type_bldg = Institute8(
            self,
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

    def type_bldg_est1a(
            self,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu=False,
            neighbour_buildings=None,
            construction_type=None):
        """Old function, consider rewriting your code

        This is an old function for archetype generation, consider rewriting
        your code to use Project.add_non_residential(). This function will be
        eliminated within the next versions
        """

        warnings.warn("You are using an old function for archetype "
                      "generation, consider rewriting you code to use "
                      "Project.add_non_residential(). This function will be "
                      "eliminated within the next versions")

        type_bldg = EST1a(
            self,
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

    def type_bldg_est1b(
            self,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu=False,
            neighbour_buildings=None,
            construction_type=None,
            number_of_apartments=None):
        """Old function, consider rewriting your code

        This is an old function for archetype generation, consider rewriting
        your code to use Project.add_non_residential(). This function will be
        eliminated within the next versions
        """

        warnings.warn("You are using an old function for archetype "
                      "generation, consider rewriting you code to use "
                      "Project.add_non_residential(). This function will be "
                      "eliminated within the next versions")

        type_bldg = EST1b(
            self,
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

    def type_bldg_est4b(
            self,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu=False,
            neighbour_buildings=None,
            construction_type=None,
            number_of_apartments=None):
        """Old function, consider rewriting your code

        This is an old function for archetype generation, consider rewriting
        your code to use Project.add_non_residential(). This function will be
        eliminated within the next versions
        """

        warnings.warn("You are using an old function for archetype "
                      "generation, consider rewriting you code to use "
                      "Project.add_non_residential(). This function will be "
                      "eliminated within the next versions")

        type_bldg = EST4b(
            self,
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

    def type_bldg_est7(
            self,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu=False,
            neighbour_buildings=None,
            construction_type=None,
            number_of_apartments=None):
        """Old function, consider rewriting your code

        This is an old function for archetype generation, consider rewriting
        your code to use Project.add_non_residential(). This function will be
        eliminated within the next versions
        """

        warnings.warn("You are using an old function for archetype "
                      "generation, consider rewriting you code to use "
                      "Project.add_non_residential(). This function will be "
                      "eliminated within the next versions")

        type_bldg = EST7(
            self,
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

    def type_bldg_residential(
            self,
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
        """Old function, consider rewriting your code

        This is an old function for archetype generation, consider rewriting
        your code to use Project.add_non_residential(). This function will be
        eliminated within the next versions
        """

        warnings.warn("You are using an old function for archetype "
                      "generation, consider rewriting you code to use "
                      "Project.add_residential(). This function will be "
                      "eliminated within the next versions")

        type_bldg = SingleFamilyDwelling(
            self,
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
        """Saves the project to a tXML file

        calls the function save_teaser_xml in data.TeaserXML.py

        Parameters
        ----------

        file_name : string
            name of the new file
        path : string
            if the Files should not be stored in OutputData, an alternative
            can be specified
        """
        if file_name is None:
            name = self.name
        else:
            name = file_name

        if path is None:
            new_path = os.path.join(utilities.get_default_path(), name)
        else:
            new_path = os.path.join(path, name)

        txml_out.save_teaser_xml(new_path, self)

    def load_project(self, path):
        """Loads the project from a teaserXML file (new format)

        calls the function load_teaser_xml in data.TeaserXML.py

        Parameters
        ----------
        path : string
            full path to a teaserXML file

        """

        txml_in.load_teaser_xml(path, self)

    def save_citygml(self, file_name=None, path=None):
        """Saves the project to a CityGML file

        calls the function save_gml in data.CityGML we make use of CityGML core
        and EnergyADE to store semantic information


        Parameters
        ----------

        file_name : string
            name of the new file
        path : string
            if the Files should not be stored in OutputData, an alternative
            can be specified

        """
        if file_name is None:
            name = self.name
        else:
            name = file_name

        if path is None:
            new_path = os.path.join(utilities.get_default_path(), name)
        else:
            new_path = os.path.join(path, name)
            utilities.create_path(utilities.get_full_path(path))

        citygml_out.save_gml(self, new_path)

    def load_citygml(self, path=None):
        """Loads buildings from a citygml file

        calls the function load_gml in data.CityGML we make use of CityGML core
        and possibly not all kinds of CityGML modelling techniques are
        supported.

        If the function of the building is given as Residential (1000) or
        Office (1120) the importer directly converts the building to
        archetype buildings. If not, only the citygml geometry is imported and
        you need take care of either the material properties and zoning or you
        may use the _convert_bldg function in citygml_input module.


        Parameters
        ----------

        path : string
            full path to a CityGML file

        """

        citygml_in.load_gml(path, self)

    def export_aixlib(
            self,
            building_model=None,
            zone_model=None,
            corG=None,
            internal_id=None,
            path=None):
        """Exports values to a record file for Modelica simulation

        Exports one (if internal_id is not None) or all buildings for
        AixLib.ThermalZones.ReducedOrder.Multizone.MultizoneEquipped models
        using the ThermalZoneEquipped model with a correction of g-value (
        double pane glazing) and supporting models, like tables and weather
        model. In contrast to versions < 0.5 TEASER now does not
        support any model options, as we observed no need, since single
        ThermalZones are identically with IBPSA models. If you miss one of
        the old options please contact us.

        Parameters
        ----------

        internal_id : float
            setter of a specific building which will be exported, if None then
            all buildings will be exported
        path : string
            if the Files should not be stored in default output path of TEASER,
            an alternative path can be specified as a full path
        """

        if building_model is not None or zone_model is not None or corG is \
                not None:

            warnings.warn("building_model, zone_model and corG are no longer "
                          "supported for AixLib export and have no effect. "
                          "The keywords will be deleted within the next "
                          "version, consider rewriting your code.")

        if path is None:
            path = os.path.join(
                utilities.get_default_path(),
                self.name)
        else:
            path = os.path.join(
                path,
                self.name)

        utilities.create_path(path)

        if internal_id is None:
            aixlib_output.export_multizone(
                buildings=self.buildings,
                prj=self,
                path=path)
        else:
            for bldg in self.buildings:
                if bldg.internal_id == internal_id:
                    aixlib_output.export_multizone(
                        buildings=[bldg],
                        prj=self,
                        path=path)
        return path

    def export_ibpsa(
            self,
            library='AixLib',
            internal_id=None,
            path=None):
        """Exports values to a record file for Modelica simulation

        For Annex 60 Library

        Parameters
        ----------

        library : str
            Used library within the framework of IBPSA library. The
            models are identical in each library, but IBPSA Modelica library is
            just a core set of models and should not be used standalone.
            Valid values are 'AixLib' (default), 'Buildings',
            'BuildingSystems' and 'IDEAS'.
        internal_id : float
            setter of a specific building which will be exported, if None then
            all buildings will be exported
        path : string
            if the Files should not be stored in default output path of TEASER,
            an alternative path can be specified as a full path
        """

        ass_error_1 = "library for IBPSA export has to be 'AixLib', " \
                      "'Buildings', 'BuildingSystems' or 'IDEAS'"

        assert library in ['AixLib', 'Buildings', 'BuildingSystems',
                           'IDEAS'], ass_error_1

        if path is None:
            path = os.path.join(
                utilities.get_default_path(),
                self.name)
        else:
            path = os.path.join(
                path,
                self.name)

        utilities.create_path(path)

        if internal_id is None:
            ibpsa_output.export_ibpsa(
                buildings=self.buildings,
                prj=self,
                path=path,
                library=library)
        else:
            for bldg in self.buildings:
                if bldg.internal_id == internal_id:
                    ibpsa_output.export_ibpsa(
                        buildings=[bldg],
                        prj=self,
                        path=path)
        return path

    def export_parameters_txt(self, path=None):
        """Exports parameters of all buildings in a readable text file

        Parameters
        ----------

        path : string
            if the Files should not be stored in OutputData, an alternative
            can be specified
        """

        if path is None:
            path = os.path.join(
                utilities.get_default_path(),
                self.name)
        else:
            path = os.path.join(
                path,
                self.name)

        text_out.export_parameters_txt(
            prj=self,
            path=path)
        return path

    def set_default(self, load_data=None):
        """Sets all attributes to default

        Caution: this will delete all buildings.

        Parameters
        ----------
        load_data : boolean, None-type
            boolean if data bindings for type elements and use conditions
            should be loaded (default = True), in addition it could be a None-
            type to use the already used data bindings
        """

        self._name = "Project"
        self.modelica_info = ModelicaInfo()

        self.weather_file_path = utilities.get_full_path(
            os.path.join(
                "data",
                "input",
                "inputdata",
                "weatherdata",
                "DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos"))

        self.buildings = []

        self.load_data = load_data

        self._number_of_elements_calc = 2
        self._merge_windows_calc = False
        self._used_library_calc = "AixLib"

        if load_data is True:
            self.data = self.instantiate_data_class()
        elif not load_data:
            pass
        else:
            self.data = None

        self.name = "Project"

        self.weather_file_header = "wetter"
        self.weather_file_path = "modelica://AixLib/Resources/WeatherData/" \
                                 "TRY2010_12_Jahr_Modelica-Library.txt"
        self.buildings = []
        self._number_of_elements_calc = 2
        self._merge_windows_calc = False
        self._used_library_calc = "AixLib"

    @property
    def number_of_elements_calc(self):
        return self._number_of_elements_calc

    @number_of_elements_calc.setter
    def number_of_elements_calc(self, value):

        ass_error_1 = "number_of_elements_calc has to be 1,2,3 or 4"

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

        ass_error_1 = "used library needs to be AixLib or IBPSA"

        assert value != ["AixLib", "IBPSA"], ass_error_1

        self._used_library_calc = value

        for bldg in self.buildings:
            bldg.used_library_calc = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            regex = re.compile('[^a-zA-z0-9]')
            self._name = regex.sub('', value)
        else:
            try:
                value = str(value)
                regex = re.compile('[^a-zA-z0-9]')
                self._name = regex.sub('', value)
            except ValueError:
                print("Can't convert name to string")

        if self._name[0].isdigit():
            self._name = "P" + self._name
