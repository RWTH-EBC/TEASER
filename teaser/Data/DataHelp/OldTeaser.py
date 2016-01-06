'''
Created September 2015

@author: TEASER 4 Development Team
'''

import xml.etree.ElementTree as ET

from teaser.Logic.BuildingObjects.BuildingPhysics.OuterWall import OuterWall
from teaser.Logic.BuildingObjects.BuildingPhysics.InnerWall import InnerWall
from teaser.Logic.BuildingObjects.BuildingPhysics.Ceiling import Ceiling
from teaser.Logic.BuildingObjects.BuildingPhysics.Floor import Floor
from teaser.Logic.BuildingObjects.BuildingPhysics.Window import Window
from teaser.Logic.BuildingObjects.BuildingPhysics.Rooftop import Rooftop
from teaser.Logic.BuildingObjects.BuildingPhysics.\
                                                 GroundFloor import GroundFloor
from teaser.Logic.BuildingObjects.BuildingPhysics.Layer import Layer
from teaser.Logic.BuildingObjects.BuildingPhysics.Material import Material
from teaser.Logic.BuildingObjects.Building import Building
from teaser.Logic.BuildingObjects.ThermalZone import ThermalZone
from teaser.Logic.BuildingObjects.TypeBuildings.\
                       UseConditions18599 import UseConditions18599


