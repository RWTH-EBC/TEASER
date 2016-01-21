# Created January 2016
# TEASER 4 Development Team

"""This module contains an example how to create the validation cases given in VDI 6007-1,
to load the respective teaserXML files, to calculate all parameters and export them as
.txt.
"""


def example_validation():
    """"First thing we need to do is to import our Project API module"""

    from teaser.Project import Project

    """We instantiate the Project class. The parameter load_data = True indicates
        that we load the XML data bases into our Project.
        This can take a few sec."""

    prj = Project(load_data=True)
    """We load all given (four) test rooms defined in teaserXML-files"""

    prj.load_project('D:/GIT/TEASER/teaser/Examples/ExampleInputFiles/VDI6007_Room1.teaserXML')
    prj.load_project('D:/GIT/TEASER/teaser/Examples/ExampleInputFiles/VDI6007_Room3.teaserXML')
    prj.load_project('D:/GIT/TEASER/teaser/Examples/ExampleInputFiles/VDI6007_Room8.teaserXML')
    prj.load_project('D:/GIT/TEASER/teaser/Examples/ExampleInputFiles/VDI6007_Room10.teaserXML')

    """Then we calculate all parameter for all buildings (one per project) with the calculation
    core 'vdi', that is exactly as defined in VDI 6007-1."""

    prj.calc_all_buildings('vdi')

    """After this, we can export our projects as .txt."""

    prj.export_parameters_txt()

if __name__ == '__main__':
    example_validation()
    print("That's it! :)")
