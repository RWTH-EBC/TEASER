from teaser.project import Project
prj = Project(False)


class Test_tabula_ab(object):
    global prj

    def test_tabula_de_ab_dk_area_1849(self):
        """
        Test for area estimation of tabula th
        """
        prj.set_default()
        prj.data = None

        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1849,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=371)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 221.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == (167+246.9)
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == (175.2+25.9)
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 57.7
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_ab_dk_area_1929(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1929,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=480)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 303
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 399
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 194
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 94.1
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0
    #
    def test_tabula_de_ab_dk_area_1949(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1949,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=2342)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 556
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 1516
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 556
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 428.6
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0
    #
    def test_tabula_de_ab_dk_area_1959(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1959,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=312)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 163
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 276
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 147
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 56.9
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0
    #
    def test_tabula_de_ab_dk_area_1971(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1971,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=1360)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 535
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == (252+483)
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 535
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 345
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0
    #
    def test_tabula_de_ab_dk_area_1977(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=1955)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 470
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == (147+437)
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == (386+84)
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 754.4
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0
    # #
    def test_tabula_de_ab_dk_area_1997(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1997,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=2496)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 782
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 1120
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 754
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 427.8
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0
    # #
    def test_tabula_de_ab_dk_area_2005(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=2005,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=2486)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 609
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 792
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 595
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 513
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.5
    #
    def test_tabula_de_ab_dk_area_2009(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=2009,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=656)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 156
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 369
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 162
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 208.2
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#test for U-value

    def test_tabula_uvalue_standard_ab_dk_1849(self):

        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1849,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=371)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.2 - 0.14)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_data:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 2.8 - 0.17)), 1)

            if "_2_" in wall.construction_data:

                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 2.1 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_data:
                assert round(
                    1 / (floor.r_conduc * floor.area),
                    1) == round((1 / (1 / 1.03 - 0.34)), 1)

            if "_2_" in floor.construction_data:

                assert round(
                    1 / (floor.r_conduc * floor.area),
                    1) == round((1 / (1 / 0.2 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.7 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_ab_dk_1929(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1929,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=480)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.38 - 0.14)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.62 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.52 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.7 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_standard_ab_dk_1949(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1949,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=2342)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 1.9 - 0.14)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.2 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 1.21 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_standard_ab_dk_1959(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1959,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=312)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.6 - 0.14)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.77 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_standard_ab_dk_1971(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1971,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=1360)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.33 - 0.14)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.6 - 0.17)), 1)

            if "_2_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.46 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.99 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.7 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_standard_ab_dk_1977(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=1955)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.19 - 0.14)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.49 - 0.17)), 1)

            if "_2_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.6 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_data:
                assert round(
                    1 / (floor.r_conduc * floor.area),
                    1) == round((1 / (1 / 0.46 - 0.34)), 1)

            if "_2_" in floor.construction_data:

                assert round(
                    1 / (floor.r_conduc * floor.area),
                    1) == round((1 / (1 / 0.19 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    # #
    def test_tabula_uvalue_standard_ab_dk_1997(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1997,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=2496)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.19 - 0.14)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.34 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.19 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.7 - 0.17)), 1)
    #
    #     # assert round(
    #     #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
    #     #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
    #     #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_standard_ab_dk_2005(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=2005,
            number_of_floors=3,
            height_of_floors=3.2,
            net_leased_area=2486)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.19 - 0.14)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.22 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)
    #
    #     # assert round(
    #     #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
    #     #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
    #     #     1) == round((1 / (1 / 2.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_standard_ab_dk_2009(self):
        prj.add_residential(
            construction_data='tabula_dk_standard',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=2009,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=656)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.19 - 0.14)), 1)

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
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#--------------------------------------------------------------------------------------------------------------------------------

