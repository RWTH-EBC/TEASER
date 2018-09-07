# Created January 2016
# TEASER 4 Development Team

"""This script loads test case 10 given in VDI 6007-1 from a teaserXML file,
calculates all parameters and exports them as .txt. Differently to the other
test cases, we don't have the original parameter calculated by Rouvel. This test
case defines the floor as connected to an adjacent room with a fixed
temperature. If you define the floor as ground floor, TEASERs calculation won't
take the coefficient of heat transfer on the outer surface into account
(ThermalZone.combine_building_elements(), what makes sense for a ground floor
that is coupled to the ground). However, we need to define this coefficient, so
we handle this floor as a rooftop. This does not affect the correctness of the
calculated parameter, however, the weightfactor needs to be copied from,
(weightfactorswall) to (weightfactorground). """

from teaser.project import Project
import teaser.logic.utilities as utilities


def parameter_room10():

    prj = Project(load_data=True)

    prj.load_project(utilities.get_full_path(
        "examples/examplefiles/VDI6007_Room10.teaserXML"))

    prj.buildings[0].calc_building_parameter(
        number_of_elements=2,
        merge_windows=True,
        used_library='AixLib')

    prj.export_parameters_txt()


if __name__ == '__main__':
    parameter_room10()
    print("That's it! :)")
