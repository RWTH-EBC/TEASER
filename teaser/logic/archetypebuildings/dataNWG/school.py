# created February 2023
# by Paul Seiwert


import math
import collections
from teaser.logic.archetypebuildings.nonresidential import NonResidential
from teaser.logic.buildingobjects.useconditions import UseConditions as UseCond
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.thermalzone import ThermalZone


class School(NonResidential):
    """Archetype School Building

    Subclass from NonResidential archetype class to represent school buildings.
    The school module contains a multi zone building. The building is based on multiple
    databases and methods. The share of the 10 usage zones are from the results of
    :cite:'Jagnow.2021'.
    Each zone has 4 outer walls, 5 windows (1 roof window), a roof and a
    ground floor. Depending on zone usage (typical length and width), an
    interior wall area is assigned. Exterior wall, window, ground floor and roof surfaces are
    calculated in relation to the net-leased area based on the aggregated mean data of
    :cite:'ENOB:dataNWG.2021', analogue to the Tabula approach. Departing from the Tabula
    approach material properties are used according to BMVBS.

    In detail the net leased area is divided into the following thermal zone
    areas:

    #. Classrooms (38.5% of net leased area)
    #. Floor (27.5% of net leased area)
    #. Storage (16% of net leased area)
    #. Office (2.5% of net leased area)
    #. Restroom (3% of net leased area)
    #. Further common rooms (6% of net leased area)
    #. Canteen (3.5% of net leased area)
    #. Lecture hall, auditorium (3% of net leased area)


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
        1: Temperature and activity degree dependent heat flux calculation for persons. The
           calculation is based on  SIA 2024 (default)
        2: Temperature and activity degree independent heat flux calculation for persons, the max.
           heatflowrate is prescribed by the parameter
           fixed_heat_flow_rate_persons.
        3: Temperature and activity degree dependent calculation with
           consideration of moisture and co2. The moisture calculation is
           based on SIA 2024 (2015) and regards persons and non-persons, the co2 calculation is based on
           Engineering ToolBox (2004) and regards only persons.
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
        zone area factor (float) and the zone usage from BoundaryConditions json
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
    """
    #:TODO: Remove office and window layout parameters from non-residential class
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
            office_layout=None,
            window_layout=None,
            construction_type=None,
            control_type=None
    ):
        """Constructor of School archetype
        """
        super(School, self).__init__(
            parent,
            name,
            year_of_construction,
            net_leased_area,
            with_ahu,
            internal_gains_mode,
        )

        self.construction_type = construction_type
        self.number_of_floors = number_of_floors
        self.height_of_floors = height_of_floors
        self.control_type = control_type

        # [area factor, usage type(has to be set)]
        self.zone_area_factors = collections.OrderedDict()
        self.zone_area_factors["Class rooms"] = [0.385, "Classroom"]
        self.zone_area_factors["Floor"] = [0.275, "Traffic area"]
        self.zone_area_factors["Storage"] = [0.16, "Stock, technical equipment, archives"]
        self.zone_area_factors["Office"] = [0.025, "Group Office (between 2 and 6 employees)"]
        self.zone_area_factors["Restroom"] = [0.03, "WC and sanitary rooms in non-residential buildings"]
        self.zone_area_factors["Further common rooms"] = [0.06, "Further common rooms"]
        self.zone_area_factors["Canteen"] = [0.035, "Canteen"]
        self.zone_area_factors["Lecture hall"] = [0.03, "Lecture hall, auditorium"]

        # [tilt, orientation]
        self.outer_wall_names = {
            "Exterior Facade North": [90, 0],
            "Exterior Facade East": [90, 90],
            "Exterior Facade South": [90, 180],
            "Exterior Facade West": [90, 270],
        }

        self.roof_names = {"Rooftop": [0, -1]}

        self.roof_window_names = {"Rooftop Windows": [0, -1]}

        self.ground_floor_names = {"Ground Floor": [0, -2]}

        self.window_names = {
            "Window Facade North": [90, 0],
            "Window Facade East": [90, 90],
            "Window Facade South": [90, 180],
            "Window Facade West": [90, 270],
        }

        self.inner_wall_names = {"InnerWall": [90, 0]}

        self.ceiling_names = {"Ceiling": [0, -1]}

        self.floor_names = {"Floor": [0, -2]}

        self.facade_estimation_factors = {
            (0, 1978): {
                "rt": 0.4001,
                "rt_win": 0.0045,
                "ow": 0.3194,
                "gf": 0.3959,
                "win": 0.2904

            },
            (1979, 2009): {
                "rt": 0.5215,
                "rt_win": 0.0067,
                "ow": 0.3380,
                "gf": 0.5202,
                "win": 0.3251
            },
            (2010, 2100): {
                "rt": 0.5281,
                "rt_win": 0.0102,
                "ow": 0.4084,
                "gf": 0.5591,
                "win": 0.2357
            }
        }

        self.building_age_group = None

        # default values for AHU
        if self.with_ahu is True:
            self.central_ahu.temperature_profile = (
                    7 * [293.15] + 12 * [295.15] + 5 * [293.15]
            )
            #  according to :cite:`DeutschesInstitutfurNormung.2016`
            self.central_ahu.min_relative_humidity_profile = 24 * [0.45]
            #  according to :cite:`DeutschesInstitutfurNormung.2016b`  and
            # :cite:`DeutschesInstitutfurNormung.2016`
            self.central_ahu.max_relative_humidity_profile = 24 * [0.65]
            self.central_ahu.v_flow_profile = (
                    7 * [0.0] + 12 * [1.0] + 5 * [0.0]
            )  # according to user
            # profile in :cite:`DeutschesInstitutfurNormung.2016`

    def _check_year_of_construction(self):
        """Assigns the bldg age group according to year of construction"""

        for key in self.facade_estimation_factors:
            if (
                    self.year_of_construction in range(key[0], key[1])
                    or self.year_of_construction == key[1]
            ):
                self.building_age_group = (key[0], key[1])

        if self.building_age_group is None:
            raise RuntimeError(
                "Year of construction not supported for this archetype" "building"
            )

    def generate_archetype(self):
        """Generates a School building.

        With given values, this class generates an school archetype building
        according to TEASER requirements.
        """
        # help area for the correct building area setting while using typeBldgs
        self.thermal_zones = None
        type_bldg_area = self.net_leased_area
        self._check_year_of_construction()
        self.net_leased_area = 0.0
        # create zones with their corresponding area, name and usage
        for key, value in self.zone_area_factors.items():
            zone = ThermalZone(self)
            zone.area = type_bldg_area * value[0]
            zone.name = key
            use_cond = UseCond(zone)
            use_cond.load_use_conditions(value[1], data_class=self.parent.data)
            use_cond.profiles_weekend_factor = 0
            use_cond.first_saturday_of_year = 1
            #use_cond.set_back_times = [7, 18]
            use_cond.calc_adj_schedules(control_type=self.control_type)
            zone.use_conditions = use_cond

        # statistical estimation of the facade

        if self.facade_estimation_factors[self.building_age_group]["ow"] != 0:
            for key, value in self.outer_wall_names.items():
                for zone in self.thermal_zones:
                    outer_wall = OuterWall(zone)
                    outer_wall.load_type_element(
                        year=self.year_of_construction,
                        construction=self.construction_type,
                        data_class=self.parent.data,
                    )
                    outer_wall.name = key
                    outer_wall.tilt = value[0]
                    outer_wall.orientation = value[1]
                    outer_wall.area = (
                                              self.facade_estimation_factors[self.building_age_group]["ow"]
                                              * zone.area
                                      ) / len(self.outer_wall_names)

        if self.facade_estimation_factors[self.building_age_group]["rt_win"] != 0:
            for key, value in self.roof_window_names.items():

                for zone in self.thermal_zones:
                    rt_window = Window(zone)
                    rt_window.load_type_element(
                        year=self.year_of_construction,
                        construction="Kunststofffenster, Isolierverglasung",
                        data_class=self.parent.data,
                    )
                    rt_window.name = key
                    rt_window.tilt = value[0]
                    rt_window.orientation = value[1]
                    rt_window.area = (
                                             self.facade_estimation_factors[self.building_age_group]["rt_win"]
                                             * zone.area
                                     ) / len(self.roof_window_names)

        if self.facade_estimation_factors[self.building_age_group]["win"] != 0:
            for key, value in self.window_names.items():
                for zone in self.thermal_zones:
                    window = Window(zone)
                    window.load_type_element(
                        self.year_of_construction,
                        construction="Kunststofffenster, Isolierverglasung",
                        data_class=self.parent.data,
                    )
                    window.name = key
                    window.tilt = value[0]
                    window.orientation = value[1]
                    window.area = (self.facade_estimation_factors[self.building_age_group]["win"] * zone.area) / \
                                  len(self.window_names)

        if self.facade_estimation_factors[self.building_age_group]["rt"] != 0:
            for key, value in self.roof_names.items():

                for zone in self.thermal_zones:
                    rt = Rooftop(zone)
                    rt.load_type_element(
                        year=self.year_of_construction,
                        construction=self.construction_type,
                        data_class=self.parent.data,
                    )
                    rt.name = key
                    rt.tilt = value[0]
                    rt.orientation = value[1]
                    rt.area = (
                                      self.facade_estimation_factors[self.building_age_group]["rt"]
                                      * zone.area
                              ) / len(self.roof_names)

        for key, value in self.inner_wall_names.items():

            for zone in self.thermal_zones:
                inner_wall = InnerWall(zone)
                inner_wall.load_type_element(
                    year=self.year_of_construction,
                    construction=self.construction_type,
                    data_class=self.parent.data,
                )
                inner_wall.name = key
                inner_wall.tilt = value[0]
                inner_wall.orientation = value[1]

        if self.number_of_floors > 1:

            for key, value in self.ceiling_names.items():

                for zone in self.thermal_zones:
                    ceiling = Ceiling(zone)
                    ceiling.load_type_element(
                        year=self.year_of_construction,
                        construction=self.construction_type,
                        data_class=self.parent.data,
                    )
                    ceiling.name = key
                    ceiling.tilt = value[0]
                    ceiling.orientation = value[1]

            for key, value in self.floor_names.items():

                for zone in self.thermal_zones:
                    floor = Floor(zone)
                    floor.load_type_element(
                        year=self.year_of_construction,
                        construction=self.construction_type,
                        data_class=self.parent.data,
                    )
                    floor.name = key
                    floor.tilt = value[0]
                    floor.orientation = value[1]

        for zone in self.thermal_zones:
            zone.set_inner_wall_area()
            zone.set_volume_zone()
        
        # needs to be revised: Add presence profile as sum of persons_profiles for all zones and clip to (0,1), set
        # temperature, min/max humidity and volume flow based on presence/absence of people in the building
        if self.central_ahu:
            setpoints = {"temperature":[293.15, 295.15],
                         "min_humidity":[15,30],
                         "max_humidity":[70,60]}

            presence_profile = self.thermal_zones[0].use_conditions.schedules.persons_profile
            for zone in self.thermal_zones:
                if zone.use_conditions.with_ahu: #
                    presence_profile += zone.use_conditions.schedules.persons_profile
            presence_profile = presence_profile.clip(0, 1).tolist()
            self.central_ahu.set_profiles_from_persons_profile(presence_profile,setpoints)

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
