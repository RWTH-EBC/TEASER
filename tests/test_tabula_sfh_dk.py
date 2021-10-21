from teaser.project import Project
prj = Project(False)


class Test_tabula_sfh_dk(object):
    global prj



    def test_tabula_de_sfh_dk_area_2009(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=145)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 171
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 150
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 149
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 24.7
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

#----------------------------------------------------------------------------------

    def test_tabula_de_sfh_dk_area_2005(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2005,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=149)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 120
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 117
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 90
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 27.4
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

#----------------------------------------------------------------------------------

    def test_tabula_de_sfh_dk_area_1997(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1997,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=122)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 143
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 124
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 122
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 24.7
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

#----------------------------------------------------------------------------------

    def test_tabula_de_sfh_dk_area_1977(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=117)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 131
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 97
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 118
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 22.3
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

#----------------------------------------------------------------------------------

    def test_tabula_de_sfh_dk_area_1971(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1971,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=153)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 180
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 121
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 160
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 33.7
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

#----------------------------------------------------------------------------------

    def test_tabula_de_sfh_dk_area_1959(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1959,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=90)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 106
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 101
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 106
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 28.2
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

#----------------------------------------------------------------------------------

    def test_tabula_de_sfh_dk_area_1949(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1949,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=119)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 89
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 109
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 88
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 21.7
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

#----------------------------------------------------------------------------------

    def test_tabula_de_sfh_dk_area_1929(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1929,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=95)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 94
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 98
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 66
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 15.1
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

#----------------------------------------------------------------------------------

    def test_tabula_de_sfh_dk_area_1849(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1849,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=132)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 155
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 146
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 127
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 27
        # assert round(
        #     sum(wall.area for wall in
        #         prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0


#------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------------------------
#test for U-value

    def test_tabula_uvalue_standard_sfh_dk_2009(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=145)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.11 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.16 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.12 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.5 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_standard_sfh_dk_2005(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2005,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=149)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.11 - 0.21)), 1)

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
            1) == round((1 / (1 / 1.9 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_standard_sfh_dk_1997(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1997,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=122)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.11 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.48 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.33 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.5 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_standard_sfh_dk_1977(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=117)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.3 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_type:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.3 - 0.17)), 1)
            if "_2_" in wall.construction_type:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.2 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.7 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_standard_sfh_dk_1971(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1971,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=153)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.3 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.44 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_standard_sfh_dk_1959(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1959,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=90)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.38 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.52 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_standard_sfh_dk_1949(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1949,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=119)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 1.5 - 0.14)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_type:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 1.6 - 0.17)), 1)
            if "_2_" in wall.construction_type:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.67 - 0.17)), 1)

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
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_standard_sfh_dk_1929(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1929,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=95)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.6 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 1.5 - 0.34)), 1)
# U-value of website is 1.03, but is seems to be wrong

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.7 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_standard_sfh_dk_1849(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1849,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=132)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.6 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.62 - 0.17)), 1)
        # U-value of website is 0.33, but is seems to be wrong

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 1 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#test for U-value for retrofit


    def test_tabula_uvalue_retrofit_sfh_dk_1997(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1997,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=122, construction_type="tabula_retrofit")

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
        #     1) == round((1 / (1 / 0.11 - 0.21)), 1)
        #
        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
        #     1) == round((1 / (1 / 0.48 - 0.17)), 1)
        #
        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
        #     1) == round((1 / (1 / 0.33 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_retrofit_sfh_dk_1977(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=117, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.13 - 0.21)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
        #     1) == round((1 / (1 / 0.3 - 0.17)), 1)

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
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_retrofit_sfh_dk_1971(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1971,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=153, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.13 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.19 - 0.17)), 1)

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
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_retrofit_sfh_dk_1959(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1959,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=90, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.35 - 0.17)), 1)

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
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_retrofit_sfh_dk_1949(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1949,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=119, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.14)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_type:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.4 - 0.17)), 1)
            if "_2_" in wall.construction_type:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.67 - 0.17)), 1)

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
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_retrofit_sfh_dk_1929(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1929,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=95, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.4 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.24 - 0.34)), 1)
# U-value of website is 1.03, but is seems to be wrong

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_retrofit_sfh_dk_1849(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1849,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=132, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.12 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.2 - 0.17)), 1)
        # U-value of website is 0.33, but is seems to be wrong

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
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------------------------------------------------------------------------------
#U-value adv retrofit

    def test_tabula_uvalue_adv_retrofit_sfh_dk_1997(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1997,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=122, construction_type="tabula_adv_retrofit")

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
        #     1) == round((1 / (1 / 0.11 - 0.21)), 1)
        #
        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.21 - 0.17)), 1)
        #
        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
        #     1) == round((1 / (1 / 0.33 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_adv_retrofit_sfh_dk_1977(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=117, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.1 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_type:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.1 - 0.17)), 1)
            if "_2_" in wall.construction_type:
                assert round(
                    1 / (wall.r_conduc * wall.area),
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
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_adv_retrofit_sfh_dk_1971(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1971,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=153, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.1 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.13 - 0.17)), 1)

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
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_adv_retrofit_sfh_dk_1959(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1959,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=90, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.35 - 0.17)), 1)

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
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_adv_retrofit_sfh_dk_1949(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1949,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=119, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.14)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:
            if "_1_" in wall.construction_type:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.12 - 0.17)), 1)
            if "_2_" in wall.construction_type:
                assert round(
                    1 / (wall.r_conduc * wall.area),
                    1) == round((1 / (1 / 0.67 - 0.17)), 1)

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
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_adv_retrofit_sfh_dk_1929(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1929,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=95, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.12 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.14 - 0.34)), 1)
# U-value of website is 1.03, but is seems to be wrong

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.9 - 0.17)), 1)

        # assert round(
        #     1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
        #          * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)

