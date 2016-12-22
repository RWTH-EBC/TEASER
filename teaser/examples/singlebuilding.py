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

from teaser.logic.buildingobjects.boundaryconditions.boundaryconditions \
    import BoundaryConditions
from teaser.logic.buildingobjects.building import Building
from teaser.logic.buildingobjects.buildingphysics.groundfloor import\
    GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.project import Project


def example_create_building():
    '''
    Instantiate a Project class (with load_data set to true), instantiate a
    Building class, with the project as a parent. This automatically adds the
    specific building and all its future changes to the project.
    '''
    prj = Project(load_data=True)
    prj.name = "Super Example Building"
    bldg = Building(parent=prj)

    '''Set some building parameters'''
    bldg.name = "Super Example Building"
    bldg.street_name = "Awesome Avenue 42"
    bldg.city = "46325 Fantastic Town"
    bldg.year_of_construction = 1988
    bldg.number_of_floors = 1
    bldg.height_of_floors = 3.5

    '''Instantiate a ThermalZone class, with building as parent and set  some
    parameters of the thermal zone'''

    tz = ThermalZone(parent=bldg)
    tz.name = "Living Room"
    tz.area = 140.0
    tz.volume = tz.area * bldg.number_of_floors * bldg.height_of_floors
    tz.infiltration_rate = 0.5

    '''Instantiate UseConditions18599 class with thermal zone as parent,
    and load the use conditions for the usage 'Living' '''

    tz.use_conditions = BoundaryConditions(parent=tz)
    tz.use_conditions.load_use_conditions("Living",prj.data)

    '''Define two elements representing a pitched roof and define Layers and
    Materials explicitly'''

    roof_south = Rooftop(parent=tz)
    roof_south.name = "Roof_South"

    roof_north = Rooftop(parent=tz)
    roof_north.name = "Roof_North"

    '''Set area, orientation and tilt of South Roof'''
    roof_south.area = 75.0
    roof_south.orientation = 180.0
    roof_south.tilt = 55.0

    '''Set coefficient of heat transfer'''
    roof_south.inner_convection = 1.7
    roof_south.outer_convection = 20.0
    roof_south.inner_radiation = 5.0
    roof_south.outer_radiation = 5.0

    '''Set layer and material'''
    layer_1s = Layer(parent=roof_south, id=0) # id indicates the order of
                                              # layer from inside to outside
    layer_1s.thickness = 0.15

    material_1_2 = Material(layer_1s)
    material_1_2.name = "Insulation"
    material_1_2.density = 120.0
    material_1_2.heat_capac = 0.04
    material_1_2.thermal_conduc = 1.0

    layer_2s = Layer(parent=roof_south, id=1)
    layer_2s.thickness = 0.15

    material_1_1 = Material(layer_2s)
    material_1_1.name = "Tile"
    material_1_1.density = 1400.0
    material_1_1.heat_capac = 0.6
    material_1_1.thermal_conduc = 2.5

    '''Set area, orientation and tilt of North Roof'''
    roof_north.area = 75.0
    roof_north.orientation = 0.0
    roof_north.tilt = 55.0

    '''Set coefficient of heat transfer'''
    roof_north.inner_convection = 1.7
    roof_north.outer_convection = 20.0
    roof_north.inner_radiation = 5.0
    roof_north.outer_radiation = 5.0

    '''Set layer and material'''
    layer_1n = Layer(parent=roof_north, id=0)
    layer_1n.thickness = 0.15

    material_1_2 = Material(layer_1n)
    material_1_2.name = "Insulation"
    material_1_2.density = 120.0
    material_1_2.heat_capac = 0.04
    material_1_2.thermal_conduc = 1.0

    layer_2n = Layer(parent=roof_north, id=1)
    layer_2n.thickness = 0.15
    layer_2n.position = 1

    material_1_1 = Material(layer_2n)
    material_1_1.name = "Tile"
    material_1_1.density = 1400.0
    material_1_1.heat_capac = 0.6
    material_1_1.thermal_conduc = 2.5

    '''We save information of the Outer and Inner walls as well as Windows
    in dicts, the key is the name, while the value is a list (if applicable)
    [year of construciton,
     construction type,
     area,
     tilt,
     orientation]
     '''

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
        out_wall.load_type_element(year=value[0],
                                   construction=value[1], data_class=prj.data)
        out_wall.area = value[2]
        out_wall.tilt = value[3]
        out_wall.orientation = value[4]

    for key, value in in_wall_dict.items():
        '''instantiate InnerWall class'''
        in_wall = InnerWall(parent = tz)
        in_wall.name = key
        '''load typical construction, based on year of construction and
        construction type'''
        in_wall.load_type_element(year=value[0],
                                  construction=value[1], data_class=prj.data)
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


    '''For a GroundFloor we are using the load_type_element function,
    which needs the year of construction and the construction type ('heavy'
    or 'light')
    '''
    ground = GroundFloor(parent=tz)
    ground.name = "Ground floor"
    ground.load_type_element(bldg.year_of_construction, 'heavy', prj.data)
    ground.area = 140.0

    '''
    We need to set the projects calculation method. The library we want to
    use is AixLib, we are using a two element model and want an extra resistance
    for the windows. To export the parameters to a Modelica record, we use
    the export_aixlib function. path = None indicates, that we want to store
    the records in TEASER'S Output folder
    '''

    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 2
    prj.merge_windows_calc = False

    prj.calc_all_buildings()

    '''
    Export the Modelica Record. If you have a Dymola License you can  export
    the model with a central AHU (MultizoneEquipped) (only default for office
    and institute buildings)
    '''
    
    prj.export_aixlib(building_model="MultizoneEquipped",
                      zone_model="ThermalZoneEquipped",
                      corG=True,
                      internal_id=None,
                      path=None)

    '''
    For OpenModelica you need to exclude the centralAHU (because it is using
    state machines). Therefore use the building_model "Multizone"
    '''

    #prj.export_aixlib(building_model="Multizone",
    #                  zone_model="ThermalZoneEquipped",
    #                  corG=True,
    #                  internal_id=None,
    #                  path=None)


    '''Or we use Annex60 method (e.g with four elements). Which exports one
    Model per zone'''

    # prj.used_library_calc = 'Annex60'
    # prj.number_of_elements_calc = 4
    # prj.merge_windows_calc = False
    #
    # prj.calc_all_buildings()
    # prj.export_annex()

    '''
    Save new TEASER XML and cityGML
    '''
    prj.save_project("ExampleProject")
    prj.save_citygml("ExampleCityGML")

if __name__ == '__main__':
    example_create_building()
    print("That's it :)")
