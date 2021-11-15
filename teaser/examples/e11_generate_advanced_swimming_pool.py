# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:22:07 2020
This is a test module to generate swimming pools based on 
teaser example 1 - generate archetype and example 2 - export aixlib models.
Last modified 2021-11-08 for Project 'Energieeffizienz in Schwimmbädern - Neubau und Bestand'
"""
import teaser.logic.utilities as utilities
import os
import xlrd
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.useconditions import UseConditions as UseCond
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.data.input import material_input_json as matInput

def generate_advanced_swimmingPool():

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
    The basic swimming pool is calculated from the WATER SURFACE. Please enter the respective WATER SURFACE
    for the parameter net_leased_area. 
    """

    prj.add_non_residential(
        method='bmvbs',
        usage='swimmingPool',
        name="Hallenbad",
        year_of_construction=1980,
        number_of_floors=1,
        height_of_floors=4.2,
        net_leased_area=412.5,
        internal_gains_mode=3)

    # Please note: as we need to load the construction information which are
    # rather big for TABULA, switching from one typology to another in the same
    # Project takes some seconds. If you know from beginning you will only use
    # TABULA typology you should instantiate you Project class without loading
    # data. Project(load_data=False).
    
    swimmingPool = prj.buildings[0]
        
    """ IMPORTANT! Excel file must be closed before compiling code!"""
    readExcelFile(swimmingPool, "2021-11-08_Swimming pool data.xlsx", prj)  
    
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

def readExcelFile(swimmingPool, fileName, prj):
    """
    Reads out zone and pool data from an Excel file and overrides the data from the previously created
    basic swimming pool. 
    Important: Rows and columns start from 0!
    

    Parameters
    ----------
    swimmingPool : object
        Class that stores swimming pool building information.
    fileName : String
        Name of the Excel file.
    prj : Project
        instance of project class
    """
    
    print("Reading zone data from Excel...")
    wb = xlrd.open_workbook(fileName)
    zoneData = wb.sheet_by_name("Zone Data")
    poolData = wb.sheet_by_name("Pool Data")
    matData = wb.sheet_by_name("Envelope Structures")
    
    # Step 1: Identify the number of zones within the building
    rowZoneName = 2
    rowZoneArea = 18     
    for col in range(1, zoneData.ncols-1, 2):
        zoneName = zoneData.cell_value(rowZoneName, col)
        zoneArea = zoneData.cell_value(rowZoneArea, col+1)
        if zoneArea != "" \
        and zoneArea != 0 \
        and zoneName not in swimmingPool.poolsInDict.keys():
            swimmingPool.poolsInDict[zoneName] = dict()
        if zoneName in swimmingPool.poolsInDict.keys(): 
            readZoneData(swimmingPool, zoneData, zoneName, rowZoneName, col)
            
    # Step 2: Override the available data for each zone        
    addBuildingZones(swimmingPool)
    overrideZoneData(swimmingPool)
    swimmingPool.net_leased_area = round(swimmingPool.net_leased_area, 2)
    swimmingPool.volume = round(swimmingPool.volume, 2)
                
    # Step 3: Identify the number and type of pools within the building
    rowPoolName = 3
    rowPoolArea = 4  
    rowPoolPerimeter = 7
    existingPools= list()
    for col in range(3, poolData.ncols-1):
        poolName = convertPoolName(poolData.cell_value(rowPoolName, col))
        poolArea = poolData.cell_value(rowPoolArea, col)
        poolPerimeter = poolData.cell_value(rowPoolPerimeter, col)        
        if poolArea != "" \
        and poolArea != 0:
            existingPools.append(poolName)    
            if poolName not in swimmingPool.poolsInDict.keys():
                swimmingPool.poolsInDict[poolName] = dict()
                swimmingPool.createPool(swimmingPool.poolsInDict, poolName, poolArea, poolPerimeter)

    remList = list()
    for pool in swimmingPool.poolsInDict.keys():
        if not pool.startswith("Zone") and not pool.startswith("Total") and pool not in existingPools:            
            remList.append(pool)      
    for zone in swimmingPool.thermal_zones:
        if zone.name == "Schwimmhalle":
            for pool in remList:        
                swimmingPool.poolsInDict.pop(pool)
                zone.paramRecord.pop(pool)
            for pool in existingPools:
                if pool not in zone.paramRecord.keys():
                    zone.paramRecord[pool] = dict()
            
    # Step 4: Override pool data from basic swimming pool
    colParamName = 0    
    for col in range(3, poolData.ncols-1):
        poolName = convertPoolName(poolData.cell_value(rowPoolName, col))
        poolArea = poolData.cell_value(rowPoolArea, col)
        
        if poolArea != "" and poolArea != 0:
            for row in range(rowPoolArea, poolData.nrows):
                paramName = poolData.cell_value(row, colParamName)
                if poolData.cell_value(row, col) != "" \
                and poolData.cell_value(row, col) != 0: 
                    
                    if paramName in swimmingPool.poolsInDict[poolName].keys() \
                    and paramName != "Construction of pool wall":
                        swimmingPool.poolsInDict[poolName][paramName] = poolData.cell_value(row, col)
                    elif paramName == "Construction of pool wall":                    
                        if poolData.cell_value(row, col) == "Reinforced concrete":
                            swimmingPool.poolsInDict[poolName][paramName] = \
                            "AixLib.DataBase.Pools.SwimmingPoolWall.ConcreteConstruction()"
                    else:
                        print("ERROR:", paramName, "not found in poolsInDict")
            print("Added pool", poolName, "with water surface:", poolArea, "m²")
    
    swimmingPool.calcPoolParameter()
    
    # Step 5: Read material data
    matDict = dict()
    colThickness = 4
    colMatId = 5
    colElementName = 0   
    elementName = ""
    for row in range(3, matData.nrows):        
        if matData.cell_value(row, colMatId) != "" and matData.cell_value(row, colElementName) != "":
            elementName = matData.cell_value(row, colElementName)
            matDict[elementName] = dict()
            matDict[elementName]["Thickness"] = list()
            matDict[elementName]["Material_Id"] = list()
            matDict[elementName]["Thickness"].append(matData.cell_value(row, colThickness))
            matDict[elementName]["Material_Id"].append(matData.cell_value(row, colMatId))
            
        elif matData.cell_value(row, colMatId) != "" and matData.cell_value(row, colElementName) == "": 
            matDict[elementName]["Thickness"].append(matData.cell_value(row, colThickness))
            matDict[elementName]["Material_Id"].append(matData.cell_value(row, colMatId)) 
        
    # Step 6: Set material data
    for zone in swimmingPool.thermal_zones:
        overrideMaterialData(zone, matDict, prj)
                    
