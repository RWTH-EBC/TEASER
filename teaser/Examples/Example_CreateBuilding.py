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
from teaser.Logic.BuildingObjects.ThermalZone import ThermalZone
from teaser.Project import Project


def example_create_building():
    '''
    Instantiate a Project class (with load_data set to true), instantiate a 
    Building class, with the project as a parent. This automatically adds the 
    specific building and all its future changes to the project.
    '''
    prj = Project(load_data = True)
    bldg = Building(parent = prj)

    '''Set some building parameters'''

    bldg.name = "SuperExampleBuilding"
    bldg.street_name = "Awesome Avenue 42"
    bldg.city = "46325 Fantastic Town"
    bldg.year_of_construction = 1988
    bldg.number_of_floors = 1
    bldg.height_of_floors = 3.5

    '''Instantiate a ThermalZone class, with building as parent and set  some 
    parameters of the thermal zone'''

    tz = ThermalZone(parent = bldg) 
    tz.name = "Living Room"
    tz.area = 140.0
    tz.volume = tz.area * bldg.number_of_floors * bldg.height_of_floors
    tz.infiltration_rate = 0.5

    '''Instantiate UseConditions18599 class with thermal zone as parent,
    and load the use conditions for the usage 'Living' '''

    tz.use_conditions = BoundaryConditions(parent = tz)
    tz.use_conditions.load_use_conditions("Living")
    
    '''We save information of the Outer and Inner walls as well as Windows
    in dicts, the key is the name, while the value is a list (if applicable)
    [year of construciton,
     construction type,
     area,
     tilt,
     orientation]'''

    out_wall_dict = {"Outer Wall 1": [bldg.year_of_construction, 'heavy',
                                      10.0, 90.0, 0.0],
                     "Outer Wall 2": [bldg.year_of_construction, 'heavy',
                                      14.0, 90.0, 90.0],
                     "Outer Wall 3": [bldg.year_of_construction, 'heavy',
                                      10.0, 90.0, 180.0],
                     "Outer Wall 4": [bldg.year_of_construction, 'heavy',
                                      14.0, 90.0, 270.0]}

    in_wall_dict = {"Inner Wall 1": [bldg.year_of_construction, 'light', 10.0],
                    "Inner Wall 2": [bldg.year_of_construction, 'heavy', 14.0],
                    "Inner Wall 3": [bldg.year_of_construction, 'light', 10.0]}
                    
    win_dict = {"Window 1": [bldg.year_of_construction,
                             5.0, 90.0, 90.0],
                "Window 2": [bldg.year_of_construction,
                             8.0, 90.0, 180.0],
                "Window 3": [bldg.year_of_construction,
                             5.0, 90.0, 270.0]}
    for key, value in out_wall_dict.items():
        '''instantiate OuterWall class'''
        out_wall = OuterWall(parent = tz)
        out_wall.name = key
        '''load typical construction, based on year of construction and 
        construction type'''
        out_wall.load_type_element(year = value[0],
                                   construction = value[1])
        out_wall.area = value[2]
        out_wall.tilt = value[3]
        out_wall.orientation = value[4]
                     
    for key, value in in_wall_dict.items():
        '''instantiate InnerWall class'''
        in_wall = InnerWall(parent = tz)
        in_wall.name = key
        '''load typical construction, based on year of construction and 
        construction type'''
        in_wall.load_type_element(year = value[0],
                                  construction = value[1])
        in_wall.area = value[2]
        
    for key, value in win_dict.items():
        '''instantiate Window class'''
        win = Window(parent = tz)
        win.name = key
        win.area = value[1]
        win.tilt = value[2]
        win.orientation = value[3]
        '''
        We know the exact properties of the window, thus we set them instead
        of loading a typical construction
        '''
        win.inner_convection = 1.7
        win.inner_radiation = 5.0
        win.outer_convection = 20.0
        win.outer_radiation = 5.0
        win.g_value = 0.789
        win.a_conv = 0.03
        win.shading_g_total = 1.0
        win.shading_max_irr = 180.0
        '''Instantiate a Layer class, with window as parent, set attributes'''
        win_layer = Layer(parent = win)
        win_layer.id = 1
        win_layer.thickness = 0.024
        '''Instantiate a Material class, with window layer as parent, 
        set attributes'''
        win_material = Material(win_layer)
        win_material.name = "GlasWindow"
        win_material.thermal_conduc = 0.067
        win_material.transmittance = 0.9

    '''Define a Rooftop and a Groundfloor, we don't need to set tilt and 
    orientation because we take the default values'''
    
    roof = Rooftop(parent = tz)
    roof.name = "Roof"
    roof.load_type_element(bldg.year_of_construction, 'heavy')
    roof.area = 140.0
    
    ground = GroundFloor(parent = tz)
    ground.name = "Ground floor"
    ground.load_type_element(bldg.year_of_construction, 'heavy')
    ground.area = 140.0

    '''
    We calculate the RC Values according to ebc procedure
    '''
    prj.calc_all_buildings(number_of_elements=2,
                           merge_windows=False,
                           used_library='AixLib')

    '''
    Export the Modelica Record
    '''
    prj.export_aixlib(building_model="MultizoneEquipped",
                      zone_model="ThermalZoneEquipped",
                      corG=False,
                      internal_id=None
                      path=None)
    '''
    Save new TEASER XML
    '''
    prj.save_gml("ExampleProject")
    prj.save_citygml("Easypeasy")
    
if __name__ == '__main__':
    example_create_building()
    print("That's it :)")
