examples
=======================

You can find more examples in the example package of the TEASER distribution.
e.g.:

[PathOfYourPythonDistribution/Lib/site-packages/teaser]

archetype.py
-------------------------------------------

This module contains an example how to create an archetype Building, to retrofit
that building and to export that building to internal XML and a Modelica record

First thing we need to do is to import our Project API module::

    from teaser.project import project

We instantiate the Project class. The parameter load_data = True indicates
that we load the XML data bases into our Project. This can take a few sec.::

    prj = Project(load_data = True)

The five functions starting with type_bldg giving us the opportunity to
create the specific type building (e.g. type_bldg_residential). The function
automatically calculates all the necessary parameter. If not specified different
it uses vdi calculation method::

    prj.type_bldg_residential(
        name="ResidentialBuilding",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.5,
        net_leased_area=100,
        with_ahu=True,
        residential_layout=1,
        neighbour_buildings=1,
        attic=1,
        cellar=1,
        construction_type="heavy",
        dormer=1)

    prj.type_bldg_office(
        name="Office1",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.5,
        net_leased_area=100,
        office_layout=1,
        window_layout=1,
        with_ahu=True,
        construction_type="heavy")

We need to set the projects calculation method. The library we want to use is
AixLib, we are using a two element model and want an extra resistance for the
windows. To export the parameters to a Modelica record, we use the export_aixlib
function. path = None indicates, that we want to store the records in \
TEASER'S Output folder::

    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 2
    prj.merge_windows_calc = False
    prj.calc_all_buildings()
    prj.export_aixlib(
        building_model="MultizoneEquipped",
        zone_model="ThermalZoneEquipped",
        corG=True,
        internal_id=None,
        path=None)

We could also use Annex60 models with same calculation method::

    prj.used_library_calc = "Annex60"
    prj.calc_all_buildings()
    prj.export_annex(number_of_elements=2,
                     merge_windows=False,
                     internal_id=None,
                     path=None)

Now we retrofit all buildings in the year 2015 (EnEV2014). That includes new
insulation layer and new windows. The name is changed to Retrofit::

    prj.name = "Project_Retrofit"
    prj.retrofit_all_buildings(2015)
    prj.export_record(
        building_model="MultizoneEquipped",
        zone_model="ThermalZoneEquipped",
        corG=True,
        internal_id=None,
        path=None)

To load our retrofitted building in TEASER later on, we can save the project into a
XML file::

    prj.save_project("Retrofit_Building", path=None)



singlebuilding.py
---------------------------------------------

This module shows how to create a building from scratch (or arbitrary sources)
calculate parameters for a Modelica model and save this example building in a
XML based format. The used classes are imported one after another. Of course
you can import all the classes at the beginning::

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
    from teaser.logic.buildingobjects.boundaryconditions.boundaryconditions \
        import BoundaryConditions
    from teaser.project import Project

    prj = Project(load_data=True)
    bldg = Building(parent=prj)

Set some building parameters::

    bldg.name = "SuperBuilding"
    bldg.street_name = "Awesome Avenue 42"
    bldg.city = "46325 Fantastic Town"
    bldg.year_of_construction = 1988

Instantiate a ThermalZone class, with building as parent and set 
some parameters of the thermal zone::

    tz = ThermalZone(parent=bldg)
    tz.name = "Living Room"
    tz.area = 45.0
    tz.volume = 123.0
    tz.infiltration_rate = 0.5

Instantiate UseConditionsOffice18599 class with thermal zone as parent, and load the use conditions for the usage 'Living'::

    tz.use_conditions = BoundaryConditions(parent=tz)
    tz.use_conditions.load_use_conditions("Living")
    
Define two elements representing a pitched roof and define Layers and
Materials explicitly::

    roof_south = Rooftop(parent=tz)
    roof_south.name = "Roof_South"

    roof_north = Rooftop(parent=tz)
    roof_north.name = "Roof_North"

Set area, orientation and tilt of South Roof::

    roof_south.area = 75.0
    roof_south.orientation = 180.0
    roof_south.tilt = 55.0

Set coefficient of heat transfer::

    roof_south.inner_convection = 1.7
    roof_south.outer_convection = 5.0
    roof_south.inner_radiation = 20.0
    roof_south.outer_radiation = 5.0

    
Set layer and material. The id indicates the position
of the layer from inside to outside::

    layer_1s = Layer(parent=roof_south, id=0) 
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

Set area, orientation and tilt of North Roof::

    roof_north.area = 75.0
    roof_north.orientation = 0.0
    roof_north.tilt = 55.0

Set coefficient of heat transfer::

    roof_north.inner_convection = 1.7
    roof_north.outer_convection = 5.0
    roof_north.inner_radiation = 20.0
    roof_north.outer_radiation = 5.0

Set layer and material::

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
    
    
For the remaining Outer and Inner walls as well as Windows, we save the information
in python dicitonaries, iterate them and instantiate the corresponding classes. In addition we
are using the load_type_element function to determine the building physics from statistical data
The key of the dict is the walls's name, while the value is a list with parameters the 
[year of construciton, construction type, area, tilt,orientation]::

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
                                   construction=value[1])
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
                                  construction=value[1])
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
        
For a GroundFloor we are using the load_type_element function explicitly,
which needs the year of construction and the construction type ('heavy'
or 'light')::

    ground = GroundFloor(parent=tz)
    ground.name = "Ground floor"
    ground.load_type_element(year=1988, construction='heavy')
    ground.area = 140.0

We calculate the RC Values according to AixLib procedure::

    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 2
    prj.merge_windows_calc = False

    prj.calc_all_buildings()

Export the Modelica model::

    prj.export_aixlib(
        building_model="MultizoneEquipped",
        zone_model="ThermalZoneEquipped",
        corG=True,
        internal_id=None,
        path=None)

Or we use Annex60 method with for elements::

    prj.used_library_calc = 'Annex60'


    prj.calc_all_buildings()
    prj.export_annex(number_of_elements=2,
                     merge_windows=False,
                     used_library='Annex60')


Save teaserXML and CityGML::

    prj.save_project(file_name="ExampleProject")
    prj.save_citygml(
        file_name="ExampleProject",
        path=None)
