# created December 2018
# by Hardy Lottermann


from teaser.logic.archetypebuildings.bmvbs.office import Office
import collections

class School(Office):
    """Type School Building

    The school module contains a multi zone building which is based
    on an office building with additional class room, wc, traffic area,
    storage, rooms, office, restaurant and kitchen zones.
    The zonal distribution is based on the research paper "Entwicklung einer
    Datenbank mit Modellgebäuden für energiebezogene Untersuchungen,
    insbesondere der Wirtschaftlichkeit" (Zentrum für Umweltbewusstes Bauen).

    The estimation of exterior wall surfaces follows the approach for office
    buildings, but with adapted parameters due to the research paper. This
    building type is by default equipped with an air handling unit.

    In detail the net leased area is divided into the following thermal zone
    areas. Due to the size of the school (small/big) the ratio of the net leased
    area differs:

    #. Class room (41-48% of net leased area)
    #. WC (3-5% of net leased area)
    #. Traffic area (30-33% of net leased area)
    #. Storage (2-6% of net leased area)
    #. Rooms (4-11% of net leased area)
    #. Office (4-5% of net leased area)
    #. Restaurant (5% of net leased area) [only for small schools]
    #. Kitchen (2% of net leased area) [only for small schools]


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
        """Constructor of School

        Adds a additional zones "Class room", "WC", "Traffic area", "Storage",
        "Rooms", "Office", "Restaurant" and "Kitchen"

        """

        super(School, self).__init__(parent,
                                     name,
                                     year_of_construction,
                                     number_of_floors,
                                     height_of_floors,
                                     net_leased_area,
                                     with_ahu,
                                     office_layout,
                                     window_layout,
                                     construction_type)


        self.zone_area_factors = collections.OrderedDict()

        # small school
        if net_leased_area < 5003 * 0.89:
            self.zone_area_factors["Class room"] = \
                [0.41, "Class room (school), group room (kindergarden)"]
            self.zone_area_factors["WC"] = \
                [0.05, "WC and sanitary rooms in non-residential buildings"]
            self.zone_area_factors["Traffic area"] = \
                [0.30, "Traffic area"]
            self.zone_area_factors["Storage"] = \
                [0.02, "Stock, technical equipment, archives"]
            self.zone_area_factors["Rooms"] = \
                [0.11, "Further common rooms"]
            self.zone_area_factors["Office"] = \
                [0.04, "Group Office (between 2 and 6 employees)"]
            self.zone_area_factors["Restaurant"] = \
                [0.05, "Restaurant"]
            self.zone_area_factors["Kitchen"] = \
                [0.02, "Kitchen - preparations, storage"]

            self.height_of_floors = 3.35
            self.est_factor_wall_area = 0.351
            self.est_factor_win_area = 0.217
        # big school (without kitchen and restaurant)
        else:
            self.zone_area_factors["Class room"] = \
                [0.48, "Class room (school), group room (kindergarden)"]
            self.zone_area_factors["WC"] = \
                [0.03, "WC and sanitary rooms in non-residential buildings"]
            self.zone_area_factors["Traffic area"] = \
                [0.33, "Traffic area"]
            self.zone_area_factors["Storage"] = \
                [0.06, "Stock, technical equipment, archives"]
            self.zone_area_factors["Rooms"] = \
                [0.04, "Further common rooms"]
            self.zone_area_factors["Office"] = \
                [0.05, "Group Office (between 2 and 6 employees)"]

            self.height_of_floors = 4.45
            self.est_factor_wall_area = 0.455
            self.est_factor_win_area = 0.271

        self.est_exponent_win = 1
        self.est_exponent_wall = 1.0
