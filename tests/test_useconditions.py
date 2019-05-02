"""Module to test UseCondition functions."""
from teaser.logic import utilities
from teaser.project import Project
import os
import helptest

prj = Project(True)


class Test_useconditions(object):
    """Unit Tests for TEASER."""

    global prj

    def test_load_use_conditions_new(self):
        """Test of load_use_conditions, no parameter checking."""
        prj.set_default()
        helptest.building_test2(prj)
        use_cond = prj.buildings[-1].thermal_zones[-1].use_conditions
        use_cond.load_use_conditions("Living",
                                     data_class=prj.data)

    def test_load_use_conditions_old(self):
        """Test of old load_boundary_conditions, no parameter checking."""
        use_cond = prj.buildings[-1].thermal_zones[-1].use_conditions
        import teaser.logic.utilities as utils
        prj.data.path_uc = utils.get_full_path(
            "data/input/inputdata/UseConditions.xml")
        prj.data.load_uc_binding()
        import teaser.data.input.boundcond_input as bc_in
        bc_in.load_boundary_conditions(
            bound_cond=use_cond,
            zone_usage="Living",
            data_class=prj.data)

    def test_save_use_conditions(self):
        """Test of save_use_conditions, no parameter checking."""
        try:
            os.remove(os.path.join(
                utilities.get_default_path(), 'UseCondUT.json'))
        except FileNotFoundError:
            pass
        path = os.path.join(
            utilities.get_default_path(), 'UseCondUT.json')
        prj.data.path_uc = path
        prj.data.load_uc_binding()
        use_cond = prj.buildings[-1].thermal_zones[-1].use_conditions
        use_cond.save_use_conditions(data_class=prj.data)
        use_cond.save_use_conditions(data_class=prj.data)
        use_cond.usage = "UnitTest"
        use_cond.save_use_conditions(data_class=prj.data)

    def test_ahu_profiles(self):
        """Test setting AHU profiles of different lengths

        Related to issue 553 at https://github.com/RWTH-EBC/TEASER/issues/553
        """

        prj_test = Project(load_data=True)
        prj_test.name = "TestAHUProfiles"

        prj_test.add_non_residential(
            method="bmvbs",
            usage="office",
            name="OfficeBuilding",
            year_of_construction=2015,
            number_of_floors=4,
            height_of_floors=3.5,
            net_leased_area=1000.0,
        )

        prj_test.used_library_calc = "AixLib"
        prj_test.number_of_elements_calc = 2

        heating_profile_workday = [
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
            293,
        ]

        heating_profile_week = []
        for day in range(7):
            for val in heating_profile_workday:
                if day < 5:
                    set_point = val
                else:
                    set_point = 290.0
                heating_profile_week.append(set_point)

        for zone in prj_test.buildings[-1].thermal_zones:
            zone.use_conditions.heating_profile = heating_profile_week
            zone.use_conditions.cooling_profile = heating_profile_week
            zone.use_conditions.persons_profile = heating_profile_week
            zone.use_conditions.machines_profile = heating_profile_week
            zone.use_conditions.lighting_profile = heating_profile_week
        assert prj_test.buildings[
            -1].thermal_zones[
                -1].use_conditions.heating_profile == heating_profile_week
        assert prj_test.buildings[
            -1].thermal_zones[
                -1].use_conditions.cooling_profile == heating_profile_week
        assert prj_test.buildings[
            -1].thermal_zones[
                -1].use_conditions.persons_profile == heating_profile_week
        assert prj_test.buildings[
            -1].thermal_zones[
                -1].use_conditions.machines_profile == heating_profile_week
        assert prj_test.buildings[
            -1].thermal_zones[
                -1].use_conditions.lighting_profile == heating_profile_week
