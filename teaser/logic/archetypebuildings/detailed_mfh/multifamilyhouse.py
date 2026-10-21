"""Detailed multi family house archetype"""

import warnings

import numpy as np

import teaser.data.utilities as datahandling
from teaser.logic.archetypebuildings.residential import Residential
from teaser.logic.archetypebuildings.detailed_mfh.geometry import (
    Plan, building_geometry, flat_area, scale_plan)
from teaser.logic.buildingobjects.building import rotate_orientation
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.useconditions import UseConditions

_ELEMENT_CLASSES = {cls.__name__: cls for cls in (
    OuterWall, Rooftop, GroundFloor, InnerWall, Floor, Ceiling, Window)}

# Volumetric heat capacity of air DIN EN 12831-1 uses, in Wh/(m3K)
_RHO_C_AIR = 0.34

# Outer surface coefficients of the stand-ins that integrate an unheated
# space into a heated zone [W/(m2K)]: convection only, so a stand-in sees
# exactly the outside air temperature, as the temperature factor assumes
_STAND_IN_OUTER_CONVECTION = 20.0
_STAND_IN_OUTER_RADIATION = 1e-9
# Smallest extra resistance of a stand-in [m2K/W], i.e. of its layer
_MIN_EXTRA_RESISTANCE = 1e-6

# Construction of the slab on the ground without a basement: the basement
# ceiling's (FloorCellar), as the construction data has a ground floor only
# for the unheated basement (uninsulated concrete)
_SLAB_ON_GROUND = "FloorCellar"

# The five groups of interior surfaces of the single-zone ROM, in the order
# BESMod's TEASERBuildingSingleZone.FourElements lists them in AArraySol:
# {ATotExt, ATotWin, AInt, AFloor, ARoof}. splitFactorSolRad has one row per
# group.
_ROM_SURFACE_GROUPS = ("OuterWall", "Window", "InnerWall", "GroundFloor",
                       "Roof")


def _zone_per_building(info):
    return "Building"


def _zone_per_flat(info):
    return f"F{info.storey}_A{info.flat}"


# The ROM zoning options, by name, each a function from a heated room's
# ZoneInfo to the name of its thermal zone
ZONINGS = {
    "building": _zone_per_building,
    "flat": _zone_per_flat,
}


