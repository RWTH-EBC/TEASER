# -*- coding: utf-8 -*-
"""
Created on Jul 2020

Last modified Dez 2021 for project 'Energieeffizienz in Schwimmbädern - 
Neubau und Bestand'
"""

import sys
import math
import collections
from teaser.logic.archetypebuildings.nonresidential import NonResidential
from teaser.logic.buildingobjects.useconditions import UseConditions as UseCond
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.buildingsystems.pool import Pool


class SwimmingFacility(NonResidential):
    """
    Archetype swimming facility based on project
    'Energieeffizienz in Schwimmbädern - Neubau und Bestand'

    Subclass from NonResidential archetype.

    The basic model contains 6 zones
    - Swimming_hall
    - Changing_rooms
    - Shower_and_sanitary_rooms
    - Entrance
    - Supervisory_room
    - Technical_room
    And 2 swimming pool:
    - Swimmer_pool
    - Nonswimmer_pool
    Each of the zones and pools hasseveral configurable parameters and
    attributes, which are listed below.


    Building parameters
    ----------

    parent: Project()
        The parent class of this object, the Project the Building belongs to.
        Allowater_area for better control of hierarchical structures. If not None it
        adds this Building instance to Project.buildings.
        (default: None)
    name : str
        Individual name
    year_of_construction : int
        Year of first construction
    height_of_floors : float [m]
        Average height of the buildings' floors
    number_of_floors : int
        Number of building's floors above ground
    net_leased_area : float [m2]
        For the swimming pool, this parameter stores the TOTAL WATER AREA 
        within the swimming pool building, unlike other building types.
    with_ahu : Boolean
        If set to True, an empty instance of BuildingAHU is instantiated and
        assigned to attribute central_ahu. This instance holds information for
        central Air Handling units. Default is False.
    internal_gains_mode: int [1, 2, 3]
        mode for the internal gains calculation by persons:
        1: Temperature and activity degree dependent calculation. The
           calculation is based on  SIA 2024 (default)
        2: Temperature and activity degree independent calculation, the max.
           heatflowrate is prescribed by the parameter
           fixed_heat_flow_rate_persons.
        3: Temperature and activity degree dependent calculation with
           consideration of moisture. The calculation is based on SIA 2024
    construction_type : str
        Construction type of used wall constructions default is "heavy")
            heavy: heavy construction
            light: light construction


    Important!
    ----------
    All variable attributes for the swimming pool zones and its pools are 
    stored within the dictionary "poolsInDict". This dictionary contains 
    information on all zones and pools within the swimming pool building. 
    The respective zone or pool is indicated with the first key (e.g. "Zone 1",
    "Swimmer pool" etc.). The second key stores the attributes like the area 
    or volume of a zone/pool. To refer to an attribute, indicate the pool 
    name/type at the first and the respective attribute at the second position. 
    To create several pools of the same type, add a number behind the pool 
    name. The name itself can't be changed. Attributes that are False or True 
    have to be written as string in small letters (convention for Modelica)!
    
    Examples:
    poolsInDict["Freeform_pool"]["Night setback"] = "false",
    poolsInDict["Swimmer_pool"]["Water area"] = 450,
    poolsInDict["Zone 1"]["Air volume"] = 3000    
    
    The listed attributes are just the ones that are set (optional) by 
    the user. Example 11 provides further information on this. 
    Calculated values are not included in this list. Changing these 
    values is expert mode. 
    

    Attributes for zones
    ----------

    Zones for poolsInDict (Designation without SPACE):
        - "Zone 1" # Swimming_hall
        - "Zone 2" # Changing_rooms
        - "Zone 3" # Shower_and_sanitary_rooms
        - "Zone 4" # Entrance
        - "Zone 5" # Supervisory_room
        - "Zone 6" # Sauna_area
        - "Zone 7" # Fitness
        - "Zone 8" # Technical_room
    Outer wall area north : float [m²]
        Default is calculated individually from total water area.
    Outer wall area east : float [m²]
        Default is calculated individually from total water area.
    Outer wall area south : float [m²]
        Default is calculated individually from total water area.
    Outer wall area west : float [m²]
        Default is calculated individually from total water area.
    Transparent element in outer wall north : float [m²]
        Default is calculated individually from total water area.
    Transparent element in outer wall east : float [m²]
        Default is calculated individually from total water area.
    Transparent element in outer wall south : float [m²]
        Default is calculated individually from total water area.
    Transparent element in outer wall west : float [m²]
        Default is calculated individually from total water area.
    Roof area : float [m²]
        Upper building closure, including horizontal transparent elements.
        Default is calculated individually from total water area.
    Ground floor area : float [m²]
        Lower building closure WITH EARTH CONTACT.
        Default is calculated individually from total water area.
    Inner walls as a sum : float [m²]
        Shared inner walls of two zones are splittet equally.
        Default is calculated individually from total water area.
    Ceiling area : float [m²]
        Inner ceiling within the building.
        Default is calculated individually from total water area.
    Floor area : float [m²]
        Inner floor within the building WITHOUT EARTH CONTACT.
        Default is calculated individually from total water area.
    Total area of zone : float [m²]
        INCLUDING WATER AREA:
        Default is calculated individually from total water area.
    Air volume : float [m³]
        Total conditioned air volume of the zone.    
        Default is calculated individually from total water area.   
       
        
    Attributes for pools
    ---------
    
    Pools for poolsInDict:
        - Swimmer_pool
        - Nonswimmer_pool
        - Multipurpose_pool
        - Toddler_pool
        - Diving_pool
        - Freeform_pool
    Water area : float [m²]
        Water area of the respective pool. Default is calculated
        individually based on the total water area.
    Average pool depth : float [m]
        Average depth of the pool. 
        Default is 3 m for "Swimmer_pool" and 0.975 m for
        "Nonswimmer_pool".
    Water volume : float [m³]
        Default is calculated individually based on the total 
        water area.
    Perimeter pool : float [m]
        Default is calculated individually based on the total
        water area.
    Pool floor with earth contact : float [m²]
        Pool floor that has direct earth contact (no zone below).
        Default is the whole water area.
    Pool floor without earth contact : float [m²]
        Pool floor that has NO direct earth contact (e.g. basement 
        below water area). Default is 0.
    Pool wall with earth contact : float [m²]
        Pool wall that has direct earth contact (no contiguous zone).
        Default is half of the whole pool wall area.
    Pool wall without earth contact : float [m²]
        Pool wall that has NO direct earth contact (e.g. contiguous
        technical zone). Default is half of the whole pool wall area.
    Pool temperature : float [K]
        Default is 299.15.
    Filter rinses per week : int
        Default is 2.
    Filter type : string
        Installed filter for the respective pool. Default is 
        "Open suction filter". Possible types are:
            - "Activated carbon filter with ozone"
            - "Closed quick filter"
            - "Closed sorption filter"
            - "Open quick filter"
            - "Open suction filter"
            - "Quantozone filter"
            - "Quartz gravel filter"
            - "Two-layer filter"
            - "Two-layer filter with ozone"
    Filter combination : string
        Default is "without ozone". Possible combinations are:
            - "without ozone"
            - "with ozone"            
            - "with ultrafiltration"
            - "with bromine"
    Water type : string
        Default is "Freshwater". Possible types are:
            - "Freshwater"
            - "Saltwater"
    Pressure loss heat exchanger : int [Pa]
        Default is 350.
    Heat recovery rinsing wastewater : boolean
        Default is "true".
    Heat recovery rate rinsing wastewater : float
        Default is 0.8.
    Wastewater treatment : boolean
        Default is "true".
    Wastewater treatment rate : boolean
        Default is 0.8.
    Night setback : boolean
        Default is "false".
    Volume flow wastewater treatment night : float
        Default is 30.
    Visitor number per hour : int
        Number of people that use the respective pool in one day.
        Default is calculated individually based on the total 
        water area.
    Pool covering outside operating hours : boolean
        Default is "true".
    Operation of artificial waves : boolean
        Default is "false".
    Wave height : float [m]
        Default is 0.
    Wave width : float [m]
        Default is 0.
    Interval wave operation : int [sec]
        Default is 1800.
    Share of wave operation : int [%]
        Default is 600.  
    Construction of pool wall : string
        Default is "Reinforced concrete". 
        Possible constructions are:
            - "Reinforced concrete"
    """
    
        
    def __init__(
        self,
        parent,        
        name=None,
        year_of_construction=None,
        number_of_floors=None,
        height_of_floors=None,
        net_leased_area=None,
        with_ahu=False,
        internal_gains_mode=1,
        construction_type=None,
        water_area=None,
        use_correction_factor=False,
    ):
        """Constructor of Swimming facility archetype
        """
        super(SwimmingFacility, self).__init__(
            parent,
            name,
            year_of_construction,
            net_leased_area,
            with_ahu,
            internal_gains_mode,
        )
        self.construction_type = construction_type
        self.number_of_floors = number_of_floors
        self.height_of_floors = height_of_floors
        if self.year_of_construction > 2015:
            self.year_of_construction = 2015
        self.water_area = water_area
        self.use_correction_factor = use_correction_factor

        """
        Creating basic swimming facility with one pool for beginners and 
        one for swimmers or only one pool for swimmers, if the water area is 
        not sufficient for two basic pools. Zone areas and volumes are 
        calculated from the WATER AREA according to 'Koordinierungskreis 
        Bäder - Richtlinien für den Bäderbau - 2013' with further adjustments 
        from the project 'Energieeffizienz in Schwimmbädern - Neubau und 
        Bestand'.
        """
        
        print("Calculating framework data for swimming facility according to an pool area of:", self.water_area)
        print()

        #self.poolsInDict = self.createBasicSwimmingFacility(self.net_leased_area)
        # pool dict with "Swimmer_pool" and "Nonswimmer_pool" [type, area, length, width, perimeter]
        self.basic_pools_dict = self.create_basic_pools(water_area)

        # [zone_usage, zone_area, zone_volume, zone_length, zone_width, zone_temperature]
        self.zone_area_factors = collections.OrderedDict()

        # Zone swimming_hall
        if len(self.basic_pools_dict) > 1:
            zone_length = self.basic_pools_dict["Swimmer_pool"][2] \
                          + self.basic_pools_dict["Nonswimmer_pool"][3] + 8.25
        else:
            zone_length = self.basic_pools_dict["Swimmer_pool"][2] + 4.5
        zone_width = self.basic_pools_dict["Swimmer_pool"][3] + 4.5
        zone_area = zone_width * zone_length
        zone_volume = zone_area * 6
        zone_temperature = 303.15
        self.zone_area_factors["Swimming_hall"] = ["Swimming hall", zone_area, zone_volume,
                                                   zone_length, zone_width, zone_temperature]

        # Zone Changing_rooms
        # zone_area = changing_rooms + sanitary_objects + cleaning_room + corridors
        changing_rooms = 3.675 + math.ceil(water_area ** 0.58 / (14 * 2)) * 21.7 + \
                        math.ceil(water_area ** 0.58 / (7 * 2)) * 23.625
        sanitary_objects = math.ceil(water_area * 0.02)
        cleaning_room = 2
        corridors = (math.ceil(water_area ** 0.58 / 14) * 3.1 + \
                     math.ceil(water_area ** 0.58 / 7) * 3.375) * 1.5
        zone_area = changing_rooms + sanitary_objects + cleaning_room + corridors
        zone_volume = zone_area * 2.75
        zone_temperature = 299.15
        zone_width = 7 + 1.5 * 2
        zone_length = zone_area / zone_width
        self.zone_area_factors["Changing_rooms"] = ["Dressing room, shower", zone_area, zone_volume,
                                                    zone_length, zone_width, zone_temperature]

        # Zone Shower_and_sanitary_rooms
        # zone_area = sanitary blocks + additional showers
        if water_area <= 150:
            zone_area = 45.24
        elif water_area <= 500:
            zone_area = 82.53
        else:
            num_shower = water_area ** 0.5
            # (Due to the arrangement of the sanitary rooms, only 4 showers can be
            # added at once for additional capacity)
            num_shower = math.ceil(num_shower / 4) * 4
            num_sanitary_double_blocks = math.floor(num_shower / 20)
            num_additional_showers = (num_shower - num_sanitary_double_blocks * 20) / 4
            zone_area = num_sanitary_double_blocks * 82.53 + num_additional_showers * 10.44
        zone_width = 4 + 2 * 0.9
        zone_length = zone_area / zone_width
        zone_temperature = 301.15
        self.zone_area_factors["Shower_and_sanitary_rooms"] = ["WC and sanitary rooms in non-residential buildings",
                                                               zone_area, zone_volume, zone_length, zone_width,
                                                               zone_temperature]

        # Zone Entrance
        # zone_area = entrance + management room
        zone_area = 12 + water_area * 0.2
        zone_volume = zone_area * 2.75
        zone_width = self.zone_area_factors["Changing_rooms"][4] + 2
        zone_length = zone_area / zone_width
        zone_temperature = 294.15
        self.zone_area_factors["Entrance"] = ["Foyer (theater and event venues)", zone_area, zone_volume,
                                              zone_length, zone_width, zone_temperature]

        # Zone Supervisory_room
        # zone_area = First aid room + swimming master room + Swimming equipment room
        # + Cleaning equipment room
        zone_area = 43
        zone_volume = zone_area * 2.5
        zone_width = 3.5
        zone_length = zone_area / zone_width
        zone_temperature = 297.15
        self.zone_area_factors["Supervisory_room"] = ["Meeting, Conference, seminar", zone_area, zone_volume,
                                                      zone_length, zone_width, zone_temperature]

        # Zone Technical_room
        zone_area = water_area + water_area * (1 / 24) + 25
        zone_volume = zone_area * 3.5
        zone_width = self.zone_area_factors["Swimming_hall"][4]
        zone_length = zone_area / zone_width
        zone_temperature = 297.15
        self.zone_area_factors["Technical_room"] = ["Stock, technical equipment, archives", zone_area, zone_volume,
                                                    zone_length, zone_width, zone_temperature]


        # Zone area correction
        if self.use_correction_factor:
            correction_factor = (2247.5 * math.log(water_area) - 10505) / (2.8582 * water_area + 336.4)

            for key in self.zone_area_factors.keys():
                self.zone_area_factors[key][1] *= correction_factor
                self.zone_area_factors[key][3] += 2
                self.zone_area_factors[key][4] = self.zone_area_factors[key][1] / self.zone_area_factors[key][3]


        # Creating potential building elements
        """
        Warning: All names of the building elements are saved without spaces!  
        """
        # [tilt, orientation]
        
        self.outer_wall_names = {
            "Exterior Facade North": [90, 0],
            "Exterior Facade East": [90, 90],
            "Exterior Facade South": [90, 180],
            "Exterior Facade West": [90, 270]}

        self.roof_names = {"Rooftop": [0, -1]}
         
        self.ground_floor_names = {
            "Ground Floor": [0, -2]}

        self.window_names = {
            "Window Facade North": [90, 0],
            "Window Facade East": [90, 90],
            "Window Facade South": [90, 180],
            "Window Facade West": [90, 270]}

        self.inner_wall_names = {"InnerWall": [90, 0]}
        
        self.floor_names = {"Floor": [0, -2]}
        
        self.ceiling_names = {"Ceiling": [0, -1]}

        self.opening_hours = [0.0] * 7 + [1.0] * 5 + [0.5] + [1.0] * 9 + [0.0] * 3
        


        if self.with_ahu is True:
            self.central_ahu.temperature_profile = (
                  #  7 * [293.15] + 12 * [295.15] + 6 * [293.15]
                  24 * [303.15])
            self.central_ahu.min_relative_humidity_profile = 24 * [0.0]  #
            self.central_ahu.max_relative_humidity_profile = 24 * [1.0]

            # AHU v_flow_profile
            self.central_ahu.v_flow_profile = (
               7 * [1.0] + 15 * [1.0] + 2 * [1.0])


    def generate_archetype(self):
        """
        Generates a swimming facility archetype.
        """

        # Creates binding for Material data of swimming pools
        # self.parent.data.SwimmingFacility_bind = dict()
        # help area for the correct building area setting while using typeBldgs
        self.thermal_zones = None  
        self.net_leased_area = 0
        self.volume = 0
        # create zones with their corresponding area, name and usage
        for key, value in self.zone_area_factors.items():
            zone = ThermalZone(self)
            zone.area = value[1]
            zone.volume = value[2]
            zone.name = key
            self.net_leased_area += self.zone_area_factors[key][1]
            self.volume += self.zone_area_factors[key][5]
            use_cond = UseCond(zone)
            use_cond.load_use_conditions(value[0], data_class=self.parent.data)
            zone.use_conditions = use_cond

            # final use conditions for  swimming facility not defined, therefore temperatures are set manually
            # Todo: Correct, when norm is final
            zone.use_conditions.with_ahu = True
            zone.use_conditions.heating_profile = self.zone_area_factors[key][5]
            zone.use_conditions._heating_profile = [self.zone_area_factors[key][5]] * 25

                      
            #if zone.use_conditions.cooling_profile[0] < \
            #    zone.use_conditions.heating_profile[0]:
            #        zone.use_conditions.cooling_profile = self.zone_area_factors[key][5]
            #        zone.use_conditions._cooling_profile = [self.zone_area_factors[key][5]] * 25
            
            zone.t_inside = self.zone_area_factors[key][5]



        """
        The following element calculations are part of the teaser office class 
        with adjustments for pools. 
        """
 
        # statistical estimation of the facade       
        self.outer_area[0] = 0
        self.outer_area[90] = 0
        self.outer_area[180] = 0
        self.outer_area[270] = 0
        self.window_area[0] = 0
        self.window_area[90] = 0
        self.window_area[180] = 0
        self.window_area[270] = 0
        self.gross_factor = 1.15  # based on :cite:`Liebchen.2007`

        # # OUTER WALLS #
        # # set the facade area to the four orientations
        for key, value in self.outer_wall_names.items():             
            #Creates an outer wall for each zone and assigns building elements  
            for zone in self.thermal_zones:
                outer_wall = OuterWall(zone)
                outer_wall.name = key
                outer_wall.load_type_element(
                    year=self.year_of_construction,
                    construction=self.construction_type,
                    data_class=self.parent.data)               
                outer_wall.tilt = value[0]
                outer_wall.orientation = value[1]
                
        # WINDOWS #
        for key, value in self.window_names.items():            
            for zone in self.thermal_zones:
                window = Window(zone)
                window.name = key
                window.load_type_element(
                    self.year_of_construction,
                    "Kunststofffenster, " "Isolierverglasung",
                    data_class=self.parent.data)                
                window.tilt = value[0]
                window.orientation = value[1]     
                
        # ROOFTOPS #
        for key, value in self.roof_names.items():
            self.outer_area[value[1]] = self.net_leased_area / self.number_of_floors * \
            self.gross_factor
            
            for zone in self.thermal_zones:
                roof = Rooftop(zone)
                roof.name = key
                roof.load_type_element(
                    year=self.year_of_construction,
                    construction=self.construction_type,
                    data_class=self.parent.data)
                roof.tilt = value[0]
                roof.orientation = value[1]
        
        # GROUNDFLOORS #
        for key, value in self.ground_floor_names.items():
            self.outer_area[value[1]] = self.net_leased_area / self.number_of_floors * \
            self.gross_factor
            
            for zone in self.thermal_zones:  
                ground_floor = GroundFloor(zone)
                ground_floor.name = key
                ground_floor.load_type_element(
                    year=self.year_of_construction,
                    construction=self.construction_type,
                    data_class=self.parent.data)
                ground_floor.tilt = value[0]
                ground_floor.orientation = value[1]
                
        # INNER WALLS #
        for key, value in self.inner_wall_names.items():    
            for zone in self.thermal_zones:
                inner_wall = InnerWall(zone)
                inner_wall.name = key
                inner_wall.load_type_element(
                    year=self.year_of_construction,
                    construction=self.construction_type,
                    data_class=self.parent.data)
                inner_wall.tilt = value[0]
                inner_wall.orientation = value[1]   

        if self.number_of_floors > 1:
            # CEILINGS #
            for key, value in self.ceiling_names.items(): 
                for zone in self.thermal_zones:
                    ceiling = Ceiling(zone)
                    ceiling.name = key
                    ceiling.load_type_element(
                        year=self.year_of_construction,
                        construction=self.construction_type,
                        data_class=self.parent.data)
                    ceiling.tilt = value[0]
                    ceiling.orientation = value[1] 
        
            # FLOORS #   
            for key, value in self.floor_names.items():
                for zone in self.thermal_zones:
                    floor = Floor(zone)
                    floor.name = key
                    floor.load_type_element(
                        year=self.year_of_construction,
                        construction=self.construction_type,
                        data_class=self.parent.data)
                    floor.tilt = value[0]
                    floor.orientation = value[1]   
                     
        # Calculate building surface area and surface areas of each zone        
        for key, value in self.outer_area.items():
            new_area = value
            orientation = key
            for zone in self.thermal_zones:
                for wall in zone.outer_walls:
                    if wall.orientation == orientation:
                        wall.area = 0.001
    
                for roof in zone.rooftops:
                    if roof.orientation == orientation:
                        roof.area = \
                            ((new_area / self.net_leased_area) * zone.area) / sum(
                            count.orientation == orientation for count in zone.rooftops
                        )
    
                for ground in zone.ground_floors:
                    if ground.orientation == orientation:
                        ground.area = \
                            ((new_area / self.net_leased_area) * zone.area) / sum(
                            count.orientation == orientation for count in \
                                zone.ground_floors
                        )
        
        for key, value in self.window_area.items():
            orientation = key
            for zone in self.thermal_zones:
                for win in zone.windows:
                    if win.orientation == orientation:
                        win.area = 0.001
                    
        # Overwrite wall and window areas for swimming pool   
        # North
        self.thermal_zones
        self.thermal_zones[0].outer_walls[0].area = \
            self.zone_area_factors["Swimming_hall"][3] * 2.2
        self.thermal_zones[0].windows[0].area = \
            self.zone_area_factors["Swimming_hall"][3] * 0.8
        self.thermal_zones[1].outer_walls[0].area = \
            self.zone_area_factors["Changing_rooms"][3] * 2
        self.thermal_zones[1].windows[0].area = \
            self.zone_area_factors["Changing_rooms"][3] * 1
        self.thermal_zones[3].outer_walls[0].area = \
            self.zone_area_factors["Entrance"][3] * 1.5
        self.thermal_zones[3].windows[0].area = \
            self.zone_area_factors["Entrance"][3] * 1.5
        self.thermal_zones[5].outer_walls[0].area = \
            self.zone_area_factors["Technical_room"][3] * 3.5
            
        zone5_facade_north = self.zone_area_factors["Changing_rooms"][3] + \
            self.zone_area_factors["Entrance"][3] - \
                self.zone_area_factors["Shower_and_sanitary_rooms"][3]
        if zone5_facade_north > 0:
            self.thermal_zones[4].outer_walls[0].area = zone5_facade_north
            
        # East
        self.thermal_zones[0].outer_walls[1].area = \
            self.zone_area_factors["Swimming_hall"][4] * 3
        self.thermal_zones[0].windows[1].area = \
            self.zone_area_factors["Swimming_hall"][4] * 3
        self.thermal_zones[3].outer_walls[1].area = \
            self.zone_area_factors["Entrance"][4] * 1.5
        self.thermal_zones[3].windows[1].area = \
            self.zone_area_factors["Entrance"][4] * 1.5
        self.thermal_zones[4].outer_walls[1].area = \
            self.zone_area_factors["Supervisory_room"][4] * 2
        self.thermal_zones[4].windows[1].area = \
            self.zone_area_factors["Supervisory_room"][4] * 1
        self.thermal_zones[5].outer_walls[1].area = \
            self.zone_area_factors["Technical_room"][4] * 3.5
            
        # South
        self.thermal_zones[0].outer_walls[2].area = \
            self.zone_area_factors["Swimming_hall"][3] * (1/8) * 6
        self.thermal_zones[0].windows[2].area = \
            self.zone_area_factors["Swimming_hall"][3] * (7/8) * 6
        self.thermal_zones[5].outer_walls[2].area = \
            self.zone_area_factors["Technical_room"][3] * 3.5
            
        # West
        self.thermal_zones[0].outer_walls[3].area = \
            self.thermal_zones[0].outer_walls[1].area
        self.thermal_zones[0].windows[3].area = \
            self.thermal_zones[0].windows[1].area
        self.thermal_zones[1].outer_walls[3].area = \
            self.zone_area_factors["Changing_rooms"][4] * 3
        self.thermal_zones[2].outer_walls[3].area = \
            self.zone_area_factors["Shower_and_sanitary_rooms"][4] * 3
        self.thermal_zones[5].outer_walls[3].area = \
            self.zone_area_factors["Technical_room"][4] * 3.5
            
        for zone in self.thermal_zones:
            self.outer_area[0] = self.outer_area[0] + zone.outer_walls[0].area
            self.outer_area[90] = self.outer_area[90] + zone.outer_walls[1].area
            self.outer_area[180] = self.outer_area[180] + zone.outer_walls[2].area
            self.outer_area[270] = self.outer_area[270] + zone.outer_walls[3].area
            self.window_area[0] = self.window_area[0] + zone.windows[0].area
            self.window_area[90] = self.window_area[90] + zone.windows[1].area
            self.window_area[180] = self.window_area[180] + zone.windows[2].area
            self.window_area[270] = self.window_area[270] + zone.windows[3].area


        # Calculates inner wall area as sum of inner walls, ceiling and 
        # floor for each zone 
        for zone in self.thermal_zones:
            zone.set_inner_wall_area()


        # Swimming hall specific calculations
        for zone in self.thermal_zones:
            if zone.name == "Swimming_hall":
                # Calculate swimming pools in swimming hall
                zone.nPools = len(self.basic_pools_dict)
                for key, value in self.basic_pools_dict.items():
                    pool = Pool(zone)
                    pool.name = key
                    pool.pool_type = value[0]
                    pool.area = value[1]
                    pool.width = value[2]
                    pool.length = value[3]
                    pool.perimeter = value[4]
                    pool.calc_pool_parameters()
                    pool.area_pool_wall_inner = 0.5*pool.perimeter*pool.depth
                    pool.area_pool_wall_exterior = 0.5*pool.perimeter*pool.depth
                    pool.area_pool_floor_inner = 0.001
                    pool.area_pool_floor_exterior = pool.area
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
                print('max_AHU',zone.use_conditions.max_ahu)
                print('min_AHU', zone.use_conditions.min_ahu)


    def create_basic_pools(self, water_area):
        """
        Create swimming pools for swimming facility archetype.
        """
        # pool dict with "Swimmer_pool" and "Nonswimmer_pool" [type, area, length, width]
        basic_pool_dic = collections.OrderedDict()

        # Pools
        main_pool_surface = water_area
        beginner_pool_surface = 0

        if water_area > 312.5 and water_area <= 582:
            beginner_pool_surface = 100
            beginner_pool_width = 8
            beginner_pool_length = 10
        elif water_area > 582:
            beginner_pool_surface = 166.7
            beginner_pool_width = 10
            beginner_pool_length = 16.66
        beginner_pool_perimeter = 2*beginner_pool_width+2*beginner_pool_length

        main_pool_surface = water_area - beginner_pool_surface

        # Assign respective pool from basic pool areas, which defines the aspect ratio
        reference = min([312.5, 415, 830, 1050, 1250], key=lambda \
                x: abs(x - main_pool_surface))

        if reference < 830:
            main_pool_length = 25
        else:
            main_pool_length = 50
        main_pool_width = main_pool_surface / main_pool_length
        main_pool_perimeter = 2*main_pool_width+ 2*main_pool_length


        basic_pool_dic["Swimmer_pool"] = ["Swimmer_pool",main_pool_surface, main_pool_length, main_pool_width,
                                          main_pool_perimeter]
        basic_pool_dic["Nonswimmer_pool"] = ["Nonswimmer_pool",beginner_pool_surface, beginner_pool_length,
                                             beginner_pool_width, beginner_pool_perimeter]

        return basic_pool_dic


    @property
    def construction_type(self):
        return self._construction_type

    @construction_type.setter
    def construction_type(self, value):
        if value is not None:
            if value == "heavy" or value == "light":
                self._construction_type = value
            else:
                raise ValueError("Construction_type has to be light or heavy")
        else:
            self._construction_type = "heavy"
