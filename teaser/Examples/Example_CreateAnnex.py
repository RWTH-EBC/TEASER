#Created July 2015
#TEASER 4 Development Team
"""
This scripts shows how to create a building from scratch (or arbitrary sources)
calculate parameters for a Modelica model and save this example building in a 
XML based format. The used classes are imported one after another. Of course
you can import all the classes at the beginning.
"""

'''
First we need to import the classes we want to use
'''

from teaser.Logic.BuildingObjects.BoundaryConditions.BoundaryConditions import \
    BoundaryConditions
from teaser.Logic.BuildingObjects.Building import Building
from teaser.Logic.BuildingObjects.BuildingPhysics.GroundFloor import\
    GroundFloor
from teaser.Logic.BuildingObjects.BuildingPhysics.InnerWall import InnerWall
from teaser.Logic.BuildingObjects.BuildingPhysics.Layer import Layer
from teaser.Logic.BuildingObjects.BuildingPhysics.Material import Material
from teaser.Logic.BuildingObjects.BuildingPhysics.OuterWall import OuterWall
from teaser.Logic.BuildingObjects.BuildingPhysics.Rooftop import Rooftop
from teaser.Logic.BuildingObjects.BuildingPhysics.Window import Window
from teaser.Logic.BuildingObjects.BuildingPhysics.Ceiling import Ceiling
from teaser.Logic.BuildingObjects.BuildingPhysics.Floor import Floor
from teaser.Logic.BuildingObjects.ThermalZone import ThermalZone
from teaser.Project import Project


