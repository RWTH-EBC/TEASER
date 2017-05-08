# created April 2017
# by TEASER Development Team

from teaser.logic.archetypebuildings.tabula.de.singlefamilyhouse import \
    SingleFamilyHouse


class MultiFamilyHouse(SingleFamilyHouse):
    """Archetype for TABULA Multi Family House

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
                construction of walls according to usual refurbishment in
                TABULA
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

        super(MultiFamilyHouse, self).__init__(
            parent,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu,
            construction_type)

        self.construction_type = construction_type
        self.number_of_floors = number_of_floors
        self.height_of_floors = height_of_floors

        self._outer_wall_names_1 = {
            "ExteriorFacadeNorth_1": [90.0, 0.0],
            "ExteriorFacadeEast_1": [90.0, 90.0],
            "ExteriorFacadeSouth_1": [90.0, 180.0],
            "ExteriorFacadeWest_1": [90.0, 270.0]}

        self._outer_wall_names_2 = {
            "ExteriorFacadeNorth_2": [90.0, 0.0],
            "ExteriorFacadeEast_2": [90.0, 90.0],
            "ExteriorFacadeSouth_2": [90.0, 180.0],
            "ExteriorFacadeWest_2": [90.0, 270.0]}

        self.roof_names_1 = {"Rooftop_1": [0, -1]}  # [0, -1]

        self.roof_names_2 = {"Rooftop_2": [0, -1]}

        self.ground_floor_names_1 = {
            "GroundFloor_1": [0, -2]}  # [0, -2]

        self.ground_floor_names_2 = {
            "GroundFloor_2": [0, -2]}

        self.door_names = {"Door": [90.0, 270]}

        self.window_names_1 = {
            "WindowFacadeNorth_1": [90.0, 0.0],
            "WindowFacadeEast_1": [90.0, 90.0],
            "WindowFacadeSouth_1": [90.0, 180.0],
            "WindowFacadeWest_1": [90.0, 270.0]}
        self.window_names_2 = {
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
                'rt1': 0.613,
                'rt2': 0.0,
                'ow1': 0.7753,
                'ow2': 0.0,
                'gf1': 0.0,
                'gf2': 0.3904,
                'win1': 0.1315,
                'win2': 0.0,
                'door': 0.009},
            (1860, 1918): {
                'rt1': 0.585,
                'rt2': 0.0,
                'ow1': 1.366,
                'ow2': 0.0,
                'gf1': 0.3211,
                'gf2': 0.2303,
                'win1': 0.157,
                'win2': 0.0,
                'door': 0.014},
            (1919, 1949): {
                'rt1': 0.7063,
                'rt2': 0.0,
                'ow1': 0.7766,
                'ow2': 0.0,
                'gf1': 0.47822,
                'gf2': 0.0,
                'win1': 0.173,
                'win2': 0.0,
                'door': 0.0066},
            (1949, 1957): {
                'rt1': 1.13,
                'rt2': 0.0,
                'ow1': 1.0613,
                'ow2': 0.0,
                'gf1': 0.559,
                'gf2': 0.161,
                'win1': 0.166,
                'win2': 0.0,
                'door': 0.018},
            (1958, 1968): {
                'rt1': 1.396,
                'rt2': 0.0,
                'ow1': 1.167,
                'ow2': 0.072,
                'gf1': 0.957,
                'gf2': 0.0,
                'win1': 0.224,
                'win2': 0.0,
                'door': 0.017},
            (1969, 1978): {
                'rt1': 1.05838,
                'rt2': 0.0,
                'ow1': 1.0266,
                'ow2': 0.0,
                'gf1': 0.4526,
                'gf2': 0.4277,
                'win1': 0.1977,
                'win2': 0.0,
                'door': 0.01156},
            (1979, 1983): {
                'rt1': 0.46667,
                'rt2': 0.0,
                'ow1': 0.738,
                'ow2': 0.0,
                'gf1': 0.386,
                'gf2': 0.0,
                'win1': 0.125,
                'win2': 0.0,
                'door': 0.00926},
            (1984, 1994): {
                'rt1': 0.8213,
                'rt2': 0.0,
                'ow1': 1.409,
                'ow2': 0.0,
                'gf1': 0.502,
                'gf2': 0.0,
                'win1': 0.198,
                'win2': 0.0,
                'door': 0.01333},
            (1995, 2001): {
                'rt1': 0.947,
                'rt2': 0.0,
                'ow1': 1.038,
                'ow2': 0.0,
                'gf1': 0.691,
                'gf2': 0.0,
                'win1': 0.266,
                'win2': 0.0,
                'door': 0.016},
            (2002, 2009): {
                'rt1': 0.58435,
                'rt2': 0.0,
                'ow1': 1.285,
                'ow2': 0.0,
                'gf1': 0.543,
                'gf2': 0.0,
                'win1': 0.1925,
                'win2': 0.0,
                'door': 0.0136},
            (2010, 2015): {
                'rt1': 0.70535,
                'rt2': 0.0,
                'ow1': 1.217,
                'ow2': 0.0,
                'gf1': 0.57647,
                'gf2': 0.0,
                'win1': 0.2246,
                'win2': 0.0,
                'door': 0.014},
            (2016, 2100): {
                'rt1': 0.70535,
                'rt2': 0.0,
                'ow1': 1.217,
                'ow2': 0.0,
                'gf1': 0.57647,
                'gf2': 0.0,
                'win1': 0.2246,
                'win2': 0.0,
                'door': 0.014}}

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
