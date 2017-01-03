# Created July 2015
# TEASER 4 Development Team

"""This module contains an example how to create an archetype Building, to retrofit
that building and to export that building to internal XML and a Modelica record
"""
import teaser.data.bindings.v_0_3_9

def example_type_building():
    """"First thing we need to do is to import our Project API module"""

    from teaser.project import Project

    """We instantiate the Project class. The parameter load_data = True indicates
    that we load the XML data bases into our Project.
    This can take a few sec."""

    prj = Project(load_data=True)
    prj.name = "ArchetypeBuildings_Ref"

    """The five functions starting with type_bldg giving us the opportunity to
    create the specific type building (e.g. type_bldg_residential). The function
    automatically calculates all the necessary parameter. If not specified different
    it uses vdi calculation method."""

    prj.type_bldg_residential(
                    name="ResidentialBuilding",
                    year_of_construction=1988,
                    number_of_floors=2,
                    height_of_floors=3.5,
                    net_leased_area=200,
                    with_ahu=False)


    prj.type_bldg_office(
                    name="Institute",
                    year_of_construction=1988,
                    number_of_floors=3,
                    height_of_floors=3.5,
                    net_leased_area=3500,
                    office_layout=1,
                    window_layout=1,
                    with_ahu=True,
                    construction_type="heavy")


    '''
    We need to set the projects calculation method. The library we want to
    use is AixLib, we are using a two element model and want an extra resistance
    for the windows. To export the parameters to a Modelica record, we use
    the export_aixlib function. path = None indicates, that we want to store
    the records in TEASER'S Output folder
    '''

    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 3
    prj.merge_windows_calc = False

    prj.calc_all_buildings()

    '''
    Export the Modelica Record. If you have a Dymola License you can  export
    the model with a central AHU (MultizoneEquipped) (only default for office
    and institute buildings)
    '''

    prj.export_aixlib(
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
    prj.name = "projectfalse"
    prj.used_library_calc = 'Annex60'
    prj.number_of_elements_calc = 2
    prj.merge_windows_calc = False

    prj.calc_all_buildings()
    prj.export_annex()

    prj.name = "projecttrue"
    prj.used_library_calc = 'Annex60'
    prj.number_of_elements_calc = 2
    prj.merge_windows_calc = True

    prj.calc_all_buildings()
    prj.export_annex()



if __name__ == '__main__':
    example_type_building()
    print("That's it! :)")
