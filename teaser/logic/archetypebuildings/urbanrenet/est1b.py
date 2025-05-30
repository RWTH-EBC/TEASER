# created June 2015
# by TEASER4 Development Team

from teaser.logic.archetypebuildings.urbanrenet.est1a \
    import EST1a


class EST1b(EST1a):
    """Urban Fabric Type EST1b.

    Subclass from EST1a for urban fabric type EST1b, with the addition of
    variable number of apartments as input parameter.


    Parameters
    ----------
    parent: Project()
        The parent class of this object, the Project the Building belongs
        to. Allows for better control of hierarchical structures. If not None it
        adds this Building instance to Project.buildings.
        Default is None
    name : str
        Individual name
    height_of_floors : float [m]
        Average height of the buildings' floors
    number_of_floors : int
        Number of building's floors above ground
    year_of_construction : int
        Year of first construction
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

    neighbour_buildings : int
        Number of neighbour buildings. CAUTION: this will not change
        the orientation of the buildings wall, but just the overall
        exterior wall and window area(!) (default = 0)

        0. no neighbour
        1. one neighbour
        2. two neighbours

    construction_data : str
        Construction type of used wall constructions default is "heavy")
            heavy: heavy construction
            light: light construction
    number_of_apartments : int
        number of apartments inside Building (default = 1)
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
            neighbour_buildings=None,
            construction_data=None,
            number_of_apartments=None,
            inner_wall_approximation_approach='teaser_default'
    ):
        """Constructor of EST1b
        """

        super(EST1b, self).__init__(
            parent,
            name,
            year_of_construction,
            number_of_floors,
            height_of_floors,
            net_leased_area,
            with_ahu,
            internal_gains_mode,
            neighbour_buildings,
            construction_data,
            inner_wall_approximation_approach)

        self.number_of_apartments = number_of_apartments
        self.est_factor_facade_to_volume = 0.87
