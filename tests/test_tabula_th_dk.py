from teaser.project import Project
prj = Project(False)


class Test_tabula_th_dk(object):
    global prj

    def test_tabula_de_th_dk_area_1849(self):
        """
        Test for area estimation of tabula th
        """
        prj.set_default()
        prj.data = None

        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1849,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=93)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 88
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 33
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 66
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 9.8
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_dk_area_1929(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1929,
            number_of_floors=3,
            height_of_floors=3.2,
            net_leased_area=117)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 65.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 59
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 48.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 15.2
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_dk_area_1949(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1949,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=95)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 75
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 30
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 62
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 13.2
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_dk_area_1959(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1959,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=87)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 90
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 38
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 58
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 16.7
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_dk_area_1971(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1971,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=86)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 73
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 37
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 50
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 37.3
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_dk_area_1977(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=111)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 95
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 22
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 65
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 16.9
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0
    #
    def test_tabula_de_th_dk_area_1997(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1997,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=85)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 53
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 30
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 43
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 12.9
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0
    #
    def test_tabula_de_th_dk_area_2005(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2005,
            number_of_floors=3,
            height_of_floors=3.2,
            net_leased_area=101)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 53
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 38
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 34
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 19.7
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.5

    def test_tabula_de_th_dk_area_2009(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2009,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=111)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 130
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 60
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 118
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 30.4
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#test for U-value

    def test_tabula_uvalue_standard_th_dk_1849(self):

        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1849,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=93)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.6 - 0.17)), 1)



        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_data:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 1.6 - 0.17)), 1)
            if "_2_" in wall.construction_data:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.6 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
        #     1) == round((1 / (1 / 1.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.34 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_dk_1929(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1929,
            number_of_floors=3,
            height_of_floors=3.2,
            net_leased_area=117)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 1.5 - 0.14)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.5 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 1.5 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.7 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_dk_1949(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1949,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=95)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.2 - 0.14)), 1)


        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.94 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.7 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_dk_1959(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1959,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=87)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.38 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.67 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.51 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.7 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_dk_1971(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1971,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=86)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.67 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.6 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_dk_1977(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=111)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.6 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.47 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_standard_th_dk_1997(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1997,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=85)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.2 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.18 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_dk_2005(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2005,
            number_of_floors=3,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.2 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.3 - 0.17)), 1)

            # if "_1_" in wall.construction_data:
            #     assert round(1 / (wall.r_conduc * wall.area),
            #                  1) == round((1 / (1 / 0.6 - 0.17)), 1)
            #
            # if "_2_" in wall.construction_data:
            #     assert round(1 / (wall.r_conduc * wall.area),
            #                  1) == round((1 / (1 / 0.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.14 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.5 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_dk_2009(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2009,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=111)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.24 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.14 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.5 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#--------------------------------------------------------------------------------------------------------------------------------------------S
#test for U-value retrofit

    def test_tabula_uvalue_retrofit_th_dk_1849(self):

        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1849,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=93)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.17)), 1)



        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_data:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.4 - 0.17)), 1)
            if "_2_" in wall.construction_data:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.6 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
        #     1) == round((1 / (1 / 1.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.12 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_th_dk_1929(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1929,
            number_of_floors=3,
            height_of_floors=3.2,
            net_leased_area=117)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.11 - 0.14)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.24 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.26 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_th_dk_1949(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1949,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=95)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.13 - 0.14)), 1)


        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.4 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.24 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_th_dk_1959(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1959,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=87)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.2 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.28 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_th_dk_1971(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1971,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=86)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.13 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.2 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.31 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_th_dk_1977(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=111)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.12 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_retrofit_th_dk_1997(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1997,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=85)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.13 - 0.21)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
        #     1) == round((1 / (1 / 0.3 - 0.17)), 1)
        #
        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
        #     1) == round((1 / (1 / 0.18 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_th_dk_2005(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2005,
            number_of_floors=3,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.13 - 0.21)), 1)

#-----------------------------------------------------------------------------------------------------------------------------------

#test for U-value adv retrofit

    def test_tabula_uvalue_adv_retrofit_th_dk_1849(self):

        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1849,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=93)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.17)), 1)



        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_data:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.12 - 0.17)), 1)
            if "_2_" in wall.construction_data:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.6 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
        #     1) == round((1 / (1 / 1.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.12 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_adv_retrofit_th_dk_1929(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1929,
            number_of_floors=3,
            height_of_floors=3.2,
            net_leased_area=117)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.08 - 0.14)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.14 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.14 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_adv_retrofit_th_dk_1949(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1949,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=95)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.14)), 1)


        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.12 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.14 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_adv_retrofit_th_dk_1959(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1959,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=87)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.13 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.15 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_adv_retrofit_th_dk_1971(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1971,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=86)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.1 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.13 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.16 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_adv_retrofit_th_dk_1977(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=111)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.12 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_adv_retrofit_th_dk_1997(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1997,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=85)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.21)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
        #     1) == round((1 / (1 / 0.3 - 0.17)), 1)
        #
        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
        #     1) == round((1 / (1 / 0.18 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_adv_retrofit_th_dk_2005(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2005,
            number_of_floors=3,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)