class DetailedMultiFamilyHouse(Residential):
    """Detailed multi family house, room by room

    The archetype builds a multi family house from Kühn/Nikolowski's floor
    plan of two flats around a staircase (see detailed_mfh.geometry):
    number_of_floors storeys of 2 * number_of_staircases flats each, over an
    unheated basement and below an unheated attic. Every flat has the same
    six rooms, scaled to net_leased_area_per_flat. The construction data of
    the colleague's three archetypes (detailed_mfh_standard) gives the
    building elements for 1949-1978, 1979-1994 and 2021 on.

    TEASER's thermal zones (the ROM) merge the heated rooms by zoning, one
    zone for the whole building or one per flat, with the elements derived
    from the rooms' three-dimensional geometry: the outer walls and windows
    with their orientations, the walls and slabs between heated rooms as
    halves on either side and, where a heated room adjoins an unheated
    space, a stand-in to the outside air (a Rooftop), or for the basement
    to the ground (a GroundFloor). Its U-value is the element's, times the
    temperature factor b = (t_room - t_u) / (t_room - t_outside), with
    t_ground instead of t_outside for the basement,
    of the unheated space's steady-state heat balance at the design
    temperatures - with the heated rooms, the outside air (envelope and air
    change), the ground and the other unheated spaces. The geometry itself
    is kept as geometry, from which export_idf writes an EnergyPlus model
    with every room as a zone and each staircase as one zone over all
    storeys.

    The archetype is rebuilt by generate_archetype(), which has to be called
    after changing any of the settings below.

    Parameters
    ----------
    parent : Project
    name : str
    year_of_construction : int
    number_of_floors : int
        Heated storeys. (default: 5)
    height_of_floors : float [m]
        Clear height of the rooms. (default: 2.5)
    net_leased_area_per_flat : float [m2]
        Net floor area of each flat, to which the rooms are scaled. None
        keeps the plan as drawn (64.9 m2), or takes net_leased_area divided
        by the number of flats if that is given.
    number_of_staircases : int
        Staircases side by side, each with two flats per storey.
        (default: 1)
    construction_data : str or ConstructionData
        detailed_mfh_standard (default)
    neighbour_buildings : int or tuple
        Buildings adjoining the gable walls, which are then adiabatic: 0
        (default), 1 (on the west side), 2, or a tuple of "west" and/or
        "east".
    net_leased_area : float [m2]
        Total net leased area, an alternative to net_leased_area_per_flat.
    with_basement : bool
        True (default) for an unheated basement below the ground floor,
        False for the ground floor's rooms and the staircases on a slab on
        the ground (GroundFloor elements).

    Attributes
    ----------
    zoning : str or callable
        "building" (default) or "flat", see ZONINGS, or a function from a
        heated room's ZoneInfo to the name of its zone.
    scaling : str
        How the rooms are scaled to net_leased_area_per_flat, "length"
        (default, along the building's length only) or "proportional".
    plan : Plan
        The floor plan's unscaled dimensions, incl. the wall and slab
        thicknesses and the basement's height.
    roof_tilt : float [deg]
        Tilt of the gable roof. (default: 30)
    room_t_set_nominal : dict [K]
        Design temperature per room type, 20 degC and 24 degC for the bath.
    unheated_air_change_rates : dict [1/h]
        Air change of the unheated spaces with the outside air, by kind:
        staircase 0.5, basement 0.5 and attic 2.5 (DIN EN 12831-1 Table 5,
        "undicht").
    rotation : float [deg]
        Rotation of the whole building clockwise, 0 with the living rooms
        facing south. Set it with rotate_building.
    geometry : Geometry
        The building's zones, built by generate_archetype.
    temperature_factors : dict
        b of each heated room towards each unheated space it adjoins,
        towards t_ground for the basement and t_outside for the others.
    room_of_element : dict
        The heated room of each element and window of the thermal zones,
        by name.
    """

    def __init__(
            self,
            parent=None,
            name=None,
            year_of_construction=None,
            number_of_floors=5,
            height_of_floors=2.5,
            net_leased_area_per_flat=None,
            number_of_staircases=1,
            construction_data=None,
            neighbour_buildings=0,
            net_leased_area=None,
            with_basement=True,
    ):
        flats = 2 * number_of_staircases * number_of_floors
        if net_leased_area_per_flat is None and net_leased_area is not None:
            net_leased_area_per_flat = net_leased_area / flats
        self.plan = Plan(room_height=height_of_floors)
        super().__init__(
            parent, name, year_of_construction,
            flats * (net_leased_area_per_flat or flat_area(self.plan)))
        self.construction_data = construction_data
        self._number_of_floors = number_of_floors
        self.height_of_floors = height_of_floors
        self.net_leased_area_per_flat = net_leased_area_per_flat
        self.number_of_staircases = number_of_staircases
        self.neighbour_buildings = neighbour_buildings
        self.with_basement = with_basement
        self.zoning = "building"
        self.scaling = "length"
        self.roof_tilt = 30.0
        self.room_t_set_nominal = {room_type: 293.15 for room_type in (
            "Living", "Bedroom", "Children", "Hallway", "Bath", "Kitchen")}
        self.room_t_set_nominal["Bath"] = 297.15
        self.unheated_air_change_rates = {
            "staircase": 0.5, "basement": 0.5, "attic": 2.5}
        self.rotation = 0.0
        self.geometry = None
        self.zone_of_room = {}
        self.room_volumes = {}
        self.temperature_factors = {}
        self.unheated_room_envelope_elements = {}
        self.interface_elements = {}
        self.surface_constructions = {}
        self.room_of_element = {}

    @property
    def construction_data(self):
        return self._construction_data

    @construction_data.setter
    def construction_data(self, value):
        self._construction_data = \
            datahandling.check_construction_data_setter_detailed_mfh(value)

    @property
    def number_of_floors(self):
        return self._number_of_floors

    @number_of_floors.setter
    def number_of_floors(self, value):
        self._number_of_floors = value

    @property
    def exports_single_zone_rom(self):
        """A single zone is exported against BESMod's
        TEASERThermalSingleZone, with the interior heat transfer parameters
        of calc_rom_inner_heat_transfer_parameters"""
        return self.thermal_zones is not None and len(self.thermal_zones) == 1

    @property
    def number_of_flats(self):
        return 2 * self.number_of_staircases * self.number_of_floors

    def _zone_name(self, info):
        zoning = ZONINGS.get(self.zoning, self.zoning) \
            if isinstance(self.zoning, str) else self.zoning
        if not callable(zoning):
            raise ValueError(f"Unknown zoning {self.zoning!r}, use one of "
                             f"{sorted(ZONINGS)} or a function.")
        return zoning(info)

    def _load(self, cls_name, construction_type=None, element_type=None,
              parent=None):
        """An element of the construction data, with its layers"""
        element = _ELEMENT_CLASSES[cls_name](parent=parent)
        element.element_construction_type = construction_type
        key = element.load_type_element(
            year=self.year_of_construction,
            construction=self.construction_data.value,
            data_class=self.data_class,
            element_type=element_type,
        )
        wanted = element_type or cls_name + (construction_type or "")
        # TEASER takes the first key that merely starts with the type, or
        # falls back to the element's class
        if key is None or key.split("_[")[0] != wanted:
            raise ValueError(
                f"{self.construction_data.value} has no {wanted} for "
                f"{self.year_of_construction}.")
        return element

    def generate_archetype(self):
        """Builds the geometry and the thermal zones from it"""
        plan = self.plan
        if plan.room_height != self.height_of_floors:
            plan = Plan(**{**plan.__dict__,
                           "room_height": self.height_of_floors})
            self.plan = plan
        if self.net_leased_area_per_flat is not None:
            plan = scale_plan(plan, self.net_leased_area_per_flat,
                              self.scaling)
        self.geometry = building_geometry(
            plan, self.number_of_floors, self.number_of_staircases,
            self.roof_tilt, self.neighbour_buildings, self.with_basement)
        geometry = self.geometry
        info = geometry.info

        self.thermal_zones = None
        # ThermalZone.area's setter adds each zone's area to the building's
        self.net_leased_area = 0.0
        self.unheated_room_envelope_elements = {}
        self.interface_elements = {}
        self.surface_constructions = {}
        self.room_of_element = {}
        self.room_volumes = {name: float(zone.volume)
                             for name, zone in geometry.zones.items()}
        self.zone_of_room = {room: self._zone_name(info[room])
                             for room in geometry.heated_rooms}

        zones = {}
        for room in geometry.heated_rooms:
            zone_name = self.zone_of_room[room]
            if zone_name not in zones:
                zones[zone_name] = []
            zones[zone_name].append(room)
        for zone_name, rooms in zones.items():
            zone = ThermalZone(parent=self)
            zone.name = zone_name
            zone.area = sum(geometry.zones[r].floor_area for r in rooms)
            zone.volume = float(sum(self.room_volumes[r] for r in rooms))
            zone.number_of_floors = len({info[r].storey for r in rooms})
            zone.height_of_floors = self.height_of_floors
            use_conditions = UseConditions(parent=zone)
            use_conditions.load_use_conditions(zone_usage="Living")
            zone.use_conditions = use_conditions
            zone.use_conditions.with_ahu = False
            zone.t_inside = sum(
                self.room_t_set_nominal[info[r].room_type] * self.room_volumes[r]
                for r in rooms) / zone.volume

        zone_by_name = {zone.name: zone for zone in self.thermal_zones}
        interfaces = []  # (room, unheated space, cls, construction type, area)
        for room in geometry.heated_rooms:
            zone = zone_by_name[self.zone_of_room[room]]
            elements = {}
            windows = {}
            for surface in geometry.zones[room].surfaces:
                spec, part = self._room_surface(room, surface)
                self.surface_constructions[surface.name] = spec
                if part == "unheated":
                    interfaces.append((room, surface.element[1], spec,
                                       surface.area))
                    continue
                # elements and windows are named after the orientation of
                # the unrotated geometry, which rotate_building keeps
                orientation, tilt = surface.orientation, surface.tilt
                key = (spec, part, orientation if spec[0] == "OuterWall"
                       else None)
                elements[key] = elements.get(key, (0.0, tilt))
                elements[key] = (elements[key][0] + surface.net_area, tilt)
                for window in surface.windows:
                    windows[orientation] = windows.get(orientation, 0.0) \
                        + window.area
            for ((cls_name, construction_type, element_type), part,
                 orientation), (area, tilt) in elements.items():
                element = self._load(cls_name, construction_type, element_type,
                                     parent=zone)
                element.name = "_".join(str(p) for p in (
                    room, element_type or cls_name + (construction_type or ""),
                    part) + ((int(round(orientation)),)
                             if orientation is not None else ()))
                element.area = area
                element.tilt = tilt
                self.room_of_element[element.name] = room
                element.orientation = 0.0 if orientation is None                     else self._rotated(orientation)
                if cls_name == "GroundFloor":
                    element.orientation, element.tilt = -2.0, 0.0
                if part == "half":
                    _halve(element)
            for orientation, area in windows.items():
                window = self._load("Window", parent=zone)
                window.name = f"{room}_Window_{int(round(orientation))}"
                window.area = area
                window.tilt = 90.0
                window.orientation = self._rotated(orientation)
                self.room_of_element[window.name] = room

        self._unheated_envelopes()
        self._integrate_unheated_spaces(interfaces, zone_by_name)

    def _rotated(self, orientation):
        """TEASER's orientation of a surface of the geometry, rotated"""
        if orientation >= 0:
            orientation = rotate_orientation(orientation, self.rotation)
        return orientation

    def _room_surface(self, room, surface):
        """The construction of a heated room's surface

        Returns ((class name, element construction type, element type), part)
        with part "full" for an element of the room alone, "half" for one
        it shares with another heated room, each getting its half, and
        "unheated" for one towards an unheated space.
        """
        info = self.geometry.info
        _, other = surface.element
        if surface.boundary == "Outdoors":
            return ("OuterWall", None, None), "full"
        if surface.boundary == "Ground":
            return ("GroundFloor", None, _SLAB_ON_GROUND), "full"
        if other == "neighbour":
            # the gable wall to the next building, heated as well
            return ("InnerWall", None, "OuterWall"), "full"
        if other == "gap":
            return {"Wall": ("InnerWall", None, None),
                    "Floor": ("Floor", None, None),
                    "Ceiling": ("Ceiling", None, None)}[surface.kind], "half"
        partner = info[other]
        if partner.heated:
            if surface.kind == "Wall":
                same_flat = (partner.flat == info[room].flat
                             and partner.storey == info[room].storey)
                return ("InnerWall", None if same_flat else "Apartment",
                        None), "half"
            return (surface.kind, None, None), "half"
        if surface.kind == "Wall":
            return ("InnerWall", "Apartment", None), "unheated"
        if surface.kind == "Floor":
            return ("Floor", "Cellar", None), "unheated"
        return ("Ceiling", "Attic", None), "unheated"

    def _unheated_surface(self, space, surface):
        """The construction of an unheated space's surface, from inside

        Returns (class name, element construction type, element type,
        reversed), reversed for a construction that the space shares with
        another zone and that is defined from that zone's side.
        """
        info = self.geometry.info
        kind = info[space].kind
        _, other = surface.element
        if surface.boundary in ("Outdoors", "Ground") or other == "neighbour":
            if kind == "basement":
                if surface.kind == "Floor":
                    return "GroundFloor", None, None, False
                return "OuterWall", "Cellar", None, False
            if surface.boundary == "Ground":
                # the floor of a staircase without a basement
                return "GroundFloor", None, _SLAB_ON_GROUND, False
            if surface.kind == "Roof":
                return "Rooftop", None, None, False
            return "OuterWall", None, None, False
        if other == "gap":
            if kind == "basement":
                return "Floor", "Cellar", None, True
            if kind == "attic":
                return "Ceiling", "Attic", None, True
            return "InnerWall", "Apartment", None, False
        partner = info[other]
        if partner.kind == "room":
            spec, _ = self._room_surface(other, _mirror(surface))
            return (*spec, True)
        # between two unheated spaces: the staircase's floor and top
        if kind == "staircase":
            if surface.kind == "Floor":
                return "Floor", "Cellar", None, False
            return "Ceiling", "Attic", None, False
        if kind == "basement":
            return "Floor", "Cellar", None, True
        return "Ceiling", "Attic", None, True

    def _unheated_envelopes(self):
        """The unheated spaces' own elements towards the outside and ground

        They belong to no thermal zone, but enter the temperature factors
        and the EnergyPlus model, and are retrofitted with the building.
        """
        for space, info in self.geometry.info.items():
            if info.heated:
                continue
            elements = {}
            for surface in self.geometry.zones[space].surfaces:
                cls_name, construction_type, element_type, reverse = \
                    self._unheated_surface(space, surface)
                self.surface_constructions[surface.name] = (
                    cls_name, construction_type, element_type) + (
                    ("reversed",) if reverse else ())
                if surface.boundary not in ("Outdoors", "Ground"):
                    continue
                key = (cls_name, construction_type, surface.boundary)
                if key not in elements:
                    element = self._load(cls_name, construction_type,
                                         element_type)
                    element.name = f"{space}_{cls_name}{construction_type or ''}"
                    element.area = 0.0
                    element._boundary = surface.boundary
                    elements[key] = element
                elements[key].area += surface.net_area
                if surface.windows:
                    if ("Window",) not in elements:
                        window = self._load("Window")
                        window.name = f"{space}_Window"
                        window.area = 0.0
                        window._boundary = "Outdoors"
                        elements[("Window",)] = window
                    elements[("Window",)].area += sum(
                        w.area for w in surface.windows)
            self.unheated_room_envelope_elements[space] = {
                element.name: element for element in elements.values()}

    def _integrate_unheated_spaces(self, interfaces, zone_by_name):
        """Temperature factors of the unheated spaces and the stand-ins"""
        geometry = self.geometry
        info = geometry.info
        zone = self.thermal_zones[0]
        t_outside, t_ground = float(zone.t_outside), float(zone.t_ground)
        spaces = [name for name, i in info.items() if not i.heated]
        index = {space: i for i, space in enumerate(spaces)}
        matrix = np.zeros((len(spaces), len(spaces)))
        rhs = np.zeros(len(spaces))

        def couple(space, h, temperature=None, other=None):
            i = index[space]
            matrix[i, i] += h
            if other is None:
                rhs[i] += h * temperature
            else:
                matrix[i, index[other]] -= h

        for space in spaces:
            for element in self.unheated_room_envelope_elements[space].values():
                h = _u_value(element, element._boundary) * element.area
                couple(space, h, t_ground if element._boundary == "Ground"
                       else t_outside)
            couple(space, _RHO_C_AIR * self.unheated_air_change_rates[
                info[space].kind] * self.room_volumes[space], t_outside)
            # towards the other unheated spaces, from the lower one only
            for surface in geometry.zones[space].surfaces:
                other = surface.element[1]
                if surface.boundary != "Surface" or info[other].heated \
                        or surface.kind != "Ceiling":
                    continue
                cls_name, construction_type, element_type, _ = \
                    self._unheated_surface(space, surface)
                h = _u_value(self._load(cls_name, construction_type,
                                        element_type), "Inside") * surface.area
                couple(space, h, other=other)
                couple(other, h, other=space)

        merged = {}
        for room, space, spec, area in interfaces:
            key = (room, space, spec)
            merged[key] = merged.get(key, 0.0) + area
        for (room, space, spec), area in merged.items():
            element = self._load(*spec)
            element.name = f"{room}_{space}_{spec[0]}{spec[1] or ''}"
            element.area = area
            self.interface_elements[(room, space, spec)] = element
            h = _u_value(element, "Inside") * area
            couple(space, h, self.room_t_set_nominal[info[room].room_type])

        temperatures = np.linalg.solve(matrix, rhs)
        self.unheated_temperatures = {
            space: float(temperatures[index[space]]) for space in spaces}
        self.temperature_factors = {}
        for (room, space, spec), element in self.interface_elements.items():
            t_room = self.room_t_set_nominal[info[room].room_type]
            # the basement follows the ground more than the outside air, so
            # its stand-ins are ground floors towards t_ground
            ground = info[space].kind == "basement"
            t_boundary = t_ground if ground else t_outside
            if t_room <= t_boundary:
                raise ValueError(
                    f"The design temperature of {room} must be above the "
                    f"{'ground' if ground else 'outside'} temperature.")
            factor = (t_room - self.unheated_temperatures[space]) / (
                t_room - t_boundary)
            self.temperature_factors[(room, space)] = factor
            _stand_in(element, factor,
                      zone_by_name[self.zone_of_room[room]], ground=ground)
            self.room_of_element[element.name] = room

    def calc_building_parameter(self, number_of_elements=None,
                                merge_windows=None, used_library=None):
        """Calculates the zones' parameters, see
        Building.calc_building_parameter, which adds to sum_heat_load
        rather than recalculating it"""
        self.sum_heat_load = 0
        super().calc_building_parameter(
            number_of_elements=number_of_elements,
            merge_windows=merge_windows, used_library=used_library)
        self.room_heat_loads = self.calc_room_heat_loads()
        self.sum_heat_load = 0
        for zone in self.thermal_zones:
            zone_heat_load = sum(self.room_heat_loads[room]
                                 for room, name in self.zone_of_room.items()
                                 if name == zone.name)
            zone.model_attr.heat_load = zone_heat_load
            zone.model_attr.cool_load = -zone_heat_load
            self.sum_heat_load += zone_heat_load
        # the heated zones touch neither the ground nor the roof, only
        # stand-ins of the basement and attic, so BESMod's ground and roof
        # area (e.g. for photovoltaics) are the building's own
        self.area_gf = self.geometry.length * self.geometry.depth
        self.area_rt = sum(surface.area
                           for surface in self.geometry.zones["Attic"].surfaces
                           if surface.kind == "Roof")
        if self.exports_single_zone_rom:
            self.calc_rom_inner_heat_transfer_parameters()

    def _areas_by_room(self, elements):
        """{room: total area [m2]} of elements, by heated room"""
        areas = {room: 0.0 for room in self.geometry.heated_rooms}
        for element in elements:
            areas[self.room_of_element[element.name]] += element.area
        return areas

    def calc_rom_inner_heat_transfer_parameters(self):
        """Parameterizes the single-zone ROM's interior heat transfer from
        the rooms

        AixLib's reduced order model couples each pair of its surface
        groups by long wave radiation with min(A_i, A_j) * hRad. A small
        group such as the windows or the stand-ins (the roof group of the
        staircases and the attic, the ground floor group of the basement)
        is so coupled with its full area to each of the other groups, several
        times as much as a surface radiates. BESMod's single-zone model
        (Systems.Demand.Building.TEASERThermalSingleZone) scales the areas
        of these couplings by ratios, which are set here so that each
        window and stand-in exchanges radiation with the surfaces of its
        own room in the ratio of their areas, and with hRad times its own
        area in total, as in the room-wise EnergyPlus model.

        - ratioWinArea*: the share of the other surfaces of the windows'
          rooms that each group has, weighted by the window areas,
        - ratio*AreaTopFloor and ratio*AreaBottomFloor: the same for the
          roof group (the stand-ins) and the ground floor, as the coupled
          area over the group's area,
        - splitFactorSolRad: the solar radiation entering through the
          windows of each orientation reaches the surfaces of the rooms it
          enters, in the ratio of their areas, except the windows it came
          through, the walls they sit in and the ceilings (incl. the
          stand-ins of the attic).

        The coupling of the outer walls with the inner walls,
        min(ATotExt, AInt) * hRad, has no ratio and stays as it is.
        """
        if len(self.thermal_zones) != 1:
            raise AttributeError(
                "The single-zone ROM parameters are only defined for a "
                "single thermal zone (zoning 'building').")
        zone = self.thermal_zones[0]
        rooms = self.geometry.heated_rooms
        elements = {
            "OuterWall": zone.outer_walls,
            "Window": zone.windows,
            "InnerWall": zone.inner_walls + zone.floors + zone.ceilings,
            "GroundFloor": zone.ground_floors,
            "Roof": zone.rooftops,
        }
        areas = {group: self._areas_by_room(group_elements)
                 for group, group_elements in elements.items()}
        totals = {group: sum(areas[group].values()) for group in areas}

        def seen(source):
            """{group: share of the other surfaces in the rooms of the
            source group's surfaces}, weighted by the source's areas"""
            shares = {group: 0.0 for group in areas}
            for room in rooms:
                area = areas[source][room]
                others = sum(areas[group][room] for group in areas) - area
                if not area or not others:
                    continue
                for group in areas:
                    if group != source:
                        shares[group] += (area / totals[source]
                                          * areas[group][room] / others)
            return shares

        def coupled(source, group):
            """The area of group the source group is coupled with, over
            group's area"""
            if not totals[group]:
                return 0.0
            return totals[source] * seen(source)[group] / totals[group]

        window = seen("Window")
        zone.ratio_win_area_ow = window["OuterWall"]
        zone.ratio_win_area_iw = window["InnerWall"]
        zone.ratio_win_area_top_floor = window["Roof"]
        zone.ratio_win_area_bottom_floor = window["GroundFloor"]
        zone.ratio_ow_area_top_floor = coupled("Roof", "OuterWall")
        zone.ratio_iw_area_top_floor = coupled("Roof", "InnerWall")
        zone.ratio_ow_area_bottom_floor = coupled("GroundFloor", "OuterWall")
        zone.ratio_iw_area_bottom_floor = coupled("GroundFloor", "InnerWall")
        # every stand-in faces the zone with its whole area
        zone.roof_area_attic_factor = 1.0
        self.calc_split_factor_sol_rad(zone, elements, areas)

    def calc_split_factor_sol_rad(self, zone, elements, areas):
        """Derives splitFactorSolRad room-wise, see
        calc_rom_inner_heat_transfer_parameters

        An orientation without any window keeps the whole-zone area split.
        """
        ceiling_stand_ins = {
            element.name for (_, _, spec), element
            in self.interface_elements.items() if spec[0] == "Ceiling"}
        solar = {**areas,
                 "InnerWall": self._areas_by_room(
                     zone.inner_walls + zone.floors),
                 "Roof": self._areas_by_room(
                     [element for element in zone.rooftops
                      if element.name not in ceiling_stand_ins])}
        groups = list(zip(zone.model_attr.orientation_facade,
                          zone.model_attr.tilt_facade))
        rooms = self.geometry.heated_rooms

        def by_room_and_group(group_elements):
            result = {(room, group): 0.0 for room in rooms for group in groups}
            for element in group_elements:
                key = (self.room_of_element[element.name],
                       (element.orientation, element.tilt))
                if key in result:
                    result[key] += element.area
            return result

        windows = by_room_and_group(elements["Window"])
        host_walls = by_room_and_group(elements["OuterWall"])
        zone_totals = {name: sum(areas[name].values())
                       for name in _ROM_SURFACE_GROUPS}
        split_factors = [[] for _ in _ROM_SURFACE_GROUPS]
        for group in groups:
            total_window = sum(windows[(room, group)] for room in rooms)
            if not total_window:
                total = sum(zone_totals.values())
                for index, name in enumerate(_ROM_SURFACE_GROUPS):
                    split_factors[index].append(
                        zone_totals[name] / total if total else 0.0)
                continue
            factors = [0.0] * len(_ROM_SURFACE_GROUPS)
            for room in rooms:
                window, host = windows[(room, group)], host_walls[(room, group)]
                if not window:
                    continue
                reached = {name: solar[name][room]
                           for name in _ROM_SURFACE_GROUPS}
                reached["OuterWall"] -= host
                reached["Window"] -= window
                reachable = sum(reached.values())
                if reachable <= 0:
                    continue
                for index, name in enumerate(_ROM_SURFACE_GROUPS):
                    factors[index] += (reached[name] / reachable
                                       * window / total_window)
            for index, factor in enumerate(factors):
                split_factors[index].append(factor)
        # as AixLib's splitFacVal, the rows of the groups with an area come
        # first and the rest are zero, e.g. for the missing ground floor;
        # BESMod's model takes one row per group with an area
        present = [index for index, name in enumerate(_ROM_SURFACE_GROUPS)
                   if zone_totals[name] > 0]
        zone.split_factor_sol_rad = (
            [split_factors[index] for index in present]
            + [[0.0] * len(groups)
               for _ in range(len(_ROM_SURFACE_GROUPS) - len(present))])

    def calc_room_heat_loads(self):
        """Static heat load of each heated room [W]

        TEASER's zone heat load (TwoElement._calc_heat_load) per room, at
        the room's own design temperature: the UA-value of its outer walls,
        windows and stand-ins towards the unheated spaces times the
        difference to t_outside (t_ground for the basement's), plus the normative infiltration of its
        volume, plus what it gives to heated neighbours designed for a
        lower temperature (e.g. the bath at 24 degC to its neighbours),
        through the whole wall or slab between them. calc_building_parameter
        takes their sum as each zone's heat load, which the exchange
        between rooms of the same zone leaves unchanged.
        """
        info = self.geometry.info
        u_values = {}
        loads = {}
        for zone in self.thermal_zones:
            use_conditions = zone.use_conditions
            to_outside = {}
            for element in zone.outer_walls + zone.rooftops + zone.windows:
                room = self.room_of_element[element.name]
                to_outside[room] = to_outside.get(room, 0.0) + element.ua_value
            to_ground = {}
            for element in zone.ground_floors:
                room = self.room_of_element[element.name]
                to_ground[room] = to_ground.get(room, 0.0) + element.ua_value
            for room, name in self.zone_of_room.items():
                if name != zone.name:
                    continue
                t_room = self.room_t_set_nominal[info[room].room_type]
                load = (to_outside.get(room, 0.0)
                        + self.room_volumes[room]
                        * use_conditions.normative_infiltration / 3600
                        * zone.heat_capac_air * zone.density_air
                        ) * (t_room - zone.t_outside)                     + to_ground.get(room, 0.0) * (t_room - zone.t_ground)
                for surface in self.geometry.zones[room].surfaces:
                    other = surface.element[1]
                    if surface.boundary != "Surface" or not info[other].heated:
                        continue
                    t_other = self.room_t_set_nominal[info[other].room_type]
                    if t_other == t_room:
                        continue
                    spec = self.surface_constructions[surface.name]
                    if spec not in u_values:
                        u_values[spec] = _u_value(self._load(*spec), "Inside")
                    load += u_values[spec] * surface.area * (t_room - t_other)
                loads[room] = load
        return loads

    @property
    def room_heat_loads_list(self):
        """room_heat_loads in the order of geometry.heated_rooms"""
        return [self.room_heat_loads[room]
                for room in self.geometry.heated_rooms]

    @property
    def room_t_set_nominal_list(self):
        """The heated rooms' design temperatures [K], in the order of
        geometry.heated_rooms"""
        return [self.room_t_set_nominal[self.geometry.info[room].room_type]
                for room in self.geometry.heated_rooms]

    def rotate_building(self, angle):
        """Rotates the building clockwise by angle [deg]"""
        self.rotation = (self.rotation + angle) % 360
        super().rotate_building(angle)


