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
import time


from teaser.Project import Project
from teaser.Logic.BuildingObjects.Building import Building
from teaser.Logic.BuildingObjects.ThermalZone import ThermalZone
from teaser.Logic.BuildingObjects.BuildingPhysics.InnerWall import InnerWall
from teaser.Logic.BuildingObjects.BuildingPhysics.OuterWall import OuterWall
from teaser.Logic.BuildingObjects.BuildingPhysics.Window import Window
from teaser.Logic.BuildingObjects.BuildingPhysics.Material import Material
from teaser.Logic.BuildingObjects.BuildingPhysics.Layer import Layer
from teaser.Logic.BuildingObjects.TypeBuildings.UseConditions18599 import UseConditions18599


def example_create_building():
    '''
    Instantiate a Project class (with load_data set to true), instantiate a 
    Building class, with the project as a parent. This automatically adds the 
    specific building and all its future changes to the project.
    '''
    prj = Project(load_data = True)
    bldg = Building(parent = prj) 
    
    '''Set some building parameters'''
    
    bldg.name = "SuperBuilding"
    bldg.street_name = "Awesome Avenue 42"
    bldg.city = "46325 Fantastic Town"
    bldg.year_of_construction = 1988
    
    '''Instantiate a ThermalZone class, with building as parent and set  some 
    parameters of the thermal zone'''
           
    tz = ThermalZone(parent = bldg) 
    tz.name = "Living Room"
    tz.area = 45.0
    tz.volume = 123.0
    tz.infiltration_rate = 0.5
    
    '''Instantiate UseConditions18599 class with thermal zone as parent,
    and load the use conditions for the usage 'Living' '''
    
    tz.use_conditions = UseConditions18599(parent = tz)
    tz.use_conditions.load_use_conditions("Living")
    
    '''
    Instantiate, each one OuterWall class, InnerWall class and Window class, 
    with thermal zone as parent
    '''
    out_wall = OuterWall(parent = tz)
    in_wall = InnerWall(parent = tz)
    win = Window(parent = tz)
    
    '''
    Out of typical construction the material properties for inner and outer wall are
    loaded
    '''
    out_wall.load_type_element(2014,"heavy")
    in_wall.load_type_element(1988, "light")
    
    '''
    We still need to set some additional attributes
    '''
    out_wall.name = "Outer Wall"
    out_wall.area = 14.0
    out_wall.tilt = 90.0
    out_wall.orientation = 0.0
    
    in_wall.name = "Inner Wall"
    in_wall.area = 28.0
     
    
    '''
    We do know the exact properties of the window, thus we set them
    '''
    win.name = "Window"
    win.area = 7.0
    win.tilt = 90.0
    win.orientation = 0.0
    win.inner_convection = 1.7
    win.inner_radiation = 5.0
    win.outer_convection = 20.0
    win.outer_radiation = 5.0
    win.g_value = 0.789
    win.a_conv = 0.03
    
    '''Instantiate a Layer class, with window as parent, set attributes'''
    win_layer = Layer(parent = win)
    win_layer.id = 1
    win_layer.thickness = 0.024
    '''Instantiate a Material class, with window layer as parent, set attributes'''
    win_material = Material(win_layer)
    win_material.name = "GlasWindow"
    win_material.thermal_conduc = 0.067
    win_material.transmittance = 0.9
    '''
    We calculate the RC Values according to ebc procedure
    '''
    prj.calc_all_buildings('ebc' )
    '''
    Export the Modelica Record
    '''
    prj.export_record("CitiesRWin")
    '''
    Save new TEASER XML
    '''
    prj.save_project("ExampleProject")
    
    
if __name__ == '__main__':
    example_create_building()
    print("That's it :)")
