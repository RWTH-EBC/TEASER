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

        # Every exported record has to be picked up by the wall type
        # collection - AixLib's own OFD collections assign each of the
        # BaseDataMultiInnerWalls slots its matching record, e.g. the load
        # bearing inner wall (IW2_vert_half) to IW2_vert_half_a/b.
        with open(os.path.join(
                wall_path, bldg.name + "_wallTypes.mo")) as wall_types_file:
            wall_types = wall_types_file.read()
        for slot, wall_type in (("OW", "OW"),
                                ("IW_vert_half_a", "IW_vert_half"),
                                ("IW_vert_half_b", "IW_vert_half"),
                                ("IW2_vert_half_a", "IW2_vert_half"),
                                ("IW2_vert_half_b", "IW2_vert_half"),
                                ("IW_hori_upp_half", "IW_hori_upHalf"),
                                ("IW_hori_low_half", "IW_hori_loHalf"),
                                ("IW_hori_att_upp_half", "IW_hori_att_upHalf"),
                                ("IW_hori_att_low_half", "IW_hori_att_loHalf"),
                                ("groundPlate_upp_half", "ground_floor_upHalf"),
                                ("groundPlate_low_half", "ground_floor_loHalf"),
                                ("roof", "roof_attic"),
                                ("roofRoomUpFloor", "roof")):
            self.assertRegex(
                wall_types,
                r"\b" + slot + r"=[\w.]*\." + bldg.name + "_" + wall_type
                + r"\(\)")

    def test_hom_to_rom_user_profile_weights(self):
        """test fac_room_t_set / fac_room_nat_vent of the HOM archetype"""

        prj = Project()
        prj.name = "BESModHOMtoROMWeights"

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
        bldg = prj.buildings[0]
        rooms = sorted(bldg.room_name_nr, key=bldg.room_name_nr.get)

        # both default to the room volumes, normalized to a weighted average
        total_volume = sum(bldg.room_volumes[room] for room in rooms)
        by_volume = [bldg.room_volumes[room] / total_volume for room in rooms]
        for weights in (bldg.fac_room_t_set, bldg.fac_room_nat_vent):
            self.assertEqual(len(weights), len(bldg.room_name_nr))
            self.assertAlmostEqual(sum(weights), 1.0)
            for weight, expected in zip(weights, by_volume):
                self.assertAlmostEqual(weight, expected)

        # weighting the room setpoints by volume has to give the same value
        # as aggregating them with t_set_nominal_aggregation does, i.e. the
        # weights really form a weighted average of the profiles
        weighted = sum(fac * t_set for fac, t_set
                       in zip(bldg.fac_room_t_set, bldg.room_t_set_nominal_list))
        bldg.t_set_nominal_aggregation = "volume_weighted_average"
        self.assertAlmostEqual(weighted, bldg.thermal_zones[0].t_inside)
        bldg.t_set_nominal_aggregation = "max"

        # the two weightings are independent of each other
        bldg.fac_room_t_set_weighting = "heat_load"
        total_heat_load = sum(bldg.room_heat_loads[room] for room in rooms)
        for weight, room in zip(bldg.fac_room_t_set, rooms):
            self.assertAlmostEqual(
                weight, bldg.room_heat_loads[room] / total_heat_load)
        for weight, expected in zip(bldg.fac_room_nat_vent, by_volume):
            self.assertAlmostEqual(weight, expected)

        bldg.fac_room_t_set_weighting = "equal"
        for weight in bldg.fac_room_t_set:
            self.assertAlmostEqual(weight, 1 / len(bldg.room_name_nr))

        # a dict and a callable give full control, and are normalized too
        bldg.fac_room_t_set_weighting = {
            room: (2.0 if room == "Bath" else 1.0) for room in rooms}
        self.assertAlmostEqual(sum(bldg.fac_room_t_set), 1.0)
        self.assertAlmostEqual(
            bldg.fac_room_t_set[bldg.room_name_nr["Bath"] - 1], 2 / 11)
        bldg.fac_room_nat_vent_weighting = lambda b: b.room_volumes
        for weight, expected in zip(bldg.fac_room_nat_vent, by_volume):
            self.assertAlmostEqual(weight, expected)

        for bad in ("nonsense",
                    {"Bath": 1.0},
                    {room: 0.0 for room in rooms},
                    dict({room: 1.0 for room in rooms}, Bath=-1.0)):
            bldg.fac_room_t_set_weighting = bad
            with self.assertRaises(ValueError):
                bldg.fac_room_t_set

        # 'heat_load' needs the room heat loads, which are only populated
        # once the building parameters have been calculated - it has to say
        # so rather than fail somewhere further down
        bldg.fac_room_t_set_weighting = "heat_load"
        bldg.room_heat_loads = {}
        with self.assertRaises(ValueError):
            bldg.fac_room_t_set

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
