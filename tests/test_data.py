'''
Created July 2015

@author: TEASER 4 Development Team
'''

import math

import helptest

from teaser.logic import utilities
from teaser.project import Project
import teaser.examples.verification.vdi6007_testcases.vdi6007_case01 as vdi1
import teaser.examples.verification.vdi6007_testcases.vdi6007_case02 as vdi2
import teaser.examples.verification.vdi6007_testcases.vdi6007_case03 as vdi3
import teaser.examples.verification.vdi6007_testcases.vdi6007_case04 as vdi4
import teaser.examples.verification.vdi6007_testcases.vdi6007_case05 as vdi5
import teaser.examples.verification.vdi6007_testcases.vdi6007_case06 as vdi6
import teaser.examples.verification.vdi6007_testcases.vdi6007_case07 as vdi7
import teaser.examples.verification.vdi6007_testcases.vdi6007_case08 as vdi8
import teaser.examples.verification.vdi6007_testcases.vdi6007_case09 as vdi9
import teaser.examples.verification.vdi6007_testcases.vdi6007_case10 as vdi10
import teaser.examples.verification.vdi6007_testcases.vdi6007_case11 as vdi11
import teaser.examples.verification.vdi6007_testcases.vdi6007_case12 as vdi12

prj = Project(True)

import os
import numpy as np
from teaser.project import Project
import teaser.logic.simulation.VDI_6007.weather as weat
import teaser.logic.simulation.VDI_6007.low_order_VDI as low_order_VDI
import teaser.logic.simulation.VDI_6007.equal_air_temperature as equ_air


