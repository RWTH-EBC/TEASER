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
    - always 4 walls, 1 roof, 1 floor, 4 windows, one door (default orientation?)
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
        mode for the internal gains calculation done in AixLib:

        1. Temperature and activity degree dependent heat flux calculation for persons. The
           calculation is based on  SIA 2024 (default)
        2. Temperature and activity degree independent heat flux calculation for persons, the max.
           heatflowrate is prescribed by the parameter
           fixed_heat_flow_rate_persons.
        3. Temperature and activity degree dependent calculation with
           consideration of moisture and co2. The moisture calculation is
           based on SIA 2024 (2015) and regards persons and non-persons, the co2 calculation is based on
           Engineering ToolBox (2004) and regards only persons.
    inner_wall_approximation_approach : str
        'teaser_default' (default) sets length of inner walls = typical
            length * height of floors + 2 * typical width * height of floors
        'typical_minus_outer' sets length of inner walls = 2 * typical
            length * height of floors + 2 * typical width * height of floors
            - length of outer or interzonal walls
        'typical_minus_outer_extended' like 'typical_minus_outer', but also
            considers that
            a) a non-complete "average room" reduces its circumference
              proportional to the square root of the area
            b) rooftops, windows and ground floors (= walls with border to
                soil) may have a vertical share
    construction_data : str
        Construction type of used wall constructions default is "existing
        state"

        - existing state:
          construction of walls according to existing state in TABULA
        - usual refurbishment:
          construction of walls according to usual refurbishment in
          TABULA
        - advanced refurbishment:
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
            inner_wall_approximation_approach='teaser_default',
            construction_data=None):

        super(TerracedHouse, self).__init__(
            parent,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu,
            internal_gains_mode,
            inner_wall_approximation_approach,
            construction_data)

        self.construction_data = construction_data
        self.number_of_floors = number_of_floors
        self.height_of_floors = height_of_floors

        self._construction_data_1 = self.construction_data.value + '_1_TH'
        self._construction_data_2 = self.construction_data.value + '_2_TH'

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
            (2007, 2010): {
                'rt1': 1.1712,
                'rt2': 0.0,
                'ow1': 0.5405,
                'ow2': 0.0,
                'gf1': 1.0631,
                'gf2': 0.0,
                'win1': 0.2739,
                'win2': 0.0,
                'door': 0.009},
            (1999, 2006): {
                'rt1': 0.5248,
                'rt2': 0.0,
                'ow1': 0.3762,
                'ow2': 0.0,
                'gf1': 0.3366,
                'gf2': 0.0,
                'win1': 0.1950,
                'win2': 0.0,
                'door': 0.009},
            (1979, 1998): {
                'rt1': 0.6235,
                'rt2': 0.0,
                'ow1': 0.3529,
                'ow2': 0.0,
                'gf1': 0.5059,
                'gf2': 0.0,
                'win1': 0.1518,
                'win2': 0.0,
                'door': 0.009},
            (1973, 1978): {
                'rt1': 0.8559,
                'rt2': 0.0,
                'ow1': 0.1982,
                'ow2': 0.0,
                'gf1': 0.5856,
                'gf2': 0.0,
                'win1': 0.1523,
                'win2': 0.0,
                'door': 0.009},
            (1961, 1972): {
                'rt1': 0.8488,
                'rt2': 0.0,
                'ow1': 0.4302,
                'ow2': 0.0,
                'gf1': 0.5814,
                'gf2': 0.0,
                'win1': 0.4337,
                'win2': 0.0,
                'door': 0.009},
            (1951, 1960): {
                'rt1': 1.0345,
                'rt2': 0.0,
                'ow1': 0.4368,
                'ow2': 0.0,
                'gf1': 0.6667,
                'gf2': 0.0,
                'win1': 0.1920,
                'win2': 0.0,
                'door': 0.009},
            (1931, 1950): {
                'rt1': 0.7895,
                'rt2': 0.0,
                'ow1': 0.3158,
                'ow2': 0.0,
                'gf1': 0.6526,
                'gf2': 0.0,
                'win1': 0.1389,
                'win2': 0.0,
                'door': 0.009},
            (1851, 1930): {
                'rt1': 0.5573,
                'rt2': 0.0,
                'ow1': 0.5043,
                'ow2': 0.0,
                'gf1': 0.4171,
                'gf2': 0.0,
                'win1': 0.1299,
                'win2': 0.0,
                'door': 0.009},
            (0, 1850): {
                'rt1': 0.9462,
                'rt2': 0.0,
                'ow1': 0.1613,
                'ow2': 0.1935,  # note that there is actually a ow2
                'gf1': 0.7097,
                'gf2': 0.0,
                'win1': 0.1054,
                'win2': 0.0,
                'door': 0.00}}

        self.building_age_group = None

        if self.with_ahu is True:
            self.central_ahu.profile_temperature = (
                7 * [293.15] +
                12 * [295.15] +
                5 * [293.15])
            self.central_ahu.profile_min_relative_humidity = (24 * [0.45])
            self.central_ahu.profile_max_relative_humidity = (24 * [0.55])
            self.central_ahu.profile_v_flow = (
                7 * [0.0] + 12 * [1.0] + 5 * [0.0])