def overrideMaterialData(zone, matDict, prj):
    for wall in zone.outer_walls:
        wallName = type(wall).__name__
        if wallName in matDict.keys():                
            wall.layer = None       
            for numLayer in range(0, len(matDict[wallName]["Thickness"])):
                mat_id = matDict[wallName]["Material_Id"][numLayer]
                thickness = matDict[wallName]["Thickness"][numLayer]
                layer = Layer(parent = wall, id = numLayer)
                layer.thickness = thickness
                material = Material(layer)
                matInput.load_material_id(material, mat_id, prj.data)
                    
        for wall in zone.inner_walls:
            wallName = type(wall).__name__
            if wallName in matDict.keys():                
                wall.layer = None       
                for numLayer in range(0, len(matDict[wallName]["Thickness"])):
                    mat_id = matDict[wallName]["Material_Id"][numLayer]
                    thickness = matDict[wallName]["Thickness"][numLayer]
                    layer = Layer(parent = wall, id = numLayer)
                    layer.thickness = thickness
                    material = Material(layer)
                    matInput.load_material_id(material, mat_id, prj.data)
                    
        for rooftop in zone.rooftops:
            rooftopName = type(rooftop).__name__
            if rooftopName in matDict.keys():                
                rooftop.layer = None       
                for numLayer in range(0, len(matDict[rooftopName]["Thickness"])):
                    mat_id = matDict[rooftopName]["Material_Id"][numLayer]
                    thickness = matDict[rooftopName]["Thickness"][numLayer]
                    layer = Layer(parent = rooftop, id = numLayer)
                    layer.thickness = thickness
                    material = Material(layer)
                    matInput.load_material_id(material, mat_id, prj.data)
                    
        for floor in zone.ground_floors:
            floorName = type(floor).__name__
            if floorName in matDict.keys():                
                floor.layer = None       
                for numLayer in range(0, len(matDict[floorName]["Thickness"])):
                    mat_id = matDict[floorName]["Material_Id"][numLayer]
                    thickness = matDict[floorName]["Thickness"][numLayer]
                    layer = Layer(parent = floor, id = numLayer)
                    layer.thickness = thickness
                    material = Material(layer)
                    matInput.load_material_id(material, mat_id, prj.data)
                    
        for floor in zone.floors:
            floorName = type(floor).__name__
            if floorName in matDict.keys():                
                floor.layer = None       
                for numLayer in range(0, len(matDict[floorName]["Thickness"])):
                    mat_id = matDict[floorName]["Material_Id"][numLayer]
                    thickness = matDict[floorName]["Thickness"][numLayer]
                    layer = Layer(parent = floor, id = numLayer)
                    layer.thickness = thickness
                    material = Material(layer)
                    matInput.load_material_id(material, mat_id, prj.data)
                    
        for ceiling in zone.ceilings:
            ceilingName = type(ceiling).__name__
            if ceilingName in matDict.keys():                
                ceiling.layer = None       
                for numLayer in range(0, len(matDict[ceilingName]["Thickness"])):
                    mat_id = matDict[ceilingName]["Material_Id"][numLayer]
                    thickness = matDict[ceilingName]["Thickness"][numLayer]
                    layer = Layer(parent = ceiling, id = numLayer)
                    layer.thickness = thickness
                    material = Material(layer)
                    matInput.load_material_id(material, mat_id, prj.data)
                    
        for window in zone.windows:
            windowName = type(window).__name__
            if windowName in matDict.keys():                
                window.layer = None       
                for numLayer in range(0, len(matDict[windowName]["Thickness"])):
                    mat_id = matDict[windowName]["Material_Id"][numLayer]
                    thickness = matDict[windowName]["Thickness"][numLayer]
                    layer = Layer(parent = window, id = numLayer)
                    layer.thickness = thickness
                    material = Material(layer)
                    matInput.load_material_id(material, mat_id, prj.data)

