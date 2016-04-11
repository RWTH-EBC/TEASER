# Created July 2015
# TEASER 4 Development Team

"""TeaserXML

This module contains function to save and load Projects in the proprietary
TEASER file format .tXML
"""


import teaser.Data.SchemaBindings.ProjectBind as pb

import teaser.Logic.Utilis as utilis

from teaser.Logic.BuildingObjects.Building import Building
from teaser.Logic.BuildingObjects.TypeBuildings.Office import Office
from teaser.Logic.BuildingObjects.TypeBuildings.Institute import Institute
from teaser.Logic.BuildingObjects.TypeBuildings.Institute4 import Institute4
from teaser.Logic.BuildingObjects.TypeBuildings.Institute8 import Institute8
from teaser.Logic.BuildingObjects.TypeBuildings.Residential import Residential
from teaser.Logic.BuildingObjects.ThermalZone import ThermalZone
from teaser.Logic.BuildingObjects.BuildingSystems.BuildingAHU import BuildingAHU
from teaser.Logic.BuildingObjects.TypeBuildings.UseConditions18599 import \
    UseConditions18599
from teaser.Logic.BuildingObjects.BuildingPhysics.OuterWall import OuterWall
from teaser.Logic.BuildingObjects.BuildingPhysics.Layer import Layer
from teaser.Logic.BuildingObjects.BuildingPhysics.Material import Material
from teaser.Logic.BuildingObjects.BuildingPhysics.Rooftop import Rooftop
from teaser.Logic.BuildingObjects.BuildingPhysics.GroundFloor import \
    GroundFloor
from teaser.Logic.BuildingObjects.BuildingPhysics.InnerWall import InnerWall
from teaser.Logic.BuildingObjects.BuildingPhysics.Ceiling import Ceiling
from teaser.Logic.BuildingObjects.BuildingPhysics.Floor import Floor
from teaser.Logic.BuildingObjects.BuildingPhysics.Window import Window


