import os
import re
import tempfile
import unittest

import numpy as np

from teaser.project import Project
from teaser.data.output.energyplus_output import export_idf
from teaser.logic.archetypebuildings.detailed_mfh.geometry import (
    Plan, building_geometry, flat_area, scale_plan)
from teaser.logic.archetypebuildings.detailed_mfh.multifamilyhouse import (
    _u_value)


def _mfh(prj=None, **kwargs):
    prj = prj or Project()
    arguments = dict(
        construction_data="detailed_mfh_standard",
        geometry_data="detailed_multi_family_house",
        name="MFH",
        year_of_construction=1990,
        number_of_floors=5,
        height_of_floors=2.5,
        net_leased_area=None,
    )
    arguments.update(kwargs)
    return prj.add_residential(**arguments)


def _surfaces(geometry):
    return {surface.name: (zone.name, surface)
            for zone in geometry.zones.values() for surface in zone.surfaces}


class TestDetailedMFHGeometry(unittest.TestCase):

    def test_plan_as_drawn(self):
        """the rooms of Kühn/Nikolowski's plan and its outer dimensions"""
        geometry = building_geometry()
        self.assertAlmostEqual(geometry.length, 17.0)
        self.assertAlmostEqual(geometry.depth, 10.0)
        self.assertAlmostEqual(flat_area(Plan()), 64.8715)
        areas = {info.room_type: geometry.zones[name].floor_area
                 for name, info in geometry.info.items()
                 if info.kind == "room" and info.flat == 1 and info.storey == 0}
        self.assertAlmostEqual(areas["Living"], 4.25 * 4.30)
        self.assertAlmostEqual(areas["Bedroom"], 3.675 * 4.30)
        self.assertAlmostEqual(areas["Children"], 2.62 * (1.66 + 0.17 + 3.06))
        self.assertAlmostEqual(areas["Hallway"], (1.50 + 0.17 + 2.25) * 1.66)
        self.assertAlmostEqual(areas["Bath"], 1.50 * 3.06)
        self.assertAlmostEqual(areas["Kitchen"], 2.25 * 3.06)

    def test_zones(self):
        """rooms, staircases, basement and attic for any size"""
        for floors, staircases in ((1, 1), (5, 1), (3, 2)):
            geometry = building_geometry(Plan(), floors, staircases)
            kinds = [info.kind for info in geometry.info.values()]
            self.assertEqual(kinds.count("room"), 12 * floors * staircases)
            self.assertEqual(kinds.count("staircase"), staircases)
            self.assertEqual(kinds.count("basement"), 1)
            self.assertEqual(kinds.count("attic"), 1)

    def test_closed_and_paired(self):
        """every box zone is closed and every shared surface paired back"""
        geometry = building_geometry(Plan(), 3, 2, neighbours=1)
        for name, info in geometry.info.items():
            if info.box is None:
                continue
            x0, x1, y0, y1, z0, z1 = info.box
            self.assertAlmostEqual(geometry.zones[name].volume,
                                   (x1 - x0) * (y1 - y0) * (z1 - z0))
        surfaces = _surfaces(geometry)
        for name, (zone, surface) in surfaces.items():
            if surface.boundary != "Surface":
                continue
            partner_zone, partner = surfaces[surface.partner]
            self.assertEqual(partner.partner, name)
            self.assertEqual(partner_zone, surface.element[1])
            self.assertAlmostEqual(partner.area, surface.area)
            self.assertAlmostEqual(float(np.dot(partner.normal, surface.normal)),
                                   -1.0)
        # the staircase spans all storeys and adjoins rooms on each
        staircase = geometry.zones["Staircase1"]
        storeys = {geometry.info[s.element[1]].storey
                   for s in staircase.surfaces
                   if s.boundary == "Surface"
                   and geometry.info[s.element[1]].kind == "room"}
        self.assertEqual(storeys, {0, 1, 2})

    def test_windows(self):
        """the windows of each flat and of the staircase"""
        geometry = building_geometry(Plan(), 2, 1)
        window_area = {}
        for name, info in geometry.info.items():
            area = sum(w.area for s in geometry.zones[name].surfaces
                       for w in s.windows)
            key = (info.kind, info.flat, info.storey)
            window_area[key] = window_area.get(key, 0.0) + area
        for flat in (1, 2):
            self.assertAlmostEqual(window_area[("room", flat, 1)], 10.671875)
        self.assertAlmostEqual(window_area[("staircase", None, None)],
                               2 * 1.875 * 1.25)

    def test_neighbours(self):
        """adjoining buildings make the gable walls adiabatic"""
        for neighbours, west, east in ((0, "Outdoors", "Outdoors"),
                                       (1, "Adiabatic", "Outdoors"),
                                       (2, "Adiabatic", "Adiabatic")):
            geometry = building_geometry(Plan(), 1, 1, neighbours=neighbours)
            boundaries = {(s.name.split("_")[-1], s.boundary)
                          for zone in ("F0_A1_Living", "F0_A2_Living", "Attic")
                          for s in geometry.zones[zone].surfaces
                          if s.name.endswith(("_W", "_E"))}
            self.assertIn(("W", west), boundaries)
            self.assertIn(("E", east), boundaries)

    def test_scaling(self):
        """the plan scales to a flat's area, with or without the depth"""
        for scaling in ("length", "proportional"):
            plan = scale_plan(Plan(), 77.0, scaling)
            self.assertAlmostEqual(flat_area(plan), 77.0)
            self.assertAlmostEqual(plan.inner_depth == Plan().inner_depth,
                                   scaling == "length")
        with self.assertRaises(ValueError):
            scale_plan(Plan(), 77.0, "unknown")