def _mirror(surface):
    """The kind a surface has seen from its partner's side"""
    from dataclasses import replace
    kind = {"Floor": "Ceiling", "Ceiling": "Floor"}.get(surface.kind,
                                                         surface.kind)
    return replace(surface, kind=kind,
                   element=(surface.element[1], surface.element[0]),
                   boundary="Surface")


def _resistance_layers(element):
    return sum(layer.thickness / layer.material.thermal_conduc
               for layer in element.layer)


def _u_value(element, boundary):
    """U-value [W/(m2K)] of an element, with its surface resistances

    boundary is what its other side faces: "Outdoors", "Ground" (no
    surface resistance) or "Inside" (the inner one again).
    """
    r_inner = 1 / (element.inner_convection + element.inner_radiation)
    if boundary == "Outdoors":
        r_outer = 1 / (element.outer_convection + element.outer_radiation)
    elif boundary == "Ground":
        r_outer = 0.0
    else:
        r_outer = r_inner
    return 1 / (r_inner + _resistance_layers(element) + r_outer)


def _new_layer(element, template, thickness):
    """A layer of element with template's material and thickness"""
    layer = Layer(parent=element)
    material = Material(parent=layer)
    source = template.material
    material.name = source.name
    material.material_id = source.material_id
    material.density = source.density
    material.thermal_conduc = source.thermal_conduc
    material.heat_capac = source.heat_capac
    material.solar_absorp = source.solar_absorp
    material.ir_emissivity = source.ir_emissivity
    layer.thickness = thickness
    return layer