def save_teaser_xml(path, project):
    '''This function saves a project to a tXML

    The function needs the Python Package PyXB.

    Parameters
    ----------
    path: string
        complete path to the output file
    project: Project()
        Teaser instance of Project()
    '''
    if path.endswith("teaserXML"):
        new_path = path
    else:
        new_path = path + ".teaserXML"
    out_file = open(new_path, 'w')

    teaser_out = pb.Project()

    for bldg in project.list_of_buildings:

        if type(bldg).__name__ == "Building":

            pyxb_bld = pb.BuildingType()

        elif type(bldg).__name__ == "Office":
            pyxb_bld = pb.OfficeType()

        elif type(bldg).__name__ == "Institute":
            pyxb_bld = pb.InstituteType()

        elif type(bldg).__name__ == "Institute4":
            pyxb_bld = pb.Institute4Type()

        elif type(bldg).__name__ == "Institute8":
            pyxb_bld = pb.Institute8Type()

        elif type(bldg).__name__ == "Residential":

            pyxb_bld = pb.ResidentialType()

        pyxb_bld.name = bldg.name
        pyxb_bld.street_name = bldg.street_name
        pyxb_bld.city = bldg.city
        pyxb_bld.type_of_building = bldg.type_of_building
        pyxb_bld.year_of_construction = str(bldg.year_of_construction)
        pyxb_bld.year_of_retrofit = str(bldg.year_of_retrofit)
        pyxb_bld.number_of_floors = bldg.number_of_floors
        pyxb_bld.height_of_floors = bldg.height_of_floors
        pyxb_bld.net_leased_area = bldg.net_leased_area
        # pyxb_bld.outer_area = bldg.outer_area
        # pyxb_bld.window_area = bldg.window_area
        if bldg.central_ahu is not None:
            pyxb_ahu = pb.BuildingAHUType()
            pyxb_ahu.heating = bldg.central_ahu.heating
            pyxb_ahu.cooling = bldg.central_ahu.cooling
            pyxb_ahu.dehumidification = bldg.central_ahu.dehumidification
            pyxb_ahu.humidification = bldg.central_ahu.humidification
            pyxb_ahu.heat_recovery = bldg.central_ahu.heat_recovery
            pyxb_ahu.by_pass_dehumidification = \
                                bldg.central_ahu.by_pass_dehumidification
            pyxb_ahu.efficiency_recovery = bldg.central_ahu.efficiency_recovery
            pyxb_ahu.efficiency_revocery_false = \
                                bldg.central_ahu.efficiency_revocery_false
            pyxb_ahu.profile_min_relative_humidity = \
                                bldg.central_ahu.profile_min_relative_humidity
            pyxb_ahu.profile_max_relative_humidity = \
                                bldg.central_ahu.profile_max_relative_humidity
            pyxb_ahu.profile_v_flow = \
                                bldg.central_ahu.profile_v_flow
            pyxb_ahu.profile_temperature = \
                                bldg.central_ahu.profile_temperature
            pyxb_bld.CentralAHU = pyxb_ahu
        else:
            pass

        for zone in bldg.thermal_zones:

            pyxb_zone = pb.ThermalZoneType()

            pyxb_zone.name = zone.name
            pyxb_zone.area = zone.area
            pyxb_zone.volume = zone.volume
            pyxb_zone.infiltration_rate = zone.infiltration_rate
            pyxb_zone.typical_length = zone.use_conditions.typical_length
            pyxb_zone.typical_width = zone.use_conditions.typical_width

            pyxb_zone.UseCondition = pb.UseConditionType()

            pyxb_use = pb.UseConditions18599Type()

            pyxb_use.usage = zone.use_conditions.usage
            pyxb_use.UsageOperationTime = pb.UsageOperationTimeType()
            pyxb_use.UsageOperationTime.usage_time = \
                zone.use_conditions.usage_time
            pyxb_use.UsageOperationTime.daily_usage_hours = \
                zone.use_conditions.daily_usage_hours
            pyxb_use.UsageOperationTime.yearly_usage_days = \
                zone.use_conditions.yearly_usage_days
            pyxb_use.UsageOperationTime.yearly_usage_hours_day = \
                zone.use_conditions.yearly_usage_hours_day
            pyxb_use.UsageOperationTime.yearly_usage_hours_night = \
                zone.use_conditions.yearly_usage_hours_night
            pyxb_use.UsageOperationTime.daily_operation_ahu_cooling = \
                zone.use_conditions.daily_operation_ahu_cooling
            pyxb_use.UsageOperationTime.yearly_heating_days = \
                zone.use_conditions.yearly_heating_days
            pyxb_use.UsageOperationTime.yearly_ahu_days = \
                zone.use_conditions.yearly_ahu_days
            pyxb_use.UsageOperationTime.yearly_cooling_days = \
                zone.use_conditions.yearly_cooling_days
            pyxb_use.UsageOperationTime.daily_operation_heating = \
                zone.use_conditions.daily_operation_heating

            pyxb_use.Lighting = pb.LightingType()
            pyxb_use.Lighting.maintained_illuminace = \
                zone.use_conditions.maintained_illuminace
            pyxb_use.Lighting.usage_level_height = \
                zone.use_conditions.usage_level_height
            pyxb_use.Lighting.red_factor_visual = \
                zone.use_conditions.red_factor_visual
            pyxb_use.Lighting.rel_absence = \
                zone.use_conditions.rel_absence
            pyxb_use.Lighting.room_index = \
                zone.use_conditions.room_index
            pyxb_use.Lighting.part_load_factor_lighting = \
                zone.use_conditions.part_load_factor_lighting
            pyxb_use.Lighting.ratio_conv_rad_lighting = \
                zone.use_conditions.ratio_conv_rad_lighting

            pyxb_use.RoomClimate = pb.RoomClimateType()
            pyxb_use.RoomClimate.set_temp_heat = \
                zone.use_conditions.set_temp_heat
            pyxb_use.RoomClimate.set_temp_cool = \
                zone.use_conditions.set_temp_cool
            pyxb_use.RoomClimate.temp_set_back = \
                zone.use_conditions.temp_set_back
            pyxb_use.RoomClimate.min_temp_heat = \
                zone.use_conditions.min_temp_heat
            pyxb_use.RoomClimate.max_temp_cool = \
                zone.use_conditions.max_temp_cool
            pyxb_use.RoomClimate.rel_humidity = \
                zone.use_conditions.rel_humidity
            pyxb_use.RoomClimate.cooling_time = \
                zone.use_conditions.cooling_time
            pyxb_use.RoomClimate.heating_time = \
                zone.use_conditions.heating_time
            pyxb_use.RoomClimate.min_air_exchange = \
                zone.use_conditions.min_air_exchange
            pyxb_use.RoomClimate.rel_absence_ahu = \
                zone.use_conditions.rel_absence_ahu
            pyxb_use.RoomClimate.part_load_factor_ahu = \
                zone.use_conditions.part_load_factor_ahu

            pyxb_use.InternalGains = pb.InternalGainsType()
            pyxb_use.InternalGains.persons = \
                zone.use_conditions.persons
            pyxb_use.InternalGains.profile_persons = \
                zone.use_conditions.profile_persons
            pyxb_use.InternalGains.machines = \
                zone.use_conditions.machines
            pyxb_use.InternalGains.profile_machines = \
                zone.use_conditions.profile_machines
            pyxb_use.InternalGains.lighting_power = \
                zone.use_conditions.lighting_power
            pyxb_use.InternalGains.profile_lighting = \
                zone.use_conditions.profile_lighting

            pyxb_use.AHU = pb.AHUType()
            pyxb_use.AHU.min_ahu = \
                zone.use_conditions.min_ahu
            pyxb_use.AHU.max_ahu = \
                zone.use_conditions.max_ahu
            pyxb_use.AHU.with_ahu = \
                zone.use_conditions.with_ahu
            pyxb_use.AHU.use_constant_ach_rate = \
                zone.use_conditions.use_constant_ach_rate
            pyxb_use.AHU.base_ach = \
                zone.use_conditions.base_ach
            pyxb_use.AHU.max_user_ach = \
                zone.use_conditions.max_user_ach
            pyxb_use.AHU.max_overheating_ach = \
                zone.use_conditions.max_overheating_ach
            pyxb_use.AHU.max_summer_ach = \
                zone.use_conditions.max_summer_ach
            pyxb_use.AHU.winter_reduction = \
                zone.use_conditions.winter_reduction

            pyxb_zone.UseCondition.UseConditions18599 = pyxb_use

            for out_wall in zone.outer_walls:

                if type(out_wall).__name__ == "OuterWall":

                    pyxb_wall = pb.OuterWallType()

                    set_basic_data_pyxb(pyxb_wall, out_wall)
                    set_layer_data_pyxb(pyxb_wall, out_wall)

                    pyxb_zone.OuterWall.append(pyxb_wall)

                if type(out_wall).__name__ == "Rooftop":

                    pyxb_wall = pb.RooftopType()

                    set_basic_data_pyxb(pyxb_wall, out_wall)
                    set_layer_data_pyxb(pyxb_wall, out_wall)

                    pyxb_zone.Rooftop.append(pyxb_wall)

                if type(out_wall).__name__ == "GroundFloor":

                    pyxb_wall = pb.GroundFloorType()

                    set_basic_data_pyxb(pyxb_wall, out_wall)
                    set_layer_data_pyxb(pyxb_wall, out_wall)

                    pyxb_zone.GroundFloor.append(pyxb_wall)

            for in_wall in zone.inner_walls:

                if type(in_wall).__name__ == "InnerWall":

                    pyxb_wall = pb.InnerWallType()

                    set_basic_data_pyxb(pyxb_wall, in_wall)
                    set_layer_data_pyxb(pyxb_wall, in_wall)

                    pyxb_zone.InnerWall.append(pyxb_wall)

                if type(in_wall).__name__ == "Ceiling":

                    pyxb_wall = pb.CeilingType()

                    set_basic_data_pyxb(pyxb_wall, in_wall)
                    set_layer_data_pyxb(pyxb_wall, in_wall)

                    pyxb_zone.Ceiling.append(pyxb_wall)

                if type(in_wall).__name__ == "Floor":

                    pyxb_wall = pb.FloorType()

                    set_basic_data_pyxb(pyxb_wall, in_wall)
                    set_layer_data_pyxb(pyxb_wall, in_wall)

                    pyxb_zone.Floor.append(pyxb_wall)

            for win in zone.windows:

                if type(win).__name__ == "Window":

                    pyxb_win = pb.WindowType()

                    set_basic_data_pyxb(pyxb_win, win)
                    set_layer_data_pyxb(pyxb_win, win)

                    pyxb_zone.Window.append(pyxb_win)

            pyxb_bld.ThermalZone.append(pyxb_zone)

        if type(bldg).__name__ == "Building":
            teaser_out.Building.append(pyxb_bld)
        elif type(bldg).__name__ == "Office":
            teaser_out.Office.append(pyxb_bld)
        elif type(bldg).__name__ == "Institute":
            teaser_out.Institute.append(pyxb_bld)
        elif type(bldg).__name__ == "Institute4":
            teaser_out.Institute4.append(pyxb_bld)
        elif type(bldg).__name__ == "Institute8":
            teaser_out.Institute8.append(pyxb_bld)
        elif type(bldg).__name__ == "Residential":
            teaser_out.Residential.append(pyxb_bld)

    out_file.write(teaser_out.toDOM().toprettyxml())