class Test_teaser(object):
    """Unit Tests for TEASER"""
    global prj

    def test_calc_vdi_room1(self):
        '''Parameter Verification for rouvel room1'''
        import teaser.examples.verification.verification_room1 as room1

        room1_prj = room1.parameter_room1()
        zone_attr = room1_prj.buildings[0].thermal_zones[0].model_attr

        # parameters inner wall Typraum S

        assert round(zone_attr.r1_iw, 13) == 0.0005956934075
        assert round(zone_attr.c1_iw / 1000, 7) == 14836.3546282
        assert round(zone_attr.area_iw, 1) == 75.5
        assert round(zone_attr.alpha_conv_inner_iw, 13) == 2.23642384105960

        # paremeters outer wall Typraum S
        r_rest = zone_attr.r_rest_ow + 1 / (zone_attr.alpha_comb_outer_ow *
                                            zone_attr.area_ow)
        assert round(r_rest, 13) == 0.0427687193786
        assert round(zone_attr.r1_ow, 13) == 0.0043679129367
        assert round(zone_attr.c1_ow / 1000, 7) == 1600.8489399
        assert round(zone_attr.area_ow, 1) == 3.5
        assert round(zone_attr.area_win, 1) == 7.0
        assert round(zone_attr.alpha_conv_inner_ow, 1) == 2.7
        assert round(zone_attr.alpha_comb_outer_ow, 1) == 25.0

    def test_calc_vdi_room3(self):
        '''Parameter Verification for room 3'''
        import teaser.examples.verification.verification_room3 as room3

        room3_prj = room3.parameter_room3()
        zone_attr = room3_prj.buildings[0].thermal_zones[0].model_attr

        # parameters inner wall Typraum L

        assert round(zone_attr.r1_iw, 13) == 0.003385649748
        assert round(zone_attr.c1_iw / 1000, 7) == 7445.3648976
        assert round(zone_attr.area_iw, 1) == 75.5
        assert round(zone_attr.alpha_conv_inner_iw, 13) == 2.23642384105960

        # parameters outer wall Typraum L
        r_rest = zone_attr.r_rest_ow + 1 / (zone_attr.alpha_comb_outer_ow *
                                            zone_attr.area_ow)
        assert round(r_rest, 13) == 0.0431403889233
        assert round(zone_attr.r1_ow, 13) == 0.004049351608
        assert round(zone_attr.c1_ow / 1000, 7) == 47.8617641
        assert round(zone_attr.area_ow, 1) == 3.5
        assert round(zone_attr.area_win, 1) == 7.0
        assert round(zone_attr.alpha_conv_inner_ow, 1) == 2.7
        assert round(zone_attr.alpha_comb_outer_ow, 1) == 25.0

    def test_calc_vdi_room8(self):
        '''Parameter Verification for room 8'''
        import teaser.examples.verification.verification_room8 as room8

        room8_prj = room8.parameter_room8()
        zone_attr = room8_prj.buildings[0].thermal_zones[0].model_attr

        assert round(zone_attr.r1_iw, 13) == 0.0006688956391
        assert round(zone_attr.c1_iw / 1000, 7) == 12391.3638631
        assert round(zone_attr.area_iw, 1) == 60.5
        assert round(zone_attr.alpha_conv_inner_iw, 13) == 2.1214876033058
        r_rest = zone_attr.r_rest_ow + 1 / (zone_attr.alpha_comb_outer_ow *
                                            zone_attr.area_ow)
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
        '''
        Parameter Verification for ebc calculation method. Values are compared
        with TEASER3 values.
        '''
        prj.set_default()
        prj.load_project(utilities.get_full_path("examples/examplefiles"
                                                 "/new.teaserXML"))

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
        '''
        Verification of the type building generation of an office building.
        Values are compared with TEASER3 values.
        '''
        from teaser.logic.archetypebuildings.bmvbs.office import Office

        prj.set_default()
        test_office = Office(parent=prj,
                             name="TestBuilding",
                             year_of_construction=1988,
                             number_of_floors=3,
                             height_of_floors=3,
                             net_leased_area=2500)

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
        test_office = Office(parent=prj,
                             name="TestBuilding",
                             year_of_construction=1988,
                             number_of_floors=3,
                             height_of_floors=3,
                             net_leased_area=2500,
                             office_layout=1,
                             window_layout=1,
                             construction_type="light")

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
        test_office = Office(parent=prj,
                             name="TestBuilding",
                             year_of_construction=1988,
                             number_of_floors=3,
                             height_of_floors=3,
                             net_leased_area=2500,
                             office_layout=2,
                             window_layout=2,
                             construction_type="heavy")

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
        test_office = Office(parent=prj,
                             name="TestBuilding",
                             year_of_construction=1988,
                             number_of_floors=3,
                             height_of_floors=3,
                             net_leased_area=2500,
                             office_layout=3,
                             window_layout=3,
                             construction_type="light")

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
        '''
        Verification of the type building generation of an office building.
        Values are compared with TEASER3 values.
        '''
        from teaser.logic.archetypebuildings.bmvbs.custom.institute4 import \
            Institute4

        prj.set_default()
        test_institute4 = Institute4(parent=prj,
                                     name="TestBuilding",
                                     year_of_construction=1988,
                                     number_of_floors=3,
                                     height_of_floors=3,
                                     net_leased_area=2500,
                                     office_layout=0,
                                     window_layout=0,
                                     construction_type="heavy")

        test_institute4.generate_archetype()

        # general parameters

        assert len(test_institute4.thermal_zones) == 7

        # zone specific parameters

        for zone in test_institute4.thermal_zones:
            if zone.name == "Meeting":
                assert zone.area == 100
            if zone.name == "Storage":
                assert zone.area == 250
            if zone.name == "Office":
                assert zone.area == 937.5
            if zone.name == "Restroom":
                assert zone.area == 100
            if zone.name == "ICT":
                assert zone.area == 50
            if zone.name == "Floor":
                assert zone.area == 562.5
            if zone.name == "Laboratory":
                assert zone.area == 500

        # facade specific parameters

        assert round(test_institute4.get_outer_wall_area(-2), 0) == 958
        assert round(test_institute4.get_outer_wall_area(-1), 0) == 958
        assert round(test_institute4.get_outer_wall_area(0), 0) == 437
        assert round(test_institute4.get_outer_wall_area(180), 0) == 437
        assert round(test_institute4.get_outer_wall_area(90), 0) == 77
        assert round(test_institute4.get_outer_wall_area(270), 0) == 77
        assert round(test_institute4.get_window_area(0), 0) == 158
        assert round(test_institute4.get_window_area(180), 0) == 158
        assert round(test_institute4.get_window_area(90), 0) == 28
        assert round(test_institute4.get_window_area(270), 0) == 28

    def test_type_bldg_institute8_with_calc(self):
        '''
        Verification of the type building generation of an office building.
        Values are compared with TEASER3 values.
        '''
        from teaser.logic.archetypebuildings.bmvbs.custom.institute8 import \
            Institute8

        prj.set_default()
        test_institute8 = Institute8(parent=prj,
                                     name="TestBuilding",
                                     year_of_construction=1988,
                                     number_of_floors=3,
                                     height_of_floors=3,
                                     net_leased_area=2500,
                                     office_layout=0,
                                     window_layout=0,
                                     construction_type="heavy")

        test_institute8.generate_archetype()

        # general parameters

        assert len(test_institute8.thermal_zones) == 7

        # zone specific parameters

        for zone in test_institute8.thermal_zones:
            if zone.name == "Meeting":
                assert zone.area == 100
            if zone.name == "Storage":
                assert zone.area == 50
            if zone.name == "Office":
                assert zone.area == 250
            if zone.name == "Restroom":
                assert zone.area == 100
            if zone.name == "ICT":
                assert zone.area == 50
            if zone.name == "Floor":
                assert zone.area == 450
            if zone.name == "Laboratory":
                assert zone.area == 1500

        # facade specific parameters

        assert round(test_institute8.get_outer_wall_area(-2), 0) == 958
        assert round(test_institute8.get_outer_wall_area(-1), 0) == 958
        assert round(test_institute8.get_outer_wall_area(0), 0) == 437
        assert round(test_institute8.get_outer_wall_area(180), 0) == 437
        assert round(test_institute8.get_outer_wall_area(90), 0) == 77
        assert round(test_institute8.get_outer_wall_area(270), 0) == 77
        assert round(test_institute8.get_window_area(0), 0) == 158
        assert round(test_institute8.get_window_area(180), 0) == 158
        assert round(test_institute8.get_window_area(90), 0) == 28
        assert round(test_institute8.get_window_area(270), 0) == 28

    def test_type_bldg_institute_with_calc(self):
        '''
        Verification of the type building generation of an office building.
        Values are compared with TEASER3 values.
        '''
        from teaser.logic.archetypebuildings.bmvbs.custom.institute import \
            Institute

        prj.set_default()
        test_institute = Institute(parent=prj,
                                   name="TestBuilding",
                                   year_of_construction=1988,
                                   number_of_floors=3,
                                   height_of_floors=3,
                                   net_leased_area=2500,
                                   office_layout=0,
                                   window_layout=0,
                                   construction_type="heavy")

        test_institute.generate_archetype()

        # general parameters

        assert len(test_institute.thermal_zones) == 7

        # zone specific parameters

        for zone in test_institute.thermal_zones:
            if zone.name == "Meeting":
                assert zone.area == 100
            if zone.name == "Storage":
                assert zone.area == 250
            if zone.name == "Office":
                assert zone.area == 1000
            if zone.name == "Restroom":
                assert zone.area == 100
            if zone.name == "ICT":
                assert zone.area == 50
            if zone.name == "Floor":
                assert zone.area == 625
            if zone.name == "Laboratory":
                assert zone.area == 375

        # facade specific parameters

        assert round(test_institute.get_outer_wall_area(-2), 0) == 958
        assert round(test_institute.get_outer_wall_area(-1), 0) == 958
        assert round(test_institute.get_outer_wall_area(0), 0) == 437
        assert round(test_institute.get_outer_wall_area(180), 0) == 437
        assert round(test_institute.get_outer_wall_area(90), 0) == 77
        assert round(test_institute.get_outer_wall_area(270), 0) == 77
        assert round(test_institute.get_window_area(0), 0) == 158
        assert round(test_institute.get_window_area(180), 0) == 158
        assert round(test_institute.get_window_area(90), 0) == 28
        assert round(test_institute.get_window_area(270), 0) == 28

    def test_type_bldg_residential_with_calc(self):
        '''
        Verification of the type building generation of an office building.
        Values are compared with TEASER3 values.
        '''
        from teaser.logic.archetypebuildings.bmvbs.singlefamilydwelling \
            import SingleFamilyDwelling

        prj.set_default()
        test_residential = SingleFamilyDwelling(parent=prj,
                                                name="TestBuilding",
                                                year_of_construction=1988,
                                                number_of_floors=3,
                                                height_of_floors=3,
                                                net_leased_area=2500)

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
        assert round(test_residential.get_outer_wall_area(0), 0) == 325
        assert round(test_residential.get_outer_wall_area(180), 0) == 325
        assert round(test_residential.get_outer_wall_area(90), 0) == 325
        assert round(test_residential.get_outer_wall_area(270), 0) == 325
        assert round(test_residential.get_window_area(0), 0) == 125
        assert round(test_residential.get_window_area(180), 0) == 125
        assert round(test_residential.get_window_area(90), 0) == 125
        assert round(test_residential.get_window_area(270), 0) == 125

        prj.set_default()
        test_residential = SingleFamilyDwelling(parent=prj,
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
                                                construction_type="light")

        test_residential.generate_archetype()

        # facade specific parameters

        assert round(test_residential.get_outer_wall_area(-2), 0) == 1108
        assert round(test_residential.get_outer_wall_area(-1), 0) == 1108
        assert round(test_residential.get_outer_wall_area(0), 0) == 398
        assert round(test_residential.get_outer_wall_area(180), 0) == 398
        assert round(test_residential.get_outer_wall_area(90), 0) == 398
        assert round(test_residential.get_outer_wall_area(270), 0) == 398
        assert round(test_residential.get_window_area(0), 0) == 125
        assert round(test_residential.get_window_area(180), 0) == 125
        assert round(test_residential.get_window_area(90), 0) == 125
        assert round(test_residential.get_window_area(270), 0) == 125

        prj.set_default()
        test_residential = SingleFamilyDwelling(parent=prj,
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
                                                construction_type="heavy")

        test_residential.generate_archetype()

        # facade specific parameters

        assert round(test_residential.get_outer_wall_area(-2), 0) == 858
        assert round(test_residential.get_outer_wall_area(-1), 0) == 484
        assert round(test_residential.get_outer_wall_area(0), 0) == 270
        assert round(test_residential.get_outer_wall_area(180), 0) == 270
        assert round(test_residential.get_outer_wall_area(90), 0) == 270
        assert round(test_residential.get_outer_wall_area(270), 0) == 270
        assert round(test_residential.get_window_area(0), 0) == 125
        assert round(test_residential.get_window_area(180), 0) == 125
        assert round(test_residential.get_window_area(90), 0) == 125
        assert round(test_residential.get_window_area(270), 0) == 125

        prj.set_default()
        test_residential = SingleFamilyDwelling(parent=prj,
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
                                                construction_type="light")

        test_residential.generate_archetype()

        # facade specific parameters

        assert round(test_residential.get_outer_wall_area(-2), 0) == 700
        assert round(test_residential.get_outer_wall_area(-1), 0) == 789
        assert round(test_residential.get_outer_wall_area(0), 0) == 255
        assert round(test_residential.get_outer_wall_area(180), 0) == 255
        assert round(test_residential.get_outer_wall_area(90), 0) == 255
        assert round(test_residential.get_outer_wall_area(270), 0) == 255
        assert round(test_residential.get_window_area(0), 0) == 125
        assert round(test_residential.get_window_area(180), 0) == 125
        assert round(test_residential.get_window_area(90), 0) == 125
        assert round(test_residential.get_window_area(270), 0) == 125

    # methods in Project, these tests only test if the API function works,
    # not if it produces reliable results.

    def test_load_save_project(self):
        '''test of load_project and save_project'''

        prj.load_project(utilities.get_full_path(("examples/examplefiles"
                                                  "/new.teaserXML")))
        therm_zone = prj.buildings[-1].thermal_zones[0]
        assert therm_zone.outer_walls[0].area == 40.0
        tz_area = sum([tz.area for tz in prj.buildings[
            -1].thermal_zones])
        assert prj.buildings[-1].net_leased_area == tz_area
        prj.save_project("unitTest")
        prj.set_default()

    # commented until we find solution for opengis PyXB bindings
    def test_save_citygml(self):
        '''test of save_gml'''
        helptest.building_test2(prj)
        prj.save_citygml("unitTest")
        prj.set_default()

    def test_calc_all_buildings(self):
        '''test of calc_all_buildings, no calculation verification'''

        helptest.building_test2(prj)
        helptest.building_test2(prj)
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = True
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()

    def test_retrofit_all_buildings(self):
        '''test of retrofit_all_buildings, no calculation verification'''

        prj.retrofit_all_buildings(2015)

    def test_export_aixlib(self):
        '''test of export_aixlib, no calculation verification'''

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_aixlib()

        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_aixlib()

    def test_export_annex(self):
        '''test of export_annex, no calculation verification'''

        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = True
        prj.used_library_calc = 'Annex60'
        prj.calc_all_buildings()
        prj.export_annex()
        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = 'Annex60'
        prj.calc_all_buildings()
        prj.export_annex()
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = True
        prj.used_library_calc = 'Annex60'
        prj.calc_all_buildings()
        prj.export_annex()
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = 'Annex60'
        prj.calc_all_buildings()
        prj.export_annex()
        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = True
        prj.used_library_calc = 'Annex60'
        prj.calc_all_buildings()
        prj.export_annex()
        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = 'Annex60'
        prj.calc_all_buildings()
        prj.export_annex()
        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = True
        prj.used_library_calc = 'Annex60'
        prj.calc_all_buildings()
        prj.export_annex()
        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = 'Annex60'
        prj.calc_all_buildings()
        prj.export_annex()
        prj.set_default()

    def test_export_parameters_txt(self):
        '''test of the export of the readable parameter output'''
        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = True
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_parameters_txt()
        prj.number_of_elements_calc = 1
        prj.merge_windows_calc = False
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_parameters_txt()
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = True
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_parameters_txt()
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_parameters_txt()
        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = True
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_parameters_txt()
        prj.number_of_elements_calc = 3
        prj.merge_windows_calc = False
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_parameters_txt()
        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = True
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_parameters_txt()
        prj.number_of_elements_calc = 4
        prj.merge_windows_calc = False
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_parameters_txt()
        prj.set_default()

    def test_instantiate_data_class(self):
        '''test of instantiate_data_class'''

        prj.instantiate_data_class()

    def test_type_bldg_office(self):
        '''test of type_bldg_office, no calculation verification
        '''

        prj.type_bldg_office(name="TestBuilding",
                             year_of_construction=1988,
                             number_of_floors=7,
                             height_of_floors=1,
                             net_leased_area=1988,
                             office_layout=0,
                             window_layout=0,
                             construction_type="heavy")

        prj.add_non_residential(
            method='bmvbs',
            usage='office',
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=False,
            office_layout=0,
            window_layout=0,
            construction_type="heavy")

    def test_type_bldg_institute(self):
        '''test of type_bldg_institute, no calculation verification'''

        prj.type_bldg_institute(name="TestBuilding",
                                year_of_construction=1988,
                                number_of_floors=7,
                                height_of_floors=1,
                                net_leased_area=1988,
                                office_layout=0,
                                window_layout=0,
                                construction_type="heavy")

        prj.add_non_residential(
            method='bmvbs',
            usage='institute',
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=True,
            office_layout=0,
            window_layout=0,
            construction_type="heavy")

    def test_type_bldg_institute4(self):
        '''test of type_bldg_institute4, no calculation verification'''

        prj.type_bldg_institute4(name="TestBuilding",
                                 year_of_construction=1988,
                                 number_of_floors=7,
                                 height_of_floors=1,
                                 net_leased_area=1988,
                                 office_layout=0,
                                 window_layout=0,
                                 construction_type="heavy")

        prj.add_non_residential(
            method='bmvbs',
            usage='institute4',
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=True,
            office_layout=0,
            window_layout=0,
            construction_type="heavy")

    def test_type_bldg_institute8(self):
        '''test of type_bldg_institute8, no calculation verification'''

        prj.type_bldg_institute8(name="TestBuilding",
                                 year_of_construction=1988,
                                 number_of_floors=7,
                                 height_of_floors=1,
                                 net_leased_area=1988,
                                 office_layout=0,
                                 window_layout=0,
                                 construction_type="heavy")

        prj.add_non_residential(
            method='bmvbs',
            usage='institute8',
            name="TestBuilding",
            year_of_construction=1988,
            number_of_floors=7,
            height_of_floors=1,
            net_leased_area=1988,
            with_ahu=True,
            office_layout=0,
            window_layout=0,
            construction_type="heavy")

    def test_type_bldg_residential(self):
        '''test of type_bldg_residential, no calculation verification'''

        prj.type_bldg_residential(name="TestBuilding",
                                  year_of_construction=1988,
                                  number_of_floors=7,
                                  height_of_floors=1,
                                  net_leased_area=1988,
                                  residential_layout=0,
                                  neighbour_buildings=0,
                                  attic=0,
                                  cellar=0,
                                  dormer=0,
                                  construction_type="heavy")

        prj.add_residential(
            method='iwu',
            usage='single_family_dwelling',
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
            construction_type="heavy")

    def test_est_bldgs(self):
        '''test of type_bldg_residential, no calculation verification'''

        prj.add_residential(
            method='urbanrenet',
            usage='est1a',
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
            construction_type="heavy",
            number_of_apartments=1)

        prj.add_residential(
            method='urbanrenet',
            usage='est1b',
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
            construction_type="heavy",
            number_of_apartments=1)

        prj.add_residential(
            method='urbanrenet',
            usage='est2',
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
            construction_type="heavy",
            number_of_apartments=1)

        prj.add_residential(
            method='urbanrenet',
            usage='est3',
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
            construction_type="heavy",
            number_of_apartments=1)

        prj.add_residential(
            method='urbanrenet',
            usage='est4a',
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
            construction_type="heavy",
            number_of_apartments=1)

        prj.add_residential(
            method='urbanrenet',
            usage='est4b',
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
            construction_type="heavy",
            number_of_apartments=1)

        prj.add_residential(
            method='urbanrenet',
            usage='est5',
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
            construction_type="heavy",
            number_of_apartments=1)

        prj.add_residential(
            method='urbanrenet',
            usage='est6',
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
            construction_type="heavy",
            number_of_apartments=1)

        prj.add_residential(
            method='urbanrenet',
            usage='est7',
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
            construction_type="heavy",
            number_of_apartments=1)

        prj.add_residential(
            method='urbanrenet',
            usage='est8a',
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
            construction_type="heavy",
            number_of_apartments=1)

        prj.add_residential(
            method='urbanrenet',
            usage='est8b',
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
            construction_type="heavy",
            number_of_apartments=1)

    # methods in Building

    def test_get_inner_wall_area(self):
        '''test of get_inner_wall_area'''
        prj.set_default()
        helptest.building_test2(prj)
        sum_area = prj.buildings[-1].get_inner_wall_area()
        assert round(sum_area, 1) == 34.0

    def test_set_outer_wall_area(self):
        '''test of set_outer_wall_area'''
        print(prj.buildings[-1].thermal_zones[-1].outer_walls[1].area)
        prj.buildings[-1].set_outer_wall_area(2.0, 0.0)

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        print(therm_zone.outer_walls[1].area)
        assert round(therm_zone.outer_walls[0].area, 3) == 2.0
        assert round(therm_zone.outer_walls[1].area, 3) == 14.0

    def test_get_outer_wall_area(self):
        '''test of get_outer_wall_area'''
        prj.buildings[-1].get_outer_wall_area(0.0)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        assert round(therm_zone.outer_walls[0].area, 3) == 2.0
        assert round(therm_zone.outer_walls[1].area, 3) == 14.0

    def test_set_window_area(self):
        '''test of set_window_area'''
        prj.buildings[-1].set_window_area(1.0, 90.0)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        assert round(therm_zone.windows[0].area, 3) == 1.0

    def test_get_window_area(self):
        '''test of get_window_area'''
        prj.buildings[-1].get_window_area(90.0)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        assert round(therm_zone.windows[0].area, 3) == 1.0

    def test_fill_outer_wall_area_dict(self):
        '''test of fill_outer_wall_area_dict'''

        prj.buildings[-1].fill_outer_area_dict()
        outwall_dict_round = {key: round(value, 2) for key, value in
                              prj.buildings[-1].outer_area.items()}
        assert outwall_dict_round == {-2.0: 140,
                                      -1.0: 140,
                                      0.0: 2.0,
                                      90.0: 14.0,
                                      180.0: 10.0,
                                      270.0: 14.0}

    def test_fill_window_area_dict(self):
        '''test of fill_window_area_dict'''
        prj.buildings[-1].fill_window_area_dict()
        assert prj.buildings[-1].window_area == {90.0: 1.0,
                                                 180.0: 8.0,
                                                 270.0: 5.0}

    def test_calc_building_parameter(self):
        '''test of calc_building_parameter'''
        prj.set_default()
        helptest.building_test2(prj)

        prj.buildings[-1].calc_building_parameter(number_of_elements=2,
                                                  merge_windows=True,
                                                  used_library='AixLib')

        assert round(prj.buildings[-1].volume, 1) == 490.0
        assert round(
            prj.buildings[-1].sum_heat_load, 4) == 5023.0256

    # methods in therm_zone

    def test_calc_zone_parameters(self):
        '''test of calc zone parameter, no calculation verification'''

        prj.buildings[-1].thermal_zones[-1].calc_zone_parameters(
            number_of_elements=2, merge_windows=False)
        prj.buildings[-1].thermal_zones[-1].calc_zone_parameters(
            number_of_elements=2, merge_windows=True)

    def test_heat_load(self):
        '''test of heating_load'''
        prj.set_default()
        helptest.building_test2(prj)
        prj.buildings[-1].thermal_zones[-1].infiltration_rate = 0.5
        prj.buildings[-1].thermal_zones[-1].calc_zone_parameters(
            number_of_elements=2,
            merge_windows=True)
        prj.buildings[-1].thermal_zones[-1].model_attr.calc_attributes()
        assert round(
            prj.buildings[-1].thermal_zones[-1].model_attr.heat_load,
            4) == 6659.6256

    def test_sum_building_elements(self):
        '''test of combine_building_elements'''
        prj.set_default()
        helptest.building_test2(prj)

        from teaser.logic.buildingobjects.calculation.four_element import\
            FourElement

        therm_zone = prj.buildings[-1].thermal_zones[-1]

        calc_attr = FourElement(therm_zone, merge_windows=True, t_bt=5)

        helplist = therm_zone.outer_walls + therm_zone.rooftops +\
            therm_zone.ground_floors + therm_zone.inner_walls +\
            therm_zone.ceilings + therm_zone.floors + therm_zone.windows

        for element in helplist:
            element.calc_equivalent_res()
            element.calc_ua_value()

        calc_attr._sum_outer_wall_elements()
        calc_attr._sum_ground_floor_elements()
        calc_attr._sum_rooftop_elements()
        calc_attr._sum_inner_wall_elements()
        calc_attr._sum_window_elements()

        # innerwall

        assert round(calc_attr.ua_value_iw, 16) == 14.286493860845841
        assert round(calc_attr.area_iw, 1) == 34.0
        assert round(calc_attr.r_conv_inner_iw, 18) == 0.010893246187363833
        assert round(calc_attr.r_rad_inner_iw, 19) == 0.0058823529411764705
        assert round(calc_attr.r_comb_inner_iw, 19) == 0.003819709702062643
        assert round(calc_attr.alpha_conv_inner_iw, 1) == 2.7
        assert round(calc_attr.alpha_rad_inner_iw, 1) == 5.0
        assert round(calc_attr.alpha_comb_inner_iw, 1) == 7.7

        # outerwall
        assert round(calc_attr.ua_value_ow, 16) == 19.83577523748189
        assert round(calc_attr.area_ow, 1) == 48.0
        assert round(calc_attr.r_conv_inner_ow, 19) == 0.007716049382716048
        assert round(calc_attr.r_rad_inner_ow, 18) == 0.004166666666666667
        assert round(calc_attr.r_comb_inner_ow, 20) == 0.0027056277056277055
        assert round(calc_attr.r_conv_outer_ow, 20) == 0.0010416666666666667
        assert round(calc_attr.r_rad_outer_ow, 18) == 0.004166666666666667
        assert round(calc_attr.r_comb_outer_ow, 20) == 0.0008333333333333334
        assert round(calc_attr.alpha_conv_inner_ow, 5) == 2.7
        assert round(calc_attr.alpha_rad_inner_ow, 5) == 5.0
        assert round(calc_attr.alpha_comb_inner_ow, 5) == 7.7
        assert round(calc_attr.alpha_conv_outer_ow, 1) == 20.0
        assert round(calc_attr.alpha_rad_outer_ow, 5) == 5.0
        assert round(calc_attr.alpha_comb_outer_ow, 1) == 25.0

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

    def test_calc_chain_matrix(self):
        '''test of calc_chain_matrix'''
        from teaser.logic.buildingobjects.calculation.two_element import\
            TwoElement

        therm_zone = prj.buildings[-1].thermal_zones[-1]

        omega = (2 * math.pi / 86400 / 5)

        calc_attr = TwoElement(therm_zone, merge_windows=True, t_bt=5)

        helplist_outer_walls = therm_zone.outer_walls + therm_zone.rooftops +\
            therm_zone.ground_floors + therm_zone.windows

        r1_ow, c1_ow = calc_attr._calc_parallel_connection(
            element_list=helplist_outer_walls,
            omega=omega)
        assert round(r1_ow, 14) == 0.00100751548411
        assert round(c1_ow, 5) == 3648580.59312

        helplist_inner_walls = therm_zone.inner_walls +\
            therm_zone.ceilings + therm_zone.floors

        r1_iw, c1_iw = calc_attr._calc_parallel_connection(
            element_list=helplist_inner_walls,
            omega=omega)
        assert round(r1_iw, 13) == 0.0097195611408
        assert round(c1_iw, 6) == 319983.518743

    def test_calc_weightfactor(self):
        '''test of calc_weightfactor'''
        prj.set_default()
        helptest.building_test2(prj)
        prj.buildings[-1].calc_building_parameter(number_of_elements=2,
                                                  merge_windows=True,
                                                  used_library='AixLib')

        calc_attr = prj.buildings[-1].thermal_zones[-1].model_attr
        print(calc_attr.weightfactor_ow)
        weightfactors_test_list = [
            0.024530650180761254,
            0.03434291025306576,
            0.024530650180761254,
            0.03434291025306576,
            0.3407000330729792]

        assert calc_attr.weightfactor_ow.sort() == \
            weightfactors_test_list.sort()
        weightfactors_test_list = [
            0.0,
            0.054214642472656345,
            0.08674342795625017,
            0.054214642472656345,
            0.0]
        assert calc_attr.weightfactor_win.sort() ==\
            weightfactors_test_list.sort()

        prj.buildings[-1].thermal_zones[-1].weightfactor_ow = []
        prj.buildings[-1].thermal_zones[-1].weightfactor_win = []

        prj.buildings[-1].calc_building_parameter(number_of_elements=2,
                                                  merge_windows=False,
                                                  used_library='AixLib')
        calc_attr = prj.buildings[-1].thermal_zones[-1].model_attr

        weightfactors_test_list = [
            0.03047939672771178,
            0.04267115541879649,
            0.03047939672771178,
            0.04267115541879649,
            0.423320678280269]

        assert calc_attr.weightfactor_ow.sort() ==\
            weightfactors_test_list.sort()

        weightfactors_test_list = [
            0.0,
            0.27777777777777778,
            0.44444444444444453,
            0.27777777777777778,
            0.0]
        assert calc_attr.weightfactor_win.sort() ==\
            weightfactors_test_list.sort()

    def test_calc_two_element(self):
        '''test of calc_two_element'''
        prj.set_default()
        helptest.building_test2(prj)

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.calc_zone_parameters(
            number_of_elements=2,
            merge_windows=True)

        zone_attr = therm_zone.model_attr
        assert round(zone_attr.area_ow, 1) == 328.0
        assert round(zone_attr.ua_value_ow, 16) == 135.5818558809656
        assert round(zone_attr.r_conv_inner_ow, 16) == 0.0016512549537649
        assert round(zone_attr.r_rad_inner_ow, 16) == 0.000609756097561
        outer_conv_roof_temp = sum(
            1 / roof.r_outer_conv for roof in therm_zone.rooftops)
        # old calc was only ow, in the new core we calc outer walls plus
        # rooftops, therefore we need to subtract it.
        r_outer_conv_ow_temp = 1 / (
            (1 / zone_attr.r_conv_outer_ow) - outer_conv_roof_temp)
        assert round(r_outer_conv_ow_temp, 9) == 0.001041667
        assert round(zone_attr.alpha_conv_inner_ow, 5) == 1.84634
        assert round(zone_attr.alpha_rad_inner_ow, 1) == 5.0
        assert round(zone_attr.r1_win, 15) == 0.003316749585406
        assert round(zone_attr.r1_ow, 15) == 0.000772773294534
        assert round(zone_attr.r1_iw, 15) == 0.009719561140816
        # old calc core was without inner window radiation and without
        # combined alpha
        r_rest = zone_attr.r_rest_ow + 1 / (zone_attr.alpha_comb_outer_ow *
                                            zone_attr.area_ow)
        assert round(r_rest, 15) == 0.004740706924836

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.calc_zone_parameters(
            number_of_elements=2,
            merge_windows=False)

        zone_attr = therm_zone.model_attr
        assert round(zone_attr.area_ow, 1) == 328.0
        assert round(zone_attr.ua_value_ow, 16) == 135.5818558809656
        assert round(zone_attr.r_conv_inner_ow, 16) == 0.0016512549537649
        assert round(zone_attr.r_rad_inner_ow, 16) == 0.000609756097561
        outer_conv_roof_temp = sum(
            1 / roof.r_outer_conv for roof in therm_zone.rooftops)
        # old calc was only ow, in the new core we calc outer walls plus
        # rooftops, therefore we need to subtract it.
        r_outer_conv_ow_temp = 1 / (
            (1 / zone_attr.r_conv_outer_ow) - outer_conv_roof_temp)
        assert round(r_outer_conv_ow_temp, 9) == 0.001041667
        assert round(zone_attr.alpha_conv_inner_ow, 5) == 1.84634
        assert round(zone_attr.alpha_rad_inner_ow, 1) == 5.0
        # old r1_win
        sum_r1_win = 0
        for win_count in therm_zone.windows:
            sum_r1_win += 1 / (win_count.r1 + win_count.r_outer_comb)
        r1_win_temp = 1 / sum_r1_win
        # new r1_win
        assert round(r1_win_temp, 15) == 0.02212271973466
        assert round(zone_attr.r1_win, 15) == 0.019900497512438001
        assert round(zone_attr.r1_ow, 15) == 0.001007515484109
        assert round(zone_attr.r1_iw, 15) == 0.009719561140816
        # old r_rest
        r_rest_ow = zone_attr.r_total_ow - zone_attr.r1_ow -\
            1 / (1 / zone_attr.r_conv_inner_ow + 1 / zone_attr.r_rad_inner_ow)
        assert round(r_rest_ow, 15) == 0.005922787404456
        assert round(zone_attr.r_rest_ow, 15) == 0.005852240613452

    def test_volume_zone(self):
        '''test of volume_zone'''

        prj.buildings[-1].thermal_zones[-1].set_volume_zone()
        assert prj.buildings[-1].thermal_zones[-1].volume == 490.0

    def test_set_inner_wall_area(self):
        '''test of set_inner_wall_area'''

        prj.buildings[-1].thermal_zones[-1].set_inner_wall_area()
        for wall in prj.buildings[-1].thermal_zones[-1].inner_walls:
            assert round(wall.area, 16) == 11.951219512195122

            # methods in UseConditions18599()

    def test_load_use_conditions(self):
        '''test of load_use_conditions, no parameter checking'''
        use_cond = prj.buildings[-1].thermal_zones[-1].use_conditions
        use_cond.load_use_conditions("Living",
                                     data_class=prj.data)

    def test_save_use_conditions(self):
        '''test of save_use_conditions, no parameter checking'''
        import os

        path = os.path.join(utilities.get_default_path(),
                            'UseCondUT.xml')
        prj.data.path_uc = path
        prj.data.load_uc_binding()
        use_cond = prj.buildings[-1].thermal_zones[-1].use_conditions
        use_cond.save_use_conditions(data_class=prj.data)

        # methods in BuildingElement

    def test_ua_value(self):
        '''test of ua_value'''
        prj.set_default()
        helptest.building_test2(prj)

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].calc_ua_value()

        assert round(
            therm_zone.outer_walls[0].ua_value,
            15) == 4.132453174475393

    def test_gather_element_properties(self):
        '''test of gather_element_properties'''
        outerWalls = prj.buildings[-1].thermal_zones[-1].outer_walls[0]
        number_of_layer, density, thermal_conduc, heat_capac, thickness = \
            outerWalls.gather_element_properties()
        assert number_of_layer == 2
        assert (density == [5., 2.]).all()
        assert (thermal_conduc == [4., 2.]).all()
        assert (heat_capac == [0.48, 0.84]).all()
        assert (thickness == [5., 2.]).all()

    def test_load_type_element(self):
        '''test of load_type_element, no parameter checking'''

        # test load function
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].load_type_element(1988, "heavy", prj.data)
        therm_zone.inner_walls[0].load_type_element(1988, "light", prj.data)
        therm_zone.windows[0].load_type_element(
            1988,
            "Kunststofffenster, Isolierverglasung",
            prj.data)

    def test_save_type_element(self):
        '''test of save_type_element, no parameter checking'''
        import os
        # test load function
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        path = os.path.join(utilities.get_default_path(),
                            'unitTestTB.xml')
        prj.data.path_tb = path
        prj.data.load_tb_binding()
        therm_zone.outer_walls[0].save_type_element(data_class=prj.data)
        therm_zone.inner_walls[0].save_type_element(data_class=prj.data)
        therm_zone.windows[0].save_type_element(data_class=prj.data)

    # methods in Wall

    def test_calc_equivalent_res_wall(self):
        '''test of calc_equivalent_res, wall'''
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
        '''test of insulate_wall'''
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].insulate_wall("EPS035", 0.04)
        assert round(therm_zone.outer_walls[0].ua_value, 6) == 2.806838

    def test_retrofit_wall(self):
        '''test of retrofit_wall'''
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(2016, "EPS035")
        assert round(therm_zone.outer_walls[0].ua_value, 6) == 2.4
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(2010, "EPS035")
        assert round(therm_zone.outer_walls[0].ua_value, 6) == 2.4
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(2005, "EPS035")
        assert round(therm_zone.outer_walls[0].ua_value, 2) == 4.13
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(1998, "EPS035")
        assert round(therm_zone.outer_walls[0].ua_value, 2) == 4.13
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(1990, "EPS035")
        assert round(therm_zone.outer_walls[0].ua_value, 2) == 4.13
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(1980, "EPS035")
        assert round(therm_zone.outer_walls[0].ua_value, 2) == 4.13

    def test_calc_equivalent_res_win(self):
        '''test of calc_equivalent_res, win'''
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.windows[0].calc_equivalent_res()

        assert round(therm_zone.windows[0].r1, 3) == 0.072

    def test_change_infiltration_rate(self):
        '''test for change of infiltration_rate'''
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        assert therm_zone.infiltration_rate == 0.2

        therm_zone.infiltration_rate = 0.7
        assert therm_zone.infiltration_rate == 0.7

        therm_zone.use_conditions.base_ach = 0.5
        assert therm_zone.infiltration_rate == 0.5


    def test_sim_results(self):

        #  Generate project and add residential building

        prj = Project(load_data=True)
        prj.name = "ArchetypeBuildings"
        prj.merge_windows_calc = True

        prj.add_residential(
            method='iwu',
            usage='single_family_dwelling',
            name='Test_res_building',
            year_of_construction=1962,
            number_of_floors=2,
            height_of_floors=2.8,
            net_leased_area=100,
            with_ahu=False,
            residential_layout=0,
            neighbour_buildings=0,
            attic=1,
            cellar=1,
            dormer=0,
            construction_type='heavy',
            number_of_apartments=None)

        #  Extract thermal_zone
        thermal_zone = prj.buildings[0].thermal_zones[0]

        #  Calculate beta angle
        beta = thermal_zone.model_attr.tilt_facade

        gamma = thermal_zone.model_attr.orientation_facade

        #  Recalculate to VDI core azimuth usage
        for i in range(len(gamma)):
            angle = gamma[i]
            if angle == -1 or angle == -2:
                gamma[i] = 0.0
            else:
                gamma[i] = angle - 180

        weather = weat.Weather(
            beta=beta,
            gamma=gamma,
            weather_path=None,
            albedo=0.2,
            timeZone=1,
            altitude=0,
            location=(49.5, 8.5),
            timestep=3600,
            do_sun_rad=True)

        timesteps = 365 * 24

        # Load constant house parameters
        if len(thermal_zone.inner_walls) != 0:
            withInnerwalls = True
        else:
            withInnerwalls = False

        # Max. irradiation
        i_max = 100

        list_window_areas = []
        list_sunblind = []
        for window in thermal_zone.windows:
            list_window_areas.append(window.area)
            list_sunblind.append(0.0)

        # Convert into house data dictionary
        #  #-------------------------------------------------------
        houseData = {"R1i": thermal_zone.model_attr.r1_iw,
                     "C1i": thermal_zone.model_attr.c1_iw,
                     "Ai": thermal_zone.model_attr.area_iw,
                     "RRest": thermal_zone.model_attr.r_rest_ow,
                     "R1o": thermal_zone.model_attr.r1_ow,
                     "C1o": thermal_zone.model_attr.c1_ow,
                     "Ao": [thermal_zone.model_attr.area_ow],
                     "Aw": thermal_zone.model_attr.window_areas,
                     "At": thermal_zone.model_attr.transparent_areas,
                     "Vair": thermal_zone.volume,
                     "rhoair": thermal_zone.density_air,
                     "cair": thermal_zone.heat_capac_air,
                     "splitfac": thermal_zone.model_attr.ratio_conv_rad_inner_win,
                     "g": thermal_zone.model_attr.weighted_g_value,
                     "alphaiwi": thermal_zone.model_attr.alpha_comb_inner_iw,
                     "alphaowi": thermal_zone.model_attr.alpha_comb_inner_ow,
                     "alphaWall": thermal_zone.model_attr.alpha_comb_outer_ow * thermal_zone.model_attr.area_ow,
                     "withInnerwalls": withInnerwalls,
                     "aowo": thermal_zone.model_attr.solar_absorp_ow,
                     "temperatureground": thermal_zone.t_ground,
                     "weightfactorswall": thermal_zone.model_attr.weightfactor_ow,
                     "weightfactorswindow": thermal_zone.model_attr.weightfactor_win,
                     "weightfactorground": thermal_zone.model_attr.weightfactor_ground,
                     "gsunblind": thermal_zone.model_attr.g_sunblind,
                     "Imax": i_max}

        #  Solar radiation input on each external area in W/m2
        #  #-------------------------------------------------------
        # solarRad_in = np.zeros((timesteps, 5))
        solarRad_in = np.transpose(weather.sun_rad)

        source_igRad = np.zeros(timesteps)

        krad = 1

        #  Equal air temperature based on VDI in K
        #  #-------------------------------------------------------
        # #  equalAirTemp = np.zeros(timesteps) + 273.15 + 10
        # equalAirTemp = weather.temp + 0.5 + 273.15

        t_black_sky = np.zeros(timesteps) + 273.15

        sunblind_in = np.zeros_like(solarRad_in)
        sunblind_in[solarRad_in > i_max] = 0.85

        eq_air_params = {"aExt": thermal_zone.model_attr.solar_absorp_ow,
                         # coefficient of absorption of exterior walls (outdoor)
                         "eExt": thermal_zone.model_attr.ir_emissivity_outer_ow,
                         # coefficient of emission of exterior walls (outdoor)
                         "wfWall": thermal_zone.model_attr.weightfactor_ow,
                         # weight factors of the walls
                         "wfWin": thermal_zone.model_attr.weightfactor_win,
                         # weight factors of the windows
                         "wfGro": thermal_zone.model_attr.weightfactor_ground,
                         # weight factor of the ground (0 if not considered)
                         "T_Gro": thermal_zone.t_ground,
                         "alpha_wall_out": thermal_zone.model_attr.alpha_conv_outer_ow,
                         "alpha_rad_wall": thermal_zone.model_attr.alpha_rad_outer_ow,
                         "withLongwave": False}

        t_dry_bulb = weather.temp + 273.15

        equalAirTemp = equ_air.equal_air_temp(HSol=solarRad_in,
                                              TBlaSky=t_black_sky,
                                              TDryBul=t_dry_bulb,
                                              sunblind=sunblind_in,
                                              params=eq_air_params)

        #  Environment temperatures in K
        #  #-------------------------------------------------------
        # weatherTemperature = np.zeros(timesteps) + 273.15 + 10  # in K
        weatherTemperature = weather.temp + 273.15

        #  Ventilation rate: Fresh air at temperature weatherTemperature in m3/s
        #  #-------------------------------------------------------
        # ventRate = np.zeros(timesteps)
        ventRate = np.zeros(timesteps) + (thermal_zone.volume *
                                          thermal_zone.infiltration_rate / 3600)

        #  Internal convective gains in W
        #  #-------------------------------------------------------
        #  TODO: Substitute with TEASER boundary conditions
        #  logic/buildingobjects/boundaryconditions/boundaryconditions.py
        #  Living (18599) / SIA for occupancy
        Q_ig = np.zeros(timesteps) + 200

        # Radiative heat transfer coef. between inner and outer walls in W/m2K
        alphaRad = np.zeros(timesteps) + \
                   thermal_zone.model_attr.alpha_rad_inner_mean

        # Define set points for heating
        #  #-------------------------------------------------------
        #  TODO: Calculate with function call (depending on occupancy)
        # t_set_heating = np.zeros(timesteps) + 273.15 + 21  # in Kelvin
        t_set_heat_day = \
            np.array([18, 18, 18, 18, 18, 18, 21, 21, 21, 21, 21, 21,
                      21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 21, 18]) + 273.15
        t_set_heating = np.tile(t_set_heat_day, 365)

        # Define set points for cooling (cooling is disabled for high values)
        #  #-------------------------------------------------------
        t_set_cooling = np.zeros(timesteps) + 273.15 + 1000  # in Kelvin

        heater_limit = np.zeros((timesteps, 3)) + 1e10
        cooler_limit = np.zeros((timesteps, 3)) - 1e10

        # Calculate indoor air temperature with VDI model
        t_air, q_hc, q_iw, q_ow = \
            low_order_VDI.reducedOrderModelVDI(houseData=houseData,
                                               weatherTemperature=weatherTemperature,
                                               solarRad_in=solarRad_in,
                                               equalAirTemp=equalAirTemp,
                                               alphaRad=alphaRad,
                                               ventRate=ventRate,
                                               Q_ig=Q_ig,
                                               source_igRad=source_igRad,
                                               krad=krad,
                                               heater_order=np.array(
                                                   [1, 2, 3]),
                                               cooler_order=np.array(
                                                   [1, 2, 3]),
                                               t_set_heating=t_set_heating,
                                               t_set_cooling=t_set_cooling,
                                               heater_limit=heater_limit,
                                               cooler_limit=cooler_limit)

        #  Load reference values
        this_path = os.path.dirname(os.path.abspath(__file__))
        filename = 'res_unretrofited.txt'
        load_path = os.path.join(this_path, 'inputs', filename)

        load_array = np.genfromtxt(fname=load_path, delimiter='\t',
                                   skip_header=1)

        temp_ref = load_array[:, 0]
        q_hc_ref = load_array[:, 1]

        np.testing.assert_array_almost_equal(t_air, temp_ref, decimal=3)
        np.testing.assert_array_almost_equal(q_hc, q_hc_ref, decimal=3)

        #  Do retrofit of building
        prj.buildings[0].retrofit_building(year_of_retrofit=2014)

        # Calculate indoor air temperature with VDI model
        t_air2, q_hc2, q_iw, q_ow = \
            low_order_VDI.reducedOrderModelVDI(houseData=houseData,
                                               weatherTemperature=weatherTemperature,
                                               solarRad_in=solarRad_in,
                                               equalAirTemp=equalAirTemp,
                                               alphaRad=alphaRad,
                                               ventRate=ventRate,
                                               Q_ig=Q_ig,
                                               source_igRad=source_igRad,
                                               krad=krad,
                                               heater_order=np.array(
                                                   [1, 2, 3]),
                                               cooler_order=np.array(
                                                   [1, 2, 3]),
                                               t_set_heating=t_set_heating,
                                               t_set_cooling=t_set_cooling,
                                               heater_limit=heater_limit,
                                               cooler_limit=cooler_limit)

        #  Load reference values
        this_path = os.path.dirname(os.path.abspath(__file__))
        filename2 = 'res_retrofited.txt'
        load_path2 = os.path.join(this_path, 'inputs', filename2)

        load_array2 = np.genfromtxt(fname=load_path2, delimiter='\t',
                                    skip_header=1)

        temp_ref2 = load_array2[:, 0]
        q_hc_ref2 = load_array2[:, 1]

        np.testing.assert_array_almost_equal(t_air2, temp_ref2, decimal=3)
        np.testing.assert_array_almost_equal(q_hc2, q_hc_ref2, decimal=3)

    #  VDI 6007 validation test cases
    #  ######################################################################

    def test_vdi_6007_validation_case1(self):
        """
        Run VDI 6007 test case 1
        """

        tuple_res = vdi1.run_case1()

        #  Check if temperature deviation is below 0.1 Kelvin
        for val in tuple_res:
            assert val < 0.15

    def test_vdi_6007_validation_case2(self):
        """
        Run VDI 6007 test case 2
        """
        tuple_res = vdi2.run_case2()

        #  Check if temperature deviation is below 0.1 Kelvin
        for val in tuple_res:
            assert val < 0.15

    def test_vdi_6007_validation_case3(self):
        """
        Run VDI 6007 test case 3
        """
        tuple_res = vdi3.run_case3()

        #  Check if temperature deviation is below 0.1 Kelvin
        for val in tuple_res:
            assert val < 0.15

    def test_vdi_6007_validation_case4(self):
        """
        Run VDI 6007 test case 4
        """
        tuple_res = vdi4.run_case4()

        #  Check if temperature deviation is below 0.1 Kelvin
        for val in tuple_res:
            assert val < 0.15

    def test_vdi_6007_validation_case5(self):
        """
        Run VDI 6007 test case 5
        """
        tuple_res = vdi5.run_case5()

        #  Check if temperature deviation is below 0.1 Kelvin
        for val in tuple_res:
            assert val < 0.15

    def test_vdi_6007_validation_case6(self):
        """
        Run VDI 6007 test case 6
        """
        tuple_res = vdi6.run_case6()

        #  Check if power deviation is below 1 Watt
        for val in tuple_res:
            assert val < 1.5

    def test_vdi_6007_validation_case7(self):
        """
        Run VDI 6007 test case 7
        """
        tuple_res = vdi7.run_case7()

        #  Check if power deviation is below 1 Watt
        for val in tuple_res:
            assert val < 1.5

    def test_vdi_6007_validation_case8(self):
        """
        Run VDI 6007 test case 8
        """
        tuple_res = vdi8.run_case8()

        #  Check if temperature deviation is below 0.1 Kelvin
        for val in tuple_res:
            assert val < 0.15

    def test_vdi_6007_validation_case9(self):
        """
        Run VDI 6007 test case 9
        """
        tuple_res = vdi9.run_case9()

        #  Check if temperature deviation is below 0.1 Kelvin
        for val in tuple_res:
            assert val < 0.15

    def test_vdi_6007_validation_case10(self):
        """
        Run VDI 6007 test case 10
        """
        tuple_res = vdi10.run_case10()

        #  Check if temperature deviation is below 0.1 Kelvin
        for val in tuple_res:
            assert val < 0.15

    def test_vdi_6007_validation_case11(self):
        """
        Run VDI 6007 test case 11

        Reference values are taken from VDI 6020 (not from VDI 6007)
        """
        tuple_res = vdi11.run_case11()

        #  Check if deviation is within limits
        for i in range(len(tuple_res)):
            if i in [0, 1, 2]:
                #  Temperature values
                assert tuple_res[i] < 1
            elif i in [3, 4, 5]:
                #  Power values
                assert tuple_res[i] < 50

    def test_vdi_6007_validation_case12(self):
        """
        Run VDI 6007 test case 12
        """
        tuple_res = vdi12.run_case12()

        #  Check if temperature deviation is below 0.1 Kelvin
        for val in tuple_res:
            assert val < 0.15

    #  ######################################################################

    def test_weather_restructuring(self):
        """
        Compare old and new weather class after TEASER restructuring
        #297
        """

        beta = [90.0, 0.0, 90.0, 0.0, 90.0, 90.0]
        gamma = [0.0, 0.0, -180.0, 0.0, -90.0, 90.0]
        weather_path = None
        albedo = 0.2
        time_zone = 1
        altitude = 0
        location = (49.5, 8.5)
        timestep = 3600
        do_sun_rad = True

        weather = weat.Weather(beta=beta,
                               gamma=gamma,
                               weather_path=weather_path,
                               albedo=albedo,
                               timeZone=time_zone,
                               altitude=altitude,
                               location=location,
                               timestep=timestep,
                               do_sun_rad=do_sun_rad)

        this_path = os.path.dirname(os.path.abspath(__file__))
        filename = 'ref_radiation.txt'
        load_path = os.path.join(this_path, 'inputs', filename)

        rad_data = np.transpose(np.genfromtxt(fname=load_path, delimiter='\t',
                                              skip_header=1))

        np.testing.assert_array_almost_equal(weather.sun_rad, rad_data,
                                             decimal=3)