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
    roof.area = 48.0
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