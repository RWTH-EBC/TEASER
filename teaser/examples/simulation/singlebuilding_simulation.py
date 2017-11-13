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

    # create a office typebuilding
    prj = Project(load_data=True)
    prj.type_bldg_office(name="Office1",
                         year_of_construction=1988,
                         number_of_floors=2,
                         height_of_floors=3.5,
                         net_leased_area=100,
                         office_layout=1,
                         window_layout=1,
                         with_ahu=True,
                         construction_type="heavy")

    # path where the export is stored
    output_path = os.path.join('D:\Temp',
                               'OutputData')

    print(os.path.join(output_path, 'OneBuildingSim'))
    prj.export_aixlib(building_model="MultizoneEquipped",
                      zone_model="ThermalZoneEquipped",
                      corG=False,
                      path=os.path.join(output_path, 'OneBuildingSim'))

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
    packageDir = output_path + "/OneBuildingSim" + "/Project"

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
    # i think we can use async here because we do not need a particular order
    # of the results
    po.map(simulateCase, li)

# Timer
    endtime = time.time()
    print('Simulation lasts: ', endtime - starttime, ' seconds or ',
          (endtime - starttime) / 60, ' minutes! or', (endtime - starttime) / (60 * 60))


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
