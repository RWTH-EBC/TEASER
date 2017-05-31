

class Test_tabula(object):
    global prj
    '''




    
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




    def test_tabula_uvalue_retrofit_sfh(self):

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
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.25 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.29 - 0.17)), 1)

            elif "_2_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.32 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.6 - 0.17)), 1)

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1947,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.25 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.28 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1956,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.4 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:

            if "_1_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.28 - 0.17)), 1)

            elif "_2_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.31 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1967,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        for wall in prj.buildings[-1].thermal_zones[-1].outer_walls:

            if "_1_" in wall.construction_type:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.23 - 0.17)), 1)

            if "_2_" in wall.construction_type:
                assert round(1 / (wall.r_conduc * wall.area),
                             1) == round((1 / (1 / 0.21 - 0.17)), 1)
        """
        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.31 - 0.17)), 1)
        """
        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1977,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.22 - 0.17)), 1)

        for floor in prj.buildings[-1].thermal_zones[-1].ground_floors:
            if "_1_" in floor.construction_type:
                assert round(1 / (floor.r_conduc * floor.area),
                             1) == round((1 / (1 / 0.28 - 0.17)), 1)
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

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1982,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.21 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.26 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1993,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.18 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.24 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2000,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.15 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.21 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2008,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.15 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.17 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2014,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.2 - 0.17)), 1)
        """
        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.24 - 0.17)), 1)
        """
        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.8 - 0.17)), 1)

        prj.add_residential(
            method='tabula_de',
            usage='single_family_house',
            name="ResidentialBuilding",
            year_of_construction=2099,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219, construction_type="tabula_retrofit")
        """
        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].outer_walls[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].outer_walls[-1].area),
            1) == round((1 / (1 / 0.15 - 0.17)), 1)
        """
        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].ground_floors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].ground_floors[-1].area),
            1) == round((1 / (1 / 0.15 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].windows[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].windows[-1].area),
            1) == round((1 / (1 / 1.1 - 0.17)), 1)

        assert round(
            1 / (prj.buildings[-1].thermal_zones[-1].doors[-1].r_conduc
                 * prj.buildings[-1].thermal_zones[-1].doors[-1].area),
            1) == round((1 / (1 / 1.3 - 0.17)), 1)



'''
