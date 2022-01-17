# -*- coding: utf-8 -*-
"""
This is an example to generate an advanced swimming pool based on 
TEASER example 1 - generate archetype and example 2 - export aixlib models.
Last modified 2021-12-06 for Project 'Energieeffizienz in Schwimmbädern - 
Neubau und Bestand'
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
    # Building Name: Name of swimming pool building.
    # Water area: Used to calculate the size of the zones. Due to the
    # code structure, the value is provided in place of the net leased area.
    # Year of construction: Building construction year without retrofitting.
    # Further parameters are currently not supported for swimming pools.   

    ''' 
    CHANGE PARAMETERS HERE:
    '''
    building_name = "Hallenbad" 
    water_area = 412.5
    year_of_construction = 1980
    excelFileName = "2022-01-17_Swimming pool_Database.xlsx"
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

    # Added buildings are stored within Project.buildings    
    swimmingPool = prj.buildings[0]
    
    # Call method to read out Excel file.    
    # IMPORTANT! Excel file must be closed before compiling code!
    readExcelFile(swimmingPool, excelFileName, prj)  
    
    for zone in swimmingPool.thermal_zones:   
        #if zone.name.startswith("Zone"):
        print ("Added", zone.name, "with zone area:", \
           zone.area, "m²")
    
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
    # will be used. 
    
    print("Exporting building(s)...")
    path = prj.export_aixlib(
        internal_id=None,
        path=filePathOutput)
    return path


def readExcelFile(swimmingPool, fileName, prj):
    """
    Reads out zone and pool data from an Excel file and overrides the data from the 
    previously created basic swimming pool. 
    IMPORTANT: Excel file must be closed! Rows and columns start from 0.    

    Parameters
    ----------
    swimmingPool : object
        Class that stores swimming pool building information.
    fileName : String
        Name of the Excel file.
    prj : Project
        Instance of project class
    """
    
    print("Reading zone data from Excel...")
    wb = xlrd.open_workbook(fileName)
    zoneData = wb.sheet_by_name("Zone Data")
    poolData = wb.sheet_by_name("Pool Data")
    matData = wb.sheet_by_name("Envelope Structures")
    
    # Step 1: Identify the number of zones within the building
    rowZoneName = 2
    rowZoneArea = 17
    colsZoneDataSheet = 17
    for col in range(1, colsZoneDataSheet-1, 2):
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
    colsPoolDataSheet = 12
    existingPools= list()
    for col in range(3, colsPoolDataSheet - 1):
        poolName = convertPoolName(poolData.cell_value(rowPoolName, col))
        poolArea = poolData.cell_value(rowPoolArea, col)
        poolPerimeter = poolData.cell_value(rowPoolPerimeter, col)        
        if poolArea != "" \
        and poolArea != 0:
            existingPools.append(poolName)    
            if poolName not in swimmingPool.poolsInDict.keys():
                swimmingPool.poolsInDict[poolName] = dict()
                swimmingPool.createPool(swimmingPool.poolsInDict, poolName, \
                poolArea, poolPerimeter)

    remList = list()
    for pool in swimmingPool.poolsInDict.keys():
        if not pool.startswith("Zone") and not pool.startswith("Total") \
        and pool not in existingPools:            
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
    for col in range(3, colsPoolDataSheet):
        poolName = convertPoolName(poolData.cell_value(rowPoolName, col))
        poolArea = poolData.cell_value(rowPoolArea, col)
        
        if poolArea != "" and poolArea != 0:
            for row in range(rowPoolArea, poolData.nrows):
                paramName = poolData.cell_value(row, colParamName)
                if poolData.cell_value(row, col) != "" \
                and poolData.cell_value(row, col) != 0: 
                    
                    if paramName in swimmingPool.poolsInDict[poolName].keys() \
                    and paramName != "Construction of pool wall":
                        swimmingPool.poolsInDict[poolName][paramName] = \
                        poolData.cell_value(row, col)
                    elif paramName == "Construction of pool wall":                    
                        if poolData.cell_value(row, col) == "Reinforced concrete":
                            swimmingPool.poolsInDict[poolName][paramName] = \
                            "AixLib.DataBase.Pools.SwimmingPoolWall.ConcreteInsulationConstruction()"
                    else:
                        print()
                        print("ERROR:", paramName, "not found in poolsInDict!")
            print("Added pool", poolName, "with water area:", poolArea, "m²")
    
    swimmingPool.calcPoolParameter()
    
    # Step 5: Read material data
    matDict = dict()
    colThickness = 2
    colMatId = 5
    colElementName = 0   
    elementName = ""
    for row in range(4, matData.nrows):        
        if matData.cell_value(row, colMatId) != "" \
        and matData.cell_value(row, colElementName) != "":
            elementName = matData.cell_value(row, colElementName)
            matDict[elementName] = dict()
            matDict[elementName]["Thickness"] = list()
            matDict[elementName]["Material_Id"] = list()
            matDict[elementName]["Thickness"].append(
                matData.cell_value(row, colThickness)/100)
            matDict[elementName]["Material_Id"].append(
                matData.cell_value(row, colMatId))
            
        elif matData.cell_value(row, colMatId) != "" \
        and matData.cell_value(row, colElementName) == "": 
            matDict[elementName]["Thickness"].append(
                matData.cell_value(row, colThickness)/100)
            matDict[elementName]["Material_Id"].append(
                matData.cell_value(row, colMatId)) 
        
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
    swimmingPool.poolsInDict[zoneName]["Outer wall area north"] = \
        zoneData.cell_value(4, col + 1)
    swimmingPool.poolsInDict[zoneName]["Outer wall area east"] = \
        zoneData.cell_value(5, col + 1)
    swimmingPool.poolsInDict[zoneName]["Outer wall area south"] = \
        zoneData.cell_value(6, col + 1)
    swimmingPool.poolsInDict[zoneName]["Outer wall area west"] = \
        zoneData.cell_value(7, col + 1)
    swimmingPool.poolsInDict[zoneName]["Transparent element in outer wall north"] = \
        zoneData.cell_value(8, col + 1)
    swimmingPool.poolsInDict[zoneName]["Transparent element in outer wall east"] = \
        zoneData.cell_value(9, col + 1)
    swimmingPool.poolsInDict[zoneName]["Transparent element in outer wall south"] = \
        zoneData.cell_value(10, col + 1)
    swimmingPool.poolsInDict[zoneName]["Transparent element in outer wall west"] = \
        zoneData.cell_value(11, col + 1)
    swimmingPool.poolsInDict[zoneName]["Roof area"] = \
        zoneData.cell_value(12, col + 1)
    swimmingPool.poolsInDict[zoneName]["Ground floor area"] = \
        zoneData.cell_value(13, col + 1)
    swimmingPool.poolsInDict[zoneName]["Inner walls as a sum"] = \
        zoneData.cell_value(14, col + 1)
    swimmingPool.poolsInDict[zoneName]["Ceiling area"] = \
        zoneData.cell_value(15, col + 1)
    swimmingPool.poolsInDict[zoneName]["Floor area"] = \
        zoneData.cell_value(16, col + 1)
    swimmingPool.poolsInDict[zoneName]["Total area of zone (including water area)"] = \
        zoneData.cell_value(17, col + 1)
    swimmingPool.poolsInDict[zoneName]["Air volume"] = \
        zoneData.cell_value(18, col + 1)      

    swimmingPool.zone_area_factors[swimmingPool.zoneDesignation[zoneName]] = \
        [swimmingPool.poolsInDict[zoneName] \
         ["Total area of zone (including water area)"], \
         swimmingPool.poolsInDict[zoneName]["Air volume"], \
         swimmingPool.zoneUseConditions[zoneName]]  


def overrideZoneData(swimmingPool):
    
    # Note: Reseting of building element areas for the entire building not needed. 
    # They are automatically replaced within the method "def area(self, value)" 
    # within the classes thermalzone and buildingelement.
    
    for zone in swimmingPool.thermal_zones:
        # General data
        zone.area = swimmingPool.poolsInDict[
            swimmingPool.zoneDesignation[zone.name]] \
            ["Total area of zone (including water area)"]
            
        zone.volume = swimmingPool.poolsInDict[
            swimmingPool.zoneDesignation[zone.name]] \
            ["Air volume"]
        
        # building elements:
        zone.outer_walls[0].area = 0.001
        if swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Outer wall area north"] != 0:
            zone.outer_walls[0].area = \
                swimmingPool.poolsInDict[
                    swimmingPool.zoneDesignation[zone.name]]["Outer wall area north"]
        zone.outer_walls[1].area = 0.001
        if swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Outer wall area east"] != 0:
            zone.outer_walls[1].area = \
                swimmingPool.poolsInDict[
                    swimmingPool.zoneDesignation[zone.name]]["Outer wall area east"]
        zone.outer_walls[2].area = 0.001
        if swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Outer wall area south"] != 0:
            zone.outer_walls[2].area = \
                swimmingPool.poolsInDict[
                    swimmingPool.zoneDesignation[zone.name]]["Outer wall area south"]
        zone.outer_walls[3].area = 0.001
        if swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Outer wall area west"] != 0:
            zone.outer_walls[3].area = \
                swimmingPool.poolsInDict[
                    swimmingPool.zoneDesignation[zone.name]]["Outer wall area west"]
        zone.windows[0].area = 0.001
        if swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]] \
                    ["Transparent element in outer wall north"] != 0:
            zone.windows[0].area = swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]] \
                    ["Transparent element in outer wall north"]
        zone.windows[1].area = 0.001
        if swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]] \
                    ["Transparent element in outer wall east"] != 0:
            zone.windows[1].area = swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]] \
                    ["Transparent element in outer wall east"]
        zone.windows[2].area = 0.001
        if swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]] \
                    ["Transparent element in outer wall south"] != 0:
            zone.windows[2].area = swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]] \
                    ["Transparent element in outer wall south"]
        zone.windows[3].area = 0.001
        if swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]] \
                    ["Transparent element in outer wall west"] != 0:
            zone.windows[3].area = swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]] \
                    ["Transparent element in outer wall west"]
        zone.rooftops[0].area = 0.001
        if swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Roof area"] != 0:        
            zone.rooftops[0].area = swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Roof area"]
        zone.ground_floors[0].area = 0.001
        if swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Ground floor area"] != 0:        
            zone.ground_floors[0].area = swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Ground floor area"]
        zone.inner_walls[0].area = 0.001
        if swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Inner walls as a sum"] != 0:
            zone.inner_walls[0].area = \
            swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Inner walls as a sum"] 


def convertPoolName(poolName):
    #Removes numbers at the end of pool names
    for i in range(0, len(poolName)):
        if poolName[i] == "n" and poolName[i-1] == "e":            
            poolName = poolName[0:i+1]
            break
    return poolName

def setThermalConductionWindows(swimmingPool, thermal_conduc):
    for zone in swimmingPool.thermal_zones:
        for win in zone.windows:
            for layer in win.layer:
                layer.material.thermal_conduc = thermal_conduc

if __name__ == '__main__':
    prj = generate_advanced_swimmingPool()
    print()
    print("SwimmingPool(s) exported successfully. That's it! :)")