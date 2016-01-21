# Created January 2016
# TEASER 4 Development Team

"""This module contains an example how to create the validation cases given in VDI 6007-1,
to load the respective teaserXML files, to calculate all parameters and export them as
.txt and models.
"""


def example_validation():
    """"First thing we need to do is to import our Project API module"""

    from teaser.Project import Project

    """We instantiate the Project class. The parameter load_data = True indicates
        that we load the XML data bases into our Project. Currently, the four test
        are defined as separate projects, so we need four project instances.
        This can take a few sec."""

    prj_1 = Project(load_data=True)
    prj_2 = Project(load_data=True)
    prj_3 = Project(load_data=True)
    prj_4 = Project(load_data=True)

    """We load all given (four) test rooms defined in teaserXML-files"""

    prj_1.load_project('D:/GIT/TEASER/teaser/Examples/ExampleInputFiles/VDI6007_Room1.teaserXML')
    prj_2.load_project('D:/GIT/TEASER/teaser/Examples/ExampleInputFiles/VDI6007_Room3.teaserXML')
    prj_3.load_project('D:/GIT/TEASER/teaser/Examples/ExampleInputFiles/VDI6007_Room8.teaserXML')
    prj_4.load_project('D:/GIT/TEASER/teaser/Examples/ExampleInputFiles/VDI6007_Room10.teaserXML')

    """Then we calculate all parameter for all buildings (one per project) with the calculation
    core 'vdi', that is exactly as defined in VDI 6007-1."""

    prj_1.calc_all_buildings('vdi')
    prj_2.calc_all_buildings('vdi')
    prj_3.calc_all_buildings('vdi')
    prj_4.calc_all_buildings('vdi')

    """After this, we can export our projects as .txt and model. For the model, we can define what
    sub-models to use."""

    prj_1.export_parameters_txt()
    prj_2.export_parameters_txt()
    prj_3.export_parameters_txt()
    prj_4.export_parameters_txt()

    prj_1.export_record('MultizoneEquipped', zone_model='ThermalZoneEquipped', corG=True)
    prj_2.export_record('MultizoneEquipped', zone_model='ThermalZoneEquipped', corG=True)
    prj_3.export_record('MultizoneEquipped', zone_model='ThermalZoneEquipped', corG=True)
    prj_4.export_record('MultizoneEquipped', zone_model='ThermalZoneEquipped', corG=True)


if __name__ == '__main__':
    example_validation()
    print("That's it! :)")