def set_basic_data_pyxb(pyxb_class, element):
    '''Helper function for save_teaser_xml to set the basic data

    Parameters
    ----------
    pyxb_class : PyXBClass
        pyxb class represantation of xml

    element : TEASERClass
        teaser class representation of a building element


    '''
    if type(element).__name__ == 'OuterWall' or \
            type(element).__name__ == 'Rooftop':

        pyxb_class.year_of_construction = element.year_of_construction
        pyxb_class.year_of_retrofit = element.year_of_retrofit
        pyxb_class.construction_type = element.construction_type

        pyxb_class.area = element.area
        pyxb_class.tilt = element.tilt
        pyxb_class.orientation = element.orientation

        pyxb_class.inner_radiation = element.inner_radiation
        pyxb_class.inner_convection = element.inner_convection
        pyxb_class.outer_radiation = element.outer_radiation
        pyxb_class.outer_convection = element.outer_convection

    elif type(element).__name__ == 'InnerWall' or \
            type(element).__name__ == 'Ceiling' or \
            type(element).__name__ == 'Floor' or \
            type(element).__name__ == 'GroundFloor':

        pyxb_class.year_of_construction = element.year_of_construction
        pyxb_class.year_of_retrofit = element.year_of_retrofit
        pyxb_class.construction_type = element.construction_type

        pyxb_class.area = element.area
        pyxb_class.tilt = element.tilt
        pyxb_class.orientation = element.orientation

        pyxb_class.inner_radiation = element.inner_radiation
        pyxb_class.inner_convection = element.inner_convection

    elif type(element).__name__ == 'Window':

        pyxb_class.year_of_construction = element.year_of_construction
        pyxb_class.year_of_retrofit = element.year_of_retrofit
        pyxb_class.construction_type = element.construction_type

        pyxb_class.area = element.area
        pyxb_class.tilt = element.tilt
        pyxb_class.orientation = element.orientation

        pyxb_class.inner_radiation = element.inner_radiation
        pyxb_class.inner_convection = element.inner_convection
        pyxb_class.outer_radiation = element.outer_radiation
        pyxb_class.outer_convection = element.outer_convection
        pyxb_class.g_Value = element.g_value
        pyxb_class.a_conv = element.a_conv
        pyxb_class.shading_g_total = element.shading_g_total
        pyxb_class.shading_max_irr = element.shading_max_irr