def _halve(element):
    """Keeps the half of the element's layers on its own side"""
    layers = list(element.layer)
    half = sum(layer.thickness for layer in layers) / 2
    kept = []
    depth = 0.0
    for layer in layers:
        if depth + layer.thickness <= half + 1e-12:
            kept.append((layer, layer.thickness))
        elif depth < half:
            kept.append((layer, half - depth))
        depth += layer.thickness
    element.layer = None
    for layer, thickness in kept:
        _new_layer(element, layer, thickness)


def _stand_in(element, factor, zone, ground=False):
    """A stand-in in zone that loses through element as much heat as
    element does to its unheated space at the temperature factor b: the
    element's layers, plus a resistance so its U-value is b times the
    element's. It absorbs no sunlight.

    A Rooftop towards the outside air, horizontal, or with ground a
    GroundFloor towards the ground temperature, without an outer surface
    resistance as TEASER's ground floors.
    """
    factor = max(factor, 1e-3)
    if ground:
        stand_in = GroundFloor(parent=zone)
        stand_in.orientation = -2
        r_outer = 0.0
    else:
        stand_in = Rooftop(parent=zone)
        stand_in.orientation = -1
        stand_in.outer_convection = _STAND_IN_OUTER_CONVECTION
        stand_in.outer_radiation = _STAND_IN_OUTER_RADIATION
        r_outer = 1 / (stand_in.outer_convection + stand_in.outer_radiation)
    stand_in.name = element.name
    stand_in.area = element.area
    stand_in.tilt = 0.0
    stand_in.inner_convection = element.inner_convection
    stand_in.inner_radiation = element.inner_radiation
    for layer in element.layer:
        _new_layer(stand_in, layer, layer.thickness)
    extra = Layer(parent=stand_in)
    material = Material(parent=extra)
    material.name = "temperature_factor_resistance"
    material.density = 1.0
    material.heat_capac = 1.0
    material.thermal_conduc = 1.0
    material.solar_absorp = 0.0
    r_extra = (1 / (factor * _u_value(element, "Inside"))
               - 1 / (stand_in.inner_convection + stand_in.inner_radiation)
               - _resistance_layers(element)
               - r_outer)
    if r_extra < _MIN_EXTRA_RESISTANCE:
        # b above what the element's own layers allow, e.g. a basement
        # colder than the ground below a ceiling of a low resistance
        r_extra = _MIN_EXTRA_RESISTANCE
        u_value = 1 / (1 / (stand_in.inner_convection
                            + stand_in.inner_radiation)
                       + _resistance_layers(element) + r_outer + r_extra)
        warnings.warn(
            f"The stand-in {element.name} reaches only a U-value of "
            f"{u_value:.3f} instead of "
            f"{factor * _u_value(element, 'Inside'):.3f} W/(m2K).")
    extra.thickness = r_extra
    return stand_in