class TestDetailedMFH(unittest.TestCase):

    def test_areas(self):
        """the flats are scaled to net_leased_area_per_flat"""
        bldg = _mfh(net_leased_area_per_flat=70.0, number_of_staircases=2,
                    number_of_floors=3)
        self.assertAlmostEqual(bldg.net_leased_area, 12 * 70.0)
        self.assertAlmostEqual(sum(z.area for z in bldg.thermal_zones),
                               12 * 70.0)
        bldg = _mfh(net_leased_area=650.0)
        self.assertAlmostEqual(bldg.net_leased_area, 650.0)

    def test_zoning(self):
        """one zone or one per flat, with the same heat load"""
        bldg = _mfh()
        self.assertEqual(len(bldg.thermal_zones), 1)
        heat_load = bldg.sum_heat_load
        bldg.zoning = "flat"
        bldg.generate_archetype()
        bldg.calc_building_parameter()
        self.assertEqual(len(bldg.thermal_zones), 10)
        self.assertAlmostEqual(bldg.sum_heat_load, heat_load, delta=1e-6)
        bldg.zoning = lambda info: f"Storey{info.storey}"
        bldg.generate_archetype()
        self.assertEqual(len(bldg.thermal_zones), 5)
        bldg.zoning = "unknown"
        with self.assertRaises(ValueError):
            bldg.generate_archetype()

    def test_halves(self):
        """the walls and slabs between heated rooms are halved"""
        bldg = _mfh(number_of_floors=2)
        zone = bldg.thermal_zones[0]
        full = sum(layer.thickness for layer in bldg._load("Ceiling").layer)
        for element in zone.ceilings + zone.floors:
            self.assertAlmostEqual(
                sum(layer.thickness for layer in element.layer), full / 2)

    def test_temperature_factors(self):
        """the stand-ins carry the heat balance of the unheated spaces"""
        bldg = _mfh()
        for (room, space), factor in bldg.temperature_factors.items():
            self.assertTrue(0 < factor < 1)
        temperatures = bldg.unheated_temperatures
        self.assertTrue(temperatures["Attic"] < temperatures["Basement"]
                        < temperatures["Staircase1"] < 293.15)
        zone = bldg.thermal_zones[0]
        stand_ins = {e.name: e for e in zone.rooftops}
        for (room, space, spec), element in bldg.interface_elements.items():
            stand_in = stand_ins[element.name]
            self.assertAlmostEqual(
                _u_value(stand_in, "Outdoors"),
                bldg.temperature_factors[(room, space)]
                * _u_value(element, "Inside"))
            self.assertEqual(stand_in.layer[-1].material.solar_absorp, 0.0)

    def test_years(self):
        """the three archetypes' constructions, and none in between"""
        u_values = []
        for year in (1965, 1990, 2025):
            bldg = _mfh(year_of_construction=year)
            wall = bldg.thermal_zones[0].outer_walls[0]
            u_values.append(_u_value(wall, "Outdoors"))
        self.assertTrue(u_values[0] > u_values[1] > u_values[2])
        with self.assertRaises(ValueError):
            _mfh(year_of_construction=2005)

    def test_rotation(self):
        """rotating turns the facades, and is kept on regenerating"""
        bldg = _mfh(number_of_floors=1)
        bldg.rotate_building(90)
        bldg.generate_archetype()
        orientations = {w.orientation for w in bldg.thermal_zones[0].windows}
        self.assertEqual(orientations, {270.0, 90.0})

    def test_export_idf(self):
        """the IDF has every zone, paired surfaces and whole constructions"""
        bldg = _mfh(number_of_floors=2, number_of_staircases=2,
                    neighbour_buildings=1)
        with tempfile.TemporaryDirectory() as directory:
            path = export_idf(bldg, os.path.join(directory, "mfh.idf"))
            with open(path) as file:
                text = re.sub(r"!.*", "", file.read())
        objects = [[field.strip() for field in obj.split(",")]
                   for obj in text.split(";") if obj.strip()]
        by_kind = {}
        for obj in objects:
            by_kind.setdefault(obj[0], []).append(obj)
        self.assertEqual({zone[1] for zone in by_kind["Zone"]},
                         set(bldg.geometry.zones))
        conditioned = {zone[1]: zone[-1] for zone in by_kind["Zone"]}
        self.assertEqual(conditioned["Staircase2"], "No")
        self.assertEqual(conditioned["F1_A4_Kitchen"], "Yes")
        constructions = {obj[1]: obj[2:] for obj in by_kind["Construction"]}
        surfaces = {obj[1]: obj for obj in by_kind["BuildingSurface:Detailed"]}
        for surface in surfaces.values():
            if surface[6] == "Surface":
                partner = surfaces[surface[7]]
                self.assertEqual(partner[7], surface[1])
                self.assertEqual(constructions[partner[3]],
                                 constructions[surface[3]][::-1])
        # a whole slab between two flats, not the zones' halves
        ceiling = surfaces["F0_A1_Living_ceiling_F1_A1_Living"]
        self.assertEqual(len(constructions[ceiling[3]]),
                         len(bldg._load("Ceiling").layer))
        infiltration = {obj[2] for obj in by_kind["ZoneInfiltration:DesignFlowRate"]}
        self.assertEqual(infiltration, {"Staircase1", "Staircase2", "Basement",
                                        "Attic"})

    def test_room_heat_loads(self):
        """the rooms' heat loads add up to the zones'"""
        bldg = _mfh(number_of_floors=2)
        bldg.zoning = "flat"
        bldg.generate_archetype()
        bldg.calc_building_parameter()
        self.assertAlmostEqual(sum(bldg.room_heat_loads_list),
                               bldg.sum_heat_load)
        self.assertEqual(len(bldg.room_heat_loads_list), 24)
        # the bath gives to its colder neighbours
        bath = bldg.room_heat_loads["F0_A1_Bath"]
        bldg.room_t_set_nominal["Bath"] = 293.15
        self.assertGreater(bath, bldg.calc_room_heat_loads()["F0_A1_Bath"])

    def test_export_besmod_with_spawn(self):
        """the ROM and the room-wise Spawn model of the BESMod export"""
        prj = Project()
        prj.name = "MFHExport"
        bldg = _mfh(prj, number_of_floors=2)
        bldg.zoning = "flat"
        bldg.generate_archetype()
        prj.used_library_calc = "AixLib"
        prj.number_of_elements_calc = 4
        prj.calc_all_buildings()
        with tempfile.TemporaryDirectory() as directory:
            epw = os.path.join(directory, "weather.epw")
            with open(epw, "w") as file:
                file.write("LOCATION")
            path = prj.export_besmod(
                examples=["TEASERHeatLoadCalculation", "HeatPumpSimple",
                          "GasBoilerBuildingOnly"],
                THydSup_nominal=328.15, path=os.path.join(directory, "out"),
                export_with_spawn=True, spawn_epw_path=epw)
            package = os.path.join(path, bldg.name)
            with open(os.path.join(package, "package.order")) as file:
                order = file.read().split()
            for name in (bldg.name, bldg.name + "_Spawn",
                         "TEASERHeatLoadCalculation" + bldg.name,
                         "HeatPumpSimple" + bldg.name + "_Spawn",
                         "GasBoilerBuildingOnly" + bldg.name + "_Spawn"):
                self.assertIn(name, order)
            files = {}
            for name in (bldg.name + ".mo", bldg.name + "_Spawn.mo",
                         "HeatPumpSimple" + bldg.name + "_Spawn.mo",
                         "TSet_" + bldg.name + "_Rooms.txt",
                         "InternalGains_" + bldg.name + "_Rooms.txt"):
                with open(os.path.join(package, name)) as file:
                    files[name] = file.read()
            self.assertTrue(os.path.isfile(
                os.path.join(package, bldg.name + "_Spawn.idf")))
        rooms = bldg.geometry.heated_rooms
        self.assertIn("nZones=4)", files[bldg.name + ".mo"])
        spawn = files[bldg.name + "_Spawn.mo"]
        self.assertIn("extends BESMod.Systems.Demand.Building.SpawnMultiZone(",
                      spawn)
        self.assertIn("zoneNames={" + ", ".join(f'"{room}"' for room in rooms)
                      + "}", spawn)
        example = files["HeatPumpSimple" + bldg.name + "_Spawn.mo"]
        self.assertIn("redeclare BESMod.Systems.UserProfiles.RoomWiseProfiles "
                      "userProfiles(", example)
        self.assertIn(f"nZones={len(rooms)},", example)
        t_set = files["TSet_" + bldg.name + "_Rooms.txt"].splitlines()
        self.assertEqual(t_set[1], f"double TZoneSet(25, {len(rooms) + 1})")
        self.assertEqual(len(t_set), 2 + 25)
        bath = rooms.index("F0_A1_Bath")
        self.assertEqual(float(t_set[2].split("\t")[1 + bath]), 297.15)
        gains = files["InternalGains_" + bldg.name + "_Rooms.txt"].splitlines()
        self.assertEqual(len(gains[2].split("\t")), len(rooms) + 1)


if __name__ == "__main__":
    unittest.main()
