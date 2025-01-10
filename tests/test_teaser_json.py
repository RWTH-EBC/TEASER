import json
from pathlib import Path
import tempfile

from teaser.examples.e6_generate_building import example_create_building
from teaser.project import Project


class TestTEASERJson(object):
    """Unit Tests for TEASER"""

    # global prj

    def test_save_teaser_json_tabula_de(self):
        """Tests the save function of a teaser residential project"""
        prj = Project(False)
        prj.add_residential(
            construction_data='tabula_de_standard',
            geometry_data='tabula_de_single_family_house',
            name="ResidentialBuilding",
            year_of_construction=1858,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=219.0
        )
        temp_filename = "test_project_tabula.json"
        with tempfile.TemporaryDirectory() as temp_dir:
            prj.save_project(file_name=temp_filename, path=temp_dir)

            file_path = Path(temp_dir) / temp_filename
            with open(file_path, 'r') as f:
                data = json.load(f)
                assert data  # Verify the JSON is not empty

    def test_save_teaser_json_iwu_de(self):
        """Tests the save function of a teaser non-residential project"""
        prj = Project(False)
        prj.add_non_residential(
            construction_data='iwu_heavy',
            geometry_data='bmvbs_office',
            name="OfficeBuilding",
            year_of_construction=1988,
            number_of_floors=4,
            height_of_floors=3.5,
            net_leased_area=4500.0
        )
        temp_filename = "test_project_iwu.json"
        with tempfile.TemporaryDirectory() as temp_dir:
            prj.save_project(file_name=temp_filename, path=temp_dir)

            file_path = Path(temp_dir) / temp_filename
            with open(file_path, 'r') as f:
                data = json.load(f)
                assert data  # Verify the JSON is not empty

    def test_save_teaser_json_kfw_de(self):
        """Tests the save function of a teaser project with kfw 55"""
        prj = Project(False)
        prj.add_residential(
            construction_data='kfw_55',
            geometry_data='tabula_de_single_family_house',
            name="OfficeBuilding",
            year_of_construction=2020,
            number_of_floors=4,
            height_of_floors=3.5,
            net_leased_area=4500.0
        )
        temp_filename = "test_project_kfw.json"
        with tempfile.TemporaryDirectory() as temp_dir:
            prj.save_project(file_name=temp_filename, path=temp_dir)

            file_path = Path(temp_dir) / temp_filename
            with open(file_path, 'r') as f:
                data = json.load(f)
                assert data  # Verify the JSON is not empty

    def test_save_and_load_teaser_json_tabula_de(self):
        """Tests save and load of a teaser archetype"""
        prj = Project(False)
        prj.add_residential(
            construction_data='kfw_55',
            geometry_data='tabula_de_single_family_house',
            name="OfficeBuilding",
            year_of_construction=2020,
            number_of_floors=4,
            height_of_floors=3.5,
            net_leased_area=4500.0
        )
        prj.calc_all_buildings()
        orig_building = prj.buildings[0]

        temp_filename = "test_project_tabula.json"
        with tempfile.TemporaryDirectory() as temp_dir:
            prj.save_project(file_name=temp_filename, path=temp_dir)

            file_path = Path(temp_dir) / temp_filename
            loaded_prj = Project()
            loaded_prj.load_project(file_path)
            loaded_bldg = loaded_prj.buildings[0]
            loaded_prj.calc_all_buildings()

            # compare loaded and saves building
            assert loaded_bldg.outer_area == orig_building.outer_area
            assert loaded_bldg.area_gf == orig_building.area_gf
            assert loaded_bldg.area_rt == orig_building.area_rt
            assert loaded_bldg.window_area == orig_building.window_area
            assert loaded_bldg.thermal_zones[0].ceilings[0].u_value == \
                   orig_building.thermal_zones[0].ceilings[0].u_value
            assert loaded_bldg.thermal_zones[0].doors[0].u_value == \
                   orig_building.thermal_zones[0].doors[0].u_value
            assert loaded_bldg.thermal_zones[0].floors[0].u_value == \
                   orig_building.thermal_zones[0].floors[0].u_value
            assert loaded_bldg.thermal_zones[0].ground_floors[0].u_value == \
                   orig_building.thermal_zones[0].ground_floors[0].u_value
            assert loaded_bldg.thermal_zones[0].rooftops[0].u_value == \
                   orig_building.thermal_zones[0].rooftops[0].u_value
            assert loaded_bldg.thermal_zones[0].windows[0].u_value == \
                   orig_building.thermal_zones[0].windows[0].u_value

    def test_save_and_load_self_generated_building(self):
        """Test save and load of a self generated building"""
        e6_prj = example_create_building()
        e6_prj.calc_all_buildings()

        e6_bldg = e6_prj.buildings[0]
        temp_filename = "test_project_self_generated_building.json"
        with tempfile.TemporaryDirectory() as temp_dir:
            e6_prj.save_project(file_name=temp_filename, path=temp_dir)

            file_path = Path(temp_dir) / temp_filename
            loaded_prj = Project()
            loaded_prj.load_project(file_path)
            loaded_bldg = loaded_prj.buildings[0]
            loaded_prj.calc_all_buildings()

            # compare loaded and saves building
            assert loaded_bldg.outer_area == e6_bldg.outer_area
            assert loaded_bldg.area_gf == e6_bldg.area_gf
            assert loaded_bldg.area_rt == e6_bldg.area_rt
            assert loaded_bldg.window_area == e6_bldg.window_area
            assert loaded_bldg.thermal_zones[0].ground_floors[0].u_value == \
                   e6_bldg.thermal_zones[0].ground_floors[0].u_value
            assert loaded_bldg.thermal_zones[0].rooftops[0].u_value == \
                   e6_bldg.thermal_zones[0].rooftops[0].u_value
            assert loaded_bldg.thermal_zones[0].windows[0].u_value == \
                   e6_bldg.thermal_zones[0].windows[0].u_value
