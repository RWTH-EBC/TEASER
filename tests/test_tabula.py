from teaser.project import Project
prj = Project(False)


class Test_tabula(object):
    global prj
    '''
    def test_tabula_de_sfh(self):

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


    def test_tabula_de_th(self):
        """
        Test for area estimation of tabula th
        """
        prj.set_default()
        prj.data = None

        prj.add_residential(
            method='tabula_de',
            usage='terraced_house',
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

        prj.add_residential(
            method='tabula_de',
            usage='terraced_house',
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

        prj.add_residential(
            method='tabula_de',
            usage='terraced_house',
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

        prj.add_residential(
            method='tabula_de',
            usage='terraced_house',
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

        prj.add_residential(
            method='tabula_de',
            usage='terraced_house',
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

        prj.add_residential(
            method='tabula_de',
            usage='terraced_house',
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

        prj.add_residential(
            method='tabula_de',
            usage='terraced_house',
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

        prj.add_residential(
            method='tabula_de',
            usage='terraced_house',
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

        prj.add_residential(
            method='tabula_de',
            usage='terraced_house',
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

        prj.add_residential(
            method='tabula_de',
            usage='terraced_house',
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


    def test_tabula_de_mfh(self):
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


    def test_tabula_de_ab(self):
        """
        Test for area estimation of tabula ab
        """
        prj.set_default()
        prj.data = None

        prj.add_residential(
            method='tabula_de',
            usage='apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1918,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=829)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 231.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 305.4
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 163.7
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 136.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

        prj.add_residential(
            method='tabula_de',
            usage='apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=1484)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 384.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 1244.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 395.6
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 278.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

        prj.add_residential(
            method='tabula_de',
            usage='apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=1603)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 353.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 1376.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 353.5
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 294.9
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

        prj.add_residential(
            method='tabula_de',
            usage='apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=3887)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 479.6
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 3247.8
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 459.2
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 687.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0

        prj.add_residential(
            method='tabula_de',
            usage='apartment_block',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=3322)

        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].rooftops), 1) == 540.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].outer_walls), 1) == 2130.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].ground_floors), 1) == 540.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].windows), 1) == 545.0
        assert round(
            sum(wall.area for wall in
                prj.buildings[-1].thermal_zones[-1].doors), 1) == 2.0


assert round(
    prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value, 1) == 2.9
assert round(
    prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 2.8
assert round(
    prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

prj.add_residential(
    method='tabula_de',
    usage='single_family_house',
    name="ResidentialBuilding",
    year_of_construction=1917,
    number_of_floors=2,
    height_of_floors=3.2,
    net_leased_area=219)

# assert round(
# prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 1.3
assert round(
    prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value, 1) == 1.7
assert round(
    prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value, 1) == 0.88
assert round(
    prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 2.8
assert round(
    prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

prj.add_residential(
    method='tabula_de',
    usage='single_family_house',
    name="ResidentialBuilding",
    year_of_construction=1947,
    number_of_floors=2,
    height_of_floors=3.2,
    net_leased_area=219)

# assert round(
# prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 1.4
assert round(
    prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value, 1) == 1.7
assert round(
    prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value, 1) == 0.77
assert round(
    prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 2.8
assert round(
    prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

prj.add_residential(
    method='tabula_de',
    usage='single_family_house',
    name="ResidentialBuilding",
    year_of_construction=1956,
    number_of_floors=2,
    height_of_floors=3.2,
    net_leased_area=219)

# assert round(
# prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 1.4
assert round(
    prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value, 1) == 1.4
for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
    if "_1_" in floor.construction_type:
        assert round(floor.u_value, 1) == 0.78
    elif "_2_" in floor.construction_type:
        assert round(floor.u_value, 1) == 1.01
assert round(
    prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 2.8
assert round(
    prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

prj.add_residential(
    method='tabula_de',
    usage='single_family_house',
    name="ResidentialBuilding",
    year_of_construction=1967,
    number_of_floors=2,
    height_of_floors=3.2,
    net_leased_area=219)

# assert round(
# prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.8
for ow in prj.buildings[-1].thermal_zones[-1].outer_walls:
    if "_1_" in ow.construction_type:
        assert round(ow.u_value, 1) == 1.2
    elif "_2_" in ow.construction_type:
        assert round(ow.u_value, 1) == 0.8
assert round(
    prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value,
    1) == 1.08
assert round(
    prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 2.8
assert round(
    prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

prj.add_residential(
    method='tabula_de',
    usage='single_family_house',
    name="ResidentialBuilding",
    year_of_construction=1977,
    number_of_floors=2,
    height_of_floors=3.2,
    net_leased_area=219)

# assert round(
# prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.5
assert round(
    prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value,
    1) == 1.0
for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
    if "_1_" in floor.construction_type:
        assert round(floor.u_value, 1) == 0.77
    elif "_2_" in floor.construction_type:
        assert round(floor.u_value, 1) == 1.0
assert round(
    prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 2.0
assert round(
    prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

prj.add_residential(
    method='tabula_de',
    usage='single_family_house',
    name="ResidentialBuilding",
    year_of_construction=1982,
    number_of_floors=2,
    height_of_floors=3.2,
    net_leased_area=219)

# assert round(
# prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.5
assert round(
    prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value,
    1) == 0.8
assert round(
    prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value,
    1) == 0.65
assert round(
    prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 4.3
assert round(
    prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

prj.add_residential(
    method='tabula_de',
    usage='single_family_house',
    name="ResidentialBuilding",
    year_of_construction=1982,
    number_of_floors=2,
    height_of_floors=3.2,
    net_leased_area=219)

# assert round(
# prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.4
assert round(
    prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value,
    1) == 0.5
assert round(
    prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value,
    1) == 0.51
assert round(
    prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 3.2
assert round(
    prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

prj.add_residential(
    method='tabula_de',
    usage='single_family_house',
    name="ResidentialBuilding",
    year_of_construction=2000,
    number_of_floors=2,
    height_of_floors=3.2,
    net_leased_area=219)

# assert round(
# prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.35
assert round(
    prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value,
    1) == 0.3
assert round(
    prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value,
    1) == 0.4
assert round(
    prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 1.9
assert round(
    prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 2.0

prj.add_residential(
    method='tabula_de',
    usage='single_family_house',
    name="ResidentialBuilding",
    year_of_construction=2008,
    number_of_floors=2,
    height_of_floors=3.2,
    net_leased_area=219)

# assert round(
# prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.25
assert round(
    prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value,
    1) == 0.3
assert round(
    prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value,
    1) == 0.28
assert round(
    prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 1.4
assert round(
    prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 2.0

prj.add_residential(
    method='tabula_de',
    usage='single_family_house',
    name="ResidentialBuilding",
    year_of_construction=2014,
    number_of_floors=2,
    height_of_floors=3.2,
    net_leased_area=219)

# assert round(
# prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.2
assert round(
    prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value,
    1) == 0.28
assert round(
    prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value,
    1) == 0.35
assert round(
    prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 1.3
assert round(
    prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 1.8
'''

    def test_tabula_uvalue_standard_sfh(self):
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
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 2.0 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 2.9 - 0.34)), 1)

        '''
            assert round(
                prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value, 1) == 2.9
            assert round(
                prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 2.8
            assert round(
                prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

            prj.add_residential(
                method='tabula_de',
                usage='single_family_house',
                name="ResidentialBuilding",
                year_of_construction=1917,
                number_of_floors=2,
                height_of_floors=3.2,
                net_leased_area=219)

            # assert round(
            # prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 1.3
            assert round(
                prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value, 1) == 1.7
            assert round(
                prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value, 1) == 0.88
            assert round(
                prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 2.8
            assert round(
                prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

            prj.add_residential(
                method='tabula_de',
                usage='single_family_house',
                name="ResidentialBuilding",
                year_of_construction=1947,
                number_of_floors=2,
                height_of_floors=3.2,
                net_leased_area=219)

            # assert round(
            # prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 1.4
            assert round(
                prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value, 1) == 1.7
            assert round(
                prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value, 1) == 0.77
            assert round(
                prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 2.8
            assert round(
                prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

            prj.add_residential(
                method='tabula_de',
                usage='single_family_house',
                name="ResidentialBuilding",
                year_of_construction=1956,
                number_of_floors=2,
                height_of_floors=3.2,
                net_leased_area=219)

            # assert round(
            # prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 1.4
            assert round(
                prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value, 1) == 1.4
            for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
                if "_1_" in floor.construction_type:
                    assert round(floor.u_value, 1) == 0.78
                elif "_2_" in floor.construction_type:
                    assert round(floor.u_value, 1) == 1.01
            assert round(
                prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 2.8
            assert round(
                prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

            prj.add_residential(
                method='tabula_de',
                usage='single_family_house',
                name="ResidentialBuilding",
                year_of_construction=1967,
                number_of_floors=2,
                height_of_floors=3.2,
                net_leased_area=219)

            # assert round(
            # prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.8
            for ow in prj.buildings[-1].thermal_zones[-1].outer_walls:
                if "_1_" in ow.construction_type:
                    assert round(ow.u_value, 1) == 1.2
                elif "_2_" in ow.construction_type:
                    assert round(ow.u_value, 1) == 0.8
            assert round(
                prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value,
                1) == 1.08
            assert round(
                prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 2.8
            assert round(
                prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

            prj.add_residential(
                method='tabula_de',
                usage='single_family_house',
                name="ResidentialBuilding",
                year_of_construction=1977,
                number_of_floors=2,
                height_of_floors=3.2,
                net_leased_area=219)

            # assert round(
            # prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.5
            assert round(
                prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value,
                1) == 1.0
            for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
                if "_1_" in floor.construction_type:
                    assert round(floor.u_value, 1) == 0.77
                elif "_2_" in floor.construction_type:
                    assert round(floor.u_value, 1) == 1.0
            assert round(
                prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 2.0
            assert round(
                prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

            prj.add_residential(
                method='tabula_de',
                usage='single_family_house',
                name="ResidentialBuilding",
                year_of_construction=1982,
                number_of_floors=2,
                height_of_floors=3.2,
                net_leased_area=219)

            # assert round(
            # prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.5
            assert round(
                prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value,
                1) == 0.8
            assert round(
                prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value,
                1) == 0.65
            assert round(
                prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 4.3
            assert round(
                prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

            prj.add_residential(
                method='tabula_de',
                usage='single_family_house',
                name="ResidentialBuilding",
                year_of_construction=1982,
                number_of_floors=2,
                height_of_floors=3.2,
                net_leased_area=219)

            # assert round(
            # prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.4
            assert round(
                prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value,
                1) == 0.5
            assert round(
                prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value,
                1) == 0.51
            assert round(
                prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 3.2
            assert round(
                prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 3.0

            prj.add_residential(
                method='tabula_de',
                usage='single_family_house',
                name="ResidentialBuilding",
                year_of_construction=2000,
                number_of_floors=2,
                height_of_floors=3.2,
                net_leased_area=219)

            # assert round(
            # prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.35
            assert round(
                prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value,
                1) == 0.3
            assert round(
                prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value,
                1) == 0.4
            assert round(
                prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 1.9
            assert round(
                prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 2.0

            prj.add_residential(
                method='tabula_de',
                usage='single_family_house',
                name="ResidentialBuilding",
                year_of_construction=2008,
                number_of_floors=2,
                height_of_floors=3.2,
                net_leased_area=219)

            # assert round(
            # prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.25
            assert round(
                prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value,
                1) == 0.3
            assert round(
                prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value,
                1) == 0.28
            assert round(
                prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 1.4
            assert round(
                prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 2.0

            prj.add_residential(
                method='tabula_de',
                usage='single_family_house',
                name="ResidentialBuilding",
                year_of_construction=2014,
                number_of_floors=2,
                height_of_floors=3.2,
                net_leased_area=219)

            # assert round(
            # prj.buildings[-1].thermal_zones[-1].rooftops[-1].u_value, 1) == 0.2
            assert round(
                prj.buildings[-1].thermal_zones[-1].outer_walls[-1].u_value,
                1) == 0.28
            assert round(
                prj.buildings[-1].thermal_zones[-1].ground_floors[-1].u_value,
                1) == 0.35
            assert round(
                prj.buildings[-1].thermal_zones[-1].windows[-1].u_value, 1) == 1.3
            assert round(
                prj.buildings[-1].thermal_zones[-1].doors[-1].u_value, 1) == 1.8
            '''
