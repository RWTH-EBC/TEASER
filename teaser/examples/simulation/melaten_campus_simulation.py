# Created July 2015
# TEASER 4 Development Team

"""
This script demonstrates a automated creation of a office typebuilding and its
simulation with dymola and the AixLib controlled by the python package
buildingspy

General Requirements:
- Buildingspy (pypi version not recommended / use github version instead)
- Dymola (with dymola.exe set to your environment variable PATH)
- AixLib (the actual master from the github repository)
- installed version of TEASER (sure you have this, your using it, but if not
                               sure checkout the github documentation!)

Python 2.7:
you can use the buildingspy package which is available over pypip, but the
actual versions are only available on github (links below)
After installation (read the docu of buildingspy!) This script should be self
describing

Python 3:
you need to install a port to python 3 from the buildingspy package. you can do
it on your own or use the ported package (links below / Only simulator package
is ported)
If its installed correctly you should be able to use this script.

Links:
Buildingspy 2.7: https://github.com/lbl-srg/BuildingsPy
Buildingspy 3.0: https://github.com/MichaMans/BuildingsPy/tree/python3
AixLib master: https://github.com/RWTH-EBC/AixLib
"""

import os
import time
import xml.etree.ElementTree as ET
from multiprocessing import Pool

import buildingspy.simulate.Simulator as si

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


def main():

    starttime = time.time()
    # Adjust this path to your TEASER teaser Examples path or whatever you want
    this_path = "D:/GIT/TEASER/teaser/Examples"
    # path of the buildings xmls
    input_path = os.path.join(this_path,
                              'ExampleInputFiles',
                              'MelatenXML')
    # path where the export is stored
    output_path = os.path.join(os.path.dirname(this_path),
                               'OutputData'
                               )

    info_list = read_XMLs(input_path)

    prj = create_reference_project(info_list)
    print(os.path.join(output_path, 'Reference'))
    prj.export_aixlib(building_model="MultizoneEquipped",
                      zone_model="ThermalZoneEquipped",
                      corG=False, path=os.path.join(output_path, 'Reference'))

    """
    Now we need to simulate this, therefore we get the names of the current
    buildings in this project
    """
    buildingNames = []
    for bld in prj.buildings:
        buildingNames.append(bld.name)

    """
    Now we define the output directory where the simulation results should be
    stored, in addition we need to define the path where the exported models
    are"""

    outputDir = "D:/TestCampusSimulation"
    packageDir = output_path + "/Reference" + "/Project"

    """
    Now we need to create a simulation list for buildingspy
    """

    li = []
    for bld in prj.buildings:
        # this is necessary for the correct names in the simulation script
        name = "Project." + bld.name + "." + bld.name
        s = si.Simulator(name, "dymola", outputDir, packageDir)
        li.append(s)

    po = Pool(processes=3)
    po.map(simulateCase, li)

# Timer
    endtime = time.time()
    print('Simulation lasts: ', endtime - starttime, ' seconds or ',
          (endtime - starttime) / 60, ' minutes! or', (endtime - starttime) / (60 * 60))


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
            this_building.height_of_floors =\
                float(info.find('Geschosshoehe').text)
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


def simulateCase(s):
    """ Set common parameters and run a simulation.

    :param s: A simulator object.

    """
    s.showGUI(show=False)
    s.setStopTime(3.1536e7)
    s.setSolver("Dassl")
    s.showProgressBar(show=True)
    s.setNumberOfIntervals(8760)
    s.getParameters()
    s.simulate()


# Main function
if __name__ == '__main__':
    main()
