"""
Created August 2019

@author: TEASER Development Team
"""

from teaser.project import Project

prj = Project(True)


class Test_examples(object):
    """Unit Tests for TEASER"""

    global prj

    def test_e1_example_generate_archetype(self):
        """Tests the executability of example 1"""
        from teaser.examples import e1_generate_archetype as e1

        prj = e1.example_generate_archetype()

        assert prj.name == "ArchetypeExample"

    def test_e2_example_export_aixlib(self):
        """Tests the executability of example 2"""
        from teaser.examples import e2_export_aixlib_models as e2

        prj = e2.example_export_aixlib()

    def test_e3_example_export_ibpsa(self):
        """Tests the executability of example 2"""
        from teaser.examples import e3_export_ibpsa_models as e3

        prj = e3.example_export_ibpsa()

    def test_e4_example_save(self):
        """Tests the executability of example 2"""
        from teaser.examples import e4_save as e4

        prj = e4.example_save()

    def test_e5_example_load(self):
        """Tests the executability of example 2"""
        from teaser.examples import e5_load as e5

        prj = e5.example_load()

    def test_e6_example_create_building(self):
        """Tests the executability of example 2"""
        from teaser.examples import e6_generate_building as e6

        prj = e6.example_create_building()

    def test_e7_example_retrofit_building(self):
        """Tests the executability of example 2"""
        from teaser.examples import e7_retrofit as e7

        prj = e7.example_retrofit_building()

    def test_e8_example_change_boundary_conditions(self):
        """Tests the executability of example 2"""
        from teaser.examples import e8_change_boundary_conditions as e8

        prj = e8.example_change_boundary_conditions()
