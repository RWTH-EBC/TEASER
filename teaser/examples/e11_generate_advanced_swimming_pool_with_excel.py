# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:22:07 2020
This is a test module to generate swimming pools based on 
teaser example 1 - generate archetype and example 2 - export aixlib models.
Last modified 2020-09-25 for Project 'Energieeffizienz in Schwimmbädern - Neubau und Bestand'
"""
import teaser.logic.archetypebuildings.eeschwimm.swimmingPool as swimmingPool
import teaser.logic.utilities as utilities
import os

def test_generate_swimmingPool():

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
    prj.name = "Output_Swimming_Pool_Advanced_Model"


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
    Please specify the following data.
    """
    
    # xlrd library will no longer read anything other than .xls files!!
    filePath=os.path.join(os.path.dirname(__file__),"2021-04-14_Hüllflächen_Zonen_Shells_of_Zones.xls")
    sheetNameAreas='Hüllflächen, Himmelsricht.'
    sheetNameElements='Strukturen Hüllfläche'
    swimmingPoolCategory='A2'

    """
    Contrary to the basic model, the parameter net_leased_area corresponds to the actual net leased area
    of the building, since the additional pool data is stored in the excel file.
    """
    
    prj.add_non_residential(
        method='bmvbs',
        usage='swimmingPool',
        name="Hallenbad",
        year_of_construction=1980,
        number_of_floors=1,
        height_of_floors=4.2,
        net_leased_area=2056.9,
        internal_gains_mode=3,
        filePath=filePath, 
        sheetNameAreas=sheetNameAreas,        
        sheetNameElements=sheetNameElements,
        swimmingPoolCategory=swimmingPoolCategory)

    # Please note: as we need to load the construction information which are
    # rather big for TABULA, switching from one typology to another in the same
    # Project takes some seconds. If you know from beginning you will only use
    # TABULA typology you should instantiate you Project class without loading
    # data. Project(load_data=False).
    
    print()
    print("Archetype(s) of indoor pool(s) successfully generated!")
    print()
    print("Excel File was read out from: ")
    print(filePath)
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

    # Deletes empty zones and pushs the "thermal zones" wich are Pools in the zone "Schwimmhalle" 
    # in the parameter "pool_zones" and delets it out of the thermal zones 
    # it should be considered that, that the function is called after all calculations 
    # directly before the export, otherwise problems can occur when handling the thermal zones. 
    for bldgs in prj.buildings:
        bldgs.orderPoolZones()

    # To export the ready-to-run models simply call Project.export_aixlib().
    # You can specify the path, where the model files should be saved.
    # None means, that the default path in your home directory
    # will be used. If you only want to export one specific building, you can
    # pass over the internal_id of that building and only this model will be
    # exported. In this case we want to export all buildings to our home
    # directory, thus we are passing over None for both parameters.

    path = prj.export_aixlib(
        internal_id=None,
        path=None)

    return path



if __name__ == '__main__':
    prj = test_generate_swimmingPool()

    print("Test SwimmingPool: That's it! :)")