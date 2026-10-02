import math
import os
import re
import unittest
from teaser.logic import utilities
from teaser.project import Project
from teaser.data.output.besmod_output import (_convert_heating_profile,
                                               _to_aixlib_azimuth)


def _read_wall_record(path):
    """Return {'n': int, 'd': [float], 'rho': [...], ...} of a wall record."""
    with open(path) as record_file:
        content = record_file.read()
    record = {"n": int(re.search(r"n=(\d+)", content).group(1))}
    for name in ("d", "rho", "lambda", "c"):
        values = re.search(name + r"=\{([^}]*)\}", content).group(1)
        record[name] = [float(value) for value in values.split(",")]
    return record


def _read_surface_orientation_record(path):
    """Return {'nSurfaces': int, 'name': [str], 'Azimut': [float], 'Tilt': [float]}"""
    with open(path) as record_file:
        content = record_file.read()
    record = {"nSurfaces": int(re.search(r"nSurfaces=(\d+)", content).group(1))}
    record["name"] = re.findall(
        r'"([^"]*)"', re.search(r"name=\{([^}]*)\}", content).group(1))
    for name in ("Azimut", "Tilt"):
        values = re.search(name + r"=\{([^}]*)\}", content).group(1)
        record[name] = [float(value) for value in values.split(",")]
    return record


