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

        self._construction_type_1 = self.construction_type + '_1_MFH'
        self._construction_type_2 = self.construction_type + '_2_MFH'

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
            (0, 1859): {
                'rt1': 0.41965,
                'rt2': 0.0,
                'ow1': 1.10679,
                'ow2': 0.0,
                'gf1': 0.18434,
                'gf2': 0.07238,
                'win1': 0.15805,
                'win2': 0.0,
                'door': 0.00295},
            (1860, 1918): {
                'rt1': 0.32949,
                'rt2': 0.0,
                'ow1': 0.46795,
                'ow2': 0.0,
                'gf1': 0.32949,
                'gf2': 0.0,
                'win1': 0.17340,
                'win2': 0.0,
                'door': 0.00641},
            (1919, 1948): {
                'rt1': 0.41169,
                'rt2': 0.08078,
                'ow1': 0.84545,
                'ow2': 0.0,
                'gf1': 0.33091,
                'gf2': 0.08078,
                'win1': 0.18494,
                'win2': 0.0,
                'door': 0.00519},
            (1949, 1957): {
                'rt1': 0.56171,
                'rt2': 0.0,
                'ow1': 0.73101,
                'ow2': 0.0,
                'gf1': 0.56171,
                'gf2': 0.0,
                'win1': 0.15617,
                'win2': 0.0,
                'door': 0.00316},
            (1958, 1968): {
                'rt1': 0.31035,
                'rt2': 0.0,
                'ow1': 0.65165,
                'ow2': 0.0,
                'gf1': 0.31035,
                'gf2': 0.0,
                'win1': 0.16219,
                'win2': 0.0,
                'door': 0.00064},
            (1969, 1978): {
                'rt1': 0.46205,
                'rt2': 0.0,
                'ow1': 0.71642,
                'ow2': 0.0,
                'gf1': 0.46205,
                'gf2': 0.0,
                'win1': 0.17335,
                'win2': 0.0,
                'door': 0.00426},
            (1979, 1983): {
                'rt1': 0.37966,
                'rt2': 0.0,
                'ow1': 0.68364,
                'ow2': 0.0,
                'gf1': 0.37966,
                'gf2': 0.0,
                'win1': 0.15199,
                'win2': 0.0,
                'door': 0.00306},
            (1984, 1994): {
                'rt1': 0.32057,
                'rt2': 0.0,
                'ow1': 0.99589,
                'ow2': 0.0,
                'gf1': 0.32057,
                'gf2': 0.0,
                'win1': 0.20694,
                'win2': 0.0,
                'door': 0.00257},
            (1995, 2001): {
                'rt1': 0.33976,
                'rt2': 0.0,
                'ow1': 0.83329,
                'ow2': 0.0,
                'gf1': 0.33976,
                'gf2': 0.0,
                'win1': 0.19497,
                'win2': 0.0,
                'door': 0.0024},
            (2002, 2009): {
                'rt1': 0.26849,
                'rt2': 0.0,
                'ow1': 0.77534,
                'ow2': 0.0,
                'gf1': 0.28288,
                'gf2': 0.0,
                'win1': 0.14096,
                'win2': 0.0,
                'door': 0.00091},
            (2010, 2015): {
                'rt1': 0.24605,
                'rt2': 0.0,
                'ow1': 0.91433,
                'ow2': 0.0,
                'gf1': 0.24605,
                'gf2': 0.0,
                'win1': 0.18667,
                'win2': 0.0,
                'door': 0.0367},
            (2016, 2100): {
                'rt1': 0.24605,
                'rt2': 0.0,
                'ow1': 0.91433,
                'ow2': 0.0,
                'gf1': 0.24605,
                'gf2': 0.0,
                'win1': 0.18667,
                'win2': 0.0,
                'door': 0.0367}}

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
