# created June 2015
# by TEASER4 Development Team
import collections

from teaser.logic.buildingobjects.building import Building
from teaser.logic.buildingobjects.useconditions import UseConditions as UseCond
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.thermalzone import ThermalZone


class Residential(Building):
    """Base class for each residential archetype.

    This is the base class for all residential archetype buildings (BMVBS,
    UrbanReNet, Tabula, etc.). It is a subclass of Building and introduces
    several parameters to be obligatory (parent, name, year_of_construction,
    net_leased_area)

    Please use this class to create new archetype methodologies.

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
    Attributes
    ----------
    central_ahu : instance of BuildingAHU
        Teaser Instance of BuildingAHU if a central AHU is embedded into the
        building (currently mostly needed for AixLib simulation).
    number_of_floors : int
        number of floors above ground (default: None)
    height_of_floors : float [m]
        Average height of the floors (default: None)
    internal_id : float
        Random id for the distinction between different buildings.
    year_of_retrofit : int
        Year of last retrofit.
    type_of_building : string
        Type of a Building (e.g. Building (unspecified), Office etc.).
    building_id : None
        ID of building, can be set by the user to keep track of a building
        even outside of TEASER, e.g. in a simulation or in post-processing.
        This is not the same as internal_id, as internal_id is e.g. not
        exported to Modelica models!
    street_name : string
        Name of the street the building is located at. (optional)
    city : string
        Name of the city the building is located at. (optional)
    longitude : float [degree]
        Longitude of building location.
    latitude : float [degree]
        Latitude of building location.
    thermal_zones : list
        List with instances of ThermalZone(), that are located in this building.
    outer_area : dict [degree: m2]
        Dictionary with orientation as key and sum of outer wall areas of
        that direction as value.
    window_area : dict [degree: m2]
        Dictionary with orientation as key and sum of window areas of
        that direction as value.
    bldg_height : float [m]
        Total building height.
    volume : float [m3]
        Total volume of all thermal zones.
    sum_heat_load : float [W]
        Total heating load of all thermal zones.
    sum_cooling_load : float [W]
        Total heating load of all thermal zones. (currently not supported)
    number_of_elements_calc : int
        Number of elements that are used for thermal zone calculation in this
        building.
        1: OneElement
        2: TwoElement
        3: ThreeElement
        4: FourElement
    merge_windows_calc : boolean
        True for merging the windows into the outer wall's RC-combination,
        False for separate resistance for window, default is False
    used_library_calc : str
        'AixLib' for https://github.com/RWTH-EBC/AixLib
        'IBPSA' for https://github.com/ibpsa/modelica
    library_attr : Annex() or AixLib() instance
        Classes with specific functions and attributes for building models in
        IBPSA and AixLib. Python classes can be found in calculation package.

    """

    def __init__(
        self,
        parent,
        name,
        year_of_construction,
        net_leased_area,
        with_ahu=False,
        internal_gains_mode=1,
    ):
        """Constructor of Residential archetype building
        """

        super(Residential, self).__init__(
            parent,
            name,
            year_of_construction,
            net_leased_area,
            with_ahu,
            internal_gains_mode,
        )
        self.zone_area_factors = collections.OrderedDict()
        self.outer_wall_geo = {"Wall1": {"area": None, "orientation": None, "tilt": 90}}
        self.roof_geo = {"Roof": {"area": None, "orientation": -1, "tilt": 0}}
        self.ground_floor_geo = {
            "Ground Floor": {"area": None, "orientation": -2, "tilt": 0}
        }
        self.window_geo = {"Window1": {"area": None, "orientation": None, "tilt": 90}}

        self.inner_wall_names = {"InnerWall": [90, 0]}
        self.ceiling_names = {"Ceiling": [0, -1]}
        self.floor_names = {"Floor": [0, -2]}
        self.construction_type = "tabula_retrofit_1_MFH"

    def generate_archetype(self):
        """Generates an archetype building.

        If you want to define you own archetype methodology please use this
        function call to do so.

        """

        pass

    def generate_geo(self):
        """Generates an non residential building with given detailed geometry data.

        To run this function you need to specify the dictionsaries:
        self.outer_wall_geo = {"Wall1": {"area": None, "orientation": None, "tilt": 90}}
        self.roof_geo = {"Roof": {"area": None, "orientation": -1, "tilt": 0}}
        self.ground_floor_geo = {
            "Ground Floor": {"area": None, "orientation": -2, "tilt": 0}
        }
        self.window_geo = {"Window1": {"area": None, "orientation": None, "tilt": 90}}

        With given values, this class generates an non residential archetype building
        according to TEASER requirements.
        """
        # help area for the correct building area setting while using typeBldgs
        self.thermal_zones = None
        type_bldg_area = self.net_leased_area
        self.net_leased_area = 0.0
        # create zones with their corresponding area, name and usage
        for key, value in self.zone_area_factors.items():
            zone = ThermalZone(self)
            zone.area = type_bldg_area * value[0]
            zone.name = key
            use_cond = UseCond(zone)
            use_cond.load_use_conditions(value[1], data_class=self.parent.data)
            zone.use_conditions = use_cond

        for key, value in self.outer_wall_geo.items():
            if value["area"] == 0:
                pass
            else:
                self.outer_area[value["orientation"]] = value["area"]

                for zone in self.thermal_zones:
                    # create wall and set building elements
                    outer_wall = OuterWall(zone)
                    outer_wall.load_type_element(
                        year=self.year_of_construction,
                        construction=self.construction_type,
                        data_class=self.parent.data,
                    )
                    outer_wall.name = key
                    outer_wall.tilt = value["tilt"]
                    outer_wall.orientation = value["orientation"]

        for key, value in self.window_geo.items():
            if value["area"] == 0:
                pass
            else:
                self.window_area[value["orientation"]] = value["area"]

                """
                There is no real classification for windows, so this is a bit hard
                code - will be fixed sometime.
                """
                for zone in self.thermal_zones:
                    window = Window(zone)
                    window.load_type_element(
                        self.year_of_construction,
                        construction=self.construction_type,
                        data_class=self.parent.data,
                    )
                    window.name = key
                    window.tilt = value["tilt"]
                    window.orientation = value["orientation"]

        for key, value in self.roof_geo.items():
            if value["area"] == 0:
                pass
            else:
                self.outer_area[value["orientation"]] = value["area"]

                for zone in self.thermal_zones:
                    roof = Rooftop(zone)
                    roof.load_type_element(
                        year=self.year_of_construction,
                        construction=self.construction_type,
                        data_class=self.parent.data,
                    )
                    roof.name = key
                    roof.tilt = value["tilt"]
                    roof.orientation = value["orientation"]

        for key, value in self.ground_floor_geo.items():
            if value["area"] == 0:
                pass
            else:
                self.outer_area[value["orientation"]] = value["area"]

                for zone in self.thermal_zones:
                    ground_floor = GroundFloor(zone)
                    ground_floor.load_type_element(
                        year=self.year_of_construction,
                        construction=self.construction_type,
                        data_class=self.parent.data,
                    )
                    ground_floor.name = key
                    ground_floor.tilt = value["tilt"]
                    ground_floor.orientation = value["orientation"]

        for key, value in self.inner_wall_names.items():

            for zone in self.thermal_zones:
                inner_wall = InnerWall(zone)
                inner_wall.load_type_element(
                    year=self.year_of_construction,
                    construction="tabula_standard",
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
                        construction="tabula_standard",
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
                        construction="tabula_standard",
                        data_class=self.parent.data,
                    )
                    floor.name = key
                    floor.tilt = value[0]
                    floor.orientation = value[1]
        else:
            pass

        for key, value in self.outer_area.items():
            self.set_outer_wall_area(value, key)
        for key, value in self.window_area.items():
            self.set_window_area(value, key)

        for zone in self.thermal_zones:
            zone.set_inner_wall_area()
            zone.set_volume_zone()
