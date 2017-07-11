# Created March 2016
# TEASER 4 Development Team

"""This module contains an example how to create a a district of EST
archetype buildings, to retrofit that district and to export that district
to internal XML and a Modelica record
"""


def example_type_district():
    """"First thing we need to do is to import our Project API module"""

    from teaser.project import Project
    from random import randint
    import buildingspy.simulate.Simulator as Si
    import time
    from multiprocessing import Pool

    """We instantiate the Project class. The parameter load_data = True indicates
    that we load the XML data bases into our Project.
    This can take a few sec."""

    starttime = time.time()

    prj_est1 = Project(load_data=True)
    prj_est1.name = "EST1"
    prj_est4 = Project(load_data=True)
    prj_est4.name = "EST4"
    prj_est7 = Project(load_data=True)
    prj_est7.name = "EST7"
    """The functions starting with type_bldg giving us the opportunity to
    create the specific type building (e.g. type_bldg_residential). The function
    automatically calculates all the necessary parameter. If not specified different
    it uses vdi calculation method."""

    number_of_buildings_est1 = 14

    for building in range(1, round((number_of_buildings_est1) * 0.67) + 1):
        name_help = "Building" + str(building)
        year_of_construction_help = randint(1960, 1980)
        prj_est1.type_bldg_est1a(name=name_help,
                                 year_of_construction=year_of_construction_help,
                                 number_of_floors=2,
                                 height_of_floors=3.15,
                                 net_leased_area=92,
                                 with_ahu=False,
                                 neighbour_buildings=0,
                                 construction_type="heavy")

    for building in range(round((number_of_buildings_est1) * 0.67) + 1,
                          number_of_buildings_est1 + 1):
        name_help = "Building" + str(building)
        year_of_construction_help = randint(1960, 1980)
        prj_est1.type_bldg_est1b(name=name_help,
                                 year_of_construction=year_of_construction_help,
                                 number_of_floors=2,
                                 height_of_floors=3.15,
                                 net_leased_area=92 * 2,
                                 with_ahu=False,
                                 neighbour_buildings=0,
                                 construction_type="heavy",
                                 number_of_apartments=2)

    number_of_buildings_est4 = 4

    for building in range(1, number_of_buildings_est4 + 1):
        name_help = "Building" + str(building)
        year_of_construction_help = randint(1960, 1980)
        prj_est4.type_bldg_est4b(name=name_help,
                                 year_of_construction=year_of_construction_help,
                                 number_of_floors=9,
                                 height_of_floors=2.6,
                                 net_leased_area=417 * 9,
                                 with_ahu=False,
                                 neighbour_buildings=2,
                                 construction_type="heavy",
                                 number_of_apartments=38)

    number_of_buildings_est7 = 29

    for building in range(1, round((number_of_buildings_est7) * 0.45) + 1):
        name_help = "Building" + str(building)
        year_of_construction_help = randint(1900, 1918)
        prj_est7.type_bldg_est7(name=name_help,
                                year_of_construction=year_of_construction_help,
                                number_of_floors=3,
                                height_of_floors=3.88,
                                net_leased_area=65 * 3,
                                with_ahu=False,
                                neighbour_buildings=2,
                                construction_type="heavy",
                                number_of_apartments=1)

    for building in range(round((number_of_buildings_est7) * 0.45) + 1,
                          number_of_buildings_est7 + 1):
        name_help = "Building" + str(building)
        year_of_construction_help = randint(1900, 1918)
        prj_est7.type_bldg_est7(name=name_help,
                                year_of_construction=year_of_construction_help,
                                number_of_floors=3,
                                height_of_floors=3.88,
                                net_leased_area=65 * 3,
                                with_ahu=False,
                                neighbour_buildings=2,
                                construction_type="heavy",
                                number_of_apartments=2)

    """To export the parameters to a Modelica record, we use the export_record
    function. path = None indicates, that we want to store the records in \
    TEASER'S Output folder"""

    prj_est1.export_aixlib(building_model="MultizoneEquipped",
                           zone_model="ThermalZoneEquipped",
                           corG=True,
                           internal_id=None,
                           path=None)

    prj_est4.export_aixlib(building_model="MultizoneEquipped",
                           zone_model="ThermalZoneEquipped",
                           corG=True,
                           internal_id=None,
                           path=None)

    prj_est7.export_aixlib(building_model="MultizoneEquipped",
                           zone_model="ThermalZoneEquipped",
                           corG=True,
                           internal_id=None,
                           path=None)

    """Now we retrofit all buildings in the year 2015 (EnEV2014). \
    That includes new insulation layer and new windows. The name is changed \
    to Retrofit"""

    prj_est1.name = "EST1_Retrofit"
    prj_est1.retrofit_all_buildings(2015)
    prj_est1.export_aixlib(building_model="MultizoneEquipped",
                           zone_model="ThermalZoneEquipped",
                           corG=True,
                           internal_id=None,
                           path=None)

    prj_est4.name = "EST4_Retrofit"
    prj_est4.retrofit_all_buildings(2015)
    prj_est4.export_aixlib(building_model="MultizoneEquipped",
                           zone_model="ThermalZoneEquipped",
                           corG=True,
                           internal_id=None,
                           path=None)

    prj_est7.name = "EST7_Retrofit"
    prj_est7.retrofit_all_buildings(2015)
    prj_est7.export_aixlib(building_model="MultizoneEquipped",
                           zone_model="ThermalZoneEquipped",
                           corG=True,
                           internal_id=None,
                           path=None)

    endtime = time.time()

    print('Pre-processing lasts: ', endtime - starttime, ' seconds or ',
          (endtime - starttime) / 60, ' minutes! or',
          (endtime - starttime) / (60 * 60), 'hours.')

    starttime = time.time()

    """
    Now we define the output directory where the simulation results should be
    stored, in addition we need to define the path where the exported models
    are"""

    outputdir_est1 = "D:/Dymola_workspace/EST1"
    packagedir_est1 = "C:/Users\mla\TEASEROutput/EST1"
    outputdir_est1_retrofit = "D:/Dymola_workspace/EST1_Retrofit"
    packagedir_est1_retrofit = "C:/Users\mla\TEASEROutput/EST1_Retrofit"
    outputdir_est4 = "D:/Dymola_workspace/EST4"
    packagedir_est4 = "C:/Users\mla\TEASEROutput/EST4"
    outputdir_est4_retrofit = "D:/Dymola_workspace/EST4_Retrofit"
    packagedir_est4_retrofit = "C:/Users\mla\TEASEROutput/EST4_Retrofit"
    outputdir_est7 = "D:/Dymola_workspace/EST7"
    packagedir_est7 = "C:/Users\mla\TEASEROutput/EST7"
    outputdir_est7_retrofit = "D:/Dymola_workspace/EST7_Retrofit"
    packagedir_est7_retrofit = "C:/Users\mla\TEASEROutput/EST7_Retrofit"

    """
    Now we need to create a simulation list for buildingspy
    """

    li_est1 = []
    for bld in prj_est1.buildings:
        # this is necessary for the correct names in the simulation script
        name = "EST1." + bld.name + "." + bld.name
        s = Si.Simulator(name, "dymola", outputdir_est1, packagedir_est1)
        li_est1.append(s)

    li_est1_retrofit = []
    for bld in prj_est1.buildings:
        # this is necessary for the correct names in the simulation script
        name = "EST1_Retrofit." + bld.name + "." + bld.name
        s = Si.Simulator(name, "dymola", outputdir_est1_retrofit,
                         packagedir_est1_retrofit)
        li_est1_retrofit.append(s)

    li_est4 = []
    for bld in prj_est4.buildings:
        # this is necessary for the correct names in the simulation script
        name = "EST4." + bld.name + "." + bld.name
        s = Si.Simulator(name, "dymola", outputdir_est4, packagedir_est4)
        li_est4.append(s)

    li_est4_retrofit = []
    for bld in prj_est4.buildings:
        # this is necessary for the correct names in the simulation script
        name = "EST4_Retrofit." + bld.name + "." + bld.name
        s = Si.Simulator(name, "dymola", outputdir_est4_retrofit,
                         packagedir_est4_retrofit)
        li_est4_retrofit.append(s)

    li_est7 = []
    for bld in prj_est7.buildings:
        # this is necessary for the correct names in the simulation script
        name = "EST7." + bld.name + "." + bld.name
        s = Si.Simulator(name, "dymola", outputdir_est7, packagedir_est7)
        li_est7.append(s)

    li_est7_retrofit = []
    for bld in prj_est7.buildings:
        # this is necessary for the correct names in the simulation script
        name = "EST7_Retrofit." + bld.name + "." + bld.name
        s = Si.Simulator(name, "dymola", outputdir_est7_retrofit,
                         packagedir_est7_retrofit)
        li_est7_retrofit.append(s)

    po = Pool(processes=3)
    po.map(simulate_case, li_est1)
    po.map(simulate_case, li_est1_retrofit)
    po.map(simulate_case, li_est4)
    po.map(simulate_case, li_est4_retrofit)
    po.map(simulate_case, li_est7)
    po.map(simulate_case, li_est7_retrofit)

    # Timer
    endtime = time.time()
    print('Simulation lasts: ', endtime - starttime, ' seconds or ', (endtime - starttime) / 60, ' minutes! or',
          (endtime - starttime) / (60 * 60), 'hours.')


def simulate_case(s):
    """ Set common parameters and run a simulation.

    :param s: A simulator object.

    """
    s.showGUI(show=True)
    s.setStopTime(3.1536e7)
    s.setNumberOfIntervals(8760)
    s.setSolver("Dassl")
    s.showProgressBar(show=True)
    s.simulate()


if __name__ == '__main__':
    example_type_district()
    print("That's it! :)")
