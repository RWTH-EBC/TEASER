# created June 2015
# by TEASER4 Development Team

from teaser.logic.archetypebuildings.residential \
 import Residential

from teaser.logic.buildingobjects.boundaryconditions.boundaryconditions \
    import BoundaryConditions as UseCond
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.groundfloor\
 import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.thermalzone import ThermalZone


class SingleFamilyDwelling(Residential):
    '''Type Building SingleFamilyDwelling.

    Subclass from Building to represent SingleFamilyDwelling Buildings. Allows for
    easier distinction between different building types and specific functions
    and attributes.

    Parameters
    ----------
    parent: Project()
        The parent class of this object, the Project the Building belongs
        to. Allows for better control of hierarchical structures.
        Default is None

    name : str
        individual name

    year_of_construction : int
        year of first construction

    number_of_floors : int
        number of floors above ground

    height_of_floors : float
        average height of the floors

    net_leased_area : float
        total net leased area of building

    with_ahu : boolean
        if building has a central AHU or not

    residential_layout : int
        type of floor plan (default = 0)

        0: compact
        1: elongated/complex

    neighbour_buildings : int
        neighbour (default = 0)

        0: no neighbour
        1: one neighbour
        2: two neighbours

    attic : int
        type of attic (default = 0)

        0: flat roof
        1: non heated attic
        2: partly heated attic
        3: heated attic

    cellar : int
        type of cellar (default = 0)

        0: no cellar
        1: non heated cellar
        2: partly heated cellar
        3: heated cellar

    construction_type : str
        construction type (default = "heavy")

        heavy: heavy construction
        light: light construction

    dormer : str
        construction type

        0: no dormer
        1: dormer

    Note
    ----------

    The listed attributes are just the ones that are set by the user
    calculated values are not included in this list.


    Attributes
    ----------

    zone_area_factors : dict
        This dictionary contains the name of the zone (str), the
        zone area factor (float) and the zone usage (str). The values can be
        taken from Lichtmess

    outer_wall_names : dict
        This dictionary contains the name of the outer walls, their orientation
        and tilt

    roof_names : dict
        This dictionary contains the name of the roofs, their orientation
        and tilt

    ground_floor_names : dict
        This dictionary contains the name of the ground floors, their
        orientation and tilt

    window_names : dict
        This dictionary contains the name of the window, their
        orientation and tilt

    inner_wall_names : dict
        This dictionary contains the name of the inner walls, their
        orientation and tilt

    ceiling_names : dict
        This dictionary contains the name of the ceilings, their
        orientation and tilt

    floor_names : dict
        This dictionary contains the name of the floors, their
        orientation and tilt

    est_living_area_factor : float
        estimation factor for calculation of number of heated floors

    est_bottom_building_closure : float
        estimation factor to calculate ground floor area

    est_upper_building_closure : float
        estimation factor to calculate attic area

    est_factor_win_area : float
        estimation factor to calculate window area

    est_factor_cellar_area : float
        estimation factor to calculate heated cellar area
    '''

    def __init__(self,
                 parent,
                 name=None,
                 year_of_construction=None,
                 number_of_floors=None,
                 height_of_floors=None,
                 net_leased_area=None,
                 with_ahu=False,
                 residential_layout=None,
                 neighbour_buildings=None,
                 attic=None,
                 cellar=None,
                 dormer=None,
                 construction_type=None):

        '''Constructor of SingleFamilyDwelling


        '''

        super(SingleFamilyDwelling, self).__init__(parent, name, year_of_construction,
                                                   net_leased_area, with_ahu)

        self.residential_layout = residential_layout
        self.neighbour_buildings = neighbour_buildings
        self.attic = attic
        self.cellar = cellar
        self.dormer = dormer
        self.construction_type = construction_type
        self.number_of_floors = number_of_floors
        self.height_of_floors = height_of_floors

        # Parameters are default values for current calculation following IWU

        # [area factor, usage type(has to be set)]
        self.zone_area_factors = {"SingleDwelling": [1, "Living"]}

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

        self.est_living_area_factor = 0.75  # fW
        self.est_bottom_building_closure = 1.33  # p_FB
        self.est_upper_building_closure = 1.0
        self.est_factor_win_area = 0.2
        self.est_factor_cellar_area = 0.5

        self.nr_of_orientation = len(self.outer_wall_names)

        # estimated intermediate calculated values
        self._living_area_per_floor = 0
        self._number_of_heated_floors = 0
        self._est_factor_heated_cellar = 0
        self._est_factor_heated_attic = 0
        self._est_roof_area = 0
        self._est_ground_floor_area = 0.0
        self._est_win_area = 0
        self._est_outer_wall_area = 0.0
        self._est_cellar_wall_area = 0
        self._est_factor_volume = 0.0

        self.est_factor_neighbour = 0.0  # n_Nachbar
        self.est_extra_floor_area = 0.0  # q_Fa

        if self.neighbour_buildings == 0:
            self._est_factor_neighbour = 0.0
            self._est_extra_floor_area = 50.0
        elif self.neighbour_buildings == 1:
            self._est_factor_neighbour = 1.0
            self._est_extra_floor_area = 30.0
        elif self.neighbour_buildings == 2:
            self._est_factor_neighbour = 2.0
            self._est_extra_floor_area = 10.0

        self._est_facade_to_floor_area = 0.0  # p_Fa

        if self.residential_layout == 0:
            self._est_facade_to_floor_area = 0.66
        elif self.residential_layout == 1:
            self._est_facade_to_floor_area = 0.8

        self._est_factor_heated_attic = 0.0  # f_TB_DG
        self._est_area_per_floor = 0.0  # p_DA
        self._est_area_per_roof = 0.0  # p_OG

        if self.attic == 0:
            self._est_factor_heated_attic = 0.0
            self._est_area_per_floor = 1.33
            self._est_area_per_roof = 0.0
        elif self.attic == 1:
            self._est_factor_heated_attic = 0.0
            self._est_area_per_floor = 0.0
            self._est_area_per_roof = 1.33
        elif self.attic == 2:
            self._est_factor_heated_attic = 0.5
            self._est_area_per_floor = 0.75
            self._est_area_per_roof = 0.67
        elif self.attic == 3:
            self._est_factor_heated_attic = 1.0
            self._est_area_per_floor = 1.5
            self._est_area_per_roof = 0.0

        self._est_factor_heated_cellar = 0.0  # f_TB_KG

        if self.cellar == 0:
            self._est_factor_heated_cellar = 0.0
        elif self.cellar == 1:
            self._est_factor_heated_cellar = 0.0
        elif self.cellar == 2:
            self._est_factor_heated_cellar = 0.5
        elif self.cellar == 3:
            self._est_factor_heated_cellar = 1.0

        self._est_factor_dormer = 0.0

        if self.dormer == 0:
            self._est_factor_dormer = 1.0
        elif self.dormer == 1:
            self._est_factor_dormer = 1.3

        if self.with_ahu is True:
            self.central_ahu.profile_temperature = (7*[293.15] +
                                                    12*[295.15] +
                                                    6*[293.15])
            self.central_ahu.profile_min_relative_humidity = (25*[0.45])
            self.central_ahu.profile_max_relative_humidity = (25*[0.55])
            self.central_ahu.profile_v_flow = (7*[0.0] + 12*[1.0] +  6*[0.0])


    def generate_archetype(self):
        '''Generates a residential building.

        With given values, this class generates a type residential
        building according to TEASER requirements
        Berechnungsgrundlagen: IWU, "Kurzverfahren Energieprofil"; 2005.

        '''
        #help area for the correct building area setting while using typeBldgs
        type_bldg_area = self.net_leased_area
        self.net_leased_area = 0.0

        self._number_of_heated_floors = self._est_factor_heated_cellar + \
                    self.number_of_floors + self.est_living_area_factor\
                     *self._est_factor_heated_attic

        self._living_area_per_floor = type_bldg_area / \
                self._number_of_heated_floors

        self._est_ground_floor_area = self.est_bottom_building_closure * \
                    self._living_area_per_floor

        self._est_roof_area = self.est_upper_building_closure * \
                self._est_factor_dormer * self._est_area_per_floor * \
                self._living_area_per_floor

        self._top_floor_area = self._est_area_per_roof * \
                self._living_area_per_floor

        if self._est_roof_area == 0:
            self._est_roof_area = self._top_floor_area

        self._est_facade_area = self._est_facade_to_floor_area * \
                self._living_area_per_floor + self._est_extra_floor_area

        self._est_win_area = self.est_factor_win_area * type_bldg_area

        self._est_cellar_wall_area = self.est_factor_cellar_area * \
                self._est_factor_heated_cellar * self._est_facade_area

        self._est_outer_wall_area = (self._number_of_heated_floors * \
                self._est_facade_area) - self._est_cellar_wall_area - \
                self._est_win_area

        # self._est_factor_volume = type_bldg_area * 2.5

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
                                        "Kunststofffenster, Isolierverglasung")
                window.name = key
                window.tilt = value[0]
                window.orientation = value[1]

        for key, value in self.roof_names.items():

            self.outer_area[value[1]] = self._est_roof_area

            for zone in self.thermal_zones:
                roof = Rooftop(zone)
                roof.load_type_element(self.year_of_construction, \
                                       self.construction_type)
                roof.name = key
                roof.tilt = value[0]
                roof.orientation = value[1]

        for key, value in self.ground_floor_names.items():

            self.outer_area[value[1]] = self._est_ground_floor_area

            for zone in self.thermal_zones:
                ground_floor = GroundFloor(zone)
                ground_floor.load_type_element(self.year_of_construction, \
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

    def generate_from_gml(self):
        """enriches lod1 or lod2 data from citygml

        adds Zones, BoundaryConditions, Material settings for walls and
        windows to the geometric representation of CityGML

        number or height of floors need to be specified
        """

        type_bldg_area = self.net_leased_area
        self.net_leased_area = 0.0
        # create zones with their corresponding area, name and usage
        for key, value in self.zone_area_factors.items():
            zone = ThermalZone(self)
            zone.area = type_bldg_area * value[0]
            zone.name = key
            use_cond = UseCond(zone)
            use_cond.load_use_conditions(value[1])
            zone.use_conditions = use_cond
            zone.use_conditions.with_ahu = False
            zone.use_conditions.persons *= zone.area * 0.01
            zone.use_conditions.machines *= zone.area * 0.01

            for surface in self.gml_surfaces:
                if surface.surface_tilt is not None:
                    if surface.surface_tilt == 90:
                        outer_wall = OuterWall(zone)
                        outer_wall.load_type_element(self.year_of_construction,
                                                     self.construction_type)
                        outer_wall.name = surface.name
                        outer_wall.tilt = surface.surface_tilt
                        outer_wall.orientation = surface.surface_orientation

                        window = Window(zone)
                        window.load_type_element(self.year_of_construction,
                                                "Kunststofffenster, Isolierverglasung")
                        window.name = "asd"+str(surface.surface_tilt)
                        window.tilt = surface.surface_tilt
                        window.orientation = surface.surface_orientation

                    elif surface.surface_tilt == 0 and surface.surface_orientation ==\
                            -2:
                        outer_wall = GroundFloor(zone)
                        outer_wall.load_type_element(self.year_of_construction,
                                                     self.construction_type)
                        outer_wall.name = surface.name
                        outer_wall.tilt = surface.surface_tilt
                        outer_wall.orientation = surface.surface_orientation

                    else:
                        outer_wall = Rooftop(zone)
                        outer_wall.load_type_element(self.year_of_construction,
                                                     self.construction_type)
                        outer_wall.name = surface.name
                        outer_wall.tilt = surface.surface_tilt
                        outer_wall.orientation = surface.surface_orientation

            for key, value in self.inner_wall_names.items():

                for zone in self.thermal_zones:
                    inner_wall = InnerWall(zone)
                    inner_wall.load_type_element(self.year_of_construction,
                                                 self.construction_type)
                    inner_wall.name = key
                    inner_wall.tilt = value[0]
                    inner_wall.orientation = value[1]

            if self.number_of_floors > 1:

                for key, value in self.ceiling_names.items():

                    for zone in self.thermal_zones:
                        ceiling = Ceiling(zone)
                        ceiling.load_type_element(self.year_of_construction,
                                                  self.construction_type)
                        ceiling.name = key
                        ceiling.tilt = value[0]
                        ceiling.orientation = value[1]

                for key, value in self.floor_names.items():

                    for zone in self.thermal_zones:
                        floor = Floor(zone)
                        floor.load_type_element(self.year_of_construction,
                                                self.construction_type)
                        floor.name = key
                        floor.tilt = value[0]
                        floor.orientation = value[1]
            else:
                pass

        for surface in self.gml_surfaces:
            if surface.surface_tilt is not None:
                if surface.surface_tilt != 0 and surface.surface_orientation !=\
                        -2 and surface.surface_orientation != -1:
                    self.set_outer_wall_area(surface.surface_area *
                                             (1- self.est_factor_win_area),
                                             surface.surface_orientation)
                else:
                    self.set_outer_wall_area(surface.surface_area,
                                             surface.surface_orientation)
        for surface in self.gml_surfaces:

            if surface.surface_tilt != 0 and surface.surface_orientation !=\
                    -2 and surface.surface_orientation != -1:
                self.set_window_area(surface.surface_area *
                                     self.est_factor_win_area,
                                     surface.surface_orientation)

        for zone in self.thermal_zones:
            zone.set_inner_wall_area()
            zone.set_volume_zone()

    @property
    def residential_layout(self):
        return self._residential_layout

    @residential_layout.setter
    def residential_layout(self, value):
        if value is not None:
            self._residential_layout = value
        else:
            self._residential_layout = 0

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
    def attic(self):
        return self._attic

    @attic.setter
    def attic(self, value):
        if value is not None:
            self._attic = value
        else:
            self._attic = 0

    @property
    def cellar(self):
        return self._cellar

    @cellar.setter
    def cellar(self, value):
        if value is not None:
            self._cellar = value
        else:
            self._cellar = 0

    @property
    def dormer(self):
        return self._dormer

    @dormer.setter
    def dormer(self, value):
        if value is not None:
            self._dormer = value
        else:
            self._dormer = 0

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
