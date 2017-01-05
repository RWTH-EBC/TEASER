# Created July 2015
# TEASER Development Team

"""This module contains an example that shows to create a building not using
the archetype approach but adding all information separately. In this example
we import all needed modules and classes where we need it in the code. For you
application we suggest to use PEP008 and import them at the beginning of the
script.
"""


def example_create_building():
    """"This function demonstrates generating a building adding all
    information separately"""

    # First step: Import the TEASER API (called Project) into your Python module

    from teaser.project import Project

    # To use the API instantiate the Project class and rename the Project. The
    # parameter load_data=True indicates that we load data into our
    # Project (e.g. for Material properties and typical wall constructions.
    # This can take a few seconds, depending on the size of the used data base.

    prj = Project(load_data=True)
    prj.name = "BuildingExample"

    # Instantiate a Building class and set the Project API as a parent to
    # this building. This will automatically add this building and all its
    # future changes to the project. This is helpful as we can use the data
    # base and API functions (like explained in e2 - e5). We also set some
    # building parameters. Be careful: Dymola does not like whitespaces in
    # names and filenames, thus we will delete them anyway in TEASER.

    from teaser.logic.buildingobjects.building import Building

    bldg = Building(parent=prj)
    bldg.name = "SuperExampleBuilding"
    bldg.street_name = "AwesomeAvenue42"
    bldg.city = "46325FantasticTown"
    bldg.year_of_construction = 1988
    bldg.number_of_floors = 1
    bldg.height_of_floors = 3.5

    # Instantiate a ThermalZone class and set the Building as a parent of it.
    # Set some parameters of the thermal zone. Be careful: Dymola does not
    # like whitespaces in  names and filenames, thus we will delete them
    # anyway in TEASER.

    from teaser.logic.buildingobjects.thermalzone import ThermalZone

    tz = ThermalZone(parent=bldg)
    tz.name = "LivingRoom"
    tz.area = 140.0
    tz.volume = tz.area * bldg.number_of_floors * bldg.height_of_floors
    tz.infiltration_rate = 0.5

    # Instantiate BoundaryConditions and load conditions for `Living`.

    from teaser.logic.buildingobjects.boundaryconditions.boundaryconditions \
        import BoundaryConditions

    tz.use_conditions = BoundaryConditions(parent=tz)
    tz.use_conditions.load_use_conditions("Living", prj.data)

    # Define two building elements reflecting a pitched roof (south = 180° and
    # north = 0°). Setting the the ThermalZone as a parent will automatically
    # assign this element to the thermal zone. We also set names, tilt and
    # coefficients for heat transfer on the inner and outer side of the
    # roofs. Please read the docs to get more information on these parameters.

    from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop

    roof_south = Rooftop(parent=tz)
    roof_south.name = "Roof_South"
    roof_south.area = 75.0
    roof_south.orientation = 180.0
    roof_south.tilt = 55.0
    roof_south.inner_convection = 1.7
    roof_south.outer_convection = 20.0
    roof_south.inner_radiation = 5.0
    roof_south.outer_radiation = 5.0

    roof_north = Rooftop(parent=tz)
    roof_north.name = "Roof_North"
    roof_north.area = 75.0
    roof_north.orientation = 0.0
    roof_north.tilt = 55.0
    roof_north.inner_convection = 1.7
    roof_north.outer_convection = 20.0
    roof_north.inner_radiation = 5.0
    roof_north.outer_radiation = 5.0

    # To define the wall constructions we need to instantiate Layer and
    # Material objects and set attributes. id indicates the order of wall
    # construction from inside to outside (so 0 is on the inner surface). You
    # need to set this value!

    from teaser.logic.buildingobjects.buildingphysics.layer import Layer

    # First layer south

    layer_s1 = Layer(parent=roof_south, id=0)
    layer_s1.thickness = 0.15

    from teaser.logic.buildingobjects.buildingphysics.material import Material

    material_s1 = Material(layer_s1)
    material_s1.name = "Insulation"
    material_s1.density = 120.0
    material_s1.heat_capac = 0.04
    material_s1.thermal_conduc = 1.0

    # Second layer south

    layer_s2 = Layer(parent=roof_south, id=1)
    layer_s2.thickness = 0.15

    material_s2 = Material(layer_s2)
    material_s2.name = "Tile"
    material_s2.density = 1400.0
    material_s2.heat_capac = 0.6
    material_s2.thermal_conduc = 2.5

    # First layer north

    layer_n1 = Layer(parent=roof_south, id=0)
    layer_n1.thickness = 0.15

    from teaser.logic.buildingobjects.buildingphysics.material import Material

    material_n1 = Material(layer_n1)
    material_n1.name = "Insulation"
    material_n1.density = 120.0
    material_n1.heat_capac = 0.04
    material_n1.thermal_conduc = 1.0

    # Second layer north

    layer_n2 = Layer(parent=roof_south, id=1)
    layer_n2.thickness = 0.15

    material_n2 = Material(layer_n2)
    material_n2.name = "Tile"
    material_n2.density = 1400.0
    material_n2.heat_capac = 0.6
    material_n2.thermal_conduc = 2.5



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
    
    #prj.export_aixlib(building_model="MultizoneEquipped",
    #                  zone_model="ThermalZoneEquipped",
    #                  corG=True,
    #                  internal_id=None,
    #                  path=None)

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
