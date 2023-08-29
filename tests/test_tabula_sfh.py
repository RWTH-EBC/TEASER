from teaser.project import Project
prj = Project(False)


class Test_tabula_sfh(object):
    global prj

    def test_tabula_de_sfh_area_1859(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.set_default()
        prj.data = None
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 134.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 169.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 85.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 28.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_sfh_area_1919(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1918,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=142)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 83.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 194.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 78.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 22.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_sfh_area_1948(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=303)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 214.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 235.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 144.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 52.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_sfh_area_1957(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=111)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 125.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 117.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 79.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 18.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_sfh_area_1968(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=121)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 168.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 149.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 115.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 27.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.1

    def test_tabula_de_sfh_area_1978(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=173)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 183.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 177.6
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 152.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 34.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_sfh_area_1983(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1982,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=216)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 100.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 159.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 83.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 27.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_sfh_area_1994(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1993,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=150)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 123.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 211.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 75.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 29.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_sfh_area_2001(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=122)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 115.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 126.6
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 84.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 32.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_sfh_area_2009(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=147)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 85.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 188.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 79.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 28.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_sfh_area_2015(self):
        """
        Test for area estimation of tabula sfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=187)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 131.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 227.6
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 107.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 42.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.6

    def test_tabula_uvalue_standard_sfh_1859(self):

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 2.6 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 2.0 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 2.9 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_sfh_1918(self):

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1918,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 1.3 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.7 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:

            if "_1_" in floor.construction_type:

                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.88 - 0.34)), 1)

            elif "_2_" in floor.construction_type:

                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 1.2 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_sfh_1948(self):

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 1.4 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.7 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.77 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_sfh_1957(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 1.4 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_type:

                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.78 - 0.34)), 1)

            elif "_2_" in floor.construction_type:

                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 1.0 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_sfh_1968(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.8 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_type:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 1.2 - 0.17)), 1)

            if "_2_" in wall.construction_type:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 1.08 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_sfh_1978(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.5 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.0 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_type:

                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.77 - 0.34)), 1)

            elif "_2_" in floor.construction_type:

                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 1.0 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_sfh_1983(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1982,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.5 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.65 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 4.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_sfh_1994(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1993,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.4 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.5 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.51 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 3.2 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_sfh_2001(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.35 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.4 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.9 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 2.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_sfh_2009(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.25 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.28 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 2.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_sfh_2015(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.2 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.28 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.35 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.8 - 0.17)), 1)

    def test_tabula_uvalue_standard_sfh_2100(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2099,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.15 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.17 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.17 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.1 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_sfh_1859(self):

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219,
            construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.41 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.35 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.49 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_sfh_1918(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1918,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219,
            construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.41 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.25 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.29 - 0.34)), 1)

            elif "_2_" in floor.construction_type:

                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.32 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_sfh_1948(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.41 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.25 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.28 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_sfh_1957(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.41 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.4 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:

            if "_1_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.28 - 0.34)), 1)

            elif "_2_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.31 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_sfh_1968(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.41 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_type:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.23 - 0.17)), 1)

            if "_2_" in wall.construction_type:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.21 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.31 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_sfh_1978(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.18 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.22 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.28 - 0.34)), 1)
            elif "_2_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.3 - 0.34)), 1)
        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_sfh_1983(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1982,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.41 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.21 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.26 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_sfh_1994(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1993,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.4 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.18 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.24 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_sfh_2001(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.35 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.15 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.21 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_sfh_2009(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.25 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.15 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.17 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_sfh_2015(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.16 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.2 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.24 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_sfh_2100(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2099,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.13 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.15 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.15 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.1 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_sfh_1859(self):

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219,
            construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.14 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.14 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.27 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_sfh_1918(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1918,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219,
            construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.14 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.13 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.22 - 0.34)), 1)

            elif "_2_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.23 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_sfh_1948(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219,
            construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.14 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.13 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.21 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_sfh_1957(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219,
            construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.14 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.13 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:

            if "_1_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.21 - 0.34)), 1)

            if "_2_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.23 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_sfh_1968(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.14 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_type:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.13 - 0.34)), 1)

            if "_2_" in wall.construction_type:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.12 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.23 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_sfh_1978(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.13 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:

            if "_1_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.21 - 0.34)), 1)

            if "_2_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.23 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_sfh_1983(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1982,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.14 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.12 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.20 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_sfh_1994(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1993,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.14 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.11 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.19 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_sfh_2001(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.14 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.14 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.17 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_sfh_2009(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.14 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.14 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.17 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_sfh_2015(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.1 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.12 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.12 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.7 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_sfh_2100(self):
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2100,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.1 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.12 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.12 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.7 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_retrofit(self):
        """
        Test for retrofit of tabula
        """
        prj.set_default()
        prj.data = None
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219,
            construction_type='tabula_standard')
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219,
            construction_type='tabula_retrofit')
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219,
            construction_type='tabula_adv_retrofit')

        prj.retrofit_all_buildings(type_of_retrofit='retrofit')

        prj.set_default()
        prj.data = None
        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        prj.retrofit_all_buildings(
            year_of_retrofit=2015,
            type_of_retrofit="retrofit",
            window_type="None",
            material="None")

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219,
            construction_type="tabula_retrofit")

        prj.retrofit_all_buildings(
            type_of_retrofit="adv_retrofit")
