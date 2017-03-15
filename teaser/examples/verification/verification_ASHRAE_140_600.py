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
    roof.orientation = 180.0
    roof.tilt = 0.0
    roof.inner_convection = 3.16
    roof.outer_convection = 24.67
    roof.inner_radiation = 5.13
    roof.outer_radiation = 4.63

    layer_s1 = Layer(parent=roof, id=0)
    layer_s1.thickness = 0.3  #Hier weiter
