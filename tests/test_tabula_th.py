from teaser.project import Project
prj = Project(False)


class Test_tabula_th(object):
    global prj

    def test_tabula_de_th_area_1919(self):
        """
        Test for area estimation of tabula th
        """
        prj.set_default()
        prj.data = None

        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1918,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=96)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 60
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 74.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 60.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 18.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_area_1948(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=113)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 50.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 64.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 50.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 21.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_area_1956(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=150)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 81.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 134.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 81.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 46.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_area_1968(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=117)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 46.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 40.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 46.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 13.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_area_1977(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=106)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 60.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 53.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 60.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 23.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_area_1983(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1982,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=108)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 97.6
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 54.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 73.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 20.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_area_1994(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1993,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=128)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 64.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 50.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 56.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 18.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_area_2001(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=149)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 77.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 59.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 51.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 22.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.5

    def test_tabula_de_th_area_2009(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=152)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 91.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 140.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 70.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 36.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_th_area_2015(self):
        """
        Test for area estimation of tabula th
        """
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=196)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 75.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 207.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 67.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 28.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.7

    def test_tabula_uvalue_standard_th_1919(self):

        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1918,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.77 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.7 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.88 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.7 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_1948(self):
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.65 - 0.17)), 1)

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

    def test_tabula_uvalue_standard_th_1957(self):
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.65 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.2 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 1.29 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_1968(self):
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.51 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.2 - 0.17)), 1)

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

    def test_tabula_uvalue_standard_th_1978(self):
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.51 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.0 - 0.17)), 1)

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

    def test_tabula_uvalue_standard_th_1983(self):
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
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
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_1994(self):
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
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
            1) == round((1 / (1 / 0.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.51 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 2.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_2001(self):
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.35 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.6 - 0.17)), 1)

            if "_2_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.45 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 2.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_2008(self):
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
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
            1) == round((1 / (1 / 0.3 - 0.17)), 1)

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
            1) == round((1 / (1 / 2.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_2015(self):
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.2 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.28 - 0.17)), 1)

            if "_2_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.28 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.35 - 0.34)), 1)

        for win in prj.buildings[-1].thermal_zones[-1].windows:
            if "_1_" in win.construction_data:
                assert round(1 / (win.r_conduc * win.area),
                             1) == round((1 / (1 / 1.3 - 0.17)), 1)

            if "_2_" in win.construction_data:
                assert round(1 / (win.r_conduc * win.area),
                             1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.8 - 0.17)), 1)

    def test_tabula_uvalue_standard_th_2100(self):
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2099,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.13 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.16 - 0.17)), 1)

            if "_2_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.16 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.16 - 0.34)), 1)

        for win in prj.buildings[-1].thermal_zones[-1].windows:
            if "_1_" in win.construction_data:
                assert round(1 / (win.r_conduc * win.area),
                             1) == round((1 / (1 / 1.1 - 0.17)), 1)

            if "_2_" in win.construction_data:
                assert round(1 / (win.r_conduc * win.area),
                             1) == round((1 / (1 / 1.1 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_th_1919(self):

        prj.add_residential(
            construction_data='tabula_de_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1918,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219
        )

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.21 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.34 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.29 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_th_1948(self):

        prj.add_residential(
            construction_data='tabula_de_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.2 - 0.17)), 1)

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

    def test_tabula_uvalue_retrofit_th_1957(self):

        prj.add_residential(
            construction_data='tabula_de_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.2 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.23 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.33 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_th_1968(self):

        prj.add_residential(
            construction_data='tabula_de_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.19 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.23 - 0.17)), 1)

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

    def test_tabula_uvalue_retrofit_th_1978(self):

        prj.add_residential(
            construction_data='tabula_de_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.19 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.22 - 0.17)), 1)

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

    def test_tabula_uvalue_retrofit_th_1983(self):

        prj.add_residential(
            construction_data='tabula_de_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1982,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

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

    def test_tabula_uvalue_retrofit_th_1994(self):

        prj.add_residential(
            construction_data='tabula_de_retrofit',
            geometry_data='tabula_de_terraced_house',
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
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_th_2001(self):

        prj.add_residential(
            construction_data='tabula_de_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.35 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.2 - 0.17)), 1)

            if "_2_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.2 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.22 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_th_2009(self):

        prj.add_residential(
            construction_data='tabula_de_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
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

    def test_tabula_uvalue_retrofit_th_2015(self):

        prj.add_residential(
            construction_data='tabula_de_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.16 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.2 - 0.17)), 1)

            if "_2_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.2 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.25 - 0.34)), 1)

        for win in prj.buildings[-1].thermal_zones[-1].windows:
            if "_1_" in win.construction_data:
                assert round(1 / (win.r_conduc * win.area),
                             1) == round((1 / (1 / 1.3 - 0.17)), 1)

            if "_2_" in win.construction_data:
                assert round(1 / (win.r_conduc * win.area),
                             1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_th_2100(self):

        prj.add_residential(
            construction_data='tabula_de_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2099,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.13 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.15 - 0.17)), 1)

            if "_2_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.15 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.15 - 0.34)), 1)

        for win in prj.buildings[-1].thermal_zones[-1].windows:
            if "_1_" in win.construction_data:
                assert round(1 / (win.r_conduc * win.area),
                             1) == round((1 / (1 / 1.1 - 0.17)), 1)

            if "_2_" in win.construction_data:
                assert round(1 / (win.r_conduc * win.area),
                             1) == round((1 / (1 / 1.1 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_th_1919(self):

        prj.add_residential(
            construction_data='tabula_de_adv_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1918,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

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
            1) == round((1 / (1 / 0.22 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_th_1948(self):

        prj.add_residential(
            construction_data='tabula_de_adv_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

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
            1) == round((1 / (1 / 0.21 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_th_1957(self):

        prj.add_residential(
            construction_data='tabula_de_adv_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

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
            1) == round((1 / (1 / 0.24 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_th_1968(self):

        prj.add_residential(
            construction_data='tabula_de_adv_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

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
            1) == round((1 / (1 / 0.23 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_th_1978(self):

        prj.add_residential(
            construction_data='tabula_de_adv_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

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
            1) == round((1 / (1 / 0.21 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_th_1983(self):

        prj.add_residential(
            construction_data='tabula_de_adv_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1982,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

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

    def test_tabula_uvalue_retrofit_adv_th_1994(self):

        prj.add_residential(
            construction_data='tabula_de_adv_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=1993,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

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

    def test_tabula_uvalue_retrofit_adv_th_2001(self):

        prj.add_residential(
            construction_data='tabula_de_adv_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.14 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.14 - 0.17)), 1)

            if "_2_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
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

    def test_tabula_uvalue_retrofit_adv_th_2008(self):

        prj.add_residential(
            construction_data='tabula_de_adv_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

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

    def test_tabula_uvalue_retrofit_adv_th_2015(self):

        prj.add_residential(
            construction_data='tabula_de_adv_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.1 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.12 - 0.17)), 1)

            if "_2_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.12 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.12 - 0.34)), 1)

        for win in prj.buildings[-1].thermal_zones[-1].windows:
            if "_1_" in win.construction_data:
                assert round(1 / (win.r_conduc * win.area),
                             1) == round((1 / (1 / 0.7 - 0.17)), 1)

            if "_2_" in win.construction_data:
                assert round(1 / (win.r_conduc * win.area),
                             1) == round((1 / (1 / 1.0 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_th_2100(self):

        prj.add_residential(
            construction_data='tabula_de_adv_retrofit',
            geometry_data='tabula_de_terraced_house',
            name="ResidentialBuilding",
            year_of_construction=2099,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.1 - 0.21)), 1)

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.12 - 0.17)), 1)

            if "_2_" in wall.construction_data:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.12 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.12 - 0.34)), 1)

        for win in prj.buildings[-1].thermal_zones[-1].windows:
            if "_1_" in win.construction_data:
                assert round(1 / (win.r_conduc * win.area),
                             1) == round((1 / (1 / 0.7 - 0.17)), 1)

            if "_2_" in win.construction_data:
                assert round(1 / (win.r_conduc * win.area),
                             1) == round((1 / (1 / 1.0 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)
