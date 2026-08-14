import os
import re
import unittest
from teaser.logic import utilities
from teaser.project import Project
from teaser.data.output.besmod_output import _convert_heating_profile


def _read_wall_record(path):
    """Return {'n': int, 'd': [float], 'rho': [...], ...} of a wall record."""
    with open(path) as record_file:
        content = record_file.read()
    record = {"n": int(re.search(r"n=(\d+)", content).group(1))}
    for name in ("d", "rho", "lambda", "c"):
        values = re.search(name + r"=\{([^}]*)\}", content).group(1)
        record[name] = [float(value) for value in values.split(",")]
    return record


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

        prj.export_besmod(examples=["TEASERHeatLoadCalculation"])

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
        prj.export_besmod(custom_examples=custom_example_template)

    def test_export_besmod_hom_wall_records(self):
        """test the HOM wall type records exported alongside the ROM"""

        prj = Project()
        prj.name = "BESModHOMWallRecords"

        prj.add_residential(
            construction_data='aixlib_S',
            geometry_data='aixlib_high_order_single_family_house',
            name="ResidentialBuildingHighOrderAixLib",
            year_of_construction=1990,
            net_leased_area=170.0,
            number_of_floors=2,
            height_of_floors=2.6)

        prj.used_library_calc = "AixLib"
        prj.number_of_elements_calc = 4
        prj.calc_all_buildings()
        path = prj.export_besmod(examples=["TEASERHeatLoadCalculation"],
                                 THydSup_nominal=55 + 273.15,
                                 export_with_hom=True)

        bldg = prj.buildings[0]
        wall_path = os.path.join(path, bldg.name, bldg.name + "_DataBase",
                                 "Walls")
        records = {}
        for wall_type in ('OW', 'roof', 'roof_attic', 'IW_vert_half',
                          'IW2_vert_half', 'IW_hori_upHalf', 'IW_hori_loHalf',
                          'ground_floor_loHalf', 'ground_floor_upHalf',
                          'IW_hori_att_upHalf', 'IW_hori_att_loHalf'):
            record = _read_wall_record(os.path.join(
                wall_path, bldg.name + "_" + wall_type + ".mo"))
            # a record with n=0 does not translate in Modelica
            self.assertGreater(record["n"], 0, wall_type)
            for name in ("d", "rho", "lambda", "c"):
                self.assertEqual(len(record[name]), record["n"], wall_type)
            records[wall_type] = record

        # The two halves of the construction between the topmost heated
        # rooms and the (unheated) attic are pre-split in the aixlib_*
        # construction data, so they have to be exported one-to-one -
        # these are AixLib's own CEattic_WSchV1984_SML_loHalf and
        # FLattic_WSchV1984_SML_upHalf, which the data was derived from.
        self.assertEqual(records["IW_hori_att_loHalf"]["d"],
                         [0.08, 0.0125, 0.015])
        self.assertEqual(records["IW_hori_att_loHalf"]["lambda"],
                         [0.09, 0.25, 0.51])
        self.assertEqual(records["IW_hori_att_upHalf"]["d"], [0.08, 0.02])
        self.assertEqual(records["IW_hori_att_upHalf"]["lambda"],
                         [0.09, 0.18])

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
        self.assertAlmostEqual(width, 0)
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
        self.assertAlmostEqual(width, 6)
        self.assertEqual(amplitude, 3)
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
        self.assertAlmostEqual(width, 4)
        self.assertEqual(amplitude, 3)
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
        self.assertAlmostEqual(width, 2)
        self.assertEqual(amplitude, 3)
