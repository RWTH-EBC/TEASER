'''
Created July 2015

@author: TEASER 4 Development Team


This Scripts loads the VDI 6007 Room from the old format of TEASER 3, 
manipulates the data thus it fits with the specification of VDI 6007 and 
computes the parameters. The parameters are then compared with the ones from
Rouvel

'''
from teaser.project import Project

import teaser.logic.utilities as utilitis

def parameter_room8():
    
    '''
    load project of VDI 6007 room from old TEASER file
    '''
    prj = Project(False)
    prj.load_project(utilitis.get_full_path(
        "examples/examplefiles/VDI6007_Room8.teaserXML"))

    '''
    execute VDI calculation for single zone
    '''
    
    prj.buildings[0].calc_building_parameter(number_of_elements=2,
                                             merge_windows=True,
                                             used_library='AixLib')
    
    return prj

prj = parameter_room8()

'''
parameters inner wall
'''
print("Parameters for inner wall")
print("r1_iw:", prj.buildings[0].thermal_zones[0].r1_iw, "K/W ---", "Rouvel: 0.000668640 K/W")
print("c1_iw: ", prj.buildings[0].thermal_zones[0].c1_iw / 1000, "kJ/K ---", "Rouvel: 12391.2 kJ/K")
print("area_iw: ", prj.buildings[0].thermal_zones[0].area_iw, "qm ---", "Rouvel: 60.50 qm")
print("alpha_weight_conv_iw: ", prj.buildings[0].thermal_zones[0].alpha_conv_inner_iw, "W/(qm*K) ---", "Rouvel: 2.121487317 W/(qm*K)")

'''
parameters outer wall
'''
print("\nParameters for outer wall")
print("r_rest_ow", prj.buildings[0].thermal_zones[0].r_rest_ow, "K/W ---", "Rouvel: 0.020705927 K/W")
print("r1_ow:", prj.buildings[0].thermal_zones[0].r1_ow, "K/W ---", "Rouvel: 0.001736253 K/W")
print("c1_ow: ", prj.buildings[0].thermal_zones[0].c1_ow / 1000, "kJ/K ---", "Rouvel: 5259.9 kJ/K")
print("area_ow: ", prj.buildings[0].thermal_zones[0].area_ow + prj.buildings[0].thermal_zones[0].area_win, "qm ---", "Rouvel: 25.5 qm")
print("alpha_conv_inner_ow: ", prj.buildings[0].thermal_zones[0].alpha_conv_inner_ow, "W/(qm*K) ---", "Rouvel: 2.7 W/(qm*K)")
print("alpha_comb_outer_ow: ", prj.buildings[0].thermal_zones[0].alpha_comb_outer_ow, "W/(qm*K) ---", "Rouvel: 25.0 W/(qm*K)")
print("weightfactor_ow: ", prj.buildings[0].thermal_zones[0].weightfactor_ow, "Rouvel: 0.057968311, 0.132498994")
print("weightfacotr_win: ", prj.buildings[0].thermal_zones[0].weightfactor_win, "Rouvel: 0.404766351, 0.404766351")