def _read_record_matrix(content, name):
    """Return a {{...},{...}} Modelica matrix of a record as [[float]]"""
    line = re.search(name + r"\s*=\s*(.+)\n", content).group(1)
    return [[float(value) for value in row.split(",")]
            for row in re.findall(r"\{([^{}]*)\}", line)]


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

        # the set temperatures default to the room heat loads, the natural
        # ventilation to the room volumes, both normalized to a weighted
        # average
        total_volume = sum(bldg.room_volumes[room] for room in rooms)
        by_volume = [bldg.room_volumes[room] / total_volume for room in rooms]
        total_heat_load = sum(bldg.room_heat_loads[room] for room in rooms)
        by_heat_load = [bldg.room_heat_loads[room] / total_heat_load for room in rooms]
        for weights, expected_weights in ((bldg.fac_room_t_set, by_heat_load),
                                          (bldg.fac_room_nat_vent, by_volume)):
            self.assertEqual(len(weights), len(bldg.room_name_nr))
            self.assertAlmostEqual(sum(weights), 1.0)
            for weight, expected in zip(weights, expected_weights):
                self.assertAlmostEqual(weight, expected)

        # weighting the room setpoints has to give the same value as
        # aggregating them with t_set_nominal_aggregation does, i.e. the
        # weights really form a weighted average of the profiles, and the
        # ROM is designed for the temperature it is operated at
        weighted = sum(fac * t_set for fac, t_set
                       in zip(bldg.fac_room_t_set, bldg.room_t_set_nominal_list))
        self.assertEqual(bldg.t_set_nominal_aggregation, "heat_load_weighted_average")
        self.assertAlmostEqual(weighted, bldg.thermal_zones[0].t_inside)
        self.assertLess(weighted, max(bldg.room_t_set_nominal_list))
        bldg.fac_room_t_set_weighting = "volume"
        weighted = sum(fac * t_set for fac, t_set
                       in zip(bldg.fac_room_t_set, bldg.room_t_set_nominal_list))
        bldg.t_set_nominal_aggregation = "volume_weighted_average"
        self.assertAlmostEqual(weighted, bldg.thermal_zones[0].t_inside)
        bldg.t_set_nominal_aggregation = "max"
        self.assertAlmostEqual(bldg.thermal_zones[0].t_inside,
                               max(bldg.room_t_set_nominal_list))

        # the two weightings are independent of each other
        bldg.fac_room_t_set_weighting = "heat_load"
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

    def test_hom_user_profiles(self):
        """test the room-wise internal gains and set temperatures the HOM and
        the ROM exported next to it are driven with"""

        prj = Project()
        prj.name = "BESModHOMUserProfiles"
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
        path = prj.export_besmod(examples=["TEASERHeatLoadCalculation"],
                                 THydSup_nominal=55 + 273.15,
                                 export_with_hom=True)
        bldg_path = os.path.join(path, bldg.name)

        # the zone's use conditions, per room by its floor area
        use_cond = bldg.thermal_zones[0].use_conditions
        gains = {
            "persons_profile": (use_cond.persons * use_cond.fixed_heat_flow_rate_persons
                                * use_cond.activity_degree_persons,
                                use_cond.ratio_conv_rad_persons),
            "machines_profile": (use_cond.machines, use_cond.ratio_conv_rad_machines),
            "lighting_profile": (use_cond.lighting_power, use_cond.ratio_conv_rad_lighting)}
        floor_area = sum(bldg.detailed_geo[room]["floor"]["area"] for room in rooms)
        energy = {profile: sum(use_cond.schedules[profile]) * value
                  for profile, (value, _) in gains.items()}
        with open(os.path.join(bldg_path, "InternalGains_" + bldg.name + "_HOM.txt")) as gains_file:
            table = [[float(value) for value in line.split()]
                     for line in gains_file.readlines()[2:]]
        self.assertEqual(len(table), 8760)
        self.assertEqual(len(table[0]), len(rooms) + 2)
        self.assertAlmostEqual(sum(sum(row[1:]) for row in table),
                               sum(energy.values()) * floor_area, places=3)
        self.assertEqual(max(row[-1] for row in table), 0.0)
        # spread over the rooms and the hours as their daily courses are
        shape_total = sum(sum(bldg.room_internal_gains_profiles[room]) for room in rooms)
        day = table[:24]
        day_total = sum(sum(row[1:-1]) for row in day)
        for column, room in enumerate(rooms, start=1):
            for row, value in zip(day, bldg.room_internal_gains_profiles[room]):
                self.assertAlmostEqual(row[column], value / shape_total * day_total)

        fac_conv = (sum(energy[profile] * ratio for profile, (_, ratio) in gains.items())
                    / sum(energy.values()))
        with open(os.path.join(bldg_path, "TEASERHeatLoadCalculation" + bldg.name + ".mo")) as rom_file:
            rom = rom_file.read()
        self.assertAlmostEqual(float(re.search(r"fac_conv=([0-9.eE+-]+)", rom).group(1)), fac_conv)
        self.assertIn("gain=1", rom)
        self.assertIn(bldg.name + "_TSetProfile TSetProfile", rom)
        self.assertIn("electrical(transfer(fraHeaRad=0.35))", rom)
        # the ROM is sized for the HOM's room-wise heat loads
        self.assertAlmostEqual(
            float(re.search(r"QBui_flow_nominal=\{([0-9.eE+-]+)\}", rom).group(1)),
            sum(bldg.room_heat_loads.values()))
        with open(os.path.join(bldg_path, bldg.name + "_HOM.mo")) as hom_file:
            self.assertAlmostEqual(
                float(re.search(r"fraRadIntGai=([0-9.eE+-]+)", hom_file.read()).group(1)),
                1 - fac_conv)

        # room_t_set_nominal, set back as the zone's heating profile is
        with open(os.path.join(bldg_path, bldg.name + "_DataBase",
                               bldg.name + "_TSetProfile.mo")) as record_file:
            matrix = re.search(r"Profile=\[(.*)\]", record_file.read(), re.S).group(1)
        profile = [[float(value) for value in row.split(",")]
                   for row in matrix.split(";")]
        set_back = max(use_cond.heating_profile)
        self.assertEqual(len(profile), len(use_cond.heating_profile) + 1)
        for row, heating in zip(profile, use_cond.heating_profile):
            for value, room in zip(row[1:], rooms):
                self.assertAlmostEqual(value, bldg.room_t_set_nominal[room] + heating - set_back)

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

    def test_to_aixlib_azimuth(self):
        """test the TEASER orientation to AixLib azimuth conversion"""

        # AixLib counts from South, East negative, West positive, while
        # TEASER counts clockwise from North
        for orientation, azimuth in ((0.0, 180.0), (90.0, -90.0),
                                     (180.0, 0.0), (270.0, 90.0),
                                     (45.0, -135.0), (359.0, 179.0)):
            self.assertAlmostEqual(_to_aixlib_azimuth(orientation), azimuth)

    def test_rotate_hom(self):
        """test rotating the HOM archetype and its exported surface record"""

        prj = Project()
        prj.name = "BESModHOMRotation"

        prj.add_residential(
            construction_data='aixlib_S',
            geometry_data='aixlib_high_order_single_family_house',
            name="ResidentialBuildingHighOrderAixLib",
            year_of_construction=1990,
            net_leased_area=170.0,
            number_of_floors=2,
            height_of_floors=2.6)

        bldg = prj.buildings[0]
        zone = bldg.thermal_zones[0]
        self.assertEqual(bldg.rotation, 0.0)

        # the six radiation surfaces have to describe the very elements the
        # archetype generates, otherwise the exported record would rotate
        # the HOM's radiation away from its walls and roof halves
        wall_orientations = {orientation for name, orientation, tilt
                             in bldg.surface_orientations if tilt == 90.0}
        roof_surfaces = {(orientation, tilt) for name, orientation, tilt
                         in bldg.surface_orientations if tilt != 90.0}
        self.assertEqual(wall_orientations, {0.0, 90.0, 180.0, 270.0})
        self.assertEqual(
            {wall.orientation for wall in zone.outer_walls}, wall_orientations)
        # left out: the horizontal (-1) stand-ins some methods integrating
        # the Attic give its air change or the ceilings below it
        self.assertEqual(
            {(roof.orientation, roof.tilt) for roof in zone.rooftops
             if roof.orientation != -1},
            roof_surfaces)

        bldg.rotate_building(30)
        self.assertEqual(bldg.rotation, 30.0)
        # every oriented element follows, including the two groups the base
        # Building.rotate_building does not know about: the inner walls and
        # the unheated Attic's own envelope, which belongs to no zone
        for elements in (zone.outer_walls, zone.rooftops, zone.windows,
                         zone.inner_walls):
            self.assertTrue(elements)
            for element in elements:
                if element.orientation == -1:
                    continue  # horizontal, nothing to rotate
                self.assertIn(element.orientation, (30.0, 120.0, 210.0, 300.0))
        attic = bldg.unheated_room_envelope_elements["Attic"]
        self.assertTrue(attic)
        for element in attic.values():
            self.assertIn(element.orientation, (30.0, 120.0, 210.0, 300.0))

        # rotating twice accumulates and wraps around
        bldg.rotate_building(340)
        self.assertEqual(bldg.rotation, 10.0)
        bldg.rotate_building(350)
        self.assertEqual(bldg.rotation, 0.0)
        self.assertEqual({wall.orientation for wall in zone.outer_walls},
                         {0.0, 90.0, 180.0, 270.0})

        bldg.rotate_building(30)
        # regenerating the archetype must not snap the building back to the
        # archetype's own orientation
        bldg.integrate_unheated_rooms = {"Attic": "din12831_f1"}
        zone = bldg.thermal_zones[0]
        self.assertEqual(bldg.rotation, 30.0)
        self.assertEqual({wall.orientation for wall in zone.outer_walls},
                         {30.0, 120.0, 210.0, 300.0})

        prj.used_library_calc = "AixLib"
        prj.number_of_elements_calc = 4
        prj.calc_all_buildings()
        path = prj.export_besmod(examples=["TEASERHeatLoadCalculation"],
                                 THydSup_nominal=55 + 273.15,
                                 export_with_hom=True)

        data_base_path = os.path.join(path, bldg.name, bldg.name + "_DataBase")
        record = _read_surface_orientation_record(os.path.join(
            data_base_path, bldg.name + "_SurfaceOrientation.mo"))
        self.assertEqual(record["nSurfaces"], 6)
        # the names stay AixLib's own, they name the radiation port of
        # AixLibHighOrderOFD rather than the compass direction
        self.assertEqual(record["name"],
                         ["N", "O", "S", "W", "Roof_N", "Roof_S"])
        # AixLib's own SurfaceOrientationData_N_E_S_W_RoofN_Roof_S holds
        # {180, -90, 0, 90, 180, 0}, all rotated by the same 30 deg here
        self.assertEqual(record["Azimut"],
                         [-150.0, -60.0, 30.0, 120.0, -150.0, 30.0])
        # the roof halves take the archetype's own roof_tilt, not AixLib's
        # fixed 45 deg - which for the default alfa_grad happens to be 45
        roof_tilt = bldg.top_level_geo_params["roof_tilt"]
        self.assertEqual(record["Tilt"],
                         [90.0, 90.0, 90.0, 90.0, roof_tilt, roof_tilt])

        # the record has to be part of its package and be picked up by the
        # exported HOM model, which is the only way the rotation reaches it
        with open(os.path.join(data_base_path, "package.order")) as order_file:
            self.assertIn(bldg.name + "_SurfaceOrientation",
                          order_file.read().split())
        with open(os.path.join(
                path, bldg.name, bldg.name + "_HOM.mo")) as hom_file:
            self.assertRegex(
                hom_file.read(),
                r"redeclare replaceable parameter\s+[\w.]*\." + bldg.name
                + r"_SurfaceOrientation SOD")

        # the ROM exported next to the HOM is rotated by the very same
        # angle - it follows from rotate_building touching the zone's own
        # elements, which calc_all_buildings then turns into the zone record
        with open(os.path.join(
                data_base_path,
                bldg.name + "_" + zone.name + ".mo")) as zone_file:
            zone_record = zone_file.read()
        azi_roof = [float(value) for value in re.search(
            r"aziRoof = \{([^}]*)\}", zone_record).group(1).split(",")]
        # the ROM's azimuths follow the same convention, in radians. Both
        # roof halves are rotated by the same 30 deg; the third entry is
        # the direction-less equivalent element the din12831_f1 attic
        # integration adds for the Attic above them.
        azi_roof = [round(math.degrees(azimuth), 6) for azimuth in azi_roof]
        self.assertIn(30.0, azi_roof)
        self.assertIn(-150.0, azi_roof)

        # rotating without recalculating afterwards would write a rotated
        # HOM next to a ROM that still holds the old orientations
        self.assertFalse(bldg.rotation_pending_recalculation)
        bldg.rotate_building(15)
        self.assertTrue(bldg.rotation_pending_recalculation)
        with self.assertWarns(UserWarning):
            prj.export_besmod(examples=["TEASERHeatLoadCalculation"],
                              THydSup_nominal=55 + 273.15,
                              export_with_hom=True)
        prj.calc_all_buildings()
        self.assertFalse(bldg.rotation_pending_recalculation)
        bldg.rotate_building(315)
        prj.calc_all_buildings()

        # an unrotated building reproduces AixLib's own record one to one
        self.assertEqual(bldg.rotation, 0.0)
        path = prj.export_besmod(examples=["TEASERHeatLoadCalculation"],
                                 THydSup_nominal=55 + 273.15,
                                 export_with_hom=True)
        record = _read_surface_orientation_record(os.path.join(
            path, bldg.name, bldg.name + "_DataBase",
            bldg.name + "_SurfaceOrientation.mo"))
        self.assertEqual(record["Azimut"], [180.0, -90.0, 0.0, 90.0, 180.0, 0.0])

    def test_hom_rom_inner_heat_transfer_parameters(self):
        """test the room-derived parameters of the single-zone ROM record"""

        prj = Project()
        prj.name = "BESModHOMROMParameters"

        prj.add_residential(
            construction_data='aixlib_S',
            geometry_data='aixlib_high_order_single_family_house',
            name="ResidentialBuildingHighOrderAixLib",
            year_of_construction=1990,
            net_leased_area=170.0,
            number_of_floors=2,
            height_of_floors=2.6)

        bldg = prj.buildings[0]
        prj.used_library_calc = "AixLib"
        prj.number_of_elements_calc = 4
        prj.calc_all_buildings()
        zone = bldg.thermal_zones[0]
        rooms = sorted(bldg.room_name_nr, key=bldg.room_name_nr.get)

        self.assertEqual(zone.number_of_rooms, len(rooms))
        self.assertEqual(zone.room_volumes,
                         [bldg.room_volumes[room] for room in rooms])

        # every oriented element of the zone sits on one of the two floors,
        # so the two shares split the whole area between them
        self.assertAlmostEqual(zone.ratio_ow_area_top_floor
                               + zone.ratio_ow_area_bottom_floor, 1.0)
        self.assertAlmostEqual(zone.ratio_iw_area_top_floor
                               + zone.ratio_iw_area_bottom_floor, 1.0)

        # AixLib's WindowSimple exchanges no long wave radiation indoors,
        # so every window coupling of the ROM has to be switched off
        for ratio in (zone.ratio_win_area_top_floor,
                      zone.ratio_win_area_bottom_floor,
                      zone.ratio_win_area_ow, zone.ratio_win_area_iw):
            self.assertEqual(ratio, 0.0)

        orientations = zone.model_attr.n_outer
        self.assertEqual(len(zone.split_factor_sol_rad), 5)
        for row in zone.split_factor_sol_rad:
            self.assertEqual(len(row), orientations)
            for factor in row:
                self.assertGreaterEqual(factor, 0.0)
        # the radiation entering through one orientation is distributed
        # completely over the five interior surface groups
        for index in range(orientations):
            self.assertAlmostEqual(
                sum(row[index] for row in zone.split_factor_sol_rad), 1.0)

        self.assertEqual(len(zone.win_area_room_factors), orientations)
        for row in zone.win_area_room_factors:
            self.assertEqual(len(row), len(rooms))
            self.assertAlmostEqual(sum(row), 1.0)

        # the elements of the 'din12831_f1' attic are built on the ceiling
        # between the rooms and the Attic, which is the surface the zone
        # sees, so there is nothing left to correct
        bldg.integrate_unheated_rooms = {"Attic": "din12831_f1"}
        prj.calc_all_buildings()
        zone = bldg.thermal_zones[0]
        self.assertAlmostEqual(zone.roof_area_attic_factor, 1.0)

        # 'const_volumes' instead spreads the Attic's own outer area over
        # the zone, so only the part of it standing for the ceiling faces
        # the zone
        bldg.integrate_unheated_rooms = {"Attic": "const_volumes"}
        prj.calc_all_buildings()
        zone = bldg.thermal_zones[0]
        attic = bldg.detailed_geo["Attic"].values()
        attic_outer = sum(info["area"] for info in attic
                          if info["type"] in ("OuterWall", "Roof",
                                              "GroundFloor"))
        attic_inner = sum(info["area"] for info in attic
                          if info["type"] in ("InnerWall", "Ceiling", "Floor"))
        room_roofs = sum(
            element.area for element in zone.rooftops
            if bldg._unheated_room_of_element(element) is None)
        attic_roofs = sum(
            element.area for element in zone.rooftops
            if bldg._unheated_room_of_element(element) is not None)
        expected = ((room_roofs + attic_roofs * attic_inner / attic_outer)
                    / (room_roofs + attic_roofs))
        self.assertAlmostEqual(zone.roof_area_attic_factor, expected)
        self.assertLess(zone.roof_area_attic_factor, 1.0)

        path = prj.export_besmod(examples=["TEASERHeatLoadCalculation"],
                                 THydSup_nominal=55 + 273.15)

        with open(os.path.join(path, bldg.name, bldg.name + ".mo")) as model:
            self.assertIn(
                "BESMod.Systems.Demand.Building.TEASERThermalSingleZone",
                model.read())
        record_path = os.path.join(path, bldg.name, bldg.name + "_DataBase",
                                   bldg.name + "_" + zone.name + ".mo")
        with open(record_path) as record_file:
            record = record_file.read()
        self.assertIn(
            "BESMod.Systems.Demand.Building.RecordsCollection."
            "BuildingSingleZoneBaseRecord", record)
        # nFloorLevels and nRooms are Modelica Integers, and a numpy scalar
        # would render as "np.float64(0.5)" instead of a plain number
        self.assertRegex(record, r"nFloorLevels = 2,")
        self.assertRegex(record, r"nRooms = " + str(len(rooms)) + ",")
        self.assertNotIn("np.float", record)
        split_factors = _read_record_matrix(record, "splitFactorSolRad")
        self.assertEqual(len(split_factors), 5)
        for row, expected_row in zip(split_factors, zone.split_factor_sol_rad):
            for factor, expected_factor in zip(row, expected_row):
                self.assertAlmostEqual(factor, expected_factor)
        transparent = _read_record_matrix(record, "FacATransparentPerRoom")
        self.assertEqual(len(transparent), zone.model_attr.n_outer)
        self.assertEqual(len(transparent[0]), len(rooms))

        # use_old falls back to the model and the record the export used
        # before, which have none of these parameters
        bldg.use_old = True
        path = prj.export_besmod(examples=["TEASERHeatLoadCalculation"],
                                 THydSup_nominal=55 + 273.15)
        with open(os.path.join(path, bldg.name, bldg.name + ".mo")) as model:
            self.assertIn("BESMod.Systems.Demand.Building.TEASERThermalZone(",
                          model.read())
        with open(record_path) as record_file:
            record = record_file.read()
        self.assertIn("AixLib.DataBase.ThermalZones.ZoneBaseRecord", record)
        self.assertNotIn("splitFactorSolRad", record)

    def test_hom_surface_coefficients(self):
        """test the ROM's outer surface coefficients set up like the HOM's"""

        def calculated_building(**attributes):
            prj = Project()
            prj.name = "BESModHOMSurfaceCoefficients"
            prj.add_residential(
                construction_data='aixlib_S',
                geometry_data='aixlib_high_order_single_family_house',
                name="ResidentialBuildingHighOrderAixLib",
                year_of_construction=2005,
                net_leased_area=170.0,
                number_of_floors=2,
                height_of_floors=2.6)
            bldg = prj.buildings[0]
            # set after add_residential, which already calculates the
            # building once, as users of the archetype do
            for name, value in attributes.items():
                setattr(bldg, name, value)
            prj.used_library_calc = "AixLib"
            prj.number_of_elements_calc = 4
            prj.calc_all_buildings()
            return bldg

        default = calculated_building()
        zone = default.thermal_zones[0]
        for window in zone.windows:
            self.assertEqual(window.inner_convection, 1e5)
            self.assertEqual(window.outer_convection, 1e5)
            self.assertEqual(window.outer_radiation, 1e-9)
            self.assertEqual(window.a_conv, 0.0)
        for element in zone.outer_walls + zone.rooftops:
            self.assertEqual(element.outer_radiation, 1e-9)
        self.assertAlmostEqual(zone.model_attr.alpha_conv_inner_win, 1e5)

        # the ROM's own coefficients for use_old, or when switched off
        for attributes in ({"use_old": True},
                           {"hom_surface_coefficients": False}):
            bldg = calculated_building(**attributes)
            for window in bldg.thermal_zones[0].windows:
                self.assertEqual(window.inner_convection, 2.7)
                self.assertEqual(window.outer_radiation, 5.0)
            for element in (bldg.thermal_zones[0].outer_walls
                            + bldg.thermal_zones[0].rooftops):
                self.assertEqual(element.outer_radiation, 5.0)
            # the windows keep their U-value, and so the Uw of the HOM
            for window, window_hom_like in zip(bldg.thermal_zones[0].windows,
                                               zone.windows):
                self.assertAlmostEqual(window.u_value, window_hom_like.u_value)

        # and forced on for use_old
        bldg = calculated_building(use_old=True, hom_surface_coefficients=True)
        self.assertEqual(bldg.thermal_zones[0].windows[0].inner_convection, 1e5)

    def test_din12831_f1_from_attic_heat_balance(self):
        """test the Attic's f1 of the din12831_f1 method"""

        prj = Project()
        prj.name = "BESModDIN12831Attic"
        prj.add_residential(
            construction_data='aixlib_S',
            geometry_data='aixlib_high_order_single_family_house',
            name="ResidentialBuildingHighOrderAixLib",
            year_of_construction=1990,
            net_leased_area=170.0,
            number_of_floors=2,
            height_of_floors=2.6)
        bldg = prj.buildings[0]
        bldg.hom_surface_coefficients = False
        bldg.integrate_unheated_rooms = {"Attic": "din12831_f1"}
        bldg.attic_air_change_rate = 1.0
        prj.used_library_calc = "AixLib"
        prj.number_of_elements_calc = 4
        prj.calc_all_buildings()

        # the whole ceiling to the Attic, both of its halves
        ceiling, layers, r_attic = bldg._ceiling_to_unheated_room(
            bldg.detailed_geo["Bedroom"]["ceiling"])
        self.assertEqual(len(layers), 5)
        u_iu = 1 / (1 / (ceiling.inner_convection + ceiling.inner_radiation)
                    + sum(layer.thickness / layer.material.thermal_conduc
                          for layer in layers)
                    + r_attic)

        stand_ins = [element for element in bldg.thermal_zones[0].rooftops
                     if "_Attic_" in element.name]
        self.assertEqual(len(stand_ins), 5)
        h_iu = sum(element.area for element in stand_ins) * u_iu
        h_ue = 0.0
        for element in bldg.unheated_room_envelope_elements["Attic"].values():
            element.calc_ua_value()
            h_ue += element.ua_value
        h_ve = 0.34 * 1.0 * bldg.room_volumes["Attic"]
        f1 = (h_ue + h_ve) / (h_iu + h_ue + h_ve)
        for element in stand_ins:
            self.assertAlmostEqual(element.u_value, f1 * u_iu)

    def test_const_volumes_whole_attic_ceiling(self):
        """test that const_volumes takes the whole ceiling to the Attic"""

        prj = Project()
        prj.name = "BESModConstVolumesAttic"
        prj.add_residential(
            construction_data='aixlib_S',
            geometry_data='aixlib_high_order_single_family_house',
            name="ResidentialBuildingHighOrderAixLib",
            year_of_construction=1990,
            net_leased_area=170.0,
            number_of_floors=2,
            height_of_floors=2.6)
        bldg = prj.buildings[0]
        bldg.integrate_unheated_rooms = {"Attic": "const_volumes"}
        _, layers, _ = bldg._ceiling_to_unheated_room(
            bldg.detailed_geo["Bedroom"]["ceiling"])
        roof = bldg.unheated_room_envelope_elements["Attic"]["roof1"]
        stand_in = next(element for element in bldg.thermal_zones[0].rooftops
                        if element.name == "Bedroom_Attic_roof1")
        # both halves of the ceiling, the Attic's air, then its roof
        self.assertEqual(len(stand_in.layer),
                         len(layers) + 1 + len(roof.layer))
        for layer, ceiling_layer in zip(stand_in.layer, layers):
            self.assertEqual(layer.material.name, ceiling_layer.material.name)

    def test_const_volumes_ua_attic_heat_balance(self):
        """test that const_volumes_ua keeps const_volumes' heat capacities
        and carries the Attic's steady-state heat balance, also after a
        retrofit insulated the Attic's roof"""

        def attic_stand_ins(method, retrofit=False):
            prj = Project()
            prj.name = "BESModConstVolumesUA"
            prj.add_residential(
                construction_data='aixlib_S',
                geometry_data='aixlib_high_order_single_family_house',
                name="ResidentialBuildingHighOrderAixLib",
                year_of_construction=1990,
                net_leased_area=170.0,
                number_of_floors=2,
                height_of_floors=2.6)
            bldg = prj.buildings[0]
            bldg.hom_surface_coefficients = False
            bldg.integrate_unheated_rooms = {"Attic": method}
            if retrofit:
                prj.retrofit_all_buildings(
                    year_of_retrofit=2015,
                    type_of_retrofit="adv_retrofit",
                    window_type='Alu- oder Stahlfenster, Isolierverglasung',
                    material='EPS_perimeter_insulation_top_layer')
            prj.used_library_calc = "AixLib"
            prj.number_of_elements_calc = 4
            prj.calc_all_buildings()
            zone = bldg.thermal_zones[0]
            return bldg, [element for element in zone.outer_walls + zone.rooftops
                          if "_Attic_" in element.name]

        def heat_capacity(elements):
            return sum(layer.thickness * element.area * layer.material.density
                       * layer.material.heat_capac
                       for element in elements for layer in element.layer)

        for retrofit in (False, True):
            bldg, plain = attic_stand_ins("const_volumes", retrofit)
            bldg, fitted = attic_stand_ins("const_volumes_ua", retrofit)
            ceilings = [info for info in bldg.detailed_geo["Attic"].values()
                        if info["type"] == "Floor"]
            # one more stand-in per ceiling, for the Attic's air change
            self.assertEqual(len(fitted), len(plain) + len(ceilings))
            self.assertAlmostEqual(heat_capacity(fitted), heat_capacity(plain))
            self.assertAlmostEqual(
                sum(bldg._indoor_area(element) for element in fitted),
                sum(info["area"] for info in ceilings))

            # the whole ceiling to the Attic in series with its envelope and
            # its air change of attic_infiltration_class "undicht", 2.5 1/h
            ceiling, layers, r_attic = bldg._ceiling_to_unheated_room(
                bldg.detailed_geo["Bedroom"]["ceiling"])
            u_iu = 1 / (1 / (ceiling.inner_convection + ceiling.inner_radiation)
                        + sum(layer.thickness / layer.material.thermal_conduc
                              for layer in layers)
                        + r_attic)
            h_ue = 0.0
            for element in bldg.unheated_room_envelope_elements["Attic"].values():
                element.calc_ua_value()
                h_ue += element.ua_value
            h_ve = 0.34 * 2.5 * bldg.room_volumes["Attic"]
            ua = 1 / (1 / (u_iu * sum(info["area"] for info in ceilings))
                      + 1 / (h_ue + h_ve))
            self.assertAlmostEqual(sum(element.ua_value for element in fitted), ua)

    def test_window_frame_fraction(self):
        """test that the window frame lets no solar radiation into ROM or HOM"""

        for use_old in (False, True):
            prj = Project()
            prj.name = "BESModWindowFrame"
            prj.add_residential(
                construction_data='aixlib_S',
                geometry_data='aixlib_high_order_single_family_house',
                name="ResidentialBuildingHighOrderAixLib",
                year_of_construction=1990,
                net_leased_area=170.0,
                number_of_floors=2,
                height_of_floors=2.6)
            bldg = prj.buildings[0]
            bldg.use_old = use_old
            prj.used_library_calc = "AixLib"
            prj.number_of_elements_calc = 4
            prj.calc_all_buildings()
            zone = bldg.thermal_zones[0]

            # AixLib's own window records have a frame share of 0.2
            for window in zone.windows:
                self.assertEqual(window.frame_fraction, 0.2)
            # the frame conducts heat, so it stays in AWin, but lets no
            # solar radiation through, so it is left out of ATransparent
            for window_area, transparent_area in zip(
                    zone.model_attr.window_areas,
                    zone.model_attr.transparent_areas):
                self.assertAlmostEqual(transparent_area, 0.8 * window_area)

            path = prj.export_besmod(examples=["TEASERHeatLoadCalculation"],
                                     THydSup_nominal=55 + 273.15,
                                     export_with_hom=True)
            database = os.path.join(path, bldg.name, bldg.name + "_DataBase")
            with open(os.path.join(database,
                                   bldg.name + "_" + zone.name + ".mo")) as record_file:
                record = record_file.read()
            for name, areas in (("AWin", zone.model_attr.window_areas),
                                ("ATransparent", zone.model_attr.transparent_areas)):
                values = re.search(r"\b" + name + r"\s*=\s*\{([^}]*)\}", record).group(1)
                for value, area in zip(values.split(","), areas):
                    self.assertAlmostEqual(float(value), area)
            with open(os.path.join(database, "Walls",
                                   bldg.name + "_windowSimple.mo")) as record_file:
                self.assertIn("frameFraction=0.2,", record_file.read())

    def test_single_zone_record_without_room_resolution(self):
        """test the single-zone ROM record of a plain ROM archetype"""

        prj = Project()
        prj.name = "BESModSingleZoneDefaults"

        prj.add_residential(
            construction_data='iwu_heavy',
            geometry_data='iwu_single_family_dwelling',
            name="ResidentialBuilding",
            year_of_construction=1988,
            number_of_floors=2,
            height_of_floors=3.2,
            net_leased_area=200.0)

        prj.used_library_calc = "AixLib"
        prj.number_of_elements_calc = 4
        prj.calc_all_buildings()
        bldg = prj.buildings[0]
        zone = bldg.thermal_zones[0]

        # a zone without a room resolution is its own single room
        self.assertEqual(zone.number_of_rooms, 1)
        self.assertEqual(zone.room_volumes, [zone.volume])
        self.assertEqual(zone.win_area_room_factors,
                         [[1.0]] * zone.model_attr.n_outer)
        self.assertIsNone(zone.split_factor_sol_rad)

        path = prj.export_besmod(examples=["TEASERHeatLoadCalculation"],
                                 THydSup_nominal=55 + 273.15)
        with open(os.path.join(path, bldg.name, bldg.name + "_DataBase",
                               bldg.name + "_" + zone.name + ".mo")) as record_file:
            record = record_file.read()
        self.assertIn("nRooms = 1,", record)
        transparent = _read_record_matrix(record, "FacATransparentPerRoom")
        # FacATransparentPerRoom is declared [nOrientations, nRooms]
        self.assertEqual(len(transparent), zone.model_attr.n_outer)
        self.assertEqual(len(transparent[0]), 1)
        # left out, so the record keeps AixLib's own whole-zone area split
        self.assertNotIn("splitFactorSolRad", record)
