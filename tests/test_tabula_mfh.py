from teaser.project import Project
prj = Project(False)


class Test_tabula_mfh(object):
    global prj

    def test_tabula_de_mfh_area_1859(self):
        """
        Test for area estimation of tabula mfh
        """
        prj.set_default()
        prj.data = None
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=677)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 284.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 749.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 173.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 107
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_mfh_area_1919(self):
        """
        Test for area estimation of tabula mfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1918,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=312)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 102.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 146
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 102.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 54.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_mfh_area_1948(self):
        """
        Test for area estimation of tabula mfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=385)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 189.6
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 325.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 158.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 71.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_mfh_area_1957(self):
        """
        Test for area estimation of tabula mfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=632)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 355.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 462.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 355.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 98.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_mfh_area_1968(self):
        """
        Test for area estimation of tabula mfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=3129)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 971.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 2039
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 971.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 507.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_mfh_area_1978(self):
        """
        Test for area estimation of tabula mfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=469)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 216.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 336.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 216.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 81.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_mfh_area_1983(self):
        """
        Test for area estimation of tabula mfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1982,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=654)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 248.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 447.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 248.3
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 99.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_mfh_area_1994(self):
        """
        Test for area estimation of tabula mfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1993,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=778)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 249.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 774.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 249.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 161.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_mfh_area_2001(self):
        """
        Test for area estimation of tabula mfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=835)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 283.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 695.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 283.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 162.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_mfh_area_2009(self):
        """
        Test for area estimation of tabula mfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=2190)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 588.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 1698.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 619.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 308.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

    def test_tabula_de_mfh_area_2015(self):
        """
        Test for area estimation of tabula mfh
        """
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=1305)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 321.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 1193.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 321.1
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 243.6
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 47.9

    def test_tabula_uvalue_standard_mfh_1859(self):

        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
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

    def test_tabula_uvalue_standard_mfh_1918(self):

        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
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
            1) == round((1 / (1 / 2.2 - 0.17)), 1)

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

    def test_tabula_uvalue_standard_mfh_1948(self):

        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        for roof in prj.buildings[-1].thermal_zones[-1].rooftops:
            if "_1_" in roof.construction_type:

                assert round(1 / (roof.r_conduc * roof.area),
                             1) == round((1 / (1 / 1.4 - 0.21)), 1)

            elif "_2_" in roof.construction_type:

                assert round(1 / (roof.r_conduc * roof.area),
                             1) == round((1 / (1 / 0.65 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.7 - 0.17)), 1)

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
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_mfh_1957(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 1.08 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 1.2 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 1.33 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_mfh_1968(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.51 - 0.21)), 1)

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
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_mfh_1978(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
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
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 4.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_mfh_1983(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1982,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.43 - 0.17)), 1)

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
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 4.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_mfh_1994(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1993,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.36 - 0.17)), 1)

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
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 4.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_mfh_2001(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.32 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.4 - 0.17)), 1)

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

    def test_tabula_uvalue_standard_mfh_2009(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
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
            1) == round((1 / (1 / 0.25 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.32 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.4 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 3.0 - 0.17)), 1)

    def test_tabula_uvalue_standard_mfh_2015(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
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

    def test_tabula_uvalue_standard_mfh_2100(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2099,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.25 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.29 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.29 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.1 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_mfh_1859(self):

        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
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

    def test_tabula_uvalue_retrofit_mfh_1918(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
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
            1) == round((1 / (1 / 0.36 - 0.17)), 1)

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

    def test_tabula_uvalue_retrofit_mfh_1948(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        for roof in prj.buildings[-1].thermal_zones[-1].rooftops:
            if "_1_" in roof.construction_type:

                assert round(1 / (roof.r_conduc * roof.area),
                             1) == round((1 / (1 / 0.41 - 0.21)), 1)

            elif "_2_" in roof.construction_type:

                assert round(1 / (roof.r_conduc * roof.area),
                             1) == round((1 / (1 / 0.2 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.25 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_type:

                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.28 - 0.34)), 1)

            elif "_2_" in floor.construction_type:

                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_mfh_1957(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.23 - 0.17)), 1)

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

    def test_tabula_uvalue_retrofit_mfh_1968(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.19 - 0.21)), 1)

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

    def test_tabula_uvalue_retrofit_mfh_1978(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

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

    def test_tabula_uvalue_retrofit_mfh_1983(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1982,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.17 - 0.17)), 1)

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

    def test_tabula_uvalue_retrofit_mfh_1994(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1993,
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
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_mfh_2001(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

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
            1) == round((1 / (1 / 0.21 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_mfh_2009(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.2 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.13 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.18 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_mfh_2015(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.1 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.14 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.18 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.7 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_mfh_2100(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2099,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.1 - 0.21)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.11 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.11 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.1 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_mfh_1859(self):

        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
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

    def test_tabula_uvalue_retrofit_adv_mfh_1918(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
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
            1) == round((1 / (1 / 0.14 - 0.17)), 1)

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

    def test_tabula_uvalue_retrofit_adv_mfh_1948(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        for roof in prj.buildings[-1].thermal_zones[-1].rooftops:
            if "_1_" in roof.construction_type:

                assert round(1 / (roof.r_conduc * roof.area),
                             1) == round((1 / (1 / 0.14 - 0.21)), 1)

            elif "_2_" in roof.construction_type:

                assert round(1 / (roof.r_conduc * roof.area),
                             1) == round((1 / (1 / 0.1 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.13 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_type:

                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.21 - 0.34)), 1)

            elif "_2_" in floor.construction_type:

                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.23 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_mfh_1957(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.11 - 0.17)), 1)

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

    def test_tabula_uvalue_retrofit_adv_mfh_1968(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.09 - 0.21)), 1)

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

    def test_tabula_uvalue_retrofit_adv_mfh_1978(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
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

    def test_tabula_uvalue_retrofit_adv_mfh_1983(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1982,
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
            1) == round((1 / (1 / 0.12 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.2 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_mfh_1994(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=1993,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

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
            1) == round((1 / (1 / 0.19 - 0.34)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 0.8 - 0.17)), 1)

    def test_tabula_uvalue_retrofit_adv_mfh_2001(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.11 - 0.21)), 1)

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

    def test_tabula_uvalue_retrofit_adv_mfh_2009(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
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

    def test_tabula_uvalue_retrofit_adv_mfh_2015(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_adv_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].rooftops[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].rooftops[-1].area),
            1) == round((1 / (1 / 0.08 - 0.17)), 1)

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

    def test_tabula_uvalue_retrofit_adv_mfh_2100(self):
        prj.add_residential(
            method='tabula_de',
            usage='multi_family_house',
            name="ResidentialBuilding",
            year_of_construction=2099,
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
            1) == round((1 / (1 / 0.11 - 0.17)), 1)

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
