#Created December 2016
#TEASER 4 Development Team

"""This module includes Annex60 calcuation class
"""

import scipy.io
import teaser.logic.utilities as utilitis
import numpy as np
import warnings


class Annex60(object):
    """Annex60 Class

    This class holds functions to sort and partly rewrite zone and building
    attributes specific for Annex60.

    Parameters
    ----------

    parent: Building()
        The parent class of this object, the Building the attributes are
        calculated for. (default: None)

    """

    def __init__(self, parent):

        self.parent = parent

    def compare_orientation(self, number_of_elements=2):
        """Compares orientation of walls of all zones and sorts them

        Fills the weighfactors of every zone according to orientation and
        tilt of all zones of the buildings. Therefore it compares orientation
        and tilt of all outer building elements and then creates lists for zone
        weightfactors, orientation, tilt, ares and sunblinds.

        Parameters
        ----------
        number_of_elements: int()
            The number of elements calculated, default is 2
        """

        orient_tilt_help = []
        orient_tilt_help2 = []
        self.parent.orientation_bldg = []
        self.parent.tilt_bldg = []

        for zone in self.parent.thermal_zones:
            for wall in zone.outer_walls:
                if wall.orientation >= 0.0:
                    orient_tilt_help.append((wall.orientation, wall.tilt))
                else:
                    warnings.warn("OuterWalls should not have orientation "
                                  "below zero")
            for roof in zone.rooftops:
                if roof.orientation >= -1.0:
                    orient_tilt_help.append((roof.orientation, roof.tilt))
                else:
                    warnings.warn("Rooftops should have orientation -1 for "
                                  "flat roofs or >= 0.0 for pitched roofs")
            for win in zone.windows:
                if win.orientation >= -1.0:
                    orient_tilt_help.append((win.orientation, win.tilt))
                else:
                    warnings.warn("Windows should have orientation -1 for "
                                  "windows in flat roofs or >= 0.0")

            for i in orient_tilt_help:
                if i in orient_tilt_help2:
                    pass
                else:
                    orient_tilt_help2.append(i)

            orient_tilt_help2.sort(key=lambda x: x[0])

            if orient_tilt_help2[0][0] == -1:
                orient_tilt_help2.insert(
                    len(orient_tilt_help2), orient_tilt_help2.pop(0))

            for i in orient_tilt_help2:
                self.parent.orientation_bldg.append(i[0])
                self.parent.tilt_bldg.append(i[1])

            self._compare_zone(
                thermal_zone=zone,
                orient_tilt=orient_tilt_help2,
                number_of_elements=number_of_elements)

            if number_of_elements == 1:

                ground_floors = zone.find_gfs(-2, 0)
                if not ground_floors:
                    zone.model_attr.weightfactor_ground.append(0.0)
                else:
                    zone.model_attr.weightfactor_ground.append(
                        sum([groundfl.wf_out for groundfl in ground_floors]))

            elif number_of_elements == 2:

                ground_floors = zone.find_gfs(-2, 0)
                if not ground_floors:
                    zone.model_attr.weightfactor_ground.append(0.0)
                else:
                    zone.model_attr.weightfactor_ground.append(
                        sum([groundfl.wf_out for groundfl in ground_floors]))

            elif number_of_elements == 3:

                zone.model_attr.weightfactor_ground.append(0.0)

            elif number_of_elements == 4:

                zone.model_attr.weightfactor_ground.append(0.0)

                rt = zone.model_attr.find_rts(i[0], i[1])
                if rt:
                    zone.orientation_rt.append(i[0])
                    zone.tilt_rt.append(i[1])
                    [zone.weightfactor_rt.append(x.wf_out) for x in rt]

    @staticmethod
    def _compare_zone(
            thermal_zone,
            orient_tilt,
            number_of_elements):
        """Compare helper function for orientation and tilt in zone

        compares and sorts thermal zone attributes for annex
        models. Helper function!

        Parameters
        ----------

        thermal_zone : ThermalZone instance
            Instance of current thermal zone
        orient_tilt : list
            orientation and tilt of current thermal zone [(orientation,tilt)]
        number_of_elements: int()
            The number of elements calculated
        """

        for i in orient_tilt:
            if number_of_elements in [1,2,3]
                walls = thermal_zone.model_attr.find_walls(i[0], i[1]) + \
                        thermal_zone.model_attr.find_rts(i[0], i[1])
            elif number_of_elements == 4:
                walls = thermal_zone.model_attr.find_walls(i[0], i[1])
            else:
                walls = []

            wins = thermal_zone.model_attr.find_wins(i[0], i[1])


            if not walls and wins:
                thermal_zone.model_attr.weightfactor_ow.append(0.0)
                thermal_zone.model_attr.outer_walls_areas.append(0.0)
                thermal_zone.model_attr.tilt_wall.append(i[1])
                thermal_zone.model_attr.orientation_wall.append(i[0])
            elif walls:
                thermal_zone.model_attr.weightfactor_ow.append(
                    sum([wall.wf_out for wall in walls]))
                [thermal_zone.model_attr.outer_walls_areas.append(x.area) for x in walls]
                thermal_zone.model_attr.tilt_wall.append(i[1])
                thermal_zone.model_attr.orientation_wall.append(i[0])
            elif wins:
                thermal_zone.model_attr.weightfactor_win.append(
                    sum([win.wf_out for win in wins]))
                thermal_zone.model_attr.window_area_list.append(
                    sum([win.area for win in wins]))
                thermal_zone.model_attr.g_sunblind_list.append(
                    sum([win.shading_g_total for win in wins]))
                [thermal_zone.model_attr.window_areas.append(x.area) for x in wins]
                thermal_zone.model_attr.tilt_win.append(i[1])
                thermal_zone.model_attr.orientation_win.append(i[0])
            elif not wins and walls:
                thermal_zone.model_attr.weightfactor_win.append(0.0)
                thermal_zone.model_attr.window_area_list.append(0.0)
                thermal_zone.model_attr.g_sunblind_list.append(0.0)
                thermal_zone.model_attr.window_areas.append(0.0)
                thermal_zone.model_attr.tilt_win.append(i[1])
                thermal_zone.model_attr.orientation_win.append(i[0])
