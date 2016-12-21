'''
Created July 2015

@author: TEASER 4 Development Team
'''

from teaser.logic import utilities
from teaser.project import Project
import math

import helptest
prj = Project(True)


class Test_teaser(object):
    """Unit Tests for TEASER"""
    global prj

    def test_calc_vdi_room1(self):
        '''Parameter Verification for rouvel room1'''
        import teaser.examples.verification.verification_room1 as room1

        room1_prj = room1.parameter_room1()
        therm_zone = room1_prj.buildings[0].thermal_zones[0]

        #parameters inner wall Typraum S

        assert round(therm_zone.r1_iw, 13) == 0.0005956934075
        assert round(therm_zone.c1_iw / 1000, 7) == 14836.3546282
        assert round(therm_zone.area_iw, 1) == 75.5
        assert round(therm_zone.alpha_conv_inner_iw, 13) == 2.23642384105960

        #paremeters outer wall Typraum S

        assert round(therm_zone.r_rest_ow, 13) == 0.0427687193786
        assert round(therm_zone.r1_ow, 13) == 0.0043679129367
        assert round(therm_zone.c1_ow / 1000, 7) == 1600.8489399
        assert round(therm_zone.area_ow, 1) == 3.5
        assert round(therm_zone.area_win, 1) == 7.0
        assert round(therm_zone.alpha_conv_inner_ow, 1) == 2.7
        assert round(therm_zone.alpha_comb_outer_ow, 1) == 25.0

    def test_calc_vdi_room3(self):
        '''Parameter Verification for room 3'''
        import teaser.examples.verification.verification_room3 as room3

        room3_prj = room3.parameter_room3()
        therm_zone = room3_prj.buildings[0].thermal_zones[0]

        #parameters inner wall Typraum L

        assert round(therm_zone.r1_iw, 13) == 0.003385649748
        assert round(therm_zone.c1_iw / 1000, 7) == 7445.3648976
        assert round(therm_zone.area_iw, 1) == 75.5
        assert round(therm_zone.alpha_conv_inner_iw, 13) == 2.23642384105960

        #parameters outer wall Typraum L

        assert round(therm_zone.r_rest_ow, 13) == 0.0431403889233
        assert round(therm_zone.r1_ow, 13) == 0.004049351608
        assert round(therm_zone.c1_ow / 1000, 7) == 47.8617641
        assert round(therm_zone.area_ow, 1) == 3.5
        assert round(therm_zone.area_win, 1) == 7.0
        assert round(therm_zone.alpha_conv_inner_ow, 1) == 2.7
        assert round(therm_zone.alpha_comb_outer_ow, 1) == 25.0

    def test_calc_vdi_room8(self):
        '''Parameter Verification for room 8'''
        import teaser.examples.verification.verification_room8 as room8

        room8_prj = room8.parameter_room8()
        therm_zone = room8_prj.buildings[0].thermal_zones[0]

        assert round(therm_zone.r1_iw, 13) == 0.0006688956391
        assert round(therm_zone.c1_iw / 1000, 7) == 12391.3638631
        assert round(therm_zone.area_iw, 1) == 60.5
        assert round(therm_zone.alpha_conv_inner_iw, 13) == 2.1214876033058

        assert round(therm_zone.r_rest_ow, 13) == 0.0207059264866
        assert round(therm_zone.r1_ow, 13) == 0.0017362530106
        assert round(therm_zone.c1_ow / 1000, 7) == 5259.932231
        assert round(therm_zone.area_ow, 1) == 11.5
        assert round(therm_zone.area_win, 1) == 14.0
        assert round(therm_zone.alpha_conv_inner_ow, 1) == 2.7
        assert round(therm_zone.alpha_comb_outer_ow, 1) == 25.0
        assert round(therm_zone.weightfactor_ow[1], 13) == 0.1324989973869
        assert round(therm_zone.weightfactor_win[0], 13) == 0.4047663456282

    #EBC Calculation Verification, with parameters from TEASER3

    def test_calc_ebc(self):
        '''
        Parameter Verification for ebc calculation method. Values are compared
        with TEASER3 values.
        '''
        prj.set_default()
        prj.load_project(utilities.get_full_path("examples/examplefiles"
                                              "/new.teaserXML"))
        therm_zone = prj.buildings[0].thermal_zones[0]
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = 'AixLib'
        prj.buildings[0].calc_building_parameter()

        assert round(therm_zone.r1_iw, 11) == 4.62113e-06
        assert round(therm_zone.c1_iw, 2) == 1209810287.22
        assert round(therm_zone.area_iw, 5) == 9866.66667
        assert round(therm_zone.alpha_conv_inner_iw, 5) == 2.37568

        assert round(therm_zone.r_rest_ow, 5) == 0.00183
        assert round(therm_zone.r1_ow, 10) == 3.06155e-05
        assert round(therm_zone.c1_ow, 3) == 226923157.846
        assert round(therm_zone.area_ow, 5) == 920.0

        assert round(therm_zone.alpha_conv_inner_ow, 5) == 1.83043

        assert round(therm_zone.alpha_conv_outer_ow, 5) == 20.0
        assert round(therm_zone.alpha_comb_outer_ow, 5) == 25.0
        assert round(therm_zone.alpha_conv_inner_win, 5) == 2.7
        assert round(therm_zone.alpha_conv_outer_win, 5) == 20.0
        assert round(therm_zone.alpha_comb_outer_win, 5) == 25.0

        assert round(therm_zone.weightfactor_ow[0], 5) == 0.04588
        assert round(therm_zone.weightfactor_win[0], 5) == 0.33333
        assert round(therm_zone.weightfactor_ground[0], 5) == 0.54398

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

        #general parameters

        assert len(test_office.thermal_zones) == 6

        #zone specific parameters

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

        #facade specific parameters

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

        #facade specific parameters

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

        #facade specific parameters

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

        #facade specific parameters

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

        #general parameters

        assert len(test_institute4.thermal_zones) == 7

        #zone specific parameters

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

        #facade specific parameters

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

        #general parameters

        assert len(test_institute8.thermal_zones) == 7

        #zone specific parameters

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

        #facade specific parameters

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

        #general parameters

        assert len(test_institute.thermal_zones) == 7

        #zone specific parameters

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

        #facade specific parameters

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
        from teaser.logic.archetypebuildings.bmvbs.singlefamilydwelling import \
            SingleFamilyDwelling

        prj.set_default()
        test_residential = SingleFamilyDwelling(parent=prj,
                                                name="TestBuilding",
                                                year_of_construction=1988,
                                                number_of_floors=3,
                                                height_of_floors=3,
                                                net_leased_area=2500)

        test_residential.generate_archetype()

        #general parameters

        assert len(test_residential.thermal_zones) == 1

        #zone specific parameters

        for zone in test_residential.thermal_zones:
            if zone.name == "SingleDwelling":
                assert zone.area == 2500

        #facade specific parameters

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

        #facade specific parameters

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

        #facade specific parameters

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

        #facade specific parameters

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

    #methods in Project, these tests only test if the API function works,
    #not if it produces reliable results.

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


    #commented until we find solution for opengis PyXB bindings
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

        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = True
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_aixlib(building_model='MultizoneEquipped')
        prj.number_of_elements_calc = 2
        prj.merge_windows_calc = False
        prj.used_library_calc = 'AixLib'
        prj.calc_all_buildings()
        prj.export_aixlib(building_model='MultizoneEquipped')

    def test_export_annex(self):
        '''test of export_annex, no calculation verification'''

        prj.number_of_elements_calc = 2
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
        prj.merge_windows_calc = False
        prj.used_library_calc = 'Annex60'
        prj.calc_all_buildings()
        prj.export_annex()

    def test_export_parameters_txt(self):
        '''test of the export of the readable parameter output'''

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

    #methods in Building

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

    def test_set_specific_wall_area(self):
        '''test of set_specific_wall_area'''
        prj.set_default()
        helptest.building_test2(prj)
        prj.buildings[-1].set_specific_wall_area(
            prj.buildings[-1].thermal_zones[-1],
            prj.buildings[-1].thermal_zones[-1].outer_walls[1],
            500)

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        assert round(therm_zone.outer_walls[0].area, 2) == 10.0
        assert round(therm_zone.outer_walls[1].area, 1) == 500

    def test_fill_outer_wall_area_dict(self):
        '''test of fill_outer_wall_area_dict'''

        prj.buildings[-1].fill_outer_area_dict()
        outwall_dict_round = {key: round(value, 2) for key, value in
                              prj.buildings[-1].outer_area.items()}
        assert outwall_dict_round == {-2.0: 140,
                                      -1.0: 140,
                                      0.0: 10.0,
                                      90.0: 500.0,
                                      180.0: 10.0,
                                      270.0: 14.0}

    def test_fill_window_area_dict(self):
        '''test of fill_window_area_dict'''
        prj.buildings[-1].fill_window_area_dict()
        assert prj.buildings[-1].window_area == {90.0: 5.0,
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
            prj.buildings[-1].sum_heating_load, 4) == 8118.4126

    #methods in therm_zone

    def test_calc_zone_parameters(self):
        '''test of calc zone parameter, no calculation verification'''

        prj.buildings[-1].thermal_zones[-1].calc_zone_parameters(
            number_of_elements=2, merge_windows=False)
        prj.buildings[-1].thermal_zones[-1].calc_zone_parameters(
            number_of_elements=2, merge_windows=True)

    def test_heating_load(self):
        '''test of heating_load'''
        prj.set_default()
        helptest.building_test2(prj)
        prj.buildings[-1].thermal_zones[-1].calc_zone_parameters(number_of_elements=2,
                                                                 merge_windows=True)
        prj.buildings[-1].thermal_zones[-1].calc_heat_load()
        assert round(
            prj.buildings[-1].thermal_zones[-1].heating_load,
            4) == 8118.4126

    def test_sum_building_elements(self):
        '''test of combine_building_elements'''
        prj.set_default()
        helptest.building_test2(prj)

        #execute zone parameters for therm_zone

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        for out_wall in therm_zone.outer_walls:
            out_wall.calc_equivalent_res()
            out_wall.calc_ua_value()

        for in_wall in therm_zone.inner_walls:
            in_wall.calc_equivalent_res()
            in_wall.calc_ua_value()

        for win in therm_zone.windows:
            win.calc_equivalent_res()
            win.calc_ua_value()

        prj.buildings[-1].thermal_zones[-1].sum_building_elements()
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        # innerwall

        assert round(therm_zone.ua_value_iw, 16) == 13.443390622904332
        assert round(therm_zone.area_iw, 1) == 34.0
        assert round(therm_zone.r_conv_inner_iw, 18) == 0.010893246187363833
        assert round(therm_zone.r_rad_inner_iw, 19) == 0.0058823529411764705
        assert round(therm_zone.r_comb_inner_iw, 19) == 0.003819709702062643
        assert round(therm_zone.alpha_conv_inner_iw, 1) == 2.7
        assert round(therm_zone.alpha_rad_inner_iw, 1) == 5.0
        assert round(therm_zone.alpha_comb_inner_iw, 1) == 7.7

        # outerwall
        assert round(therm_zone.ua_value_ow, 16) == 19.83577523748189
        assert round(therm_zone.area_ow, 1) == 48.0
        assert round(therm_zone.r_conv_inner_ow, 19) == 0.007716049382716048
        assert round(therm_zone.r_rad_inner_ow, 18) == 0.004166666666666667
        assert round(therm_zone.r_comb_inner_ow, 20) == 0.0027056277056277055
        assert round(therm_zone.r_conv_outer_ow, 20) == 0.0010416666666666667
        assert round(therm_zone.r_rad_outer_ow, 18) == 0.004166666666666667
        assert round(therm_zone.r_comb_outer_ow, 20) == 0.0008333333333333334
        assert round(therm_zone.alpha_conv_inner_ow, 5) == 2.7
        assert round(therm_zone.alpha_rad_inner_ow, 5) == 5.0
        assert round(therm_zone.alpha_comb_inner_ow, 5) == 7.7
        assert round(therm_zone.alpha_conv_outer_ow, 1) == 20.0
        assert round(therm_zone.alpha_rad_outer_ow, 5) == 5.0
        assert round(therm_zone.alpha_comb_outer_ow, 1) == 25.0

        # groundfloor
        assert round(therm_zone.ua_value_gf, 16) == 58.351477449455686
        assert round(therm_zone.area_gf, 1) == 140.0
        assert round(therm_zone.r_conv_inner_gf, 19) == 0.004201680672268907
        assert round(therm_zone.r_rad_inner_gf, 18) == 0.001428571428571429
        assert round(therm_zone.r_comb_inner_gf, 20) == 0.0010660980810234541
        assert round(therm_zone.alpha_conv_inner_gf, 5) == 1.7
        assert round(therm_zone.alpha_rad_inner_gf, 5) == 5.0
        assert round(therm_zone.alpha_comb_inner_gf, 5) == 6.7

        # outerwall
        assert round(therm_zone.ua_value_rt, 16) == 57.394603194028036
        assert round(therm_zone.area_rt, 1) == 140.0
        assert round(therm_zone.r_conv_inner_rt, 19) == 0.004201680672268907
        assert round(therm_zone.r_rad_inner_rt, 18) == 0.001428571428571429
        assert round(therm_zone.r_comb_inner_rt, 20) == 0.0010660980810234541
        assert round(therm_zone.r_conv_outer_rt, 20) == 0.00035714285714285714
        assert round(therm_zone.r_rad_outer_rt, 18) == 0.001428571428571429
        assert round(therm_zone.r_comb_outer_rt, 20) == 0.00028571428571428574
        assert round(therm_zone.alpha_conv_inner_rt, 5) == 1.7
        assert round(therm_zone.alpha_rad_inner_rt, 5) == 5.0
        assert round(therm_zone.alpha_comb_inner_rt, 5) == 6.7
        assert round(therm_zone.alpha_conv_outer_rt, 1) == 20.0
        assert round(therm_zone.alpha_rad_outer_rt, 5) == 5.0
        assert round(therm_zone.alpha_comb_outer_rt, 1) == 25.0

        #window
        assert round(therm_zone.ua_value_win, 16) == 32.87895310796074
        assert round(therm_zone.area_win, 1) == 18.0
        assert round(therm_zone.r_conv_inner_win, 19) == 0.032679738562091505
        assert round(therm_zone.r_rad_inner_win, 4) == 0.0111
        assert round(therm_zone.r_comb_inner_win, 19) == 0.008291873963515755
        assert round(therm_zone.r_conv_outer_win, 5) == 0.00278
        assert round(therm_zone.r_rad_outer_win, 4) == 0.0111
        assert round(therm_zone.r_comb_outer_win, 4) == 0.0022
        assert round(therm_zone.alpha_conv_inner_win, 1) == 1.7
        assert round(therm_zone.alpha_comb_outer_win, 1) == 25.0
        assert round(therm_zone.alpha_conv_outer_win, 1) == 20.0
        assert round(therm_zone.weighted_g_value, 3) == 0.789

    def test_calc_chain_matrix(self):
        '''test of calc_chain_matrix'''
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        omega=(2 * math.pi / 86400 / 5)
        r1_ow, c1_ow = prj.buildings[-1].thermal_zones[-1].calc_chain_matrix(
            element_list=therm_zone.outer_walls,
            omega=omega)
        assert round(r1_ow, 14) == 0.00100751548411
        assert round(c1_ow, 5) == 3648580.59312

        r1_iw, c1_iw = prj.buildings[-1].thermal_zones[-1].calc_chain_matrix(
            element_list=therm_zone.inner_walls,
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

        therm_zone = prj.buildings[-1].thermal_zones[-1]

        assert therm_zone.weightfactor_ow == [0.024530650180761254,
                                              0.03434291025306576,
                                              0.024530650180761254,
                                              0.03434291025306576,
                                              0.3407000330729792]
        assert therm_zone.weightfactor_win == [0.0,
                                               0.054214642472656345,
                                               0.08674342795625017,
                                               0.054214642472656345,
                                               0.0]

        prj.buildings[-1].thermal_zones[-1].weightfactor_ow = []
        prj.buildings[-1].thermal_zones[-1].weightfactor_win = []

        prj.buildings[-1].calc_building_parameter(number_of_elements=2,
                                                  merge_windows=False,
                                                  used_library='AixLib')
        therm_zone = prj.buildings[-1].thermal_zones[-1]

        assert therm_zone.weightfactor_ow == [0.03047939672771178,
                                              0.04267115541879649,
                                              0.03047939672771178,
                                              0.04267115541879649,
                                              0.423320678280269]
        assert therm_zone.weightfactor_win == [0.0,
                                               0.27777777777777778,
                                               0.44444444444444453,
                                               0.27777777777777778,
                                               0.0]

    def test_calc_two_element(self):
        '''test of calc_two_element'''
        prj.set_default()
        helptest.building_test2(prj)

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.calc_zone_parameters(number_of_elements=2,
                                        merge_windows=True)

        assert round(therm_zone.area_ow, 1) == 328.0
        assert round(therm_zone.ua_value_ow, 16) == 135.5818558809656
        assert round(therm_zone.r_conv_inner_ow, 16) == 0.0016512549537649
        assert round(therm_zone.r_rad_inner_ow, 16) == 0.000609756097561
        assert round(therm_zone.r_conv_outer_ow, 9) == 0.001041667
        assert round(therm_zone.alpha_conv_inner_ow, 5) == 1.84634
        assert round(therm_zone.alpha_rad_inner_ow, 1) == 5.0
        assert round(therm_zone.r1_win, 1) == 301.5
        assert round(therm_zone.r1_ow, 15) == 0.000772773294534
        assert round(therm_zone.r1_iw, 15) == 0.009719561140816
        assert round(therm_zone.r_rest_ow, 15) == 0.004740706924836

        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.calc_zone_parameters(number_of_elements=2,
                                        merge_windows=False)

        assert round(therm_zone.area_ow, 1) == 328.0
        assert round(therm_zone.ua_value_ow, 16) == 135.5818558809656
        assert round(therm_zone.r_conv_inner_ow, 16) == 0.0016512549537649
        assert round(therm_zone.r_rad_inner_ow, 16) == 0.000609756097561
        assert round(therm_zone.r_conv_outer_ow, 9) == 0.001041667
        assert round(therm_zone.alpha_conv_inner_ow, 5) == 1.84634
        assert round(therm_zone.alpha_rad_inner_ow, 1) == 5.0
        assert round(therm_zone.r1_win, 15) == 0.02212271973466
        assert round(therm_zone.r1_ow, 15) == 0.001007515484109
        assert round(therm_zone.r1_iw, 15) == 0.009719561140816
        assert round(therm_zone.r_rest_ow, 15) == 0.005922787404456


    def test_volume_zone(self):
        '''test of volume_zone'''

        prj.buildings[-1].thermal_zones[-1].set_volume_zone()
        assert prj.buildings[-1].thermal_zones[-1].volume == 490.0

    def test_set_inner_wall_area(self):
        '''test of set_inner_wall_area'''

        prj.buildings[-1].thermal_zones[-1].set_inner_wall_area()
        for wall in prj.buildings[-1].thermal_zones[-1].inner_walls:
            assert round(wall.area, 16) == 11.951219512195122

   #methods in UseConditions18599()

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

   #methods in BuildingElement

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

    #methods in Wall

    def test_calc_equivalent_res_wall(self):
        '''test of calc_equivalent_res, wall'''
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]

        therm_zone.outer_walls[0].calc_equivalent_res()

        #parameters for outwall

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
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(2016, "EPS035")
        assert round(therm_zone.outer_walls[0].ua_value, 6) == 2.4

    def test_calc_equivalent_res_win(self):
        '''test of calc_equivalent_res, win'''
        prj.set_default()
        helptest.building_test2(prj)
        therm_zone = prj.buildings[-1].thermal_zones[-1]
        therm_zone.windows[0].calc_equivalent_res()

        assert round(therm_zone.windows[0].r1, 3) == 0.072