#----------------------------------------------------------------------------------

    def test_tabula_uvalue_adv_retrofit_sfh_dk_1849(self):
        prj.add_residential(
            method='tabula_dk',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1849,
            number_of_floors=1,
            height_of_floors=3.2,
            net_leased_area=132, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.13 - 0.17)), 1)
        # U-value of website is 0.33, but is seems to be wrong

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
        #     1) == round((1 / (1 / 2.0 - 0.17)), 1)


#----------------------------------------------------------------------------------

    # def test_tabula_uvalue_retrofit_adv_sfh_dk_2009(self):
    #     prj.add_residential(
    #         method='tabula_de',
    #         usage='single_family_house',
    #         name="ResidentialBuilding",
    #         year_of_construction=2008,
    #         number_of_floors=2,
    #         height_of_floors=3.2,
    #         net_leased_area=219, construction_type="tabula_adv_retrofit")
    #
    #     assert round(
    #         1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
    #              * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
    #         1) == round((1 / (1 / 0.14 - 0.21)), 1)
    #
    #     assert round(
    #         1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
    #              * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
    #         1) == round((1 / (1 / 0.14 - 0.17)), 1)
    #
    #     assert round(
    #         1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
    #              * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
    #         1) == round((1 / (1 / 0.17 - 0.34)), 1)
    #
    #     assert round(
    #         1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
    #              * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
    #         1) == round((1 / (1 / 0.8 - 0.17)), 1)
    #
    #     assert round(
    #         1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
    #              * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
    #         1) == round((1 / (1 / 0.8 - 0.17)), 1)


    # def test_tabula_retrofit(self):
    #     """
    #     Test for retrofit of tabula
    #     """
    #     prj.set_default()
    #     prj.data = None
    #     prj.add_residential(
    #         method='tabula_de',
    #         usage='single_family_house',
    #         name="ResidentialBuilding",
    #         year_of_construction=1858,
    #         number_of_floors=2,
    #         height_of_floors=3.2,
    #         net_leased_area=219,
    #         construction_type='tabula_standard')
    #     prj.add_residential(
    #         method='tabula_de',
    #         usage='single_family_house',
    #         name="ResidentialBuilding",
    #         year_of_construction=1858,
    #         number_of_floors=2,
    #         height_of_floors=3.2,
    #         net_leased_area=219,
    #         construction_type='tabula_retrofit')
    #     prj.add_residential(
    #         method='tabula_de',
    #         usage='single_family_house',
    #         name="ResidentialBuilding",
    #         year_of_construction=1858,
    #         number_of_floors=2,
    #         height_of_floors=3.2,
    #         net_leased_area=219,
    #         construction_type='tabula_adv_retrofit')
    #
    #     prj.retrofit_all_buildings(type_of_retrofit='retrofit')
    #
    #     prj.set_default()
    #     prj.data = None
    #     prj.add_residential(
    #         method='tabula_de',
    #         usage='single_family_house',
    #         name="ResidentialBuilding",
    #         year_of_construction=1858,
    #         number_of_floors=2,
    #         height_of_floors=3.2,
    #         net_leased_area=219)
    #
    #     prj.retrofit_all_buildings(
    #         year_of_retrofit=2015,
    #         type_of_retrofit="retrofit",
    #         window_type="None",
    #         material="None")
    #
    #     prj.add_residential(
    #         method='tabula_de',
    #         usage='single_family_house',
    #         name="ResidentialBuilding",
    #         year_of_construction=1858,
    #         number_of_floors=2,
    #         height_of_floors=3.2,
    #         net_leased_area=219,
    #         construction_type="tabula_retrofit")
    #
    #     prj.retrofit_all_buildings(
    #         type_of_retrofit="adv_retrofit")
