# created April 2017
# by TEASER Development Team

from teaser.logic.archetypebuildings.tabula.de.singlefamilyhouse import \
    SingleFamilyHouse


class TerracedHouse(SingleFamilyHouse):
    """Archetype for TABULA Single Family House

    Archetype according to TABULA building typology
    (http://webtool.building-typology.eu/#bm).

    Description of:
       - estimation factors
       - always 4 walls, 1 roof, 1 floor, 4 windows, one door (default
       orientation?)
       - how we calculate facade and window area
       - calculate u-values
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
            advanced refurbishment:
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

        super(TerracedHouse, self).__init__(
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

        self._construction_type_1 = self.construction_type + '_1_TH'
        self._construction_type_2 = self.construction_type + '_2_TH'

        self.zone_area_factors = {"SingleDwelling": [1, "Living"]}

        self._outer_wall_names_1 = {
            "ExteriorFacadeNorth_1": [90.0, 0.0],
            "ExteriorFacadeSouth_1": [90.0, 180.0]}

        self._outer_wall_names_2 = {
            "ExteriorFacadeNorth_2": [90.0, 0.0],
            "ExteriorFacadeSouth_2": [90.0, 180.0]}

        self.roof_names_1 = {"Rooftop_1": [0, -1]}  # [0, -1]

        self.roof_names_2 = {"Rooftop_2": [0, -1]}

        self.ground_floor_names_1 = {
            "GroundFloor_1": [0, -2]}  # [0, -2]

        self.ground_floor_names_2 = {
            "GroundFloor_2": [0, -2]}

        self.door_names = {"Door": [90.0, 270]}

        self.window_names_1 = {
            "WindowFacadeNorth_1": [90.0, 0.0],
            "WindowFacadeSouth_1": [90.0, 180.0]}
        self.window_names_2 = {
            "WindowFacadeNorth_2": [90.0, 0.0],
            "WindowFacadeSouth_2": [90.0, 180.0]}

        # [tilt, orientation]

        self.inner_wall_names = {"InnerWall": [90.0, 0.0]}

        self.ceiling_names = {"Ceiling": [0.0, -1]}

        self.floor_names = {"Floor": [0.0, -2]}

        # Rooftop1, Rooftop2, Wall1, Wall2, GroundFloor1, GroundFloor2,
        # Window1, Window2, Door
        # Area/ReferenceFloorArea
        self.facade_estimation_factors = {
            (1860, 1918): {
                'rt1': 0.625,
                'rt2': 0.0,
                'ow1': 0.77604,
                'ow2': 0.0,
                'gf1': 0.625,
                'gf2': 0.0,
                'win1': 0.18854,
                'win2': 0.0,
                'door': 0.02083},
            (1919, 1948): {
                'rt1': 0.44602,
                'rt2': 0.0,
                'ow1': 0.56726,
                'ow2': 0.0,
                'gf1': 0.44602,
                'gf2': 0.0,
                'win1': 0.19027,
                'win2': 0.0,
                'door': 0.0177},
            (1949, 1957): {
                'rt1': 0.54133,
                'rt2': 0.0,
                'ow1': 0.898,
                'ow2': 0.0,
                'gf1': 0.54133,
                'gf2': 0.0,
                'win1': 0.31133,
                'win2': 0.0,
                'door': 0.01333},
            (1958, 1968): {
                'rt1': 0.39487,
                'rt2': 0.0,
                'ow1': 0.3453,
                'ow2': 0.0,
                'gf1': 0.39487,
                'gf2': 0.0,
                'win1': 0.11538,
                'win2': 0.0,
                'door': 0.01709},
            (1969, 1978): {
                'rt1': 0.57453,
                'rt2': 0.0,
                'ow1': 0.5066,
                'ow2': 0.0,
                'gf1': 0.57453,
                'gf2': 0.0,
                'win1': 0.22075,
                'win2': 0.0,
                'door': 0.01887},
            (1979, 1983): {
                'rt1': 0.9037,
                'rt2': 0.0,
                'ow1': 0.50093,
                'ow2': 0.0,
                'gf1': 0.67593,
                'gf2': 0.0,
                'win1': 0.18796,
                'win2': 0.0,
                'door': 0.01852},
            (1984, 1994): {
                'rt1': 0.50703,
                'rt2': 0.0,
                'ow1': 0.39766,
                'ow2': 0.0,
                'gf1': 0.43828,
                'gf2': 0.0,
                'win1': 0.14688,
                'win2': 0.0,
                'door': 0.01563},
            (1995, 2001): {
                'rt1': 0.51946,
                'rt2': 0.0,
                'ow1': 0.30336,
                'ow2': 0.09329,
                'gf1': 0.34832,
                'gf2': 0.0,
                'win1': 0.15034,
                'win2': 0.0,
                'door': 0.01678},
            (2002, 2009): {
                'rt1': 0.60066,
                'rt2': 0.0,
                'ow1': 0.92566,
                'ow2': 0.0,
                'gf1': 0.46513,
                'gf2': 0.0,
                'win1': 0.23882,
                'win2': 0.0,
                'door': 0.01316},
            (2010, 2015): {
                'rt1': 0.38622,
                'rt2': 0.0,
                'ow1': 0.70306,
                'ow2': 0.35306,
                'gf1': 0.34592,
                'gf2': 0.0,
                'win1': 0.1301,
                'win2': 0.01327,
                'door': 0.01378},
            (2016, 2100): {
                'rt1': 0.38622,
                'rt2': 0.0,
                'ow1': 0.70306,
                'ow2': 0.35306,
                'gf1': 0.34592,
                'gf2': 0.0,
                'win1': 0.1301,
                'win2': 0.01327,
                'door': 0.01378}}

        self.building_age_group = None

        if self.with_ahu is True:
            self.central_ahu.profile_temperature = (
                7 * [293.15] +
                12 * [295.15] +
                6 * [293.15])
            self.central_ahu.profile_min_relative_humidity = (25 * [0.45])
            self.central_ahu.profile_max_relative_humidity = (25 * [0.55])
            self.central_ahu.profile_v_flow = (
                7 * [0.0] + 12 * [1.0] + 6 * [0.0])
