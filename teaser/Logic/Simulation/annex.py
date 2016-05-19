'''
Created May 2016

@author: TEASER Development Team
'''

"""annex.py

This module contains functions to sort and partly rewrite zone attributes
specific for annex simulation, including the export of boundary conditions
and AHU operation values
"""
import scipy.io
import teaser.Logic.Utilis as utilis
import numpy as np


def compare_orientation(bldg):
    """Fills the zone weightfactors according to orientation and tilt of
        building

        compares orientation and tilt of all outer building elements and then
        creates lists for zone weightfactors and building orientation and tilt

        Parameters
        ----------

        bldg: Building()
            TEASER instance of Building()
    """

    orient_tilt_help1 = []
    orient_tilt_help2 = []
    for zone in bldg.thermal_zones:
        for wall in zone.outer_walls:
            if wall.orientation != -2:
                orient_tilt_help1.append([wall.orientation, wall.tilt])
            else:
                pass
        for win in zone.windows:
            if win.orientation != -2:
                orient_tilt_help1.append([win.orientation, win.tilt])
            else:
                pass

        for i in orient_tilt_help1:
            if i in orient_tilt_help2:
                pass
            else:
                orient_tilt_help2.append(i)
    
        orient_tilt_help2.sort(key=lambda x: x[0])
    
        if orient_tilt_help2[0][0] == -1:
            orient_tilt_help2.insert(len(orient_tilt_help2), orient_tilt_help2.pop(0))
    
        for i in orient_tilt_help2:
            bldg.orientation_bldg.append(i[0])
            bldg.tilt_bldg.append(i[1])

        groundfloors = zone.find_walls(-2, 0)
        if groundfloors == []:
            zone.weightfactor_ground.append(0.0)
        else:
            zone.weightfactor_ground.append(
                sum([groundfl.wf_out for groundfl in groundfloors]))

        for i in orient_tilt_help2:
            walls = zone.find_walls(i[0], i[1])
            wins = zone.find_wins(i[0], i[1])


            zone.tilt_wall.append(i[1])
            zone.orientation_wall.append(i[0])

            zone.tilt_win.append(i[1])
            zone.orientation_win.append(i[0])

            if walls == []:
                zone.weightfactor_ow.append(0.0)
                zone.outer_walls_areas.append(0.0)
            else:
                zone.weightfactor_ow.append(
                    sum([wall.wf_out for wall in walls]))
                [zone.outer_walls_areas.append(i.area) for i in walls]
            if wins == []:
                zone.weightfactor_win.append(0.0)
                zone.window_area_list.append(0.0)
                zone.g_sunblind_list.append(0.0)
                zone.window_areas.append(0.0)
            else:
                zone.weightfactor_win.append(
                    sum([win.wf_out for win in wins]))
                zone.window_area_list.append(
                    sum([win.area for win in wins]))
                zone.g_sunblind_list.append(
                    sum([win.shading_g_total for win in wins]))
                [zone.window_areas.append(i.area) for i in wins]
        print(zone.window_areas)
        print(zone.outer_walls_areas)
        print("asd",zone.orientation_wall)
