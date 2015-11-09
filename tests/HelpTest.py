import math

from teaser.Logic.BuildingObjects.Building import Building
from teaser.Logic.BuildingObjects.BuildingPhysics.InnerWall import InnerWall
from teaser.Logic.BuildingObjects.BuildingPhysics.Layer import Layer
from teaser.Logic.BuildingObjects.BuildingPhysics.Material import Material
from teaser.Logic.BuildingObjects.BuildingPhysics.OuterWall import OuterWall
from teaser.Logic.BuildingObjects.BuildingPhysics.Window import Window
from teaser.Logic.BuildingObjects.ThermalZone import ThermalZone
from teaser.Logic.BuildingObjects.TypeBuildings.UseConditions18599 import UseConditions18599

def building_test2(prj):
    """
    building which is hardcoded for testing
    """
    

    bldg = Building(prj)

    bldg.name = "RWTHBuilding"
    bldg.street_name = "Templergraben 55"
    bldg.city = "52062 Aachen"

    # bldg.type_of_building = "Buerogebaeude"

    bldg.year_of_construction = "1988"
    bldg.number_of_floors = 5.0
    bldg.height_of_floors = 1.0
    bldg.net_leased_area = 2000.0
    bldg.construction_type = "heavy"

    # bldg.thermal_zones = []
    # bldg.outer_area = {}
    # bldg.window_area ={}

    bldg.volume = 30.0
    # bldg.sum_heating_load = 0
    # bldg.sum_cooling_load = 0

    # bldg.file_ahu = ""
    # bldg.file_internal_gains = ""
    # bldg.file_set_t = ""
    # bldg.file_weather = ""
    '''
     thermalzone
     '''
    tz = ThermalZone(bldg)
    tz.name = "test1"
    tz.area = 10.0
    tz.volume = 25.0
    tz.infiltration_rate = 5.0
    tz.use_conditions = UseConditions18599()
    '''
    outerwall
    '''

    out_wall = OuterWall(tz)
    out_wall.construction_type = "abc"
    out_wall._year_of_renovation = 2015
    out_wall.year_of_construction = 3050
    out_wall.building_age_group = [0, 1998]
    out_wall.name = "Outer Wall"
    out_wall.area = 10.0
    out_wall.tilt = 90.0
    out_wall.orientation = 0.0
    out_wall.inner_radiation = 5.0
    out_wall.inner_convection = 2.7
    out_wall.outer_radiation = 5.0
    out_wall.outer_convection = 20.0

    # outerwall layer
    out_wall_layer1 = Layer(out_wall)
    out_wall_layer1.id = 1
    out_wall_layer1.thickness = 5.0
    out_wall_material = Material(out_wall_layer1)
    out_wall_material.name = "material1"
    out_wall_material.density = 5.0
    out_wall_material.thermal_conduc = 4.0
    out_wall_material.heat_capac = 0.48
    out_wall_material.transmittance = 2.0

    out_wall_layer2 = Layer(out_wall)
    out_wall_layer2.id = 2
    out_wall_layer2.thickness = 2.0
    out_wall_material = Material(out_wall_layer2)
    out_wall_material.name = "material"
    out_wall_material.density = 2.0
    out_wall_material.thermal_conduc = 2.0
    out_wall_material.heat_capac = 0.84
    out_wall_material.transmittance = 6.0

    """second outerwall"""
    out_wall2 = OuterWall(tz)
    out_wall2.name = "Outer Wall2"
    out_wall2.area = 12.0
    out_wall2.tilt = 90.0
    out_wall2.orientation = 0.0
    out_wall2.inner_radiation = 5.0
    out_wall2.inner_convection = 2.7
    out_wall2.outer_radiation = 5.0
    out_wall2.outer_convection = 20.0

    # outerwall layer
    out_wall2_layer1 = Layer(out_wall2)
    out_wall2_layer1.id = 1
    out_wall2_layer1.thickness = 2.0
    out_wall2_material = Material(out_wall2_layer1)
    out_wall2_material.name = "material1"
    out_wall2_material.density = 4.0
    out_wall2_material.thermal_conduc = 5.0
    out_wall2_material.heat_capac = 0.98
    out_wall2_material.transmittance = 1.5

    out_wall2_layer2 = Layer(out_wall2)
    out_wall2_layer2.id = 2
    out_wall2_layer2.thickness = 4.0
    out_wall2_material = Material(out_wall2_layer2)
    out_wall2_material.name = "material"
    out_wall2_material.density = 2.0
    out_wall2_material.thermal_conduc = 3.0
    out_wall2_material.heat_capac = 0.44
    out_wall2_material.transmittance = 5.0

    '''
    parameters InnerWall
    '''
    in_wall = InnerWall(tz)
    in_wall.construction_type = "heavy"
    in_wall._year_of_renovation = 2015
    in_wall.year_of_construction = 3050
    in_wall.building_age_group = [0, 1998]
    in_wall.name = "InnerWall"
    in_wall.area = 5.0
    in_wall.tilt = 90.0
    in_wall.orientation = 1.0
    in_wall.inner_radiation = 5.0
    in_wall.inner_convection = 3.7

    # layer innerwall
    in_wall_layer1 = Layer(in_wall)
    in_wall_layer1.id = 1
    in_wall_layer1.thickness = 2.5
    in_wall_material = Material(in_wall_layer1)
    in_wall_material.name = "material1"
    in_wall_material.density = 4.0
    in_wall_material.thermal_conduc = 4.0
    in_wall_material.heat_capac = 0.72

    in_wall_layer2 = Layer(in_wall)
    in_wall_layer2.id = 2
    in_wall_layer2.thickness = 2.0
    in_wall_material = Material(in_wall_layer2)
    in_wall_material.name = "material2"
    in_wall_material.density = 2.0
    in_wall_material.thermal_conduc = 2.0
    in_wall_material.heat_capac = 0.84

    '''
    second InnerWall
    '''
    in_wall2 = InnerWall(tz)
    in_wall2.name = "InnerWall"
    in_wall2.area = 5.0
    in_wall2.tilt = 90.0
    in_wall2.orientation = 1.0
    in_wall2.inner_radiation = 5.0
    in_wall2.inner_convection = 3.7

    # layer innerwall
    in_wall2_layer1 = Layer(in_wall2)
    in_wall2_layer1.id = 1
    in_wall2_layer1.thickness = 2.5
    in_wall2_material = Material(in_wall2_layer1)
    in_wall2_material.name = "material1"
    in_wall2_material.density = 4.0
    in_wall2_material.thermal_conduc = 4.0
    in_wall2_material.heat_capac = 0.72

    in_wall2_layer2 = Layer(in_wall2)
    in_wall2_layer2.id = 2
    in_wall2_layer2.thickness = 2.0
    in_wall2_material = Material(in_wall2_layer2)
    in_wall2_material.name = "material2"
    in_wall2_material.density = 2.0
    in_wall2_material.thermal_conduc = 2.0
    in_wall2_material.heat_capac = 0.84

    '''
    parameters Window
    '''
    window = Window(tz)
    window.construction_type = "light"
    # window._year_of_renovation = 2015
    # window.year_of_construction = 3050
    window.building_age_group = [0, 1998]
    # window.id = "window1"
    window.name = "Window"
    window.area = 10.0
    window.tilt = 90.0
    window.orientation = 0.0
    window.inner_radiation = 5.0
    window.inner_convection = 1.7
    window.outer_radiation = 5.0
    window.outer_convection = 25.0

    # layer window
    window_layer1 = Layer(window)
    window_layer1.id = 1
    window_layer1.thickness = 5.0
    window_material = Material(window_layer1)
    window_material.name = "glass"
    window_material.thermal_conduc = 4.0
    window_material.transmittance = 2.0
    
    return bldg