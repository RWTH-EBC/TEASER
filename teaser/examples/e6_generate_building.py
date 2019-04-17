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
    bldg.year_of_construction = 2015
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
    # roofs. If the building has a flat roof, please use -1 as
    # orientation. Please read the docs to get more information on these
    # parameters.

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
    layer_s1.thickness = 0.3

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

    layer_n1 = Layer(parent=roof_north, id=0)
    layer_n1.thickness = 0.3

    from teaser.logic.buildingobjects.buildingphysics.material import Material

    material_n1 = Material(layer_n1)
    material_n1.name = "Insulation"
    material_n1.density = 120.0
    material_n1.heat_capac = 0.04
    material_n1.thermal_conduc = 1.0

    # Second layer north

    layer_n2 = Layer(parent=roof_north, id=1)
    layer_n2.thickness = 0.15

    material_n2 = Material(layer_n2)
    material_n2.name = "Tile"
    material_n2.density = 1400.0
    material_n2.heat_capac = 0.6
    material_n2.thermal_conduc = 2.5

    # Another option is to use the database for typical wall constructions,
    # but set area, tilt, orientation individually. To simplify code,
    # we save individual information for exterior walls, interior walls into
    # dictionaries.
    # outer walls
    # {'name_of_wall': [area, tilt, orientation]}
    # interior walls
    # {'name_of_wall': [area, tilt, orientation]}

    from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall

    out_wall_dict = {"OuterWall_north": [10.0, 90.0, 0.0],
                     "OuterWall_east": [14.0, 90.0, 90.0],
                     "OuterWall_south": [10.0, 90.0, 180.0],
                     "OuterWall_west": [14.0, 90.0, 270.0]}

    # For ground floors the orientation is always -2

    ground_floor_dict = {"GroundFloor": [100.0, 0.0, -2]}

    from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall

    in_wall_dict = {"InnerWall1": [10.0],
                    "InnerWall2": [14.0],
                    "InnerWall3": [10.0]}

    for key, value in out_wall_dict.items():
        # Instantiate class, key is the name
        out_wall = OuterWall(parent=tz)
        out_wall.name = key
        # Use load_type_element() function of the building element, and pass
        # over the year of construction of the building and the type of
        # construction (in this case `heavy`).

        out_wall.load_type_element(
            year=bldg.year_of_construction,
            construction='heavy')

        # area, tilt and orientation need to be set individually.

        out_wall.area = value[0]
        out_wall.tilt = value[1]
        out_wall.orientation = value[2]

    # Repeat the procedure for inner walls and ground floors

    for key, value in in_wall_dict.items():

        in_wall = InnerWall(parent=tz)
        in_wall.name = key
        in_wall.load_type_element(
            year=bldg.year_of_construction,
            construction='heavy')
        in_wall.area = value[0]

    from teaser.logic.buildingobjects.buildingphysics.groundfloor import \
        GroundFloor

    for key, value in ground_floor_dict.items():

        ground = GroundFloor(parent=tz)
        ground.name = key
        ground.load_type_element(
            year=bldg.year_of_construction,
            construction='heavy')
        ground.area = value[0]
        ground.tilt = value[1]
        ground.orientation = value[2]

    from teaser.logic.buildingobjects.buildingphysics.window import Window

    win_dict = {"Window_east": [5.0, 90.0, 90.0],
                "Window_south": [8.0, 90.0, 180.0],
                "Window_west": [5.0, 90.0, 270.0]}

    for key, value in win_dict.items():

        win = Window(parent=tz)
        win.name = key
        win.area = value[0]
        win.tilt = value[1]
        win.orientation = value[2]

        # Additional to the already known attributes the window has
        # additional attributes. Window.g_value describes the solar gain
        # through windows, a_conv the convective heat transmission due to
        # absorption of the window on the inner side. shading_g_total and
        # shading_max_irr refers to the shading (solar gain reduction of the
        # shading and shading_max_irr the threshold of irradiance to
        # automatically apply shading).

        win.inner_convection = 1.7
        win.inner_radiation = 5.0
        win.outer_convection = 20.0
        win.outer_radiation = 5.0
        win.g_value = 0.789
        win.a_conv = 0.03
        win.shading_g_total = 0.0
        win.shading_max_irr = 180.0

        # One equivalent layer for windows

        win_layer = Layer(parent=win)
        win_layer.id = 1
        win_layer.thickness = 0.024

        # Material for glass

        win_material = Material(win_layer)
        win_material.name = "GlasWindow"
        win_material.thermal_conduc = 0.067
        win_material.transmittance = 0.9


if __name__ == '__main__':
    example_create_building()
    print("Example 6: That's it :)")