def addBuildingZones(swimmingPool):
    for zoneName, value in swimmingPool.zone_area_factors.items():
        if zoneName == "Saunabereich" or zoneName == "Fitness":
            zone = ThermalZone(swimmingPool)
            # swimmingPool.thermal_zones.add_zone(zone)
            zone.area = value[0] 
            zone.volume = value[1]
            zone.name = zoneName
            use_cond = UseCond(zone)
            use_cond.load_use_conditions(value[2], data_class=swimmingPool.parent.data)
            zone.use_conditions = use_cond
            
            # OUTER WALLS #
            for key, value in swimmingPool.outer_wall_names.items():
                #Creates an outer wall for each zone and assigns building elements  
                outer_wall = OuterWall(zone)
                outer_wall.name = key
                outer_wall.load_type_element(
                    year=swimmingPool.year_of_construction,
                    construction=swimmingPool.construction_type,
                    data_class=swimmingPool.parent.data)               
                outer_wall.tilt = value[0]
                outer_wall.orientation = value[1]
                
            # WINDOWS #        
            for key, value in swimmingPool.window_names.items():                        
                window = Window(zone)
                window.name = key
                window.load_type_element(
                    swimmingPool.year_of_construction,
                    "Kunststofffenster, " "Isolierverglasung",
                    data_class=swimmingPool.parent.data)                
                window.tilt = value[0]
                window.orientation = value[1]     
                    
            # ROOFTOPS #
            for key, value in swimmingPool.roof_names.items():
                roof = Rooftop(zone)
                roof.name = key
                roof.load_type_element(
                    year=swimmingPool.year_of_construction,
                    construction=swimmingPool.construction_type,
                    data_class=swimmingPool.parent.data)
                roof.tilt = value[0]
                roof.orientation = value[1]
            
            # GROUNDFLOORS #
            for key, value in swimmingPool.ground_floor_names.items(): 
                ground_floor = GroundFloor(zone)
                ground_floor.name = key
                ground_floor.load_type_element(
                    year=swimmingPool.year_of_construction,
                    construction=swimmingPool.construction_type,
                    data_class=swimmingPool.parent.data)
                ground_floor.tilt = value[0]
                ground_floor.orientation = value[1]
                    
            # INNER WALLS #
            for key, value in swimmingPool.inner_wall_names.items():    
                inner_wall = InnerWall(zone)
                inner_wall.name = key
                inner_wall.load_type_element(
                    year=swimmingPool.year_of_construction,
                    construction=swimmingPool.construction_type,
                    data_class=swimmingPool.parent.data)
                inner_wall.tilt = value[0]
                inner_wall.orientation = value[1]   
    
            if swimmingPool.number_of_floors > 1:
                # CEILINGS #
                for key, value in swimmingPool.ceiling_names.items(): 
                    ceiling = Ceiling(zone)
                    ceiling.name = key
                    ceiling.load_type_element(
                        year=swimmingPool.year_of_construction,
                        construction=swimmingPool.construction_type,
                        data_class=swimmingPool.parent.data)
                    ceiling.tilt = value[0]
                    ceiling.orientation = value[1] 
            
                # FLOORS #   
                for key, value in swimmingPool.floor_names.items():
                    floor = Floor(zone)
                    floor.name = key
                    floor.load_type_element(
                        year=swimmingPool.year_of_construction,
                        construction=swimmingPool.construction_type,
                        data_class=swimmingPool.parent.data)
                    floor.tilt = value[0]
                    floor.orientation = value[1] 

                    