def set_layer_data_pyxb(pyxb_class, element):
    '''Helper function for save_teaser_xml to set the layer data

    Parameters
    ----------
    pyxb_class : PyXBClass
        pyxb class represantation of xml

    element : TEASERClass
        teaser class representation of a building element

    '''
    for layer in element.layer:

        pyxb_layer = pb.LayerType()

        pyxb_layer.id = layer.id
        pyxb_layer.thickness = layer.thickness

        pyxb_material = pb.MaterialType()

        pyxb_material.name = layer.material.name
        pyxb_material.density = layer.material.density
        pyxb_material.thermal_conduc = layer.material.thermal_conduc
        pyxb_material.heat_capac = layer.material.heat_capac
        pyxb_material.solar_absorp = layer.material.solar_absorp
        pyxb_material.ir_emissivity = layer.material.ir_emissivity

        pyxb_layer.Material = pyxb_material

        pyxb_class.Layer.append(pyxb_layer)


def load_teaser_xml(path, prj):
    '''This function loads a project from new teaserXML

    Parameters
    ----------
    path: string
        path of teaserXML file

    project: Project()
        Teaser instance of Project()


    '''

    xml_file = open(path, 'r')
    project_bind = pb.CreateFromDocument(xml_file.read())

    for pyxb_bld in project_bind.Building:
        _load_building(prj=prj, pyxb_bld=pyxb_bld, type="Building")
    for pyxb_bld in project_bind.Office:
        _load_building(prj=prj, pyxb_bld=pyxb_bld, type="Office")

    for pyxb_bld in project_bind.Institute:
        _load_building(prj=prj, pyxb_bld=pyxb_bld, type="Institute")

    for pyxb_bld in project_bind.Institute4:
        _load_building(prj=prj, pyxb_bld=pyxb_bld, type="Institute4")

    for pyxb_bld in project_bind.Institute8:
        _load_building(prj=prj, pyxb_bld=pyxb_bld, type="Institute8")

    for pyxb_bld in project_bind.Residential:
        _load_building(prj=prj, pyxb_bld=pyxb_bld, type="Residential")



