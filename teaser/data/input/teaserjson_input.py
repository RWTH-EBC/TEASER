"""Load Projects in the proprietary TEASER file format .json."""

from teaser.logic.buildingobjects.building import Building
from teaser.logic.archetypebuildings.tabula.de.apartmentblock import ApartmentBlock
from teaser.logic.archetypebuildings.tabula.de.multifamilyhouse import MultiFamilyHouse
from teaser.logic.archetypebuildings.tabula.de.singlefamilyhouse import (
    SingleFamilyHouse,
)
from teaser.logic.archetypebuildings.tabula.de.terracedhouse import TerracedHouse
from teaser.logic.archetypebuildings.bmvbs.office import Office
from teaser.logic.archetypebuildings.bmvbs.singlefamilydwelling import (
    SingleFamilyDwelling,
)
from teaser.logic.archetypebuildings.bmvbs.custom.institute import Institute
from teaser.logic.archetypebuildings.bmvbs.custom.institute4 import Institute4
from teaser.logic.archetypebuildings.bmvbs.custom.institute8 import Institute8
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.buildingsystems.buildingahu import BuildingAHU
from teaser.logic.buildingobjects.useconditions import UseConditions
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.buildingphysics.door import Door
import json
import collections


def load_teaser_json(path, project):
    """Load a project from json.

    TEASERs internal file format to store information.

    Parameters
    ----------
    path: string
        path of teaserjson file

    project: Project()
        Teaser instance of Project()


    """
    __building_class = {
        "Office": {"method": "bmvbs", "teaser_class": Office},
        "Institute": {"method": "bmvbs", "teaser_class": Institute},
        "Institute4": {"method": "bmvbs", "teaser_class": Institute4},
        "Institute8": {"method": "bmvbs", "teaser_class": Institute8},
        "Building": {"method": "undefined", "teaser_class": Building},
        "SingleFamilyDwelling": {"method": "iwu", "teaser_class": SingleFamilyDwelling},
        "SingleFamilyHouse": {"method": "tabula_de", "teaser_class": SingleFamilyHouse},
        "TerracedHouse": {"method": "tabula_de", "teaser_class": TerracedHouse},
        "MultiFamilyHouse": {"method": "tabula_de", "teaser_class": MultiFamilyHouse},
        "ApartmentBlock": {"method": "tabula_de", "teaser_class": ApartmentBlock},
    }
    with open(path, "r+") as f:
        prj_in = json.load(f, object_pairs_hook=collections.OrderedDict)

    project.name = prj_in["project"]["name"]
    project.weather_file_path = prj_in["project"]["weather_file_path"]
    project.number_of_elements_calc = prj_in["project"]["number_of_elements_calc"]
    project.merge_windows_calc = prj_in["project"]["merge_windows_calc"]
    project.used_library_calc = prj_in["project"]["used_library_calc"]
    project.modelica_info.start_time = prj_in["project"]["modelica_info"]["start_time"]
    project.modelica_info.stop_time = prj_in["project"]["modelica_info"]["stop_time"]
    project.modelica_info.interval_output = prj_in["project"]["modelica_info"][
        "interval_output"
    ]
    project.modelica_info.current_solver = prj_in["project"]["modelica_info"][
        "current_solver"
    ]
    project.modelica_info.equidistant_output = prj_in["project"]["modelica_info"][
        "equidistant_output"
    ]
    project.modelica_info.results_at_events = prj_in["project"]["modelica_info"][
        "results_at_events"
    ]
    project.modelica_info.version = prj_in["project"]["modelica_info"]["version"]

    for bldg_name, bldg_in in prj_in["project"]["buildings"].items():
        bl_class = __building_class[bldg_in["classification"]["class"]]["teaser_class"]
        bldg = bl_class(parent=project)
        bldg.name = bldg_name
        bldg.street_name = bldg_in["street_name"]
        bldg.city = bldg_in["city"]
        bldg.year_of_construction = bldg_in["year_of_construction"]
        bldg.year_of_retrofit = bldg_in["year_of_retrofit"]
        bldg.number_of_floors = bldg_in["number_of_floors"]
        bldg.height_of_floors = bldg_in["height_of_floors"]
        # bldg.net_leased_area = bldg_in["net_leased_area"]
        bldg.outer_area = bldg_in["outer_area"]
        bldg.window_area = bldg_in["window_area"]

        try:
            bldg.central_ahu = BuildingAHU(parent=bldg)
            bldg.central_ahu.heating = bldg_in["central_ahu"]["heating"]
            bldg.central_ahu.cooling = bldg_in["central_ahu"]["cooling"]
            bldg.central_ahu.dehumidification = bldg_in["central_ahu"][
                "dehumidification"
            ]
            bldg.central_ahu.humidification = bldg_in["central_ahu"]["humidification"]
            bldg.central_ahu.heat_recovery = bldg_in["central_ahu"]["heat_recovery"]
            bldg.central_ahu.by_pass_dehumidification = bldg_in["central_ahu"][
                "by_pass_dehumidification"
            ]
            bldg.central_ahu.efficiency_recovery = bldg_in["central_ahu"][
                "efficiency_recovery"
            ]
            bldg.central_ahu.efficiency_recovery_false = bldg_in["central_ahu"][
                "efficiency_recovery_false"
            ]
            bldg.central_ahu.min_relative_humidity_profile = bldg_in["central_ahu"][
                "min_relative_humidity_profile"
            ]
            bldg.central_ahu.max_relative_humidity_profile = bldg_in["central_ahu"][
                "max_relative_humidity_profile"
            ]
            bldg.central_ahu.v_flow_profile = bldg_in["central_ahu"]["v_flow_profile"]
            bldg.central_ahu.temperature_profile = bldg_in["central_ahu"][
                "temperature_profile"
            ]
        except KeyError:
            pass

        for tz_name, zone_in in bldg_in["thermal_zones"].items():
            tz = ThermalZone(parent=bldg)
            tz.name = tz_name
            tz.area = zone_in["area"]
            tz.volume = zone_in["volume"]
            tz.use_conditions = UseConditions(parent=tz)
            tz.use_conditions.usage = zone_in["use_conditions"]["usage"]
            tz.use_conditions.typical_length = zone_in["use_conditions"][
                "typical_length"
            ]
            tz.use_conditions.typical_width = zone_in["use_conditions"]["typical_width"]
            tz.use_conditions.with_heating = zone_in["use_conditions"]["with_heating"]
            tz.use_conditions.with_cooling = zone_in["use_conditions"]["with_cooling"]
            tz.use_conditions.with_ideal_thresholds = zone_in["use_conditions"][
                "with_ideal_thresholds"
            ]
            tz.use_conditions.T_threshold_heating = zone_in["use_conditions"][
                "T_threshold_heating"
            ]
            tz.use_conditions.T_threshold_cooling = zone_in["use_conditions"][
                "T_threshold_cooling"
            ]
            tz.use_conditions.fixed_heat_flow_rate_persons = zone_in["use_conditions"][
                "fixed_heat_flow_rate_persons"
            ]
            tz.use_conditions.activity_degree_persons = zone_in["use_conditions"][
                "activity_degree_persons"
            ]
            tz.use_conditions.persons = zone_in["use_conditions"]["persons"]
            tz.use_conditions.internal_gains_moisture_no_people = zone_in[
                "use_conditions"
            ]["internal_gains_moisture_no_people"]
            tz.use_conditions.ratio_conv_rad_persons = zone_in["use_conditions"][
                "ratio_conv_rad_persons"
            ]
            tz.use_conditions.machines = zone_in["use_conditions"]["machines"]
            tz.use_conditions.ratio_conv_rad_machines = zone_in["use_conditions"][
                "ratio_conv_rad_machines"
            ]
            tz.use_conditions.lighting_power = zone_in["use_conditions"][
                "lighting_power"
            ]
            tz.use_conditions.ratio_conv_rad_lighting = zone_in["use_conditions"][
                "ratio_conv_rad_lighting"
            ]
            tz.use_conditions.use_constant_infiltration = zone_in["use_conditions"][
                "use_constant_infiltration"
            ]
            tz.use_conditions.infiltration_rate = zone_in["use_conditions"][
                "infiltration_rate"
            ]
            tz.use_conditions.max_user_infiltration = zone_in["use_conditions"][
                "max_user_infiltration"
            ]
            tz.use_conditions.max_overheating_infiltration = zone_in["use_conditions"][
                "max_overheating_infiltration"
            ]
            tz.use_conditions.max_summer_infiltration = zone_in["use_conditions"][
                "max_summer_infiltration"
            ]
            tz.use_conditions.winter_reduction_infiltration = zone_in["use_conditions"][
                "winter_reduction_infiltration"
            ]
            tz.use_conditions.min_ahu = zone_in["use_conditions"]["min_ahu"]
            tz.use_conditions.max_ahu = zone_in["use_conditions"]["max_ahu"]
            tz.use_conditions.with_ahu = zone_in["use_conditions"]["with_ahu"]
            tz.use_conditions.heating_profile = zone_in["use_conditions"][
                "heating_profile"
            ]
            tz.use_conditions.cooling_profile = zone_in["use_conditions"][
                "cooling_profile"
            ]
            tz.use_conditions.persons_profile = zone_in["use_conditions"][
                "persons_profile"
            ]
            tz.use_conditions.machines_profile = zone_in["use_conditions"][
                "machines_profile"
            ]
            tz.use_conditions.lighting_profile = zone_in["use_conditions"][
                "lighting_profile"
            ]

            for wall_name, wall_in in zone_in["outer_walls"].items():
                out_wall = OuterWall(parent=tz)
                out_wall.name = wall_name
                set_basic_data_teaser(wall_in, out_wall)
                set_layer_data_teaser(wall_in, out_wall)
            for door_name, door_in in zone_in["doors"].items():
                door = Door(parent=tz)
                door.name = door_name
                set_basic_data_teaser(door_in, door)
                set_layer_data_teaser(door_in, door)
            for roof_name, roof_in in zone_in["rooftops"].items():
                roof = Rooftop(parent=tz)
                roof.name = roof_name
                set_basic_data_teaser(roof_in, roof)
                set_layer_data_teaser(roof_in, roof)
            for gf_name, gf_in in zone_in["ground_floors"].items():
                gf = GroundFloor(parent=tz)
                gf.name = gf_name
                set_basic_data_teaser(gf_in, gf)
                set_layer_data_teaser(gf_in, gf)
            for win_name, win_in in zone_in["windows"].items():
                win = Window(parent=tz)
                win.name = win_name
                set_basic_data_teaser(win_in, win)
                set_layer_data_teaser(win_in, win)
            for iw_name, iw_in in zone_in["inner_walls"].items():
                in_wall = InnerWall(parent=tz)
                in_wall.name = iw_name
                set_basic_data_teaser(iw_in, in_wall)
                set_layer_data_teaser(iw_in, in_wall)
            for fl_name, fl_in in zone_in["floors"].items():
                floor = Floor(parent=tz)
                floor.name = fl_name
                set_basic_data_teaser(fl_in, floor)
                set_layer_data_teaser(fl_in, floor)
            for cl_name, cl_in in zone_in["ceilings"].items():
                ceil = Ceiling(parent=tz)
                ceil.name = cl_name
                set_basic_data_teaser(cl_in, ceil)
                set_layer_data_teaser(cl_in, ceil)


