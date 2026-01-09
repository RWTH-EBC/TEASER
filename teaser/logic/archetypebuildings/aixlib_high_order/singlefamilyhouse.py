import warnings
import teaser.data.utilities as datahandling
from teaser.logic.archetypebuildings.residential import Residential
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


class AixLibHighOrderSingleFamilyHouse(Residential):
    def __init__(
            self,
            parent=None,
            name=None,
            year_of_construction=None,
            height_of_floors=2.6,
            net_leased_area=170,
            construction_data=None
    ):
        super(AixLibHighOrderSingleFamilyHouse, self).__init__(
            parent,
            name,
            year_of_construction,
            net_leased_area,
        )
        self.construction_data = construction_data
        self.height_of_floors = height_of_floors

        if self.construction_data.is_tabula_de() or self.construction_data.is_tabula_dk():
            self._construction_data_1 = self.construction_data.value + "_1_SFH"
        else:
            self._construction_data_1 = self.construction_data.value

        self.number_of_floors = 2
        self._wall_types = ['OW', 'roof', 'roof_attic', 'IW_vert_half', 'IW_hori_upHalf', 'IW_hori_loHalf',
                            'ground_floor_loHalf',
                            'ground_floor_upHalf', 'IW_hori_att_upHalf', 'IW_hori_att_loHalf']
        self._hom_dim_parameters = {}
        self._original_hom_dim_parameters = {
            "thickness_iw_simple": 0.145,
            "l1": 3.3,
            "l2": 2.44,
            "l3": 1.33,
            "l4": 3.3,
            "room_width": 3.92,
            "room_height": 2.6,
            "windowarea_11": 8.44,
            "window_11_orientation": 180,
            "windowarea_12": 1.73,
            "windowarea_22": 1.73,
            "windowarea_41": 1.4,
            "windowarea_51": 3.46,
            "windowarea_52": 1.73,
            "width_door_31": 1.01,
            "height_door_31": 2.25,
            "width_door_42": 1.25,
            "height_door_42": 2.25,
            "heigth_dwarf_wall": 1,
            "room_ceiling_attic_width": 2.28,
            "room_roof_length": 2.21,
            "windowarea_62": 1.73,
            "windowarea_63": 1.73,
            "windowarea_72": 1.73,
            "windowarea_73": 1.73,
            "windowarea_92": 1.73,
            "windowarea_102": 1.73,
            "windowarea_103": 1.73,
            "alfa_grad": 90,
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
            "Bathroom": 9,
            "Children2": 10,
        }
        self.top_level_geo_params = {}
        self.scale_building_geometry()

        self.element_orientations = {
        # "attic_2Ro_5Rooms.roof1": ("North", 0.0, "Roof"),
        "upperFloor_Building.Children1.roof": ("North", 0.0, "Roof"),
        "upperFloor_Building.Children1.outside_wall1": ("North", 0.0, "OuterWall"),
        "upperFloor_Building.Corridor.roof": ("North", 0.0, "Roof"),
        "upperFloor_Building.Corridor.outside_wall1": ("North", 0.0, "OuterWall"),
        "upperFloor_Building.Bath.roof": ("North", 0.0, "Roof"),
        "upperFloor_Building.Bath.outside_wall1": ("North", 0.0, "OuterWall"),
        "groundFloor_Building.Hobby.outside_wall1": ("North", 0.0, "OuterWall"),
        "groundFloor_Building.WC_Storage.outside_wall1": ("North", 0.0, "OuterWall"),
        "groundFloor_Building.Corridor.outside_wall1": ("North", 0.0, "OuterWall"),

        # "attic_2Ro_5Rooms.OW1": ("East", 90.0, "OuterWall"),
        "upperFloor_Building.Children2.outside_wall2": ("East", 90.0, "OuterWall"),
        "upperFloor_Building.Bath.outside_wall2": ("East", 90.0, "OuterWall"),
        "groundFloor_Building.Kitchen.outside_wall2": ("East", 90.0, "OuterWall"),
        "groundFloor_Building.WC_Storage.outside_wall2": ("East", 90.0, "OuterWall"),

        # "attic_2Ro_5Rooms.roof2": ("South", 180.0, "Roof"),
        "upperFloor_Building.Bedroom.roof": ("South", 180.0, "Roof"),
        "upperFloor_Building.Bedroom.outside_wall1": ("South", 180.0, "OuterWall"),
        "upperFloor_Building.Children2.roof": ("South", 180.0, "Roof"),
        "upperFloor_Building.Children2.outside_wall1": ("South", 180.0, "OuterWall"),
        "groundFloor_Building.Livingroom.outside_wall1": ("South", 180.0, "OuterWall"),
        "groundFloor_Building.Kitchen.outside_wall1": ("South", 180.0, "OuterWall"),

        # "attic_2Ro_5Rooms.OW2": ("West", 270.0, "OuterWall"),
        "upperFloor_Building.Bedroom.outside_wall2": ("West", 270.0, "OuterWall"),
        "upperFloor_Building.Children1.outside_wall2": ("West", 270.0, "OuterWall"),
        "groundFloor_Building.Livingroom.outside_wall2": ("West", 270.0, "OuterWall"),
        "groundFloor_Building.Hobby.outside_wall2": ("West", 270.0, "OuterWall")
        }
        self.attic_outer = {
        "attic_2Ro_5Rooms.roof1": ("North", 0.0, "Roof"),
        "attic_2Ro_5Rooms.OW1": ("East", 90.0, "OuterWall"),
        "attic_2Ro_5Rooms.roof2": ("South", 180.0, "Roof"),
        "attic_2Ro_5Rooms.OW2": ("West", 270.0, "OuterWall"),
        }

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
        l2 = bldg_length * og_dim["l2"]/ og_dim["bldg_inner_length"]
        l3 = bldg_length * og_dim["l3"] / og_dim["bldg_inner_length"]
        l4 = bldg_length * og_dim["l4"] / og_dim["bldg_inner_length"]

        self.top_level_geo_params["l1"] = l1
        self.top_level_geo_params["l2"] = l2
        self.top_level_geo_params["l3"] = l3
        self.top_level_geo_params["l4"] = l4

        thickness_iw_simple = 0.145
        self.top_level_geo_params["thickness_iw_simple"] = thickness_iw_simple
        room1_length = l1 + l2 + thickness_iw_simple
        room3_length = l2 + l3
        room5_length = l3 + l4 + thickness_iw_simple

        self.top_level_geo_params["room1_length"] = room1_length
        self.top_level_geo_params["room3_length"] = room3_length
        self.top_level_geo_params["room5_length"] = room5_length

        roof_length = bldg_length + 2 * thickness_iw_simple  # inner wall thicknesses load simpled?
        self.top_level_geo_params["roof_length"] = roof_length

        alfa_grad = 90  # maybe test 110 for 35 roof_tilt
        roof_tilt = (180 - alfa_grad) / 2
        self.top_level_geo_params["roof_tilt"] = roof_tilt
        self.top_level_geo_params["alfa_grad"] = alfa_grad
        height_of_floors = self.height_of_floors
        self.top_level_geo_params["height_of_floors"] = height_of_floors
        room_height_short = 1  # here fixed
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

        windowarea_11 = 8.44 * room1_length / 5.885
        windowarea_12 = 1.73 * room_width / 3.92
        windowarea_22 = 1.73 * roof_width / 3.92
        windowarea_41 = 1.4 * l4 / 3.3
        windowarea_51 = 3.46 * room5_length / 4.775
        windowarea_52 = 1.73 * room_width / 3.92

        self.top_level_geo_params["windowarea_11"] = windowarea_11
        self.top_level_geo_params["windowarea_12"] = windowarea_12
        self.top_level_geo_params["windowarea_22"] = windowarea_22
        self.top_level_geo_params["windowarea_41"] = windowarea_41
        self.top_level_geo_params["windowarea_51"] = windowarea_51
        self.top_level_geo_params["windowarea_52"] = windowarea_52

        windowarea_i_up_roof = 1.73 * room_width_short / 2.28
        windowarea_i_up_wall = 1.73 * bldg_length / og_dim["bldg_inner_length"]
        self.top_level_geo_params["windowarea_i_up_roof"] = windowarea_i_up_roof
        self.top_level_geo_params["windowarea_i_up_wall"] = windowarea_i_up_wall
        return self.top_level_geo_params

    def generate_archetype(self):
        """Generates a SingleFamilyHouse archetype buildings

        With given values, this function generates an archetype building for
        AixLib HOM Single Family House.
        """
        self.thermal_zones = None
        zone = ThermalZone(parent=self)
        zone.name = "single_zone_building"
        zone.area = self.net_leased_area
        zone.number_of_floors = self.number_of_floors
        zone.height_of_floors = self.height_of_floors
        zone.volume = self.net_leased_area * self.height_of_floors
        use_cond = UseCond(parent=zone)
        use_cond.load_use_conditions(zone_usage="Living")  # create use conditions for single rooms
        zone.use_conditions = use_cond
        zone.use_conditions.with_ahu = False

        outer_wall = OuterWall(zone)
        outer_wall.load_type_element(
            year=self.year_of_construction,
            construction=self._construction_data_1,
            data_class=self.parent.data
        )
        outer_wall.name = "dummy_outer_wall" # LivingRoom outside_wall2 West
        outer_wall.tilt = 90
        outer_wall.orientation = 270
        outer_wall.area = (self.top_level_geo_params["room1_length"]*self.top_level_geo_params["height_of_floors"] -
                           self.top_level_geo_params["windowarea_11"])

        window = Window(zone)
        construction = (
            "Waermeschutzverglasung, dreifach"
            if self.construction_data.is_kfw()
            else self._construction_data_1
        )
        window.load_type_element(
            self.year_of_construction,
            construction=construction,
            data_class=self.parent.data,
        )
        window.name = "dummy_window"  # LivingRoom window11 West
        window.tilt = 90
        window.orientation = 270
        window.area = self.top_level_geo_params["windowarea_11"]

        gf = GroundFloor(zone)
        gf.load_type_element(
            year=self.year_of_construction,
            construction=self._construction_data_1,
            data_class=self.parent.data
        )
        gf.name = "dummy_ground_floor" # LivingRoom ground_floor
        gf.tilt = 0
        gf.orientation = -2
        gf.area = self.top_level_geo_params["room1_length"] * self.top_level_geo_params["room_width"]

        rt = Rooftop(zone)
        rt.load_type_element(
            year=self.year_of_construction,
            construction=self._construction_data_1,
            data_class=self.parent.data
        )
        rt.name = "dummy_rooftop"  # Bedroom roof
        rt.tilt = self.top_level_geo_params["roof_tilt"]
        rt.orientation = 180
        rt.area = (self.top_level_geo_params["room1_length"] * self.top_level_geo_params["wRO"] -
                   self.top_level_geo_params["windowarea_i_up_roof"])

        rt_attic = Rooftop(zone)
        rt_attic.element_construction_type = "Attic"
        rt_attic.load_type_element(
            year=self.year_of_construction,
            construction=self._construction_data_1,
            data_class=self.parent.data
        )
        rt_attic.name = "dummy_rooftop_attic"  # attic_2Ro_5Rooms.roof1
        rt_attic.tilt = self.top_level_geo_params["roof_tilt"]
        rt_attic.orientation = 0
        rt_attic.area = (self.top_level_geo_params["roof_length"] * self.top_level_geo_params["wROi"])

        inner_wall = InnerWall(zone)
        inner_wall.load_type_element(
            year=self.year_of_construction,
            construction=self.construction_data.value,
            data_class=self.parent.data
        )
        inner_wall.name = "dummy_inner_wall"  # LivingRoom IW_simple to Kitchen
        inner_wall.tilt = 90
        inner_wall.orientation = 90
        inner_wall.area = (self.top_level_geo_params["room_width"] *
                           self.top_level_geo_params["height_of_floors"])

        inner_wall_load = InnerWall(zone)
        inner_wall_load.element_construction_type = "LoadBearing"
        inner_wall_load.load_type_element(
            year=self.year_of_construction,
            construction=self.construction_data.value,
            data_class=self.parent.data
        )
        inner_wall_load.name = "dummy_inner_wall_load"  # LivingRoom IW_loadBearing to hobby
        inner_wall_load.tilt = 90
        inner_wall_load.orientation = 180
        inner_wall_load.area = (self.top_level_geo_params["l1"] *
                                self.top_level_geo_params["height_of_floors"])

        ceiling = Ceiling(zone)
        ceiling.load_type_element(
            year=self.year_of_construction,
            construction=self.construction_data.value,
            data_class=self.parent.data
        )
        ceiling.name = "dummy_ceiling"  # LivingRoom ceiling
        ceiling.tilt = 0
        ceiling.orientation = -1
        ceiling.area = (self.top_level_geo_params["room1_length"] *
                        self.top_level_geo_params["room_width"])

        ceiling_attic = Ceiling(zone)
        ceiling_attic.element_construction_type = "Attic"
        ceiling_attic.load_type_element(
            year=self.year_of_construction,
            construction=self.construction_data.value,
            data_class=self.parent.data
        )
        ceiling_attic.name = "dummy_ceiling_attic"  # Bedroom ceiling_attic
        ceiling_attic.tilt = 0
        ceiling_attic.orientation = -1
        ceiling_attic.area = (self.top_level_geo_params["room1_length"] *
                             self.top_level_geo_params["room_width_short"])

        floor = Floor(zone)
        floor.load_type_element(
            year=self.year_of_construction,
            construction=self.construction_data.value,
            data_class=self.parent.data
        )
        floor.name = "dummy_floor"  # Bedroom floor
        floor.tilt = 0
        floor.orientation = -2
        floor.area = (self.top_level_geo_params["room1_length"] *
                        self.top_level_geo_params["room_width"])

        floor_attic = Floor(zone)   # attic_2Ro_5Rooms
        floor_attic.element_construction_type = "Attic"
        floor_attic.load_type_element(
            year=self.year_of_construction,
            construction=self.construction_data.value,
            data_class=self.parent.data
        )
        floor_attic.name = "dummy_floor_attic"  # attic_2Ro_5Rooms floor
        floor_attic.tilt = 0
        floor_attic.orientation = -2
        floor_attic.area = (self.top_level_geo_params["roof_length"] *
                            self.top_level_geo_params["roof_width"])

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
