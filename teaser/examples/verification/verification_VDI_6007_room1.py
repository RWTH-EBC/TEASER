# Created July 2015
# TEASER Development Team

"""
This script loads the VDI 6007 Room 1 as *.teaserXML and computes
parameters. The parameters are then compared with the ones from Rouvel
"""

from teaser.project import Project
import teaser.logic.utilities as utilities


def parameter_room1():

    prj = Project(False)
    prj.name = "VDI_Verification_Room1"

    prj.load_project(utilities.get_full_path(
        "examples/examplefiles/VDI6007_Room1.teaserXML"))

    prj.buildings[0].calc_building_parameter(
        number_of_elements=2,
        merge_windows=True,
        used_library='AixLib')

    return prj


if __name__ == "__main__":
    prj = parameter_room1()

    """
    parameters inner wall Typraum S
    """
    print("Parameters for inner wall")
    print("r1_iw:", prj.buildings[0].thermal_zones[0].model_attr.r1_iw,
          "K/W ---", "Rouvel: 0.000595515 K/W")
    print("c1_iw: ", prj.buildings[0].thermal_zones[0].model_attr.c1_iw / 1000,
          "kJ/K ---", "Rouvel: 14836.2 kJ/K")
    print("area_iw: ", prj.buildings[0].thermal_zones[0].model_attr.area_iw,
          "m2 ---", "Rouvel: 75.5 m2")
    print("alpha_weight_conv_iw: ",
          prj.buildings[0].thermal_zones[0].model_attr.alpha_conv_inner_iw,
          "W/(m2*K) ---", "Rouvel: 2.236423594 W/(m2*K)")

    """
    parameters outer wall Typraum S
    """
    print("\nParameters for outer wall")
    print("r_rest_ow", prj.buildings[0].thermal_zones[0].model_attr.r_rest_ow,
          "K/W ---", "Rouvel: 0.042768721 K/W")
    print("r1_ow:", prj.buildings[0].thermal_zones[0].model_attr.r1_ow,
          "K/W ---", "Rouvel: 0.004367913 K/W")
    print("c1_ow: ", prj.buildings[0].thermal_zones[0].model_attr.c1_ow / 1000,
          "kJ/K ---", "Rouvel: 1600.8 kJ/K")
    print("area_ow+area_win: ", prj.buildings[0].thermal_zones[
        0].model_attr.area_ow * prj.buildings[0].thermal_zones[
        0].model_attr.area_win,
        "m2 ---", "Rouvel: 10.5 m2")
    print("alpha_conv_inner_ow: ",
          prj.buildings[0].thermal_zones[0].model_attr.alpha_conv_inner_ow,
          "W/(m2*K) ""---", "Rouvel: 2.7 W/(qm*K)")
    print("alpha_comb_outer_ow: ",
          prj.buildings[0].thermal_zones[0].model_attr.alpha_comb_outer_ow,
          "W/(m2*K) ---", "Rouvel: 25.0 W/(m2*K)")