def set_basic_data_teaser(wall_in, element):
    """Set basic data for a building element.

    Helper function.

    Parameters
    ----------
    wall_in : collection.OrderedDict
        OrderedDict for walls
    element : TEASERClass
        teaser class representation of a building element

    """
    element.area = wall_in["area"]
    element.tilt = wall_in["tilt"]
    element.orientation = wall_in["orientation"]
    element.inner_radiation = wall_in["inner_radiation"]
    element.inner_convection = wall_in["inner_convection"]
    element.year_of_construction = wall_in["year_of_construction"]
    element.year_of_retrofit = wall_in["year_of_retrofit"]
    element.construction_type = wall_in["construction_type"]

    if (
        type(element).__name__ == "OuterWall"
        or type(element).__name__ == "Rooftop"
        or type(element).__name__ == "Door"
    ):

        element.outer_radiation = wall_in["outer_radiation"]
        element.outer_convection = wall_in["outer_convection"]

    elif type(element).__name__ == "Window":

        element.outer_radiation = wall_in["outer_radiation"]
        element.outer_convection = wall_in["outer_convection"]
        element.g_value = wall_in["g_value"]
        element.a_conv = wall_in["a_conv"]
        element.shading_g_total = wall_in["shading_g_total"]
        element.shading_max_irr = wall_in["shading_max_irr"]


def set_layer_data_teaser(wall_in, element):
    """Set layer data of a building element.

    Helper function.

    Parameters
    ----------
    wall_in : collection.OrderedDict
        OrderedDict for walls
    element : TEASERClass
        teaser class representation of a building element

    """
    for lay_id, layer_in in wall_in["layer"].items():
        layer = Layer(element)

        layer.id = int(lay_id)
        layer.thickness = layer_in["thickness"]

        Material(layer)

        layer.material.name = layer_in["material"]["name"]
        layer.material.density = layer_in["material"]["density"]
        layer.material.thermal_conduc = layer_in["material"]["thermal_conduc"]
        layer.material.heat_capac = layer_in["material"]["heat_capac"]
        layer.material.solar_absorp = layer_in["material"]["solar_absorp"]
        layer.material.ir_emissivity = layer_in["material"]["ir_emissivity"]
