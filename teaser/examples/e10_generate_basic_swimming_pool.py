# -*- coding: utf-8 -*-
"""
This is an example to generate a basic swimming pool based on 
TEASER example 1 - generate archetype and example 2 - export aixlib models.
Last modified 2021-11-15 for Project 'Energieeffizienz in Schwimmbädern - 
Neubau und Bestand'
"""
import teaser.logic.utilities as utilities
import os

def generate_basic_swimmingPool():

    # First step: Import the TEASER API (called Project) into your Python
    # module
    
    from teaser.project import Project

    # To use the API, instantiate the Project class and rename the Project. The
    # parameter load_data=True indicates that we load `iwu` typology archetype
    # data into our Project (e.g. for Material properties and typical wall
    # constructions. This can take a few seconds, depending on the size of the
    # used data base). Be careful: Dymola does not like whitespaces in names and
    # filenames, thus we will delete them anyway in TEASER.
    
    prj = Project(load_data=True)
    prj.name = "Output_Swimming_Pool_Basic_Model"

    # To generate non-residential archetype buildings the function
    # Project.add_non_residential() is used. 
    # The following parameters need to be provided for swimming pools:
    # Building Name: Name of swimming pool building.
    # Water area: Used to calculate the size of the zones. Due to the
    # code structure, the value is provided in place of the net leased area.
    # Year of construction: Building construction year without retrofitting.
    # Further parameters are currently not supported for swimming pools.    

    ''' 
    CHANGE PARAMETERS HERE:
    '''
    building_name = "SwimmingFacility"
    water_area = 412.5
    year_of_construction = 1980
    filePathOutput = None

    # This should not be changed for now:
    prj.add_non_residential(
        method='bmvbs',
        usage='swimmingPool',
        name=building_name,
        year_of_construction=year_of_construction,
        number_of_floors=1,
        height_of_floors=3.5,
        net_leased_area=water_area,
        internal_gains_mode=3)
    
    # Added buildings are stored within Project.buildings. The following code is
    # optional and should provide some basic information about the calculated 
    # building within the console.   
    
    swimmingPool = prj.buildings[0]
    for zone in swimmingPool.poolsInDict.keys():   
        if zone.startswith("Zone"):
            print ("Added", swimmingPool.zoneDesignation[zone],  "with zone area:", \
               swimmingPool.poolsInDict[zone]\
               ["Total area of zone (including water area)"], "m²")    
  
    print()
    print("Total net leased area of building:", swimmingPool.net_leased_area, "m²")
    print("Total air volume of building:", swimmingPool.volume, "m³")
    print() 

    # Set the calculation libary and provide the weather data for Modelica.
    # For swimming pools, number of elements is set to 4, so outer walls,
    # roof and the ground floor are treated as separate elements.
    
    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 4
    prj.weather_file_path = utilities.get_full_path(
        os.path.join(
            "data",
            "input",
            "inputdata",
            "weatherdata",
            "DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos"))

    # To make sure the parameters are calculated correctly we recommend to
    # run calc_all_buildings() function
    
    prj.calc_all_buildings()

    # To export the ready-to-run models simply call Project.export_aixlib().
    # You can specify the path, where the model files should be saved.
    # None means, that the default path in your home directory
    # will be used. 
    
    print("Exporting building(s)...")
    path = prj.export_aixlib(
        internal_id=None,
        path=filePathOutput)
    
    return path

if __name__ == '__main__':
    prj = generate_basic_swimmingPool()
    print()
    print("SwimmingPool(s) exported successfully. That's it! :)")