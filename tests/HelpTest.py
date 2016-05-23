from teaser.logic.BuildingObjects.BoundaryConditions.BoundaryConditions \
    import BoundaryConditions
from teaser.logic.BuildingObjects.Building import Building
from teaser.logic.BuildingObjects.BuildingPhysics.GroundFloor import GroundFloor
from teaser.logic.BuildingObjects.BuildingPhysics.InnerWall import InnerWall
from teaser.logic.BuildingObjects.BuildingPhysics.Layer import Layer
from teaser.logic.BuildingObjects.BuildingPhysics.Material import Material
from teaser.logic.BuildingObjects.BuildingPhysics.OuterWall import OuterWall
from teaser.logic.BuildingObjects.BuildingPhysics.Rooftop import Rooftop
from teaser.logic.BuildingObjects.BuildingPhysics.Window import Window
from teaser.logic.BuildingObjects.ThermalZone import ThermalZone


def building_test2(prj):
    """
    building which is hardcoded for testing
    """
    bldg = Building(parent = prj)

    '''Set some building parameters'''

    bldg.name = "UnitTestBuilding"
    bldg.street_name = "Unit Street 42"
    bldg.city = "46325 Testing Town"
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

    tz.use_conditions = BoundaryConditions(tz)
    tz.use_conditions.usage = "Living"
    tz.use_conditions.cooling_time = [5,18]
    tz.use_conditions.heating_time = [5,18]
    tz.use_conditions.set_temp_heat = 288.15
    tz.use_conditions.set_temp_cool = 298.15
    tz.use_conditions.temp_set_back= 4.0
    tz.use_conditions.min_air_exchange= 0.0
    tz.use_conditions.min_ahu= 0.0
    tz.use_conditions.max_ahu = 2.6
    tz.use_conditions.with_ahu = True
    tz.use_conditions.persons = 3
    tz.use_conditions.machines = 3
    tz.use_conditions.lighting_power = 3
    tz.use_conditions.activity_type_machines = 2
    tz.use_conditions.ratio_conv_rad_machines = 0.5
    tz.use_conditions.profile_machines = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
                                          0.2, 0.4, 0.6, 0.8, 0.8, 0.4, 0.6,
                                          0.8, 0.8, 0.4, 0.2, 0.0, 0.0, 0.0,
                                          0.0, 0.0, 0.0]
    tz.use_conditions.profile_persons = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                                         0.2, 0.4, 0.6, 0.8, 0.8, 0.4, 0.6,
                                         0.8, 0.8, 0.4, 0.2, 0.1, 0.1, 0.1,
                                         0.1, 0.1, 0.1]
    tz.use_conditions.profile_lighting = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                                          0.2, 0.4, 0.6, 0.8, 0.8, 0.4, 0.6,
                                          0.8, 0.8, 0.4, 0.2, 0.1, 0.1, 0.1,
                                          0.1, 0.1, 0.1]
    tz.use_conditions.use_constant_ach_rate = False
    tz.use_conditions.base_ach = 0.2
    tz.use_conditions.max_user_ach = 1.0
    tz.use_conditions.max_overheating_ach = [3.0, 2.0]
    tz.use_conditions.max_summer_ach = [1.0, 273.15 + 10, 273.15 + 17]
    tz.use_conditions.winter_reduction = [0.2, 273.15, 273.15 + 10]

    out_wall_dict = [["Outer Wall 1", [bldg.year_of_construction, 'heavy',
                                      10.0, 90.0, 0.0]],
                     ["Outer Wall 2", [bldg.year_of_construction, 'heavy',
                                      14.0, 90.0, 90.0]],
                     ["Outer Wall 3", [bldg.year_of_construction, 'heavy',
                                      10.0, 90.0, 180.0]],
                     ["Outer Wall 4", [bldg.year_of_construction, 'heavy',
                                      14.0, 90.0, 270.0]]]
    #import collections
    #out_wall_dict = collections.OrderedDict(sorted(out_wall_dict.items(), key=lambda t: t[0]))
    for value in out_wall_dict:
        '''instantiate OuterWall class'''
        out_wall = OuterWall(parent = tz)
        out_wall.name = value[0]
        out_wall.year_of_construction = value[1][0]
        out_wall.construction_type = value[1][1]
        out_wall.area = value[1][2]
        out_wall.tilt = value[1][3]
        out_wall.orientation = value[1][4]
        out_wall.building_age_group = [1994, 1998]
        out_wall.inner_radiation = 5.0
        out_wall.inner_convection = 2.7
        out_wall.outer_radiation = 5.0
        out_wall.outer_convection = 20.0

        out_wall_layer1 = Layer(out_wall)
        out_wall_layer1.id = 1
        out_wall_layer1.thickness = 5.0
        out_wall_material = Material(out_wall_layer1)
        out_wall_material.name = "material1"
        out_wall_material.density = 5.0
        out_wall_material.thermal_conduc = 4.0
        out_wall_material.heat_capac = 0.48
        out_wall_material.transmittance = 0.0

        out_wall_layer2 = Layer(out_wall)
        out_wall_layer2.id = 2
        out_wall_layer2.thickness = 2.0
        out_wall_material = Material(out_wall_layer2)
        out_wall_material.name = "material"
        out_wall_material.density = 2.0
        out_wall_material.thermal_conduc = 2.0
        out_wall_material.heat_capac = 0.84
        out_wall_material.transmittance = 0.0

    in_wall_dict = [["Inner Wall 1", [bldg.year_of_construction, 'light', 10.0]],
                    ["Inner Wall 2", [bldg.year_of_construction, 'heavy', 14.0]],
                    ["Inner Wall 3", [bldg.year_of_construction, 'light', 10.0]]]

    for value in in_wall_dict:
        '''instantiate OuterWall class'''
        in_wall = InnerWall(parent = tz)
        in_wall.name = value[0]
        in_wall.year_of_construction = value[1][0]
        in_wall.construction_type = value[1][1]
        in_wall.area = value[1][2]
        in_wall.building_age_group = [1994, 1998]
        in_wall.inner_radiation = 5.0
        in_wall.inner_convection = 2.7

        in_wall_layer1 = Layer(in_wall)
        in_wall_layer1.id = 1
        in_wall_layer1.thickness = 5.0
        in_wall_material = Material(in_wall_layer1)
        in_wall_material.name = "material1"
        in_wall_material.density = 5.0
        in_wall_material.thermal_conduc = 4.0
        in_wall_material.heat_capac = 0.48

        in_wall_layer2 = Layer(in_wall)
        in_wall_layer2.id = 2
        in_wall_layer2.thickness = 2.0
        in_wall_material = Material(in_wall_layer2)
        in_wall_material.name = "material"
        in_wall_material.density = 2.0
        in_wall_material.thermal_conduc = 2.0
        in_wall_material.heat_capac = 0.84

    win_dict = [["Window 1", [bldg.year_of_construction,
                             5.0, 90.0, 90.0]],
                ["Window 2", [bldg.year_of_construction,
                             8.0, 90.0, 180.0]],
                ["Window 3", [bldg.year_of_construction,
                             5.0, 90.0, 270.0]]]

    for value in win_dict:
        win = Window(parent = tz)
        win.construction_type = "Window"
        win.name = value[0]
        win.area = value[1][1]
        win.tilt = value[1][2]
        win.orientation = value[1][3]
        win.building_age_group = [1994, 1998]

        win.inner_convection = 1.7
        win.inner_radiation = 5.0
        win.outer_convection = 20.0
        win.outer_radiation = 5.0
        win.g_value = 0.789
        win.a_conv = 0.03
        win.shading_g_total = 1.0
        win.shading_max_irr = 180.0
        win_layer = Layer(parent = win)
        win_layer.id = 1
        win_layer.thickness = 0.024

        win_material = Material(win_layer)
        win_material.name = "GlasWindow"
        win_material.thermal_conduc = 0.067
        win_material.transmittance = 0.9

    roof = Rooftop(parent = tz)
    roof.name = "Roof"
    roof.year_of_construction = bldg.year_of_construction
    roof.construction_type = "heavy"
    roof.area = 140.0

    roof_layer1 = Layer(roof)
    roof_layer1.id = 1
    roof_layer1.thickness = 5.0
    roof_material = Material(roof_layer1)
    roof_material.name = "material1"
    roof_material.density = 5.0
    roof_material.thermal_conduc = 4.0
    roof_material.heat_capac = 0.48

    roof_layer2 = Layer(roof)
    roof_layer2.id = 2
    roof_layer2.thickness = 2.0
    roof_material = Material(roof_layer2)
    roof_material.name = "material"
    roof_material.density = 2.0
    roof_material.thermal_conduc = 2.0
    roof_material.heat_capac = 0.84

    ground = GroundFloor(parent = tz)
    ground.name = "ground"
    ground.year_of_construction = bldg.year_of_construction
    ground.construction_type = "heavy"
    ground.area = 140.0

    ground_layer1 = Layer(ground)
    ground_layer1.id = 1
    ground_layer1.thickness = 5.0
    ground_material = Material(ground_layer1)
    ground_material.name = "material1"
    ground_material.density = 5.0
    ground_material.thermal_conduc = 4.0
    ground_material.heat_capac = 0.48

    ground_layer2 = Layer(ground)
    ground_layer2.id = 2
    ground_layer2.thickness = 2.0
    ground_material = Material(ground_layer2)
    ground_material.name = "material"
    ground_material.density = 2.0
    ground_material.thermal_conduc = 2.0
    ground_material.heat_capac = 0.84

    return bldg
