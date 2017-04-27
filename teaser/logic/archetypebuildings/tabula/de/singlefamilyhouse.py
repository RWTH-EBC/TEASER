# created April 2017
# by TEASER Development Team

from teaser.logic.archetypebuildings.residential \
    import Residential
from teaser.logic.buildingobjects.boundaryconditions.boundaryconditions \
    import BoundaryConditions as UseCond
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.groundfloor \
    import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.thermalzone import ThermalZone


class SingleFamilyHouse(Residential):
    """Archetype for TABULA Single Family House

    Archetype according to TABULA building typology 
    (http://webtool.building-typology.eu/#bm). 
    
    Description of:
       - estimation factors
       - always 4 walls, 1 roof, 1 floor, 4 windows, one door (default 
       orientation?)
       - how we calcualte facade and window area
       - calcualte u-values
       - zones (one zone)
       - differences between TABULA und our approach (net floor area, height 
       and number of storeys)
       - how to proceed with rooftops (keep them as flat roofs or pitched 
       roofs? what orientation?)
       
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
    construction_type : str
        Construction type of used wall constructions default is "existing 
        state"
            existing state: 
                construction of walls according to existing state in TABULA
            usual refurbishment: 
                construction of walls according to usual refurbishment in TABULA
            advanced refurbishmet:
                construction of walls according to advanced refurbishment in 
                TABULA
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
            construction_type=None):

        super(SingleFamilyHouse, self).__init__(
            parent,
            name,
            year_of_construction,
            net_leased_area,
            with_ahu)

        self.construction_type = construction_type
        self.number_of_floors = number_of_floors
        self.height_of_floors = height_of_floors

        self.zone_area_factors = {"SingleDwelling": [1, "Living"]}

        self._outer_wall_names_1 = {
            "ExteriorFacadeNorth_1": [90.0, 0.0],
            "ExteriorFacadeEast_1": [90.0, 90.0],
            "ExteriorFacadeSouth_1": [90.0, 180.0],
            "ExteriorFacadeWest_1": [90.0, 270.0]}

        self._outer_wall_names_2 ={
            "ExteriorFacadeNorth_2": [90.0, 0.0],
            "ExteriorFacadeEast_2": [90.0, 90.0],
            "ExteriorFacadeSouth_2": [90.0, 180.0],
            "ExteriorFacadeWest_2": [90.0, 270.0]}

        self.roof_names = {"Rooftop_1": [0, -1],
                           "Rooftop_2": [0, -1]}  # [0, -1]

        self.ground_floor_names = {"GroundFloor_1": [0, -2],
                                   "GroundFloor_2": [0, -2]}  # [0, -2]

        self.door_names = {"Door": [90.0, 270]}

        self.window_names = {"WindowFacadeNorth_1": [90.0, 0.0],
                             "WindowFacadeEast_1": [90.0, 90.0],
                             "WindowFacadeSouth_1": [90.0, 180.0],
                             "WindowFacadeWest_1": [90.0, 270.0],
                             "WindowFacadeNorth_2": [90.0, 0.0],
                             "WindowFacadeEast_2": [90.0, 90.0],
                             "WindowFacadeSouth_2": [90.0, 180.0],
                             "WindowFacadeWest_2": [90.0, 270.0]}
        # [tilt, orientation]

        self.inner_wall_names = {"InnerWall": [90.0, 0.0]}

        self.ceiling_names = {"Ceiling": [0.0, -1]}

        self.floor_names = {"Floor": [0.0, -2]}

        # Rooftop1, Rooftop2, Wall1, Wall2, GroundFloor1, GroundFloor2, 
        # Window1, Window2, Door
        # Area/ReferenceFloorArea
        self.facade_estimation_factors = {
            (0, 1859): {
                'rt1': 0.61,
                'rt2': 0.61,
                'ow1': 0.78,
                'ow2': 0.78,
                'gf1': 0.0,
                'gf2': 0.39,
                'win1': 0.13,
                'win2': 0.0,
                'door': 0.0091},
            (1860, 1918): {
                'rt1': 0.61,
                'rt2': 0.61,
                'ow1': 0.78,
                'ow2': 0.0,
                'gf1': 0.0,
                'gf2': 0.39,
                'win1': 0.13,
                'win2': 0.0,
                'door': 0.0091},
            (1919, 1949): {
                'rt1': 0.61,
                'rt2': 0.61,
                'ow1': 0.78,
                'ow2': 0.0,
                'gf1': 0.0,
                'gf2': 0.39,
                'win1': 0.13,
                'win2': 0.0,
                'door': 0.0091},
            (1949, 1957): {
                'rt1': 0.61,
                'rt2': 0.61,
                'ow1': 0.78,
                'ow2': 0.0,
                'gf1': 0.0,
                'gf2': 0.39,
                'win1': 0.13,
                'win2': 0.0,
                'door': 0.0091},
            (1958, 1968): {
                'rt1': 0.61,
                'rt2': 0.61,
                'ow1': 0.78,
                'ow2': 0.0,
                'gf1': 0.0,
                'gf2': 0.39,
                'win1': 0.13,
                'win2': 0.0,
                'door': 0.0091},
            (1969, 1978): {
                'rt1': 0.61,
                'rt2': 0.61,
                'ow1': 0.78,
                'ow2': 0.0,
                'gf1': 0.0,
                'gf2': 0.39,
                'win1': 0.13,
                'win2': 0.0,
                'door': 0.0091},
            (1979, 1983): {
                'rt1': 0.61,
                'rt2': 0.61,
                'ow1': 0.78,
                'ow2': 0.0,
                'gf1': 0.0,
                'gf2': 0.39,
                'win1': 0.13,
                'win2': 0.0,
                'door': 0.0091},
            (1984, 1994): {
                'rt1': 0.61,
                'rt2': 0.61,
                'ow1': 0.78,
                'ow2': 0.0,
                'gf1': 0.0,
                'gf2': 0.39,
                'win1': 0.13,
                'win2': 0.0,
                'door': 0.0091},
            (1995, 2001): {
                'rt1': 0.61,
                'rt2': 0.61,
                'ow1': 0.78,
                'ow2': 0.0,
                'gf1': 0.0,
                'gf2': 0.39,
                'win1': 0.13,
                'win2': 0.0,
                'door': 0.0091},
            (2002, 2009): {
                'rt1': 0.61,
                'rt2': 0.61,
                'ow1': 0.78,
                'ow2': 0.0,
                'gf1': 0.0,
                'gf2': 0.39,
                'win1': 0.13,
                'win2': 0.0,
                'door': 0.0091},
            (2010, 2015): {
                'rt1': 0.61,
                'rt2': 0.61,
                'ow1': 0.78,
                'ow2': 0.0,
                'gf1': 0.0,
                'gf2': 0.39,
                'win1': 0.13,
                'win2': 0.0,
                'door': 0.0091},
            (2016, 2100): {
                'rt1': 0.61,
                'rt2': 0.61,
                'ow1': 0.78,
                'ow2': 0.0,
                'gf1': 0.0,
                'gf2': 0.39,
                'win1': 0.13,
                'win2': 0.0,
                'door': 0.0091}}

        self.building_age_group = None

        for key in self.facade_estimation_factors:
            if self.year_of_construction in range(key[0], key[1]) or \
                    self.year_of_construction == key[1]:
                self.building_age_group = (key[0], key[1])

        if self.with_ahu is True:
            self.central_ahu.profile_temperature = (
                7 * [293.15] +
                12 * [295.15] +
                6 * [293.15])
            self.central_ahu.profile_min_relative_humidity = (25 * [0.45])
            self.central_ahu.profile_max_relative_humidity = (25 * [0.55])
            self.central_ahu.profile_v_flow = (
                7 * [0.0] + 12 * [1.0] + 6 * [0.0])

    def generate_archetype(self):
        """Generates a SingleFamilyHouse archetype buildings
        
        With given values, this function generates an archetype building for 
        Tabula Single Family House.
        """

        # help area for the correct building area setting while using typeBldgs
        type_bldg_area = self.net_leased_area
        self.net_leased_area = 0.0

        self._living_area_per_floor = type_bldg_area / self.number_of_floors

        for key, value in self.zone_area_factors.items():
            zone = ThermalZone(parent=self)
            zone.name = key
            zone.area = type_bldg_area * value[0]
            use_cond = UseCond(parent=zone)
            use_cond.load_use_conditions(
                zone_usage=value[1])

        for key, value in self._outer_wall_names_1.items():
            self.outer_area[value[1]] = 0.0
        for key, value in self._outer_wall_names_2.items():
            self.outer_area[value[1]] = 0.0

        self.nr_of_orientation_1 = len(self._outer_wall_names_1)
        self.nr_of_orientation_2 = len(self._outer_wall_names_2)

        for key, value in self._outer_wall_names_1.items():
            self.outer_area[value[1]] += (
                (self.facade_estimation_factors[
                     self.building_age_group]['ow1'] * type_bldg_area) /
                self.nr_of_orientation_1)

            for zone in self.thermal_zones:
                outer_wall = OuterWall(zone)
                outer_wall.load_type_element(
                    year=self.year_of_construction,
                    construction=self.construction_type,
                    data_class=self.parent.data)
                outer_wall.name = key
                outer_wall.tilt = value[0]
                outer_wall.orientation = value[1]

        for key, value in self._outer_wall_names_2.items():
            self.outer_area[value[1]] += (
                (self.facade_estimation_factors[
                     self.building_age_group]['ow2'] * type_bldg_area) /
                self.nr_of_orientation_2)

            for zone in self.thermal_zones:
                outer_wall = OuterWall(zone)
                outer_wall.load_type_element(
                    year=self.year_of_construction,
                    construction=self.construction_type,
                    data_class=self.parent.data)
                outer_wall.name = key
                outer_wall.tilt = value[0]
                outer_wall.orientation = value[1]

        for key, value in self.outer_area.items():
            self.set_outer_wall_area(value, key)

        for zone in self.thermal_zones:
            zone.set_inner_wall_area()
            zone.set_volume_zone()
