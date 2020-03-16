# created April 2017
# by TEASER Development Team

from teaser.logic.archetypebuildings.tabula.de.singlefamilyhouse import \
    SingleFamilyHouse


class ApartmentBlock(SingleFamilyHouse):
    """Archetype for TABULA Apartment Block

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
            internal_gains_mode=1,
            construction_type=None):

        super(ApartmentBlock, self).__init__(
            parent,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu,
            internal_gains_mode,
            construction_type)

        self.construction_type = construction_type
        self.number_of_floors = number_of_floors
        self.height_of_floors = height_of_floors

        self._construction_type_1 = self.construction_type + '_1_AB'
        self._construction_type_2 = self.construction_type + '_2_AB'

        self.zone_area_factors = {"SingleDwelling": [1, "Living"]}

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
            (2007, 2010): {
                'rt1': 0.2378,
                'rt2': 0.0,
                'ow1': 0.5625,
                'ow2': 0.0,
                'gf1': 0.2470,
                'gf2': 0.0,
                'win1': 0.3174,
                'win2': 0.0,
                'door': 0.009},
            (1999, 2006): {
                'rt1': 0.24497,
                'rt2': 0.0,
                'ow1': 0.3186,
                'ow2': 0.0,
                'gf1': 0.23934,
                'gf2': 0.0,
                'win1': 0.20636,
                'win2': 0.0,
                'door': 0.009},
            (1979, 1998): {
                'rt1': 0.3133,
                'rt2': 0.0,
                'ow1': 0.4487,
                'ow2': 0.0,
                'gf1': 0.3021,
                'gf2': 0.0,
                'win1': 0.1714,
                'win2': 0.0,
                'door': 0.009},
            (1973, 1978): {
                'rt1': 0.2404,
                'rt2': 0.0,
                'ow1': 0.0752,
                'ow2': 0.2235,
                'gf1': 0.1974,
                'gf2': 0.0430,
                'win1': 0.3859,
                'win2': 0.0,
                'door': 0.009},
            (1961, 1972): {
                'rt1': 0.3934,
                'rt2': 0.0,
                'ow1': 0.18529,
                'ow2': 0.35515,
                'gf1': 0.3934,
                'gf2': 0.0,
                'win1': 0.2537,
                'win2': 0.0,
                'door': 0.009},
            (1951, 1960): {
                'rt1': 0.5224,
                'rt2': 0.0,
                'ow1': 0.8846,
                'ow2': 0.0,
                'gf1': 0.4712,
                'gf2': 0.0,
                'win1': 0.1824,
                'win2': 0.0,
                'door': 0.009},
            (1931, 1950): {
                'rt1': 0.2374,
                'rt2': 0.0,
                'ow1': 0.6473,
                'ow2': 0.0,
                'gf1': 0.2374,
                'gf2': 0.0,
                'win1': 0.1830,
                'win2': 0.0,
                'door': 0.009},
            (1851, 1930): {
                'rt1': 0.6313,
                'rt2': 0.0,
                'ow1': 0.8313,
                'ow2': 0.0,
                'gf1': 0.4042,
                'gf2': 0.0,
                'win1': 0.1960,
                'win2': 0.0,
                'door': 0.009},
            (0, 1850): {
                'rt1': 0.5970,
                'rt2': 0.0,
                'ow1': 0.4501,
                'ow2': 0.6655,
                'gf1': 0.4722,
                'gf2': 0.0698,
                'win1': 0.1555,
                'win2': 0.0,
                'door': 0.009}}

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
