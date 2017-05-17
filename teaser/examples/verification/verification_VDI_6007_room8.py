# Created July 2015
# TEASER Development Team

"""
This script loads the VDI 6007 Room 8 as *.teaserXML and computes
parameters. The parameters are then compared with the ones from Rouvel
"""

from teaser.project import Project
import teaser.logic.utilities as utilities


def parameter_room8():

    prj = Project(False)
    prj.name = "VDI_Verification_Room8"

    prj.load_project(utilities.get_full_path(
        "examples/examplefiles/VDI6007_Room8.teaserXML"))

    prj.buildings[0].calc_building_parameter(
        number_of_elements=2,
        merge_windows=True,
        used_library='AixLib')

    return prj


if __name__ == "__main__":
    prj = parameter_room8()

    """
    parameters inner wall
    """
    print("Parameters for inner wall")
    print("r1_iw:", prj.buildings[0].thermal_zones[0].model_attr.r1_iw,
          "K/W ---", "Rouvel: 0.000668640 K/W")
    print("c1_iw: ", prj.buildings[0].thermal_zones[0].model_attr.c1_iw / 1000,
          "kJ/K ---", "Rouvel: 12391.2 kJ/K")
    print("area_iw: ", prj.buildings[0].thermal_zones[0].model_attr.area_iw,
          "m2 ---", "Rouvel: 60.50 m2")
    print("alpha_weight_conv_iw: ",
          prj.buildings[0].thermal_zones[0].model_attr.alpha_conv_inner_iw,
          "W/(m2*K) ---", "Rouvel: 2.121487317 W/(m2*K)")

    """
    parameters outer wall
    """

    print("\nParameters for outer wall")
    print("r_rest_ow", prj.buildings[0].thermal_zones[0].model_attr.r_rest_ow,
          "K/W ---", "Rouvel: 0.020705927 K/W")
    print("r1_ow:", prj.buildings[0].thermal_zones[0].model_attr.r1_ow,
          "K/W ---", "Rouvel: 0.001736253 K/W")
    print("c1_ow: ", prj.buildings[0].thermal_zones[0].model_attr.c1_ow / 1000,
          "kJ/K ---", "Rouvel: 5259.9 kJ/K")
    print("area_ow + area_win: ", prj.buildings[0].thermal_zones[
        0].model_attr.area_ow + prj.buildings[0].thermal_zones[
        0].model_attr.area_win,
        "m2 ---", "Rouvel: 25.5 m2")
    print("alpha_conv_inner_ow: ",
          prj.buildings[0].thermal_zones[0].model_attr.alpha_conv_inner_ow,
          "W/(m2*K) ---", "Rouvel: 2.7 W/(m2*K)")
    print("alpha_comb_outer_ow: ",
          prj.buildings[0].thermal_zones[0].model_attr.alpha_comb_outer_ow,
          "W/(m2*K) ---", "Rouvel: 25.0 W/(m2*K)")
    prj.buildings[0].thermal_zones[0].model_attr.weightfactor_ow.sort()
    print("weightfactor_ow: ",
          prj.buildings[0].thermal_zones[0].model_attr.weightfactor_ow,
          "Rouvel: 0.057968311, 0.132498994")
    prj.buildings[0].thermal_zones[0].model_attr.weightfactor_win.sort()
    print("weightfactor_win: ",
          prj.buildings[0].thermal_zones[0].model_attr.weightfactor_win,
          "Rouvel: 0.404766351, 0.404766351")