def load_teaser_xml(path, project):
    '''
    Reads the old TeaserXML into the new class structure

    Parameters
    ----------
    path: string
        where the TeaserXML file is stored

    project: Project()
        instance of Project class
    '''

    tree_teaser = ET.parse(path)
    root = tree_teaser.getroot()


    for bldg_node in (root.findall("Allgemein")):
        building = Building(project, bldg_node.find("Gebaeude").text,
                            bldg_node.find("Baujahr").text,
                            float(bldg_node.find("Geschosszahl").text),
                            float(bldg_node.find("Geschosshoehe").text))
        building.street_name = bldg_node.find("Strasse").text
        building.city = bldg_node.find("Ort").text
        building.type_of_building = bldg_node.find("Gebaeudetyp").text
        building.height_of_floors = float(bldg_node.find("Geschosshoehe").text)
        building.number_of_floors = float(bldg_node.find("Geschosszahl").text)
        if root.findall("Zonen/Zone") is None:
            building.net_leased_area = float(bldg_node.find(
                "Nettoflaeche").text)
        '''
        building.structureFloorPlan = bldg_node.find("Grundrissstruktur").text
        building.neighbourBuildings = bldg_node.find("Nachbargebaeude").text
        building.attic = bldg_node.find("Dach").text
        building.celler = bldg_node.find("Keller").text
        building.construction_type = bldg_node.find("Bauweise").text
        '''
        project.name = bldg_node.find("Projekt").text

    # Parse the zones
    for zone_count in (root.findall("Zonen/Zone")):
        thermal_zone = ThermalZone(building)
        use_conditions = UseConditions18599()
        thermal_zone.name = zone_count.find("Name").text
        # not sure we need this (use_conditions.usage), but first keep it
        use_conditions.usage = zone_count.find("Typ").text
        thermal_zone.area = float(zone_count.find("Flaeche").text)
        use_conditions.coolingStart = float(zone_count.find
                                            ("Betriebszeit_Kuehlung_Beginn")
                                            .text)
        use_conditions.coolingEnd = float(zone_count.find
                                          ("Betriebszeit_Kuehlung_Ende").text)
        use_conditions.heatingStart = float(zone_count.find
                                            ("Betriebszeit_Heizung_Beginn")
                                            .text)
        use_conditions.heatingEnd = float(zone_count.find
                                          ("Betriebszeit_Heizung_Ende").text)
        use_conditions.setTempCool = float(zone_count.find
                                           ("Solltemperatur_Heizung").text)
        use_conditions.setTempHeat = float(zone_count.find
                                           ("Solltemperatur_Kuehlung").text)
        use_conditions.tempSetBack = float(zone_count.find
                                           ("Temperaturabsenkung").text)
        use_conditions.yearlyUsageDays = float(zone_count.find
                                               ("jaehrliche_Nutzungstage")
                                               .text)
        use_conditions.minAirFlow = float(zone_count.find
                                          ("Mindestaussenluftvolumenstrom")
                                          .text)
        use_conditions.persons = float(zone_count.find("Personenlast").text)
        use_conditions.usageProfilePersons = (zone_count.find
                                              ("Nutzungsprofil_Personen").text)
        use_conditions.machines = zone_count.find("Geraetelast").text
        use_conditions.usageProfileMachines = (zone_count.find
                                               ("Nutzungsprofil_Geraete").text)
        use_conditions.lightning = float(zone_count.find("Beleuchtung").text)
        use_conditions.usageStart = zone_count.find("Nutzungszeit_von").text
        use_conditions.usageEnd = zone_count.find("Nutzungszeit_bis").text
        use_conditions.minAHU = float(zone_count.find("minAHU").text)
        use_conditions.maxAHU = float(zone_count.find("maxAHU").text)
        use_conditions.withAHU = bool(zone_count.find("withAHU").text)
        thermal_zone.use_conditions = use_conditions

        # Get all elements from "innenwand" and assign them to innerWall class
        for in_wall_node in zone_count.findall("Innenwand"):
            in_wall = InnerWall(thermal_zone)
            set_basic_data_teaser(in_wall_node, in_wall)
            set_layer_data_teaser(in_wall_node, in_wall)

        # Get all elements from "Decke" and assign them to ceiling class
        for in_wall_node in zone_count.findall("Decke"):
            ceiling = Ceiling(thermal_zone)
            set_basic_data_teaser(in_wall_node, ceiling)
            set_layer_data_teaser(in_wall_node, ceiling)

        # Get all elements from "Boden" and assign them to floor class
        for in_wall_node in zone_count.findall("Boden"):
            floor = Floor(thermal_zone)
            set_basic_data_teaser(in_wall_node, floor)
            set_layer_data_teaser(in_wall_node, floor)

    orientation_dict = {0: 0.0, 2: 90.0, 4: 180.0, 6: 270.0, -1:-1, -2:-2}

    for zone_count in building.thermal_zones:

        for out_wall_node in (root.findall("Huellen/Huelle")):
            type_of_outerwall = int(out_wall_node.find("typ").text)

            if type_of_outerwall == 0:
                out_wall = OuterWall(zone_count)
                set_basic_data_teaser(out_wall_node, out_wall,
                                      orientation_dict)
                set_layer_data_teaser(out_wall_node, out_wall)

            elif type_of_outerwall == 1:
                window = Window(zone_count)
                set_basic_data_teaser(out_wall_node, window, orientation_dict)
                set_layer_data_teaser(out_wall_node, window)

            elif type_of_outerwall == 2:
                rooftop = Rooftop(zone_count)
                set_basic_data_teaser(out_wall_node, rooftop, orientation_dict)
                set_layer_data_teaser(out_wall_node, rooftop)

            elif type_of_outerwall == 3:
                groundfloor = GroundFloor(zone_count)
                set_basic_data_teaser(out_wall_node, groundfloor,
                                      orientation_dict)
                set_layer_data_teaser(out_wall_node, groundfloor)

    for buildingCount in project.list_of_buildings:
        for zone_count in buildingCount.thermal_zones:
            zone_count.set_volume_zone()
        for key, value in buildingCount.outer_area.items():
            buildingCount.set_outer_wall_area(value, key)
        for key, value in buildingCount.window_area.items():
            buildingCount.set_window_area(value, key)


