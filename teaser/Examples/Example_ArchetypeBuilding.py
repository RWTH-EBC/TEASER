# Created July 2015
# TEASER 4 Development Team

"""This module contains an example how to create a type Buidling, to retrofit
that building and to export that building to internal XML and a Modelica record
"""


def example_type_building():
    """"First thing we need to do is to import our Project API module"""

    from teaser.Project import Project

    """We instantiate the Project class. The parameter load_data = True indicates
    that we load the XML data bases into our Project. 
    This can take a few sec."""

    prj = Project(load_data=True)

    """The five functions starting with type_bldg giving us the opportunity to
    create the specific type building (e.g. type_bldg_residential). The function
    automatically calculates all the necessary parameter. If not specified different
    it uses vdi calculation method."""

    prj.type_bldg_residential(name="ResidentialBuilding",
                              year_of_construction=1988,
                              number_of_floors=2,
                              height_of_floors=3.5,
                              net_leased_area=100,
                              with_ahu=True,
                              residential_layout=1,
                              neighbour_buildings=1,
                              attic=1,
                              cellar=1,
                              construction_type="heavy",
                              dormer=1)

    prj.type_bldg_est1a(name="EST1aBuilding",
                              year_of_construction=1988,
                              number_of_floors=2,
                              height_of_floors=3.5,
                              net_leased_area=100,
                              with_ahu=True,
                              neighbour_buildings=1,
                              construction_type="heavy")

    prj.type_bldg_est1b(name="EST1bBuilding",
                              year_of_construction=1988,
                              number_of_floors=2,
                              height_of_floors=3.5,
                              net_leased_area=100,
                              with_ahu=True,
                              neighbour_buildings=1,
                              construction_type="heavy",
                              number_of_apartments=5)

    prj.type_bldg_office(name="Office1",
                         year_of_construction=1988,
                         number_of_floors=2,
                         height_of_floors=3.5,
                         net_leased_area=100,
                         office_layout=1,
                         window_layout=1,
                         with_ahu=True,
                         construction_type="heavy")

    """To export the parameters to a Modelica record, we use the export_record
    function. path = None indicates, that we want to store the records in \
    TEASER'S Output folder"""

    prj.export_record(building_model="MultizoneEquipped",
                      zone_model="ThermalZoneEquipped",
                      corG=True,
                      internal_id=None,
                      path=None)

    """Now we retrofit all buildings in the year 2015 (EnEV2014). \
    That includes new insulation layer and new windows. The name is changed \
    to Retrofit"""

    prj.name = "Project_Retrofit"
    prj.retrofit_all_buildings(2015)
    prj.export_record(building_model="MultizoneEquipped",
                      zone_model="ThermalZoneEquipped",
                      corG=True,
                      internal_id=None,
                      path=None)

    """To load our retrofitted building in TEASER, we can save to project \
    into a XML file"""

    prj.save_project("Retrofit_Building",
                     path=None)

    '''Save the human readable output txt'''
    prj.export_parameters_txt(path=None)

    '''   
    Save the human readable output txt
    '''
    prj.save_citygml(path=None)


if __name__ == '__main__':
    example_type_building()
    print("That's it! :)")