def readZoneData(swimmingPool, zoneData, zoneName, rowZoneName, col):         
    swimmingPool.poolsInDict[zoneName]["Outer wall area north"] = zoneData.cell_value(4, col + 1)
    swimmingPool.poolsInDict[zoneName]["Outer wall area east"] = zoneData.cell_value(5, col + 1)
    swimmingPool.poolsInDict[zoneName]["Outer wall area south"] = zoneData.cell_value(6, col + 1)
    swimmingPool.poolsInDict[zoneName]["Outer wall area west"] = zoneData.cell_value(7, col + 1)
    swimmingPool.poolsInDict[zoneName]["Transparent element in outer wall north"] = \
        zoneData.cell_value(8, col + 1)
    swimmingPool.poolsInDict[zoneName]["Transparent element in outer wall east"] = \
        zoneData.cell_value(9, col + 1)
    swimmingPool.poolsInDict[zoneName]["Transparent element in outer wall south"] = \
        zoneData.cell_value(10, col + 1)
    swimmingPool.poolsInDict[zoneName]["Transparent element in outer wall west"] = \
        zoneData.cell_value(11, col + 1)
    swimmingPool.poolsInDict[zoneName]["Roof area"] = zoneData.cell_value(12, col + 1)
    swimmingPool.poolsInDict[zoneName]["Ground floor area"] = zoneData.cell_value(13, col + 1)
    swimmingPool.poolsInDict[zoneName]["Inner walls as a sum"] = zoneData.cell_value(14, col + 1)
    swimmingPool.poolsInDict[zoneName]["Ceiling area"] = zoneData.cell_value(15, col + 1)
    swimmingPool.poolsInDict[zoneName]["Floor area"] = zoneData.cell_value(16, col + 1)
    swimmingPool.poolsInDict[zoneName]["Total area of zone (including water surface)"] = \
        zoneData.cell_value(17, col + 1)
    swimmingPool.poolsInDict[zoneName]["Air volume"] = zoneData.cell_value(18, col + 1)      

    swimmingPool.zone_area_factors[swimmingPool.zoneDesignation[zoneName]] = \
        [swimmingPool.poolsInDict[zoneName]["Total area of zone (including water surface)"], \
         swimmingPool.poolsInDict[zoneName]["Air volume"], \
         swimmingPool.zoneUseConditions[zoneName]]  

    print ("Added", swimmingPool.zoneDesignation[zoneName], "with zone area:", \
       swimmingPool.poolsInDict[zoneName]["Total area of zone (including water surface)"], "m²")