def set_basic_data_teaser(wall_node, element, orientation_dict=0):
    '''
    Helper function to set the basic data

    Parameters
    -----------
    wall_node: XMLNode
        represantation of a xml node

    element: TEASERClass
        teaser class representation of a building element


    '''

    if (type(element).__name__ == 'OuterWall' or
       type(element).__name__ == 'Rooftop' or
       type(element).__name__ == 'Window' or
       type(element).__name__ == 'GroundFloor'):

            if(type(element).__name__ != 'Window'):
                element.parent.parent.outer_area[orientation_dict[
                    float(wall_node.find("orientierung").text)]] = \
                    (float(wall_node.find("flaeche").text))

            else:
                element.parent.parent.window_area[orientation_dict[
                    float(wall_node.find("orientierung").text)]] = \
                    (float(wall_node.find("flaeche").text))

            element.id = wall_node.find("name").text
            element.orientation = orientation_dict[float(wall_node.find
                                                         ("orientierung").text)
                                                   ]
            element.area = float(wall_node.find("flaeche").text)
            if (type(element).__name__ == 'Rooftop'or
               type(element).__name__ == 'GroundFloor'):
                element.tilt = 0.0
            else:
                element.tilt = 90.0

            element.construction_type = wall_node.find("bauart").text
            element.year_of_construction = wall_node.find("baualter").text
            # this is a default value from old teaser
            element.inner_radiation = 5.0
            element.inner_convection = float(wall_node.find
                                             ("waermeuebergangInnen")
                                             .text) - element.inner_radiation

            if(type(element).__name__ != 'GroundFloor'):
                # this is a default value from old teaser
                element.outer_radiation = 5.0
                element.outer_convection = float(wall_node.find
                                                 ("waermeuebergangAussen")
                                                 .text) - element.outer_radiation

            if(type(element).__name__ == 'Window'):
                element.a_conv = float(wall_node.find("a_kon").text)
                element.g_value = float(wall_node.find("g_Wert").text)
                element.shading = float(wall_node.find("g_tot").text)

    elif (type(element).__name__ == 'InnerWall' or
            type(element).__name__ == 'Ceiling' or
            type(element).__name__ == 'Floor'):

            element.id = wall_node.find("typ").text
            element.construction_type = wall_node.find("bauart").text
            element.year_of_construction = (wall_node.find("baualter").text)
            element.area = float(wall_node.find("flaeche").text)
            element.inner_radiation = 5.0
            element.inner_convection = float(wall_node.find
                                             ("waermeuebergangInnen")
                                             .text) - element.inner_radiation


def set_layer_data_teaser(wall_node, element):
    '''
    Helper function to set the layer data

    Parameters
    -----------

    wall_node: XMLNode
        represantation of a xml node

    element: TEASERClass
        teaser class representation of a building element


    '''

    if(type(element).__name__ == 'Ceiling' or
            type(element).__name__ == 'Floor' or
            type(element).__name__ == 'InnerWall'):

        for layer_node in wall_node.find("Schichten"):
            layer = Layer(element)
            material = Material(layer)
            material.name = layer_node.find("material").text
            material.density = float(layer_node.find("rho_Wert").text)
            material.thermal_conduc = float(layer_node.find("lambda_Wert")
                                            .text)
            material.heat_capac = float(layer_node.find("c_Wert").text)
            layer.thickness = float(layer_node.find("dicke").text)

    elif (type(element).__name__ == 'Rooftop' or
          type(element).__name__ == 'GroundFloor' or
          type(element).__name__ == 'OuterWall'):

        for layer_node in wall_node.find("schichten"):
            layer = Layer(element)
            material = Material(layer)
            material.name = layer_node.find("material").text
            material.density = float(layer_node.find("rho_Wert").text)
            material.thermal_conduc = float(layer_node.find("lambda_Wert")
                                            .text)
            material.heat_capac = float(layer_node.find("c_Wert").text)
            layer.thickness = float(layer_node.find("dicke").text)

    elif(type(element).__name__ == 'Window'):

            layer = Layer(element)
            material = Material(layer)
            material.name = "glass"
            material.thermal_conduc = float(wall_node.find("lambda_Wert").text)
            material.transmittance = float(wall_node.find
                                           ("transmissionsGrad").text)
            layer.thickness = float(wall_node.find("dicke").text)
