# Created July 2015
# Marcus Fuchs

'''
This module contains an example for the retrofit of an entire district
(Melaten)
'''

import os
import xml.etree.ElementTree as ET

import teaser.logic.utilities as utilitis
from teaser.project import Project


class BuildingInfo(object):
    """
    Light-weight class to hold building info
    """
    def __init__(self):
        """
        Constructor for BuildinInfo
        """
        self.year_of_construction = None
        self.usage_type = None
        self.building_number = None
        self.area = None
        self.floors = None
        self.weight = None
        self.height_of_floors = None
        self.office_layout = None


def main():

    this_path = os.path.dirname(__file__)
    input_path = os.path.join(this_path,
                              'examplefiles',
                              'MelatenXML')

    output_path = utilitis.get_default_path()

    info_list = read_XMLs(input_path)

    prj = create_reference_project(info_list)
    prj.name = "Melaten_Ref"

    '''
    We need to set the projects calculation method. The library we want to
    use is AixLib, we are using a two element model and want an extra resistance
    for the windows. To export the parameters to a Modelica record, we use
    the export_aixlib function. path = None indicates, that we want to store
    the records in TEASER'S Output folder
    '''

    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 2
    prj.merge_windows_calc = False

    prj.calc_all_buildings()

    '''
    Export the Modelica Record. If you have a Dymola License you can  export
    the model with a central AHU (MultizoneEquipped) (only default for office
    and institute buildings)
    '''

    prj.export_aixlib(building_model="MultizoneEquipped",
                      zone_model="ThermalZoneEquipped",
                      corG=True,
                      internal_id=None,
                      path=None)

    '''
    For OpenModelica you need to exclude the centralAHU (because it is using
    state machines). Therefore use the building_model "Multizone"
    '''

    #prj.export_aixlib(building_model="Multizone",
    #                  zone_model="ThermalZoneEquipped",
    #                  corG=True,
    #                  internal_id=None,
    #                  path=None)


    '''Or we use Annex60 method (e.g with four elements). Which exports one
    Model per zone'''

    #prj.used_library_calc = 'Annex60'
    #prj.number_of_elements_calc = 4
    #prj.merge_windows_calc = False

    #prj.calc_all_buildings()
    #prj.export_annex()

    prj.name = "Melaten_Retrofit"
    prj.retrofit_all_buildings(2015)

    '''You could also change the exports here as seen above'''

    prj.export_aixlib(building_model="MultizoneEquipped",
                      zone_model="ThermalZoneEquipped",
                      corG=True,
                      internal_id=None,
                      path=None)


def read_XMLs(input_path):
    """Reads the building XMLs to list of `BuildingInfo` objects

    Parameters
    ----------

    input_path : str
        Path where the XMLs are located

    Returns
    -------
    info_list: list
        A list of `BuildingInfo` objects with information about each building

    """
    info_list = []
    for file in os.listdir(input_path):
        if file.endswith(".xml"):
            print(file)
            this_building = BuildingInfo()

            this_XML = open(os.path.join(input_path,
                                         file), 'r')
            tree = ET.parse(this_XML)
            root = tree.getroot()
            info = root.find('Allgemein')

            this_building.year_of_construction = int(info.find('Baujahr').text)

            usage_type = info.find('Gebaeudetyp').text
            if usage_type == 'Buerogebaeude':
                this_building.usage_type = 'office'
            elif usage_type == 'Wohngebaeude':
                this_building.usage_type = 'residential'
            elif usage_type == 'Institut Allgemein':
                this_building.usage_type = 'institute'
            elif usage_type == 'Institut 4':
                this_building.usage_type = 'institute4'
            elif usage_type == 'Institut 8':
                this_building.usage_type = 'institute8'

            this_building.building_number = info.find('Gebaeude').text

            this_building.floors = int(info.find('Geschosszahl').text)

            this_building.area = float(info.find('Nettoflaeche').text)

            this_building.weight = 'light'
            this_building.height_of_floors = float(info.find(
                'Geschosshoehe').text)
            this_building.office_layout = 0

            print(this_building.year_of_construction)
            print(this_building.usage_type)
            print(this_building.building_number)
            print(this_building.floors)
            print(this_building.weight)
            print(this_building.height_of_floors)
            print(this_building.office_layout)
            print('------------')
            this_XML.close()

            info_list.append(this_building)

    return info_list


def create_reference_project(info_list):
    """Reads building XMLs and creates type buildings into `prj`
    """
    prj = Project(True)

    for building in info_list[:]:
        print('------------')
        print(building.building_number)
        print(building.area)
        print(building)

        if building.usage_type == 'office':
            prj.type_bldg_office(
                name=str(building.building_number),
                year_of_construction=building.year_of_construction,
                number_of_floors=building.floors,
                height_of_floors=building.height_of_floors,
                net_leased_area=building.area,
                office_layout=0,
                window_layout=0,
                construction_type=building.weight)
        elif building.usage_type == 'institute8':
            prj.type_bldg_institute8(
                name=str(building.building_number),
                year_of_construction=building.year_of_construction,
                number_of_floors=building.floors,
                height_of_floors=building.height_of_floors,
                net_leased_area=building.area,
                office_layout=0,
                window_layout=0,
                construction_type=building.weight)
        elif building.usage_type == 'institute4':
            prj.type_bldg_institute4(
                name=str(building.building_number),
                year_of_construction=building.year_of_construction,
                number_of_floors=building.floors,
                height_of_floors=building.height_of_floors,
                net_leased_area=building.area,
                office_layout=0,
                window_layout=0,
                construction_type=building.weight)
        elif building.usage_type == 'institute':
            prj.type_bldg_institute(
                name=str(building.building_number),
                year_of_construction=building.year_of_construction,
                number_of_floors=building.floors,
                height_of_floors=building.height_of_floors,
                net_leased_area=building.area,
                office_layout=0,
                window_layout=0,
                construction_type=building.weight)
        elif building.usage_type == 'residential':
            prj.type_bldg_residential(
                name=str(building.building_number),
                year_of_construction=building.year_of_construction,
                number_of_floors=building.floors,
                height_of_floors=building.height_of_floors,
                net_leased_area=building.area,
                residential_layout=0,
                neighbour_buildings=0,
                attic=0,
                cellar=0,
                dormer=0,
                construction_type=building.weight)
    return prj


# Main function
if __name__ == '__main__':
    main()
