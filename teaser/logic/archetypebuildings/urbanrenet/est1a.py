# created June 2015
# by TEASER4 Development Team

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


class EST1a(Residential):
    """Archetype for Urban Fabric Type EST1a.

    Subclass from Residential for urban fabric type EST1a. Boundary values
    for this archetype are taken from :cite:`Hegger.2014`. The archetype
    calculation
    is adapted from :cite:`KurzverfahrenIWU`, with the change of using the
    facade area to volume ratio of the building. For further information see
    :cite:`Lauster.2016`.

    Parameters
    ----------
    parent: Project()
        The parent class of this object, the Project the Building belongs
        to. Allows for better control of hierarchical structures. If not None it
        adds this Building instance to Project.buildings.
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
    neighbour_buildings : int
        Number of neighbour buildings. CAUTION: this will not change
        the orientation of the buildings wall, but just the overall
        exterior wall and window area(!) (default = 0)
            0: no neighbour
            1: one neighbour
            2: two neighbours
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
    est_factor_win_area : float
        Estimation factor to calculate window area
    est_factor_facade_to_volume : float
        Estimation factor to describe the facade area to volume ratio

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
            neighbour_buildings=None,
            construction_type=None):
        """Constructor of EST1a
        """

        super(EST1a, self).__init__(
            parent,
            name,
            year_of_construction,
            net_leased_area,
            with_ahu)

        self.neighbour_buildings = neighbour_buildings
        self.construction_type = construction_type
        self.number_of_apartments = 1
        self.number_of_floors = number_of_floors
        self.height_of_floors = height_of_floors

        # Parameters are default values for current calculation following
        # Hegger

        # [area factor, usage type(has to be set)]
        self.zone_area_factors = {}
        for value in range(1, self._number_of_apartments + 1):
            zone_name = "Apartment " + str(value)
            zone = {zone_name: [1 / self._number_of_apartments, "Living"]}
            self.zone_area_factors.update(zone)

        self.outer_wall_names = {"Exterior Facade North": [90.0, 0.0],
                                 "Exterior Facade East": [90.0, 90.0],
                                 "Exterior Facade South": [90.0, 180.0],
                                 "Exterior Facade West": [90.0, 270.0]}
        # [tilt, orientation]

        self.roof_names = {"Rooftop": [0, -1]}  # [0, -1]

        self.ground_floor_names = {"Ground Floor": [0, -2]}  # [0, -2]

        self.window_names = {"Window Facade North": [90.0, 0.0],
                             "Window Facade East": [90.0, 90.0],
                             "Window Facade South": [90.0, 180.0],
                             "Window Facade West": [90.0, 270.0]}
        # [tilt, orientation]

        self.inner_wall_names = {"InnerWall": [90.0, 0.0]}

        self.ceiling_names = {"Ceiling": [0.0, -1]}

        self.floor_names = {"Floor": [0.0, -2]}

        self.est_factor_win_area = 0.2
        self.est_factor_facade_to_volume = 0.87

        self.nr_of_orientation = len(self.outer_wall_names)

        # estimated intermediate calculated values
        self._est_roof_area = 0
        self._est_ground_floor_area = 0.0
        self._est_win_area = 0
        self._est_outer_wall_area = 0.0

        self.est_factor_neighbour = 0.0

        if self.neighbour_buildings == 0:
            self._est_factor_neighbour = 0.0
        elif self.neighbour_buildings == 1:
            self._est_factor_neighbour = 1.0
        elif self.neighbour_buildings == 2:
            self._est_factor_neighbour = 2.0

        if self.with_ahu is True:
            self.central_ahu.profile_temperature = (7 * [293.15] +
                                                    12 * [295.15] +
                                                    6 * [293.15])
            #  according to :cite:`DeutschesInstitutfurNormung.2016`
            self.central_ahu.profile_min_relative_humidity = (25 * [0.45])
            #  according to :cite:`DeutschesInstitutfurNormung.2016b`  and
            # :cite:`DeutschesInstitutfurNormung.2016`
            self.central_ahu.profile_max_relative_humidity = (25 * [0.65])
            self.central_ahu.profile_v_flow = (
                7 * [0.0] + 12 * [1.0] + 6 * [0.0])  # according to user  #
            # profile in :cite:`DeutschesInstitutfurNormung.2016`

    def generate_archetype(self):
        """Generates a residential building.

        With given values, this class generates a type residential
        building according to TEASER requirements.

        """
        # help area for the correct building area setting while using typeBldgs
        self.thermal_zones = None
        type_bldg_area = self.net_leased_area
        self.net_leased_area = 0.0

        self._est_ground_floor_area = type_bldg_area / self.number_of_floors

        self._est_roof_area = type_bldg_area / self.number_of_floors

        self._est_win_area = self.est_factor_win_area * type_bldg_area * \
            (1 - self._est_factor_neighbour / 4)

        self._est_outer_wall_area = (self.est_factor_facade_to_volume *
                                     type_bldg_area *
                                     self.height_of_floors -
                                     self._est_ground_floor_area -
                                     self._est_roof_area -
                                     self._est_win_area) *\
            (1 - self._est_factor_neighbour / 4)

        for key, value in self.zone_area_factors.items():
            zone = ThermalZone(self)
            zone.name = key
            zone.area = type_bldg_area * value[0]
            use_cond = UseCond(zone)
            use_cond.load_use_conditions(value[1])

            zone.use_conditions = use_cond

        for key, value in self.outer_wall_names.items():
            # North and South

            if value[1] == 0 or value[1] == 180.0:
                self.outer_area[value[1]] = self._est_outer_wall_area / \
                    self.nr_of_orientation
            # East and West
            elif value[1] == 90 or value[1] == 270:

                self.outer_area[value[1]] = self._est_outer_wall_area / \
                    self.nr_of_orientation

            for zone in self.thermal_zones:
                # create wall and set building elements
                outer_wall = OuterWall(zone)
                outer_wall.load_type_element(self.year_of_construction,
                                             self.construction_type)
                outer_wall.name = key
                outer_wall.tilt = value[0]
                outer_wall.orientation = value[1]

        for key, value in self.window_names.items():

            if value[1] == 0 or value[1] == 180:

                self.window_area[value[1]] = self._est_win_area / \
                    self.nr_of_orientation

            elif value[1] == 90 or value[1] == 270:

                self.window_area[value[1]] = self._est_win_area / \
                    self.nr_of_orientation

            '''
            There is no real classification for windows, so this is a bit hard
            code - will be fixed sometime
            '''
            for zone in self.thermal_zones:
                window = Window(zone)

                window.load_type_element(self.year_of_construction,
                                         "Kunststofffenster, Isolierverglasung"
                                         )
                window.name = key
                window.tilt = value[0]
                window.orientation = value[1]

        for key, value in self.roof_names.items():

            self.outer_area[value[1]] = self._est_roof_area

            for zone in self.thermal_zones:
                roof = Rooftop(zone)
                roof.load_type_element(self.year_of_construction,
                                       self.construction_type)
                roof.name = key
                roof.tilt = value[0]
                roof.orientation = value[1]

        for key, value in self.ground_floor_names.items():

            self.outer_area[value[1]] = self._est_ground_floor_area

            for zone in self.thermal_zones:
                ground_floor = GroundFloor(zone)
                ground_floor.load_type_element(self.year_of_construction,
                                               self.construction_type)
                ground_floor.name = key
                ground_floor.tilt = value[0]
                ground_floor.orientation = value[1]

        for key, value in self.inner_wall_names.items():

            for zone in self.thermal_zones:
                inner_wall = InnerWall(zone)
                inner_wall.load_type_element(self.year_of_construction,
                                             self.construction_type)
                inner_wall.name = key
                inner_wall.tilt = value[0]
                inner_wall.orientation = value[1]
                # zone.inner_walls.append(inner_wall)

        if self.number_of_floors > 1:

            for key, value in self.ceiling_names.items():

                for zone in self.thermal_zones:
                    ceiling = Ceiling(zone)
                    ceiling.load_type_element(self.year_of_construction,
                                              self.construction_type)
                    ceiling.name = key
                    ceiling.tilt = value[0]
                    ceiling.orientation = value[1]
                    # zone.inner_walls.append(ceiling)

            for key, value in self.floor_names.items():

                for zone in self.thermal_zones:
                    floor = Floor(zone)
                    floor.load_type_element(self.year_of_construction,
                                            self.construction_type)
                    floor.name = key
                    floor.tilt = value[0]
                    floor.orientation = value[1]
                    # zone.inner_walls.append(floor)
        else:
            pass

        for key, value in self.outer_area.items():
            self.set_outer_wall_area(value, key)
        for key, value in self.window_area.items():
            self.set_window_area(value, key)

        for zone in self.thermal_zones:
            zone.set_inner_wall_area()
            zone.set_volume_zone()

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

    @property
    def neighbour_buildings(self):
        return self._neighbour_buildings

    @neighbour_buildings.setter
    def neighbour_buildings(self, value):
        if value is not None:
            self._neighbour_buildings = value
        else:
            self._neighbour_buildings = 0

    @property
    def number_of_apartments(self):
        return self._number_of_apartments

    @number_of_apartments.setter
    def number_of_apartments(self, value):
        if value is not None and value >= 1:
            self._number_of_apartments = value
        else:
            self._number_of_apartments = 1