def _load_building(prj, pyxb_bld, type):

    if type == "Building":
        bldg = Building(prj)

    elif type == "Office":
        bldg = Office(prj)

    elif type == "Institute":

        bldg = Institute(prj)

    elif type == "Institute4":
        bldg = Institute4(prj)

    elif type == "Institute8":
        bldg = Institute8(prj)

    elif type == "Residential":
        bldg = Residential(prj)

    bldg.name = pyxb_bld.name
    bldg.street_name = pyxb_bld.street_name
    bldg.city = pyxb_bld.city
    bldg.type_of_building = pyxb_bld.type_of_building
    bldg.year_of_construction = pyxb_bld.year_of_construction
    bldg.year_of_retrofit = pyxb_bld.year_of_retrofit
    bldg.number_of_floors = pyxb_bld.number_of_floors
    bldg.height_of_floors = pyxb_bld.height_of_floors

    if not pyxb_bld.ThermalZone:
        bldg.net_leased_area = pyxb_bld.net_leased_area

    if pyxb_bld.CentralAHU:
        pyxb_ahu = pyxb_bld.CentralAHU
        bldg.central_ahu = BuildingAHU(bldg)

        bldg.central_ahu.heating = pyxb_ahu.heating
        bldg.central_ahu.cooling = pyxb_ahu.cooling
        bldg.central_ahu.dehumidification = pyxb_ahu.dehumidification
        bldg.central_ahu.humidification = pyxb_ahu.humidification
        bldg.central_ahu.heat_recovery = pyxb_ahu.heat_recovery
        bldg.central_ahu.by_pass_dehumidification = \
                            pyxb_ahu.by_pass_dehumidification
        bldg.central_ahu.efficiency_recovery =pyxb_ahu.efficiency_recovery
        bldg.central_ahu.efficiency_revocery_false = \
                            pyxb_ahu.efficiency_revocery_false
        bldg.central_ahu.profile_min_relative_humidity = \
                            pyxb_ahu.profile_min_relative_humidity
        bldg.central_ahu.profile_max_relative_humidity = \
                            pyxb_ahu.profile_max_relative_humidity
        bldg.central_ahu.profile_v_flow = \
                            pyxb_ahu.profile_v_flow
        bldg.central_ahu.profile_temperature = \
                            pyxb_ahu.profile_temperature

    for pyxb_zone in pyxb_bld.ThermalZone:

        zone = ThermalZone(bldg)

        zone.name = pyxb_zone.name
        zone.area = pyxb_zone.area
        zone.volume = pyxb_zone.volume
        zone.infiltration_rate = pyxb_zone.infiltration_rate
        # zone.use_conditions.typical_length = pyxb_zone.typical_length
        # zone.use_conditions.typical_width = pyxb_zone.typical_width

        zone.use_conditions = UseConditions18599(zone)

        pyxb_use = pyxb_zone.UseCondition.UseConditions18599

        zone.use_conditions.usage = \
            pyxb_use.usage

        zone.use_conditions.usage_time = \
            pyxb_use.UsageOperationTime.usage_time
        zone.use_conditions.daily_usage_hours = \
            pyxb_use.UsageOperationTime.daily_usage_hours
        zone.use_conditions.yearly_usage_days = \
            pyxb_use.UsageOperationTime.yearly_usage_days
        zone.use_conditions.yearly_usage_hours_day = \
            pyxb_use.UsageOperationTime.yearly_usage_hours_day
        zone.use_conditions.yearly_usage_hours_night = \
            pyxb_use.UsageOperationTime.yearly_usage_hours_night
        zone.use_conditions.daily_operation_ahu_cooling = \
            pyxb_use.UsageOperationTime.daily_operation_ahu_cooling
        zone.use_conditions.yearly_heating_days = \
            pyxb_use.UsageOperationTime.yearly_heating_days
        zone.use_conditions.yearly_ahu_days = \
            pyxb_use.UsageOperationTime.yearly_ahu_days
        zone.use_conditions.yearly_cooling_days = \
            pyxb_use.UsageOperationTime.yearly_cooling_days
        zone.use_conditions.daily_operation_heating = \
            pyxb_use.UsageOperationTime.daily_operation_heating

        zone.use_conditions.maintained_illuminace = \
            pyxb_use.Lighting.maintained_illuminace
        zone.use_conditions.usage_level_height = \
            pyxb_use.Lighting.usage_level_height
        zone.use_conditions.red_factor_visual = \
            pyxb_use.Lighting.red_factor_visual
        zone.use_conditions.rel_absence = \
            pyxb_use.Lighting.rel_absence
        zone.use_conditions.room_index = \
            pyxb_use.Lighting.room_index
        zone.use_conditions.part_load_factor_lighting = \
            pyxb_use.Lighting.part_load_factor_lighting
        zone.use_conditions.ratio_conv_rad_lighting = \
            pyxb_use.Lighting.ratio_conv_rad_lighting

        zone.use_conditions.set_temp_heat = \
            pyxb_use.RoomClimate.set_temp_heat
        zone.use_conditions.set_temp_cool = \
            pyxb_use.RoomClimate.set_temp_cool
        zone.use_conditions.temp_set_back = \
            pyxb_use.RoomClimate.temp_set_back
        zone.use_conditions.min_temp_heat = \
            pyxb_use.RoomClimate.min_temp_heat
        zone.use_conditions.max_temp_cool = \
            pyxb_use.RoomClimate.max_temp_cool
        zone.use_conditions.rel_humidity = \
            pyxb_use.RoomClimate.rel_humidity
        zone.use_conditions.cooling_time = \
            pyxb_use.RoomClimate.cooling_time
        zone.use_conditions.heating_time = \
            pyxb_use.RoomClimate.heating_time
        zone.use_conditions.min_air_exchange = \
            pyxb_use.RoomClimate.min_air_exchange
        zone.use_conditions.rel_absence_ahu = \
            pyxb_use.RoomClimate.rel_absence_ahu
        zone.use_conditions.part_load_factor_ahu = \
            pyxb_use.RoomClimate.part_load_factor_ahu

        zone.use_conditions.persons = \
            pyxb_use.InternalGains.persons
        zone.use_conditions.profile_persons = \
            pyxb_use.InternalGains.profile_persons
        zone.use_conditions.machines = \
            pyxb_use.InternalGains.machines
        zone.use_conditions.profile_machines = \
            pyxb_use.InternalGains.profile_machines
        zone.use_conditions.lighting_power = \
            pyxb_use.InternalGains.lighting_power
        zone.use_conditions.profile_lighting = \
            pyxb_use.InternalGains.profile_lighting

        zone.use_conditions.min_ahu = \
            pyxb_use.AHU.min_ahu
        zone.use_conditions.max_ahu = \
            pyxb_use.AHU.max_ahu
        zone.use_conditions.with_ahu = \
            pyxb_use.AHU.with_ahu
        zone.use_constant_ach_rate = \
            pyxb_use.AHU.use_constant_ach_rate
        zone.base_ach = \
            pyxb_use.AHU.base_ach
        zone.max_user_ach = \
            pyxb_use.AHU.max_user_ach
        zone.max_overheating_ach = \
            pyxb_use.AHU.max_overheating_ach
        zone.max_summer_ach = \
            pyxb_use.AHU.max_summer_ach
        zone.winter_reduction = \
            pyxb_use.AHU.winter_reduction

        for pyxb_wall in pyxb_zone.OuterWall:

            out_wall = OuterWall(zone)

            set_basic_data_teaser(pyxb_wall, out_wall)
            set_layer_data_teaser(pyxb_wall, out_wall)

            # zone.outer_walls.append(out_wall)

        for pyxb_wall in pyxb_zone.Rooftop:

            roof = Rooftop(zone)

            set_basic_data_teaser(pyxb_wall, roof)
            set_layer_data_teaser(pyxb_wall, roof)

            # zone.outer_walls.append(roof)

        for pyxb_wall in pyxb_zone.GroundFloor:

            gr_floor = GroundFloor(zone)

            set_basic_data_teaser(pyxb_wall, gr_floor)
            set_layer_data_teaser(pyxb_wall, gr_floor)

            # zone.outer_walls.append(gr_floor)

        for pyxb_wall in pyxb_zone.InnerWall:

            in_wall = InnerWall(zone)

            set_basic_data_teaser(pyxb_wall, in_wall)
            set_layer_data_teaser(pyxb_wall, in_wall)

            # zone.inner_walls.append(in_wall)

        for pyxb_wall in pyxb_zone.Ceiling:

            ceiling = Ceiling(zone)

            set_basic_data_teaser(pyxb_wall, ceiling)
            set_layer_data_teaser(pyxb_wall, ceiling)

            # zone.inner_walls.append(ceiling)

        for pyxb_wall in pyxb_zone.Floor:

            floor = Floor(zone)

            set_basic_data_teaser(pyxb_wall, floor)
            set_layer_data_teaser(pyxb_wall, floor)

            # zone.inner_walls.append(floor)

        for pyxb_win in pyxb_zone.Window:

            win = Window(zone)

            set_basic_data_teaser(pyxb_win, win)
            set_layer_data_teaser(pyxb_win, win)