def overrideZoneData(swimmingPool):
    
    # Reset building areas
    swimmingPool.outer_area[0] = 0
    swimmingPool.outer_area[90] = 0
    swimmingPool.outer_area[180] = 0
    swimmingPool.outer_area[270] = 0
    swimmingPool.outer_area[-1] = 0
    swimmingPool.outer_area[-2] = 0
    swimmingPool.window_area[0] = 0
    swimmingPool.window_area[90] = 0
    swimmingPool.window_area[180] = 0
    swimmingPool.window_area[270] = 0
    swimmingPool.net_leased_area = 0
    swimmingPool.volume = 0
    
    for zone in swimmingPool.thermal_zones:
        zone.outer_walls[0].area = 0.001
        if swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Outer wall area north"] != 0:
            zone.outer_walls[0].area = \
                swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Outer wall area north"]
        zone.outer_walls[1].area = 0.001
        if swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Outer wall area east"] != 0:
            zone.outer_walls[1].area = \
                swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Outer wall area east"]
        zone.outer_walls[2].area = 0.001
        if swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Outer wall area south"] != 0:
            zone.outer_walls[2].area = \
                swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Outer wall area south"]
        zone.outer_walls[3].area = 0.001
        if swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Outer wall area west"] != 0:
            zone.outer_walls[3].area = \
                swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Outer wall area west"]
        zone.windows[0].area = 0.001
        if swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]\
        ["Transparent element in outer wall north"] != 0:
            zone.windows[0].area = \
                swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]] \
                ["Transparent element in outer wall north"]
        zone.windows[1].area = 0.001
        if swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]] \
        ["Transparent element in outer wall east"] != 0:
            zone.windows[1].area = \
                swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]] \
                ["Transparent element in outer wall east"]
        zone.windows[2].area = 0.001
        if swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]] \
        ["Transparent element in outer wall south"] != 0:
            zone.windows[2].area = \
                swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]] \
                ["Transparent element in outer wall south"]
        zone.windows[3].area = 0.001
        if swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]] \
        ["Transparent element in outer wall west"] != 0:
            zone.windows[3].area = \
                swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]] \
                ["Transparent element in outer wall west"]
        zone.rooftops[0].area = 0.001
        if swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Roof area"] != 0:        
            zone.rooftops[0].area = \
                swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Roof area"]
        zone.ground_floors[0].area = 0.001
        if swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Ground floor area"] != 0:        
            zone.ground_floors[0].area = \
                swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Ground floor area"]
        zone.inner_walls[0].area = 0.001
        if swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Inner walls as a sum"] != 0:
            zone.inner_walls[0].area = \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Inner walls as a sum"] 
    
        swimmingPool.outer_area[0] += \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Outer wall area north"]
        swimmingPool.outer_area[90] += \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Outer wall area east"]
        swimmingPool.outer_area[180] += \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Outer wall area south"]
        swimmingPool.outer_area[270] += \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Outer wall area west"]
        swimmingPool.window_area[0] += \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Transparent element in outer wall north"]
        swimmingPool.window_area[90] += \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Transparent element in outer wall east"]
        swimmingPool.window_area[180] += \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Transparent element in outer wall south"]
        swimmingPool.window_area[270] += \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Transparent element in outer wall west"]
        swimmingPool.outer_area[-1] += \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Roof area"]
        swimmingPool.outer_area[-2] += \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Ground floor area"]
        swimmingPool.net_leased_area += \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]] \
            ["Total area of zone (including water surface)"]
        swimmingPool.volume += \
            swimmingPool.poolsInDict[swimmingPool.zoneDesignation[zone.name]]["Air volume"]

def convertPoolName(poolName):
    for i in range(0, len(poolName)):
        if poolName[i] == "n" and poolName[i-1] == "e":            
            poolName = poolName[0:i+1]
            break
    return poolName

if __name__ == '__main__':
    prj = generate_advanced_swimmingPool()
    print()
    print("SwimmingPool(s) exported successfully. That's it! :)")