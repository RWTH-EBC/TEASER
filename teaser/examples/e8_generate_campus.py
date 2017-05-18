# Created July 2015
# Marcus Fuchs

"""This module contains an example how to generate a whole campus with 112
buildings. The building information are stored in a data base. As we can't
provide public access to the data base we exported available building
information in XML files. The files can be found in
examples.examplefiles.MelatenXML. To load we use the function read_XMLs and
to handle data, we have a light-weight class called BuildingInfo.
This example is not as well documented as the others. If you are new to
TEASER please read examples e1 to e7 first.
"""

import os
import xml.etree.ElementTree as ET
import teaser.logic.utilities as utilities
from teaser.project import Project


class BuildingInfo(object):
    """
    Light-weight class to hold building info
    """

    def __init__(self):
        """
        Constructor for BuildingInfo
        """
        self.year_of_construction = None
        self.usage_type = None
        self.building_number = None
        self.area = None
        self.floors = None
        self.weight = None
        self.height_of_floors = None
        self.office_layout = None


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

            this_XML = open(os.path.join(input_path, file), 'r')
            tree = ET.parse(this_XML)
            root = tree.getroot()
            info = root.find('Allgemein')

            this_building.year_of_construction = int(info.find('Baujahr').text)

            usage_type = info.find('Gebaeudetyp').text
            if usage_type == 'Buerogebaeude':
                this_building.usage_type = 'office'
            elif usage_type == 'Wohngebaeude':
                this_building.usage_type = 'single_family_dwelling'
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

            this_XML.close()

            info_list.append(this_building)

    return info_list


def create_reference_project(info_list):
    """Reads BuildingInfo and creates type buildings into `prj`
    """
    prj = Project(True)

    for building in info_list[:]:
        print('------------')
        print(building.building_number)
        print(building.area)
        print(building)

        if building.usage_type == 'office' \
                or building.usage_type == 'institute' \
                or building.usage_type == 'institute4' \
                or building.usage_type == 'institute8':
            prj.add_non_residential(
                method='bmvbs',
                usage=building.usage_type,
                name=str(building.building_number),
                year_of_construction=building.year_of_construction,
                number_of_floors=building.floors,
                height_of_floors=building.height_of_floors,
                net_leased_area=building.area,
                construction_type=building.weight)
        elif building.usage_type == 'single_family_dwelling':
            prj.add_residential(
                method='iwu',
                usage=building.usage_type,
                name=str(building.building_number),
                year_of_construction=building.year_of_construction,
                number_of_floors=building.floors,
                height_of_floors=building.height_of_floors,
                net_leased_area=building.area,
                construction_type=building.weight)
    return prj


if __name__ == '__main__':
    this_path = os.path.dirname(__file__)
    input_path = os.path.join(
        this_path,
        'examplefiles',
        'MelatenXML')

    info_list = read_XMLs(input_path)
    prj = create_reference_project(info_list)
    prj.name = "Melaten_Ref"

    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 2
    prj.weather_file_path = utilities.get_full_path(
        os.path.join(
            "data",
            "input",
            "inputdata",
            "weatherdata",
            "DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos"))

    prj.calc_all_buildings()

    prj.export_aixlib(
        internal_id=None,
        path=None)

    prj.name = "Melaten_Retrofit"
    prj.retrofit_all_buildings(year_of_retrofit=2015)

    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 2
    prj.weather_file_path = utilities.get_full_path(
        os.path.join(
            "data",
            "input",
            "inputdata",
            "weatherdata",
            "DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos"))

    prj.calc_all_buildings()

    prj.export_aixlib(
        internal_id=None,
        path=None)

    print("Example 8: That's it! :)")
