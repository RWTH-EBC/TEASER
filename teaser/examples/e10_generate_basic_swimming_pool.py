# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:22:07 2020
This is a test module to generate swimming pools based on 
teaser example 1 - generate archetype and example 2 - export aixlib models.
Further implementations enable the data import from an Excel file.
Last modified 2021-11-08 for Project 'Energieeffizienz in Schwimmbädern - Neubau und Bestand'
"""
import teaser.logic.utilities as utilities
import os

def generate_basic_swimmingPool():

    # First step: Import the TEASER API (called Project) into your Python
    # module

    from teaser.project import Project

    # To use the API instantiate the Project class and rename the Project. The
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
    # Method "bmvbs" (placeholder), usage "swimmingPool", name,
    # year of construction, number of floors, height of floors,
    # net_leased_area, internal_gains_mode = 3, filePath to Excel file,
    # sheetNameAreas to provide the sheet name within the Excel file, 
    # that stores area values, sheetNameElements for building elements.
    # swimmingPoolCategory (placeholder)
    
    """
    The basic swimming pool is calculated from the WATER SURFACE. Please enter the respective WATER SURFACE
    for the parameter net_leased_area. 
    """
    building_name = "Hallenbad"
    water_area = 412.5
    year_of_construction = 1980
    number_of_floors = 1
    height_of_floors = 4.2

    prj.add_non_residential(
        method='bmvbs',
        usage='swimmingPool',
        name=building_name,
        year_of_construction=year_of_construction,
        number_of_floors=number_of_floors,
        height_of_floors=height_of_floors,
        net_leased_area=water_area,
        internal_gains_mode=3)

    # Please note: as we need to load the construction information which are
    # rather big for TABULA, switching from one typology to another in the same
    # Project takes some seconds. If you know from beginning you will only use
    # TABULA typology you should instantiate you Project class without loading
    # data. Project(load_data=False).
    
    for bldg in prj.buildings: 
        if bldg.name == "Hallenbad":        
            swimmingPool = bldg
    for zone in swimmingPool.poolsInDict.keys():   
        if zone.startswith("Zone"):
            print ("Added", swimmingPool.zoneDesignation[zone],  "with zone area:", \
               swimmingPool.poolsInDict[zone]["Total area of zone (including water surface)"], "m²")    
  
    print()
    print("Total net leased area of building:", swimmingPool.net_leased_area, "m²")
    print("Total air volume of building:", swimmingPool.volume, "m³")
    print() 

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
    # will be used. If you only want to export one specific building, you can
    # pass over the internal_id of that building and only this model will be
    # exported. In this case we want to export all buildings to our home
    # directory, thus we are passing over None for both parameters.
    
    print("Exporting building(s)...")
    path = prj.export_aixlib(
        internal_id=None,
        path=None)
    
    return path

if __name__ == '__main__':
    prj = generate_basic_swimmingPool()
    print()
    print("SwimmingPool(s) exported successfully. That's it! :)")