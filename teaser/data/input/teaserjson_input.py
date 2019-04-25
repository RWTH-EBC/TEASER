"""TeaserXML_input

This module contains function to load Projects in the proprietary
TEASER file format .tXML
"""

import xml.etree.ElementTree as element_tree
import warnings
from teaser.logic.buildingobjects.building import Building
from teaser.logic.archetypebuildings.bmvbs.office import Office
from teaser.logic.archetypebuildings.bmvbs.singlefamilydwelling import \
    SingleFamilyDwelling
from teaser.logic.archetypebuildings.bmvbs.custom.institute import Institute
from teaser.logic.archetypebuildings.bmvbs.custom.institute4 import Institute4
from teaser.logic.archetypebuildings.bmvbs.custom.institute8 import Institute8
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.buildingsystems.buildingahu import\
    BuildingAHU
from teaser.logic.buildingobjects.useconditions import UseConditions
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.groundfloor import \
    GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.buildingphysics.door import Door


def load_teaser_json(path, prj):
    """This function loads a project from teaserJSON

    TEASERs internal file format to store information.

    Parameters
    ----------
    path: string
        path of teaserXML file

    prj: Project()
        Teaser instance of Project()


    """
    pass
