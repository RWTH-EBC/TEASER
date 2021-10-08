# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:25:12 2020

Last modified 2021-09 for Project 'Energieeffizienz in Schwimmbädern - Neubau und Bestand'
"""

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


class SwimmingPool(NonResidential):
    """
    Archetype swimming pool based on project 'Energieeffizienz in Schwimmbädern - Neubau und Bestand'

    Subclass from NonResidential archetype.

    The model contains 6 zones of the swimming pool
    Each of the zones has variable outer walls, windows, roofs and ground floors.

    Parameters
    ----------

    parent: Project()
        The parent class of this object, the Project the Building belongs to.
        Allows for better control of hierarchical structures. If not None it
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
        Total net leased area of building. This is area is NOT the footprint
        of a building
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
    office_layout : int
        Structure of the floor plan of office buildings, default is 1,
        which is representative for one elongated floor.
            1: elongated 1 floor
            2: elongated 2 floors
            3: compact (e.g. for a square base building)
    window_layout : int
        Structure of the window facade type, default is 0, which is a generic facade
        representing a statistical mean value of window area. This is the foundation
        for calculating the other window layouts with correction factors.
            0: generic facade
            1: punctuated facade (individual windows)
            2: banner facade (continuous windows)
            3: full glazing
    construction_type : str
        Construction type of used wall constructions default is "heavy")
            heavy: heavy construction
            light: light construction

    Note
    ----------
    The listed attributes are just the ones that are set by the user
    calculated values are not included in this list. Changing these values is
    expert mode.

    Attributes
    ----------

    zone_area_factors : dict
        This dictionary contains the name of the zone (str), the
        zone area factor (float), the zone volume factor (float) and the zone usage from BoundaryConditions json
        (str). (Default see doc string above)
    outer_wall_names : dict
        This dictionary contains a random name for the outer walls,
        their orientation and tilt. Default is a building in north-south
        orientation)
    roof_names : dict
        This dictionary contains the name of the roofs, their orientation
        and tilt. Default is one flat roof.
    ground_floor_names : dict
        This dictionary contains the name of the ground floors, their
        orientation and tilt. Default is one ground floor.
    window_names : dict
        This dictionary contains the name of the window, their
        orientation and tilt. Default is a building in north-south
        orientation)
    inner_wall_names : dict
        This dictionary contains the name of the inner walls, their
        orientation and tilt. Default is one cumulated inner wall.
    ceiling_names : dict
        This dictionary contains the name of the ceilings, their
        orientation and tilt. Default is one cumulated ceiling.
    floor_names : dict
        This dictionary contains the name of the floors, their
        orientation and tilt. Default is one cumulated floor.
    gross_factor : float
        gross factor used to correct the rooftop and floor area (default is
        1.15)
    est_factor_wall_area : float
        estimation factor to calculate outer wall area
    est_exponent_wall : float
        estimation factor exponent to calculate outer wall area
    est_factor_win_area : float
        estimation factor to calculate window area
    est_exponent_win : float
        estimation factor exponent to calculate window area
    isSwimmingPool : boolean
        Indicates for other classes that a swimming pool will be created
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
        office_layout=None,
        window_layout=None,
        construction_type=None        
    ):
        """Constructor of SwimmingPool archetype
        """
        super(SwimmingPool, self).__init__(
            parent,
            name,
            year_of_construction,
            net_leased_area,
            with_ahu,
            internal_gains_mode,
        )
        self.office_layout = office_layout
        self.window_layout = window_layout
        self.construction_type = construction_type
        self.number_of_floors = number_of_floors
        self.height_of_floors = height_of_floors

        # [area factor, volume factor, usage type(has to be set)]
        self.zone_area_factors = collections.OrderedDict()
        
        """
        Creating basic swimming pool building with one pool for beginners and one for swimmers or only 
        one pool for swimmers, if the water area is not sufficient for two basic pools.
        Zone areas and volumes are calculated from the WATER SURFACE according to 'Koordinierungskreis 
        Bäder - Richtlinien für den Bäderbau - 2013'. Therefore, the NET LEASED AREA is used as 
        WATER SURFACE. The basic building contains the zones 1 - 5 and 8.
        """
        
        print("Calculating zone data for basic swimming pool:", name)             
        
        self.poolsInDict = self.setPoolBaseParameters(self.net_leased_area, True) 
        
        # Calculating actual net leased area
        self.net_leased_area = 0
        for value in self.poolsInDict.keys():
            if str(value).startswith("Zone"):
                self.net_leased_area = self.net_leased_area + self.poolsInDict[value]\
                ["Total area of zone (including water surface) [m²]"]
        
        self.net_leased_area = round(self.net_leased_area, 2)
        print("Calculated total net leased area:", self.net_leased_area, "m²")
        print()         
        
        # Calculating number of zones
        self.numZones=0
        for zone in self.poolsInDict.keys(): 
            if str(zone).startswith("Zone"):
                self.numZones+=1                 
                           
        # Zone designations
        self.zoneDesignation = dict()
        self.zoneDesignation["Zone 1"] = "Eingangsbereich"
        self.zoneDesignation["Zone 2"] = "Umkleiden"
        self.zoneDesignation["Zone 3"] = "Duschen und Sanitärräume"
        self.zoneDesignation["Zone 4"] = "Schwimmhalle"
        self.zoneDesignation["Zone 5"] = "Aufsichtsraum"
        self.zoneDesignation["Zone 6"] = "Saunabereich"
        self.zoneDesignation["Zone 7"] = "Fitness"
        self.zoneDesignation["Zone 8"] = "Technikraum"        
        
        # Use conditions for zones
        self.zoneUseConditions = dict()
        self.zoneUseConditions["Zone 1"] = "Foyer (theater and event venues)"          
        self.zoneUseConditions["Zone 2"] = "Group Office (between 2 and 6 employees)"
        self.zoneUseConditions["Zone 3"] = "WC and sanitary rooms in non-residential buildings"
        self.zoneUseConditions["Zone 4"] = "Gym (without spectator area)"
        self.zoneUseConditions["Zone 5"] = "Meeting, Conference, seminar"
        self.zoneUseConditions["Zone 6"] = "Sauna area"
        self.zoneUseConditions["Zone 7"] = "Gym (without spectator area)"
        self.zoneUseConditions["Zone 8"] = "Stock, technical equipment, archives"
        self.zoneUseConditions["Water"] = "Gym (without spectator area)"  
        
        #Creating building zones
        # Zone won't be created if area is 0
        for zone in self.zoneDesignation.keys():
            if zone in self.poolsInDict.keys():
                self.zone_area_factors[self.zoneDesignation[zone]] = \
                [self.poolsInDict[zone]["Total area of zone (including water surface) [m²]"], \
                 self.poolsInDict[zone]["Air volume [m³]"], \
                 self.zoneUseConditions[zone]]                                                              
        
        #Creating zones for water volumes 
                                          
        # for value in self.poolsInDict.keys():           
        #     if "becken" in value \
        #     and self.poolsInDict[value]["Water surface"] != "" \
        #     and self.poolsInDict[value]["Water surface"] != 0:            
        #         self.zone_area_factors[str(value)] = \
        #         [self.poolsInDict[value]["Water surface"], 
        #          self.poolsInDict[value]["Water volume"],
        #          self.zoneUseConditions["Water"]]                                                     
                                                              
        for key, value in self.zone_area_factors.items():
            print ("Added", key, "with zone area:", value[0], "m²")
        print()               
     

        # Creating potential building elements
        # Warning: All the names of the building elements are saved without spaces
        # in their names!            
        # [tilt, orientation]
        
        self.outer_wall_names = {
            "Exterior Facade North": [90, 0],
            "Exterior Facade East": [90, 90],
            "Exterior Facade South": [90, 180],
            "Exterior Facade West": [90, 270],
            "PoolWall":[90, 0]}

        self.roof_names = {"Rooftop": [0, -1]}
         
        self.ground_floor_names = {
            "Floor With Earth Contact": [0, -2],
            "Pool Floor With Earth Contact": [0, -2]}

        self.window_names = {
            "Window Facade North": [90, 0],
            "Window Facade East": [90, 90],
            "Window Facade South": [90, 180],
            "Window Facade West": [90, 270]}

        self.inner_wall_names = {"InnerWall": [90, 0],
                                 "InnerPoolWall":[90, 0]}
        
        self.floor_names = {"Floor": [0, -2],
                            "Pool Area Above Technical Room": [0, -2]}
        
        self.ceiling_names = {"Ceiling": [0, -1]}



        """
        The following parameters are part of the teaser office class and won't be used 
        for the swimming pool calculation if all needed parameters are provided.
        """

        self.gross_factor = 1.15  # based on :cite:`Liebchen.2007`
        self.est_factor_wall_area = 0.7658
        self.est_exponent_wall = 0.9206
        self.est_factor_win_area = 0.074
        self.est_exponent_win = 1.0889

        # estimated intermediate calculated values
        self._est_outer_wall_area = 0
        self._est_win_area = 0
        self._est_roof_area = 0
        self._est_floor_area = 0
        self._est_facade_area = 0
        self._est_width = 0
        self._est_length = 0

        if self.window_layout == 0:
            self.corr_factor_wall = 1.0
            self.corr_factor_win = 1.0
        elif self.window_layout == 1:
            self.corr_factor_wall = 0.75
            self.corr_factor_win = 0.25
        elif self.window_layout == 2:
            self.corr_factor_wall = 0.5
            self.corr_factor_win = 0.5
        elif self.window_layout == 3:
            self.corr_factor_wall = 0.1
            self.corr_factor_win = 0.9
        else:
            raise ValueError("window_layout value has to be between 0 - 3")

        if self.office_layout == 0 or self.office_layout == 1:
            self._est_width = 13.0
        elif self.office_layout == 2:
            self._est_width = 15.0
        elif self.office_layout == 3:
            self._est_width = math.sqrt(
                (self.net_leased_area / self.number_of_floors) * self.gross_factor
            )
        else:
            raise ValueError("office_layout value has to be between 0 - 3")
        if self.net_leased_area is not None and self.number_of_floors is not None:
            self._est_length = (
                (self.net_leased_area / self.number_of_floors) * self.gross_factor
            ) / self._est_width
        else:
            pass

        
        # Default values for AHU from Teaser. Adaptation for swimming pools pending.
            if self.with_ahu is True:
                self.central_ahu.temperature_profile = (
                    7 * [293.15] + 12 * [295.15] + 6 * [293.15]
                )
                #  according to :cite:`DeutschesInstitutfurNormung.2016`
                self.central_ahu.min_relative_humidity_profile = 25 * [0.45]  #
                #  according to :cite:`DeutschesInstitutfurNormung.2016b`  and
                # :cite:`DeutschesInstitutfurNormung.2016`
                self.central_ahu.max_relative_humidity_profile = 25 * [0.65]
                self.central_ahu.v_flow_profile = (
                    7 * [0.0] + 12 * [1.0] + 6 * [0.0]
                )  # according to user
                # profile in :cite:`DeutschesInstitutfurNormung.2016`


    def generate_archetype(self):
        """Generates an office building.

        With given values, this class generates an office archetype building
        according to TEASER requirements.
        """
        print("Generating archetype. Please wait...")
        print()
        # Creates binding for Material data of swimming pools
        self.parent.data.swimmingpool_bind = dict()
        # help area for the correct building area setting while using typeBldgs
        self.thermal_zones = None        
        type_bldg_area = self.net_leased_area
        self.net_leased_area = 0.0
        # create zones with their corresponding area, name and usage
        for key, value in self.zone_area_factors.items():
            zone = ThermalZone(self)
            zone.area = value[0] 
            zone.volume = value[1]
            zone.name = key
            # Additional Parameters for Pools 
            if zone.name == "Schwimmhalle":                  
                zone.paramRecord = dict()
                for pool in self.poolsInDict.keys():
                    if "becken" in pool:                                                
                        zone.paramRecord[pool] = dict()
            use_cond = UseCond(zone)
            use_cond.load_use_conditions(value[2], data_class=self.parent.data)
            zone.use_conditions = use_cond
        

        """
        The following element calculations are part of the teaser office class and 
        won't be used for the swimming pool calculation if all needed parameters 
        are provided. 
        """
        # statistical estimation of the facade
        self._est_outer_wall_area = (
            self.est_factor_wall_area * type_bldg_area ** self.est_exponent_wall
        )
        self._est_win_area = (
            self.est_factor_win_area * type_bldg_area ** self.est_exponent_win
        )
        self._est_roof_area = (
            type_bldg_area / self.number_of_floors
        ) * self.gross_factor
        self._est_floor_area = (
            type_bldg_area / self.number_of_floors
        ) * self.gross_factor
        # manipulation of wall according to facade design
        # (received from window_layout)
        self._est_facade_area = self._est_outer_wall_area + self._est_win_area
        if not self.window_layout == 0:
            self._est_outer_wall_area = self._est_facade_area * self.corr_factor_wall
            self._est_win_area = self._est_facade_area * self.corr_factor_win
        else:
            pass

        # OUTER WALLS #
        # set the facade area to the four orientations
        for key, value in self.outer_wall_names.items():

            # North and South
            if value[1] == 0 or value[1] == 180:
                self.outer_area[value[1]] = self._est_outer_wall_area * (
                    self._est_length / (2 * self._est_width + 2 * self._est_length))
            # East and West
            elif value[1] == 90 or value[1] == 270:
                self.outer_area[value[1]] = self._est_outer_wall_area * (
                    self._est_width / (2 * self._est_width + 2 * self._est_length))
         
            
            #Creates an outer wall for each zone and assigns building elements             
            for idx, zone in enumerate(self.thermal_zones):
                #Creates only for Zones which are Pools an Outer Wall as Pool Wall 
                if (idx < self.numZones and key == "PoolWall"):
                    continue
                elif (idx >= self.numZones and key != "PoolWall"):
                    continue
                # create wall and set building elements
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

            if value[1] == 0 or value[1] == 180:

                self.window_area[value[1]] = self._est_win_area * (
                    self._est_length / (2 * self._est_width + 2 * self._est_length)
                )

            elif value[1] == 90 or value[1] == 270:

                self.window_area[value[1]] = self._est_win_area * (
                    self._est_width / (2 * self._est_width + 2 * self._est_length)
                )

            """
            There is no real classification for windows, so this is a bit hard
            code - will be fixed sometime.
            """
     
            for idx, zone in enumerate(self.thermal_zones):
                 #Only created for Zones which are not Pools
                if (idx >= self.numZones):
                    continue
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

            self.outer_area[value[1]] = self._est_roof_area

            for idx, zone in enumerate(self.thermal_zones):
                #Only created for Zones which are not Pools
                if (idx >= self.numZones):
                    continue
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

            self.outer_area[value[1]] = self._est_floor_area    
            
            for idx, zone in enumerate(self.thermal_zones):  
                #Creates only for Zones which are Pools a Ground Floor as Pool Floor
                if (idx < self.numZones and key == "Pool Floor With Earth Contact"):
                    continue
                elif (idx >= self.numZones and key != "Pool Floor With Earth Contact"):
                    continue
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

            for idx, zone in enumerate(self.thermal_zones):
                #Creates only for Zones which are Pools a Inner Wall as Wall
                if (idx < self.numZones and key == "InnerPoolWall"):
                    continue
                elif (idx >= self.numZones and key != "InnerPoolWall"):
                    continue 
                inner_wall = InnerWall(zone)
                inner_wall.name = key
                inner_wall.load_type_element(
                    year=self.year_of_construction,
                    construction=self.construction_type,
                    data_class=self.parent.data)
                inner_wall.tilt = value[0]
                inner_wall.orientation = value[1]        

        # CEILINGS #
        for key, value in self.ceiling_names.items(): 
            for idx, zone in enumerate(self.thermal_zones):
                #Only created for Zones which are not Pools
                if (idx >= self.numZones):
                    continue   
                
                if self.number_of_floors > 1:
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
            for idx, zone in enumerate(self.thermal_zones):
                #Creates only for Zones which are Pools a Floor as Pool Floor
                if (idx < self.numZones and key == "Pool Area Above Technical Room"):
                    continue
                elif (idx >= self.numZones and key != "Pool Area Above Technical Room"):
                    continue
                
                if key == "Floor" and self.number_of_floors > 1:
                    floor = Floor(zone)
                    floor.name = key
                    floor.load_type_element(
                        year=self.year_of_construction,
                        construction=self.construction_type,
                        data_class=self.parent.data)
                    floor.tilt = value[0]
                    floor.orientation = value[1] 
                        
        zoneAreas = []
        for i in range(1, 9):
            zone = "Zone " + str(i)
            if zone in self.poolsInDict.keys():
                zoneAreas.append(self.poolsInDict[zone]["Total area of zone (including water surface) [m²]"])
            else:
                zoneAreas.append(0)            

        #Calculates building surface area and surface areas of each zone and orientation.
        for key, value in self.outer_area.items():
            self.set_outer_wall_area(value, key)

        #Calculates window surface areas for each zone and orientation.
        for key, value in self.window_area.items():
            self.set_window_area(value, key)

        #Calculates inner wall area as sum of innerWalls, ceiling and floor for each zone
        zoneId=0
        for idx, zone in enumerate(self.thermal_zones):
            while zoneId < len(zoneAreas) and zoneAreas[zoneId]==0:                    
                zoneId+=1 
            zone.set_inner_wall_area()
            zoneId+=1
        
        # Calculate additional Parameters for Pools out of the input from Excel stored in "poolsInDict"
        # Results will be stored in paramRecord Dict for each Pool
        numOfPools = 0
        for zone in self.thermal_zones:
            if zone.name == "Schwimmhalle":
                numOfPools = len(zone.paramRecord)                
                for pool in zone.paramRecord.keys():                    
                    paramRecord = dict()
    
                    ## T_pool ##
                    paramRecord["T_pool"] = self.poolsInDict[pool]["Pool temperature"]
    
                    ## A_pool ##
                    paramRecord["A_pool"] = self.poolsInDict[pool]["Water surface"]
    
                    ## d_pool ##
                    paramRecord["d_pool"] = self.poolsInDict[pool]["Depth pool"]
    
                    ## V_pool ##
                    paramRecord["V_pool"] = self.poolsInDict[pool]["Water volume"]
                    
                    ## Q ## 
                    # Hilfsparameter zur Berechnung von Q
                    # k
                    if self.poolsInDict[pool]["Filter kombination"] == "without ozone" or self.poolsInDict[pool]["Filter kombination"] == "with bromine":
                        k = 0.5
                    elif self.poolsInDict[pool]["Filter kombination"] == "with ozone":
                        k = 0.6
                    elif self.poolsInDict[pool]["Filter kombination"] == "with ultrafiltration":
                        k = 1
                    else:
                        k = None
                    # m, a, n
                    if pool == "Kleinkinderbecken":
                        m = 2
                    elif pool.startswith("Freiformbecken") or pool == "Nichtschwimmerbecken" or pool == "Mehrzweckbecken":
                        a = 2.7
                        n = 1
                    elif pool == "Schwimmerbecken" or pool == "Springerbecken":
                        a = 4.5
                        n = 1
                    else:
                        a = None
                        n = None
                        m = None
                    # Nennbelastung N
                    if pool == "Kleinkinderbecken" and m is not None and k is not None:
                        N = (self.poolsInDict[pool]["Water volume"]) * m * k
                    elif n is not None and a is not None:
                        N = (self.poolsInDict[pool]["Water surface"]) * n/a
                    else:
                        N = None
                    # Berechnung von Q
                    if N is not None and k is not None:
                        Q_H = N/k
                    else:
                        Q_H = 0    
                    if pool == "Kleinkinderbecken" and self.poolsInDict[pool]["Water surface"] < 20 and m is not None:
                        Q_K = m * self.poolsInDict[pool]["Water volume"]
                    else:
                        Q_K = 0
                    Q_B = self.poolsInDict[pool]["Perimeter pool"]
                    if self.poolsInDict[pool]["Perimeter pool"] > 40:
                        Q = max(Q_B, Q_H)
                    else: 
                        Q = min(Q_H, Q_K, Q_B)
                    # Umrechnung in m³/h
                    Q = Q/3600
                    paramRecord["Q"] = Q
    
                    ## Q_night ##
                    Q_night = self.poolsInDict[pool]["Volume flow wastewater treatment night"]
                    if Q_night < Q_B:
                        Q_night = Q_B
                    Q_night = Q_night/3600
                    paramRecord["Q_night"] = Q_night
    
                    ## V_storage ##
                    # Parameter v_f
                    if self.poolsInDict[pool]["Filter type"] == "Activated carbon filter with ozone" or self.poolsInDict[pool]["Filter type"] == "Two-layer filter with ozone":
                        v_f = 50
                    elif self.poolsInDict[pool]["Filter type"] == "Open quick filter":
                        v_f = 15
                    elif (self.poolsInDict[pool]["Filter type"] == "Closed quick filter" 
                    or self.poolsInDict[pool]["Filter type"] == "Closed sorption filter" 
                    or self.poolsInDict[pool]["Filter type"] == "Open suction filter" 
                    or self.poolsInDict[pool]["Filter type"] == "Quantozone filter" 
                    or self.poolsInDict[pool]["Filter type"] == "Quartz gravel filter" 
                    or self.poolsInDict[pool]["Filter type"] == "Two-layer filter"):
                        if self.poolsInDict[pool]["Water type"] == "Freshwater":
                            v_f = 30
                        else:
                            v_f = 20
                    else:
                        v_f = None
                    v_f = v_f/3600
                    # A_Filter
                    if v_f is not None:
                        A_Filter = Q/v_f
                    else:
                        A_Filter = None
                    # V_v
                    if a is not None:
                        V_v = 0.075 * self.poolsInDict[pool]["Water surface"] / a
                    else:
                        V_v = None
                    # V_w
                    if self.poolsInDict[pool]["Perimeter pool"] > 0:
                        V_w = 0.052 * self.poolsInDict[pool]["Water surface"] * 10**(-0.144*Q/self.poolsInDict[pool]["Perimeter pool"])
                    else:
                        V_w = None
                    # V_fs
                    if A_Filter is not None:
                        V_fs = A_Filter * 5
                    else:
                        V_fs = None
                    # Berechnung V_storage
                    if V_fs is not None and V_w is not None and V_v is not None:
                        V_storage = V_fs + V_v + V_w
                    else:
                        V_storage = 0
                    paramRecord["V_storage"] = V_storage
                    
                    ## beta ##
                    if pool.startswith("Freiformbecken") or pool == "Mehrzweckbecken":
                        beta_inUse = 40
                    else:
                        if self.poolsInDict[pool]["Depth pool"] > 1.35:
                            beta_inUse = 28
                        else:
                            beta_inUse = 40
                    beta_inUse = beta_inUse/3600
                    paramRecord["beta_inUse"] = beta_inUse
                    
                    ## use_parialLoad ##
                    paramRecord["use_partialLoad"] = self.poolsInDict[pool]["Night setback"]
                    
                    ## use_idealHeatExchanger ##
                    paramRecord["use_idealHeatExchanger"] = self.poolsInDict[pool]["Ideal heat recovery"]
                    
                    ## use_HeatRecovery ##
                    paramRecord["use_HRS"] = self.poolsInDict[pool]["Heat recovery rinsing wastewater"]
                    paramRecord["efficiencyHRS"] = self.poolsInDict[pool]["Heat recovery rate rinsing wastewater"]                
    
                    ## use_poolCover ##
                    paramRecord["use_poolCover"] = self.poolsInDict[pool]["Pool covering outside operating hours"]
    
                    ## use_wavePool ##
                    paramRecord["use_wavePool"] = self.poolsInDict[pool]["Operation of artificial waves"]
                    paramRecord["h_wave"] = self.poolsInDict[pool]["Wave height"]
                    paramRecord["w_wave"] = self.poolsInDict[pool]["Wave width"]
                    paramRecord["wavePool_period"] = self.poolsInDict[pool]["Interval wave operation"]
                    paramRecord["wavePool_startTime"] = self.poolsInDict[pool]["Wave operation starting time"]
                    paramRecord["wavePool_width"] = self.poolsInDict[pool]["Width wave pool"]
                    
                    ## waterRecycling ##
                    paramRecord["use_waterRecycling"] = self.poolsInDict[pool]["Wastewater treatment"]
    
                    ## x_recycling ##
                    paramRecord["x_recycling"] = self.poolsInDict[pool]["Wastewater treatment rate"]
    
                    ## m_flow_out ##
                    m_Besucher = 0.03 * 995.65 * self.poolsInDict[pool]["Visitor number"] * 1/(24*3600)
                    m_Filter = 995.65 * self.poolsInDict[pool]["Filter rinses per week"] * V_fs * 1/(7*24*3600)
                    m_flow_out = max(m_Besucher, m_Filter)
                    paramRecord["m_flow_out"] = m_flow_out
                    
                    ## poolWalls ##
                    paramRecord["AInnerPoolWall"] = self.poolsInDict[pool]["Pool wall without earth contact"]
                    paramRecord["APoolWallWithEarthContact"] = self.poolsInDict[pool]["Pool wall with earth contact"]
                    paramRecord["APoolFloorWithEarthContact"] = self.poolsInDict[pool]["Pool floor with earth contact"]
                    paramRecord["AInnerPoolFloor"] = self.poolsInDict[pool]["Pool floor without earth contact"]
                    paramRecord["hConWaterHorizontal"] = self.poolsInDict[pool]["hConWaterHorizontal"]
                    paramRecord["hConWaterVertical"] = self.poolsInDict[pool]["hConWaterVertical"]
                    paramRecord["PoolWallParam"] = self.poolsInDict[pool]["PoolWallParam"]                                    
                    
                    #Sets Data to Record
                    zone.paramRecord[pool] = paramRecord                                     

        self.number_of_pools = numOfPools        
       
        
    def setPoolBaseParameters(self, waterSurface, areaCorrection = False):
        """
        Creating basic swimming pool building with one pool for beginners and one for swimmers.
        Zone areas and volumes are calculated from the WATER SURFACE according to 'Koordinierungskreis 
        Bäder - Richtlinien für den Bäderbau - 2013'. Therefore, the NET LEASED AREA is used as 
        WATER SURFACE. The building contains the zones 1 - 5 and 7.
        """
        ws = waterSurface
        
        # Create dict for zones and pools
        poolsInDict = dict()
        poolsInDict["Schwimmerbecken"] = dict()
        if ws >= 412.5:
            poolsInDict["Nichtschwimmerbecken"] = dict()   
         
        for i in range(1,9):
            if i != 6 and i !=7:
                zoneNum = "Zone " + str(i)                
                poolsInDict[zoneNum] = dict()                
                
        # Calculate zone areas and volumes according to 'Koordinierungskreis Bäder - 
        # Richtlinien für den Bäderbau - 2013'
        
        # Zone 1
        # zoneArea = entrance + management room
        zoneArea = 12 + ws * 0.2
        poolsInDict["Zone 1"]["Total area of zone (including water surface) [m²]"] = zoneArea
        
        # Zone 2
        # zoneArea = changingRooms + sanitaryObjects + cleaningRoom + corridors         
        changingRooms = 3.675 + math.ceil(ws**0.58 / (14 * 2)) * 21.7 + math.ceil(ws**0.58 / (7 * 2)) * 23.625
        sanitaryObjects = math.ceil(ws * 0.02)
        cleaningRoom = 2
        corridors = (math.ceil(ws**0.58 / 14) * 3.1 + math.ceil(ws**0.58 / 7) * 3.375) * 1.5
        zoneArea = changingRooms + sanitaryObjects + cleaningRoom + corridors        
        poolsInDict["Zone 2"]["Total area of zone (including water surface) [m²]"] = zoneArea

        # Zone 3
        # zoneArea = sanitary blocks + additional showers         
        if ws <= 150:
            zoneArea = 45.24
        elif ws <= 500:
            zoneArea = 82.53
        else:
            numShowers = ws**0.5            
            # (Due to the arrangement of the sanitary rooms, 4 showers will be added at once for additional capacity)
            numShowers = math.ceil(numShowers / 4) * 4
            numSanitaryDoubleBlocks = math.floor(numShowers/20)            
            numAdditionalShowers = (numShowers - numSanitaryDoubleBlocks * 20) / 4
            zoneArea = numSanitaryDoubleBlocks * 82.53 + numAdditionalShowers * 10.44 # 4 additional showers 
            
        poolsInDict["Zone 3"]["Total area of zone (including water surface) [m²]"] = zoneArea
        
        
        
        # Zone 4       
        if ws < 412.5:
            poolsInDict["Schwimmerbecken"]["Water surface"] = ws
            
        else:            
            
            if ws <= 582:
                poolsInDict["Nichtschwimmerbecken"]["Water surface"] = 100
                beginnerPoolWidth = 8   
                beginnerPoolLength = 10
            else:
                poolsInDict["Nichtschwimmerbecken"]["Water surface"] = 166.7
                beginnerPoolWidth = 10   
                beginnerPoolLength = 16.66
                
            poolsInDict["Schwimmerbecken"]["Water surface"] = ws - poolsInDict["Nichtschwimmerbecken"]["Water surface"]
            
        #Assign respective pool from basic pool areas, which defines the aspect ratio
        reference = min([312.5, 415, 830, 1050, 1250], key = lambda \
                x:abs(x - poolsInDict["Schwimmerbecken"]["Water surface"]))
        
        if reference < 830:
            mainPoolLength = 25
        else:
            mainPoolLength = 50
        
        mainPoolWidth = poolsInDict["Schwimmerbecken"]["Water surface"]/mainPoolLength
        
        if ws >= 412.5:
            hallLength = mainPoolLength + beginnerPoolWidth + 8.25            
        else:
            hallLength = mainPoolLength + 4.5
            
        hallWidth = mainPoolWidth + 4.5    
        zoneArea = hallWidth * hallLength
        
        if ws >= 412.5:
            poolsInDict["Nichtschwimmerbecken"]["Depth pool"] = 0.975
            poolsInDict["Nichtschwimmerbecken"]["Water volume"] = \
                poolsInDict["Nichtschwimmerbecken"]["Depth pool"] * \
                    poolsInDict["Nichtschwimmerbecken"]["Water surface"]        
        
        poolsInDict["Schwimmerbecken"]["Depth pool"] = 3
        poolsInDict["Schwimmerbecken"]["Water volume"] = poolsInDict["Schwimmerbecken"]["Depth pool"] * \
            poolsInDict["Schwimmerbecken"]["Water surface"]
        
        poolsInDict["Zone 4"]["Total area of zone (including water surface) [m²]"] = zoneArea
        
        # Zone 5
        # zoneArea = First aid room + swimming master room + + Swimming equipment room + Cleaning equipment room
        poolsInDict["Zone 5"]["Total area of zone (including water surface) [m²]"] = 43  
        
        # Zone 8
        zoneArea = ws + ws * (1/24) + 25
        poolsInDict["Zone 8"]["Total area of zone (including water surface) [m²]"] = zoneArea
        
        # Zone area correction
        correctionFactor=1
        if areaCorrection == True and ws >= 250:
            correctionFactor = (2293.6*math.log(ws)-10723)/(2.8549*ws+333.64)
            
        for value in poolsInDict.keys():
            if str(value).startswith("Zone"):
                zoneArea = poolsInDict[value]["Total area of zone (including water surface) [m²]"] = \
                    poolsInDict[value]["Total area of zone (including water surface) [m²]"] * correctionFactor
                poolsInDict[value]["Total area of zone (including water surface) [m²]"] = round(zoneArea, 2)
                            
        # Air volumes of all zones        
        poolsInDict["Zone 1"]["Air volume [m³]"] = \
            round(poolsInDict["Zone 1"]["Total area of zone (including water surface) [m²]"] * 2.75, 2) 
        poolsInDict["Zone 2"]["Air volume [m³]"] = \
            round(poolsInDict["Zone 2"]["Total area of zone (including water surface) [m²]"] * 2.75, 2)
        poolsInDict["Zone 3"]["Air volume [m³]"] = \
            round(poolsInDict["Zone 3"]["Total area of zone (including water surface) [m²]"] * 2.75, 2)
        poolsInDict["Zone 4"]["Air volume [m³]"] = \
            round(poolsInDict["Zone 4"]["Total area of zone (including water surface) [m²]"] * 6, 2)
        poolsInDict["Zone 5"]["Air volume [m³]"] = \
            round(poolsInDict["Zone 5"]["Total area of zone (including water surface) [m²]"] * 2.5, 2)
        poolsInDict["Zone 8"]["Air volume [m³]"] = \
            round(poolsInDict["Zone 8"]["Total area of zone (including water surface) [m²]"] * 3.5, 2)
        
        # Additional pool data
        poolsInDict["Schwimmerbecken"]["Pool temperature"] = 299.15        
        poolsInDict["Schwimmerbecken"]["Perimeter pool"] = 2 * mainPoolWidth + 2 * mainPoolLength                     
        poolsInDict["Schwimmerbecken"]["Visitor number"] = round(ws**0.58 * 2/3, 0) #num of changing rooms
        poolsInDict = self.basicPoolDataRecord(poolsInDict, "Schwimmerbecken")        

        
        if ws >= 412.5:
            poolsInDict["Nichtschwimmerbecken"]["Pool temperature"] = 299.15
            poolsInDict["Nichtschwimmerbecken"]["Perimeter pool"] = 2 * beginnerPoolWidth + 2 * beginnerPoolLength
            poolsInDict["Nichtschwimmerbecken"]["Visitor number"] = round(ws**0.58 * 1/3, 0) 
            poolsInDict = self.basicPoolDataRecord(poolsInDict, "Nichtschwimmerbecken")
        return poolsInDict
        
    def basicPoolDataRecord(self, poolsInDict, poolName):
        poolsInDict[poolName]["Night setback"] = "true"        
        poolsInDict[poolName]["Volume flow wastewater treatment night"] = 30        
        poolsInDict[poolName]["Pool covering outside operating hours"] = "false"        
        poolsInDict[poolName]["Operation of artificial waves"] = "false"        
        poolsInDict[poolName]["Wave height"] = 0        
        poolsInDict[poolName]["Wave width"] = 0        
        poolsInDict[poolName]["Wastewater treatment"] = "true"        
        poolsInDict[poolName]["Wastewater treatment rate"] = 0.8       
        poolsInDict[poolName]["Filter rinses per week"] = 2        
        poolsInDict[poolName]["Filter kombination"] = "without ozone"        
        poolsInDict[poolName]["Filter type"] = "Open suction filter"        
        poolsInDict[poolName]["Water type"] = "Freshwater"  
        poolsInDict[poolName]["Ideal heat recovery"] = "true"
        poolsInDict[poolName]["Heat recovery rinsing wastewater"] = "true"
        poolsInDict[poolName]["Heat recovery rate rinsing wastewater"] = 0.8
        poolsInDict[poolName]["Interval wave operation"] = 1800
        poolsInDict[poolName]["Wave operation starting time"] = 0
        poolsInDict[poolName]["Width wave pool"] = 10/30*100
        poolsInDict[poolName]["Pool floor without earth contact"] = 0.001
        poolsInDict[poolName]["Pool floor with earth contact"] = 559.82
        poolsInDict[poolName]["Pool wall without earth contact"] = 21.658
        poolsInDict[poolName]["Pool wall with earth contact"] = 143.32
        poolsInDict[poolName]["hConWaterHorizontal"] = 50.0
        poolsInDict[poolName]["hConWaterVertical"] = 5200.0
        poolsInDict[poolName]["PoolWallParam"] = "AixLib.DataBase.Pools.SwimmingPoolWall.ConcreteConstruction()"
        return poolsInDict
        
    
    @property
    def office_layout(self):
        return self._office_layout

    @office_layout.setter
    def office_layout(self, value):
        if value is not None:
            self._office_layout = value
        else:
            self._office_layout = 0

    @property
    def window_layout(self):
        return self._window_layout

    @window_layout.setter
    def window_layout(self, value):
        if value is not None:
            self._window_layout = value
        else:
            self._window_layout = 0

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
