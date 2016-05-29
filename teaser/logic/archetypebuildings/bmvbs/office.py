# created June 2015
# by TEASER4 Development Team


import math

from teaser.logic.archetypebuildings.nonresidential\
 import NonResidential
from teaser.logic.buildingobjects.boundaryconditions.boundaryconditions import BoundaryConditions as UseCond
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.groundfloor\
 import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.thermalzone import ThermalZone


class Office(NonResidential):
    '''Type Office Building

    Subclass from TypeBuilding to represent office buildings. Allows for
    easier distinction between different building types and specific functions
    and attributes.
    Superclass for institute building.

    German office building, containing 6 zones. Each zone has 4 outer walls,
    4 windows a roof and a floor. Default values are given according to BMVBS.
    Changing these default values is expert mode.

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

    office_layout : int
        type of floor plan (default = 0)

        0: use default values
        1: elongated 1 floor
        2: elongated 2 floors
        3: compact

    window_layout : int
        type of window layout (default = 0)

        0: use default values
        1: punctuated facade
        2: banner facade
        3: full glazing

    construction_type : str
        construction type (default = "heavy")

        heavy: heavy construction
        light: light construction


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

    gross_factor : float
        gross factor used to calculate the area of the different zones

    est_factor_wall_area : float
        estimation factor to calculate outer wall area

    est_exponent_wall : float
        another estimation factor to calculate outer wall area

    est_factor_win_area : float
        estimation factor to calculate window area

    est_exponent_win : float
        another estimation factor to calculate window area

    '''

    def __init__(self,
                 parent=None,
                 name=None,
                 year_of_construction=None,
                 number_of_floors=None,
                 height_of_floors=None,
                 net_leased_area=None,
                 with_ahu=False,
                 office_layout=None,
                 window_layout=None,
                 construction_type=None):
        '''Constructor of Office


        '''
        super(Office, self).__init__(parent,
                                     name,
                                     year_of_construction,
                                     net_leased_area,
                                     with_ahu)

        self.office_layout = office_layout
        self.window_layout = window_layout
        self.construction_type = construction_type
        self.number_of_floors = number_of_floors
        self.height_of_floors = height_of_floors
        # Parameters are default values for current
        # calculation following Lichtmess

        # [area factor, usage type(has to be set)]
        self.zone_area_factors = \
            {"Meeting": [0.04, "Meeting, Conference, seminar"],
             "Storage": [0.15, "Stock, technical equipment, archives"],
             "Office": [0.5, "Group Office (between 2 and 6 employees)"],
             "Restroom": [0.04, "WC and sanitary rooms in non-residential buildings"],
             "ICT": [0.02, "Data center"],
             "Floor": [0.25, "Traffic area"]}

        # [tilt, orientation]
        self.outer_wall_names = {"Exterior Facade North": [90, 0],
                                 "Exterior Facade East": [90, 90],
                                 "Exterior Facade South": [90, 180],
                                 "Exterior Facade West": [90, 270]}

        self.roof_names = {"Rooftop": [0, -1]}

        self.ground_floor_names = {"Ground Floor": [0, -2]}

        self.window_names = {"Window Facade North": [90, 0],
                             "Window Facade East": [90, 90],
                             "Window Facade South": [90, 180],
                             "Window Facade West": [90, 270]}

        self.inner_wall_names = {"InnerWall": [90, 0]}

        self.ceiling_names = {"Ceiling": [0, -1]}

        self.floor_names = {"Floor": [0, -2]}

        self.gross_factor = 1.15
        self.est_factor_wall_area = 0.7658
        self.est_exponent_wall = 0.9206
        self.est_factor_win_area = 0.074
        self.est_exponent_win = 1.0889

        # estimated intermediate calculated values
        self._est_outer_wall_area = 0
        self._est_win_area = 0
        self._est_roof_area = 0
        self._est_floor_area = 0
        self._est_facade_area = 0
        self._est_width = 0
        self._est_length = 0

        if self.window_layout == 0:
            self.corr_factor_wall = 1.0
            self.corr_factor_win = 1.0
        elif self.window_layout == 1:
            self.corr_factor_wall = 0.75
            self.corr_factor_win = 0.25
        elif self.window_layout == 2:
            self.corr_factor_wall = 0.5
            self.corr_factor_win = 0.5
        elif self.window_layout == 3:
            self.corr_factor_wall = 0.1
            self.corr_factor_win = 0.9
        else:
            raise ValueError("window_layout value has to be between 0 - 3")

        if self.office_layout == 0 or self.office_layout == 1:
            self._est_width = 13.0
        elif self.office_layout == 2:
            self._est_width = 15.0
        elif self.office_layout == 3:
            self._est_width = math.sqrt((self.net_leased_area /
                                         self.number_of_floors) *
                                         self.gross_factor)
        else:
            raise ValueError("office_layout value has to be between 0 - 3")
        if self.net_leased_area is not None and self.number_of_floors is not \
                None:
            self._est_length = ((self.net_leased_area / self.number_of_floors) *
                            self.gross_factor) / self._est_width
        else:
            pass

        if self.with_ahu is True:
            self.central_ahu.profile_temperature = (7*[293.15] +
                                                    12*[295.15] +
                                                    6*[293.15])
            self.central_ahu.profile_min_relative_humidity = (25*[0.45])
            self.central_ahu.profile_max_relative_humidity = (25*[0.55])
            self.central_ahu.profile_v_flow = (7*[0.0] + 12*[1.0] + 6*[0.0])

    def generate_archetype(self):
        '''Generates an office building.

        With given values, this class generates a type building according to
        TEASER requirements.

        '''
        #help area for the correct building area setting while using typeBldgs
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

            zone.use_conditions.persons = zone.area * 0.01 * \
                zone.use_conditions.persons
            zone.use_conditions.machines = zone.area * 0.01 * \
                zone.use_conditions.machines

            # self.thermal_zones.append(zone)

        # statistical estimation of the facade

        self._est_outer_wall_area = self.est_factor_wall_area * \
                                type_bldg_area ** self.est_exponent_wall
        self._est_win_area = self.est_factor_win_area * \
                             type_bldg_area ** self.est_exponent_win
        self._est_roof_area = (type_bldg_area / self.number_of_floors) * \
                              self.gross_factor
        self._est_floor_area = (type_bldg_area / self.number_of_floors) * \
                               self.gross_factor

        # manipulation of wall according to facade design
        # (received from window_layout)

        self._est_facade_area = self._est_outer_wall_area + self._est_win_area

        if not self.window_layout == 0:
            self._est_outer_wall_area = self._est_facade_area * \
                                        self.corr_factor_wall
            self._est_win_area = self._est_facade_area * self.corr_factor_win
        else:
            pass

        # set the facade area to the four orientations

        for key, value in self.outer_wall_names.items():
            # North and South
            if value[1] == 0 or value[1] == 180:
                self.outer_area[value[1]] = self._est_outer_wall_area * \
                 (self._est_length / (2 * self._est_width + 2 * self._est_length))
            # East and West
            elif value[1] == 90 or value[1] == 270:

                self.outer_area[value[1]] = self._est_outer_wall_area * \
                (self._est_width / (2 * self._est_width + 2 * self._est_length))
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

                self.window_area[value[1]] = self._est_win_area * \
                (self._est_length / (2 * self._est_width + 2 * self._est_length))

            elif value[1] == 90 or value[1] == 270:

                self.window_area[value[1]] = self._est_win_area * \
                (self._est_width / (2 * self._est_width + 2 * self._est_length))

            '''
            There is no real classification for windows, so this is a bit hard
            code - will be fixed sometime.
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
                roof.load_type_element(self.year_of_construction,
                                       self.construction_type)
                roof.name = key
                roof.tilt = value[0]
                roof.orientation = value[1]
                # zone.outer_walls.append(roof)

        for key, value in self.ground_floor_names.items():

            self.outer_area[value[1]] = self._est_floor_area

            for zone in self.thermal_zones:
                ground_floor = GroundFloor(zone)
                ground_floor.load_type_element(self.year_of_construction,
                                               self.construction_type)
                ground_floor.name = key
                ground_floor.tilt = value[0]
                ground_floor.orientation = value[1]
                # zone.outer_walls.append(ground_floor)

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
            if surface.surface_tilt is not None:
                if surface.surface_tilt != 0 and surface.surface_orientation !=\
                        -2 and surface.surface_orientation != -1:
                    self.set_window_area(surface.surface_area *
                                         self.est_factor_win_area,
                                         surface.surface_orientation)

        for zone in self.thermal_zones:
            zone.set_inner_wall_area()
            zone.set_volume_zone()

    @property
    def office_layout(self):
        return self._office_layout

    @office_layout.setter
    def office_layout(self, value):
        if value is not None:
            self._office_layout = value
        else:
            self._office_layout = 0

    @property
    def window_layout(self):
        return self._window_layout

    @window_layout.setter
    def window_layout(self, value):
        if value is not None:
            self._window_layout = value
        else:
            self._window_layout = 0

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
