'''
Created July 2015

@author: TEASER 4 Development Team

This Scripts loads an project from TEASER 3 and executes the calculation

'''

from teaser.project import Project
import teaser.logic.utilities as utilitis

'''
load project of VDI 6007 room from  TEASER file
'''
prj = Project(False)

prj.load_project(utilitis.get_full_path(
    "examples/examplefiles/new.teaserXML"))

'''
execute VDI calculation for single zone
'''

prj.buildings[0].calc_building_parameter('ebc')

'''
parameters inner wall 
'''
print("Parameters for inner wall")
print("r1_iw:", prj.buildings[0].thermal_zones[0].r1_iw,"K/W ---", "TEASER 3: 4.62113316216e-06 K/W")
print("c1_iw: ", prj.buildings[0].thermal_zones[0].c1_iw,"kJ/K ---", "TEASER 3: 1209810287.22 kJ/K")
print("area_iw: ", prj.buildings[0].thermal_zones[0].area_iw,"qm ---", "TEASER 3: 9866.66666667 qm")
print("alpha_conv_iw: ", prj.buildings[0].thermal_zones[0].alpha_conv_inner_iw,
      "W/(qm*K) ---", "TEASER 3: 2.37567567568W/(qm*K)")

'''
parameters outer wall 
'''

print("\nParameters for outer wall")
print("r_rest_ow", prj.buildings[0].thermal_zones[0].r_rest_ow,"K/W ---", "TEASER 3: 0.00196902259415 K/W")
print("r1_ow:", prj.buildings[0].thermal_zones[0].r1_ow,"K/W ---", "TEASER 3: 3.06155256089e-05K/W")
print("c1_ow: ", prj.buildings[0].thermal_zones[0].c1_ow,"kJ/K ---", "TEASER 3: 226923157.846 kJ/K")
print("area_ow: ", prj.buildings[0].thermal_zones[0].area_ow,"qm ---", "TEASER 3: 920.0 qm")

print("alpha_conv_inner_ow: ", prj.buildings[0].thermal_zones[0].alpha_conv_inner_ow,"W/(qm*K) ---", "TEASER 3: 1.83043478261 W/(qm*K)")

print("alpha_conv_outer_ow: ", prj.buildings[0].thermal_zones[0].alpha_conv_outer_ow,"W/(qm*K) ---", "TEASER 3: 20.0 W/(qm*K)")
print("alpha_comb_outer_ow: ", prj.buildings[0].thermal_zones[0].alpha_comb_outer_ow,"W/(qm*K) ---", "TEASER 3: 25.0 W/(qm*K)")
print("alpha_conv_inner_win: ", prj.buildings[0].thermal_zones[0].alpha_conv_inner_win,"W/(qm*K) ---", "TEASER 3: 2.7 W/(qm*K)")
print("alpha_conv_outer_win: ", prj.buildings[0].thermal_zones[0].alpha_conv_outer_win,"W/(qm*K) ---", "TEASER 3: 20.0 W/(qm*K)")
print("alpha_comb_outer_win: ", prj.buildings[0].thermal_zones[0].alpha_comb_outer_win,"W/(qm*K) ---", "TEASER 3: 25.0 W/(qm*K)")
'''
The weightfactors in TEASER 3 are not correctly calculated because they take outer convection and radiation for ground floors into account!
'''
print("weightfactor_ow", prj.buildings[0].thermal_zones[0].weightfactor_ow, "TEASER 3: {0.0489486325367, 0.0244743162683, 0.0489486325367, 0.0244743162683, 0.325684732247}" )
print("weightfactor_win", prj.buildings[0].thermal_zones[0].weightfactor_win, "TEASER 3: {0.333333333333, 0.166666666667, 0.333333333333, 0.166666666667, 0}")
print("weightfactor_ground", prj.buildings[0].thermal_zones[0].weightfactor_ground, "TEASER 3: 0.527469370143")
