Examples package
=======================

Example_TypeBuilding 
-------------------------------------------

This module contains an example how to create a type Buidling, to retrofit
that building and to export that building to internal XML and a Modelica record
	
First thing we need to do is to import our Project API module::

    from teaser.Project import Project
	
We instantiate the Project class. The parameter load_data = True indicates
that we load the XML data bases into our Project. This can take a few sec.::

	prj = Project(load_data = True)

The five functions starting with type_bldg giving us the opportunity to
create the specific type building (e.g. type_bldg_residential). The function
automatically calculates all the necessary parameter. If not specified different
it uses vdi calculation method::
	
	prj.type_bldg_residential(name = "ResidentialBuilding",
						  year_of_construction = 1988,
                          number_of_floors = 5,
                          height_of_floors = 5,
                          net_leased_area = 500,
                          residential_layout = 1,
                          neighbour_buildings = 1,
                          attic = 1,
                          cellar =  1,
                          construction_type = "light",
                          dormer = 1)
	
To export the parameters to a Modelica record, we use the export_record
function. path = None indicates, that we want to store the records in 
TEASER'S Output folder::

	prj.export_record(model_type = 'AixLib',
					path = None)

Now we retrofit all buildings in the year 2015 (EnEV2014). That includes new 
insulation layer and new windows. The name is changed to Retrofit::

	prj.name = "Project_Retrofit"
	prj.retrofit_all_buildings(2015)
	prj.export_record(model_type = 'AixLib',
                  path = None)

To load our retrofitted building in TEASER lateron, we can save the project into a
XML file::

	prj.save_project("Retrofit_Building",
					path = None)


	
Example_CreateBuilding 
---------------------------------------------

This modeule shows how to create a building from scratch (or arbitrary sources)
calculate parameters for a Modelica model and save this example building in a 
XML based format. The used classes are imported one after another. Of course
you can import all the classes at the beginning.::

	from teaser.Project import Project
	from teaser.Logic.BuildingObjects.Building import Building
	
	prj = Project(load_data = True)
	bldg = Building(parent = prj) 
	
Set some building parameters::
    
    bldg.name = "SuperBuilding"
    bldg.street_name = "Awesome Avenue 42"
    bldg.city = "46325 Fantastic Town"
    bldg.year_of_construction = 1988
    
Instantiate a ThermalZone class, with building as parent and set  some parameters of the thermal zone::

    from teaser.Logic.BuildingObjects.ThermalZone import ThermalZone  
	
    tz = ThermalZone(parent = bldg) 
    tz.name = "Living Room"
    tz.area = 45.0
    tz.volume = 123.0
    tz.infiltration_rate = 0.5
    
Instantiate UseConditionsOffice18599 class with thermal zone as parent, and load the use conditions for the usage 'Living'::
    
    from teaser.Logic.BuildingObjects.TypeBuildings.UseConditionsOffice18599 \
    import UseConditionsOffice18599

    tz.use_conditions = UseConditionsOffice18599(parent = tz)
    tz.use_conditions.load_use_conditions("Living")

Instantiate, each one OuterWall class, InnerWall class and Window class, with thermal zone as parent::

    from teaser.Logic.BuildingObjects.BuildingPhysics.InnerWall import InnerWall
    from teaser.Logic.BuildingObjects.BuildingPhysics.OuterWall import OuterWall
    from teaser.Logic.BuildingObjects.BuildingPhysics.Window import Window

    out_wall = OuterWall(parent = tz)
    in_wall = InnerWall(parent = tz)
    win = Window(parent = tz)
    
Out of typical construction the material properties for inner and outer wall are loaded::

    out_wall.load_type_element(2014,"heavy")
    in_wall.load_type_element(1988, "light")
    

We still need to set some additional attributes::

	out_wall.name = "Outer Wall"
	out_wall.area = 14.0
	out_wall.tilt = 90.0
	out_wall.orientation = 0.0
	
	in_wall.name = "Inner Wall"
	in_wall.area = 28.0
  
We do know the exact properties of the window, thus we set them::
    
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
    
Instantiate a Layer class, with window as parent, set attributes::
	
    from teaser.Logic.BuildingObjects.BuildingPhysics.Layer import Layer
	
    win_layer = Layer(parent = win)
    win_layer.id = 1
    win_layer.thickness = 0.024
	
Instantiate a Material class, with window layer as parent, set attributes::

   from teaser.Logic.BuildingObjects.BuildingPhysics.Material import Material
	
    win_material = Material(parent = win_layer)
    win_material.name = "GlasWindow"
    win_material.thermal_conduc = 0.067
    win_material.transmittance = 0.9

We calculate the RC Values according to ebc procedure::

    prj.calc_all_buildings(calculation_core = 'ebc' )

Export the Modelica Record::

    prj.export_record(model_type "CitiesRWin",
					path = None)
    
Save new TEASER XML::
    
    prj.save_project(file_name = "ExampleProject",
					path = None)