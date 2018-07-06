# created June 2015
# by TEASER4 Development Team


from teaser.logic.archetypebuildings.bmvbs.office import Office


class Institute4(Office):
    """Type Institute Building (type 4)

    The institute type 4 module contains a multi zone building which is based
    on an
    office building with an additional laboratory zone. The zonal
    distribution is based on investigations of the Forschungszentrum Juelich
    :cite:`Lauster.2018`. According to the dataset from Juelich,
    the typebuilding institute type 4 is based on the buildingsclass of BWZK
    with
    the number 2230, 2240 and 2250
    :cite:`Bauministerkonferenz.Dezember2010`. The estimation of exterior
    wall surfaces follows the approach for office buildings, but with adapted
    parameters :cite:`Lauster.2018`. This building type is by default
    equipped with an air handling unit without humidification.

    In detail the net leased area is divided into the following thermal zone
    areas:

    #. Office (22% of net leased area)
    #. Floor (20% of net leased area)
    #. Storage (28% of net leased area)
    #. Meeting (4% of net leased area)
    #. Restroom (4% of net leased area)
    #. ICT (2% of net leased area)
    #. Laboratory (20% of the net leased area)

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
    office_layout : int
        Structure of the floor plan of office buildings, default is 1,
        which is representative for one elongated floor.
            1: elongated 1 floor
            2: elongated 2 floors
            3: compact (e.g. for a square base building)
    window_layout : int
        Structure of the window facade type, default is 1, which is
        representative for a punctuated facade.
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
        zone area factor (float) and the zone usage from BoundaryConditions XML
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

    """

    def __init__(self,
                 parent,
                 name=None,
                 year_of_construction=None,
                 number_of_floors=None,
                 height_of_floors=None,
                 net_leased_area=None,
                 with_ahu=True,
                 office_layout=None,
                 window_layout=None,
                 construction_type=None):
        """Constructor of Institute4

        adds an additional zone "Laboratory"

        """

        super(Institute4, self).__init__(parent,
                                         name,
                                         year_of_construction,
                                         number_of_floors,
                                         height_of_floors,
                                         net_leased_area,
                                         with_ahu,
                                         office_layout,
                                         window_layout,
                                         construction_type)
        self.zone_area_factors["Office"] = \
            [0.22, "Group Office (between 2 and 6 employees)"]
        self.zone_area_factors["Floor"] = \
            [0.2, "Traffic area"]
        self.zone_area_factors["Laboratory"] = \
            [0.2, "Laboratory"]
        self.zone_area_factors["Storage"] = \
            [0.28, "Stock, technical equipment, archives"]
        self.zone_area_factors["Meeting"] = \
            [0.04, "Meeting, Conference, seminar"]
        self.zone_area_factors["Restroom"] = \
            [0.04, "WC and sanitary rooms in non-residential buildings"]
        self.zone_area_factors["ICT"] = \
            [0.02, "Data center"]
        self.est_exponent_wall = 0.6177
        self.est_factor_wall_area = 13.895

        self.central_ahu.humidification = False
