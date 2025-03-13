# -*- coding: utf-8 -*-
"""
This is an example to generate an advanced swimming pool based on 
TEASER example 1 - generate archetype and example 2 - export aixlib models.
Last modified 2021-12-06 for Project 'Energieeffizienz in Schwimmbädern - 
Neubau und Bestand'
"""
import teaser.logic.utilities as utilities
import os
#import xlrd
import pandas as pd
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
from teaser.logic.buildingobjects.buildingsystems.pool import Pool
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

    prj = Project()
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
    --- CHANGE PARAMETERS HERE ---
    '''
    building_name = "Hallenbad"
    water_area = 550.0
    year_of_construction = 2012
    excelFileName = "Swimming pool_Database.xlsx"
    filePathOutput = None


    prj.add_non_residential(
        construction_data='iwu_heavy',
        geometry_data='swimming_facility',
        name=building_name,
        year_of_construction=year_of_construction,
        number_of_floors=2,
        height_of_floors=3.5,
        net_leased_area=water_area,
        with_ahu=True,
        internal_gains_mode=3
        )

    # Added buildings are stored within Project.buildings    
    swimmingFacitlity = prj.buildings[0]
    
    # Read data from excel and set values for zones, pools and material
    readExcelFile(swimmingFacitlity, excelFileName, prj)

    print("Your individual swimming facility includes:")
    for zone in swimmingFacitlity.thermal_zones:
        print(zone.name, "with zone area:", zone.area, " m²")
    for pool in swimmingFacitlity.thermal_zones[0].pools:
        print(pool.name, "with water area:", pool.area, " m²")
    
    print()
    print("Total net leased area of building:", swimmingFacitlity.net_leased_area, "m²")
    print("Total air volume of building:", swimmingFacitlity.volume, "m³")
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

    # scale heater of all zones to ensure enough power
    for bld in prj.buildings:
        for zone in bld.thermal_zones:
            zone.model_attr.heat_load *= 100


    # To export the ready-to-run models simply call Project.export_aixlib().
    # You can specify the path, where the model files should be saved.
    # None means, that the default path in your home directory
    # will be used. 
    
    print("Exporting building(s)...")
    path = prj.export_aixlib(
        internal_id=None,
        path=filePathOutput,
        use_postprocessing_calc=True)
    return path


def readExcelFile(swimmingFacitlity, fileName, prj):
    """
    Reads out zone and pool data from an Excel file and overrides the data from the 
    previously created basic swimming pool.

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
    print()
    zoneData = pd.read_excel(fileName,sheet_name="Zone Data", header=2, index_col=0)
    poolData = pd.read_excel(fileName,sheet_name="Pool Data", header=3, index_col=0)
    matData = pd.read_excel(fileName, sheet_name="Envelope Structures", header=2)



    for zone in swimmingFacitlity.thermal_zones:
        print('Start overwriting default data with individual data.')
        i = 0
        # Set area of outer walls and windows
        for dir in range(4):
            # outer wall
            if zoneData[zone.name].values[dir] > 0.0:
                zone.outer_walls[dir].area = zoneData[zone.name].values[dir]
            else:
                zone.outer_walls[dir].area = 0.0001
            # windows
            if zoneData[zone.name].values[dir+4] > 0.0:
                zone.windows[dir].area = zoneData[zone.name].values[dir+4]
            else:
                zone.windows[dir].area = 0.0001



        # Set area of rooftop
        if zoneData[zone.name].values[8] > 0:
            print(zone.rooftops[0].area)
            print(zoneData[zone.name].values[8])
            zone.rooftops[0].area = zoneData[zone.name].values[8]
        else:
            zone.rooftops[0].area = 0.0001

        # Set area of grounfloor
        if zoneData[zone.name].values[9] > 0:
            zone.ground_floors[0].area = zoneData[zone.name].values[9]
        else:
            zone.ground_floors[0].area = 0.0001

        # Set area of inner walls
        if zoneData[zone.name].values[10] > 0:
            zone.inner_walls[0].area = zoneData[zone.name].values[10]
        else:
            zone.inner_walls[0].area = 0.0001

        # Set area of ceilings
        if zoneData[zone.name].values[11] > 0:
            zone.ceilings[0].area = zoneData[zone.name].values[11]
        else:
            zone.ceilings[0].area = 0.0001

        # Set area of floors
        if zoneData[zone.name].values[12] > 0:
            zone.floors[0].area = zoneData[zone.name].values[12]
        else:
            zone.floors[0].area = 0.0001

        # Total area of zones
        zone.area = zoneData[zone.name].values[13]

        # Total volume of zones
        zone.volume = zoneData[zone.name].values[14]

        # Number of pools
        if zone.name == "swimming_hall":
            zone.nPools = zoneData[zone.name].values[15]
            zone.pools.clear()


    #swimmingFacitlity.thermal_zones[0].pools.clear()
    #swimmingFacitlity.basic_pools_dict.clear()
    list_pools = poolData.keys()[3:swimmingFacitlity.thermal_zones[0].nPools+3]

    # dict for swimming pools [name, area, length, width,perimeter]
    #basic_pools_dict = {}

    #for pool in list_pools:
    #    print(poolData[pool].values[0])
    #    print(pool)
    #    basic_pools_dict[pool] = [poolData[pool].values[0],poolData[pool].values[1],poolData[pool].values[2],
    #                              poolData[pool].values[3], poolData[pool].values[4]]

    #print(basic_pools_dict)

    print(list_pools)
    # Generate and calculate swimming pools:
    for zone in swimmingFacitlity.thermal_zones:
        if zone.name == "Swimming_hall_1":
            for i in list_pools:
                print(i)
                pool = Pool(zone)
                pool.name = i
                pool.pool_type = poolData[i].values[0]
                pool.area = poolData[i].values[1]
                pool.length = poolData[i].values[2]
                pool.width = poolData[i].values[3]
                pool.perimeter = poolData[i].values[4]
                pool.depth = poolData[i].values[5]
                pool.volume = poolData[i].values[6]
                pool.area_pool_floor_exterior = poolData[i].values[7]
                pool.area_pool_floor_inner = poolData[i].values[8]
                pool.area_pool_wall_exterior = poolData[i].values[9]
                pool.area_pool_wall_inner = poolData[i].values[10]
                pool.temperature = poolData[i].values[11]
                pool.num_filter_rinses = poolData[i].values[12]
                pool.filter_type = poolData[i].values[13]
                print("filter combination",poolData[i].values[14])
                pool.filter_combination = poolData[i].values[14]
                pool.water_type = poolData[i].values[15]
                pool.use_heat_recovery = poolData[i].values[16]
                pool.eta_heat_recovery = poolData[i].values[17]
                pool.dp_heat_exchanger = poolData[i].values[18]
                pool.use_water_recycling = poolData[i].values[19]
                pool.x_recycling = poolData[i].values[20]
                pool.night_set_back_volume_flow = poolData[i].values[21]
                pool.volume_flow_night = poolData[i].values[22]
                pool.num_visitors = poolData[i].values[23]
                pool.use_pool_cover = poolData[i].values[24]
                pool.use_wave_pool = poolData[i].values[25]
                pool.wave_height = poolData[i].values[26]
                pool.wave_width = poolData[i].values[27]
                pool.wave_period = poolData[i].values[28]
                pool.wave_share_period = poolData[i].values[29]
                pool.pool_wall_construction_type = poolData[i].values[30]
                pool.calc_pool_parameters()
            print('Pools are sucessfully added')

            # AHU design according to VDI 2089
            abs_hum_swimming_hall = 0.0143  # Absolute humidity within the swimming hall in kg/kg
            abs_hum_amb = 0.009  # Average absolute humidity outdoor air in kg/kg
            m_flow_evap_pools_sum = 0  # Sum of evaporation of all pools (occupied pools) in kg/h
            m_flow_evap_pools_add_sum = 0  # Zero for basis swimming facility in kg/h
            m_flow_evap_attr = 0  # Zero for basic/ sport-oriented swimming pool in kg/g

            for pool in zone.pools:
                m_flow_evap_pools_sum += pool.m_flow_evap_pool_used

            m_flow_evap_max = m_flow_evap_pools_sum + m_flow_evap_pools_add_sum + m_flow_evap_attr  # Max evaporation in kg/h
            m_flow_ahu_nominal = m_flow_evap_max / (abs_hum_swimming_hall - abs_hum_amb)  # Design air flow in kg/h

            # AHU design, nominal mass flow in m3/(h*m2)  m2: area of swimming hall
            # density: 1.225 kg/m3
            zone.use_conditions.max_ahu = m_flow_ahu_nominal / (1.225 * zone.area)
            zone.use_conditions.min_ahu = 0.3 * zone.use_conditions.max_ahu
            print('max_AHU', zone.use_conditions.max_ahu)
            print('min_AHU', zone.use_conditions.min_ahu)
        else:
            zone.use_conditions.ahu = False


    # Step 5: Read material data

    matDict = {'OuterWall': {'thickness': [], 'material_id': []},
               'InnerWall': {'thickness': [], 'material_id': []},
               'Rooftop': {'thickness': [], 'material_id': []},
               'GroundFloor': {'thickness': [], 'material_id': []},
               'Ceiling': {'thickness': [], 'material_id': []},
               'Window': {'thickness': [], 'material_id': []}}

    for row in range(len(matData)):
        if pd.isna(matData['thickness'][row]) == False and pd.isna(matData['material_id'][row]) == False:
            matDict[matData['name'][row]]["thickness"].append(matData['thickness'][row]/100)
            matDict[matData['name'][row]]["material_id"].append(matData['material_id'][row])


    # Step 6: Set material data
    for zone in swimmingFacitlity.thermal_zones:
        overrideMaterialData(zone, matData, prj)

                    
def overrideMaterialData(zone, matDict, prj):
    for wall in zone.outer_walls:
        wallName = type(wall).__name__
        if wallName in matDict.keys():                
            wall.layer = None       
            for numLayer in range(0, len(matDict[wallName]["Thickness"])):
                mat_id = matDict[wallName]["Material_Id"][numLayer]
                thickness = matDict[wallName]["Thickness"][numLayer]
                layer = Layer(parent=wall, id=numLayer)
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
        if zoneName == "Sauna_area" or zoneName == "Fitness":
            zone = ThermalZone(swimmingPool)
            zone.area = value[0] 
            zone.volume = value[1]
            zone.name = zoneName
            use_cond = UseCond(zone)
            use_cond.load_use_conditions(value[2], data_class=swimmingPool.parent.data)
            zone.use_conditions = use_cond
            
            if zoneName == "Sauna_area":
                swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Temperature"] = 297.15
            elif zoneName == "Fitness":
                swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Temperature"] = 294.15
                
            zone.use_conditions._heating_profile = [swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Temperature"]] * 25
            
            if zone.use_conditions._cooling_profile[0] < \
                zone.use_conditions._heating_profile[0]:
                    zone.use_conditions._cooling_profile = \
                    zone.use_conditions._heating_profile
            
            zone.t_inside = swimmingPool.poolsInDict[
                swimmingPool.zoneDesignation[zone.name]]["Temperature"]
            
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



if __name__ == '__main__':
    prj = generate_advanced_swimmingPool()
    print()
    print("SwimmingPool(s) exported successfully. That's it! :)")