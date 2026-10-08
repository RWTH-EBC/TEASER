import os
import re
import tempfile
import unittest

from teaser.project import Project
from teaser.data.output.energyplus_output import IDF_VERSION, export_idf


def _objects(path):
    """The IDF's objects as lists of fields, comments left out"""
    with open(path) as file:
        text = re.sub(r"!.*", "", file.read())
    return [[field.strip() for field in obj.split(",")]
            for obj in text.split(";") if obj.strip()]


class Test_energyplus_output(unittest.TestCase):

    def test_export_idf(self):
        """test the IDF of the HOM archetype for its structure"""
        prj = Project()
        prj.name = "EnergyPlusExport"
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
        bldg.rotate_building(30)

        with tempfile.TemporaryDirectory() as directory:
            path = export_idf(bldg, os.path.join(directory, "hom.idf"),
                              run_period_days=7)
            objects = _objects(path)

        by_kind = {}
        for obj in objects:
            by_kind.setdefault(obj[0], []).append(obj)
        self.assertEqual(by_kind["Version"][0][1], IDF_VERSION)
        self.assertEqual(float(by_kind["Building"][0][2]), 30.0)
        self.assertEqual({zone[1] for zone in by_kind["Zone"]},
                         set(bldg.room_volumes))
        self.assertEqual(len(by_kind["FenestrationSurface:Detailed"]), 13)

        materials = {obj[1] for obj in by_kind["Material"]} | {
            obj[1] for obj in by_kind["WindowMaterial:SimpleGlazingSystem"]}
        constructions = {obj[1]: obj[2:] for obj in by_kind["Construction"]}
        for layers in constructions.values():
            self.assertTrue(set(layers) <= materials)

        surfaces = {obj[1]: obj for obj in by_kind["BuildingSurface:Detailed"]}
        for surface in surfaces.values():
            self.assertIn(surface[3], constructions)
            boundary, partner = surface[6], surface[7]
            if boundary == "Surface":
                # paired back, with the layers in reverse order
                self.assertEqual(surfaces[partner][7], surface[1])
                self.assertEqual(constructions[surfaces[partner][3]],
                                 constructions[surface[3]][::-1])
            # the vertex count matches the coordinates that follow it
            self.assertEqual(int(surface[11]) * 3, len(surface) - 12)
        for window in by_kind["FenestrationSurface:Detailed"]:
            self.assertIn(window[4], surfaces)
            self.assertIn(window[3], constructions)

        # the outer wall, outside first, is TEASER's turned round
        wall = next(e for e in bldg.thermal_zones[0].outer_walls
                    if e.name == "Livingroom_outside_wall1")
        self.assertEqual(
            [layer.split("_")[0] for layer in
             constructions["Livingroom_outside_wall1"]],
            [layer.material.name.split("_")[0] for layer in wall.layer[::-1]])

        # the attic, which EnergyPlus simulates on its own, has its air change
        infiltration = by_kind["ZoneInfiltration:DesignFlowRate"]
        self.assertEqual([obj[2] for obj in infiltration], ["Attic"])
        self.assertEqual(float(infiltration[0][8]), 2.5)

    def test_export_besmod_with_spawn(self):
        """test the Spawn variant of the BESMod export"""
        prj = Project()
        prj.name = "SpawnExport"
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

        with tempfile.TemporaryDirectory() as directory:
            # the weather file is only copied, its content does not matter
            epw = os.path.join(directory, "weather.epw")
            with open(epw, "w") as file:
                file.write("LOCATION")
            with self.assertWarns(UserWarning):
                path = prj.export_besmod(
                    examples=["TEASERHeatLoadCalculation",
                              "GasBoilerBuildingOnly", "HeatPumpMonoenergetic"],
                    THydSup_nominal=328.15, path=os.path.join(directory, "out"),
                    export_with_hom=True, export_with_spawn=True,
                    spawn_epw_path=epw)
            package = os.path.join(path, bldg.name)
            with open(os.path.join(package, "package.order")) as file:
                order = file.read().split()
            for name in (bldg.name + "_Spawn", bldg.name + "_HOM",
                         "TEASERHeatLoadCalculation" + bldg.name + "_Spawn",
                         "GasBoilerBuildingOnly" + bldg.name + "_Spawn",
                         "HeatPumpMonoenergetic" + bldg.name + "_HOM"):
                self.assertIn(name, order)
                self.assertTrue(os.path.isfile(
                    os.path.join(package, name + ".mo")))
            # no Spawn variant of the example with mechanical ventilation
            self.assertNotIn("HeatPumpMonoenergetic" + bldg.name + "_Spawn",
                             order)
            self.assertTrue(os.path.isfile(
                os.path.join(package, bldg.name + "_Spawn.idf")))
            self.assertTrue(os.path.isfile(
                os.path.join(path, "Resources", "weather.epw")))
            with open(os.path.join(package, bldg.name + "_Spawn.mo")) as file:
                model = file.read()
            with open(os.path.join(
                    package, "TEASERHeatLoadCalculation" + bldg.name
                    + "_Spawn.mo")) as file:
                example = file.read()

            # without Spawn, a fresh export has the HOM and nothing of Spawn
            path = prj.export_besmod(
                examples=["TEASERHeatLoadCalculation"], THydSup_nominal=328.15,
                path=os.path.join(directory, "hom_only"), export_with_hom=True)
            files = os.listdir(os.path.join(path, bldg.name))
            self.assertIn(bldg.name + "_HOM.mo", files)
            self.assertFalse([name for name in files if "Spawn" in name])
        self.assertIn("extends BESMod.Systems.Demand.Building.SpawnHighOrder(",
                      model)
        rooms = sorted(bldg.room_name_nr, key=bldg.room_name_nr.get)
        self.assertIn("zoneNames={" + ", ".join(
            f'"{room}"' for room in rooms + ["Attic"]) + "}", model)
        self.assertIn(f"redeclare {bldg.name}_Spawn building", example)


if __name__ == "__main__":
    unittest.main()
