import copy
import warnings

import numpy as np

import teaser.data.utilities as datahandling
from teaser.logic.archetypebuildings.residential import Residential
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.logic.buildingobjects.useconditions import UseConditions as UseCond
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.buildingphysics.door import Door
from teaser.logic.buildingobjects.building import rotate_orientation
from math import sin, cos, tan, atan, pi, sqrt


def _check_number_of_floors(room_names: list, room_floor: dict):
    floor_names = []
    for room_name in room_names:
        floor_names.append(room_floor[room_name])
    return len(set(floor_names))


# The six oriented surfaces the AixLib HOM's building envelope receives
# solar radiation on, in the order BESMod's AixLibHighOrder connects them to
# its RadOnTiltedSurfaceAdaptor array: the four facades and the two halves
# of the pitched roof. The names are AixLib's own (from its
# SurfaceOrientationData_N_E_S_W_RoofN_Roof_S record, "O" for East), and
# stay with the port rather than the compass direction once the building is
# rotated. The orientations are TEASER's (0 = North, clockwise) for the
# unrotated archetype and therefore repeat the "ori" entries generate_archetype
# gives the matching elements - test_hom_surface_orientations keeps the two
# in sync. "roof" tilt is not AixLib's fixed 45 deg but the archetype's own
# roof_tilt.
# The five groups of interior surfaces the single-zone ROM distributes the
# solar radiation entering through the windows over, in the order BESMod's
# TEASERBuildingSingleZone.FourElements lists them in AArraySol:
# {ATotExt, ATotWin, AInt, AFloor, ARoof}. splitFactorSolRad has one row per
# group - see calc_split_factor_sol_rad.
_ROM_SOLAR_SURFACE_GROUPS = ("OuterWall", "Window", "InnerWall",
                             "GroundFloor", "Roof")

# Surface coefficients of AixLibHighOrderSingleFamilyHouse's
# hom_surface_coefficients, in W/(m2K): high enough for a window's
# convection to drop out of its U-value, and close enough to zero for the
# outer radiation to drop out.
HOM_WINDOW_CONVECTION = 1e5
HOM_OUTER_RADIATION = 1e-9

_HOM_RADIATION_SURFACES = (
    ("N", 0.0, "wall"),
    ("O", 90.0, "wall"),
    ("S", 180.0, "wall"),
    ("W", 270.0, "wall"),
    ("Roof_N", 0.0, "roof"),
    ("Roof_S", 180.0, "roof"),
)

# Air change rates [1/h] of an unheated room's own air by
# attic_infiltration_class, as DIN EN 12831-1 Table 5 heads its "dicht" and
# "undicht" columns - used where attic_air_change_rate is not set.
_ATTIC_AIR_CHANGE_RATES = {"dicht": 0.5, "undicht": 2.5}

# Volumetric heat capacity of air DIN EN 12831-1 uses, in Wh/(m3K)
_RHO_C_AIR = 0.34

# Daily course of the internal gains of each heated room [W], hour by hour
# from midnight: the hourly means of BESMod's Resources/InternalGainsHOM.txt,
# which the AixLib HOM's OFD house was driven with. Only their shape across
# the rooms and the day is used; the export scales them to the zone's use
# conditions (see AixLibHighOrderSingleFamilyHouse.room_internal_gains_profiles).
_ROOM_INTERNAL_GAINS_PROFILES = {
    "Livingroom": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 301, 301, 504, 504, 454, 0, 0],
    "Hobby": [0, 0, 0, 0, 0, 0, 0, 426, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 652, 427, 0, 0, 0, 0],
    "Corridor_gf": [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
    "WC_Storage": [0, 0, 0, 0, 0, 0, 0, 163, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 163, 0, 0, 0, 0, 0],
    "Kitchen": [0, 0, 0, 0, 0, 0, 0, 355, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 680, 329, 0, 0, 0, 0],
    "Bedroom": [166, 166, 166, 166, 166, 166, 165, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 165, 166],
    "Children1": [83, 83, 83, 83, 83, 83, 83, 0, 0, 0, 0, 0, 0, 0, 126, 126, 0, 300, 0, 0, 213, 83, 83, 83],
    "Corridor_upp": [50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50],
    "Bath": [0, 0, 0, 0, 0, 0, 0, 447, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 221, 271, 0, 0],
    "Children2": [83, 83, 83, 83, 83, 83, 83, 0, 0, 0, 0, 0, 0, 0, 126, 126, 0, 300, 0, 0, 213, 83, 83, 83],
}

# Name of the virtual outer element const_volumes_ua gives an unheated
# room's air change, see _integrate_unheated_rooms_const_volumes
_AIR_CHANGE = "air_change"


