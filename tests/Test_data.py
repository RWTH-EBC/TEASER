'''
Created July 2015

@author: TEASER 4 Development Team
'''

from teaser.Project import Project
from teaser.Logic import Utilis
# import xml.etree.ElementTree as et

import HelpTest
prj = Project(True)


class Test_teaser(object):
    """Unit Tests for TEASER"""
    global prj

    def test_calc_vdi_room1(self):
        """Parameter Verification for rouvel room1"""
        import teaser.Examples.Verification.ParameterVerification_1 as room1

        room1_prj = room1.parameter_room1()
        therm_zone = room1_prj.list_of_buildings[0].thermal_zones[0]

        #parameters inner wall Typraum S

        assert round(therm_zone.r1_iw, 13) == 0.0005956934075
        assert round(therm_zone.c1_iw / 1000, 7) == 14836.3546282
        assert round(therm_zone.area_iw, 1) == 75.5
        assert round(therm_zone.alpha_conv_iw, 13) == 2.23642384105960

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
        import teaser.Examples.Verification.ParameterVerification_3 as room3

        room3_prj = room3.parameter_room3()
        therm_zone = room3_prj.list_of_buildings[0].thermal_zones[0]

        #parameters inner wall Typraum L

        assert round(therm_zone.r1_iw, 13) == 0.003385649748
        assert round(therm_zone.c1_iw / 1000, 7) == 7445.3648976
        assert round(therm_zone.area_iw, 1) == 75.5
        assert round(therm_zone.alpha_conv_iw, 13) == 2.23642384105960

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
        import teaser.Examples.Verification.ParameterVerification_8 as room8

        room8_prj = room8.parameter_room8()
        therm_zone = room8_prj.list_of_buildings[0].thermal_zones[0]

        assert round(therm_zone.r1_iw, 13) == 0.0006688956391
        assert round(therm_zone.c1_iw / 1000, 7) == 12391.3638631
        assert round(therm_zone.area_iw, 1) == 60.5
        assert round(therm_zone.alpha_conv_iw, 13) == 2.1214876033058

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
        prj.load_project(Utilis.get_full_path("Examples\\ExampleInputFiles"
                                              "\\new.teaserXML"))
        therm_zone = prj.list_of_buildings[0].thermal_zones[0]

        prj.list_of_buildings[0].calc_building_parameter('ebc')

        assert round(therm_zone.r1_iw, 11) == 4.62113e-06
        assert round(therm_zone.c1_iw, 2) == 1209810287.22
        assert round(therm_zone.area_iw, 5) == 9866.66667
        assert round(therm_zone.alpha_conv_iw, 5) == 2.37568

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
        from teaser.Logic.BuildingObjects.TypeBuildings.Office import Office

        prj.set_default()
        test_office = Office(parent=prj,
                             name="TestBuilding",
                             year_of_construction=1988,
                             number_of_floors=3,
                             height_of_floors=3,
                             net_leased_area=2500)

        test_office.generate_office()

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

        test_office.generate_office()

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

        test_office.generate_office()

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

        test_office.generate_office()

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
        from teaser.Logic.BuildingObjects.TypeBuildings.Institute4 import \
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

        test_institute4.generate_office()

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
        from teaser.Logic.BuildingObjects.TypeBuildings.Institute8 import \
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

        test_institute8.generate_office()

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
        from teaser.Logic.BuildingObjects.TypeBuildings.Institute import \
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

        test_institute.generate_office()

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
        from teaser.Logic.BuildingObjects.TypeBuildings.Residential import \
            Residential

        prj.set_default()
        test_residential = Residential(parent=prj,
                                       name="TestBuilding",
                                       year_of_construction=1988,
                                       number_of_floors=3,
                                       height_of_floors=3,
                                       net_leased_area=2500)

        test_residential.generate_residential()

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
        test_residential = Residential(parent=prj,
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

        test_residential.generate_residential()

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
        test_residential = Residential(parent=prj,
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

        test_residential.generate_residential()

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
        test_residential = Residential(parent=prj,
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

        test_residential.generate_residential()

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

        prj.load_project(Utilis.get_full_path(("Examples/ExampleInputFiles"
                                               "/new.teaserXML")))
        therm_zone = prj.list_of_buildings[-1].thermal_zones[0]
        assert therm_zone.outer_walls[0].area == 40.0
        tz_area = sum([tz.area for tz in prj.list_of_buildings[
            -1].thermal_zones])
        assert prj.list_of_buildings[-1].net_leased_area == tz_area
        prj.save_project("unitTest")
        prj.set_default()

    def test_load_old_teaser(self):
        '''test of load_old_teaser'''

        prj.load_old_teaser(Utilis.get_full_path(("Examples/ExampleInputFiles"
                                               "/Teaser3/SixZoneOffice.xml")))
        tz_area = sum([tz.area for tz in prj.list_of_buildings[
            -1].thermal_zones])
        assert prj.list_of_buildings[-1].net_leased_area == tz_area
        prj.set_default()

    #commented until we find solution for opengis PyXB bindings
    def test_save_citygml(self):
        '''test of save_gml'''
        HelpTest.building_test2(prj)
        prj.save_citygml("unitTest")
        prj.set_default()

    def test_calc_all_buildings(self):
        '''test of calc_all_buildings, no calculation verification'''

        HelpTest.building_test2(prj)
        HelpTest.building_test2(prj)
        prj.calc_all_buildings('vdi')
        prj.calc_all_buildings('ebc')

    def test_retrofit_all_buildings(self):
        '''test of retrofit_all_buildings, no calculation verification'''

        prj.retrofit_all_buildings(2015)

    def test_export_record(self):
        '''test of export_record, no calculation verification'''

        prj.calc_all_buildings('vdi')
        prj.export_record('AixLib')
        prj.export_record('CitiesType_old')
        prj.calc_all_buildings('ebc')
        prj.export_record('CitiesRWin')

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
        HelpTest.building_test2(prj)
        sum_area = prj.list_of_buildings[-1].get_inner_wall_area()
        assert round(sum_area, 1) == 10.0

    def test_set_outer_wall_area(self):
        '''test of set_outer_wall_area'''

        prj.list_of_buildings[-1].set_outer_wall_area(2.0, 0.0)
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        assert round(therm_zone.outer_walls[0].area, 3) == 0.01
        assert round(therm_zone.outer_walls[1].area, 3) == 0.01

    def test_get_outer_wall_area(self):
        '''test of get_outer_wall_area'''
        prj.list_of_buildings[-1].get_outer_wall_area(0.0)
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        assert round(therm_zone.outer_walls[0].area, 3) == 0.01
        assert round(therm_zone.outer_walls[1].area, 3) == 0.01

    def test_set_window_area(self):
        '''test of set_window_area'''
        prj.list_of_buildings[-1].set_window_area(1.0, 0.0)
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        assert round(therm_zone.windows[0].area, 3) == 0.005

    def test_get_window_area(self):
        '''test of get_window_area'''
        prj.list_of_buildings[-1].get_window_area(0.0)
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        assert round(therm_zone.windows[0].area, 3) == 0.005

    def test_set_specific_wall_area(self):
        '''test of set_specific_wall_area'''
        prj.set_default()
        HelpTest.building_test2(prj)
        prj.list_of_buildings[-1].set_specific_wall_area(
            prj.list_of_buildings[-1].thermal_zones[-1],
            prj.list_of_buildings[-1].thermal_zones[-1].outer_walls[1],
            500)

        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        assert round(therm_zone.outer_walls[0].area, 2) == 0.05
        assert round(therm_zone.outer_walls[1].area, 1) == 500

    def test_fill_outer_wall_area_dict(self):
        '''test of fill_outer_wall_area_dict'''

        prj.list_of_buildings[-1].fill_outer_area_dict()
        outwall_dict_round = {key: round(value, 2) for key, value in
                              prj.list_of_buildings[-1].outer_area.items()}
        assert outwall_dict_round == {0.0: 500.05}

    def test_fill_window_area_dict(self):
        '''test of fill_window_area_dict'''
        prj.list_of_buildings[-1].fill_window_area_dict()
        assert prj.list_of_buildings[-1].window_area == {0.0: 10.0}

    def test_calc_building_parameter(self):
        '''test of calc_building_parameter'''
        prj.set_default()
        HelpTest.building_test2(prj)

        prj.list_of_buildings[-1].calc_building_parameter('vdi')

        assert round(prj.list_of_buildings[-1].volume, 1) == 55.0
        assert round(
            prj.list_of_buildings[-1].sum_heating_load,
            12) == 1058.375695317738

    #methods in therm_zone

    def test_calc_zone_parameters(self):
        '''test of calc zone parameter, no calculation verification'''

        prj.list_of_buildings[-1].thermal_zones[-1].calc_zone_parameters('vdi')
        prj.list_of_buildings[-1].thermal_zones[-1].calc_zone_parameters('ebc')

    def test_heating_load(self):
        '''test of heating_load'''
        prj.list_of_buildings[-1].thermal_zones[-1].calc_heat_load()
        assert round(
            prj.list_of_buildings[-1].thermal_zones[-1].heating_load,
            1) == 1058.4

    def test_combine_building_elements(self):
        '''test of combine_building_elements'''
        prj.set_default()
        HelpTest.building_test2(prj)

        #execute zone parameters for therm_zone

        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        for out_wall in therm_zone.outer_walls:
            out_wall.calc_equivalent_res()
            out_wall.calc_ua_value()

        for in_wall in therm_zone.inner_walls:
            in_wall.calc_equivalent_res()
            in_wall.calc_ua_value()

        for win in therm_zone.windows:
            win.calc_equivalent_res()
            win.calc_ua_value()

        prj.list_of_buildings[-1].thermal_zones[-1].combine_building_elements()
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        # innerwall
        assert round(therm_zone.ua_value_iw, 16) == 5.747316267547481
        assert round(therm_zone.area_iw, 1) == 10.0
        assert round(therm_zone.r_conv_iw, 18) == 0.02702702702702703
        assert round(therm_zone.r_rad_iw, 19) == 0.020000000000000004
        assert round(therm_zone.r_comb_iw, 19) == 0.011494252873563218
        assert round(therm_zone.alpha_conv_iw, 17) == 3.6999999999999997
        assert round(therm_zone.alpha_rad_iw, 16) == 4.999999999999999
        assert round(therm_zone.alpha_comb_iw, 1) == 8.7

        # outerwall
        assert round(therm_zone.ua_value_ow, 16) == 10.437611940738702
        assert round(therm_zone.area_ow, 1) == 22.0
        assert round(therm_zone.r_conv_inner_ow, 19) == 0.016835016835016835
        assert round(therm_zone.r_rad_inner_ow, 18) == 0.00909090909090909
        assert round(therm_zone.r_comb_inner_ow, 20) == 0.0059031877213695395
        assert round(therm_zone.r_conv_outer_ow, 20) == 0.0022727272727272726
        assert round(therm_zone.r_rad_outer_ow, 18) == 0.00909090909090909
        assert round(therm_zone.r_comb_outer_ow, 20) == 0.0018181818181818182
        assert round(therm_zone.alpha_conv_inner_ow, 1) == 2.7
        assert round(therm_zone.alpha_conv_outer_ow, 1) == 20.0
        assert round(therm_zone.alpha_comb_outer_ow, 1) == 25.0
        assert round(therm_zone.r_comb_outer_ow, 20) == 0.0018181818181818182

        assert round(therm_zone.ua_value_win, 16) == 6.980378537940616
        assert round(therm_zone.area_win, 1) == 10.0
        assert round(therm_zone.r_conv_inner_win, 19) == 0.058823529411764705
        assert round(therm_zone.r_rad_inner_win, 19) == 0.020000000000000004
        assert round(therm_zone.r_comb_inner_win, 19) == 0.014925373134328358
        assert round(therm_zone.r_conv_outer_win, 3) == 0.004
        assert round(therm_zone.r_rad_outer_win, 19) == 0.020000000000000004
        assert round(therm_zone.r_comb_outer_win, 19) == 0.0033333333333333335
        assert round(therm_zone.alpha_conv_inner_win, 1) == 1.7
        assert round(therm_zone.alpha_comb_outer_win, 1) == 30.0
        assert round(therm_zone.alpha_conv_outer_win, 1) == 25.0
        assert round(therm_zone.weighted_g_value, 1) == 0

    def test_parallel_connection(self):
        '''test of test_parallel_connection'''

        prj.list_of_buildings[-1].thermal_zones[-1].parallel_connection("vdi")
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]

        assert round(therm_zone.r1_ow, 14) == 0.00738585853265
        assert round(therm_zone.c1_ow, 5) == 217636.98018
        assert round(therm_zone.r1_iw, 13) == 0.0198372019253
        assert round(therm_zone.c1_iw, 7) == 68489.5680589
        assert round(therm_zone.r1_win, 1) == 48.0
        assert round(therm_zone.r1_ow, 14) == 0.00738585853265
        assert round(therm_zone.r_total, 17) == 0.05741190415875247
        assert round(therm_zone.r_rad_ow_iw, 5) == 0.00625
        assert round(therm_zone.r_rest_ow, 13) == 0.0457959271828

        prj.list_of_buildings[-1].thermal_zones[-1].parallel_connection("ebc")
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]

        assert round(therm_zone.r1_ow, 13) == 0.0114424496081
        assert round(therm_zone.c1_ow, 5) == 217636.98018
        assert round(therm_zone.r1_iw, 13) == 0.0198372019253
        assert round(therm_zone.c1_iw, 7) == 68489.5680589
        assert round(therm_zone.r1_win, 12) == 0.128333333333
        assert round(therm_zone.r1_ow, 13) == 0.0114424496081
        assert round(therm_zone.r_total, 18) == 0.09580735571294165
        assert round(therm_zone.r_rad_ow_iw, 19) == 0.00909090909090909
        assert round(therm_zone.r_rest_ow, 13) == 0.0784617183834

    def test_calc_weightfactor(self):
        '''test of calc_weightfactor'''
        prj.list_of_buildings[-1].thermal_zones[-1].calc_weightfactors('vdi')
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        assert therm_zone.weightfactor_ow == [0.5992431763879407]
        assert therm_zone.weightfactor_win == [0.4007568236120593]

        prj.list_of_buildings[-1].thermal_zones[-1].weightfactor_ow = []
        prj.list_of_buildings[-1].thermal_zones[-1].weightfactor_win = []

        prj.list_of_buildings[-1].thermal_zones[-1].calc_weightfactors('ebc')
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        assert therm_zone.weightfactor_ow == [1.0]
        assert therm_zone.weightfactor_win == [1.0]

    def test_volume_zone(self):
        '''test of volume_zone'''

        prj.list_of_buildings[-1].thermal_zones[-1].set_volume_zone()
        assert prj.list_of_buildings[-1].thermal_zones[-1].volume == 10.0

    def test_set_inner_wall_area(self):
        '''test of set_inner_wall_area'''

        prj.list_of_buildings[-1].thermal_zones[-1].set_inner_wall_area()
        for wall in prj.list_of_buildings[-1].thermal_zones[-1].inner_walls:
            assert round(wall.area, 16) == 0.2439024390243902

   #methods in UseConditions18599()

    def test_load_use_conditions(self):
        '''test of load_use_conditions, no parameter checking'''
        use_cond = prj.list_of_buildings[-1].thermal_zones[-1].use_conditions
        use_cond.load_use_conditions("Living")

    def test_save_use_conditions(self):
        '''test of save_use_conditions, no parameter checking'''
        path = Utilis.get_default_path()
        use_cond = prj.list_of_buildings[-1].thermal_zones[-1].use_conditions
        use_cond.parent = None
        use_cond.save_use_conditions(path=path, file_name="UseCondUT")

   #methods in BuildingElement

    def test_ua_value(self):
        '''test of ua_value'''
        prj.set_default()
        HelpTest.building_test2(prj)

        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].calc_ua_value()

        assert round(
            therm_zone.outer_walls[0].ua_value,
            15) == 4.132453174475393

    def test_gather_element_properties(self):
        '''test of gather_element_properties'''
        outerWalls = prj.list_of_buildings[-1].thermal_zones[-1].outer_walls[0]
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
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].load_type_element(1988, "heavy")
        therm_zone.inner_walls[0].load_type_element(1988, "light")
        therm_zone.windows[0].load_type_element(1988, "heavy")

    def test_save_type_element(self):
        '''test of load_type_element, no parameter checking'''

        # test load function
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        path = Utilis.get_default_path()
        therm_zone.outer_walls[0].parent = None
        therm_zone.outer_walls[0].save_type_element(path=path,
                                                    file_name="unitTestTB")
        therm_zone.inner_walls[0].parent = None
        therm_zone.inner_walls[0].save_type_element(path=path,
                                                    file_name="unitTestTB")
        therm_zone.windows[0].parent = None
        therm_zone.windows[0].save_type_element(path=path,
                                                file_name="unitTestTB")

    #methods in Wall

    def test_calc_equivalent_res_wall(self):
        '''test of calc_equivalent_res, wall'''
        prj.set_default()
        HelpTest.building_test2(prj)
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]

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
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].insulate_wall("EPS035", 0.04)
        assert round(therm_zone.outer_walls[0].ua_value, 6) == 2.806838

    def test_retrofit_wall(self):
        '''test of retrofit_wall'''
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        therm_zone.outer_walls[0].retrofit_wall(2016, "EPS035")
        assert round(therm_zone.outer_walls[0].ua_value, 6) == 2.4

    def test_calc_equivalent_res_win(self):
        '''test of calc_equivalent_res, win'''
        prj.set_default()
        HelpTest.building_test2(prj)
        therm_zone = prj.list_of_buildings[-1].thermal_zones[-1]
        therm_zone.windows[0].calc_equivalent_res()

        assert round(therm_zone.windows[0].r1, 3) == 0.125
