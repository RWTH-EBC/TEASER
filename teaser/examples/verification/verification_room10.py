# Created January 2016
# TEASER 4 Development Team

"""This module loads test case 10 given in VDI 6007-1 form a teaserXML file,
calculates all parameters and exports them as .txt. Differently to the other test cases,
we don't have the original parameter calculated by Rouvel. This test case defines the floor
as connected to an adjacent room with a fixed temperature. If you define the floor as ground floor,
TEASERs calculation won't take the coefficient of heat transfer on the outer surface into account 
(ThermalZone.combine_building_elements(), what makes sense for a ground floor 
that is coupled to the ground). However, we need to define this coefficient,
so we handle this floor as a rooftop. This does not affect the correctness of
the calculted parameter, however, the weightfactor needs to be copied from, 
(weightfactorswall) to (weightfactorground).
"""


def parameter_room10():
    """"First thing we need to do is to import our Project API module"""

    from teaser.Project import Project

    """We instantiate the Project class. The parameter load_data = True indicates
        that we load the XML data bases into our Project.
        This can take a few sec."""

    prj = Project(load_data=True)
    """We load the given test room defined in teaserXML-file"""

    prj.load_project(utilis.get_full_path(
        "examples\\examplefiles\\VDI6007_Room10.teaserXML"))

    """Then we calculate all parameter with the calculation
    core 'vdi', that is exactly as defined in VDI 6007-1."""

    prj.calc_all_buildings(number_of_elements=2,
                           merge_windows=True,
                           used_library='AixLib')

    """After this, we can export our projects as .txt."""

    prj.export_parameters_txt()

if __name__ == '__main__':
    parameter_room10()
    print("That's it! :)")
