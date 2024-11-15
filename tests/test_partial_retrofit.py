import itertools

from teaser.project import Project


class Test_tabula_sfh(object):

    def test_tabula_de_sfh_area_1859(self):
        """
        Test for area estimation of tabula sfh
        """
        for elements, retrofit_choices in itertools.product(
                [
                    None,
                    ["outer_walls", "windows", "rooftops", "ground_floors"],
                    ["outer_walls", "windows"]
                ],
                [
                    None,
                    ["standard", "retrofit", "adv_retrofit"],
                    ["standard", "retrofit"]
                ]
        ):
            prj = Project(False)
            prj.add_residential_retrofit_combinations(
                elements=elements,
                retrofit_choices=retrofit_choices,
                construction_data='tabula_de_standard',
                geometry_data='tabula_de_single_family_house',
                name="ResidentialBuilding",
                year_of_construction=1858,
                number_of_floors=2,
                height_of_floors=3.2,
                net_leased_area=219
            )
            len_elements = len(elements) if elements is not None else 4
            len_choices = len(retrofit_choices) if retrofit_choices is not None else 3
            assert len(prj.buildings) == len_choices ** len_elements, \
                "Number of generated buildings does not match expectation"
