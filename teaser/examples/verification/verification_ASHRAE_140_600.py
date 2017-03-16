# Created March 2017
# TEASER Development Team

"""
This script contains of three functions. The first one loads the light-weight
ASHRAE 140 test room 600 from a *.teaserXML file. The second one creates
that room within the code. The third one computes parameter with the help of
one of the aforementioned functions.
"""

from teaser.project import Project
from teaser.logic.buildingobjects.building import Building
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
import teaser.logic.utilities as utilities


def from_scratch():

    prj = Project(load_data=True)
    prj.name = "ASHRAE140Verification"

    bldg = Building(parent=prj)
    bldg.name = "TestBuilding"

    tz = ThermalZone(parent=bldg)
    tz.name = "TestRoom600"
    tz.area = 8.0 * 6.0
    tz.volume = tz.area * 2.7
    tz.infiltration_rate = 0.41  # Check again with Peter

    # Let's see if it makes sense for completeness to define boundary
    # conditions here. They won't be exported when using only the Annex60
    # thermal zone model.

    # from teaser.logic.buildingobjects.boundaryconditions.boundaryconditions \
    #     import BoundaryConditions
    #
    # tz.use_conditions = BoundaryConditions(parent=tz)
    # tz.use_conditions.load_use_conditions("Living", prj.data)

    roof = Rooftop(parent=tz)
    roof.name = "Roof"
    roof.area = 8.0 * 6.0
    roof.orientation = -1.0
    roof.tilt = 0.0
    roof.inner_convection = 3.16
    roof.outer_convection = 24.67
    roof.inner_radiation = 5.13
    roof.outer_radiation = 4.63

    layer_r1 = Layer(parent=roof, id=0)
    layer_r1.thickness = 0.01

    material_r1 = Material(layer_r1)
    material_r1.name = "Plasterboard"
    material_r1.density = 950.0  # Check with Peter if correct unit
    material_r1.heat_capac = 840.0  # Check with Peter if correct unit
    material_r1.thermal_conduc = 0.16

    layer_r2 = Layer(parent=roof, id=1)
    layer_r2.thickness = 0.112

    material_r2 = Material(layer_r2)
    material_r2.name = "Fiberglass"
    material_r2.density = 12
    material_r2.heat_capac = 840
    material_r2.thermal_conduc = 0.04

    layer_r3 = Layer(parent=roof, id=2)
    layer_r3.thickness = 0.019

    material_r3 = Material(layer_r3)
    material_r3.name = "Roofdeck"
    material_r3.density = 530
    material_r3.heat_capac = 900
    material_r3.thermal_conduc = 0.14
    material_r3.solar_absorp = 0.6  # Check with Peter if this is
    # absorption doefficient


    # Peter: Is it possible to reuse material definition? If so, how?

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
    material_own1.density = 950.0  # Check with Peter if correct unit
    material_own1.heat_capac = 840.0  # Check with Peter if correct unit
    material_own1.thermal_conduc = 0.16

    layer_own2 = Layer(parent=out_wall_north, id=1)
    layer_own2.thickness = 0.066

    material_own2 = Material(layer_own2)
    material_own2.name = "Fiberglass"
    material_own2.density = 12
    material_own2.heat_capac = 840
    material_own2.thermal_conduc = 0.04

    layer_own3 = Layer(parent=out_wall_north, id=2)
    layer_own3.thickness = 0.009

    material_own3 = Material(layer_own3)
    material_own3.name = "WoodSiding"
    material_own3.density = 530
    material_own3.heat_capac = 900
    material_own3.thermal_conduc = 0.14
    material_own3.solar_absorp = 0.6  # Check with Peter if this is
    # absorption doefficient

    out_wall_east = OuterWall(parent=tz)
    out_wall_east.name = "OuterWallEast"
    out_wall_east.area = 6.0 * 2.7
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
    material_owe1.density = 950.0  # Check with Peter if correct unit
    material_owe1.heat_capac = 840.0  # Check with Peter if correct unit
    material_owe1.thermal_conduc = 0.16

    layer_owe2 = Layer(parent=out_wall_east, id=1)
    layer_owe2.thickness = 0.066

    material_owe2 = Material(layer_owe2)
    material_owe2.name = "Fiberglass"
    material_owe2.density = 12
    material_owe2.heat_capac = 840
    material_owe2.thermal_conduc = 0.04

    layer_owe3 = Layer(parent=out_wall_east, id=2)
    layer_owe3.thickness = 0.009

    material_owe3 = Material(layer_owe3)
    material_owe3.name = "WoodSiding"
    material_owe3.density = 530
    material_owe3.heat_capac = 900
    material_owe3.thermal_conduc = 0.14
    material_owe3.solar_absorp = 0.6  # Check with Peter if this is
    # absorption doefficient

    out_wall_south = OuterWall(parent=tz)
    out_wall_south.name = "OuterWallSouth"
    out_wall_south.area = (8.0 * 2.7) - 2 * (3 * 2)  # minus two windows
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
    material_ows1.density = 950.0  # Check with Peter if correct unit
    material_ows1.heat_capac = 840.0  # Check with Peter if correct unit
    material_ows1.thermal_conduc = 0.16

    layer_ows2 = Layer(parent=out_wall_south, id=1)
    layer_ows2.thickness = 0.066

    material_ows2 = Material(layer_ows2)
    material_ows2.name = "Fiberglass"
    material_ows2.density = 12
    material_ows2.heat_capac = 840
    material_ows2.thermal_conduc = 0.04

    layer_ows3 = Layer(parent=out_wall_south, id=2)
    layer_ows3.thickness = 0.009

    material_ows3 = Material(layer_ows3)
    material_ows3.name = "WoodSiding"
    material_ows3.density = 530
    material_ows3.heat_capac = 900
    material_ows3.thermal_conduc = 0.14
    material_ows3.solar_absorp = 0.6  # Check with Peter if this is
    # absorption doefficient

    out_wall_west = OuterWall(parent=tz)
    out_wall_west.name = "OuterWallWest"
    out_wall_west.area = 6 * 2.7
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
    material_oww1.density = 950.0  # Check with Peter if correct unit
    material_oww1.heat_capac = 840.0  # Check with Peter if correct unit
    material_oww1.thermal_conduc = 0.16

    layer_oww2 = Layer(parent=out_wall_west, id=1)
    layer_oww2.thickness = 0.066

    material_oww2 = Material(layer_oww2)
    material_oww2.name = "Fiberglass"
    material_oww2.density = 12
    material_oww2.heat_capac = 840
    material_oww2.thermal_conduc = 0.04

    layer_oww3 = Layer(parent=out_wall_west, id=2)
    layer_oww3.thickness = 0.009

    material_oww3 = Material(layer_oww3)
    material_oww3.name = "WoodSiding"
    material_oww3.density = 530
    material_oww3.heat_capac = 900
    material_oww3.thermal_conduc = 0.14
    material_oww3.solar_absorp = 0.6  # Check with Peter if this is
    # absorption doefficient

    in_wall_floor = Floor(parent=tz)
    in_wall_floor.name = "InnerWallFloor"
    in_wall_floor.area = 6 * 8
    in_wall_floor.orientation = -2.0
    in_wall_floor.tilt = 0.0
    in_wall_floor.inner_convection = 3.16
    in_wall_floor.inner_radiation = 5.13