#test for U-value retrofit

    def test_tabula_uvalue_retrofit_ab_dk_1849(self):

        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1849,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=371)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.13 - 0.14)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_data:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.57 - 0.17)), 1)

            if "_2_" in wall.construction_data:

                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 2.1 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_data:
                assert round(
                    1 / (floor.r_conduc * floor.area),
                    1) == round((1 / (1 / 0.24 - 0.34)), 1)

            if "_2_" in floor.construction_data:

                assert round(
                    1 / (floor.r_conduc * floor.area),
                    1) == round((1 / (1 / 0.2 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_ab_dk_1929(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1929,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=480)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.14)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.33 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.29 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_retrofit_ab_dk_1949(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1949,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=2342)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.11 - 0.14)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.23 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.25 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_retrofit_ab_dk_1959(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1959,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=312)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.14)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.4 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.23 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_retrofit_ab_dk_1971(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1971,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=1360)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.14)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_data:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.1 - 0.17)), 1)

            if "_2_" in wall.construction_data:

                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.46 - 0.17)), 1)

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
    #
    def test_tabula_uvalue_retrofit_ab_dk_1977(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=1955)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.14)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_data:
                assert round(
                    1 / (floor.r_conduc * floor.area),
                    1) == round((1 / (1 / 0.27 - 0.34)), 1)

            if "_2_" in floor.construction_data:

                assert round(
                    1 / (floor.r_conduc * floor.area),
                    1) == round((1 / (1 / 0.19 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

            # assert round(
            #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
            #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    # #
    def test_tabula_uvalue_retrofit_ab_dk_1997(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1997,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=2496)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.14)), 1)


        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)
    #
    #     # assert round(
    #     #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
    #     #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
    #     #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_retrofit_ab_dk_2005(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=2005,
            number_of_floors=3,
            height_of_floors=3.2,
            net_leased_area=2486)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.14)), 1)

    #
    #     # assert round(
    #     #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
    #     #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
    #     #     1) == round((1 / (1 / 2.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_retrofit_ab_dk_2009(self):
        prj.add_residential(
            construction_data='tabula_dk_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=2009,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=656)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.14)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#-------------------------------------------------------------------------------------------------------------------------------

#test for U-value adv retrofit

    def test_tabula_uvalue_adv_retrofit_ab_dk_1849(self):

        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1849,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=371)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.14)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_data:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.32 - 0.17)), 1)

            if "_2_" in wall.construction_data:

                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 2.1 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_data:
                assert round(
                    1 / (floor.r_conduc * floor.area),
                    1) == round((1 / (1 / 0.14 - 0.34)), 1)

            if "_2_" in floor.construction_data:

                assert round(
                    1 / (floor.r_conduc * floor.area),
                    1) == round((1 / (1 / 0.2 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_adv_retrofit_ab_dk_1929(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1929,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=480)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.14)), 1)

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
    #
    def test_tabula_uvalue_adv_retrofit_ab_dk_1949(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1949,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=2342)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.14)), 1)

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
    #
    def test_tabula_uvalue_adv_retrofit_ab_dk_1959(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1959,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=312)

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
            1) == round((1 / (1 / 0.13 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_adv_retrofit_ab_dk_1971(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1971,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=1360)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.14)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_data:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.08 - 0.17)), 1)

            if "_2_" in wall.construction_data:

                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.46 - 0.17)), 1)

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
    #
    def test_tabula_uvalue_adv_retrofit_ab_dk_1977(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=1955)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.14)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_data:
                assert round(
                    1 / (floor.r_conduc * floor.area),
                    1) == round((1 / (1 / 0.15 - 0.34)), 1)

            if "_2_" in floor.construction_data:

                assert round(
                    1 / (floor.r_conduc * floor.area),
                    1) == round((1 / (1 / 0.19 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

            # assert round(
            #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
            #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_adv_retrofit_ab_dk_1997(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1997,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=2496)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.14)), 1)


        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)
    #
    #     # assert round(
    #     #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
    #     #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
    #     #     1) == round((1 / (1 / 3.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_adv_retrofit_ab_dk_2005(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=2005,
            number_of_floors=3,
            height_of_floors=3.2,
            net_leased_area=2486)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.14)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

    #
    #     # assert round(
    #     #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
    #     #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
    #     #     1) == round((1 / (1 / 2.0 - 0.17)), 1)
    #
    def test_tabula_uvalue_adv_retrofit_ab_dk_2009(self):
        prj.add_residential(
            construction_data='tabula_dk_adv_retrofit',
            geometry_data='tabula_dk_apartment_block',
            name="ResidentialBuilding",
            year_of_construction=2009,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=656)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.14)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)