def D1_North():
    '''
    Instantiate a Project class (with load_data set to true), instantiate a 
    Building class, with the project as a parent. This automatically adds the 
    specific building and all its future changes to the project.
    '''
    
    bldg = Building(parent=prj)

    '''Set some building parameters'''

    bldg.name = "D1 North"
    bldg.city = "Annex"
    bldg.year_of_construction = 2014
    bldg.number_of_floors = 1
    bldg.height_of_floors = 2.8

    '''Instantiate a ThermalZone class, with building as parent and set  some 
    parameters of the thermal zone'''

    tz1 = ThermalZone(parent=bldg)
    tz1.name = "Living Room"
    tz1.area = 53.9
    tz1.volume = tz1.area * bldg.number_of_floors * bldg.height_of_floors
    tz1.infiltration_rate = 0.5

    '''Instantiate BoundaryConditions class with thermal zone as parent,
    and load the use conditions for the usage 'Living' '''

    tz1.use_conditions = BoundaryConditions(parent = tz1)
    tz1.use_conditions.load_use_conditions("Living")

    '''We save information of the Outer and Inner walls as well as Windows
    in dicts, the key is the name, while the value is a list (if applicable)
    [year of construciton,
     construction type,
     area,
     tilt,
     orientation]'''

    out_wall_dict = {"Outer Wall 1": [bldg.year_of_construction, 'light_annex',
                                      8.736, 90.0, 0.0],
                     "Outer Wall 2": [bldg.year_of_construction, 'light_annex',
                                      17.516, 90.0, 90.0],
                     "Outer Wall 3": [bldg.year_of_construction, 'light_annex',
                                      27.176, 90.0, 180.0],
                     "Outer Wall 4": [bldg.year_of_construction, 'light_annex',
                                      10.146, 90.0, 270.0]}

    win_dict = {"Window 1": [bldg.year_of_construction, "light_annex",
                            4.8, 90.0, 90.0],
                "Window 2": [bldg.year_of_construction, "light_annex",
                             7.04, 90.0, 180.0],
                "Window 3": [bldg.year_of_construction, "light_annex",
                             4.47, 90.0, 270.0]}

    for key, value in out_wall_dict.items():
        '''instantiate OuterWall class'''
        out_wall = OuterWall(parent=tz1)
        out_wall.name = key
        '''load typical construction, based on year of construction and
        construction type'''
        out_wall.load_type_element(year=value[0],
                                   construction=value[1])
        out_wall.area = value[2]
        out_wall.tilt = value[3]
        out_wall.orientation = value[4]

    for key, value in win_dict.items():
        '''instantiate Window class'''
        win = Window(parent=tz1)
        win.name = key
        win.area = value[2]
        win.tilt = value[3]
        win.orientation = value[4]
        win.load_type_element(year=value[0],
                              construction=value[1])

    '''Define a Rooftop and a Groundfloor, we don't need to set tilt and
    orientation because we take the default values'''

    ground = GroundFloor(parent=tz1)
    ground.name = "Ground floor"
    ground.load_type_element(bldg.year_of_construction, 'light_annex')
    ground.area = 53.9


    ceiling = Ceiling(parent=tz1)
    ceiling.name = "Ceiling"
    ceiling.load_type_element(bldg.year_of_construction, 'light_annex')
    ceiling.area = 53.9

    tz2 = ThermalZone(parent=bldg)
    tz2.name = "Traffic Area"
    tz2.area = 31.3
    tz2.volume = tz2.area * bldg.number_of_floors * bldg.height_of_floors
    tz2.infiltration_rate = 0.5

    '''Instantiate BoundaryConditions class with thermal zone as parent,
    and load the use conditions for the usage 'Living' '''

    tz2.use_conditions = BoundaryConditions(parent = tz2)
    tz2.use_conditions.load_use_conditions("Traffic area")

    '''We save information of the Outer and Inner walls as well as Windows
    in dicts, the key is the name, while the value is a list (if applicable)
    [year of construciton,
     construction type,
     area,
     tilt,
     orientation]'''

    out_wall_dict = {"Outer Wall 1": [bldg.year_of_construction, 'light_annex',
                                      38.912, 90.0, 0.0],
                     "Outer Wall 4": [bldg.year_of_construction, 'light_annex',
                                      7.784, 90.0, 270.0]}

    win_dict = {"Window 1": [bldg.year_of_construction, "light_annex",
                            1.24, 90.0, 90.0]}

    for key, value in out_wall_dict.items():
        '''instantiate OuterWall class'''
        out_wall = OuterWall(parent=tz2)
        out_wall.name = key
        '''load typical construction, based on year of construction and
        construction type'''
        out_wall.load_type_element(year=value[0],
                                   construction=value[1])
        out_wall.area = value[2]
        out_wall.tilt = value[3]
        out_wall.orientation = value[4]

    for key, value in win_dict.items():
        '''instantiate Window class'''
        win = Window(parent=tz2)
        win.name = key
        win.area = value[2]
        win.tilt = value[3]
        win.orientation = value[4]
        win.load_type_element(year=value[0],
                              construction=value[1])

    '''Define a Rooftop and a Groundfloor, we don't need to set tilt and
    orientation because we take the default values'''

    floor = Floor(parent=tz2)
    floor.name = "Floor"
    floor.load_type_element(bldg.year_of_construction, 'light_annex')
    floor.area = 15.1

    roof = Rooftop(parent = tz2)
    roof.name = "Roof"
    roof.load_type_element(bldg.year_of_construction, 'light_annex')
    roof.area = 23.29

    groundFloor = GroundFloor(parent=tz2)
    groundFloor.name = "Ground Floor"
    groundFloor.load_type_element(bldg.year_of_construction, 'light_annex')
    groundFloor.area = 16.2

    ceiling = Ceiling(parent = tz2)
    ceiling.name = "Ceiling"
    ceiling.load_type_element(bldg.year_of_construction, 'light_annex')
    ceiling.area = 16.2

    tz3 = ThermalZone(parent=bldg)
    tz3.name = "Bed Room"
    tz3.area = 48.8
    tz3.volume = tz3.area * bldg.number_of_floors * bldg.height_of_floors
    tz3.infiltration_rate = 0.5

    '''Instantiate BoundaryConditions class with thermal zone as parent,
    and load the use conditions for the usage 'Living' '''

    tz3.use_conditions = BoundaryConditions(parent = tz3)
    tz3.use_conditions.load_use_conditions("Bed room")

    '''We save information of the Outer and Inner walls as well as Windows
    in dicts, the key is the name, while the value is a list (if applicable)
    [year of construciton,
     construction type,
     area,
     tilt,
     orientation]'''

    out_wall_dict = {"Outer Wall 1": [bldg.year_of_construction, 'light_annex',
                                      9.66, 90.0, 0.0],
                     "Outer Wall 2": [bldg.year_of_construction, 'light_annex',
                                      11.648, 90.0, 90.0],
                     "Outer Wall 3": [bldg.year_of_construction, 'light_annex',
                                      30.372, 90.0, 180.0],
                     "Outer Wall 4": [bldg.year_of_construction, 'light_annex',
                                      19, 90.0, 270.0]}

    win_dict = {"Window 1": [bldg.year_of_construction, "light_annex",
                            1.68, 90.0, 90.0],
                "Window 2": [bldg.year_of_construction, "light_annex",
                             4.32, 90.0, 180.0],
                "Window 3": [bldg.year_of_construction, "light_annex",
                             2.7, 90.0, 270.0]}

    for key, value in out_wall_dict.items():
        '''instantiate OuterWall class'''
        out_wall = OuterWall(parent=tz3)
        out_wall.name = key
        '''load typical construction, based on year of construction and
        construction type'''
        out_wall.load_type_element(year=value[0],
                                   construction=value[1])
        out_wall.area = value[2]
        out_wall.tilt = value[3]
        out_wall.orientation = value[4]

    for key, value in win_dict.items():
        '''instantiate Window class'''
        win = Window(parent=tz3)
        win.name = key
        win.area = value[2]
        win.tilt = value[3]
        win.orientation = value[4]
        win.load_type_element(year=value[0],
                              construction=value[1])

    '''Define a Rooftop and a Groundfloor, we don't need to set tilt and
    orientation because we take the default values'''

    floor = Floor(parent=tz3)
    floor.name = "Floor"
    floor.load_type_element(bldg.year_of_construction, 'light_annex')
    floor.area = 48.8

    roof = Rooftop(parent = tz3)
    roof.name = "Roof"
    roof.load_type_element(bldg.year_of_construction, 'light_annex')
    roof.area = 75.26


    tz4 = ThermalZone(parent=bldg)
    tz4.name = "WC and sanitary rooms in non-residential buildings"
    tz4.area = 6
    tz4.volume = tz4.area * bldg.number_of_floors * bldg.height_of_floors
    tz4.infiltration_rate = 0.5

    '''Instantiate BoundaryConditions class with thermal zone as parent,
    and load the use conditions for the usage 'Living' '''

    tz4.use_conditions = BoundaryConditions(parent = tz4)
    tz4.use_conditions.load_use_conditions("WC and sanitary rooms in non-residential buildings")

    '''We save information of the Outer and Inner walls as well as Windows
    in dicts, the key is the name, while the value is a list (if applicable)
    [year of construciton,
     construction type,
     area,
     tilt,
     orientation]'''

    out_wall_dict = {"Outer Wall 1": [bldg.year_of_construction, 'light_annex',
                                      8.96, 90.0, 0.0],
                     "Outer Wall 2": [bldg.year_of_construction, 'light_annex',
                                      8.252, 90.0, 90.0]}

    win_dict = {"Window 1": [bldg.year_of_construction, "light_annex",
                            0.96, 90.0, 90.0]}

    for key, value in out_wall_dict.items():
        '''instantiate OuterWall class'''
        out_wall = OuterWall(parent=tz4)
        out_wall.name = key
        '''load typical construction, based on year of construction and
        construction type'''
        out_wall.load_type_element(year=value[0],
                                   construction=value[1])
        out_wall.area = value[2]
        out_wall.tilt = value[3]
        out_wall.orientation = value[4]

    for key, value in win_dict.items():
        '''instantiate Window class'''
        win = Window(parent=tz4)
        win.name = key
        win.area = value[2]
        win.tilt = value[3]
        win.orientation = value[4]
        win.load_type_element(year=value[0],
                              construction=value[1])

    '''Define a Rooftop and a Groundfloor, we don't need to set tilt and
    orientation because we take the default values'''

    floor = Floor(parent=tz4)
    floor.name = "Floor"
    floor.load_type_element(bldg.year_of_construction, 'light_annex')
    floor.area = 6

    roof = Rooftop(parent = tz4)
    roof.name = "Roof"
    roof.load_type_element(bldg.year_of_construction, 'light_annex')
    roof.area = 9.25

    '''
    We calculate the RC Values according to ebc procedure
    '''
    prj.calc_all_buildings('ebc')
    '''
    Export the Modelica Record
    '''
    prj.export_record(building_model="MultizoneEquipped",
                      zone_model="ThermalZoneEquipped",
                      corG=False,)
    '''
    Save new TEASER XML
    '''
    prj.save_project("ExampleProject")


if __name__ == '__main__':
    prj = Project(load_data=True)
    D1_North()
    print("That's it :)")
