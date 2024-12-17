import os
import unittest
from teaser.logic import utilities
from teaser.project import Project
from teaser.data.output.besmod_output import _convert_heating_profile


class Test_besmod_output(unittest.TestCase):

    def test_export_besmod(self):
        """test of export_besmod, no calculation verification"""

        prj = Project()

        prj.add_residential(
            construction_data='iwu_heavy',
            geometry_data='iwu_single_family_dwelling',
            name="ResidentialBuilding",
            year_of_construction=1988,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=200.0)

        prj.add_non_residential(
            construction_data='iwu_heavy',
            geometry_data='bmvbs_institute',
            name="InstituteBuilding",
            year_of_construction=1952,
            number_of_floors=5,
            height_of_floors=4.0,
            net_leased_area=3400.0)

        prj.number_of_elements_calc = 1
        prj.used_library_calc = "IBPSA"
        with self.assertRaises(AttributeError):
            prj.export_besmod()
        prj.used_library_calc = "AixLib"
        with self.assertRaises(NotImplementedError):
            prj.export_besmod()
        prj.number_of_elements_calc = 4
        prj.calc_all_buildings()
        prj.export_besmod()
        with self.assertRaises(ValueError):
            prj.export_besmod(examples="wrong_example")
        examples = ["TEASERHeatLoadCalculation",
                    "HeatPumpMonoenergetic",
                    "GasBoilerBuildingOnly"]
        with self.assertRaises(ValueError):
            prj.export_besmod(examples=examples)

        prj.export_besmod(examples=examples,
                          THydSup_nominal=55 + 273.15)

        t_hyd_sup_nominal = {"ResidentialBuilding": 328.15,
                             "WrongBuilding": {"Office": 343.15,
                                               "Floor": 343.15,
                                               "Storage": 343.15,
                                               "Meeting": 343.15,
                                               "Restroom": 343.15,
                                               "ICT": 343.15,
                                               "Laboratory": 328.15}}
        with self.assertRaises(KeyError):
            prj.export_besmod(examples=examples,
                              THydSup_nominal=t_hyd_sup_nominal)

        t_hyd_sup_nominal = {"ResidentialBuilding": 328.15,
                             "InstituteBuilding": {"WrongZone": 343.15,
                                                   "Floor": 343.15,
                                                   "Storage": 343.15,
                                                   "Meeting": 343.15,
                                                   "Restroom": 343.15,
                                                   "ICT": 343.15,
                                                   "Laboratory": 328.15}}
        with self.assertRaises(KeyError):
            prj.export_besmod(examples=examples,
                              THydSup_nominal=t_hyd_sup_nominal)

        t_hyd_sup_nominal = {"ResidentialBuilding": 328.15,
                             "InstituteBuilding": "WrongValue"}
        with self.assertRaises(ValueError):
            prj.export_besmod(examples=examples,
                              THydSup_nominal=t_hyd_sup_nominal)

        t_hyd_sup_nominal = {"ResidentialBuilding": 328.15,
                             "InstituteBuilding": {"Office": 343.15,
                                                   "Floor": 343.15,
                                                   "Storage": 343.15,
                                                   "Meeting": 343.15,
                                                   "Restroom": 343.15,
                                                   "ICT": 343.15,
                                                   "Laboratory": 328.15}}
        prj.export_besmod(examples=examples,
                          THydSup_nominal=t_hyd_sup_nominal)

        q_bui_old_flow_design = {
            bldg.name: {
                tz.name: tz.model_attr.heat_load for tz in bldg.thermal_zones
            }
            for bldg in prj.buildings
        }
        custom_template_path = utilities.get_full_path("examples/examplefiles/custom_besmod_templates")
        custom_example_template = {"ModelicaConferencePaper": os.path.join(custom_template_path, "custom_template.txt")}
        custom_script = {"HeatPumpMonoenergetic": os.path.join(custom_template_path, "custom_script_hp_mono.txt"),
                         "ModelicaConferencePaper": os.path.join(custom_template_path, "custom_script.txt")}
        t_hyd_sup_nominal_old = {1950: 90 + 273.15,
                               1980: 70 + 273.15}
        prj.export_besmod(examples=examples,
                          THydSup_nominal=t_hyd_sup_nominal,
                          QBuiOld_flow_design=q_bui_old_flow_design,
                          THydSupOld_design=t_hyd_sup_nominal_old,
                          custom_examples=custom_example_template,
                          custom_script=custom_script)

    def test_convert_heating_profile(self):
        """Test the conversion of heating profiles for BESMod"""
        with self.assertRaises(ValueError):
            _convert_heating_profile([293.15])
        heating_profile = [290.15,
                           290.15,
                           290.15,
                           290.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           290.15,
                           290.15,
                           290.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           290.15,
                           290.15,
                           290.15]
        with self.assertRaises(ValueError):
            _convert_heating_profile(heating_profile)
        heating_profile = [293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15]
        t_set_zone_nominal, start_time, width, amplitude = _convert_heating_profile(heating_profile)
        self.assertEqual(t_set_zone_nominal, 293.15)
        self.assertAlmostEqual(start_time, 0)
        self.assertAlmostEqual(width, 1e-50)
        self.assertEqual(amplitude, 0)
        heating_profile = [290.15,
                           290.15,
                           290.15,
                           290.15,
                           290.15,
                           290.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15]
        t_set_zone_nominal, start_time, width, amplitude = _convert_heating_profile(heating_profile)
        self.assertEqual(t_set_zone_nominal, 293.15)
        self.assertAlmostEqual(start_time, 0)
        self.assertAlmostEqual(width, 6 / 24 * 100)
        self.assertEqual(amplitude, -3)
        heating_profile = [293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           290.15,
                           290.15,
                           290.15,
                           290.15]
        t_set_zone_nominal, start_time, width, amplitude = _convert_heating_profile(heating_profile)
        self.assertEqual(t_set_zone_nominal, 293.15)
        self.assertAlmostEqual(start_time, 20 * 3600)
        self.assertAlmostEqual(width, 4 / 24 * 100)
        self.assertEqual(amplitude, -3)
        heating_profile = [290.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           293.15,
                           290.15]
        t_set_zone_nominal, start_time, width, amplitude = _convert_heating_profile(heating_profile)
        self.assertEqual(t_set_zone_nominal, 293.15)
        self.assertAlmostEqual(start_time, 23 * 3600)
        self.assertAlmostEqual(width, 2 / 24 * 100)
        self.assertEqual(amplitude, -3)
