# Created March 2017
# TEASER Development Team

"""
This script contains of three functions. The first one loads the light-weight
ASHRAE 140 test room 620 from a *.teaserXML file. The second one creates
that room within the code. The third one computes parameter with the help of
one of the aforementioned functions.
"""

import os
from teaser.project import Project
from teaser.logic.buildingobjects.building import Building
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.groundfloor import \
    GroundFloor
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.boundaryconditions.boundaryconditions \
    import BoundaryConditions
import teaser.logic.utilities as utilities


def main(number_of_elements=2):

    prj = from_scratch(number_of_elements=number_of_elements, save=False)
    # prj = load_file()

    prj.used_library_calc = 'IBPSA'
    prj.number_of_elements_calc = number_of_elements
    prj.merge_windows_calc = False
    prj.weather_file_path = utilities.get_full_path(
        os.path.join(
            "data",
            "input",
            "inputdata",
            "weatherdata",
            "ASHRAE140.mos"))

    prj.buildings[0].calc_building_parameter(
        number_of_elements=number_of_elements,
        merge_windows=False,
        used_library='IBPSA')

    prj.export_parameters_txt()
    prj.export_ibpsa()


def from_scratch(
        number_of_elements,
        save=False,
        path=utilities.get_default_path()):
    """This function creates the test room from scratch.

    Notes: The standard defines an solar absorption coefficient for interior
    surfaces of 0.6. We do not consider this, but we could by multiplying
    the solar radiation after the window by 0.6.

    Parameters
    ----------
    number_of_elements: int
        Number of elements of model
    path: str (optional)
        Path where Project should be stored as .teaserXML
    save: bool (optional)
        True if Project should be stored as .teaserXML at path

    Returns
    -------

    prj: Project
        Project that contains the building with the test room

    """
    prj = Project(load_data=True)
    prj.name = "ASHRAE140Verification"

    bldg = Building(parent=prj)
    bldg.name = "TestBuilding"

    tz = ThermalZone(parent=bldg)
    tz.name = "TestRoom620"
    tz.area = 8.0 * 6.0
    tz.volume = tz.area * 2.7
    tz.infiltration_rate = 0.41

    tz.use_conditions = BoundaryConditions(parent=tz)

    roof = Rooftop(parent=tz)
    roof.name = "Roof"
    roof.area = 8.0 * 6.0
    roof.orientation = -1.0
    roof.tilt = 0.0
    roof.inner_convection = 1
    roof.outer_convection = 24.67
    roof.inner_radiation = 5.13
    roof.outer_radiation = 4.63

    layer_r1 = Layer(parent=roof, id=0)
    layer_r1.thickness = 0.01

    material_r1 = Material(layer_r1)
    material_r1.name = "Plasterboard"
    material_r1.density = 950.0
    material_r1.heat_capac = 840.0 / 1000
    material_r1.thermal_conduc = 0.16
    material_r1.ir_emissivity = 0.9

    layer_r2 = Layer(parent=roof, id=1)
    layer_r2.thickness = 0.1118

    material_r2 = Material(layer_r2)
    material_r2.name = "Fiberglass"
    material_r2.density = 12
    material_r2.heat_capac = 840 / 1000
    material_r2.thermal_conduc = 0.04

    layer_r3 = Layer(parent=roof, id=2)
    layer_r3.thickness = 0.019

    material_r3 = Material(layer_r3)
    material_r3.name = "Roofdeck"
    material_r3.density = 530
    material_r3.heat_capac = 900 / 1000
    material_r3.thermal_conduc = 0.14
    material_r3.solar_absorp = 0.6
    material_r3.ir_emissivity = 0.9

    out_wall_north = OuterWall(parent=tz)
    out_wall_north.name = "OuterWallNorth"
    out_wall_north.area = 8.0 * 2.7
    out_wall_north.orientation = 0.0
    out_wall_north.tilt = 90.0
    out_wall_north.inner_convection = 3.16
    out_wall_north.outer_convection = 24.67
    out_wall_north.inner_radiation = 5.13
    out_wall_north.outer_radiation = 4.63

    layer_own1 = Layer(parent=out_wall_north, id=0)
    layer_own1.thickness = 0.012

    material_own1 = Material(layer_own1)
    material_own1.name = "Plasterboard"
    material_own1.density = 950.0
    material_own1.heat_capac = 840.0 / 1000
    material_own1.thermal_conduc = 0.16
    material_own1.ir_emissivity = 0.9

    layer_own2 = Layer(parent=out_wall_north, id=1)
    layer_own2.thickness = 0.066

    material_own2 = Material(layer_own2)
    material_own2.name = "Fiberglass"
    material_own2.density = 12
    material_own2.heat_capac = 840 / 1000
    material_own2.thermal_conduc = 0.04

    layer_own3 = Layer(parent=out_wall_north, id=2)
    layer_own3.thickness = 0.009

    material_own3 = Material(layer_own3)
    material_own3.name = "WoodSiding"
    material_own3.density = 530
    material_own3.heat_capac = 900 / 1000
    material_own3.thermal_conduc = 0.14
    material_own3.solar_absorp = 0.6
    material_own3.ir_emissivity = 0.9

    out_wall_east = OuterWall(parent=tz)
    out_wall_east.name = "OuterWallEast"
    out_wall_east.area = 6.0 * 2.7 - 3.0 * 2.0  # minus one window
    out_wall_east.orientation = 90.0
    out_wall_east.tilt = 90.0
    out_wall_east.inner_convection = 3.16
    out_wall_east.outer_convection = 24.67
    out_wall_east.inner_radiation = 5.13
    out_wall_east.outer_radiation = 4.63

    layer_owe1 = Layer(parent=out_wall_east, id=0)
    layer_owe1.thickness = 0.012

    material_owe1 = Material(layer_owe1)
    material_owe1.name = "Plasterboard"
    material_owe1.density = 950.0
    material_owe1.heat_capac = 840.0 / 1000
    material_owe1.thermal_conduc = 0.16
    material_owe1.ir_emissivity = 0.9

    layer_owe2 = Layer(parent=out_wall_east, id=1)
    layer_owe2.thickness = 0.066

    material_owe2 = Material(layer_owe2)
    material_owe2.name = "Fiberglass"
    material_owe2.density = 12
    material_owe2.heat_capac = 840 / 1000
    material_owe2.thermal_conduc = 0.04

    layer_owe3 = Layer(parent=out_wall_east, id=2)
    layer_owe3.thickness = 0.009

    material_owe3 = Material(layer_owe3)
    material_owe3.name = "WoodSiding"
    material_owe3.density = 530
    material_owe3.heat_capac = 900 / 1000
    material_owe3.thermal_conduc = 0.14
    material_owe3.solar_absorp = 0.6
    material_owe3.ir_emissivity = 0.9

    out_wall_south = OuterWall(parent=tz)
    out_wall_south.name = "OuterWallSouth"
    out_wall_south.area = (8.0 * 2.7)
    out_wall_south.orientation = 180.0
    out_wall_south.tilt = 90.0
    out_wall_south.inner_convection = 3.16
    out_wall_south.outer_convection = 24.67
    out_wall_south.inner_radiation = 5.13
    out_wall_south.outer_radiation = 4.63

    layer_ows1 = Layer(parent=out_wall_south, id=0)
    layer_ows1.thickness = 0.012

    material_ows1 = Material(layer_ows1)
    material_ows1.name = "Plasterboard"
    material_ows1.density = 950.0
    material_ows1.heat_capac = 840.0 / 1000
    material_ows1.thermal_conduc = 0.16
    material_ows1.ir_emissivity = 0.9

    layer_ows2 = Layer(parent=out_wall_south, id=1)
    layer_ows2.thickness = 0.066

    material_ows2 = Material(layer_ows2)
    material_ows2.name = "Fiberglass"
    material_ows2.density = 12
    material_ows2.heat_capac = 840 / 1000
    material_ows2.thermal_conduc = 0.04

    layer_ows3 = Layer(parent=out_wall_south, id=2)
    layer_ows3.thickness = 0.009

    material_ows3 = Material(layer_ows3)
    material_ows3.name = "WoodSiding"
    material_ows3.density = 530
    material_ows3.heat_capac = 900 / 1000
    material_ows3.thermal_conduc = 0.14
    material_ows3.solar_absorp = 0.6
    material_ows3.ir_emissivity = 0.9

    out_wall_west = OuterWall(parent=tz)
    out_wall_west.name = "OuterWallWest"
    out_wall_west.area = 6 * 2.7 - 3.0 * 2.0  # minus one window
    out_wall_west.orientation = 270.0
    out_wall_west.tilt = 90.0
    out_wall_west.inner_convection = 3.16
    out_wall_west.outer_convection = 24.67
    out_wall_west.inner_radiation = 5.13
    out_wall_west.outer_radiation = 4.63

    layer_oww1 = Layer(parent=out_wall_west, id=0)
    layer_oww1.thickness = 0.012

    material_oww1 = Material(layer_oww1)
    material_oww1.name = "Plasterboard"
    material_oww1.density = 950.0
    material_oww1.heat_capac = 840.0 / 1000
    material_oww1.thermal_conduc = 0.16
    material_oww1.ir_emissivity = 0.9

    layer_oww2 = Layer(parent=out_wall_west, id=1)
    layer_oww2.thickness = 0.066

    material_oww2 = Material(layer_oww2)
    material_oww2.name = "Fiberglass"
    material_oww2.density = 12
    material_oww2.heat_capac = 840 / 1000
    material_oww2.thermal_conduc = 0.04

    layer_oww3 = Layer(parent=out_wall_west, id=2)
    layer_oww3.thickness = 0.009

    material_oww3 = Material(layer_oww3)
    material_oww3.name = "WoodSiding"
    material_oww3.density = 530
    material_oww3.heat_capac = 900 / 1000
    material_oww3.thermal_conduc = 0.14
    material_oww3.solar_absorp = 0.6
    material_oww3.ir_emissivity = 0.9

    in_wall_floor = Floor(parent=tz)
    in_wall_floor.name = "InnerWallFloor"
    in_wall_floor.area = 6 * 8
    in_wall_floor.orientation = -2.0
    in_wall_floor.tilt = 0.0
    in_wall_floor.inner_convection = 4.13
    in_wall_floor.inner_radiation = 5.13

    layer_iwf1 = Layer(parent=in_wall_floor, id=0)
    layer_iwf1.thickness = 0.025

    material_iwf1 = Material(layer_iwf1)
    material_iwf1.name = "TimberFlooring"
    material_iwf1.density = 650
    material_iwf1.heat_capac = 1200 / 1000
    material_iwf1.thermal_conduc = 0.14
    material_iwf1.ir_emissivity = 0.9

    layer_iwf2 = Layer(parent=in_wall_floor, id=1)
    layer_iwf2.thickness = 1.003

    material_iwf2 = Material(layer_iwf2)
    material_iwf2.name = "Insulation"
    material_iwf2.density = 0.000000000001  # 0.0001, as small as possible
    material_iwf2.heat_capac = 0.000000000001  # 0.0001, as small as possible
    material_iwf2.thermal_conduc = 0.04

    win_1 = Window(parent=tz)
    win_1.name = "WindowWest"
    win_1.area = 3 * 2
    win_1.tilt = 90.0
    win_1.orientation = 270.0
    win_1.inner_convection = 3.16
    win_1.inner_radiation = 5.13
    win_1.outer_convection = 16.37
    win_1.outer_radiation = 4.63
    win_1.g_value = 0.789
    win_1.a_conv = 0.03  # for the given U-value extracted from VDI 6007-2/-3

    win_1_layer = Layer(parent=win_1)
    win_1_layer.id = 1
    win_1_layer.thickness = 0.024

    win_1_material = Material(win_1_layer)
    win_1_material.name = "GlasWindow"
    win_1_material.thermal_conduc = 0.15
    win_1_material.transmittance = 0.907
    win_1_material.ir_emissivity = 0.9

    win_2 = Window(parent=tz)
    win_2.name = "WindowEast"
    win_2.area = 3 * 2
    win_2.tilt = 90.0
    win_2.orientation = 90.0
    win_2.inner_convection = 3.16
    win_2.inner_radiation = 5.13
    win_2.outer_convection = 16.37
    win_2.outer_radiation = 4.63
    win_2.g_value = 0.789
    win_2.a_conv = 0.03  # for the given U-value extracted from VDI 6007-2/-3

    win_2_layer = Layer(parent=win_2)
    win_2_layer.id = 1
    win_2_layer.thickness = 0.024

    win_2_material = Material(win_2_layer)
    win_2_material.name = "GlasWindow"
    win_2_material.thermal_conduc = 0.15
    win_2_material.transmittance = 0.907
    win_2_material.ir_emissivity = 0.9

    #  This is a dummy ground floor to export three and four elements models.
    #  Please set values for floor plate in three element and four element
    #  models to default.

    if number_of_elements >= 3:
        out_wall_gf = GroundFloor(parent=tz)
        out_wall_gf.name = "ExtWallGroundFloor"
        out_wall_gf.area = 6 * 8
        out_wall_gf.orientation = -2.0
        out_wall_gf.tilt = 0.0
        out_wall_gf.inner_convection = 4.13
        out_wall_gf.inner_radiation = 5.13

        layer_ofgw1 = Layer(parent=out_wall_gf, id=0)
        layer_ofgw1.thickness = 1.003

        material_ofgw1 = Material(layer_ofgw1)
        material_ofgw1.name = "Insulation"
        material_ofgw1.density = 0.0001  # as small as possible
        material_ofgw1.heat_capac = 0.0001  # as small as possible
        material_ofgw1.thermal_conduc = 0.04

    if save:
        prj.save_project(file_name='ASHRAE140_620', path=path)

    return prj


def load_file():

    prj = Project(load_data=True)

    prj.load_project(utilities.get_full_path(os.path.join("examples",
                                                          "examplefiles",
                                                          "ASHRAE140_620."
                                                          "teaserXML")))

    return prj


if __name__ == '__main__':
    main()
    print("ASHRAE 620: That's it!")
