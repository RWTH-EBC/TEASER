import unittest
from collections import defaultdict

import numpy as np

from teaser.project import Project
from teaser.logic.archetypebuildings.aixlib_high_order.geometry import (
    building_geometry)


def _archetype(net_leased_area=170.0, roof_tilt=45.0):
    prj = Project()
    prj.name = "HOMGeometry"
    prj.add_residential(
        construction_data='aixlib_S',
        geometry_data='aixlib_high_order_single_family_house',
        name="ResidentialBuildingHighOrderAixLib",
        year_of_construction=1990,
        net_leased_area=net_leased_area,
        number_of_floors=2,
        height_of_floors=2.6)
    bldg = prj.buildings[0]
    bldg.roof_tilt = roof_tilt
    return bldg


class Test_hom_geometry(unittest.TestCase):

    def test_matches_inner_geometry(self):
        """test that the 3D rooms have the archetype's areas and volumes"""
        for net_leased_area, roof_tilt in ((170.0, 45.0), (120.0, 30.0),
                                           (250.0, 60.0)):
            bldg = _archetype(net_leased_area, roof_tilt)
            zones = building_geometry(bldg)
            self.assertEqual(set(zones), set(bldg.room_volumes))

            areas = defaultdict(float)
            windows = defaultdict(float)
            for zone in zones.values():
                for surface in zone.surfaces:
                    if surface.element:
                        areas[surface.element] += surface.net_area
                        windows[surface.element] += sum(
                            window.area for window in surface.windows)
            for room, elements in bldg.detailed_geo.items():
                if room == "Attic":
                    continue
                for name, info in elements.items():
                    self.assertAlmostEqual(areas[(room, name)], info["area"])
                    self.assertAlmostEqual(
                        windows[(room, name)],
                        info["windowarea"] if info.get("with_window") else 0)
                self.assertAlmostEqual(zones[room].volume,
                                       bldg.room_volumes[room])
                self.assertAlmostEqual(
                    zones[room].floor_area,
                    bldg.detailed_geo[room]["floor"]["area"])

            # the attic covers the whole length of the rooms below it, one
            # inner wall thickness more than the archetype's roof_length
            geo = bldg.top_level_geo_params
            length = geo["roof_length"] + geo["thickness_iw_simple"]
            self.assertAlmostEqual(zones["Attic"].volume,
                                   bldg.room_volumes["Attic"]
                                   * length / geo["roof_length"])
            for name in ("outside_wall1", "outside_wall2"):
                self.assertAlmostEqual(
                    areas[("Attic", name)],
                    bldg.detailed_geo["Attic"][name]["area"])
            for room, ceiling in (("Bedroom", "floorRoom1"),
                                  ("Children2", "floorRoom5")):
                self.assertAlmostEqual(
                    areas[("Attic", ceiling)],
                    bldg.detailed_geo[room]["ceiling"]["area"])

    def test_closed_and_paired(self):
        """test that the zones are closed and the inner surfaces paired"""
        zones = building_geometry(_archetype())
        surfaces = {s.name: s for z in zones.values() for s in z.surfaces}
        self.assertEqual(len(surfaces),
                         sum(len(z.surfaces) for z in zones.values()))
        for zone in zones.values():
            closure = sum((s.area * s.normal for s in zone.surfaces),
                          np.zeros(3))
            self.assertAlmostEqual(np.linalg.norm(closure), 0)
            self.assertGreater(zone.volume, 0)
        for surface in surfaces.values():
            if surface.boundary != "Surface":
                self.assertIsNone(surface.partner)
                continue
            partner = surfaces[surface.partner]
            self.assertEqual(partner.partner, surface.name)
            self.assertAlmostEqual(partner.area, surface.area)
            self.assertAlmostEqual(np.dot(partner.normal, surface.normal), -1)

    def test_orientation_and_windows(self):
        """test that the envelope faces where the archetype says, and that
        the windows lie in their surfaces"""
        for net_leased_area, roof_tilt in ((170.0, 45.0), (120.0, 30.0),
                                           (250.0, 60.0)):
            bldg = _archetype(net_leased_area, roof_tilt)
            zones = building_geometry(bldg)
            n_windows = 0
            for zone in zones.values():
                for surface in zone.surfaces:
                    n_windows += len(surface.windows)
                    if surface.boundary not in ("Outdoors", "Ground"):
                        continue
                    info = bldg.detailed_geo[surface.element[0]][
                        surface.element[1]]
                    if surface.boundary == "Ground":
                        self.assertEqual(surface.orientation, -2)
                        continue
                    self.assertAlmostEqual(surface.orientation, info["ori"])
                    self.assertAlmostEqual(surface.tilt, info["tilt"])
                    edges = list(zip(surface.vertices,
                                     np.roll(surface.vertices, -1, axis=0)))
                    for window in surface.windows:
                        self.assertAlmostEqual(
                            np.dot(window.normal, surface.normal), 1)
                        for point in window.vertices:
                            self.assertAlmostEqual(
                                np.dot(point - surface.vertices[0],
                                       surface.normal), 0)
                            for a, b in edges:
                                self.assertGreaterEqual(
                                    np.dot(np.cross(b - a, point - a),
                                           surface.normal), -1e-9)
            self.assertEqual(n_windows, 13)


if __name__ == "__main__":
    unittest.main()