class AixLibHighOrderSingleFamilyHouse(Residential):
    def __init__(
            self,
            parent=None,
            name=None,
            year_of_construction=None,
            height_of_floors=2.6,
            net_leased_area=170,
            construction_data=None,
    ):
        """

        Parameters
        ----------
        parent
        name
        year_of_construction
        height_of_floors
        net_leased_area
            Default is original AixLib HOM dim. similar TABULA buildings span
            from 111 to 216
        construction_data
        """
        super(AixLibHighOrderSingleFamilyHouse, self).__init__(
            parent,
            name,
            year_of_construction,
            net_leased_area,
        )
        # scale_building_geometry's own scaling target, captured once here
        # rather than read back from self.net_leased_area on every
        # generate_archetype call: ThermalZone.area's setter incrementally
        # adjusts self.net_leased_area towards the actually-achieved zone
        # floor area (which is only ever approximately equal to the
        # requested value), so re-reading self.net_leased_area as the
        # scaling input on each call would compound that small mismatch
        # into unbounded drift over repeated calls.
        self._net_leased_area_target = self.net_leased_area
        self.construction_data = construction_data
        self.height_of_floors = height_of_floors

        if self.construction_data.is_tabula_de() or self.construction_data.is_tabula_dk():
            self.construction_data_1 = self.construction_data.value + "_1_SFH"
        else:
            self.construction_data_1 = self.construction_data.value

        # only single zone roms
        self.integrate_unheated_rooms_integration_methods = [
            "const_volumes",
            "const_volumes_ua",
            "din12831_f1",
        ]
        # Reassigning this (whole-dict, e.g. integrate_unheated_rooms =
        # {"Attic": "din12831_f1"}) regenerates the archetype automatically
        # - see the property setter below.
        self.integrate_unheated_rooms = {"Attic": "const_volumes_ua"}
        # Used by the "const_volumes_ua" and "din12831_f1" methods: the air change rate of the
        # unheated room's own air in its heat balance, "dicht" (0.5 1/h) or
        # "undicht" (2.5 1/h) as in DIN EN 12831-1 Table 5, unless
        # attic_air_change_rate gives it directly in 1/h. Reassigning
        # either regenerates the archetype automatically.
        self.attic_infiltration_class = "undicht"
        self.attic_air_change_rate = None
        # Tilt of the two roof halves against the horizontal [deg], 45 as in
        # AixLib's OFD house. It shapes the upper floor's rooms below the
        # roof, the Attic and the roof areas, e.g. for photovoltaics on them.
        # Reassigning it regenerates the archetype automatically.
        self.roof_tilt = 45.0
        # Sets the ROM's outer surface coefficients up the way the HOM
        # handles them (see _set_hom_surface_coefficients). None applies
        # them exactly when the building is exported against
        # TEASERThermalSingleZone, i.e. with a single thermal zone and
        # use_old False; True or False forces them on or off.
        self.hom_surface_coefficients = None

        self.zoning = {"single_zone_heated": [
            "Livingroom",
            "Hobby",
            "Corridor_gf",
            "WC_Storage",
            "Kitchen",
            "Bedroom",
            "Children1",
            "Corridor_upp",
            "Bath",
            "Children2",
        ]}

        self._wall_types = ['OW', 'roof', 'roof_attic', 'IW_vert_half', 'IW_hori_upHalf', 'IW_hori_loHalf',
                            'ground_floor_loHalf',
                            'ground_floor_upHalf', 'IW_hori_att_upHalf', 'IW_hori_att_loHalf']
        self._original_hom_dim_parameters = {
            "height_of_floors": 2.6,
            "thickness_iw_simple": 0.145,
            "l1": 3.3,
            "l2": 2.44,
            "l3": 1.33,
            "l4": 3.3,
            "room_width": 3.92,
            "room_height": 2.6,
            "windowarea_11": 8.44,
            "windowarea_12": 1.73,
            "windowarea_22": 1.73,
            "windowarea_41": 1.4,
            "windowarea_51": 3.46,
            "windowarea_52": 1.73,
            "width_door_31": 1.01,
            "height_door_31": 2.25,
            "width_door_42": 1.25,
            "height_door_42": 2.25,
            "height_dwarf_wall": 1,
            "room_ceiling_attic_width": 2.28,
            "room_roof_length": 2.21,
            "windowarea_62": 1.73,
            "windowarea_63": 1.73,
            "windowarea_72": 1.73,
            "windowarea_73": 1.73,
            "windowarea_92": 1.73,
            "windowarea_102": 1.73,
            "windowarea_103": 1.73,
        }
        self.update_calc_original_hom_dim_parameters()

        self.room_name_nr = {
            "Livingroom": 1,
            "Hobby": 2,
            "Corridor_gf": 3,
            "WC_Storage": 4,
            "Kitchen": 5,
            "Bedroom": 6,
            "Children1": 7,
            "Corridor_upp": 8,
            "Bath": 9,
            "Children2": 10,
        }
        self.room_floor = {
            "Livingroom": "gf",
            "Hobby": "gf",
            "Corridor_gf": "gf",
            "WC_Storage": "gf",
            "Kitchen": "gf",
            "Bedroom": "upp",
            "Children1": "upp",
            "Corridor_upp": "upp",
            "Bath": "upp",
            "Children2": "upp",
        }
        # Nominal/design indoor temperature per room [K], used for the
        # room-wise heat load (calc_room_heat_loads) and, aggregated via
        # t_set_nominal_aggregation, for the single-zone ROM's own
        # zone.t_inside. Override individual rooms as needed, e.g. to tune
        # the default DIN-EN-12831-style assumption that only the bathroom
        # is designed for a higher temperature than the rest of the house.
        # Unlike integrate_unheated_rooms/t_set_nominal_aggregation/
        # attic_infiltration_class below, editing this dict in place
        # (room_t_set_nominal["Bath"] = ...) does NOT auto-regenerate -
        # call generate_archetype() explicitly afterwards.
        self.room_t_set_nominal = {room: 293.15 for room in self.room_name_nr}
        self.room_t_set_nominal["Bath"] = 297.15
        # How room_t_set_nominal is reduced to the ROM's single
        # zone.t_inside, which BESMod takes as TSetZone_nominal both for
        # the zone's nominal heat flow and for the design of its heating
        # system (e.g. the heating curve). Built-in options:
        # "heat_load_weighted_average" (default - the rooms weighted by
        # their heat load, the same as the default fac_room_t_set the zone
        # is operated with, since the zone's heat loss is the sum of the
        # rooms' heat transfer coefficients times their temperature
        # differences), "volume_weighted_average" and "max" (designs the
        # whole zone for its warmest room; the room-wise heat loads already
        # size the heating for that room). Alternatively, assign a callable
        # taking (room_names, self) and returning a temperature in K for
        # full custom control. Reassigning this regenerates the archetype
        # automatically.
        self.t_set_nominal_aggregation = "heat_load_weighted_average"
        # Weights that reduce the HOM's room-wise user profiles to the
        # single value the ROM's one merged zone takes - facRoomTSet and
        # facRoomNatVent of BESMod's TEASERHOMtoROM user profile, which
        # multiply the room-wise set temperature [K] / natural ventilation
        # air exchange rate [1/h] profiles and sum them up. Both are
        # therefore weighted averages, and each weighting is normalized to
        # sum to 1 (see _room_weights) - what matters is the ratio between
        # rooms, not the absolute values.
        #
        # Built-in options: "volume" (room_volumes, the physically correct
        # aggregation for an air exchange rate, since it conserves the total
        # ventilation air flow of the merged zone - the default for
        # fac_room_nat_vent), "heat_load" (room_heat_loads, close to
        # weighting the rooms by their heat transfer coefficients, which is
        # what a set temperature acts through - the default for
        # fac_room_t_set) and "equal". Alternatively assign a
        # dict {room_name: weight} covering every heated room, or a callable
        # taking (self) and returning such a dict, for full custom control.
        # These are plain attributes: unlike t_set_nominal_aggregation,
        # reassigning them does not regenerate the archetype (nothing about
        # the archetype itself depends on them - they are only read when
        # exporting), so they can be changed right up to the export.
        self.fac_room_t_set_weighting = "heat_load"
        # Daily course of each heated room's internal gains [W], 24 hourly
        # values from midnight, by default those of AixLib's OFD house. The
        # HOM export only takes their shape across the rooms and the day:
        # it scales them, day by day, to the energy the zone's use
        # conditions give the building (see
        # besmod_output._write_hom_user_profiles), so the HOM and the ROM
        # exported next to it get the internal gains of the use conditions,
        # spread over the rooms and the hours as in the OFD house.
        self.room_internal_gains_profiles = copy.deepcopy(_ROOM_INTERNAL_GAINS_PROFILES)
        self.fac_room_nat_vent_weighting = "volume"
        # Rotation of the whole building clockwise against the archetype's
        # own orientation [deg], i.e. 0 keeps the Livingroom facade facing
        # South as the original AixLib HOM has it. Set it through
        # rotate_building (which also rotates the already generated
        # elements); it is kept here so that a later generate_archetype()
        # rebuilds the elements rotated instead of snapping them back to
        # the archetype's own orientation, and so the HOM export can write
        # the rotated surfaces into its SurfaceOrientation record.
        self.rotation = 0.0
        # The rotation the zones' ROM parameters were last calculated for,
        # so the HOM export can tell whether the two halves it writes still
        # agree - see rotation_pending_recalculation.
        self._rotation_at_last_calc = 0.0
        # Populated by calc_building_parameter (room_name -> heat_load [W]
        # / list ordered by room_name_nr), cached here so exports can read
        # them directly without recomputing - always in sync since
        # calc_building_parameter is itself the prerequisite for
        # zone.model_attr.heat_load to be current (e.g. after retrofit).
        self.room_heat_loads = {}
        self.room_heat_loads_list = []
        self.top_level_geo_params = {}
        self.detailed_geo = {}
        self.room_volumes = {}
        # Persistent, retrofittable elements for unheated rooms' own
        # envelope (e.g. the Attic's roof/gable walls). These are not part
        # of any ThermalZone (the ROM only has the single heated zone), so
        # they would never be touched by retrofit otherwise. Structure:
        # {unheated_room_name: {element_name: BuildingElement}}
        self.unheated_room_envelope_elements = {}

        # From here on, reassigning integrate_unheated_rooms,
        # t_set_nominal_aggregation or attic_infiltration_class
        # regenerates the archetype automatically (see their setters
        # below) - guarded by this flag so the initial assignments above,
        # made before the rest of __init__'s state exists, don't trigger
        # a premature generate_archetype() call.
        self._initialized = True

    def update_calc_original_hom_dim_parameters(self):
        def_params = self._original_hom_dim_parameters.copy()
        self._original_hom_dim_parameters["bldg_inner_width"] = 2 * def_params["room_width"]
        self._original_hom_dim_parameters["bldg_inner_length"] = (def_params["l1"] + def_params["l2"] +
                                                                  def_params["l3"] + def_params["l4"])
        self._original_hom_dim_parameters["room1_length"] = (def_params["l1"] + def_params["l2"] +
                                                             def_params["thickness_iw_simple"])
        self._original_hom_dim_parameters["room3_length"] = (def_params["l2"] + def_params["l3"] +
                                                             def_params["thickness_iw_simple"])
        self._original_hom_dim_parameters["room5_length"] = (def_params["l3"] + def_params["l4"] +
                                                             def_params["thickness_iw_simple"])

    def scale_building_geometry(self):
        og_dim = self._original_hom_dim_parameters
        self.top_level_geo_params = {}
        if self.year_of_construction < 1995:
            tir = 4
        elif 2002 > self.year_of_construction >= 1995:
            tir = 3
        elif 2009 > self.year_of_construction >= 2002:
            tir = 2
        else:
            tir = 1
        self.top_level_geo_params["tir"] = tir

        net_leased_area = self._net_leased_area_target

        bldg_width = sqrt(net_leased_area / 2 * (og_dim["bldg_inner_width"] / og_dim["bldg_inner_length"]))
        bldg_length = net_leased_area / 2 / bldg_width

        room_width = bldg_width / 2
        self.top_level_geo_params['room_width'] = room_width

        l1 = bldg_length * og_dim["l1"] / og_dim["bldg_inner_length"]
        l2 = bldg_length * og_dim["l2"] / og_dim["bldg_inner_length"]
        l3 = bldg_length * og_dim["l3"] / og_dim["bldg_inner_length"]
        l4 = bldg_length * og_dim["l4"] / og_dim["bldg_inner_length"]

        self.top_level_geo_params["l1"] = l1
        self.top_level_geo_params["l2"] = l2
        self.top_level_geo_params["l3"] = l3
        self.top_level_geo_params["l4"] = l4

        thickness_iw_simple = og_dim["thickness_iw_simple"]
        self.top_level_geo_params["thickness_iw_simple"] = thickness_iw_simple
        room1_length = l1 + l2 + thickness_iw_simple
        room3_length = l2 + l3 + thickness_iw_simple
        room5_length = l3 + l4 + thickness_iw_simple

        self.top_level_geo_params["room1_length"] = room1_length
        self.top_level_geo_params["room3_length"] = room3_length
        self.top_level_geo_params["room5_length"] = room5_length

        roof_length = bldg_length + 2 * thickness_iw_simple  # inner wall thicknesses load simpled?
        self.top_level_geo_params["roof_length"] = roof_length

        roof_tilt = self.roof_tilt
        # the angle at the ridge, which AixLib's attic takes
        alfa_grad = 180 - 2 * roof_tilt
        self.top_level_geo_params["roof_tilt"] = roof_tilt
        self.top_level_geo_params["alfa_grad"] = alfa_grad
        height_of_floors = self.height_of_floors
        self.top_level_geo_params["height_of_floors"] = height_of_floors
        room_height_short = og_dim["height_dwarf_wall"]
        room_width_short = room_width - (height_of_floors - room_height_short) / tan(roof_tilt * pi / 180)
        if room_width_short <= 0:
            raise ValueError(
                f"A roof_tilt of {roof_tilt} deg is too flat for {self.name}: "
                f"the roof would meet the upper floor's ceiling outside its "
                f"rooms. It needs at least "
                f"{atan((height_of_floors - room_height_short) / room_width) * 180 / pi:.1f} deg "
                f"for rooms {room_width:.2f} m wide.")
        self.top_level_geo_params["room_width_short"] = room_width_short
        self.top_level_geo_params["room_height_short"] = room_height_short
        wRO = (height_of_floors - room_height_short) / sin(roof_tilt * pi / 180)
        self.top_level_geo_params["wRO"] = wRO

        roof_width = 2 * room_width_short + thickness_iw_simple  # better to use load wall thickness could also be computed directly in modelica
        self.top_level_geo_params["roof_width"] = roof_width
        wROi = roof_width / 2 / cos(roof_tilt * pi / 180)
        self.top_level_geo_params["wROi"] = wROi
        # print(f"Complete building height: {height_of_floors*2+wROi*sin(roof_tilt*pi/180)}")

        windowarea_11 = og_dim["windowarea_11"] * room1_length / og_dim["room1_length"]
        windowarea_12 = og_dim["windowarea_12"] * room_width / og_dim["room_width"]
        windowarea_22 = og_dim["windowarea_22"] * roof_width / og_dim["room_width"]
        windowarea_41 = og_dim["windowarea_41"] * l4 / og_dim["l4"]
        windowarea_51 = og_dim["windowarea_51"] * room5_length / og_dim["room5_length"]
        windowarea_52 = og_dim["windowarea_52"] * room_width / og_dim["room_width"]

        self.top_level_geo_params["windowarea_11"] = windowarea_11
        self.top_level_geo_params["windowarea_12"] = windowarea_12
        self.top_level_geo_params["windowarea_22"] = windowarea_22
        self.top_level_geo_params["windowarea_41"] = windowarea_41
        self.top_level_geo_params["windowarea_51"] = windowarea_51
        self.top_level_geo_params["windowarea_52"] = windowarea_52

        # Make roof windows separately changeable? Or length scaling instead of width scaling?
        windowarea_i_up_roof = 1.73 * room_width_short / og_dim["room_ceiling_attic_width"]
        windowarea_i_up_wall = 1.73 * bldg_length / og_dim["bldg_inner_length"]

        self.top_level_geo_params["windowarea_62"] = windowarea_i_up_wall
        self.top_level_geo_params["windowarea_63"] = windowarea_i_up_roof
        self.top_level_geo_params["windowarea_72"] = windowarea_i_up_wall
        self.top_level_geo_params["windowarea_73"] = windowarea_i_up_roof
        self.top_level_geo_params["windowarea_92"] = windowarea_i_up_wall
        self.top_level_geo_params["windowarea_102"] = windowarea_i_up_wall
        self.top_level_geo_params["windowarea_103"] = windowarea_i_up_roof

        self.top_level_geo_params["windowarea_i_up_roof"] = windowarea_i_up_roof
        self.top_level_geo_params["windowarea_i_up_wall"] = windowarea_i_up_wall

        # Heron's formula
        semi_perimeter = (roof_width + wROi + wROi) * 0.5
        self.top_level_geo_params["attic_vert_wall_area"] = (
            np.sqrt(semi_perimeter * (semi_perimeter - roof_width) *
                    (semi_perimeter - wROi) * (semi_perimeter - wROi))
        )

        self.top_level_geo_params["upp_gable_wall_area"] = (self.top_level_geo_params["room_width"] *
                                                            self.top_level_geo_params["height_of_floors"] -
                                                            ((self.top_level_geo_params["height_of_floors"] -
                                                              self.top_level_geo_params["room_height_short"]) * (
                                                                     self.top_level_geo_params["room_width"] -
                                                                     self.top_level_geo_params["room_width_short"]
                                                             )) / 2)

        return self.top_level_geo_params

    def generate_archetype(self):
        """Generates a SingleFamilyHouse archetype buildings

        With given values, this function generates an archetype building for
        AixLib HOM Single Family House.
        """
        self.scale_building_geometry()
        self.detailed_geo = {
            "Livingroom": {
                "outside_wall1": {
                    "ori": 180,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room1_length"] *
                            self.top_level_geo_params["height_of_floors"] -
                            self.top_level_geo_params["windowarea_11"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_11"],
                },
                "outside_wall2": {
                    "ori": 270,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room_width"] *
                            self.top_level_geo_params["height_of_floors"] -
                            self.top_level_geo_params["windowarea_12"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_12"],
                },
                "floor": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room1_length"] * self.top_level_geo_params["room_width"],
                    "type": "GroundFloor",
                    "element_construction_type": None,
                },
                "ceiling": {
                    "ori": -1,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room1_length"] * self.top_level_geo_params["room_width"],
                    "type": "Ceiling",
                    "element_construction_type": None,
                    "adjacent": ("Bedroom", "floor")
                },
                "inside_wall1a": {
                    "ori": 0,
                    "tilt": 90,
                    "area": (self.top_level_geo_params["room1_length"] - self.top_level_geo_params["l2"]) *
                            self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Hobby", "inside_wall1")
                },
                "inside_wall1b": {
                    "ori": 0,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l2"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Corridor_gf", "inside_wall2a")
                },
                "inside_wall2": {
                    "ori": 90,  # direction of outside of room
                    "tilt": 90,
                    "area": self.top_level_geo_params["room_width"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": None,
                    "adjacent": ("Kitchen", "inside_wall2")
                }
            },
            "Kitchen": {
                "outside_wall1": {
                    "ori": 180,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room5_length"] *
                            self.top_level_geo_params["height_of_floors"] -
                            self.top_level_geo_params["windowarea_51"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_51"],
                },
                "outside_wall2": {
                    "ori": 90,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room_width"] *
                            self.top_level_geo_params["height_of_floors"] -
                            self.top_level_geo_params["windowarea_52"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_52"],
                },
                "floor": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room5_length"] * self.top_level_geo_params["room_width"],
                    "type": "GroundFloor",
                    "element_construction_type": None,
                },
                "ceiling": {
                    "ori": -1,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room5_length"] * self.top_level_geo_params["room_width"],
                    "type": "Ceiling",
                    "element_construction_type": None,
                    "adjacent": ("Children2", "floor")
                },
                "inside_wall1a": {
                    "ori": 0,
                    "tilt": 90,
                    "area": (self.top_level_geo_params["room5_length"] - self.top_level_geo_params["l3"]) *
                            self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("WC_Storage", "inside_wall1")
                },
                "inside_wall1b": {
                    "ori": 0,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l3"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Corridor_gf", "inside_wall2b")
                },
                "inside_wall2": {
                    "ori": 270,  # direction of outside of room
                    "tilt": 90,
                    "area": self.top_level_geo_params["room_width"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": None,
                    "adjacent": ("Livingroom", "inside_wall2")
                },
            },
            "Hobby": {
                "outside_wall1": {
                    "ori": 0,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l1"] * self.top_level_geo_params["height_of_floors"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": False,
                },
                "outside_wall2": {
                    "ori": 270,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room_width"] *
                            self.top_level_geo_params["height_of_floors"] -
                            self.top_level_geo_params["windowarea_22"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_22"],
                },
                "floor": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["l1"] * self.top_level_geo_params["room_width"],
                    "type": "GroundFloor",
                    "element_construction_type": None,
                },
                "ceiling": {
                    "ori": -1,
                    "tilt": 0,
                    "area": self.top_level_geo_params["l1"] * self.top_level_geo_params["room_width"],
                    "type": "Ceiling",
                    "element_construction_type": None,
                    "adjacent": ("Children1", "floor")
                },
                "inside_wall1": {
                    "ori": 180,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l1"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Livingroom", "inside_wall1a")
                },
                "inside_wall2": {
                    "ori": 90,  # direction of outside of room
                    "tilt": 90,
                    "area": self.top_level_geo_params["room_width"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": None,
                    "adjacent": ("Corridor_gf", "inside_wall1")
                },
            },
            "Corridor_gf": {
                "outside_wall1": {
                    "ori": 0,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room3_length"] * self.top_level_geo_params["height_of_floors"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": False,
                },
                "floor": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room3_length"] * self.top_level_geo_params["room_width"],
                    "type": "GroundFloor",
                    "element_construction_type": None,
                },
                "ceiling": {
                    "ori": -1,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room3_length"] * self.top_level_geo_params["room_width"],
                    "type": "Ceiling",
                    "element_construction_type": None,
                    "adjacent": ("Corridor_upp", "floor")
                },
                "inside_wall1": {
                    "ori": 270,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room_width"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": None,
                    "adjacent": ("Hobby", "inside_wall2")
                },
                "inside_wall2a": {
                    "ori": 90,
                    "tilt": 90,
                    "area": (self.top_level_geo_params["room3_length"] - self.top_level_geo_params["l3"]) *
                            self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Livingroom", "inside_wall1b")
                },
                "inside_wall2b": {
                    "ori": 90,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l3"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Kitchen", "inside_wall1b")
                },
                "inside_wall3": {
                    "ori": 90,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room_width"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": None,
                    "adjacent": ("WC_Storage", "inside_wall2")
                }
            },
            "WC_Storage": {
                "outside_wall1": {
                    "ori": 0,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l4"] *
                            self.top_level_geo_params["height_of_floors"] -
                            self.top_level_geo_params["windowarea_41"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_41"],
                },
                "outside_wall2": {
                    "ori": 90,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room_width"] *
                            self.top_level_geo_params["height_of_floors"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": False,
                },
                "floor": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["l4"] * self.top_level_geo_params["room_width"],
                    "type": "GroundFloor",
                    "element_construction_type": None,
                },
                "ceiling": {
                    "ori": -1,
                    "tilt": 0,
                    "area": self.top_level_geo_params["l4"] * self.top_level_geo_params["room_width"],
                    "type": "Ceiling",
                    "element_construction_type": None,
                    "adjacent": ("Bath", "floor")
                },
                "inside_wall1": {
                    "ori": 180,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l4"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Kitchen", "inside_wall1a")
                },
                "inside_wall2": {
                    "ori": 270,  # direction of outside of room
                    "tilt": 90,
                    "area": self.top_level_geo_params["room_width"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": None,
                    "adjacent": ("Corridor_gf", "inside_wall3")
                },
            },
            "Bedroom": {
                "roof": {
                    "ori": 180,
                    "tilt": self.top_level_geo_params["roof_tilt"],
                    "area": self.top_level_geo_params["wRO"] *
                            self.top_level_geo_params["room1_length"] -
                            self.top_level_geo_params["windowarea_63"],
                    "type": "Roof",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_63"],
                },
                "outside_wall1": {
                    "ori": 180,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room1_length"] *
                            self.top_level_geo_params["room_height_short"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": False,
                },
                "outside_wall2": {
                    "ori": 270,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room_width"] *
                            self.top_level_geo_params["height_of_floors"] -
                            ((self.top_level_geo_params["height_of_floors"] -
                              self.top_level_geo_params["room_height_short"]) * (
                                     self.top_level_geo_params["room_width"] -
                                     self.top_level_geo_params["room_width_short"]
                             )) / 2 -
                            self.top_level_geo_params["windowarea_62"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_62"],
                },
                "floor": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room1_length"] * self.top_level_geo_params["room_width"],
                    "type": "Floor",
                    "element_construction_type": None,
                    "adjacent": ("Livingroom", "ceiling")
                },
                "ceiling": {
                    "ori": -1,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room1_length"] * self.top_level_geo_params["room_width_short"],
                    "type": "Ceiling",
                    "element_construction_type": "Attic",
                    "adjacent": ("Attic", "floorRoom1")
                },
                "inside_wall1a": {
                    "ori": 0,
                    "tilt": 90,
                    "area": (self.top_level_geo_params["room1_length"] - self.top_level_geo_params["l2"]) *
                            self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Children1", "inside_wall1")
                },
                "inside_wall1b": {
                    "ori": 0,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l2"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Corridor_upp", "inside_wall2a")
                },
                "inside_wall2": {
                    "ori": 90,  # direction of outside of room
                    "tilt": 90,
                    "area": self.top_level_geo_params["room_width"] *
                            self.top_level_geo_params["height_of_floors"] -
                            ((self.top_level_geo_params["height_of_floors"] -
                              self.top_level_geo_params["room_height_short"]) * (
                                     self.top_level_geo_params["room_width"] -
                                     self.top_level_geo_params["room_width_short"]
                             )) / 2,
                    "type": "InnerWall",
                    "element_construction_type": None,
                    "adjacent": ("Children2", "inside_wall2")
                }
            },
            "Children2": {
                "roof": {
                    "ori": 180,
                    "tilt": self.top_level_geo_params["roof_tilt"],
                    "area": self.top_level_geo_params["wRO"] *
                            self.top_level_geo_params["room5_length"] -
                            self.top_level_geo_params["windowarea_103"],
                    "type": "Roof",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_103"],
                },
                "outside_wall1": {
                    "ori": 180,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room5_length"] *
                            self.top_level_geo_params["room_height_short"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": False,
                },
                "outside_wall2": {
                    "ori": 90,
                    "tilt": 90,
                    "area": self.top_level_geo_params["upp_gable_wall_area"] -
                            self.top_level_geo_params["windowarea_102"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_102"],
                },
                "floor": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room5_length"] * self.top_level_geo_params["room_width"],
                    "type": "Floor",
                    "element_construction_type": None,
                    "adjacent": ("Kitchen", "ceiling")
                },
                "ceiling": {
                    "ori": -1,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room5_length"] * self.top_level_geo_params["room_width_short"],
                    "type": "Ceiling",
                    "element_construction_type": "Attic",
                    "adjacent": ("Attic", "floorRoom5")
                },
                "inside_wall1a": {
                    "ori": 0,
                    "tilt": 90,
                    "area": (self.top_level_geo_params["room5_length"] - self.top_level_geo_params["l3"]) *
                            self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Bath", "inside_wall1")
                },
                "inside_wall1b": {
                    "ori": 0,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l3"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Corridor_upp", "inside_wall2b")
                },
                "inside_wall2": {
                    "ori": 270,  # direction of outside of room
                    "tilt": 90,
                    "area": self.top_level_geo_params["upp_gable_wall_area"],
                    "type": "InnerWall",
                    "element_construction_type": None,
                    "adjacent": ("Bedroom", "inside_wall2")
                },
            },
            "Children1": {
                "roof": {
                    "ori": 0,
                    "tilt": self.top_level_geo_params["roof_tilt"],
                    "area": self.top_level_geo_params["wRO"] *
                            self.top_level_geo_params["l1"] -
                            self.top_level_geo_params["windowarea_73"],
                    "type": "Roof",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_73"],
                },
                "outside_wall1": {
                    "ori": 0,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l1"] * self.top_level_geo_params["room_height_short"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": False,
                },
                "outside_wall2": {
                    "ori": 270,
                    "tilt": 90,
                    "area": self.top_level_geo_params["upp_gable_wall_area"] -
                            self.top_level_geo_params["windowarea_72"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_72"],
                },
                "floor": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["l1"] * self.top_level_geo_params["room_width"],
                    "type": "Floor",
                    "element_construction_type": None,
                    "adjacent": ("Hobby", "ceiling")
                },
                "ceiling": {
                    "ori": -1,
                    "tilt": 0,
                    "area": self.top_level_geo_params["l1"] * self.top_level_geo_params["room_width_short"],
                    "type": "Ceiling",
                    "element_construction_type": "Attic",
                    "adjacent": ("Attic", "floorRoom2")
                },
                "inside_wall1": {
                    "ori": 180,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l1"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Bedroom", "inside_wall1a")
                },
                "inside_wall2": {
                    "ori": 90,  # direction of outside of room
                    "tilt": 90,
                    "area": self.top_level_geo_params["upp_gable_wall_area"],
                    "type": "InnerWall",
                    "element_construction_type": None,
                    "adjacent": ("Corridor_upp", "inside_wall1")
                },
            },
            "Corridor_upp": {
                "roof": {
                    "ori": 0,
                    "tilt": self.top_level_geo_params["roof_tilt"],
                    "area": self.top_level_geo_params["wRO"] *
                            self.top_level_geo_params["room3_length"],
                    "type": "Roof",
                    "element_construction_type": None,
                    "with_window": False
                },
                "outside_wall1": {
                    "ori": 0,
                    "tilt": 90,
                    "area": self.top_level_geo_params["room3_length"] * self.top_level_geo_params["room_height_short"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": False,
                },
                "floor": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room3_length"] * self.top_level_geo_params["room_width"],
                    "type": "Floor",
                    "element_construction_type": None,
                    "adjacent": ("Corridor_gf", "ceiling")
                },
                "ceiling": {
                    "ori": -1,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room3_length"] * self.top_level_geo_params["room_width_short"],
                    "type": "Ceiling",
                    "element_construction_type": "Attic",
                    "adjacent": ("Attic", "floorRoom3")
                },
                "inside_wall1": {
                    "ori": 270,
                    "tilt": 90,
                    "area": self.top_level_geo_params["upp_gable_wall_area"],
                    "type": "InnerWall",
                    "element_construction_type": None,
                    "adjacent": ("Children1", "inside_wall2")
                },
                "inside_wall2a": {
                    "ori": 90,
                    "tilt": 90,
                    "area": (self.top_level_geo_params["room3_length"] - self.top_level_geo_params["l3"]) *
                            self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Bedroom", "inside_wall1b")
                },
                "inside_wall2b": {
                    "ori": 90,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l3"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Children2", "inside_wall1b")
                },
                "inside_wall3": {
                    "ori": 90,
                    "tilt": 90,
                    "area": self.top_level_geo_params["upp_gable_wall_area"],
                    "type": "InnerWall",
                    "element_construction_type": None,
                    "adjacent": ("Bath", "inside_wall2")
                }
            },
            "Bath": {
                "roof": {
                    "ori": 0,
                    "tilt": self.top_level_geo_params["roof_tilt"],
                    "area": self.top_level_geo_params["wRO"] *
                            self.top_level_geo_params["l4"],
                    "type": "Roof",
                    "element_construction_type": None,
                    "with_window": False
                },
                "outside_wall1": {
                    "ori": 0,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l4"] *
                            self.top_level_geo_params["room_height_short"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": False,
                },
                "outside_wall2": {
                    "ori": 90,
                    "tilt": 90,
                    "area": self.top_level_geo_params["upp_gable_wall_area"] -
                            self.top_level_geo_params["windowarea_92"],
                    "type": "OuterWall",
                    "element_construction_type": None,
                    "with_window": True,
                    "windowarea": self.top_level_geo_params["windowarea_92"],
                },
                "floor": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["l4"] * self.top_level_geo_params["room_width"],
                    "type": "Floor",
                    "element_construction_type": None,
                    "adjacent": ("WC_Storage", "ceiling")
                },
                "ceiling": {
                    "ori": -1,
                    "tilt": 0,
                    "area": self.top_level_geo_params["l4"] * self.top_level_geo_params["room_width_short"],
                    "type": "Ceiling",
                    "element_construction_type": "Attic",
                    "adjacent": ("Attic", "floorRoom4")
                },
                "inside_wall1": {
                    "ori": 180,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l4"] * self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Children2", "inside_wall1a")
                },
                "inside_wall2": {
                    "ori": 270,  # direction of outside of room
                    "tilt": 90,
                    "area": self.top_level_geo_params["upp_gable_wall_area"],
                    "type": "InnerWall",
                    "element_construction_type": None,
                    "adjacent": ("Corridor_upp", "inside_wall3")
                },
            },
            "Attic": {
                "roof1": {
                    "ori": 180,
                    "tilt": self.top_level_geo_params["roof_tilt"],
                    "area": self.top_level_geo_params["wROi"] *
                            self.top_level_geo_params["roof_length"],
                    "type": "Roof",
                    "element_construction_type": "Attic",
                    "with_window": False,
                },
                "roof2": {
                    "ori": 0,
                    "tilt": self.top_level_geo_params["roof_tilt"],
                    "area": self.top_level_geo_params["wROi"] *
                            self.top_level_geo_params["roof_length"],
                    "type": "Roof",
                    "element_construction_type": "Attic",
                    "with_window": False,
                },
                "outside_wall1": {
                    "ori": 90,
                    "tilt": 90,
                    "area": self.top_level_geo_params["attic_vert_wall_area"],
                    "type": "OuterWall",
                    "element_construction_type": "Attic",
                    "with_window": False,
                },
                "outside_wall2": {
                    "ori": 270,
                    "tilt": 90,
                    "area": self.top_level_geo_params["attic_vert_wall_area"],
                    "type": "OuterWall",
                    "element_construction_type": "Attic",
                    "with_window": False,
                },
                "floorRoom1": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room1_length"] * self.top_level_geo_params["room_width_short"],
                    "type": "Floor",
                    "element_construction_type": "Attic",
                    "adjacent": ("Bedroom", "ceiling")
                },
                "floorRoom2": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["l1"] * self.top_level_geo_params["room_width_short"],
                    "type": "Floor",
                    "element_construction_type": "Attic",
                    "adjacent": ("Children1", "ceiling")
                },
                "floorRoom3": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room3_length"] * self.top_level_geo_params["room_width_short"],
                    "type": "Floor",
                    "element_construction_type": "Attic",
                    "adjacent": ("Corridor_upp", "ceiling")
                },
                "floorRoom4": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["l4"] * self.top_level_geo_params["room_width_short"],
                    "type": "Floor",
                    "element_construction_type": "Attic",
                    "adjacent": ("Bath", "ceiling")
                },
                "floorRoom5": {
                    "ori": -2,
                    "tilt": 0,
                    "area": self.top_level_geo_params["room5_length"] * self.top_level_geo_params["room_width_short"],
                    "type": "Floor",
                    "element_construction_type": "Attic",
                    "adjacent": ("Children2", "ceiling")
                }
            }
        }
        self._apply_rotation_to_detailed_geo()
        self.room_volumes = {
            "Livingroom": self.top_level_geo_params["room1_length"] *
                          self.top_level_geo_params["room_width"] *
                          self.top_level_geo_params["height_of_floors"],
            "Hobby": self.top_level_geo_params["l1"] *
                     self.top_level_geo_params["room_width"] *
                     self.top_level_geo_params["height_of_floors"],
            "Corridor_gf": self.top_level_geo_params["room3_length"] *
                           self.top_level_geo_params["room_width"] *
                           self.top_level_geo_params["height_of_floors"],
            "WC_Storage": self.top_level_geo_params["l4"] *
                          self.top_level_geo_params["room_width"] *
                          self.top_level_geo_params["height_of_floors"],
            "Kitchen": self.top_level_geo_params["room5_length"] *
                       self.top_level_geo_params["room_width"] *
                       self.top_level_geo_params["height_of_floors"],
            "Bedroom": self.top_level_geo_params["room1_length"] *
                       self.top_level_geo_params["upp_gable_wall_area"],
            "Children1": self.top_level_geo_params["l1"] *
                         self.top_level_geo_params["upp_gable_wall_area"],
            "Corridor_upp": self.top_level_geo_params["room3_length"] *
                            self.top_level_geo_params["upp_gable_wall_area"],
            "Bath": self.top_level_geo_params["l4"] *
                    self.top_level_geo_params["upp_gable_wall_area"],
            "Children2": self.top_level_geo_params["room5_length"] *
                         self.top_level_geo_params["upp_gable_wall_area"],
            "Attic": self.top_level_geo_params["roof_length"] *
                     self.top_level_geo_params["attic_vert_wall_area"]
        }

        self.thermal_zones = None
        # ThermalZone.area's setter incrementally adjusts
        # self.net_leased_area (subtracting the zone's old area,
        # adding its new one) rather than replacing it - correct for a
        # persistent zone being resized, but since thermal_zones was
        # just reset above (each call creates fresh ThermalZone
        # instances), the "subtract old" side never happens without this
        # reset, so net_leased_area (and, through
        # scale_building_geometry's use of it as a scaling input, the
        # whole building) would grow unboundedly across repeated
        # generate_archetype calls. scale_building_geometry already used
        # the pre-reset value above, so resetting here is safe.
        self.net_leased_area = 0.0
        self.unheated_room_envelope_elements = {}
        if len(self.zoning) != 1 and self.integrate_unheated_rooms:
            raise AttributeError("The integration of unheated rooms is only supported for "
                                 "single-zone-ROMs")
        adj_ele_heated_to_unheated = {}
        for zone_name, room_names in self.zoning.items():
            zone = ThermalZone(parent=self)
            zone.name = zone_name
            zone.area = sum([self.detailed_geo[r]["floor"]["area"] for r in room_names])
            zone.number_of_floors = _check_number_of_floors(room_names, self.room_floor)
            zone.height_of_floors = self.height_of_floors
            zone.volume = sum([self.room_volumes[r] for r in room_names])
            use_cond = UseCond(parent=zone)
            use_cond.load_use_conditions(zone_usage="Living")  # create use conditions for single rooms
            zone.use_conditions = use_cond
            zone.use_conditions.with_ahu = False
            zone.t_inside = self._aggregate_t_set_nominal(room_names)

            for room_name in room_names:
                for ele_name, ele_info in self.detailed_geo[room_name].items():
                    adj_ele_unheated = ele_info.get("adjacent", (None, None))
                    if adj_ele_unheated[0] in self.integrate_unheated_rooms:
                        adj_ele_heated_to_unheated[(room_name, ele_name)] = adj_ele_unheated
                        continue  # handle elements to unheated rooms later
                    ele_type = ele_info["type"]
                    is_inner = False
                    if ele_type == "OuterWall":
                        element = OuterWall(parent=zone)
                    elif ele_type == "GroundFloor":
                        element = GroundFloor(parent=zone)
                    elif ele_type == "Roof":
                        element = Rooftop(parent=zone)
                    elif ele_type == "InnerWall":
                        element = InnerWall(parent=zone)
                        is_inner = True
                    elif ele_type == "Floor":
                        element = Floor(parent=zone)
                        is_inner = True
                    elif ele_type == "Ceiling":
                        element = Ceiling(parent=zone)
                        is_inner = True
                    else:
                        raise ValueError("Element type not recognized")

                    element.name = f"{room_name}_{ele_name}"
                    element.element_construction_type = ele_info["element_construction_type"]
                    element.load_type_element(
                        year=self.year_of_construction,
                        construction=self._construction_data.value if is_inner else self.construction_data_1,
                        data_class=self.data_class,
                    )
                    element.tilt = ele_info["tilt"]
                    element.orientation = ele_info["ori"]
                    element.area = ele_info["area"]

                    if ele_info.get("with_window", False):
                        window = Window(zone)
                        construction = (
                            "Waermeschutzverglasung, dreifach"
                            if self.construction_data.is_kfw()
                            else self.construction_data_1
                        )
                        window.load_type_element(
                            self.year_of_construction,
                            construction=construction,
                            data_class=self.data_class,
                        )
                        window.name = f"{room_name}_{ele_name}_win"
                        window.tilt = ele_info["tilt"]
                        window.orientation = ele_info["ori"]
                        window.area = ele_info["windowarea"]
            self._integrate_unheated_rooms(zone, adj_ele_heated_to_unheated)

    def _apply_rotation_to_detailed_geo(self):
        """Rotates the just-built detailed_geo by self.rotation

        detailed_geo is written out from scratch on every
        generate_archetype call and holds the archetype's own, unrotated
        orientations, so without this a building rotated earlier would snap
        back to the original AixLib HOM's orientation on every
        regeneration - e.g. when reassigning integrate_unheated_rooms.
        Rotating detailed_geo rather than the finished elements covers all
        three places that read "ori" from it at once: the heated zone's
        elements, their windows and the unheated rooms' own envelope.
        """
        if not self.rotation:
            return
        for room_geo in self.detailed_geo.values():
            for ele_info in room_geo.values():
                # -1 (roof/ceiling) and -2 (floor) are TEASER sentinels,
                # not angles, and stay as they are
                if ele_info["ori"] >= 0:
                    ele_info["ori"] = rotate_orientation(
                        ele_info["ori"], self.rotation)

    def rotate_building(self, angle):
        """Rotates the building to a given angle

        Extends Building.rotate_building, which covers the oriented
        elements a ROM archetype has (each zone's OuterWalls, Rooftops and
        Windows), by the two groups this archetype adds: the inner walls,
        whose orientation is the direction of the room's outside, and the
        unheated rooms' own envelope elements, which belong to no
        ThermalZone and are therefore invisible to the base implementation.

        The angle is also accumulated in self.rotation, both so a later
        generate_archetype() rebuilds the elements rotated (see
        _apply_rotation_to_detailed_geo) and so the HOM export can write
        the rotated surfaces into its SurfaceOrientation record: the HOM's
        Modelica geometry is fixed, so rotating the HOM means rotating the
        directions the solar radiation reaches it from.

        Parameters
        ----------

        angle: float
            rotation of the building clockwise, between 0 and 360 degrees
        """
        super(AixLibHighOrderSingleFamilyHouse, self).rotate_building(angle)
        elements = [wall for zone in self.thermal_zones
                    for wall in zone.inner_walls]
        elements.extend(element
                        for room_elements
                        in self.unheated_room_envelope_elements.values()
                        for element in room_elements.values())
        for element in elements:
            if element.orientation >= 0:
                element.orientation = rotate_orientation(
                    element.orientation, angle)
        self.rotation = rotate_orientation(self.rotation, angle)

    @property
    def rotation_pending_recalculation(self):
        """Whether the building was rotated after its last parameter calculation

        The ROM half of the export reads the zones' calculated model_attr,
        which keeps the orientations of the last
        calc_building_parameter call, while the HOM half reads
        surface_orientations, which follows rotate_building immediately.
        Rotating between the calculation and the export would therefore
        write a rotated HOM next to an unrotated ROM without this.
        """
        return self.rotation != self._rotation_at_last_calc

    @property
    def surface_orientations(self):
        """Orientation and tilt of the six surfaces the HOM is irradiated on

        Returns
        -------
        list of (str, float, float)
            (name, orientation, tilt) per surface, in the order BESMod's
            AixLibHighOrder connects them to its RadOnTiltedSurfaceAdaptor
            array - see _HOM_RADIATION_SURFACES. Orientation is in TEASER's
            convention (degrees clockwise from North) and already includes
            self.rotation; tilt is 90 deg for the four facades and the
            archetype's own roof_tilt for the two roof halves.
        """
        roof_tilt = self.top_level_geo_params["roof_tilt"]
        return [
            (name,
             rotate_orientation(orientation, self.rotation),
             90.0 if kind == "wall" else roof_tilt)
            for name, orientation, kind in _HOM_RADIATION_SURFACES
        ]

    def _room_of_element(self, element):
        """The heated room an element of the zone belongs to, or None

        Every element generate_archetype creates is named
        "{room_name}_..." (the equivalent elements integrating an unheated
        room into the zone are "{room_name}_{unheated_room}_...", so they
        belong to the heated room they connect to as well).
        """
        for room in self.room_name_nr:
            if element.name.startswith(room + "_"):
                return room
        return None

    def _unheated_room_of_element(self, element):
        """The unheated room an equivalent element of the zone represents

        Returns None for an element that is a heated room's own envelope.
        """
        room = self._room_of_element(element)
        if room is None:
            return None
        rest = element.name[len(room) + 1:]
        for unheated_room in self.integrate_unheated_rooms:
            if rest.startswith(unheated_room + "_"):
                return unheated_room
        return None

    def _indoor_area(self, element):
        """The area of an element's surface facing the heated zone [m2]

        Equal to element.area for a heated room's own envelope, but not for
        the equivalent elements that integrate an unheated room: with the
        'const_volumes' methods those carry the unheated room's *outer*
        area, while the surface the zone actually sees is the element
        between the two rooms (e.g. the ceiling below the Attic). Their
        ratio is the same for every piece, since
        _integrate_unheated_rooms_const_volumes distributes both areas with
        the same weights. The 'din12831_f1' method instead builds its
        elements on that in-between element itself, so there is nothing to
        correct.
        """
        unheated_room = self._unheated_room_of_element(element)
        if unheated_room is None:
            return element.area
        if self.integrate_unheated_rooms[unheated_room] not in (
                "const_volumes", "const_volumes_ua"):
            return element.area
        geo = self.detailed_geo[unheated_room].values()
        outer_area = sum(info["area"] for info in geo
                         if info["type"] in ("OuterWall", "Roof", "GroundFloor"))
        inner_area = sum(info["area"] for info in geo
                         if info["type"] in ("InnerWall", "Ceiling", "Floor"))
        if self.integrate_unheated_rooms[unheated_room] == "const_volumes_ua":
            # its virtual outer element for the air change
            outer_area += inner_area
        return element.area * inner_area / outer_area

    def _areas_by_room(self, elements, indoor=False):
        """{room_name: total area [m2]} of elements, grouped by heated room"""
        areas = {room: 0.0 for room in self.room_name_nr}
        for element in elements:
            room = self._room_of_element(element)
            if room is None:
                continue
            areas[room] += self._indoor_area(element) if indoor else element.area
        return areas

    def _floor_share(self, areas, floor):
        """Share of areas ({room: area}) that sits on one floor ("gf"/"upp")"""
        total = sum(areas.values())
        if total == 0:
            return 0.0
        return sum(area for room, area in areas.items()
                   if self.room_floor[room] == floor) / total

    def calc_rom_inner_heat_transfer_parameters(self):
        """Parameterizes the single-zone ROM's interior heat transfer from
        the HOM's room-wise geometry.

        BESMod's single-zone building model
        (Systems.Demand.Building.TEASERThermalSingleZone) refines AixLib's
        reduced order model with parameters this archetype can fill from
        the detailed room geometry it already has, instead of leaving them
        at the whole-zone defaults:

        - the shares of the exterior wall, interior wall and window areas
          that sit on the top and on the bottom floor, which size the long
          wave radiation exchange of the roof and of the ground floor plate
          with the other interior surfaces (each only sees its own floor),
        - RoofAreaAtticFactor, the part of the roof element group whose
          surface actually faces the heated zone - with an unheated Attic
          integrated, that group also carries the Attic's own envelope,
        - splitFactorSolRad, which distributes the solar radiation entering
          through the windows of each orientation over the five interior
          surface groups. In the HOM that radiation only ever reaches the
          surfaces of the room it enters, so deriving it room-wise is
          exactly what the single merged zone cannot do on its own.

        Called at the end of calc_building_parameter, since the per
        orientation parameters have to follow the very orientation order
        the zone's model_attr ended up with.
        """
        if len(self.thermal_zones) != 1:
            raise AttributeError(
                "The single-zone ROM parameters are only defined for the "
                "archetype's single heated zone.")
        zone = self.thermal_zones[0]
        rooms = sorted(self.room_name_nr, key=self.room_name_nr.get)

        outer_wall_areas = self._areas_by_room(zone.outer_walls)
        roof_areas = self._areas_by_room(zone.rooftops, indoor=True)
        inner_areas = self._areas_by_room(
            zone.inner_walls + zone.floors + zone.ceilings)
        ground_floor_areas = self._areas_by_room(zone.ground_floors)
        window_areas = self._areas_by_room(zone.windows)

        zone.ratio_ow_area_top_floor = self._floor_share(outer_wall_areas, "upp")
        zone.ratio_ow_area_bottom_floor = self._floor_share(outer_wall_areas, "gf")
        zone.ratio_iw_area_top_floor = self._floor_share(inner_areas, "upp")
        zone.ratio_iw_area_bottom_floor = self._floor_share(inner_areas, "gf")

        # AixLib's WindowSimple, which the HOM export uses, exchanges no
        # long wave radiation with the other interior surfaces at all, so
        # the ROM must not either - every one of its window couplings is
        # switched off by a ratio of zero.
        zone.ratio_win_area_top_floor = 0.0
        zone.ratio_win_area_bottom_floor = 0.0
        zone.ratio_win_area_ow = 0.0
        zone.ratio_win_area_iw = 0.0

        total_roof_area = sum(element.area for element in zone.rooftops)
        zone.roof_area_attic_factor = (
            sum(roof_areas.values()) / total_roof_area
            if total_roof_area else 1.0)

        # The solar radiation entering through a window reaches the room's
        # floor and its walls, but not the ceiling above it - so the
        # ceilings are part of AInt above, and of the interior area the
        # long wave exchange is sized on, but not of the area the radiation
        # is split over. The upper rooms' floors stay in: they are the
        # ground floor rooms' ceilings seen from above, and it is the upper
        # side of that construction the sun reaches.
        solar_inner_areas = self._areas_by_room(
            zone.inner_walls + zone.floors)
        self.calc_split_factor_sol_rad(
            zone, rooms, outer_wall_areas, roof_areas, solar_inner_areas,
            ground_floor_areas, window_areas)

    def calc_split_factor_sol_rad(self, zone, rooms, outer_wall_areas,
                                  roof_areas, inner_areas,
                                  ground_floor_areas, window_areas):
        """Derives splitFactorSolRad room-wise

        The radiation entering through the windows of one orientation is
        distributed over the five interior surface groups
        (_ROM_SOLAR_SURFACE_GROUPS) in the ratio of their areas - but in
        the HOM it only ever reaches the room it enters, so doing that per
        room and weighting the rooms by their share of the orientation's
        transparent area gives the merged zone a distribution it could not
        derive from its own aggregated areas.

        Within a room, the surfaces the radiation cannot reach are left
        out: the windows it came through and the wall or roof they sit in.
        The room's ceiling is not among the areas passed in at all, for the
        same reason (see calc_rom_inner_heat_transfer_parameters). Every
        column therefore still sums to 1.

        An orientation without any window keeps the whole-zone area split,
        there being no radiation to distribute room-wise.
        """
        groups = list(zip(zone.model_attr.orientation_facade,
                          zone.model_attr.tilt_facade))
        window_by_group = {room: {group: 0.0 for group in groups}
                           for room in rooms}
        host_wall_by_group = {room: {group: 0.0 for group in groups}
                              for room in rooms}
        host_roof_by_group = {room: {group: 0.0 for group in groups}
                              for room in rooms}
        hosts = {element.name: element
                 for element in zone.outer_walls + zone.rooftops}
        for window in zone.windows:
            room = self._room_of_element(window)
            group = (window.orientation, window.tilt)
            if room is None or group not in window_by_group[room]:
                continue
            window_by_group[room][group] += window.area
            # the window's own wall or roof, which it was cut out of - see
            # generate_archetype, where a window is named "{element}_win"
            host = hosts.get(window.name[:-len("_win")])
            if isinstance(host, Rooftop):
                host_roof_by_group[room][group] += self._indoor_area(host)
            elif host is not None:
                host_wall_by_group[room][group] += host.area

        room_totals = {
            room: (outer_wall_areas[room] + roof_areas[room]
                   + inner_areas[room] + ground_floor_areas[room]
                   + window_areas[room])
            for room in rooms
        }
        zone_areas = {
            "OuterWall": sum(outer_wall_areas.values()),
            "Window": sum(window_areas.values()),
            "InnerWall": sum(inner_areas.values()),
            "GroundFloor": sum(ground_floor_areas.values()),
            "Roof": sum(roof_areas.values()),
        }

        split_factors = [[] for _ in _ROM_SOLAR_SURFACE_GROUPS]
        for group in groups:
            transparent = {room: window_by_group[room][group] for room in rooms}
            total_transparent = sum(transparent.values())
            if total_transparent == 0:
                total_area = sum(zone_areas.values())
                for index, name in enumerate(_ROM_SOLAR_SURFACE_GROUPS):
                    split_factors[index].append(
                        zone_areas[name] / total_area if total_area else 0.0)
                continue
            for index, name in enumerate(_ROM_SOLAR_SURFACE_GROUPS):
                factor = 0.0
                for room in rooms:
                    if not transparent[room]:
                        continue
                    reachable = (room_totals[room]
                                 - window_by_group[room][group]
                                 - host_wall_by_group[room][group]
                                 - host_roof_by_group[room][group])
                    if reachable <= 0:
                        continue
                    if name == "OuterWall":
                        area = outer_wall_areas[room] - host_wall_by_group[room][group]
                    elif name == "Window":
                        area = window_areas[room] - window_by_group[room][group]
                    elif name == "Roof":
                        area = roof_areas[room] - host_roof_by_group[room][group]
                    elif name == "InnerWall":
                        area = inner_areas[room]
                    else:
                        area = ground_floor_areas[room]
                    factor += (area / reachable
                               * transparent[room] / total_transparent)
                split_factors[index].append(factor)

        zone.split_factor_sol_rad = split_factors

    def _aggregate_t_set_nominal(self, room_names):
        """Reduce room_t_set_nominal to a single nominal temperature [K]
        for a zone containing room_names, using self.t_set_nominal_aggregation
        ("max", "volume_weighted_average", or a custom callable taking
        (room_names, self) and returning a temperature in K).
        """
        aggregation = self.t_set_nominal_aggregation
        if callable(aggregation):
            return aggregation(room_names, self)
        if aggregation == "max":
            return max(self.room_t_set_nominal[r] for r in room_names)
        if aggregation == "heat_load_weighted_average" and all(
                r in self.room_heat_loads for r in room_names):
            total_heat_load = sum(self.room_heat_loads[r] for r in room_names)
            return sum(
                self.room_t_set_nominal[r] * self.room_heat_loads[r] for r in room_names
            ) / total_heat_load
        if aggregation in ("volume_weighted_average", "heat_load_weighted_average"):
            # before the room-wise heat loads exist, e.g. while
            # generate_archetype builds the zone, heat_load_weighted_average
            # starts out from the room volumes - calc_building_parameter
            # replaces it once they are known
            total_volume = sum(self.room_volumes[r] for r in room_names)
            return sum(
                self.room_t_set_nominal[r] * self.room_volumes[r] for r in room_names
            ) / total_volume
        raise ValueError(
            f"Unknown t_set_nominal_aggregation {aggregation!r}. Use "
            "'heat_load_weighted_average', 'volume_weighted_average', 'max', "
            "or a callable taking (room_names, self)."
        )

    def _compute_adjacent_to_unheated(self, room_names):
        """Re-derive the (room_name, ele_name) -> (unheated_room, unheated_ele_name)
        mapping for a zone's rooms from detailed_geo. Pure geometry lookup
        (no elements touched), so it is cheap to recompute e.g. when
        rebuilding the unheated-room integration after a retrofit.
        """
        adj_ele_heated_to_unheated = {}
        for room_name in room_names:
            for ele_name, ele_info in self.detailed_geo[room_name].items():
                adj = ele_info.get("adjacent", (None, None))
                if adj[0] in self.integrate_unheated_rooms:
                    adj_ele_heated_to_unheated[(room_name, ele_name)] = adj
        return adj_ele_heated_to_unheated

    def _get_or_create_unheated_envelope_element(self, room, ele_name, ele_info):
        """Get (or, on first call, create) the persistent, retrofittable
        real element representing one piece of an unheated room's own
        envelope (e.g. one of the Attic's roof/gable walls).

        Unlike the rest of detailed_geo, this element is not disposable: it
        is cached on self.unheated_room_envelope_elements so retrofit can be
        applied to it directly (it belongs to no ThermalZone and would
        otherwise never be retrofitted), and so _integrate_unheated_rooms
        can later rebuild the zone's equivalent-resistance elements from its
        actual, possibly-retrofitted state.
        """
        room_elements = self.unheated_room_envelope_elements.setdefault(room, {})
        element = room_elements.get(ele_name)
        if element is not None:
            return element

        if ele_info["type"] == "OuterWall":
            element = OuterWall(parent=None)
        elif ele_info["type"] == "GroundFloor":
            element = GroundFloor(parent=None)
        elif ele_info["type"] == "Roof":
            element = Rooftop(parent=None)
        else:
            raise ValueError("Element type not recognized")

        element.name = f"{room}_{ele_name}"
        element.element_construction_type = ele_info["element_construction_type"]
        element.load_type_element(
            year=self.year_of_construction,
            construction=self.construction_data_1,
            data_class=self.data_class,
        )
        element.tilt = ele_info["tilt"]
        element.orientation = ele_info["ori"]
        element.area = ele_info["area"]
        room_elements[ele_name] = element
        return element

    def _integrate_unheated_rooms(self, zone, adj_ele_heated_to_unheated):
        """(Re)builds the zone's elements that integrate unheated rooms
        (e.g. the Attic) into the single heated zone, dispatching to the
        method selected per unheated room in integrate_unheated_rooms:
        'const_volumes' (equivalent-resistance network, see
        _integrate_unheated_rooms_const_volumes), 'const_volumes_ua' (the
        same network, fitted to the unheated room's steady-state heat
        balance) or 'din12831_f1' (DIN
        EN 12831-1 temperature adjustment factor from the unheated room's
        heat balance, see _integrate_unheated_rooms_din12831_f1).

        Safe to call more than once for the same zone (e.g. after
        retrofitting the unheated rooms' own envelope elements via
        retrofit_building): both methods find their own existing elements
        by name and rebuild them in place, rather than duplicating them.
        """
        for room, method in self.integrate_unheated_rooms.items():
            if method in ("const_volumes", "const_volumes_ua"):
                self._integrate_unheated_rooms_const_volumes(
                    zone, room, adj_ele_heated_to_unheated,
                    fit_ua=method == "const_volumes_ua",
                )
            elif method == "din12831_f1":
                self._integrate_unheated_rooms_din12831_f1(
                    zone, room, adj_ele_heated_to_unheated,
                )
            else:
                raise ValueError(
                    f"Unknown integrate_unheated_rooms method {method!r} for "
                    f"{room!r}. Use one of "
                    f"{self.integrate_unheated_rooms_integration_methods}."
                )

    def _integrate_unheated_rooms_const_volumes(self, zone, room, adj_ele_heated_to_unheated,
                                                fit_ua=False):
        """(Re)builds the zone's equivalent-resistance elements that
        integrate one unheated room (e.g. the Attic) into the single
        heated zone, following the 'const_volumes' method.

        Each element the heated rooms share with the unheated room (e.g.
        a ceiling) is replaced by one stand-in per outer element of the
        unheated room (e.g. each roof half and gable wall), with that outer
        element's orientation and a share of its area. A stand-in's layers
        are the shared element's, thinned by inner/outer area of the
        unheated room, a layer of the unheated room's air, thick enough to
        hold its whole volume over all stand-ins, and the outer element's.
        This keeps the heat capacities of all three, not their thermal
        resistances.

        With fit_ua ('const_volumes_ua'), the air layer's conductivity is
        set instead so that every stand-in carries its share of the
        unheated room's steady-state heat balance: the shared elements
        (H_iu) in series with the outer elements and the air change
        (H_ue + H_ve, see _unheated_room_ventilation), split over the
        stand-ins as the heat divides at one common temperature of the
        unheated room - over the shared elements by their H_iu, over the
        outer elements by their UA and H_ve. The air change leaves the
        unheated room without passing its envelope, so it gets stand-ins
        of its own: a virtual outer element as large as the shared
        elements, horizontal and without layers, which the heat
        capacities are spread over as well.

        Safe to call more than once for the same zone (e.g. after
        retrofitting the unheated rooms' own envelope elements via
        retrofit_building): existing equivalent elements are found by name
        and rebuilt in place from the current (possibly retrofitted) state
        of the unheated rooms' envelope elements, rather than duplicated.
        """
        existing_by_name = {
            element.name: element
            for element in zone.outer_walls + zone.rooftops + zone.ground_floors
        }
        outer_elements = {_n: _i for _n, _i in self.detailed_geo[room].items() if
                          _i["type"] in ["OuterWall", "Roof", "GroundFloor"]}
        inner_elements = {_n: _i for _n, _i in self.detailed_geo[room].items() if
                          _i["type"] in ["InnerWall", "Ceiling", "Floor"]}
        unheated_tot_outer_area = sum([ele["area"] for ele in outer_elements.values()])
        unheated_tot_inner_area = sum([ele["area"] for ele in inner_elements.values()])
        # The stand-ins share out the unheated room's outer area and volume
        # by its inner elements, which only adds up if each of them is
        # shared with a heated room - as the Attic's floors are.
        shared = {unheated[1] for unheated in adj_ele_heated_to_unheated.values()
                  if unheated[0] == room}
        if set(inner_elements) - shared:
            raise NotImplementedError(
                f"const_volumes needs every inner element of {room} to adjoin "
                f"a heated room, which "
                f"{sorted(set(inner_elements) - shared)} do not.")

        h_outer = {}
        for outer_ele_name, outer_ele_info in outer_elements.items():
            outer_element = self._get_or_create_unheated_envelope_element(
                room, outer_ele_name, outer_ele_info,
            )
            outer_element.calc_ua_value()
            h_outer[outer_ele_name] = outer_element.ua_value
        if fit_ua:
            # The air change bypasses the unheated room's envelope, so it
            # gets a path of its own: a virtual outer element without
            # layers, as large as the shared elements and, like
            # din12831_f1's stand-ins, horizontal.
            outer_elements[_AIR_CHANGE] = {
                "type": "Roof",
                "area": unheated_tot_inner_area,
                "ori": -1,
                "tilt": 0.0,
            }
            h_outer[_AIR_CHANGE] = self._unheated_room_ventilation(room)
            unheated_tot_outer_area += unheated_tot_inner_area
        h_inner = {}

        for heated, unheated in adj_ele_heated_to_unheated.items():
            if unheated[0] != room:
                continue
            ele_info = self.detailed_geo[heated[0]][heated[1]]
            if ele_info["type"] == "Ceiling":
                # the whole ceiling, not just the heated room's half of it
                inner_dummy_element, inner_layers, r_unheated = \
                    self._ceiling_to_unheated_room(ele_info)
            else:
                if ele_info["type"] == "InnerWall":
                    inner_dummy_element = InnerWall(parent=None)
                elif ele_info["type"] == "Floor":
                    inner_dummy_element = Floor(parent=None)
                else:
                    raise ValueError("Element type not recognized")
                inner_dummy_element.element_construction_type = ele_info["element_construction_type"]
                inner_dummy_element.load_type_element(
                    year=self.year_of_construction,
                    construction=self._construction_data.value,
                    data_class=self.data_class,
                )
                inner_layers = inner_dummy_element.layer
                r_unheated = 1 / (inner_dummy_element.inner_convection
                                  + inner_dummy_element.inner_radiation)
            h_inner[heated] = ele_info["area"] / (
                1 / (inner_dummy_element.inner_convection + inner_dummy_element.inner_radiation)
                + sum(layer.thickness / layer.material.thermal_conduc
                      for layer in inner_layers)
                + r_unheated)
            for outer_ele_name, outer_ele_info in outer_elements.items():
                if outer_ele_name == _AIR_CHANGE:
                    outer_element = None
                else:
                    outer_element = self._get_or_create_unheated_envelope_element(
                        room, outer_ele_name, outer_ele_info,
                    )

                # room ("Attic") is included so this can never collide
                # with a heated room's own real element names (e.g.
                # both a heated room and Attic can have an
                # "outside_wall1" key in detailed_geo).
                eq_name = f"{heated[0]}_{room}_{outer_ele_name}"
                outer_equivalent_part_element = existing_by_name.get(eq_name)
                if outer_equivalent_part_element is None:
                    if outer_ele_info["type"] == "OuterWall":
                        outer_equivalent_part_element = OuterWall(parent=zone)
                    elif outer_ele_info["type"] == "GroundFloor":
                        outer_equivalent_part_element = GroundFloor(parent=zone)
                    elif outer_ele_info["type"] == "Roof":
                        outer_equivalent_part_element = Rooftop(parent=zone)
                    else:
                        raise ValueError("Element type not recognized")
                    outer_equivalent_part_element.name = eq_name
                    existing_by_name[eq_name] = outer_equivalent_part_element
                else:
                    outer_equivalent_part_element.layer = None

                eq_area = outer_ele_info["area"] * \
                          ele_info["area"] / \
                          unheated_tot_inner_area
                outer_equivalent_part_element.area = eq_area
                outer_equivalent_part_element.orientation = outer_ele_info["ori"]
                outer_equivalent_part_element.tilt = outer_ele_info["tilt"]
                outer_equivalent_part_element.inner_convection = inner_dummy_element.inner_convection
                outer_equivalent_part_element.inner_radiation = inner_dummy_element.inner_radiation * \
                                                                unheated_tot_inner_area/unheated_tot_outer_area
                if outer_element is None:
                    outer_equivalent_part_element.outer_convection = 20.0
                    outer_equivalent_part_element.outer_radiation = 5.0
                else:
                    outer_equivalent_part_element.outer_convection = outer_element.outer_convection
                    outer_equivalent_part_element.outer_radiation = outer_element.outer_radiation
                for layer in inner_layers:
                    layer = copy.deepcopy(layer)
                    layer.parent = outer_equivalent_part_element
                    layer.thickness = layer.thickness * unheated_tot_inner_area/unheated_tot_outer_area
                air_layer = Layer(parent=outer_equivalent_part_element)
                air_layer.thickness = self.room_volumes[room] / unheated_tot_outer_area
                air_material = Material(parent=air_layer)
                air_material.load_material_template(
                    mat_name="air_layer",
                    data_class=self.data_class,
                )
                outer_layers = [] if outer_element is None else outer_element.layer
                for layer in outer_layers:
                    layer = copy.deepcopy(layer)
                    layer.parent = outer_equivalent_part_element
                outer_equivalent_part_element._fit_ua_share = (heated, outer_ele_name)

        if fit_ua:
            self._fit_const_volumes_ua(zone, room, h_inner, h_outer)

    def _fit_const_volumes_ua(self, zone, room, h_inner, h_outer):
        """Sets the air layers of const_volumes' stand-ins for one
        unheated room so they carry its steady-state heat balance

        See _integrate_unheated_rooms_const_volumes. h_inner holds H_iu of
        each shared element, h_outer the UA of each outer element and H_ve
        of the air change, all in W/K.
        """
        h_iu = sum(h_inner.values())
        h_out = sum(h_outer.values())
        ua_total = 1 / (1 / h_iu + 1 / h_out)
        for element in zone.outer_walls + zone.rooftops + zone.ground_floors:
            share = getattr(element, "_fit_ua_share", None)
            if share is None or share[0] not in h_inner:
                continue
            heated, outer_ele_name = share
            ua_target = ua_total * h_inner[heated] / h_iu * h_outer[outer_ele_name] / h_out
            air_layer = next(layer for layer in element.layer
                             if layer.material.name == "air_layer")
            r_rest = (1 / (element.inner_convection + element.inner_radiation)
                      + 1 / (element.outer_convection + element.outer_radiation)
                      + sum(layer.thickness / layer.material.thermal_conduc
                            for layer in element.layer if layer is not air_layer))
            r_air = element.area / ua_target - r_rest
            if r_air <= 0:
                raise ValueError(
                    f"const_volumes_ua can not fit {element.name}: its layers "
                    f"other than {room}'s air already conduct less than its "
                    f"share of the steady-state heat balance.")
            air_layer.material.thermal_conduc = air_layer.thickness / r_air

    def _unheated_room_heat_transfer_outside(self, room):
        """Heat transfer coefficient [W/K] of an unheated room to outside
        air - DIN EN 12831-1's H_ue plus its air change H_ve

        H_ue sums the UA-values of the room's own envelope (roof, gable
        walls, ...), taken from the persistent, retrofittable unheated-room
        envelope elements, so this reflects any retrofit already applied
        via retrofit_building. H_ve takes attic_air_change_rate, or the
        rate of attic_infiltration_class.
        """
        h_ue = 0.0
        for ele_name, ele_info in self.detailed_geo[room].items():
            if ele_info["type"] not in ("OuterWall", "Roof", "GroundFloor"):
                continue
            element = self._get_or_create_unheated_envelope_element(
                room, ele_name, ele_info,
            )
            element.calc_ua_value()
            h_ue += element.ua_value
        return h_ue + self._unheated_room_ventilation(room)

    def _unheated_room_ventilation(self, room):
        """Heat transfer coefficient [W/K] of an unheated room's air change
        with outside air - DIN EN 12831-1's H_ve

        Takes attic_air_change_rate, or the rate of attic_infiltration_class.
        """
        air_change_rate = self.attic_air_change_rate
        if air_change_rate is None:
            air_change_rate = _ATTIC_AIR_CHANGE_RATES[self.attic_infiltration_class]
        return _RHO_C_AIR * air_change_rate * self.room_volumes[room]

    def _ceiling_to_unheated_room(self, ele_info):
        """The whole ceiling between a heated room below and an unheated
        room above

        For aixlib_* construction data, TypeElements_AixLib.json holds the
        ceiling towards the Attic as its two halves, CeilingAttic (the
        heated room's) and FloorAttic (the Attic's), so the whole ceiling
        is both, the second turned round. Other construction data only has
        the whole construction under Ceiling.

        Returns
        -------
        ceiling : Ceiling
            the heated room's side, for its surface coefficients
        layers : list of Layer
            from the heated room's side to the unheated room's
        r_unheated : float [m2K/W]
            combined surface resistance on the unheated room's side
        """
        ceiling = Ceiling(parent=None)
        ceiling.element_construction_type = ele_info["element_construction_type"]
        ceiling_key = ceiling.load_type_element(
            year=self.year_of_construction,
            construction=self._construction_data.value,
            data_class=self.data_class,
        )
        layers = list(ceiling.layer)
        r_unheated = 1 / (ceiling.inner_convection + ceiling.inner_radiation)
        if (ceiling.element_construction_type is not None and ceiling_key is not None
                and ceiling_key.startswith("Ceiling" + ceiling.element_construction_type)):
            floor = Floor(parent=None)
            floor.element_construction_type = ceiling.element_construction_type
            floor.load_type_element(
                year=self.year_of_construction,
                construction=self._construction_data.value,
                data_class=self.data_class,
            )
            layers += list(reversed(floor.layer))
            r_unheated = 1 / (floor.inner_convection + floor.inner_radiation)
        return ceiling, layers, r_unheated

    def _integrate_unheated_rooms_din12831_f1(self, zone, room, adj_ele_heated_to_unheated):
        """Integrates one unheated room (e.g. the Attic) into the zone by
        DIN EN 12831-1's temperature adjustment factor f1 instead of
        const_volumes' equivalent-resistance network.

        f1 = (H_ue + H_ve) / (H_iu + H_ue + H_ve) comes from the unheated
        room's own steady-state heat balance: H_iu is the ceilings from
        the heated rooms, H_ue its own envelope to outside and H_ve its air
        change (see _unheated_room_heat_transfer_outside). DIN EN 12831-1
        tabulates f1 for a few classes of Uue, Uiu and airtightness
        (Table 5), which leave out e.g. a leaky attic under an insulated
        roof; the heat balance holds for any construction and retrofit.

        Each heated room's real ceiling to the unheated room is replaced
        by a Rooftop element that reuses the whole ceiling's layers plus
        one added resistive layer, sized so the element's U-value equals
        the ceiling's own U-value (Uiu) times f1. t_outside is then applied
        directly across this element - unlike const_volumes, the unheated
        room's own air temperature is never modelled, matching how DIN EN
        12831 itself does not treat the unheated space as its own thermal
        zone.

        Only "Ceiling" adjacency to the unheated room is supported (the
        only kind this archetype's rooms actually have towards the
        Attic). Safe to call more than once for the same zone, same as
        _integrate_unheated_rooms_const_volumes.
        """
        existing_by_name = {element.name: element for element in zone.rooftops}
        ceilings = {}
        for heated, unheated in adj_ele_heated_to_unheated.items():
            if unheated[0] != room:
                continue
            room_name, ele_name = heated
            ele_info = self.detailed_geo[room_name][ele_name]
            if ele_info["type"] != "Ceiling":
                raise ValueError(
                    f"din12831_f1 only supports Ceiling adjacency to an "
                    f"unheated room, got {ele_info['type']!r} for "
                    f"{room_name}.{ele_name}."
                )
            ceiling, layers, r_unheated = self._ceiling_to_unheated_room(ele_info)
            r_heated = 1 / (ceiling.inner_convection + ceiling.inner_radiation)
            r_conduc = sum(layer.thickness / layer.material.thermal_conduc
                           for layer in layers)
            u_iu = 1 / (r_heated + r_conduc + r_unheated)
            ceilings[heated] = (ele_info, ceiling, layers, r_conduc, u_iu)

        h_iu = sum(ele_info["area"] * u_iu
                   for ele_info, _, _, _, u_iu in ceilings.values())
        h_outside = self._unheated_room_heat_transfer_outside(room)
        f1 = h_outside / (h_iu + h_outside)

        for (room_name, ele_name), (ele_info, ceiling, layers, r_conduc, u_iu) \
                in ceilings.items():
            eq_name = f"{room_name}_{room}_{ele_name}"
            element = existing_by_name.get(eq_name)
            if element is None:
                element = Rooftop(parent=zone)
                element.name = eq_name
                existing_by_name[eq_name] = element
            else:
                element.layer = None

            element.area = ele_info["area"]
            element.orientation = ele_info["ori"]
            element.tilt = ele_info["tilt"]
            element.inner_convection = ceiling.inner_convection
            element.inner_radiation = ceiling.inner_radiation
            element.outer_convection = 20.0
            element.outer_radiation = 5.0
            for layer in layers:
                new_layer = copy.deepcopy(layer)
                new_layer.parent = element

            # f1 < 1, so the added resistance is always positive
            r_inner_comb = 1 / (element.inner_convection + element.inner_radiation)
            r_outer_comb = 1 / (element.outer_convection + element.outer_radiation)
            r_extra = 1 / (u_iu * f1) - r_inner_comb - r_conduc - r_outer_comb
            extra_layer = Layer(parent=element)
            extra_material = Material(parent=extra_layer)
            extra_material.load_material_template(
                mat_name="air_layer",
                data_class=self.data_class,
            )
            extra_layer.thickness = r_extra * extra_material.thermal_conduc

    def retrofit_building(
            self,
            year_of_retrofit=None,
            type_of_retrofit=None,
            window_type=None,
            material=None,
    ):
        """Retrofits all zones in the building, and the unheated rooms'
        own envelope elements.

        The Attic (and any other unheated room integrated via
        'const_volumes') has no ThermalZone of its own - only its
        equivalent-resistance stand-ins live in the single heated zone - so
        its real envelope elements would never be retrofitted by the base
        implementation. This override retrofits them directly, then
        rebuilds the zone's equivalent elements from their new state, in
        addition to the normal zone/window/outer-envelope retrofit.

        Parameters are the same as Building.retrofit_building.
        """
        self.sum_heat_load = 0

        if year_of_retrofit is not None:
            self.year_of_retrofit = year_of_retrofit

        for elements in self.unheated_room_envelope_elements.values():
            for element in elements.values():
                element.retrofit_wall(
                    self.year_of_retrofit, material, data_class=self.data_class,
                )

        for zone in self.thermal_zones:
            zone.retrofit_zone(type_of_retrofit, window_type, material)
            adj_ele_heated_to_unheated = self._compute_adjacent_to_unheated(
                self.zoning[zone.name]
            )
            self._integrate_unheated_rooms(zone, adj_ele_heated_to_unheated)

        self.calc_building_parameter(
            number_of_elements=self.number_of_elements_calc,
            merge_windows=self.merge_windows_calc,
            used_library=self.used_library_calc,
        )

    def calc_building_parameter(
            self,
            number_of_elements=None,
            merge_windows=None,
            used_library=None,
    ):
        """Calculates all building parameters, then makes the room-wise
        heat load (calc_room_heat_loads) the authoritative source for
        each zone's heat_load/cool_load and the building's sum_heat_load,
        instead of the zone-level value TwoElement/FourElement compute
        from the zone's single, aggregated t_inside.

        This keeps the two calculations from silently disagreeing once
        rooms have different nominal temperatures (room_t_set_nominal):
        the room-wise sum reflects that (e.g. the bathroom's own, higher
        design temperature), the generic zone-level calculation cannot
        (it only ever sees the zone's one, aggregated t_inside).

        Also caches the room-wise heat loads as room_heat_loads (dict) and
        room_heat_loads_list (list, ordered by room_name_nr) attributes,
        so exports can read them directly instead of calling
        calc_room_heat_loads again.

        Does NOT regenerate the archetype itself - integrate_unheated_rooms,
        t_set_nominal_aggregation and attic_infiltration_class each
        regenerate on assignment (see their setters), and room_t_set_nominal
        needs an explicit generate_archetype() call after editing it
        in-place (same as most other TEASER attributes). This method must
        stay regeneration-free so it can safely be called more than once
        after a retrofit (e.g. by Project.calc_all_buildings) without
        rebuilding fresh, non-retrofitted elements from year_of_construction.

        Parameters are the same as Building.calc_building_parameter.
        """
        self._set_hom_surface_coefficients(
            self.hom_surface_coefficients or (
                self.hom_surface_coefficients is None
                and len(self.thermal_zones) == 1 and not self.use_old))
        super().calc_building_parameter(
            number_of_elements=number_of_elements,
            merge_windows=merge_windows,
            used_library=used_library,
        )
        room_heat_loads = self.calc_room_heat_loads()
        self.room_heat_loads = room_heat_loads
        self.room_heat_loads_list = self._order_by_room_nr(room_heat_loads)
        self.sum_heat_load = 0
        for zone in self.thermal_zones:
            # now that the room-wise heat loads are known
            zone.t_inside = self._aggregate_t_set_nominal(self.zoning[zone.name])
            zone_heat_load = sum(
                room_heat_loads[room] for room in self.zoning[zone.name]
            )
            zone.model_attr.heat_load = zone_heat_load
            zone.model_attr.cool_load = -zone_heat_load
            self.sum_heat_load += zone_heat_load
        self._rotation_at_last_calc = self.rotation
        self.calc_rom_inner_heat_transfer_parameters()

    def _set_hom_surface_coefficients(self, hom_like):
        """Sets the zones' outer surface coefficients up the way the HOM
        handles them, or back to those of the type elements

        AixLib's WindowSimple passes heat through a window by Uw alone,
        straight between outside and room air. The ROM puts a convective
        and a radiative resistance on either side of the glazing instead,
        so its windows lose their heat through the inner surface node. Each
        window therefore gets inner and outer convection so high that they
        drop out, no outer radiation and no convective share of the solar
        gains (a_conv), with its layers scaled so that its total U-value -
        and with it the Uw the HOM is exported with - stays the same.

        The HOM's outer convection coefficients (ASHRAE Fundamentals)
        already cover the long-wave exchange outside, and its walls see no
        sky, so all other outer elements get no outer radiation either,
        which also drops the sky correction from the ROM's equivalent air
        temperature.

        Each element keeps what it had before, so calc_building_parameter
        can switch this on or off on every call - generate_archetype
        calculates the building before use_old or hom_surface_coefficients
        can be changed - and a window a retrofit put in is set up anew.

        Parameters
        ----------
        hom_like : bool
            True sets the coefficients up like the HOM's, False restores
            the elements' own.
        """
        for zone in self.thermal_zones:
            for window in zone.windows:
                original = getattr(window, "_before_hom_surface_coefficients", None)
                if hom_like and original is None:
                    window._before_hom_surface_coefficients = (
                        window.inner_convection, window.outer_convection,
                        window.outer_radiation, window.a_conv,
                        [layer.thickness for layer in window.layer])
                    r_total = sum(layer.thickness / layer.material.thermal_conduc
                                  for layer in window.layer)
                    r_total += 1 / (window.inner_convection + window.inner_radiation)
                    r_total += 1 / (window.outer_convection + window.outer_radiation)
                    window.inner_convection = HOM_WINDOW_CONVECTION
                    window.outer_convection = HOM_WINDOW_CONVECTION
                    window.outer_radiation = HOM_OUTER_RADIATION
                    window.a_conv = 0.0
                    r_layers = (r_total
                                - 1 / (window.inner_convection + window.inner_radiation)
                                - 1 / (window.outer_convection + window.outer_radiation))
                    scale = r_layers / sum(layer.thickness / layer.material.thermal_conduc
                                           for layer in window.layer)
                    for layer in window.layer:
                        layer.thickness *= scale
                elif not hom_like and original is not None:
                    (window.inner_convection, window.outer_convection,
                     window.outer_radiation, window.a_conv, thicknesses) = original
                    for layer, thickness in zip(window.layer, thicknesses):
                        layer.thickness = thickness
                    window._before_hom_surface_coefficients = None
            for element in zone.outer_walls + zone.rooftops + zone.doors:
                original = getattr(element, "_before_hom_surface_coefficients", None)
                if hom_like and original is None:
                    element._before_hom_surface_coefficients = element.outer_radiation
                    element.outer_radiation = HOM_OUTER_RADIATION
                elif not hom_like and original is not None:
                    element.outer_radiation = original
                    element._before_hom_surface_coefficients = None

    def calc_room_heat_loads(self):
        """Simplified, room-wise static heat load for each heated room.

        Uses the same method TEASER already applies at zone level (see
        TwoElement._calc_heat_load): UA-value of the envelope times the
        nominal indoor/outdoor (and ground) temperature difference, plus
        infiltration - just evaluated per room instead of aggregated over
        the whole (single, merged) zone. Room elements are found by name
        (every element and window created for a room is named
        "{room_name}_...", see generate_archetype), so this also picks up
        a room's share of the unheated-room equivalent elements (e.g. its
        connection to the Attic via its ceiling), since those are named
        after the heated room they belong to.

        Includes transmission and infiltration to the outside/ground, plus
        transmission exchange with other heated rooms in the same zone via
        the room's own InnerWall/Ceiling/Floor elements (DIN 12831-style:
        each such element's own ua_value times the difference between the
        two rooms' nominal temperatures - positive if the neighbor is
        colder, negative i.e. a net gain if it is warmer). Elements
        adjacent to an unheated room (e.g. the Attic) are excluded here -
        those are already covered via ua_value_outside, since the
        unheated-room integration methods replace them with equivalent
        elements facing outside directly. Each room uses its own nominal
        temperature (room_t_set_nominal) rather than the zone's single
        t_inside, so e.g. the bathroom's higher design temperature is
        reflected. Since zone.t_inside is itself the aggregate (see
        t_set_nominal_aggregation) of these per-room values, the sum of
        this method's results will generally not equal the zone-level
        heat_load computed from t_inside alone - see
        calc_building_parameter, which uses this method's sum as the
        zone's authoritative heat_load instead. Room-to-room exchange
        terms cancel out of that zone-level sum (room i's gain from room j
        is room j's equal and opposite loss to room i), so adding them
        here does not change the zone/building total, only how it is
        distributed between rooms.

        Call this before and after retrofit_building to get the room heat
        loads for both states - element ua_values (and therefore the
        result) reflect whatever retrofit has already been applied.

        Must be called after the zone's parameters have been calculated at
        least once (e.g. via calc_building_parameter/calc_all_buildings),
        same prerequisite as the zone-level heat_load.

        Returns
        -------
        room_heat_loads : dict
            {room_name: heat_load [W]} for every heated room.
        """
        zone = self.thermal_zones[0]
        use_cond = zone.use_conditions

        if zone.parent.parent.t_soil_mode == 2:
            t_ground = zone.t_ground - zone.t_ground_amplitude
        else:
            t_ground = zone.t_ground

        inner_elements_by_name = {
            ele.name: ele
            for ele in zone.inner_walls + zone.floors + zone.ceilings
        }

        room_heat_loads = {}
        for room_names in self.zoning.values():
            for room_name in room_names:
                prefix = f"{room_name}_"
                ua_value_outside = sum(
                    ele.ua_value for ele in zone.outer_walls + zone.rooftops
                    if ele.name.startswith(prefix)
                ) + sum(
                    win.ua_value for win in zone.windows
                    if win.name.startswith(prefix)
                )
                ua_value_ground = sum(
                    ele.ua_value for ele in zone.ground_floors
                    if ele.name.startswith(prefix)
                )

                heat_load_outside_factor = (
                    ua_value_outside
                    + self.room_volumes[room_name]
                    * use_cond.normative_infiltration
                    / 3600
                    * zone.heat_capac_air
                    * zone.density_air
                )
                heat_load_ground_factor = ua_value_ground

                t_set_nominal_room = self.room_t_set_nominal[room_name]

                room_to_room_exchange = 0.0
                for ele_name, ele_info in self.detailed_geo[room_name].items():
                    adjacent_room, _ = ele_info.get("adjacent", (None, None))
                    if adjacent_room is None or adjacent_room in self.integrate_unheated_rooms:
                        continue
                    ele = inner_elements_by_name.get(f"{prefix}{ele_name}")
                    if ele is None:
                        continue
                    room_to_room_exchange += ele.ua_value * (
                        t_set_nominal_room - self.room_t_set_nominal[adjacent_room]
                    )

                room_heat_loads[room_name] = (
                    heat_load_outside_factor * (t_set_nominal_room - zone.t_outside)
                    + heat_load_ground_factor * (t_set_nominal_room - t_ground)
                    + room_to_room_exchange
                )

        return room_heat_loads

    def calc_room_heat_loads_list(self):
        """Room-wise heat loads as a list, ordered by room_name_nr (1..10).

        Convenience wrapper around calc_room_heat_loads for use in
        Modelica array parameters (e.g. QRooms_flow_nominal), where rooms
        are referenced by their fixed room_name_nr index rather than by
        name. Same call-before/after-retrofit usage as
        calc_room_heat_loads.

        Returns
        -------
        room_heat_loads : list of float
            Heat load [W] of each room, room_heat_loads[0] is the room
            with room_name_nr 1, room_heat_loads[-1] the room with
            room_name_nr 10 (== len(room_name_nr)).
        """
        return self._order_by_room_nr(self.calc_room_heat_loads())

    def _order_by_room_nr(self, room_values):
        """Reorders a dict keyed by room_name into a list ordered by
        room_name_nr (1..10), e.g. for Modelica array parameters.
        """
        rooms_by_nr = sorted(self.room_name_nr, key=self.room_name_nr.get)
        return [room_values[room] for room in rooms_by_nr]

    @property
    def room_t_set_nominal_list(self):
        """room_t_set_nominal as a list ordered by room_name_nr (1..10),
        e.g. for a Modelica array parameter - the room-wise counterpart to
        the single, aggregated t_inside used at zone level.

        Unlike room_heat_loads_list, this does not depend on the zone's
        calculated elements and needs no prior calc_building_parameter
        call: it is always a direct, live view of room_t_set_nominal, so
        overriding individual rooms there is reflected immediately.
        """
        return self._order_by_room_nr(self.room_t_set_nominal)

    def _room_weights(self, weighting, attribute_name):
        """Resolves one of the fac_room_* weightings (see
        fac_room_t_set_weighting) into a list of weights ordered by
        room_name_nr (1..10) and normalized to sum to 1.

        Parameters
        ----------
        weighting : str or dict or callable
            The weighting to resolve - "volume", "heat_load", "equal", a
            {room_name: weight} dict, or a callable taking (self) and
            returning such a dict.

        attribute_name : str
            Name of the attribute the weighting came from, only used to
            point at it in error messages.

        Returns
        -------
        weights : list of float
            Weight of each room, summing to 1. weights[0] is the room with
            room_name_nr 1, weights[-1] the room with room_name_nr 10.
        """
        if callable(weighting):
            weights = weighting(self)
        elif isinstance(weighting, dict):
            weights = weighting
        elif weighting == "volume":
            # room_volumes also holds the unheated rooms (e.g. the Attic),
            # which have no room_name_nr and no profile column - taking the
            # heated rooms by name here drops them.
            weights = {room: self.room_volumes[room] for room in self.room_name_nr}
        elif weighting == "heat_load":
            if not self.room_heat_loads:
                raise ValueError(
                    f"{attribute_name}='heat_load' needs the room-wise heat "
                    f"loads of building {self.name!r}, which are only "
                    f"available once its parameters have been calculated. "
                    f"Call calc_building_parameter() (or the project's "
                    f"calc_all_buildings()) first."
                )
            weights = self.room_heat_loads
        elif weighting == "equal":
            weights = {room: 1.0 for room in self.room_name_nr}
        else:
            raise ValueError(
                f"Unknown {attribute_name} {weighting!r}. Use 'volume', "
                f"'heat_load', 'equal', a dict of per-room weights or a "
                f"callable."
            )

        missing = set(self.room_name_nr) - set(weights)
        if missing:
            raise ValueError(
                f"{attribute_name} is missing a weight for "
                f"{sorted(missing)}. Every heated room needs one."
            )
        weights = self._order_by_room_nr(weights)
        # A negative weight has no meaning in a weighted average of
        # temperatures or air exchange rates, and would silently distort
        # the result rather than fail, so reject it here.
        if any(weight < 0 for weight in weights):
            raise ValueError(
                f"{attribute_name} contains a negative weight: {weights}."
            )
        total = sum(weights)
        if total == 0:
            raise ValueError(
                f"{attribute_name} weights sum to zero, so they cannot be "
                f"normalized to a weighted average."
            )
        return [weight / total for weight in weights]

    @property
    def fac_room_t_set(self):
        """Weights reducing the room-wise set temperature profiles to the
        single ROM zone's setpoint, ordered by room_name_nr (1..10) and
        normalized to sum to 1 - facRoomTSet of BESMod's TEASERHOMtoROM.

        Controlled by fac_room_t_set_weighting ("volume" by default, see
        there for the other options, e.g. "heat_load").
        """
        return self._room_weights(
            self.fac_room_t_set_weighting, "fac_room_t_set_weighting")

    @property
    def fac_room_nat_vent(self):
        """Weights reducing the room-wise natural ventilation profiles to
        the single ROM zone's air exchange rate, ordered by room_name_nr
        (1..10) and normalized to sum to 1 - facRoomNatVent of BESMod's
        TEASERHOMtoROM.

        Controlled by fac_room_nat_vent_weighting, which defaults to
        "volume": an air exchange rate is per unit of room volume, so
        volume weights are the aggregation that conserves the merged zone's
        total ventilation air flow. Changing this is possible (same options
        as fac_room_t_set_weighting) but will not conserve it.
        """
        return self._room_weights(
            self.fac_room_nat_vent_weighting, "fac_room_nat_vent_weighting")

    @property
    def construction_data(self):
        return self._construction_data

    @construction_data.setter
    def construction_data(self, value):
        self._construction_data = datahandling.check_construction_data_setter_tabula_de(value)

    @property
    def number_of_floors(self):
        return 2

    @number_of_floors.setter
    def number_of_floors(self, value):
        if value is not None:
            warnings.warn("`number_of_floors` for AixLibHighOrderSingleFamilyHouse is fixed to 2 "
                          "and cannot be changed.", UserWarning)

    @property
    def inner_wall_approximation_approach(self):
        return self._inner_wall_approximation_approach

    @inner_wall_approximation_approach.setter
    def inner_wall_approximation_approach(self, value):
        if value != 'teaser_default':
            warnings.warn("`inner_wall_approximation_approach` has no effect for"
                          " AixLibHighOrderSingleFamilyHouse", UserWarning)
        self._inner_wall_approximation_approach = 'detailed'

    @property
    def integrate_unheated_rooms(self):
        return self._integrate_unheated_rooms_config

    @integrate_unheated_rooms.setter
    def integrate_unheated_rooms(self, value):
        # Backing field is NOT named _integrate_unheated_rooms - that name
        # is already the dispatcher method (see below); reusing it here
        # would shadow the method with this dict.
        self._integrate_unheated_rooms_config = value
        if getattr(self, "_initialized", False):
            self.generate_archetype()

    @property
    def t_set_nominal_aggregation(self):
        return self._t_set_nominal_aggregation

    @t_set_nominal_aggregation.setter
    def t_set_nominal_aggregation(self, value):
        self._t_set_nominal_aggregation = value
        if getattr(self, "_initialized", False):
            self.generate_archetype()

    @property
    def attic_air_change_rate(self):
        return self._attic_air_change_rate

    @attic_air_change_rate.setter
    def attic_air_change_rate(self, value):
        self._attic_air_change_rate = value
        if getattr(self, "_initialized", False):
            self.generate_archetype()

    @property
    def roof_tilt(self):
        return self._roof_tilt

    @roof_tilt.setter
    def roof_tilt(self, value):
        value = float(value)
        if not 0 < value < 90:
            raise ValueError(f"roof_tilt has to be between 0 and 90 deg, got {value}.")
        self._roof_tilt = value
        if getattr(self, "_initialized", False):
            self.generate_archetype()

    @property
    def attic_infiltration_class(self):
        return self._attic_infiltration_class

    @attic_infiltration_class.setter
    def attic_infiltration_class(self, value):
        self._attic_infiltration_class = value
        if getattr(self, "_initialized", False):
            self.generate_archetype()