def set_basic_data_teaser(pyxb_class, element):
    '''Helper function for load_teaser_xml to set the basic data

    Parameters
    ----------
    pyxb_class : PyXBClass
        pyxb class represantation of xml

    element : TEASERClass
        teaser class representation of a building element

    '''
    if type(element).__name__ == 'OuterWall' or \
            type(element).__name__ == 'Rooftop':

        element.year_of_construction = pyxb_class.year_of_construction
        element.year_of_retrofit = pyxb_class.year_of_retrofit
        element.construction_type = pyxb_class.construction_type

        element.area = pyxb_class.area
        element.tilt = pyxb_class.tilt
        element.orientation = pyxb_class.orientation

        element.inner_radiation = pyxb_class.inner_radiation
        element.inner_convection = pyxb_class.inner_convection
        element.outer_radiation = pyxb_class.outer_radiation
        element.outer_convection = pyxb_class.outer_convection

    elif type(element).__name__ == 'InnerWall' or \
            type(element).__name__ == 'Ceiling' or \
            type(element).__name__ == 'Floor' or \
            type(element).__name__ == 'GroundFloor':

        element.year_of_construction = pyxb_class.year_of_construction
        element.year_of_retrofit = pyxb_class.year_of_retrofit
        element.construction_type = pyxb_class.construction_type

        element.area = pyxb_class.area
        element.tilt = pyxb_class.tilt
        element.orientation = pyxb_class.orientation

        element.inner_radiation = pyxb_class.inner_radiation
        element.inner_convection = pyxb_class.inner_convection

    elif type(element).__name__ == 'Window':

        element.year_of_construction = pyxb_class.year_of_construction
        element.year_of_retrofit = pyxb_class.year_of_retrofit
        element.construction_type = pyxb_class.construction_type

        element.area = pyxb_class.area
        element.tilt = pyxb_class.tilt
        element.orientation = pyxb_class.orientation

        element.inner_radiation = pyxb_class.inner_radiation
        element.inner_convection = pyxb_class.inner_convection
        element.outer_radiation = pyxb_class.outer_radiation
        element.outer_convection = pyxb_class.outer_convection
        element.g_Value = pyxb_class.g_value
        element.a_conv = pyxb_class.a_conv
        element.shading_g_total = pyxb_class.shading_g_total
        element.shading_max_irr = pyxb_class.shading_max_irr


def set_layer_data_teaser(pyxb_class, element):
    '''Helper function for load_teaser_xml to set the layer data

    Parameters
    ----------
    pyxb_class : PyXBClass
        pyxb class represantation of xml

    element : TEASERClass
        teaser class representation of a building element

    '''
    for pyxb_layer in pyxb_class.Layer:

        layer = Layer(element)

        layer.id = pyxb_layer.id
        layer.thickness = pyxb_layer.thickness

        Material(layer)

        layer.material.name = pyxb_layer.Material.name
        layer.material.density = pyxb_layer.Material.density
        layer.material.thermal_conduc = pyxb_layer.Material.thermal_conduc
        layer.material.heat_capac = pyxb_layer.Material.heat_capac
        layer.material.solar_absorp = pyxb_layer.Material.solar_absorp
        layer.material.ir_emissivity = pyxb_layer.Material.ir_emissivity
