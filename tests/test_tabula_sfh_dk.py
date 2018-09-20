
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
