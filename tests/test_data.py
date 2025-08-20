"""
Created July 2015

@author: TEASER 4 Development Team
"""
from teaser.logic import utilities
from teaser.logic.buildingobjects.calculation.four_element import FourElement
from teaser.logic.buildingobjects.calculation.three_element import ThreeElement
from teaser.logic.buildingobjects.calculation.two_element import TwoElement
from teaser.project import Project
from teaser.data.utilities import ConstructionData
from teaser.data.dataclass import DataClass
from teaser.logic.buildingobjects.buildingphysics.interzonalfloor \
    import InterzonalFloor
from teaser.logic.buildingobjects.buildingphysics.interzonalceiling \
    import InterzonalCeiling
from teaser.logic.buildingobjects.buildingphysics.interzonalwall \
    import InterzonalWall
import math
import os
import helptest
from pytest import approx

prj = Project(False)
prj.data = DataClass(construction_data=ConstructionData.iwu_heavy)


class Test_teaser(object):
    """Unit Tests for TEASER"""

    global prj

    def test_calc_vdi_room1(self):
        """Parameter Verification for rouvel room1"""
        import teaser.examples.verification.verification_VDI_6007_room1 as room1

        room1_prj = room1.parameter_room1()
        zone_attr = room1_prj.buildings[0].thermal_zones[0].model_attr

        # parameters inner wall Typraum S

        assert round(zone_attr.r1_iw, 13) == 0.0005956934075
        assert round(zone_attr.c1_iw / 1000, 7) == 14836.3546282
        assert round(zone_attr.area_iw, 1) == 75.5
        assert round(zone_attr.alpha_conv_inner_iw, 13) == 2.23642384105960

        # paremeters outer wall Typraum S
        r_rest = zone_attr.r_rest_ow + 1 / (
            zone_attr.alpha_comb_outer_ow * zone_attr.area_ow
        )
        assert round(r_rest, 13) == 0.0427687193786
        assert round(zone_attr.r1_ow, 13) == 0.0043679129367
        assert round(zone_attr.c1_ow / 1000, 7) == 1600.8489399
        assert round(zone_attr.area_ow, 1) == 3.5
        assert round(zone_attr.area_win, 1) == 7.0
        assert round(zone_attr.alpha_conv_inner_ow, 1) == 2.7
        assert round(zone_attr.alpha_comb_outer_ow, 1) == 25.0

    def test_calc_vdi_room3(self):
        """Parameter Verification for room 3"""
        import teaser.examples.verification.verification_VDI_6007_room3 as room3

        room3_prj = room3.parameter_room3()
        zone_attr = room3_prj.buildings[0].thermal_zones[0].model_attr

        # parameters inner wall Typraum L

        assert round(zone_attr.r1_iw, 13) == 0.003385649748
        assert round(zone_attr.c1_iw / 1000, 7) == 7445.3648976
        assert round(zone_attr.area_iw, 1) == 75.5
        assert round(zone_attr.alpha_conv_inner_iw, 13) == 2.23642384105960

        # parameters outer wall Typraum L
        r_rest = zone_attr.r_rest_ow + 1 / (
            zone_attr.alpha_comb_outer_ow * zone_attr.area_ow
        )
        assert round(r_rest, 13) == 0.0431403889233
        assert round(zone_attr.r1_ow, 13) == 0.004049351608
        assert round(zone_attr.c1_ow / 1000, 7) == 47.8617641
        assert round(zone_attr.area_ow, 1) == 3.5
        assert round(zone_attr.area_win, 1) == 7.0
        assert round(zone_attr.alpha_conv_inner_ow, 1) == 2.7
        assert round(zone_attr.alpha_comb_outer_ow, 1) == 25.0

    def test_calc_vdi_room8(self):
        """Parameter Verification for room 8"""
        import teaser.examples.verification.verification_VDI_6007_room8 as room8

        room8_prj = room8.parameter_room8()
        zone_attr = room8_prj.buildings[0].thermal_zones[0].model_attr

        assert round(zone_attr.r1_iw, 13) == 0.0006688956391
        assert round(zone_attr.c1_iw / 1000, 7) == 12391.3638631
        assert round(zone_attr.area_iw, 1) == 60.5
        assert round(zone_attr.alpha_conv_inner_iw, 13) == 2.1214876033058
        r_rest = zone_attr.r_rest_ow + 1 / (
            zone_attr.alpha_comb_outer_ow * zone_attr.area_ow
        )
        assert round(r_rest, 13) == 0.0207059264866
        assert round(zone_attr.r1_ow, 13) == 0.0017362530106
        assert round(zone_attr.c1_ow / 1000, 7) == 5259.932231
        assert round(zone_attr.area_ow, 1) == 11.5
        assert round(zone_attr.area_win, 1) == 14.0
        assert round(zone_attr.alpha_conv_inner_ow, 1) == 2.7
        assert round(zone_attr.alpha_comb_outer_ow, 1) == 25.0
        assert round(zone_attr.weightfactor_ow[1], 13) == 0.1324989973869
        assert round(zone_attr.weightfactor_win[0], 13) == 0.4047663456282

    # EBC Calculation Verification, with parameters from TEASER3

    def test_calc_ebc(self):
        """
        Parameter Verification for ebc calculation method. Values are compared
        with TEASER3 values.
        """
        prj.set_default()
        prj.load_project(
            utilities.get_full_path("examples/examplefiles/unitTestCalc.json")
        )

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.buildings[0].calc_building_parameter()
        zone_attr = prj.buildings[0].thermal_zones[0].model_attr

        assert round(zone_attr.r1_iw, 11) == 4.62113e-06
        assert round(zone_attr.c1_iw, 2) == 1209810287.22
        assert round(zone_attr.area_iw, 5) == 9866.66667
        assert round(zone_attr.alpha_conv_inner_iw, 5) == 2.37568

        assert round(zone_attr.r_rest_ow, 5) == 0.00181
        assert round(zone_attr.r1_ow, 10) == 3.06155e-05
        assert round(zone_attr.c1_ow, 3) == 226923157.846
        assert round(zone_attr.area_ow, 5) == 920.0

        assert round(zone_attr.alpha_conv_inner_ow, 5) == 1.83043

        assert round(zone_attr.alpha_conv_outer_ow, 5) == 20.0
        assert round(zone_attr.alpha_comb_outer_ow, 5) == 25.0
        assert round(zone_attr.alpha_conv_inner_win, 5) == 2.7
        assert round(zone_attr.alpha_conv_outer_win, 5) == 20.0
        assert round(zone_attr.alpha_comb_outer_win, 5) == 25.0

        assert round(zone_attr.weightfactor_ow[0], 5) == 0.04588
        assert round(zone_attr.weightfactor_win[0], 5) == 0.33333
        assert round(zone_attr.weightfactor_ground, 5) == 0.54398

    def test_type_bldg_office_with_calc(self):
        """
        Verification of the type building generation of an office building.
        Values are compared with TEASER3 values.
        """
        from teaser.logic.archetypebuildings.bmvbs.office import Office

        prj.set_default()
        test_office = Office(
            parent=prj,
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=3,
            height_of_floors=3,
            net_leased_area=2500,
        )

        test_office.generate_archetype()

        # general parameters

        assert len(test_office.thermal_zones) == 6

        # zone specific parameters

        for zone in test_office.thermal_zones:
            if zone.name == "Meeting":
                assert zone.area == 100
            if zone.name == "Storage":
                assert zone.area == 375
            if zone.name == "Office":
                assert zone.area == 1250
            if zone.name == "Restroom":
                assert zone.area == 100
            if zone.name == "ICT":
                assert zone.area == 50
            if zone.name == "Floor":
                assert zone.area == 625

        # facade specific parameters

        assert round(test_office.get_outer_wall_area(-2), 0) == 958
        assert round(test_office.get_outer_wall_area(-1), 0) == 958
        assert round(test_office.get_outer_wall_area(0), 0) == 437
        assert round(test_office.get_outer_wall_area(180), 0) == 437
        assert round(test_office.get_outer_wall_area(90), 0) == 77
        assert round(test_office.get_outer_wall_area(270), 0) == 77
        assert round(test_office.get_window_area(0), 0) == 158
        assert round(test_office.get_window_area(180), 0) == 158
        assert round(test_office.get_window_area(90), 0) == 28
        assert round(test_office.get_window_area(270), 0) == 28

        prj.set_default()
        test_office = Office(
            parent=prj,
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=3,
            height_of_floors=3,
            net_leased_area=2500,
            office_layout=1,
            window_layout=1,
            construction_data="iwu_light",
        )

        test_office.generate_archetype()

        # facade specific parameters

        assert round(test_office.get_outer_wall_area(-2), 0) == 958
        assert round(test_office.get_outer_wall_area(-1), 0) == 958
        assert round(test_office.get_outer_wall_area(0), 0) == 446
        assert round(test_office.get_outer_wall_area(180), 0) == 446
        assert round(test_office.get_outer_wall_area(90), 0) == 79
        assert round(test_office.get_outer_wall_area(270), 0) == 79
        assert round(test_office.get_window_area(0), 0) == 149
        assert round(test_office.get_window_area(180), 0) == 149
        assert round(test_office.get_window_area(90), 0) == 26
        assert round(test_office.get_window_area(270), 0) == 26

        prj.set_default()
        test_office = Office(
            parent=prj,
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=3,
            height_of_floors=3,
            net_leased_area=2500,
            office_layout=2,
            window_layout=2,
            construction_data="iwu_heavy",
        )

        test_office.generate_archetype()

        # facade specific parameters

        assert round(test_office.get_outer_wall_area(-2), 0) == 958
        assert round(test_office.get_outer_wall_area(-1), 0) == 958
        assert round(test_office.get_outer_wall_area(0), 0) == 283
        assert round(test_office.get_outer_wall_area(180), 0) == 283
        assert round(test_office.get_outer_wall_area(90), 0) == 67
        assert round(test_office.get_outer_wall_area(270), 0) == 67
        assert round(test_office.get_window_area(0), 0) == 283
        assert round(test_office.get_window_area(180), 0) == 283
        assert round(test_office.get_window_area(90), 0) == 67
        assert round(test_office.get_window_area(270), 0) == 67

        prj.set_default()
        test_office = Office(
            parent=prj,
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=3,
            height_of_floors=3,
            net_leased_area=2500,
            office_layout=3,
            window_layout=3,
            construction_data="iwu_light",
        )

        test_office.generate_archetype()

        # facade specific parameters

        assert round(test_office.get_outer_wall_area(-2), 0) == 958
        assert round(test_office.get_outer_wall_area(-1), 0) == 958
        assert round(test_office.get_outer_wall_area(0), 0) == 35
        assert round(test_office.get_outer_wall_area(180), 0) == 35
        assert round(test_office.get_outer_wall_area(90), 0) == 35
        assert round(test_office.get_outer_wall_area(270), 0) == 35
        assert round(test_office.get_window_area(0), 0) == 315
        assert round(test_office.get_window_area(180), 0) == 315
        assert round(test_office.get_window_area(90), 0) == 315
        assert round(test_office.get_window_area(270), 0) == 315

    def test_type_bldg_institute4_with_calc(self):
        """
        Verification of the type building generation of an office building.
        Values are compared with TEASER3 values.
        """
        from teaser.logic.archetypebuildings.bmvbs.custom.institute4 import Institute4

        prj.set_default()
        test_institute4 = Institute4(
            parent=prj,
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=3,
            height_of_floors=3,
            net_leased_area=2500,
            office_layout=0,
            window_layout=0,
            construction_data="iwu_heavy",
        )

        test_institute4.generate_archetype()

        # general parameters

        assert len(test_institute4.thermal_zones) == 7

        # zone specific parameters

        for zone in test_institute4.thermal_zones:
            if zone.name == "Meeting":
                assert zone.area == 100
            if zone.name == "Storage":
                assert round(zone.area) == 700
            if zone.name == "Office":
                assert zone.area == 550
            if zone.name == "Restroom":
                assert zone.area == 100
            if zone.name == "ICT":
                assert zone.area == 50
            if zone.name == "Floor":
                assert zone.area == 500
            if zone.name == "Laboratory":
                assert zone.area == 500

        # facade specific parameters

        assert round(test_institute4.get_outer_wall_area(-2), 0) == 958
        assert round(test_institute4.get_outer_wall_area(-1), 0) == 958
        assert round(test_institute4.get_outer_wall_area(0), 0) == 742
        assert round(test_institute4.get_outer_wall_area(180), 0) == 742
        assert round(test_institute4.get_outer_wall_area(90), 0) == 131
        assert round(test_institute4.get_outer_wall_area(270), 0) == 131
        assert round(test_institute4.get_window_area(0), 0) == 158
        assert round(test_institute4.get_window_area(180), 0) == 158
        assert round(test_institute4.get_window_area(90), 0) == 28
        assert round(test_institute4.get_window_area(270), 0) == 28

    def test_type_bldg_institute8_with_calc(self):
        """
        Verification of the type building generation of an office building.
        Values are compared with TEASER3 values.
        """
        from teaser.logic.archetypebuildings.bmvbs.custom.institute8 import Institute8

        prj.set_default()
        test_institute8 = Institute8(
            parent=prj,
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=3,
            height_of_floors=3,
            net_leased_area=2500,
            office_layout=0,
            window_layout=0,
            construction_data="iwu_heavy",
        )

        test_institute8.generate_archetype()

        # general parameters

        assert len(test_institute8.thermal_zones) == 7

        # zone specific parameters

        for zone in test_institute8.thermal_zones:
            if zone.name == "Meeting":
                assert zone.area == 100
            if zone.name == "Storage":
                assert zone.area == 750
            if zone.name == "Office":
                assert zone.area == 100
            if zone.name == "Restroom":
                assert zone.area == 100
            if zone.name == "ICT":
                assert zone.area == 50
            if zone.name == "Floor":
                assert zone.area == 150
            if zone.name == "Laboratory":
                assert zone.area == 1250

        # facade specific parameters

        assert round(test_institute8.get_outer_wall_area(-2), 0) == 958
        assert round(test_institute8.get_outer_wall_area(-1), 0) == 958
        assert round(test_institute8.get_outer_wall_area(0), 0) == 742
        assert round(test_institute8.get_outer_wall_area(180), 0) == 742
        assert round(test_institute8.get_outer_wall_area(90), 0) == 131
        assert round(test_institute8.get_outer_wall_area(270), 0) == 131
        assert round(test_institute8.get_window_area(0), 0) == 158
        assert round(test_institute8.get_window_area(180), 0) == 158
        assert round(test_institute8.get_window_area(90), 0) == 28
        assert round(test_institute8.get_window_area(270), 0) == 28

    def test_type_bldg_institute_with_calc(self):
        """
        Verification of the type building generation of an office building.
        Values are compared with TEASER3 values.
        """
        from teaser.logic.archetypebuildings.bmvbs.custom.institute import Institute

        prj.set_default()
        test_institute = Institute(
            parent=prj,
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=3,
            height_of_floors=3,
            net_leased_area=2500,
            office_layout=0,
            window_layout=0,
            construction_data="iwu_heavy",
        )

        test_institute.generate_archetype()

        # general parameters

        assert len(test_institute.thermal_zones) == 7

        # zone specific parameters

        for zone in test_institute.thermal_zones:
            if zone.name == "Meeting":
                assert zone.area == 100
            if zone.name == "Storage":
                assert zone.area == 1000
            if zone.name == "Office":
                assert zone.area == 400
            if zone.name == "Restroom":
                assert zone.area == 100
            if zone.name == "ICT":
                assert zone.area == 50
            if zone.name == "Floor":
                assert zone.area == 475
            if zone.name == "Laboratory":
                assert zone.area == 375

        # facade specific parameters

        assert round(test_institute.get_outer_wall_area(-2), 0) == 958
        assert round(test_institute.get_outer_wall_area(-1), 0) == 958
        assert round(test_institute.get_outer_wall_area(0), 0) == 836
        assert round(test_institute.get_outer_wall_area(180), 0) == 836
        assert round(test_institute.get_outer_wall_area(90), 0) == 147
        assert round(test_institute.get_outer_wall_area(270), 0) == 147
        assert round(test_institute.get_window_area(0), 0) == 158
        assert round(test_institute.get_window_area(180), 0) == 158
        assert round(test_institute.get_window_area(90), 0) == 28
        assert round(test_institute.get_window_area(270), 0) == 28

    def test_type_bldg_residential_with_calc(self):
        """
        Verification of the type building generation of an office building.
        Values are compared with TEASER3 values.
        """
        from teaser.logic.archetypebuildings.bmvbs.singlefamilydwelling import (
            SingleFamilyDwelling,
        )

        prj.set_default()
        test_residential = SingleFamilyDwelling(
            parent=prj,
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=3,
            height_of_floors=3,
            net_leased_area=2500,
        )

        test_residential.generate_archetype()

        # general parameters

        assert len(test_residential.thermal_zones) == 1

        # zone specific parameters

        for zone in test_residential.thermal_zones:
            if zone.name == "SingleDwelling":
                assert zone.area == 2500

        # facade specific parameters

        assert round(test_residential.get_outer_wall_area(-2), 0) == 1108
        assert round(test_residential.get_outer_wall_area(-1), 0) == 1108
        assert round(test_residential.get_outer_wall_area(0), 0) == 312
        assert round(test_residential.get_outer_wall_area(180), 0) == 312
        assert round(test_residential.get_outer_wall_area(90), 0) == 312
        assert round(test_residential.get_outer_wall_area(270), 0) == 312
        assert round(test_residential.get_window_area(0), 0) == 125
        assert round(test_residential.get_window_area(180), 0) == 125
        assert round(test_residential.get_window_area(90), 0) == 125
        assert round(test_residential.get_window_area(270), 0) == 125

        prj.set_default()
        test_residential = SingleFamilyDwelling(
            parent=prj,
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=3,
            height_of_floors=3,
            net_leased_area=2500,
            residential_layout=1,
            neighbour_buildings=1,
            attic=1,
            dormer=1,
            cellar=1,
            construction_data="iwu_light",
        )

        test_residential.generate_archetype()

        # facade specific parameters

        assert round(test_residential.get_outer_wall_area(-2), 0) == 1108
        assert round(test_residential.get_outer_wall_area(-1), 0) == 1108
        assert round(test_residential.get_outer_wall_area(0), 0) == 393
        assert round(test_residential.get_outer_wall_area(180), 0) == 393
        assert round(test_residential.get_outer_wall_area(90), 0) == 393
        assert round(test_residential.get_outer_wall_area(270), 0) == 393
        assert round(test_residential.get_window_area(0), 0) == 125
        assert round(test_residential.get_window_area(180), 0) == 125
        assert round(test_residential.get_window_area(90), 0) == 125
        assert round(test_residential.get_window_area(270), 0) == 125

        prj.set_default()
        test_residential = SingleFamilyDwelling(
            parent=prj,
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=3,
            height_of_floors=3,
            net_leased_area=2500,
            residential_layout=0,
            neighbour_buildings=2,
            attic=2,
            dormer=0,
            cellar=2,
            construction_data="iwu_heavy",
        )

        test_residential.generate_archetype()

        # facade specific parameters

        assert round(test_residential.get_outer_wall_area(-2), 0) == 858
        assert round(test_residential.get_outer_wall_area(-1), 0) == 484
        assert round(test_residential.get_outer_wall_area(0), 0) == 267
        assert round(test_residential.get_outer_wall_area(180), 0) == 267
        assert round(test_residential.get_outer_wall_area(90), 0) == 267
        assert round(test_residential.get_outer_wall_area(270), 0) == 267
        assert round(test_residential.get_window_area(0), 0) == 125
        assert round(test_residential.get_window_area(180), 0) == 125
        assert round(test_residential.get_window_area(90), 0) == 125
        assert round(test_residential.get_window_area(270), 0) == 125

        prj.set_default()
        test_residential = SingleFamilyDwelling(
            parent=prj,
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=3,
            height_of_floors=3,
            net_leased_area=2500,
            residential_layout=0,
            neighbour_buildings=2,
            attic=3,
            dormer=0,
            cellar=3,
            construction_data="iwu_light",
        )

        test_residential.generate_archetype()

        # facade specific parameters

        assert round(test_residential.get_outer_wall_area(-2), 0) == 700
        assert round(test_residential.get_outer_wall_area(-1), 0) == 789
        assert round(test_residential.get_outer_wall_area(0), 0) == 251
        assert round(test_residential.get_outer_wall_area(180), 0) == 251
        assert round(test_residential.get_outer_wall_area(90), 0) == 251
        assert round(test_residential.get_outer_wall_area(270), 0) == 251
        assert round(test_residential.get_window_area(0), 0) == 125
        assert round(test_residential.get_window_area(180), 0) == 125
        assert round(test_residential.get_window_area(90), 0) == 125
        assert round(test_residential.get_window_area(270), 0) == 125

    # # methods in Project, these tests only test if the API function works,
    # # not if it produces reliable results.

    def test_load_save_project(self):
        """test of load_project and save_project"""

        prj.load_project(
            utilities.get_full_path(("examples/examplefiles" "/unitTest.json"))
        )
        therm_zone = prj.buildings[-1].thermal_zones[0]
        assert round(therm_zone.outer_walls[0].area, 2) == 137.23
        tz_area = sum([tz.area for tz in prj.buildings[-1].thermal_zones])
        assert prj.buildings[-1].net_leased_area == tz_area
        prj.save_project(file_name="unitTest", path=None)
        prj.save_project(file_name=None, path=utilities.get_default_path())
        prj.set_default()

    def test_load_save_project_new(self):
        """test of load_project and save_project"""
        prj.set_default(load_data=False)
        prj.load_project(os.path.join(utilities.get_default_path(), "unitTest.json"))
        therm_zone = prj.buildings[-1].thermal_zones[0]
        assert therm_zone.area == 994.0
        tz_area = sum([tz.area for tz in prj.buildings[-1].thermal_zones])
        for tz in prj.buildings[-1].thermal_zones:
            print(tz.name, tz.area)
        print(prj.buildings[-1].name, prj.buildings[-1].net_leased_area)
        assert prj.buildings[-1].net_leased_area == tz_area
        assert prj.buildings[-1].net_leased_area == 1988.0
        assert prj.buildings[-1].name == "TestBuilding"
        prj.name = "Project"
        prj.save_project(file_name="unitTest_new.json", path=None)

    def test_calc_all_buildings(self):
        """test of calc_all_buildings, no calculation verification"""

        helptest.building_test2(prj)
        helptest.building_test2(prj)
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings(raise_errors=True)

    def test_number_of_elements_propagation(self):
        """Tests propagation of changes in number_of_elements_calc"""

        helptest.building_test2(prj)
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings(raise_errors=True)

        assert prj.number_of_elements_calc == 2
        bldg = prj.buildings[-1]
        assert bldg.number_of_elements_calc == 2
        tz = bldg.thermal_zones[0]
        assert isinstance(tz.model_attr, TwoElement)
        assert not hasattr(tz.model_attr, 'area_gf')
        assert not hasattr(tz.model_attr, 'area_rt')

        prj.number_of_elements_calc = 3
        prj.calc_all_buildings(raise_errors=True)

        assert prj.number_of_elements_calc == 3
        bldg = prj.buildings[-1]
        assert bldg.number_of_elements_calc == 3
        tz = bldg.thermal_zones[0]
        assert isinstance(tz.model_attr, ThreeElement)
        assert tz.model_attr.area_gf == 140.0
        assert not hasattr(tz.model_attr, 'area_rt')

        prj.number_of_elements_calc = 4
        prj.calc_all_buildings(raise_errors=True)

        assert prj.number_of_elements_calc == 4
        bldg = prj.buildings[-1]
        assert bldg.number_of_elements_calc == 4
        tz = bldg.thermal_zones[0]
        assert isinstance(tz.model_attr, FourElement)
        assert tz.model_attr.area_rt == 140.0
        assert tz.model_attr.area_gf == 140.0

    def test_calc_building_parameter(self):
        """Check that calc_building_parameter() not overwrites prj settings"""
        helptest.building_test2(prj)
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings(raise_errors=True)

        assert prj.number_of_elements_calc == 2
        bldg = prj.buildings[-1]
        assert bldg.number_of_elements_calc == 2
        bldg.calc_building_parameter()
        tz = bldg.thermal_zones[0]
        assert isinstance(tz.model_attr, TwoElement)
        assert not hasattr(tz.model_attr, 'area_gf')
        assert not hasattr(tz.model_attr, 'area_rt')

        prj.number_of_elements_calc = 3
        prj.calc_all_buildings(raise_errors=True)

        assert prj.number_of_elements_calc == 3
        bldg = prj.buildings[-1]
        assert bldg.number_of_elements_calc == 3
        bldg.calc_building_parameter()
        tz = bldg.thermal_zones[0]
        assert isinstance(tz.model_attr, ThreeElement)
        assert tz.model_attr.area_gf == 140.0
        assert not hasattr(tz.model_attr, 'area_rt')

        prj.number_of_elements_calc = 4
        prj.calc_all_buildings(raise_errors=True)

        assert prj.number_of_elements_calc == 4
        bldg = prj.buildings[-1]
        assert bldg.number_of_elements_calc == 4
        bldg.calc_building_parameter()
        tz = bldg.thermal_zones[0]
        assert isinstance(tz.model_attr, FourElement)
        assert tz.model_attr.area_rt == 140.0
        assert tz.model_attr.area_gf == 140.0

    def test_retrofit_all_buildings(self):
        """test of retrofit_all_buildings, no calculation verification"""
        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="iwu_single_family_dwelling",
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219,
        )
        prj.add_residential(
            construction_data="tabula_de_standard",
            geometry_data="tabula_de_single_family_house",
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219,
        )
        prj.retrofit_all_buildings(year_of_retrofit=2015, type_of_retrofit="retrofit")

    def test_export_aixlib(self):
        """test of export_aixlib, no calculation verification"""

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib(building_model="Test", zone_model="Test", corG="Test")

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.buildings.append(prj.buildings[-1])

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib(path=utilities.get_default_path())

        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings(raise_errors=True)
        prj.export_aixlib()

        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib(building_model="Test", zone_model="Test", corG="Test")

        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.buildings.append(prj.buildings[-1])

        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib(path=utilities.get_default_path())

    def test_export_ibpsa(self):
        """test of export_ibpsa, no calculation verification"""

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa(library="AixLib")
        prj.export_ibpsa(library="Buildings")
        prj.export_ibpsa(library="BuildingSystems")
        prj.export_ibpsa(library="IDEAS")
        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa(library="AixLib")
        prj.export_ibpsa(library="Buildings")
        prj.export_ibpsa(library="BuildingSystems")
        prj.export_ibpsa(library="IDEAS")
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa(library="AixLib")
        prj.export_ibpsa(library="Buildings")
        prj.export_ibpsa(library="BuildingSystems")
        prj.export_ibpsa(library="IDEAS")
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa(library="AixLib")
        prj.export_ibpsa(library="Buildings")
        prj.export_ibpsa(library="BuildingSystems")
        prj.export_ibpsa(library="IDEAS")
        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa(library="AixLib")
        prj.export_ibpsa(library="Buildings")
        prj.export_ibpsa(library="BuildingSystems")
        prj.export_ibpsa(library="IDEAS")
        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa(library="AixLib")
        prj.export_ibpsa(library="Buildings")
        prj.export_ibpsa(library="BuildingSystems")
        prj.export_ibpsa(library="IDEAS")
        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa(library="AixLib")
        prj.export_ibpsa(library="Buildings")
        prj.export_ibpsa(library="BuildingSystems")
        prj.export_ibpsa(library="IDEAS")
        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa(library="AixLib")
        prj.export_ibpsa(library="Buildings")
        prj.export_ibpsa(library="BuildingSystems")
        prj.export_ibpsa(library="IDEAS")
        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa(internal_id=prj.buildings[-1].internal_id)
        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa(path=utilities.get_default_path())
        prj.set_default()

    def test_export_aixlib_five(self):
        """test AixLib export with five elements, no calculation verification"""

        prj.set_default(load_data=True)
        helptest.building_test2(prj)
        helptest.interzonal_test2(prj)
        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings(raise_errors=True)
        prj.export_aixlib(path=utilities.get_default_path() + '_2')

    def test_instantiate_data_class(self):
        """test of instantiate_data_class"""

        prj.instantiate_data_class()

    def test_type_bldg_office(self):
        """test of type_bldg_office, no calculation verification
        """
        prj.set_default(load_data=False)

        prj.add_non_residential(
            construction_data="iwu_heavy",
            geometry_data="bmvbs_office",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            office_layout=0,
            window_layout=0,
        )
        prj.add_non_residential(
            construction_data="iwu_heavy",
            geometry_data="bmvbs_office",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            internal_gains_mode=2,
            office_layout=0,
            window_layout=0,
        )
        prj.add_non_residential(
            construction_data="iwu_heavy",
            geometry_data="bmvbs_office",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            internal_gains_mode=3,
            office_layout=0,
            window_layout=0,
        )

    def test_type_bldg_institute(self):
        """test of type_bldg_institute, no calculation verification"""

        prj.add_non_residential(
            construction_data="iwu_heavy",
            geometry_data="bmvbs_institute",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=True,
            office_layout=0,
            window_layout=0,

        )
        prj.add_non_residential(
            construction_data="iwu_heavy",
            geometry_data="bmvbs_institute",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            internal_gains_mode=2,
            office_layout=0,
            window_layout=0,
        )
        prj.add_non_residential(
            construction_data="iwu_heavy",
            geometry_data="bmvbs_institute",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            internal_gains_mode=3,
            office_layout=0,
            window_layout=0,
        )

    def test_type_bldg_institute4(self):
        """test of type_bldg_institute4, no calculation verification"""

        prj.add_non_residential(
            construction_data="iwu_heavy",
            geometry_data="bmvbs_institute4",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=True,
            office_layout=0,
            window_layout=0,
        )

    def test_type_bldg_institute8(self):
        """test of type_bldg_institute8, no calculation verification"""

        prj.add_non_residential(
            construction_data="iwu_heavy",
            geometry_data="bmvbs_institute8",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=True,
            office_layout=0,
            window_layout=0,
        )

    def test_type_bldg_residential(self):
        """test of type_bldg_residential, no calculation verification"""

        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="iwu_single_family_dwelling",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=0,
            cellar=0,
            dormer=0,
        )

    def test_est_bldgs(self):
        """test of type_bldg_est, no calculation verification"""

        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="urbanrenet_est1a",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=0,
            cellar=0,
            dormer=0,
            number_of_apartments=1,
        )

        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="urbanrenet_est1b",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=0,
            cellar=0,
            dormer=0,
            number_of_apartments=1,
        )

        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="urbanrenet_est2",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=0,
            cellar=0,
            dormer=0,
            number_of_apartments=1,
        )

        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="urbanrenet_est3",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=0,
            cellar=0,
            dormer=0,
            number_of_apartments=1,
        )

        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="urbanrenet_est4a",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=0,
            cellar=0,
            dormer=0,
            number_of_apartments=1,
        )

        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="urbanrenet_est4b",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=0,
            cellar=0,
            dormer=0,
            number_of_apartments=1,
        )

        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="urbanrenet_est5",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=0,
            cellar=0,
            dormer=0,
            number_of_apartments=1,
        )

        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="urbanrenet_est6",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=0,
            cellar=0,
            dormer=0,
            number_of_apartments=1,
        )

        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="urbanrenet_est7",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=0,
            cellar=0,
            dormer=0,
            number_of_apartments=1,
        )

        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="urbanrenet_est8a",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=0,
            cellar=0,
            dormer=0,
            number_of_apartments=1,
        )

        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="urbanrenet_est8b",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=0,
            cellar=0,
            dormer=0,
            number_of_apartments=1,
        )

    # methods in Building

    def test_get_inner_wall_area(self):
        """test of get_inner_wall_area"""
        prj.set_default()
        helptest.building_test2(prj)
        sum_area = prj.buildings[-1].get_inner_wall_area()
        assert round(sum_area, 1) == 34.0

    def test_set_outer_wall_area(self):
        """test of set_outer_wall_area"""
        print(prj.buildings[-1].thermal_zones[-1].outer_walls[1].area)
        prj.buildings[-1].set_outer_wall_area(2.0, 0.0)

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        print(therm_zone.outer_walls[1].area)
        assert round(therm_zone.outer_walls[0].area, 3) == 2.0
        assert round(therm_zone.outer_walls[1].area, 3) == 14.0

    def test_get_outer_wall_area(self):
        """test of get_outer_wall_area"""
        prj.buildings[-1].get_outer_wall_area(0.0)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        assert round(therm_zone.outer_walls[0].area, 3) == 2.0
        assert round(therm_zone.outer_walls[1].area, 3) == 14.0

    def test_set_window_area(self):
        """test of set_window_area"""
        prj.buildings[-1].set_window_area(1.0, 90.0)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        assert round(therm_zone.windows[0].area, 3) == 1.0

    def test_get_window_area(self):
        """test of get_window_area"""
        prj.buildings[-1].get_window_area(90.0)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        assert round(therm_zone.windows[0].area, 3) == 1.0

    def test_fill_outer_wall_area_dict(self):
        """test of fill_outer_wall_area_dict"""

        prj.buildings[-1].fill_outer_area_dict()
        outwall_dict_round = {
            key: round(value, 2) for key, value in prj.buildings[-1].outer_area.items()
        }
        assert outwall_dict_round == {
            -2.0: 140,
            -1.0: 140,
            0.0: 2.0,
            90.0: 14.0,
            180.0: 10.0,
            270.0: 14.0,
        }

    def test_fill_window_area_dict(self):
        """test of fill_window_area_dict"""
        prj.buildings[-1].fill_window_area_dict()
        assert prj.buildings[-1].window_area == {90.0: 1.0, 180.0: 8.0, 270.0: 5.0}

    def test_calc_building_parameter(self):
        """test of calc_building_parameter"""
        prj.set_default()
        helptest.building_test2(prj)

        prj.buildings[-1].calc_building_parameter(
            number_of_elements=2, merge_windows=True, used_library="AixLib"
        )

        assert round(prj.buildings[-1].volume, 1) == 490.0
        assert round(prj.buildings[-1].sum_heat_load, 4) == 6659.6256

    # methods in therm_zone

    def test_calc_zone_parameters(self):
        """test of calc zone parameter, no calculation verification"""

        prj.buildings[-1].thermal_zones[-1].calc_zone_parameters(
            number_of_elements=2, merge_windows=False
        )
        prj.buildings[-1].thermal_zones[-1].calc_zone_parameters(
            number_of_elements=2, merge_windows=True
        )

    def test_heat_load(self):
        """test of heating_load"""
        prj.set_default()
        helptest.building_test2(prj)
        prj.buildings[-1].thermal_zones[-1].use_conditions.base_infiltration = 0.5
        prj.buildings[-1].thermal_zones[-1].calc_zone_parameters(
            number_of_elements=2, merge_windows=True
        )
        prj.buildings[-1].thermal_zones[-1].model_attr.calc_attributes()
        assert (
            round(prj.buildings[-1].thermal_zones[-1].model_attr.heat_load, 4)
            == 6659.6256
        )

    def test_sum_building_elements_one(self):
        """test of combine_building_elements"""
        prj.set_default()
        helptest.building_test2(prj)

        from teaser.logic.buildingobjects.calculation.one_element import OneElement

        therm_zone = prj.buildings[-1].thermal_zones[-1]

        calc_attr = OneElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        calc_attr._sum_outer_wall_elements()
        calc_attr._sum_window_elements()

        # outerwall
        assert calc_attr.ua_value_ow == approx(135.5818558809656, abs=1e-14)
        assert calc_attr.area_ow == approx(328.0, abs=0.1)
        assert calc_attr.r_conv_inner_ow == approx(0.0016512549537648611,
                                                   abs=1e-19)
        assert calc_attr.r_rad_inner_ow == approx(0.000609756097560976,
                                                  abs=1e-18)
        assert calc_attr.r_comb_inner_ow == approx(0.00044531528322052017,
                                                   abs=1e-20)
        assert calc_attr.r_conv_outer_ow == approx(0.00026595744680851064,
                                                   abs=1e-20)
        assert calc_attr.r_rad_outer_ow == approx(0.001063829787234043,
                                                  abs=1e-18)
        assert calc_attr.r_comb_outer_ow == approx(0.0002127659574468085,
                                                   abs=1e-20)
        assert calc_attr.alpha_conv_inner_ow == approx(1.84634, abs=0.00001)
        assert calc_attr.alpha_rad_inner_ow == approx(5.0, abs=0.00001)
        assert calc_attr.alpha_comb_inner_ow == approx(6.84634, abs=0.00001)
        assert calc_attr.alpha_conv_outer_ow == approx(20.0, abs=0.1)
        assert calc_attr.alpha_rad_outer_ow == approx(5.0, abs=0.00001)
        assert calc_attr.alpha_comb_outer_ow == approx(25.0, abs=0.1)

        # window
        assert calc_attr.ua_value_win == approx(32.87895310796074, abs=1e-14)
        assert calc_attr.area_win == approx(18.0, abs=0.1)
        assert calc_attr.r_conv_inner_win == approx(0.032679738562091505,
                                                    abs=1e-19)
        assert calc_attr.r_rad_inner_win == approx(0.0111, abs=0.0001)
        assert calc_attr.r_comb_inner_win == approx(0.008291873963515755,
                                                    abs=1e-19)
        assert calc_attr.r_conv_outer_win == approx(0.00278, abs=0.00001)
        assert calc_attr.r_rad_outer_win == approx(0.0111, abs=0.0001)
        assert calc_attr.r_comb_outer_win == approx(0.0022, abs=0.0001)
        assert calc_attr.alpha_conv_inner_win == approx(1.7, abs=0.1)
        assert calc_attr.alpha_comb_outer_win == approx(25.0, abs=0.1)
        assert calc_attr.alpha_conv_outer_win == approx(20.0, abs=0.1)
        assert calc_attr.weighted_g_value == approx(0.789, abs=0.001)

    def test_calc_chain_matrix_one(self):
        """test of calc_chain_matrix"""

        from teaser.logic.buildingobjects.calculation.one_element import OneElement

        therm_zone = prj.buildings[-1].thermal_zones[-1]

        calc_attr = OneElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        omega = 2 * math.pi / 86400 / 5

        helplist_outer_walls = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.windows
        )

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls, omega=omega
        )
        assert round(r1_ow, 14) == 0.00100751548411
        assert round(c1_ow, 5) == 3648580.59312

    def test_sum_building_elements_two(self):
        """test of combine_building_elements"""
        prj.set_default()
        helptest.building_test2(prj)

        from teaser.logic.buildingobjects.calculation.two_element import TwoElement

        therm_zone = prj.buildings[-1].thermal_zones[-1]

        calc_attr = TwoElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        calc_attr._sum_outer_wall_elements()
        calc_attr._sum_inner_wall_elements()
        calc_attr._sum_window_elements()

        # innerwall
        assert calc_attr.ua_value_iw == approx(14.286493860845841, abs=1e-14)
        assert calc_attr.area_iw == approx(34.0, abs=0.1)
        assert calc_attr.r_conv_inner_iw == approx(0.010893246187363833,
                                                   abs=1e-18)
        assert calc_attr.r_rad_inner_iw == approx(0.0058823529411764705,
                                                  abs=1e-19)
        assert calc_attr.r_comb_inner_iw == approx(0.003819709702062643,
                                                   abs=1e-19)
        assert calc_attr.alpha_conv_inner_iw == approx(2.7, abs=0.1)
        assert calc_attr.alpha_rad_inner_iw == approx(5.0, abs=0.1)
        assert calc_attr.alpha_comb_inner_iw == approx(7.7, abs=0.1)

        # outerwall
        assert calc_attr.ua_value_ow == approx(135.5818558809656, abs=1e-14)
        assert calc_attr.area_ow == approx(328.0, abs=0.1)
        assert calc_attr.r_conv_inner_ow == approx(0.0016512549537648611,
                                                   abs=1e-19)
        assert calc_attr.r_rad_inner_ow == approx(0.000609756097560976,
                                                  abs=1e-18)
        assert calc_attr.r_comb_inner_ow == approx(0.00044531528322052017,
                                                   abs=1e-20)
        assert calc_attr.r_conv_outer_ow == approx(0.00026595744680851064,
                                                   abs=1e-20)
        assert calc_attr.r_rad_outer_ow == approx(0.001063829787234043,
                                                  abs=1e-18)
        assert calc_attr.r_comb_outer_ow == approx(0.0002127659574468085,
                                                   abs=1e-20)
        assert calc_attr.alpha_conv_inner_ow == approx(1.84634, abs=0.00001)
        assert calc_attr.alpha_rad_inner_ow == approx(5.0, abs=0.00001)
        assert calc_attr.alpha_comb_inner_ow == approx(6.84634, abs=0.00001)
        assert calc_attr.alpha_conv_outer_ow == approx(20.0, abs=0.1)
        assert calc_attr.alpha_rad_outer_ow == approx(5.0, abs=0.00001)
        assert calc_attr.alpha_comb_outer_ow == approx(25.0, abs=0.1)

        # window
        assert calc_attr.ua_value_win == approx(32.87895310796074, abs=1e-14)
        assert calc_attr.area_win == approx(18.0, abs=0.1)
        assert calc_attr.r_conv_inner_win == approx(0.032679738562091505,
                                                    abs=1e-19)
        assert calc_attr.r_rad_inner_win == approx(0.0111, abs=0.0001)
        assert calc_attr.r_comb_inner_win == approx(0.008291873963515755,
                                                    abs=1e-19)
        assert calc_attr.r_conv_outer_win == approx(0.00278, abs=0.00001)
        assert calc_attr.r_rad_outer_win == approx(0.0111, abs=0.0001)
        assert calc_attr.r_comb_outer_win == approx(0.0022, abs=0.0001)
        assert calc_attr.alpha_conv_inner_win == approx(1.7, abs=0.1)
        assert calc_attr.alpha_comb_outer_win == approx(25.0, abs=0.1)
        assert calc_attr.alpha_conv_outer_win == approx(20.0, abs=0.1)
        assert calc_attr.weighted_g_value == approx(0.789, abs=0.001)

    def test_calc_chain_matrix_two(self):
        """test of calc_chain_matrix"""
        from teaser.logic.buildingobjects.calculation.two_element import TwoElement

        therm_zone = prj.buildings[-1].thermal_zones[-1]

        calc_attr = TwoElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        omega = 2 * math.pi / 86400 / 5

        calc_attr = TwoElement(therm_zone, merge_windows=True, t_bt=5)

        helplist_outer_walls = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.windows
        )

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls, omega=omega
        )
        assert round(r1_ow, 14) == 0.00100751548411
        assert round(c1_ow, 5) == 3648580.59312

        helplist_inner_walls = (
            therm_zone.inner_walls + therm_zone.ceilings + therm_zone.floors
        )

        r1_iw, c1_iw = calc_attr._calc_parallel_connection(
            element_list=helplist_inner_walls, omega=omega
        )
        assert round(r1_iw, 13) == 0.0097195611408
        assert round(c1_iw, 6) == 319983.518743

    def test_sum_building_elements_three(self):
        """test of combine_building_elements"""
        prj.set_default()
        helptest.building_test2(prj)

        from teaser.logic.buildingobjects.calculation.three_element import ThreeElement

        therm_zone = prj.buildings[-1].thermal_zones[-1]

        calc_attr = ThreeElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        calc_attr._sum_outer_wall_elements()
        calc_attr._sum_ground_floor_elements()
        calc_attr._sum_inner_wall_elements()
        calc_attr._sum_window_elements()

        # innerwall
        assert calc_attr.ua_value_iw == approx(14.286493860845841, abs=1e-14)
        assert calc_attr.area_iw == approx(34.0, abs=0.1)
        assert calc_attr.r_conv_inner_iw == approx(0.010893246187363833,
                                                   abs=1e-18)
        assert calc_attr.r_rad_inner_iw == approx(0.0058823529411764705,
                                                  abs=1e-19)
        assert calc_attr.r_comb_inner_iw == approx(0.003819709702062643,
                                                   abs=1e-19)
        assert calc_attr.alpha_conv_inner_iw == approx(2.7, abs=0.1)
        assert calc_attr.alpha_rad_inner_iw == approx(5.0, abs=0.1)
        assert calc_attr.alpha_comb_inner_iw == approx(7.7, abs=0.1)

        # outerwall
        assert calc_attr.ua_value_ow == approx(77.23037843150993, abs=1e-13)
        assert calc_attr.area_ow == approx(188.0, abs=0.1)
        assert calc_attr.r_conv_inner_ow == approx(0.0027203482045701846,
                                                   abs=1e-19)
        assert calc_attr.r_rad_inner_ow == approx(0.001063829787234043,
                                                  abs=1e-18)
        assert calc_attr.r_comb_inner_ow == approx(0.0007647598654022638,
                                                   abs=1e-20)
        assert calc_attr.r_conv_outer_ow == approx(0.00026595744680851064,
                                                   abs=1e-20)
        assert calc_attr.r_rad_outer_ow == approx(0.001063829787234043,
                                                  abs=1e-18)
        assert calc_attr.r_comb_outer_ow == approx(0.0002127659574468085,
                                                   abs=1e-20)
        assert calc_attr.alpha_conv_inner_ow == approx(1.95532, abs=0.00001)
        assert calc_attr.alpha_rad_inner_ow == approx(5.0, abs=0.00001)
        assert calc_attr.alpha_comb_inner_ow == approx(6.95532, abs=0.00001)
        assert calc_attr.alpha_conv_outer_ow == approx(20.0, abs=0.1)
        assert calc_attr.alpha_rad_outer_ow == approx(5.0, abs=0.00001)
        assert calc_attr.alpha_comb_outer_ow == approx(25.0, abs=0.1)

        # groundfloor
        assert calc_attr.ua_value_gf == approx(58.351477449455686, abs=1e-14)
        assert calc_attr.area_gf == approx(140.0, abs=0.1)
        assert calc_attr.r_conv_inner_gf == approx(0.004201680672268907,
                                                   abs=1e-19)
        assert calc_attr.r_rad_inner_gf == approx(0.001428571428571429,
                                                  abs=1e-18)
        assert calc_attr.r_comb_inner_gf == approx(0.0010660980810234541,
                                                   abs=1e-20)
        assert calc_attr.alpha_conv_inner_gf == approx(1.7, abs=0.00001)
        assert calc_attr.alpha_rad_inner_gf == approx(5.0, abs=0.00001)
        assert calc_attr.alpha_comb_inner_gf == approx(6.7, abs=0.00001)

        # window
        assert calc_attr.ua_value_win == approx(32.87895310796074, abs=1e-14)
        assert calc_attr.area_win == approx(18.0, abs=0.1)
        assert calc_attr.r_conv_inner_win == approx(0.032679738562091505,
                                                    abs=1e-19)
        assert calc_attr.r_rad_inner_win == approx(0.0111, abs=0.0001)
        assert calc_attr.r_comb_inner_win == approx(0.008291873963515755,
                                                    abs=1e-19)
        assert calc_attr.r_conv_outer_win == approx(0.00278, abs=0.00001)
        assert calc_attr.r_rad_outer_win == approx(0.0111, abs=0.0001)
        assert calc_attr.r_comb_outer_win == approx(0.0022, abs=0.0001)
        assert calc_attr.alpha_conv_inner_win == approx(1.7, abs=0.1)
        assert calc_attr.alpha_comb_outer_win == approx(25.0, abs=0.1)
        assert calc_attr.alpha_conv_outer_win == approx(20.0, abs=0.1)
        assert calc_attr.weighted_g_value == approx(0.789, abs=0.001)

    def test_calc_chain_matrix_three(self):
        """test of calc_chain_matrix"""
        from teaser.logic.buildingobjects.calculation.three_element import ThreeElement

        therm_zone = prj.buildings[-1].thermal_zones[-1]

        calc_attr = ThreeElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        omega = 2 * math.pi / 86400 / 5

        helplist_outer_walls = (
            therm_zone.outer_walls + therm_zone.rooftops + therm_zone.windows
        )

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls, omega=omega
        )
        assert round(r1_ow, 14) == 0.00175779297228
        assert round(c1_ow, 5) == 2091259.60825

        helplist_inner_walls = (
            therm_zone.inner_walls + therm_zone.ceilings + therm_zone.floors
        )

        r1_iw, c1_iw = calc_attr._calc_parallel_connection(
            element_list=helplist_inner_walls, omega=omega
        )
        assert round(r1_iw, 13) == 0.0097195611408
        assert round(c1_iw, 6) == 319983.518743

    def test_sum_building_elements_four(self):
        """test of combine_building_elements"""
        prj.set_default()
        helptest.building_test2(prj)

        from teaser.logic.buildingobjects.calculation.four_element import FourElement

        therm_zone = prj.buildings[-1].thermal_zones[-1]

        calc_attr = FourElement(therm_zone, merge_windows=True, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        calc_attr._sum_outer_wall_elements()
        calc_attr._sum_ground_floor_elements()
        calc_attr._sum_rooftop_elements()
        calc_attr._sum_inner_wall_elements()
        calc_attr._sum_window_elements()

        # innerwall
        assert calc_attr.ua_value_iw == approx(14.286493860845841, abs=1e-14)
        assert calc_attr.area_iw == approx(34.0, abs=0.1)
        assert calc_attr.r_conv_inner_iw == approx(0.010893246187363833,
                                                   abs=1e-18)
        assert calc_attr.r_rad_inner_iw == approx(0.0058823529411764705,
                                                  abs=1e-19)
        assert calc_attr.r_comb_inner_iw == approx(0.003819709702062643,
                                                   abs=1e-19)
        assert calc_attr.alpha_conv_inner_iw == approx(2.7, abs=0.1)
        assert calc_attr.alpha_rad_inner_iw == approx(5.0, abs=0.1)
        assert calc_attr.alpha_comb_inner_iw == approx(7.7, abs=0.1)

        # outerwall
        assert calc_attr.ua_value_ow == approx(19.83577523748189, abs=1e-14)
        assert calc_attr.area_ow == approx(48.0, abs=0.1)
        assert calc_attr.r_conv_inner_ow == approx(0.007716049382716048,
                                                   abs=1e-19)
        assert calc_attr.r_rad_inner_ow == approx(0.004166666666666667,
                                                  abs=1e-18)
        assert calc_attr.r_comb_inner_ow == approx(0.0027056277056277055,
                                                   abs=1e-20)
        assert calc_attr.r_conv_outer_ow == approx(0.0010416666666666667,
                                                   abs=1e-20)
        assert calc_attr.r_rad_outer_ow == approx(0.004166666666666667,
                                                  abs=1e-18)
        assert calc_attr.r_comb_outer_ow == approx(0.0008333333333333334,
                                                   abs=1e-20)
        assert calc_attr.alpha_conv_inner_ow == approx(2.7, abs=0.00001)
        assert calc_attr.alpha_rad_inner_ow == approx(5.0, abs=0.00001)
        assert calc_attr.alpha_comb_inner_ow == approx(7.7, abs=0.00001)
        assert calc_attr.alpha_conv_outer_ow == approx(20.0, abs=0.1)
        assert calc_attr.alpha_rad_outer_ow == approx(5.0, abs=0.00001)
        assert calc_attr.alpha_comb_outer_ow == approx(25.0, abs=0.1)

        # groundfloor
        assert calc_attr.ua_value_gf == approx(58.351477449455686, abs=1e-14)
        assert calc_attr.area_gf == approx(140.0, abs=0.1)
        assert calc_attr.r_conv_inner_gf == approx(0.004201680672268907,
                                                   abs=1e-19)
        assert calc_attr.r_rad_inner_gf == approx(0.001428571428571429,
                                                  abs=1e-18)
        assert calc_attr.r_comb_inner_gf == approx(0.0010660980810234541,
                                                   abs=1e-20)
        assert calc_attr.alpha_conv_inner_gf == approx(1.7, abs=0.00001)
        assert calc_attr.alpha_rad_inner_gf == approx(5.0, abs=0.00001)
        assert calc_attr.alpha_comb_inner_gf == approx(6.7, abs=0.00001)

        # roof/top (rt)
        assert calc_attr.ua_value_rt == approx(57.394603194028036, abs=1e-14)
        assert calc_attr.area_rt == approx(140.0, abs=0.1)
        assert calc_attr.r_conv_inner_rt == approx(0.004201680672268907,
                                                   abs=1e-19)
        assert calc_attr.r_rad_inner_rt == approx(0.001428571428571429,
                                                  abs=1e-18)
        assert calc_attr.r_comb_inner_rt == approx(0.0010660980810234541,
                                                   abs=1e-20)
        assert calc_attr.r_conv_outer_rt == approx(0.00035714285714285714,
                                                   abs=1e-20)
        assert calc_attr.r_rad_outer_rt == approx(0.001428571428571429,
                                                  abs=1e-18)
        assert calc_attr.r_comb_outer_rt == approx(0.00028571428571428574,
                                                   abs=1e-20)
        assert calc_attr.alpha_conv_inner_rt == approx(1.7, abs=0.00001)
        assert calc_attr.alpha_rad_inner_rt == approx(5.0, abs=0.00001)
        assert calc_attr.alpha_comb_inner_rt == approx(6.7, abs=0.00001)
        assert calc_attr.alpha_conv_outer_rt == approx(20.0, abs=0.1)
        assert calc_attr.alpha_rad_outer_rt == approx(5.0, abs=0.00001)
        assert calc_attr.alpha_comb_outer_rt == approx(25.0, abs=0.1)

        # window
        assert calc_attr.ua_value_win == approx(32.87895310796074, abs=1e-14)
        assert calc_attr.area_win == approx(18.0, abs=0.1)
        assert calc_attr.r_conv_inner_win == approx(0.032679738562091505,
                                                    abs=1e-19)
        assert calc_attr.r_rad_inner_win == approx(0.0111, abs=0.0001)
        assert calc_attr.r_comb_inner_win == approx(0.008291873963515755,
                                                    abs=1e-19)
        assert calc_attr.r_conv_outer_win == approx(0.00278, abs=0.00001)
        assert calc_attr.r_rad_outer_win == approx(0.0111, abs=0.0001)
        assert calc_attr.r_comb_outer_win == approx(0.0022, abs=0.0001)
        assert calc_attr.alpha_conv_inner_win == approx(1.7, abs=0.1)
        assert calc_attr.alpha_comb_outer_win == approx(25.0, abs=0.1)
        assert calc_attr.alpha_conv_outer_win == approx(20.0, abs=0.1)
        assert calc_attr.weighted_g_value == approx(0.789, abs=0.001)

    def test_calc_chain_matrix_four(self):
        """test of calc_chain_matrix"""
        from teaser.logic.buildingobjects.calculation.four_element import FourElement

        therm_zone = prj.buildings[-1].thermal_zones[-1]

        calc_attr = FourElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        omega = 2 * math.pi / 86400 / 5

        helplist_outer_walls = therm_zone.outer_walls + therm_zone.windows

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls, omega=omega
        )
        assert round(r1_ow, 14) == 0.00688468914141
        assert round(c1_ow, 5) == 533938.62338

        helplist_inner_walls = (
            therm_zone.inner_walls + therm_zone.ceilings + therm_zone.floors
        )

        r1_iw, c1_iw = calc_attr._calc_parallel_connection(
            element_list=helplist_inner_walls, omega=omega
        )
        assert round(r1_iw, 13) == 0.0097195611408
        assert round(c1_iw, 6) == 319983.518743

    def test_sum_building_elements_one_with_interzonals(self):
        """test of combine_building_elements"""
        prj.set_default()
        helptest.building_test2(prj)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=False)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=True)

        from teaser.logic.buildingobjects.calculation.one_element import OneElement

        therm_zone = prj.buildings[-1].thermal_zones[0]

        calc_attr = OneElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
            + therm_zone.interzonal_elements
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        calc_attr._sum_outer_wall_elements()
        calc_attr._sum_window_elements()

        # outerwall
        assert round(calc_attr.ua_value_ow, 7) == 144.1972679
        assert round(calc_attr.area_ow, 1) == 348.0
        assert round(calc_attr.r_conv_inner_ow, 9) == 0.001539409
        assert round(calc_attr.r_rad_inner_ow, 9) == 0.000574713
        assert round(calc_attr.r_comb_inner_ow, 8) == 0.00041848
        assert round(calc_attr.r_conv_outer_ow, 8) == 0.00026288
        assert round(calc_attr.r_rad_outer_ow, 8) == 0.00096154
        assert round(calc_attr.r_comb_outer_ow, 8) == 0.00020644
        assert round(calc_attr.alpha_conv_inner_ow, 5) == 1.86667
        assert round(calc_attr.alpha_rad_inner_ow, 5) == 5.0
        assert round(calc_attr.alpha_comb_inner_ow, 5) == 6.86667
        assert round(calc_attr.alpha_conv_outer_ow, 7) == 18.2884615
        assert round(calc_attr.alpha_rad_outer_ow, 5) == 5.0
        assert round(calc_attr.alpha_comb_outer_ow, 7) == 23.2884615

        # window
        assert round(calc_attr.ua_value_win, 16) == 32.87895310796074
        assert round(calc_attr.area_win, 1) == 18.0
        assert round(calc_attr.r_conv_inner_win, 19) == 0.032679738562091505
        assert round(calc_attr.r_rad_inner_win, 4) == 0.0111
        assert round(calc_attr.r_comb_inner_win, 19) == 0.008291873963515755
        assert round(calc_attr.r_conv_outer_win, 5) == 0.00278
        assert round(calc_attr.r_rad_outer_win, 4) == 0.0111
        assert round(calc_attr.r_comb_outer_win, 4) == 0.0022
        assert round(calc_attr.alpha_conv_inner_win, 1) == 1.7
        assert round(calc_attr.alpha_comb_outer_win, 1) == 25.0
        assert round(calc_attr.alpha_conv_outer_win, 1) == 20.0
        assert round(calc_attr.weighted_g_value, 3) == 0.789

    def test_calc_chain_matrix_one_with_interzonals(self):
        """test of calc_chain_matrix"""

        from teaser.logic.buildingobjects.calculation.one_element import OneElement

        therm_zone = prj.buildings[-1].thermal_zones[0]

        calc_attr = OneElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
            + therm_zone.interzonal_elements
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        omega = 2 * math.pi / 86400 / 5

        helplist_outer_walls = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.windows
            + therm_zone.find_izes_outer(add_reversed=True)
        )

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls, omega=omega
        )
        assert round(r1_ow, 14) == 0.00093987316367
        assert round(c1_ow, 5) == 8406194.80039

    def test_sum_building_elements_two_with_interzonals(self):
        """test of combine_building_elements"""
        prj.set_default()
        helptest.building_test2(prj)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=False)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=True)

        from teaser.logic.buildingobjects.calculation.two_element import TwoElement

        therm_zone = prj.buildings[-1].thermal_zones[0]

        calc_attr = TwoElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
            + therm_zone.interzonal_elements
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        calc_attr._sum_outer_wall_elements()
        calc_attr._sum_inner_wall_elements()
        calc_attr._sum_window_elements()

        # innerwall
        assert round(calc_attr.ua_value_iw, 8) == 25.26923546
        assert round(calc_attr.area_iw, 1) == 54.0
        assert round(calc_attr.r_conv_inner_iw, 8) == 0.00736377
        assert round(calc_attr.r_rad_inner_iw, 9) == 0.003703704
        assert round(calc_attr.r_comb_inner_iw, 9) == 0.002464268
        assert round(calc_attr.alpha_conv_inner_iw, 9) == 2.514814815
        assert round(calc_attr.alpha_rad_inner_iw, 1) == 5.0
        assert round(calc_attr.alpha_comb_inner_iw, 9) == 7.514814815

        # outerwall
        assert round(calc_attr.ua_value_ow, 7) == 144.1972679
        assert round(calc_attr.area_ow, 1) == 348.0
        assert round(calc_attr.r_conv_inner_ow, 9) == 0.001539409
        assert round(calc_attr.r_rad_inner_ow, 9) == 0.000574713
        assert round(calc_attr.r_comb_inner_ow, 8) == 0.00041848
        assert round(calc_attr.r_conv_outer_ow, 8) == 0.00026288
        assert round(calc_attr.r_rad_outer_ow, 8) == 0.00096154
        assert round(calc_attr.r_comb_outer_ow, 8) == 0.00020644
        assert round(calc_attr.alpha_conv_inner_ow, 5) == 1.86667
        assert round(calc_attr.alpha_rad_inner_ow, 5) == 5.0
        assert round(calc_attr.alpha_comb_inner_ow, 5) == 6.86667
        assert round(calc_attr.alpha_conv_outer_ow, 7) == 18.2884615
        assert round(calc_attr.alpha_rad_outer_ow, 5) == 5.0
        assert round(calc_attr.alpha_comb_outer_ow, 7) == 23.2884615

        # window
        assert round(calc_attr.ua_value_win, 16) == 32.87895310796074
        assert round(calc_attr.area_win, 1) == 18.0
        assert round(calc_attr.r_conv_inner_win, 19) == 0.032679738562091505
        assert round(calc_attr.r_rad_inner_win, 4) == 0.0111
        assert round(calc_attr.r_comb_inner_win, 19) == 0.008291873963515755
        assert round(calc_attr.r_conv_outer_win, 5) == 0.00278
        assert round(calc_attr.r_rad_outer_win, 4) == 0.0111
        assert round(calc_attr.r_comb_outer_win, 4) == 0.0022
        assert round(calc_attr.alpha_conv_inner_win, 1) == 1.7
        assert round(calc_attr.alpha_comb_outer_win, 1) == 25.0
        assert round(calc_attr.alpha_conv_outer_win, 1) == 20.0
        assert round(calc_attr.weighted_g_value, 3) == 0.789

    def test_calc_chain_matrix_two_with_interzonals(self):
        """test of calc_chain_matrix"""
        from teaser.logic.buildingobjects.calculation.two_element import TwoElement

        therm_zone = prj.buildings[-1].thermal_zones[0]

        calc_attr = TwoElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
            + therm_zone.interzonal_elements
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        omega = 2 * math.pi / 86400 / 5

        calc_attr = TwoElement(therm_zone, merge_windows=True, t_bt=5)

        helplist_outer_walls = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.windows
        )

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls, omega=omega, mode='ow'
        )
        assert round(r1_ow, 14) == 0.00100751548411
        assert round(c1_ow, 5) == 3648580.59312

        helplist_inner_elements = (
            therm_zone.inner_walls + therm_zone.ceilings + therm_zone.floors
        )

        r1_iw, c1_iw = calc_attr._calc_parallel_connection(
            element_list=helplist_inner_elements, omega=omega,
            mode='iw'
        )
        assert round(r1_iw, 13) == 0.0097195611408
        assert round(c1_iw, 6) == 319983.518743

        helplist_outer_walls_with_nzb = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.windows
            + therm_zone.find_izes_outer(add_reversed=True)
        )

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls_with_nzb, omega=omega, mode='ow'
        )
        assert round(r1_ow, 14) == 0.00093987316367
        assert round(c1_ow, 5) == 8406194.80039

        helplist_inner_elements_with_nzb = (
            therm_zone.inner_walls + therm_zone.ceilings
            + therm_zone.floors + calc_attr.nzbs_for_iw
        )

        r1_iw_2, c1_iw_2 = calc_attr._calc_parallel_connection(
            element_list=helplist_inner_elements_with_nzb, omega=omega,
            mode='iw'
        )
        assert round(r1_iw_2, 13) == 0.0060615482113
        assert round(c1_iw_2, 6) == 1038852.970991

    def test_sum_building_elements_three_with_interzonals(self):
        """test of combine_building_elements"""
        prj.set_default()
        helptest.building_test2(prj)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=False)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=True)

        from teaser.logic.buildingobjects.calculation.three_element import ThreeElement

        therm_zone = prj.buildings[-1].thermal_zones[0]

        calc_attr = ThreeElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
            + therm_zone.interzonal_elements
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        calc_attr._sum_outer_wall_elements()
        calc_attr._sum_ground_floor_elements()
        calc_attr._sum_inner_wall_elements()
        calc_attr._sum_window_elements()

        # innerwall
        assert round(calc_attr.ua_value_iw, 8) == 25.26923546
        assert round(calc_attr.area_iw, 1) == 54.0
        assert round(calc_attr.r_conv_inner_iw, 8) == 0.00736377
        assert round(calc_attr.r_rad_inner_iw, 9) == 0.003703704
        assert round(calc_attr.r_comb_inner_iw, 9) == 0.002464268
        assert round(calc_attr.alpha_conv_inner_iw, 9) == 2.514814815
        assert round(calc_attr.alpha_rad_inner_iw, 1) == 5.0
        assert round(calc_attr.alpha_comb_inner_iw, 9) == 7.514814815

        # outerwall
        assert round(calc_attr.ua_value_ow, 8) == 85.84579041
        assert round(calc_attr.area_ow, 1) == 208.0
        assert round(calc_attr.r_conv_inner_ow, 9) == 0.002429543
        assert round(calc_attr.r_rad_inner_ow, 9) == 0.000961538
        assert round(calc_attr.r_comb_inner_ow, 9) == 0.000688895
        assert round(calc_attr.r_conv_outer_ow, 8) == 0.00026288
        assert round(calc_attr.r_rad_outer_ow, 8) == 0.00096154
        assert round(calc_attr.r_comb_outer_ow, 8) == 0.00020644
        assert round(calc_attr.alpha_conv_inner_ow, 9) == 1.978846154
        assert round(calc_attr.alpha_rad_inner_ow, 5) == 5.0
        assert round(calc_attr.alpha_comb_inner_ow, 9) == 6.978846154
        assert round(calc_attr.alpha_conv_outer_ow, 7) == 18.2884615
        assert round(calc_attr.alpha_rad_outer_ow, 5) == 5.0
        assert round(calc_attr.alpha_comb_outer_ow, 7) == 23.2884615

        # groundfloor
        assert round(calc_attr.ua_value_gf, 16) == 58.351477449455686
        assert round(calc_attr.area_gf, 1) == 140.0
        assert round(calc_attr.r_conv_inner_gf, 19) == 0.004201680672268907
        assert round(calc_attr.r_rad_inner_gf, 18) == 0.001428571428571429
        assert round(calc_attr.r_comb_inner_gf, 20) == 0.0010660980810234541
        assert round(calc_attr.alpha_conv_inner_gf, 5) == 1.7
        assert round(calc_attr.alpha_rad_inner_gf, 5) == 5.0
        assert round(calc_attr.alpha_comb_inner_gf, 5) == 6.7

        # window
        assert round(calc_attr.ua_value_win, 16) == 32.87895310796074
        assert round(calc_attr.area_win, 1) == 18.0
        assert round(calc_attr.r_conv_inner_win, 19) == 0.032679738562091505
        assert round(calc_attr.r_rad_inner_win, 4) == 0.0111
        assert round(calc_attr.r_comb_inner_win, 19) == 0.008291873963515755
        assert round(calc_attr.r_conv_outer_win, 5) == 0.00278
        assert round(calc_attr.r_rad_outer_win, 4) == 0.0111
        assert round(calc_attr.r_comb_outer_win, 4) == 0.0022
        assert round(calc_attr.alpha_conv_inner_win, 1) == 1.7
        assert round(calc_attr.alpha_comb_outer_win, 1) == 25.0
        assert round(calc_attr.alpha_conv_outer_win, 1) == 20.0
        assert round(calc_attr.weighted_g_value, 3) == 0.789

    def test_calc_chain_matrix_three_with_interzonals(self):
        """test of calc_chain_matrix"""
        from teaser.logic.buildingobjects.calculation.three_element import ThreeElement

        therm_zone = prj.buildings[-1].thermal_zones[0]

        calc_attr = ThreeElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
            + therm_zone.interzonal_elements
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        omega = 2 * math.pi / 86400 / 5

        helplist_outer_walls = (
            therm_zone.outer_walls + therm_zone.rooftops + therm_zone.windows
        )

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls, omega=omega, mode='ow'
        )
        assert round(r1_ow, 14) == 0.00175779297228
        assert round(c1_ow, 5) == 2091259.60825

        helplist_inner_walls = (
            therm_zone.inner_walls + therm_zone.ceilings + therm_zone.floors
        )

        r1_iw, c1_iw = calc_attr._calc_parallel_connection(
            element_list=helplist_inner_walls, omega=omega, mode='iw'
        )
        assert round(r1_iw, 13) == 0.0097195611408
        assert round(c1_iw, 6) == 319983.518743

        helplist_outer_walls_with_nzb = (
            therm_zone.outer_walls + therm_zone.rooftops + therm_zone.windows
            + therm_zone.find_izes_outer(add_reversed=True)
        )

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls_with_nzb, omega=omega, mode='ow'
        )
        assert round(r1_ow, 14) == 0.00129426438757
        assert round(c1_ow, 5) == 6856087.1177

        helplist_inner_elements_with_nzb = (
            therm_zone.inner_walls + therm_zone.ceilings
            + therm_zone.floors + calc_attr.nzbs_for_iw
        )

        r1_iw_2, c1_iw_2 = calc_attr._calc_parallel_connection(
            element_list=helplist_inner_elements_with_nzb, omega=omega,
            mode='iw'
        )
        assert round(r1_iw_2, 13) == 0.0060615482113
        assert round(c1_iw_2, 6) == 1038852.970991

    def test_sum_building_elements_four_with_interzonals(self):
        """test of combine_building_elements"""
        prj.set_default()
        helptest.building_test2(prj)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=False)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=True)

        from teaser.logic.buildingobjects.calculation.four_element \
            import FourElement

        therm_zone = prj.buildings[-1].thermal_zones[0]

        calc_attr = FourElement(therm_zone, merge_windows=True, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
            + therm_zone.interzonal_elements
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        calc_attr._sum_outer_wall_elements()
        calc_attr._sum_ground_floor_elements()
        calc_attr._sum_rooftop_elements()
        calc_attr._sum_inner_wall_elements()
        calc_attr._sum_window_elements()

        # innerwall
        assert round(calc_attr.ua_value_iw, 8) == 25.26923546
        assert round(calc_attr.area_iw, 1) == 54.0
        assert round(calc_attr.r_conv_inner_iw, 8) == 0.00736377
        assert round(calc_attr.r_rad_inner_iw, 9) == 0.003703704
        assert round(calc_attr.r_comb_inner_iw, 9) == 0.002464268
        assert round(calc_attr.alpha_conv_inner_iw, 9) == 2.514814815
        assert round(calc_attr.alpha_rad_inner_iw, 1) == 5.0
        assert round(calc_attr.alpha_comb_inner_iw, 9) == 7.514814815

        # outerwall
        assert round(calc_attr.ua_value_ow, 8) == 28.45118721
        assert round(calc_attr.area_ow, 1) == 68.0
        assert round(calc_attr.r_conv_inner_ow, 9) == 0.005760369
        assert round(calc_attr.r_rad_inner_ow, 9) == 0.002941176
        assert round(calc_attr.r_comb_inner_ow, 8) == 0.00194704
        assert round(calc_attr.r_conv_outer_ow, 9) == 0.000996016
        assert round(calc_attr.r_rad_outer_ow, 9) == 0.002941176
        assert round(calc_attr.r_comb_outer_ow, 9) == 0.000744048
        assert round(calc_attr.alpha_conv_inner_ow, 9) == 2.552941176
        assert round(calc_attr.alpha_rad_inner_ow, 5) == 5.0
        assert round(calc_attr.alpha_comb_inner_ow, 9) == 7.552941176
        assert round(calc_attr.alpha_conv_outer_ow, 8) == 14.76470588
        assert round(calc_attr.alpha_rad_outer_ow, 5) == 5.0
        assert round(calc_attr.alpha_comb_outer_ow, 8) == 19.76470588

        # groundfloor
        assert round(calc_attr.ua_value_gf, 16) == 58.351477449455686
        assert round(calc_attr.area_gf, 1) == 140.0
        assert round(calc_attr.r_conv_inner_gf, 19) == 0.004201680672268907
        assert round(calc_attr.r_rad_inner_gf, 18) == 0.001428571428571429
        assert round(calc_attr.r_comb_inner_gf, 20) == 0.0010660980810234541
        assert round(calc_attr.alpha_conv_inner_gf, 5) == 1.7
        assert round(calc_attr.alpha_rad_inner_gf, 5) == 5.0
        assert round(calc_attr.alpha_comb_inner_gf, 5) == 6.7

        # outerwall
        assert round(calc_attr.ua_value_rt, 16) == 57.394603194028036
        assert round(calc_attr.area_rt, 1) == 140.0
        assert round(calc_attr.r_conv_inner_rt, 19) == 0.004201680672268907
        assert round(calc_attr.r_rad_inner_rt, 18) == 0.001428571428571429
        assert round(calc_attr.r_comb_inner_rt, 20) == 0.0010660980810234541
        assert round(calc_attr.r_conv_outer_rt, 20) == 0.00035714285714285714
        assert round(calc_attr.r_rad_outer_rt, 18) == 0.001428571428571429
        assert round(calc_attr.r_comb_outer_rt, 20) == 0.00028571428571428574
        assert round(calc_attr.alpha_conv_inner_rt, 5) == 1.7
        assert round(calc_attr.alpha_rad_inner_rt, 5) == 5.0
        assert round(calc_attr.alpha_comb_inner_rt, 5) == 6.7
        assert round(calc_attr.alpha_conv_outer_rt, 1) == 20.0
        assert round(calc_attr.alpha_rad_outer_rt, 5) == 5.0
        assert round(calc_attr.alpha_comb_outer_rt, 1) == 25.0

        # window
        assert round(calc_attr.ua_value_win, 16) == 32.87895310796074
        assert round(calc_attr.area_win, 1) == 18.0
        assert round(calc_attr.r_conv_inner_win, 19) == 0.032679738562091505
        assert round(calc_attr.r_rad_inner_win, 4) == 0.0111
        assert round(calc_attr.r_comb_inner_win, 19) == 0.008291873963515755
        assert round(calc_attr.r_conv_outer_win, 5) == 0.00278
        assert round(calc_attr.r_rad_outer_win, 4) == 0.0111
        assert round(calc_attr.r_comb_outer_win, 4) == 0.0022
        assert round(calc_attr.alpha_conv_inner_win, 1) == 1.7
        assert round(calc_attr.alpha_comb_outer_win, 1) == 25.0
        assert round(calc_attr.alpha_conv_outer_win, 1) == 20.0
        assert round(calc_attr.weighted_g_value, 3) == 0.789

    def test_calc_chain_matrix_four_with_interzonals(self):
        """test of calc_chain_matrix"""
        from teaser.logic.buildingobjects.calculation.four_element \
            import FourElement

        therm_zone = prj.buildings[-1].thermal_zones[0]

        calc_attr = FourElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
            + therm_zone.interzonal_elements
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        omega = 2 * math.pi / 86400 / 5

        helplist_outer_walls = therm_zone.outer_walls + therm_zone.windows

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls, omega=omega, mode='ow'
        )
        assert round(r1_ow, 14) == 0.00688468914141
        assert round(c1_ow, 5) == 533938.62338

        helplist_inner_walls = (
            therm_zone.inner_walls + therm_zone.ceilings + therm_zone.floors
        )

        r1_iw, c1_iw = calc_attr._calc_parallel_connection(
            element_list=helplist_inner_walls, omega=omega, mode='iw'
        )
        assert round(r1_iw, 13) == 0.0097195611408
        assert round(c1_iw, 6) == 319983.518743

        helplist_outer_walls_with_nzb = (
                therm_zone.outer_walls
                + therm_zone.windows
                + therm_zone.find_izes_outer(add_reversed=True)
        )

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls_with_nzb, omega=omega, mode='ow'
        )
        assert round(r1_ow, 14) == 0.00196382289565
        assert round(c1_ow, 5) == 5310295.24128

        helplist_inner_elements_with_nzb = (
            therm_zone.inner_walls + therm_zone.ceilings
            + therm_zone.floors + calc_attr.nzbs_for_iw
        )

        r1_iw_2, c1_iw_2 = calc_attr._calc_parallel_connection(
            element_list=helplist_inner_elements_with_nzb, omega=omega,
            mode='iw'
        )
        assert round(r1_iw_2, 13) == 0.0060615482113
        assert round(c1_iw_2, 6) == 1038852.970991

    def test_calc_weightfactor_one(self):
        """test of calc_weightfactor"""
        prj.set_default()
        helptest.building_test2(prj)
        prj.buildings[-1].calc_building_parameter(
            number_of_elements=1, merge_windows=True, used_library="IBPSA"
        )

        calc_attr = prj.buildings[-1].thermal_zones[-1].model_attr

        weightfactors_test_list = [
            0,
            0.024530650180761254,
            0.03434291025306576,
            0.024530650180761254,
            0.03434291025306576,
            0.3407000330729792,
        ]

        calc_attr.weightfactor_ow.sort()
        weightfactors_test_list.sort()

        assert calc_attr.weightfactor_ow == weightfactors_test_list

        weightfactors_test_list = [
            0.08674342795625017,
            0.0,
            0.0,
            0.0,
            0.054214642472656345,
            0.054214642472656345,
        ]
        calc_attr.weightfactor_win.sort()
        weightfactors_test_list.sort()

        assert calc_attr.weightfactor_win == weightfactors_test_list
        assert calc_attr.weightfactor_ground == 0.34638013315780397

        prj.buildings[-1].thermal_zones[-1].weightfactor_ow = []
        prj.buildings[-1].thermal_zones[-1].weightfactor_win = []

        prj.buildings[-1].calc_building_parameter(
            number_of_elements=1, merge_windows=False, used_library="AixLib"
        )
        calc_attr = prj.buildings[-1].thermal_zones[-1].model_attr

        weightfactors_test_list = [
            0.03047939672771178,
            0.423320678280269,
            0.03047939672771178,
            0.0,
            0.04267115541879649,
            0.04267115541879649,
        ]
        calc_attr.weightfactor_ow.sort()
        weightfactors_test_list.sort()

        assert calc_attr.weightfactor_ow == weightfactors_test_list

        weightfactors_test_list = [
            0.44444444444444453,
            0.0,
            0.0,
            0.0,
            0.2777777777777778,
            0.2777777777777778,
        ]

        calc_attr.weightfactor_win.sort()
        weightfactors_test_list.sort()
        assert calc_attr.weightfactor_win.sort() == weightfactors_test_list.sort()
        assert calc_attr.weightfactor_ground == 0.4303782174267145

    def test_calc_weightfactor_two(self):
        """test of calc_weightfactor"""
        prj.set_default()
        helptest.building_test2(prj)
        prj.buildings[-1].calc_building_parameter(
            number_of_elements=2, merge_windows=True, used_library="IBPSA"
        )

        calc_attr = prj.buildings[-1].thermal_zones[-1].model_attr

        weightfactors_test_list = [
            0.0,
            0.024530650180761254,
            0.03434291025306576,
            0.024530650180761254,
            0.03434291025306576,
            0.3407000330729792,
        ]
        calc_attr.weightfactor_ow.sort()
        weightfactors_test_list.sort()

        assert calc_attr.weightfactor_ow == weightfactors_test_list
        weightfactors_test_list = [
            0.0,
            0.0,
            0.054214642472656345,
            0.08674342795625017,
            0.054214642472656345,
            0.0,
        ]
        calc_attr.weightfactor_win.sort()
        weightfactors_test_list.sort()
        assert calc_attr.weightfactor_win == weightfactors_test_list
        assert calc_attr.weightfactor_ground == 0.34638013315780397

        prj.buildings[-1].thermal_zones[-1].weightfactor_ow = []
        prj.buildings[-1].thermal_zones[-1].weightfactor_win = []

        prj.buildings[-1].calc_building_parameter(
            number_of_elements=2, merge_windows=False, used_library="AixLib"
        )
        calc_attr = prj.buildings[-1].thermal_zones[-1].model_attr

        weightfactors_test_list = [
            0.0,
            0.03047939672771178,
            0.04267115541879649,
            0.03047939672771178,
            0.04267115541879649,
            0.423320678280269,
        ]
        calc_attr.weightfactor_ow.sort()
        weightfactors_test_list.sort()
        assert calc_attr.weightfactor_ow == weightfactors_test_list

        weightfactors_test_list = [
            0.0,
            0.0,
            0.27777777777777778,
            0.44444444444444453,
            0.27777777777777778,
            0.0,
        ]

        calc_attr.weightfactor_win.sort()
        weightfactors_test_list.sort()
        assert calc_attr.weightfactor_win == weightfactors_test_list
        assert calc_attr.weightfactor_ground == 0.4303782174267145

    def test_calc_weightfactor_three(self):
        """test of calc_weightfactor"""

        prj.set_default()
        helptest.building_test2(prj)
        prj.buildings[-1].calc_building_parameter(
            number_of_elements=3, merge_windows=True, used_library="IBPSA"
        )

        calc_attr = prj.buildings[-1].thermal_zones[-1].model_attr
        weightfactors_test_list = [
            0.03753045374718346,
            0.5212510365068732,
            0.05254263524605685,
            0.03753045374718346,
            0.05254263524605685,
        ]
        calc_attr.weightfactor_ow.sort()
        weightfactors_test_list.sort()

        assert calc_attr.weightfactor_ow == approx(weightfactors_test_list,
                                                   abs=1e-14)

        weightfactors_test_list = [
            0.13271234911406493,
            0.0,
            0.08294521819629057,
            0.0,
            0.08294521819629057,
        ]
        calc_attr.weightfactor_win.sort()
        weightfactors_test_list.sort()
        assert calc_attr.weightfactor_win == approx(weightfactors_test_list,
                                                    abs=1e-14)
        assert calc_attr.weightfactor_ground == 0

        prj.buildings[-1].thermal_zones[-1].weightfactor_ow = []
        prj.buildings[-1].thermal_zones[-1].weightfactor_win = []

        prj.buildings[-1].calc_building_parameter(
            number_of_elements=3, merge_windows=False, used_library="AixLib"
        )
        calc_attr = prj.buildings[-1].thermal_zones[-1].model_attr

        weightfactors_test_list = [
            0.05350813058801943,
            0.7431609731775066,
            0.07491138282322722,
            0.05350813058801943,
            0.07491138282322722,
        ]

        calc_attr.weightfactor_ow.sort()
        weightfactors_test_list.sort()

        assert calc_attr.weightfactor_ow == approx(weightfactors_test_list,
                                                   abs=1e-14)

        weightfactors_test_list = [
            0.44444444444444453,
            0.0,
            0.2777777777777778,
            0.0,
            0.2777777777777778,
        ]
        calc_attr.weightfactor_win.sort()
        weightfactors_test_list.sort()
        assert calc_attr.weightfactor_win == approx(weightfactors_test_list,
                                                    abs=1e-14)
        assert calc_attr.weightfactor_ground == 0

    def test_calc_weightfactor_four(self):
        """test of calc_weightfactor"""
        prj.set_default()
        helptest.building_test2(prj)
        prj.buildings[-1].calc_building_parameter(
            number_of_elements=4, merge_windows=True, used_library="IBPSA"
        )

        calc_attr = prj.buildings[-1].thermal_zones[-1].model_attr

        weightfactors_test_list = [
            0.07839276240589141,
            0.10974986736824797,
            0.07839276240589141,
            0.10974986736824797,
        ]

        calc_attr.weightfactor_ow.sort()
        weightfactors_test_list.sort()

        assert calc_attr.weightfactor_ow == weightfactors_test_list
        weightfactors_test_list = [
            0.27720655131187616,
            0.17325409456992255,
            0.0,
            0.17325409456992255,
        ]
        calc_attr.weightfactor_win.sort()
        weightfactors_test_list.sort()
        assert calc_attr.weightfactor_win == weightfactors_test_list
        assert calc_attr.weightfactor_ground == 0
        assert calc_attr.weightfactor_rt == [1]

        prj.buildings[-1].thermal_zones[-1].weightfactor_ow = []
        prj.buildings[-1].thermal_zones[-1].weightfactor_win = []

        prj.buildings[-1].calc_building_parameter(
            number_of_elements=4, merge_windows=False, used_library="AixLib"
        )
        calc_attr = prj.buildings[-1].thermal_zones[-1].model_attr

        weightfactors_test_list = [
            0.20833333333333331,
            0.29166666666666663,
            0.20833333333333331,
            0.29166666666666663,
        ]
        calc_attr.weightfactor_ow.sort()
        weightfactors_test_list.sort()
        assert calc_attr.weightfactor_ow == weightfactors_test_list

        weightfactors_test_list = [
            0.44444444444444453,
            0.2777777777777778,
            0.0,
            0.2777777777777778,
        ]

        calc_attr.weightfactor_win.sort()
        weightfactors_test_list.sort()
        assert calc_attr.weightfactor_win == weightfactors_test_list
        assert calc_attr.weightfactor_ground == 0
        assert calc_attr.weightfactor_rt == [1]

    def test_calc_one_element(self):
        """test of calc_two_element"""
        prj.set_default()
        helptest.building_test2(prj)

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.calc_zone_parameters(number_of_elements=1, merge_windows=True)

        zone_attr = therm_zone.model_attr
        assert round(zone_attr.area_ow, 1) == 328.0
        assert round(zone_attr.ua_value_ow, 16) == 135.5818558809656
        assert round(zone_attr.r_conv_inner_ow, 16) == 0.0016512549537649
        assert round(zone_attr.r_rad_inner_ow, 16) == 0.000609756097561

        assert round(zone_attr.r_conv_outer_ow, 9) == 0.000265957
        assert round(zone_attr.alpha_conv_inner_ow, 5) == 1.84634
        assert round(zone_attr.alpha_rad_inner_ow, 1) == 5.0
        assert round(zone_attr.r1_ow, 15) == 0.000772773294534
        assert round(zone_attr.c1_ow, 5) == 3648580.59312
        assert round(zone_attr.r_rest_ow, 14) == 0.00461875570532

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.calc_zone_parameters(number_of_elements=1, merge_windows=False)

        zone_attr = therm_zone.model_attr
        assert round(zone_attr.area_ow, 1) == 328.0
        assert round(zone_attr.ua_value_ow, 16) == 135.5818558809656
        assert round(zone_attr.r_conv_inner_ow, 16) == 0.0016512549537649
        assert round(zone_attr.r_rad_inner_ow, 16) == 0.000609756097561

        assert round(zone_attr.r_conv_outer_ow, 9) == 0.000265957
        assert round(zone_attr.alpha_conv_inner_ow, 5) == 1.84634
        assert round(zone_attr.alpha_rad_inner_ow, 1) == 5.0
        assert round(zone_attr.r1_win, 13) == 0.0199004975124
        assert round(zone_attr.r1_ow, 15) == 0.001007515484109
        assert round(zone_attr.c1_ow, 5) == 3648580.59312
        assert round(zone_attr.r_rest_ow, 14) == 0.00585224061345

    def test_calc_two_element(self):
        """test of calc_two_element"""
        prj.set_default()
        helptest.building_test2(prj)

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.calc_zone_parameters(number_of_elements=2, merge_windows=True)

        zone_attr = therm_zone.model_attr
        assert round(zone_attr.area_ow, 1) == 328.0
        assert round(zone_attr.ua_value_ow, 16) == 135.5818558809656
        assert round(zone_attr.r_conv_inner_ow, 16) == 0.0016512549537649
        assert round(zone_attr.r_rad_inner_ow, 16) == 0.000609756097561
        assert round(zone_attr.r_conv_outer_ow, 9) == 0.000265957
        assert round(zone_attr.alpha_conv_inner_ow, 5) == 1.84634
        assert round(zone_attr.alpha_rad_inner_ow, 1) == 5.0
        assert round(zone_attr.r1_ow, 15) == 0.000772773294534
        assert round(zone_attr.c1_ow, 5) == 3648580.59312
        assert round(zone_attr.r1_iw, 15) == 0.009719561140816
        assert round(zone_attr.c1_iw, 5) == 319983.51874

        assert round(zone_attr.r_rest_ow, 14) == 0.00461875570532

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.calc_zone_parameters(number_of_elements=2, merge_windows=False)

        zone_attr = therm_zone.model_attr
        assert round(zone_attr.area_ow, 1) == 328.0
        assert round(zone_attr.ua_value_ow, 16) == 135.5818558809656
        assert round(zone_attr.r_conv_inner_ow, 16) == 0.0016512549537649
        assert round(zone_attr.r_rad_inner_ow, 16) == 0.000609756097561
        assert round(zone_attr.r_conv_outer_ow, 9) == 0.000265957
        assert round(zone_attr.alpha_conv_inner_ow, 5) == 1.84634
        assert round(zone_attr.alpha_rad_inner_ow, 1) == 5.0
        assert round(zone_attr.r1_win, 13) == 0.0199004975124
        assert round(zone_attr.r1_ow, 15) == 0.001007515484109
        assert round(zone_attr.c1_ow, 5) == 3648580.59312
        assert round(zone_attr.r1_iw, 15) == 0.009719561140816
        assert round(zone_attr.r_rest_ow, 14) == 0.00585224061345

    def test_calc_three_element(self):
        """test of calc_three_element"""
        prj.set_default()
        helptest.building_test2(prj)

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.calc_zone_parameters(number_of_elements=3,
                                        merge_windows=True)

        zone_attr = therm_zone.model_attr
        assert zone_attr.area_ow == approx(188.0, abs=0.1)
        assert zone_attr.ua_value_ow == approx(77.23037843150993, abs=1e-13)
        assert zone_attr.r_conv_inner_ow == approx(0.0027203482045702,
                                                   abs=1e-14)
        assert zone_attr.r_rad_inner_ow == approx(0.001063829787234, abs=1e-14)
        assert zone_attr.r_conv_outer_ow == approx(0.000265957, abs=1e-9)
        assert zone_attr.alpha_conv_inner_ow == approx(1.95532, abs=0.00001)
        assert zone_attr.alpha_rad_inner_ow == approx(5.0, abs=0.1)
        assert zone_attr.r1_ow == approx(0.00114890338306, abs=1e-14)
        assert zone_attr.c1_ow == approx(2091259.60825, abs=0.00001)
        assert zone_attr.r1_iw == approx(0.009719561140816, abs=1e-15)
        assert zone_attr.c1_iw == approx(319983.51874, abs=0.00001)
        assert zone_attr.r_rest_ow == approx(0.00702003101, abs=1e-11)
        assert zone_attr.area_gf == approx(140.0, abs=0.1)
        assert zone_attr.ua_value_gf == approx(58.351477449455686, abs=1e-14)
        assert zone_attr.r_conv_inner_gf == approx(0.0042016806722689,
                                                   abs=1e-14)
        assert zone_attr.r_rad_inner_gf == approx(0.0014285714285714,
                                                  abs=1e-14)
        assert zone_attr.alpha_conv_inner_gf == approx(1.7, abs=0.00001)
        assert zone_attr.alpha_rad_inner_gf == approx(5.0, abs=0.1)
        assert zone_attr.r1_gf == approx(0.00236046484848, abs=1e-14)
        assert zone_attr.c1_gf == approx(1557320.98487, abs=0.00001)
        assert zone_attr.r_rest_gf == approx(0.0137109637229, abs=1e-13)

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.calc_zone_parameters(number_of_elements=3,
                                        merge_windows=False)

        zone_attr = therm_zone.model_attr
        assert zone_attr.area_ow == approx(188.0, abs=0.1)
        assert zone_attr.ua_value_ow == approx(77.23037843150993, abs=1e-13)
        assert zone_attr.r_conv_inner_ow == approx(0.0027203482045702,
                                                   abs=1e-14)
        assert zone_attr.r_rad_inner_ow == approx(0.001063829787234, abs=1e-14)
        assert zone_attr.r_conv_outer_ow == approx(0.000265957, abs=1e-9)
        assert zone_attr.alpha_conv_inner_ow == approx(1.95532, abs=0.00001)
        assert zone_attr.alpha_rad_inner_ow == approx(5.0, abs=0.1)
        assert zone_attr.r1_win == approx(0.0199004975124, abs=1e-13)
        assert zone_attr.r1_ow == approx(0.0017577929723, abs=1e-13)
        assert zone_attr.c1_ow == approx(2091259.60825, abs=0.00001)
        assert zone_attr.r1_iw == approx(0.009719561140816, abs=1e-15)
        assert zone_attr.c1_iw == approx(319983.51874, abs=0.00001)
        assert zone_attr.r_rest_ow == approx(0.0102102921341, abs=1e-13)
        assert zone_attr.area_gf == approx(140.0, abs=0.1)
        assert zone_attr.ua_value_gf == approx(58.351477449455686, abs=1e-14)
        assert zone_attr.r_conv_inner_gf == approx(0.0042016806722689,
                                                   abs=1e-14)
        assert zone_attr.r_rad_inner_gf == approx(0.0014285714285714,
                                                  abs=1e-14)
        assert zone_attr.alpha_conv_inner_gf == approx(1.7, abs=0.00001)
        assert zone_attr.alpha_rad_inner_gf == approx(5.0, abs=0.1)
        assert zone_attr.r1_gf == approx(0.00236046484848, abs=1e-14)
        assert zone_attr.c1_gf == approx(1557320.98487, abs=0.00001)
        assert zone_attr.r_rest_gf == approx(0.0137109637229, abs=1e-13)

    def test_calc_four_element(self):
        """test of calc_four_element"""
        prj.set_default()
        helptest.building_test2(prj)

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.calc_zone_parameters(number_of_elements=4, merge_windows=True)

        zone_attr = therm_zone.model_attr
        assert round(zone_attr.area_ow, 1) == 48.0
        assert round(zone_attr.ua_value_ow, 16) == 19.83577523748189
        assert round(zone_attr.r_conv_inner_ow, 16) == 0.007716049382716
        assert round(zone_attr.r_rad_inner_ow, 16) == 0.0041666666666667
        assert round(zone_attr.r_conv_outer_ow, 9) == 0.001041667
        assert round(zone_attr.alpha_conv_inner_ow, 5) == 2.7
        assert round(zone_attr.alpha_rad_inner_ow, 1) == 5.0
        assert round(zone_attr.r1_ow, 14) == 0.00223838915931
        assert round(zone_attr.c1_ow, 5) == 533938.62338
        assert round(zone_attr.r1_iw, 14) == 0.00971956114082
        assert round(zone_attr.c1_iw, 5) == 319983.51874
        assert round(zone_attr.r_rest_ow, 13) == 0.0138583242416
        assert round(zone_attr.area_gf, 1) == 140.0
        assert round(zone_attr.ua_value_gf, 16) == 58.351477449455686
        assert round(zone_attr.r_conv_inner_gf, 16) == 0.0042016806722689
        assert round(zone_attr.r_rad_inner_gf, 16) == 0.0014285714285714
        assert round(zone_attr.alpha_conv_inner_gf, 5) == 1.7
        assert round(zone_attr.alpha_rad_inner_gf, 1) == 5.0
        assert round(zone_attr.r1_gf, 14) == 0.00236046484848
        assert round(zone_attr.c1_gf, 5) == 1557320.98487
        assert round(zone_attr.r_rest_gf, 13) == 0.0137109637229

        assert round(zone_attr.area_rt, 1) == 140.0
        assert round(zone_attr.ua_value_rt, 16) == 57.394603194028036
        assert round(zone_attr.r_conv_inner_rt, 16) == 0.0042016806722689
        assert round(zone_attr.r_rad_inner_rt, 16) == 0.0014285714285714
        assert round(zone_attr.r_conv_outer_rt, 9) == 0.000357143
        assert round(zone_attr.alpha_conv_inner_rt, 5) == 1.7
        assert round(zone_attr.alpha_rad_inner_rt, 1) == 5.0
        assert round(zone_attr.r1_rt, 14) == 0.00236046484848
        assert round(zone_attr.c1_rt, 5) == 1557320.98487
        assert round(zone_attr.r_rest_rt, 13) == 0.0137109637229

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.calc_zone_parameters(number_of_elements=4, merge_windows=False)

        zone_attr = therm_zone.model_attr
        assert round(zone_attr.area_ow, 1) == 48.0
        assert round(zone_attr.ua_value_ow, 16) == 19.83577523748189
        assert round(zone_attr.r_conv_inner_ow, 16) == 0.007716049382716
        assert round(zone_attr.r_rad_inner_ow, 16) == 0.0041666666666667
        assert round(zone_attr.r_conv_outer_ow, 9) == 0.001041667
        assert round(zone_attr.alpha_conv_inner_ow, 5) == 2.7
        assert round(zone_attr.alpha_rad_inner_ow, 1) == 5.0
        assert round(zone_attr.r1_win, 13) == 0.0199004975124
        assert round(zone_attr.r1_ow, 14) == 0.00688468914141
        assert round(zone_attr.c1_ow, 5) == 533938.62338
        assert round(zone_attr.r1_iw, 14) == 0.00971956114082
        assert round(zone_attr.c1_iw, 5) == 319983.51874
        assert round(zone_attr.r_rest_ow, 13) == 0.0399903108586

        assert round(zone_attr.area_gf, 1) == 140.0
        assert round(zone_attr.ua_value_gf, 16) == 58.351477449455686
        assert round(zone_attr.r_conv_inner_gf, 16) == 0.0042016806722689
        assert round(zone_attr.r_rad_inner_gf, 16) == 0.0014285714285714
        assert round(zone_attr.alpha_conv_inner_gf, 5) == 1.7
        assert round(zone_attr.alpha_rad_inner_gf, 1) == 5.0
        assert round(zone_attr.r1_gf, 14) == 0.00236046484848
        assert round(zone_attr.c1_gf, 5) == 1557320.98487
        assert round(zone_attr.r_rest_gf, 13) == 0.0137109637229

        assert round(zone_attr.area_rt, 1) == 140.0
        assert round(zone_attr.ua_value_rt, 16) == 57.394603194028036
        assert round(zone_attr.r_conv_inner_rt, 16) == 0.0042016806722689
        assert round(zone_attr.r_rad_inner_rt, 16) == 0.0014285714285714
        assert round(zone_attr.r_conv_outer_rt, 9) == 0.000357143
        assert round(zone_attr.alpha_conv_inner_rt, 5) == 1.7
        assert round(zone_attr.alpha_rad_inner_rt, 1) == 5.0
        assert round(zone_attr.r1_rt, 14) == 0.00236046484848
        assert round(zone_attr.c1_rt, 5) == 1557320.98487
        assert round(zone_attr.r_rest_rt, 13) == 0.0137109637229

    def test_volume_zone(self):
        """test of volume_zone"""

        prj.buildings[-1].thermal_zones[-1].set_volume_zone()
        assert prj.buildings[-1].thermal_zones[-1].volume == 490.0

    def test_set_inner_wall_area(self):
        """test of set_inner_wall_area"""
        prj.buildings[-1].inner_wall_approximation_approach \
            = 'typical_minus_outer'
        prj.buildings[-1].thermal_zones[-1].set_inner_wall_area()
        for wall in prj.buildings[-1].thermal_zones[-1].inner_walls:
            assert round(wall.area, 16) == 99.65023392678924
        prj.buildings[-1].inner_wall_approximation_approach \
            = 'typical_minus_outer_extended'
        prj.buildings[-1].thermal_zones[-1].set_inner_wall_area()
        for wall in prj.buildings[-1].thermal_zones[-1].inner_walls:
            assert round(wall.area, 16) == 99.65023392678924
        prj.buildings[-1].inner_wall_approximation_approach = 'teaser_default'
        prj.buildings[-1].thermal_zones[-1].set_inner_wall_area()
        for wall in prj.buildings[-1].thermal_zones[-1].inner_walls:
            assert round(wall.area, 16) == 11.951219512195122
        # methods in BuildingElement

    def test_ua_value(self):
        """test of ua_value"""
        prj.set_default(load_data=False)
        helptest.building_test2(prj)

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].calc_ua_value()

        assert round(therm_zone.outer_walls[0].ua_value, 15) == 4.132453174475393

    def test_gather_element_properties(self):
        """test of gather_element_properties"""
        outerWalls = prj.buildings[-1].thermal_zones[-1].outer_walls[0]
        number_of_layer, density, thermal_conduc, heat_capac, thickness = (
            outerWalls.gather_element_properties()
        )
        assert number_of_layer == 2
        assert (density == [5.0, 2.0]).all()
        assert (thermal_conduc == [4.0, 2.0]).all()
        assert (heat_capac == [0.48, 0.84]).all()
        assert (thickness == [5.0, 2.0]).all()

    def test_load_type_element(self):
        """test of load_type_element, no parameter checking"""

        # test load function
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].load_type_element(1988, "iwu_heavy", prj.data)
        therm_zone.inner_walls[0].load_type_element(1988, "iwu_light", prj.data)
        therm_zone.windows[0].load_type_element(
            1988, "Kunststofffenster, Isolierverglasung", prj.data
        )

    def test_save_type_element(self):
        """test of save_type_element, no parameter checking"""
        import os

        # test load function
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        path = os.path.join(utilities.get_default_path(), "unitTestTB.json")
        prj.data.path_tb = path
        prj.data.load_tb_binding()
        therm_zone.outer_walls[0].save_type_element(data_class=prj.data)
        therm_zone.inner_walls[0].save_type_element(data_class=prj.data)
        therm_zone.windows[0].save_type_element(data_class=prj.data)

    def test_delete_type_element(self):
        """test of save_type_element, no parameter checking"""
        import os

        # test load function
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        path = os.path.join(utilities.get_default_path(), "unitTestTB.json")
        prj.data.path_tb = path
        prj.data.load_tb_binding()
        therm_zone.outer_walls[0].delete_type_element(data_class=prj.data)
        therm_zone.inner_walls[0].delete_type_element(data_class=prj.data)
        therm_zone.windows[0].delete_type_element(data_class=prj.data)

    # methods in Wall

    def test_calc_equivalent_res_wall(self):
        """test of calc_equivalent_res, wall"""
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]

        therm_zone.outer_walls[0].calc_equivalent_res()

        # parameters for outwall

        assert round(therm_zone.outer_walls[0].c1, 6) == 111237.213205
        assert round(therm_zone.outer_walls[0].c2, 7) == 59455.3856787
        assert round(therm_zone.outer_walls[0].r1, 13) == 0.0330465078788
        assert round(therm_zone.outer_walls[0].r2, 13) == 0.0549256129353
        assert round(therm_zone.outer_walls[0].r3, 12) == 0.137027879186
        assert round(therm_zone.outer_walls[0].c1_korr, 6) == 111237.213205

    def test_insulate_wall(self):
        """test of insulate_wall"""
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].insulate_wall("EPS_040_15", 0.04)
        assert round(therm_zone.outer_walls[0].ua_value, 6) == 2.924088

    def test_retrofit_wall(self):
        """test of retrofit_wall"""
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(2016, "EPS_040_15")
        assert round(therm_zone.outer_walls[0].ua_value, 6) == 2.4
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(2010, "EPS_040_15")
        assert round(therm_zone.outer_walls[0].ua_value, 6) == 2.4
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(2005, "EPS_040_15")
        assert round(therm_zone.outer_walls[0].ua_value, 2) == 4.13
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(1998, "EPS_040_15")
        assert round(therm_zone.outer_walls[0].ua_value, 2) == 4.13
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(1990, "EPS_040_15")
        assert round(therm_zone.outer_walls[0].ua_value, 2) == 4.13
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(1980, "EPS_040_15")
        assert round(therm_zone.outer_walls[0].ua_value, 2) == 4.13
        prj.set_default(load_data=True)
        helptest.building_test2(prj)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=False)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=True)
        therm_zone_heated = prj.buildings[-1].thermal_zones[0]
        therm_zone_unheated = prj.buildings[-1].thermal_zones[1]
        second_heated_zone = prj.buildings[-1].thermal_zones[2]
        assert therm_zone_heated.use_conditions.with_heating is True
        assert therm_zone_unheated.use_conditions.with_heating is False
        assert second_heated_zone.use_conditions.with_heating is True
        therm_zone_other_heated = prj.buildings[-1].thermal_zones[2]
        for interzonal_element in therm_zone_heated.interzonal_walls:
            previous_ua_value = interzonal_element.ua_value
            interzonal_element.retrofit_wall(2015, "EPS_040_15")
            if interzonal_element.other_side is therm_zone_unheated:
                assert (round(interzonal_element.ua_value, 2)
                        == 0.24 * interzonal_element.area)
                assert (interzonal_element.layer[-1].material.name
                        == "EPS_040_15")
            if interzonal_element.other_side is second_heated_zone:
                assert (round(interzonal_element.ua_value, 2)
                        == round(previous_ua_value, 2))
        for interzonal_element in therm_zone_heated.interzonal_ceilings:
            previous_ua_value = interzonal_element.ua_value
            interzonal_element.retrofit_wall(2015, "EPS_040_15")
            if interzonal_element.other_side is therm_zone_unheated:
                assert (round(interzonal_element.ua_value, 2)
                        == 0.2 * interzonal_element.area)
                assert (interzonal_element.layer[-1].material.name
                        == "EPS_040_15")
            if interzonal_element.other_side is second_heated_zone:
                assert (round(interzonal_element.ua_value, 2)
                        == round(previous_ua_value, 2))
        for interzonal_element in therm_zone_heated.interzonal_floors:
            previous_ua_value = interzonal_element.ua_value
            interzonal_element.retrofit_wall(2015, "EPS_040_15")
            if interzonal_element.other_side is therm_zone_unheated:
                assert (round(interzonal_element.ua_value, 2)
                        == 0.3 * interzonal_element.area)
                assert (interzonal_element.layer[-1].material.name
                        == "EPS_040_15")
            if interzonal_element.other_side is second_heated_zone:
                assert (round(interzonal_element.ua_value, 2)
                        == round(previous_ua_value, 2))
        for interzonal_element in therm_zone_unheated.interzonal_walls:
            interzonal_element.retrofit_wall(2015, "EPS_040_15")
            assert (round(interzonal_element.ua_value, 2)
                    == 0.24 * interzonal_element.area)
            assert interzonal_element.layer[0].material.name == "EPS_040_15"
        for interzonal_element in therm_zone_unheated.interzonal_ceilings:
            interzonal_element.retrofit_wall(2015, "EPS_040_15")
            assert (round(interzonal_element.ua_value, 2)
                    == 0.2 * interzonal_element.area)
            assert interzonal_element.layer[0].material.name == "EPS_040_15"
        for interzonal_element in therm_zone_unheated.interzonal_floors:
            interzonal_element.retrofit_wall(2015, "EPS_040_15")
            assert (round(interzonal_element.ua_value, 2)
                    == 0.3 * interzonal_element.area)
            assert interzonal_element.layer[0].material.name == "EPS_040_15"

    def test_interzonal_type_element(self):
        prj.set_default(load_data=True)
        helptest.building_test2(prj)
        helptest.interzonal_test2(prj)

        heated_zone = prj.buildings[-1].thermal_zones[-2]
        unheated_zone = prj.buildings[-1].thermal_zones[-1]
        iz_ceiling = heated_zone.interzonal_ceilings[-1]
        iz_floor = unheated_zone.interzonal_floors[-1]

        assert iz_ceiling.layer[0].material.name == "lime_plaster"
        assert len(iz_ceiling.layer) == len(iz_floor.layer)
        for ceiling_layer, floor_layer in zip(iz_ceiling.layer,
                                              reversed(iz_floor.layer)):
            assert ceiling_layer.material.name == floor_layer.material.name
            assert ceiling_layer.thickness == floor_layer.thickness

        floor_properties = iz_floor.gather_element_properties()
        ceiling_properties = iz_ceiling.gather_element_properties()
        assert floor_properties[0] == ceiling_properties[0]
        for (floor_layer_density,
             floor_layer_thermal_conduc,
             floor_layer_heat_capac,
             floor_layer_thickness,
             ceiling_layer_density,
             ceiling_layer_thermal_conduc,
             ceiling_layer_heat_capac,
             ceiling_layer_thickness) in zip(
                *[list(property_list).__reversed__()
                  for property_list in floor_properties[1:]],
                *ceiling_properties[1:]
        ):
            assert floor_layer_density == ceiling_layer_density
            assert floor_layer_thermal_conduc == ceiling_layer_thermal_conduc
            assert floor_layer_heat_capac == floor_layer_heat_capac
            assert floor_layer_thickness == ceiling_layer_thickness

        iz_wall_1 = unheated_zone.interzonal_walls[-1]
        iz_wall_2 = heated_zone.interzonal_walls[-1]

        assert iz_wall_1.layer[0].material.name == "concrete_wz05"
        assert iz_wall_2.layer[0].material.name == "concrete_CEM_II_BS325R_wz05"

    def test_save_load_building_issue679(self):
        prj.buildings[-1].thermal_zones[-1].time_to_minimal_t_ground = 25324
        prj.t_soil_mode = 3
        prj.t_soil_file_path = "example_file_path"
        prj.buildings[-1].inner_wall_approximation_approach \
            = 'typical_minus_outer'
        prj.buildings[-1].thermal_zones[-1].number_of_floors = 25
        prj.buildings[-1].thermal_zones[-1].height_of_floors = 3.148
        prj.buildings[-1].thermal_zones[-1].t_ground = 283.5
        prj.buildings[-1].thermal_zones[-1].t_ground_amplitude = 10
        prj.save_project(file_name="unitTestInterzonal",
                         path=utilities.get_default_path())
        prj.set_default(load_data=True)
        prj.load_project(os.path.join(utilities.get_default_path(),
                                      "unitTestInterzonal.json"))

        assert prj.buildings[-1].thermal_zones[-1].time_to_minimal_t_ground == 25324
        assert prj.t_soil_mode == 3
        assert prj.t_soil_file_path == "example_file_path"
        assert prj.buildings[-1].inner_wall_approximation_approach \
               == 'typical_minus_outer'
        assert prj.buildings[-1].thermal_zones[-2].interzonal_walls[-1].other_side \
               is prj.buildings[-1].thermal_zones[-1]
        assert prj.buildings[-1].thermal_zones[-1].interzonal_floors[-1].other_side \
               is prj.buildings[-1].thermal_zones[-2]
        assert len(prj.buildings[-1].thermal_zones[-2].interzonal_elements) == 2
        assert len(prj.buildings[-1].thermal_zones[-1].interzonal_elements) == 2
        assert prj.buildings[-1].thermal_zones[-1].number_of_floors == 25
        assert prj.buildings[-1].thermal_zones[-1].height_of_floors == 3.148
        assert prj.buildings[-1].thermal_zones[-1].t_ground == 283.5
        assert prj.buildings[-1].thermal_zones[-1].t_ground_amplitude == 10

    def test_sum_building_elements_five(self):
        """test of FiveElement calculator"""
        prj.set_default()
        helptest.building_test2(prj)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=False)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=True)

        from teaser.logic.buildingobjects.calculation.five_element import FiveElement

        therm_zone = prj.buildings[0].thermal_zones[0]

        calc_attr = FiveElement(therm_zone, merge_windows=True, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
            + therm_zone.interzonal_elements
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        calc_attr._sum_outer_wall_elements()
        calc_attr._sum_ground_floor_elements()
        calc_attr._sum_rooftop_elements()
        calc_attr._sum_inner_wall_elements()
        calc_attr._sum_window_elements()
        calc_attr._sum_interzonal_elements()

        # interzonal elements (lumping wall and floor)
        assert len(calc_attr.nzbs_per_nz) == 1
        assert len(calc_attr.nzbs_per_nz[0]) == 2
        assert round(calc_attr.ua_value_nzb[0], 16) == 8.615411975711941
        assert len(calc_attr.ua_value_nzb) == 1
        assert round(calc_attr.area_nzb[0], 1) == 20.0
        assert len(calc_attr.area_nzb) == 1
        assert round(calc_attr.r_conv_inner_nzb[0], 19) == 0.022727272727272728
        assert len(calc_attr.r_conv_inner_nzb) == 1
        assert round(calc_attr.r_rad_inner_nzb[0], 4) == 0.01
        assert len(calc_attr.r_conv_inner_nzb) == 1
        assert round(calc_attr.r_comb_inner_nzb[0], 19) == 0.006944444444444444
        assert len(calc_attr.r_comb_inner_nzb) == 1
        assert round(calc_attr.r_conv_outer_nzb[0], 5) == 0.02273
        assert len(calc_attr.r_conv_outer_nzb) == 1
        assert round(calc_attr.r_rad_outer_nzb[0], 4) == 0.01
        assert len(calc_attr.r_rad_outer_nzb) == 1
        assert round(calc_attr.r_comb_outer_nzb[0], 4) == 0.0069
        assert len(calc_attr.r_comb_outer_nzb) == 1
        assert round(calc_attr.alpha_conv_inner_nzb[0], 1) == 2.2
        assert len(calc_attr.alpha_conv_inner_nzb) == 1
        assert round(calc_attr.alpha_comb_outer_nzb[0], 1) == 7.2
        assert len(calc_attr.alpha_comb_outer_nzb) == 1
        assert round(calc_attr.alpha_conv_outer_nzb[0], 1) == 2.2
        assert len(calc_attr.alpha_conv_outer_nzb) == 1
        assert round(calc_attr.ir_emissivity_outer_nzb[0], 3) == 0.9
        assert len(calc_attr.ir_emissivity_outer_nzb) == 1

        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings(raise_errors=True)

        therm_zone_1 = prj.buildings[0].thermal_zones[1]
        therm_zone_2 = prj.buildings[0].thermal_zones[2]

        calc_attr = therm_zone.model_attr
        calc_attr_1 = therm_zone_1.model_attr
        calc_attr_2 = therm_zone_2.model_attr

        # check that attributes of the elements match if they represent the
        # same physical element
        assert calc_attr.other_nz_indexes[0] == 1
        assert len(calc_attr.other_nz_indexes) == 1
        assert calc_attr_1.other_nz_indexes[0] == 0
        assert len(calc_attr_2.other_nz_indexes) == 0
        assert round(calc_attr.r_total_nzb[0], 5) == round(calc_attr_1.r_total_nzb[0], 5)
        assert len(calc_attr.r_total_nzb) == 1
        assert len(calc_attr_2.r_total_nzb) == 0
        assert round(calc_attr.r1_nzb[0], 5) == round(calc_attr_1.r_rest_nzb[0], 5)
        assert len(calc_attr.r1_nzb) == 1
        assert len(calc_attr_2.r1_nzb) == 0
        assert round(calc_attr.r_rest_nzb[0], 5) == round(calc_attr_1.r1_nzb[0], 5)
        assert len(calc_attr.r_rest_nzb) == 1
        assert len(calc_attr_2.r_rest_nzb) == 0

    def test_calc_chain_matrix_five(self):
        """test of calc_chain_matrix"""
        from teaser.logic.buildingobjects.calculation.five_element \
            import FiveElement

        prj.set_default()
        helptest.building_test2(prj)
        helptest.interzonal_test2(prj, connect_to_index=0, add_heated=False)

        therm_zone = prj.buildings[-1].thermal_zones[-2]

        calc_attr = FiveElement(therm_zone, merge_windows=False, t_bt=5)

        helplist = (
            therm_zone.outer_walls
            + therm_zone.rooftops
            + therm_zone.ground_floors
            + therm_zone.inner_walls
            + therm_zone.ceilings
            + therm_zone.floors
            + therm_zone.windows
            + therm_zone.interzonal_elements
        )

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        omega = 2 * math.pi / 86400 / 5

        helplist_outer_walls = therm_zone.outer_walls + therm_zone.windows

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls, omega=omega, mode='ow'
        )
        assert round(r1_ow, 14) == 0.00688468914141
        assert round(c1_ow, 5) == 533938.62338

        helplist_inner_walls = (
            therm_zone.inner_walls + therm_zone.ceilings + therm_zone.floors
        )

        r1_iw, c1_iw = calc_attr._calc_parallel_connection(
            element_list=helplist_inner_walls, omega=omega, mode='iw'
        )
        assert round(r1_iw, 13) == 0.0097195611408
        assert round(c1_iw, 6) == 319983.518743

        r1_izw, c1_izw = calc_attr._calc_parallel_connection(
            element_list=therm_zone.interzonal_elements, omega=omega, mode='ow'
        )
        assert round(r1_izw, 13) == 0.0023421240754
        assert round(c1_izw, 6) == 4782078.891281

        therm_zone_2 = prj.buildings[-1].thermal_zones[-1]

        calc_attr_2 = FiveElement(therm_zone_2, merge_windows=True, t_bt=5)

        for element in therm_zone_2.interzonal_elements:
            element.calc_equivalent_res()
            element.calc_ua_value()

        r1_izw_2, c1_izw_2 = calc_attr_2._calc_parallel_connection(
            element_list=therm_zone_2.interzonal_elements, omega=omega,
            mode='izw_backwards'
        )
        # CAUTION: these values need to be equal to the ones above
        # when applied in practice, FiveElement._calc_interzonal_elements will
        #  revertedly apply the values to the final model parameters
        assert round(r1_izw_2, 13) == 0.0023421240754
        assert round(c1_izw_2, 6) == 4782078.891281

    def test_calc_equivalent_res_win(self):
        """test of calc_equivalent_res, win"""
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.windows[0].calc_equivalent_res()

        assert round(therm_zone.windows[0].r1, 3) == 0.072

    def test_load_save_material(self):
        """test of load_material_template and save_material_template,
        no parameter checking"""

        from teaser.logic.buildingobjects.buildingphysics.material import Material

        path = os.path.join(utilities.get_default_path(), "MatUT.json")

        mat = Material(parent=None)
        mat.load_material_template(mat_name="Tiledroof", data_class=prj.data)

        from teaser.data.dataclass import DataClass

        dat = DataClass(construction_data=ConstructionData.iwu_heavy)
        dat.path_mat = path
        dat.load_mat_binding()

        mat.save_material_template(data_class=dat)

    def test_properties_project(self):
        """Tests properties of project class"""
        prj.number_of_elements_calc
        prj.merge_windows_calc
        prj.used_library_calc
        prj.name = 123
        assert prj.name == "P123"

    def test_warnings_prj(self):
        """Tests misc parts in project.py"""

        prj.data = DataClass(construction_data=ConstructionData.iwu_heavy)
        from teaser.logic.buildingobjects.building import Building
        from teaser.logic.buildingobjects.thermalzone import ThermalZone
        from teaser.logic.buildingobjects.useconditions import UseConditions

        # warnings for not calculated buildings
        bld = Building(parent=prj)
        tz = ThermalZone(parent=bld)
        tz.use_conditions = UseConditions(parent=tz)
        prj.calc_all_buildings()
        prj.set_default(load_data=False)
        # warning if iwu and number_of_apartments is used
        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="iwu_single_family_dwelling",
            name="test",
            year_of_construction=1988,
            number_of_floors=1,
            height_of_floors=7,
            net_leased_area=1988,
            number_of_apartments=1,
        )
        # not all buildings if internal id is passed over
        prj.add_residential(
            construction_data="iwu_heavy",
            geometry_data="iwu_single_family_dwelling",
            name="test1",
            year_of_construction=1988,
            number_of_floors=15,
            height_of_floors=6,
            net_leased_area=1988,
        )
        prj.calc_all_buildings()
        prj.export_aixlib(internal_id=prj.buildings[-1].internal_id)
        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa(internal_id=prj.buildings[-1].internal_id)

        prj.set_default(load_data="Test")
        prj.data = DataClass(construction_data=ConstructionData.iwu_heavy)

    def test_export_aixlib_only_iw(self):
        """
        Tests AixLib output for a building with inner walls only
        """

        from teaser.logic.buildingobjects.building import Building

        prj.set_default(load_data=False)

        bldg = Building(parent=prj)
        bldg.name = "SuperExampleBuilding"
        bldg.street_name = "AwesomeAvenue42"
        bldg.city = "46325FantasticTown"
        bldg.year_of_construction = 2015
        bldg.number_of_floors = 1
        bldg.height_of_floors = 3.5

        from teaser.logic.buildingobjects.thermalzone import ThermalZone

        tz = ThermalZone(parent=bldg)
        tz.name = "LivingRoom"
        tz.area = 140.0
        tz.volume = tz.area * bldg.number_of_floors * bldg.height_of_floors

        from teaser.logic.buildingobjects.useconditions import UseConditions

        tz.use_conditions = UseConditions(parent=tz)
        tz.use_conditions.load_use_conditions("Living", prj.data)

        from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall

        in_wall_dict = {
            "InnerWall1": [10.0],
            "InnerWall2": [14.0],
            "InnerWall3": [10.0],
        }

        for key, value in in_wall_dict.items():

            in_wall = InnerWall(parent=tz)
            in_wall.name = key
            in_wall.load_type_element(
                year=bldg.year_of_construction, construction="iwu_heavy"
            )
            in_wall.area = value[0]

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

    def test_export_only_ow(self):
        """
        Tests AixLib output for a building with outer walls only
        """

        from teaser.logic.buildingobjects.building import Building

        bldg = Building(parent=prj)
        bldg.name = "SuperExampleBuilding"
        bldg.street_name = "AwesomeAvenue42"
        bldg.city = "46325FantasticTown"
        bldg.year_of_construction = 2015
        bldg.number_of_floors = 1
        bldg.height_of_floors = 3.5

        from teaser.logic.buildingobjects.thermalzone import ThermalZone

        tz = ThermalZone(parent=bldg)
        tz.name = "LivingRoom"
        tz.area = 140.0
        tz.volume = tz.area * bldg.number_of_floors * bldg.height_of_floors

        from teaser.logic.buildingobjects.useconditions import UseConditions

        tz.use_conditions = UseConditions(parent=tz)
        tz.use_conditions.load_use_conditions("Living", prj.data)

        from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall

        out_wall_dict = {
            "OuterWall_north": [10.0, 90.0, 0.0],
            "OuterWall_east": [14.0, 90.0, 90.0],
            "OuterWall_south": [10.0, 90.0, 180.0],
            "OuterWall_west": [14.0, 90.0, 270.0],
        }

        for key, value in out_wall_dict.items():
            out_wall = OuterWall(parent=tz)
            out_wall.name = key

            out_wall.load_type_element(
                year=bldg.year_of_construction, construction="iwu_heavy"
            )

            out_wall.area = value[0]
            out_wall.tilt = value[1]
            out_wall.orientation = value[2]

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

    def test_export_only_win(self):
        """
        Tests AixLib output for a building with windows only
        """

        from teaser.logic.buildingobjects.building import Building

        bldg = Building(parent=prj)
        bldg.name = "SuperExampleBuilding"
        bldg.street_name = "AwesomeAvenue42"
        bldg.city = "46325FantasticTown"
        bldg.year_of_construction = 2015
        bldg.number_of_floors = 1
        bldg.height_of_floors = 3.5

        from teaser.logic.buildingobjects.thermalzone import ThermalZone

        tz = ThermalZone(parent=bldg)
        tz.name = "LivingRoom"
        tz.area = 140.0
        tz.volume = tz.area * bldg.number_of_floors * bldg.height_of_floors

        from teaser.logic.buildingobjects.useconditions import UseConditions

        tz.use_conditions = UseConditions(parent=tz)
        tz.use_conditions.load_use_conditions("Living", prj.data)

        from teaser.logic.buildingobjects.buildingphysics.window import Window
        from teaser.logic.buildingobjects.buildingphysics.layer import Layer
        from teaser.logic.buildingobjects.buildingphysics.material import Material

        win_dict = {
            "Window_east": [5.0, 90.0, 90.0],
            "Window_south": [8.0, 90.0, 180.0],
            "Window_west": [5.0, 90.0, 270.0],
        }

        for key, value in win_dict.items():

            win = Window(parent=tz)
            win.name = key
            win.area = value[0]
            win.tilt = value[1]
            win.orientation = value[2]

            win.inner_convection = 1.7
            win.inner_radiation = 5.0
            win.outer_convection = 20.0
            win.outer_radiation = 5.0
            win.g_value = 0.789
            win.a_conv = 0.03
            win.shading_g_total = 0.0
            win.shading_max_irr = 180.0

            win_layer = Layer(parent=win)
            win_layer.id = 1
            win_layer.thickness = 0.024

            win_material = Material(win_layer)
            win_material.name = "GlasWindow"
            win_material.thermal_conduc = 0.067
            win_material.transmittance = 0.9

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = True
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

    def test_export_only_rt(self):
        """
        Tests AixLib output for a building with rooftops only
        """

        from teaser.logic.buildingobjects.building import Building

        bldg = Building(parent=prj)
        bldg.name = "SuperExampleBuilding"
        bldg.street_name = "AwesomeAvenue42"
        bldg.city = "46325FantasticTown"
        bldg.year_of_construction = 2015
        bldg.number_of_floors = 1
        bldg.height_of_floors = 3.5

        from teaser.logic.buildingobjects.thermalzone import ThermalZone

        tz = ThermalZone(parent=bldg)
        tz.name = "LivingRoom"
        tz.area = 140.0
        tz.volume = tz.area * bldg.number_of_floors * bldg.height_of_floors

        from teaser.logic.buildingobjects.useconditions import UseConditions

        tz.use_conditions = UseConditions(parent=tz)
        tz.use_conditions.load_use_conditions("Living", prj.data)

        from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop

        roof_south = Rooftop(parent=tz)
        roof_south.name = "Roof_South"
        roof_south.area = 75.0
        roof_south.orientation = 180.0
        roof_south.tilt = 55.0
        roof_south.inner_convection = 1.7
        roof_south.outer_convection = 20.0
        roof_south.inner_radiation = 5.0
        roof_south.outer_radiation = 5.0

        roof_north = Rooftop(parent=tz)
        roof_north.name = "Roof_North"
        roof_north.area = 75.0
        roof_north.orientation = 0.0
        roof_north.tilt = 55.0
        roof_north.inner_convection = 1.7
        roof_north.outer_convection = 20.0
        roof_north.inner_radiation = 5.0
        roof_north.outer_radiation = 5.0

        from teaser.logic.buildingobjects.buildingphysics.layer import Layer

        layer_s1 = Layer(parent=roof_south, id=0)
        layer_s1.thickness = 0.3

        from teaser.logic.buildingobjects.buildingphysics.material import Material

        material_s1 = Material(layer_s1)
        material_s1.name = "Insulation"
        material_s1.density = 120.0
        material_s1.heat_capac = 0.04
        material_s1.thermal_conduc = 1.0

        layer_s2 = Layer(parent=roof_south, id=1)
        layer_s2.thickness = 0.15

        material_s2 = Material(layer_s2)
        material_s2.name = "Tile"
        material_s2.density = 1400.0
        material_s2.heat_capac = 0.6
        material_s2.thermal_conduc = 2.5

        layer_n1 = Layer(parent=roof_north, id=0)
        layer_n1.thickness = 0.3

        material_n1 = Material(layer_n1)
        material_n1.name = "Insulation"
        material_n1.density = 120.0
        material_n1.heat_capac = 0.04
        material_n1.thermal_conduc = 1.0

        layer_n2 = Layer(parent=roof_north, id=1)
        layer_n2.thickness = 0.15

        material_n2 = Material(layer_n2)
        material_n2.name = "Tile"
        material_n2.density = 1400.0
        material_n2.heat_capac = 0.6
        material_n2.thermal_conduc = 2.5

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

    def test_export_only_gf(self):
        """
        Tests AixLib output for a building with ground floors only
        """

        from teaser.logic.buildingobjects.building import Building

        bldg = Building(parent=prj)
        bldg.name = "SuperExampleBuilding"
        bldg.street_name = "AwesomeAvenue42"
        bldg.city = "46325FantasticTown"
        bldg.year_of_construction = 2015
        bldg.number_of_floors = 1
        bldg.height_of_floors = 3.5

        from teaser.logic.buildingobjects.thermalzone import ThermalZone

        tz = ThermalZone(parent=bldg)
        tz.name = "LivingRoom"
        tz.area = 140.0
        tz.volume = tz.area * bldg.number_of_floors * bldg.height_of_floors

        from teaser.logic.buildingobjects.useconditions import UseConditions

        tz.use_conditions = UseConditions(parent=tz)
        tz.use_conditions.load_use_conditions("Living", prj.data)

        from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor

        ground_floor_dict = {"GroundFloor": [100.0, 0.0, -2]}

        for key, value in ground_floor_dict.items():

            ground = GroundFloor(parent=tz)
            ground.name = key
            ground.load_type_element(
                year=bldg.year_of_construction, construction="iwu_heavy"
            )
            ground.area = value[0]
            ground.tilt = value[1]
            ground.orientation = value[2]

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 5
        prj.merge_windows_calc = False
        prj.used_library_calc = "AixLib"
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = "IBPSA"
        prj.calc_all_buildings()
        prj.export_ibpsa()

    def test_ashrae_140_600(self):

        from teaser.examples.verification.verification_ASHRAE_140_600 import (
            main as exmain,
        )

        exmain(number_of_elements=1)
        exmain(number_of_elements=2)
        exmain(number_of_elements=3)
        exmain(number_of_elements=4)

    def test_ashrae_140_620(self):

        from teaser.examples.verification.verification_ASHRAE_140_620 import (
            main as exmain,
        )

        exmain(number_of_elements=1)
        exmain(number_of_elements=2)
        exmain(number_of_elements=3)
        exmain(number_of_elements=4)

    def test_ashrae_140_900(self):

        from teaser.examples.verification.verification_ASHRAE_140_900 import (
            main as exmain,
        )

        exmain(number_of_elements=1)
        exmain(number_of_elements=2)
        exmain(number_of_elements=3)
        exmain(number_of_elements=4)

    def test_ashrae_140_920(self):

        from teaser.examples.verification.verification_ASHRAE_140_920 import (
            main as exmain,
        )

        exmain(number_of_elements=1)
        exmain(number_of_elements=2)
        exmain(number_of_elements=3)
        exmain(number_of_elements=4)

    # def test_type_bldg_residential_profiles(self):
    #     """
    #     Verification of the type building generation of an office building.
    #     Values are compared with TEASER3 values.
    #     """
    #     from teaser.logic.archetypebuildings.bmvbs.singlefamilydwelling \
    #         import SingleFamilyDwelling
    #
    #     prj.set_default()
    #     test_residential = SingleFamilyDwelling(parent=prj,
    #                                             name="TestBuilding",
    #                                             year_of_construction=1988,
    #                                             number_of_floors=3,
    #                                             height_of_floors=3,
    #                                             net_leased_area=2500)
    #
    #     test_residential.generate_archetype()
    #
    #     prj.calc_all_buildings()
    #
    #     path_to_export = prj.export_aixlib(
    #         internal_id=None,
    #         path=None)
    #
    #     from scipy.io import loadmat
    #     file = loadmat(os.path.join(
    #         path_to_export,
    #         "TestBuilding",
    #         "InternalGains_TestBuilding.mat"))
    #
    #     use_cond = test_residential.thermal_zones[0].use_conditions
    #
    #     assert (file['Internals'].transpose()[1][1:] ==
    #             use_cond.profile_persons).all()
    #
    #     assert (file['Internals'].transpose()[2][1:] ==
    #             use_cond.profile_machines).all()
    #
    #     assert (file['Internals'].transpose()[3][1:] ==
    #             use_cond.profile_lighting).all()

    def test_ahu_profiles(self):
        """Test setting AHU profiles of different lengths

        Related to issue 553 at https://github.com/RWTH-EBC/TEASER/issues/553
        """

        prj_test = Project()
        prj_test.name = "TestAHUProfiles"

        prj_test.add_non_residential(
            construction_data="iwu_heavy",
            geometry_data="bmvbs_office",
            name="OfficeBuilding",
            year_of_construction=2015,
            number_of_floors=4,
            height_of_floors=3.5,
            net_leased_area=1000.0,
        )

        prj_test.used_library_calc = "AixLib"
        prj_test.number_of_elements_calc = 2

        v_flow_workday = [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]

        v_flow_week = []
        for day in range(7):
            for val in v_flow_workday:
                if day < 5:
                    ratio = val
                else:
                    if val == 1:
                        ratio = 0.2
                    else:
                        ratio = 0.0
                v_flow_week.append(ratio)

        prj_test.buildings[-1].central_ahu.profile_v_flow = v_flow_week

        assert prj_test.buildings[-1].central_ahu.profile_v_flow == v_flow_week

    def test_export_bldg_threshold(self):

        prj.set_default(load_data=False)

        prj.add_non_residential(
            construction_data="iwu_heavy",
            geometry_data="bmvbs_institute",
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=True,
            office_layout=0,
            window_layout=0,
        )
        prj.buildings[-1].thermal_zones[0].use_conditions.with_ahu = True
        prj.buildings[-1].thermal_zones[0].use_conditions.with_ideal_thresholds = True
        prj.buildings[-1].thermal_zones[1].use_conditions.with_ahu = False
        prj.buildings[-1].thermal_zones[1].use_conditions.with_ideal_thresholds = False
        prj.buildings[-1].thermal_zones[-1].use_conditions.with_ahu = True
        prj.buildings[-1].thermal_zones[-1].use_conditions.with_ideal_thresholds = True
        prj.calc_all_buildings()
        prj.export_aixlib()

    def test_tz_naming(self):

        from teaser.logic.buildingobjects.building import Building
        from teaser.logic.buildingobjects.thermalzone import ThermalZone

        # warnings for not calculated buildings
        bld = Building(parent=prj)
        tz1 = ThermalZone(parent=bld)
        tz1.name = "living"

        tz2 = ThermalZone(parent=bld)
        tz2.name = "kitchen"

        tz3 = ThermalZone(parent=bld)
        tz3.name = "living"

        assert tz1.name == "living"
        assert tz2.name == "kitchen"
        assert tz3.name == "living_1"
