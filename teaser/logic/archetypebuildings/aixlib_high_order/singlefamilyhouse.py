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
from math import sin, cos, tan, pi, sqrt


def _check_number_of_floors(room_names: list, room_floor: dict):
    floor_names = []
    for room_name in room_names:
        floor_names.append(room_floor[room_name])
    return len(set(floor_names))


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
        self.construction_data = construction_data
        self.height_of_floors = height_of_floors

        if self.construction_data.is_tabula_de() or self.construction_data.is_tabula_dk():
            self.construction_data_1 = self.construction_data.value + "_1_SFH"
        else:
            self.construction_data_1 = self.construction_data.value

        # only single zone roms
        self.integrate_unheated_rooms_integration_methods = [
            "const_volumes",
            # "inner_heated_as_outer_no_sun",
        ]
        self.integrate_unheated_rooms = {"Attic": "const_volumes"}

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
            "alfa_grad": 90,  # ToDo: maybe test 110 for 35 roof_tilt make changeable
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
        self.top_level_geo_params = {}
        self.detailed_geo = {}
        self.room_volumes = {}
        # Persistent, retrofittable elements for unheated rooms' own
        # envelope (e.g. the Attic's roof/gable walls). These are not part
        # of any ThermalZone (the ROM only has the single heated zone), so
        # they would never be touched by retrofit otherwise. Structure:
        # {unheated_room_name: {element_name: BuildingElement}}
        self.unheated_room_envelope_elements = {}

    def update_calc_original_hom_dim_parameters(self):
        def_params = self._original_hom_dim_parameters.copy()
        self._original_hom_dim_parameters["bldg_inner_width"] = 2 * def_params["room_width"]
        self._original_hom_dim_parameters["bldg_inner_length"] = (def_params["l1"] + def_params["l2"] +
                                                                  def_params["l3"] + def_params["l4"])
        self._original_hom_dim_parameters["room1_length"] = (def_params["l1"] + def_params["l2"] +
                                                             def_params["thickness_iw_simple"])
        self._original_hom_dim_parameters["room3_length"] = def_params["l2"] + def_params["l3"]
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

        net_leased_area = self.net_leased_area

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
        room3_length = l2 + l3
        room5_length = l3 + l4 + thickness_iw_simple

        self.top_level_geo_params["room1_length"] = room1_length
        self.top_level_geo_params["room3_length"] = room3_length
        self.top_level_geo_params["room5_length"] = room5_length

        roof_length = bldg_length + 2 * thickness_iw_simple  # inner wall thicknesses load simpled?
        self.top_level_geo_params["roof_length"] = roof_length

        alfa_grad = og_dim["alfa_grad"]
        roof_tilt = (180 - alfa_grad) / 2
        self.top_level_geo_params["roof_tilt"] = roof_tilt
        self.top_level_geo_params["alfa_grad"] = alfa_grad
        height_of_floors = self.height_of_floors
        self.top_level_geo_params["height_of_floors"] = height_of_floors
        room_height_short = og_dim["height_dwarf_wall"]
        room_width_short = room_width - (height_of_floors - room_height_short) / tan(roof_tilt * pi / 180)
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
                    "area": (self.top_level_geo_params["room3_length"] - self.top_level_geo_params["l4"]) *
                            self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Livingroom", "inside_wall1b")
                },
                "inside_wall2b": {
                    "ori": 90,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l4"] * self.top_level_geo_params["height_of_floors"],
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
                    "area": (self.top_level_geo_params["room3_length"] - self.top_level_geo_params["l4"]) *
                            self.top_level_geo_params["height_of_floors"],
                    "type": "InnerWall",
                    "element_construction_type": "LoadBearing",
                    "adjacent": ("Bedroom", "inside_wall1b")
                },
                "inside_wall2b": {
                    "ori": 90,
                    "tilt": 90,
                    "area": self.top_level_geo_params["l4"] * self.top_level_geo_params["height_of_floors"],
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
        """(Re)builds the zone's equivalent-resistance elements that
        integrate unheated rooms (e.g. the Attic) into the single heated
        zone, following the 'const_volumes' method.

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
        for room, method in self.integrate_unheated_rooms.items():
            if method != "const_volumes":
                continue
            outer_elements = {_n: _i for _n, _i in self.detailed_geo[room].items() if
                              _i["type"] in ["OuterWall", "Roof", "GroundFloor"]}
            inner_elements = {_n: _i for _n, _i in self.detailed_geo[room].items() if
                              _i["type"] in ["InnerWall", "Ceiling", "Floor"]}
            unheated_tot_outer_area = sum([ele["area"] for ele in outer_elements.values()])
            unheated_tot_inner_area = sum([ele["area"] for ele in inner_elements.values()])

            for heated, unheated in adj_ele_heated_to_unheated.items():
                if unheated[0] != room:
                    continue
                ele_info = self.detailed_geo[heated[0]][heated[1]]
                if ele_info["type"] == "InnerWall":
                    inner_dummy_element = InnerWall(parent=None)
                elif ele_info["type"] == "Floor":
                    inner_dummy_element = Floor(parent=None)
                elif ele_info["type"] == "Ceiling":
                    inner_dummy_element = Ceiling(parent=None)
                else:
                    raise ValueError("Element type not recognized")
                inner_dummy_element.element_construction_type = ele_info["element_construction_type"]
                inner_dummy_element.load_type_element(
                    year=self.year_of_construction,
                    construction=self._construction_data.value,
                    data_class=self.data_class,
                )
                for outer_ele_name, outer_ele_info in outer_elements.items():
                    outer_element = self._get_or_create_unheated_envelope_element(
                        room, outer_ele_name, outer_ele_info,
                    )

                    eq_name = f"{heated[0]}_{outer_ele_name}"
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
                              unheated_tot_inner_area  # maybe unheated_to_heated_tot_inner_area
                    outer_equivalent_part_element.area = eq_area
                    outer_equivalent_part_element.orientation = outer_ele_info["ori"]
                    outer_equivalent_part_element.tilt = outer_ele_info["tilt"]
                    outer_equivalent_part_element.inner_convection = inner_dummy_element.inner_convection
                    outer_equivalent_part_element.outer_convection = outer_element.outer_convection
                    outer_equivalent_part_element.inner_radiation = inner_dummy_element.inner_radiation * \
                                                                    unheated_tot_inner_area/unheated_tot_outer_area
                    outer_equivalent_part_element.outer_radiation = outer_element.outer_radiation
                    inner_layers = inner_dummy_element.layer
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
                    outer_layers = outer_element.layer
                    for layer in outer_layers:
                        layer = copy.deepcopy(layer)
                        layer.parent = outer_equivalent_part_element

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
