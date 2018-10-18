# Created December 2016
# TEASER 4 Development Team

"""This module includes IBPSA calculation class
"""

import os

import numpy as np
import scipy.io

import teaser.logic.utilities as utilities


class IBPSA(object):
    """IBPSA Class

    This class holds functions to sort and partly rewrite zone and building
    attributes specific for IBPSA simulation. This includes the export of
    boundary conditions.

    Parameters
    ----------

    parent: Building()
        The parent class of this object, the Building the attributes are
        calculated for. (default: None)

    Attributes
    ----------

    file_internal_gains : str
        Filename for internal gains file
    version : dict
        Dictionary with supported libraries and their version numbers
    consider_heat_capacity : bool
        decides whether air capacity is considered or not for all thermal
        zones in the building


    """

    def __init__(self, parent):

        self.parent = parent
        self.file_internal_gains = "InternalGains_" + self.parent.name + ".mat"
        self.version = {'AixLib': '0.7.2', 'Buildings': '5.1.0',
                        'BuildingSystems': '2.0.0-beta2', 'IDEAS': '1.0.0'}
        self.consider_heat_capacity = True

    @staticmethod
    def create_profile(duration_profile=86400, time_step=3600):
        """Creates a profile for building boundary conditions

        This function creates a list with an equidistant profile given the
        duration of the profile in seconds (default one day, 86400 s) and the
        time_step in seconds (default one hour, 3600 s). Needed for boundary
        input of the building for Modelica simulation

        Note
        -----
        As Python starts from counting the range from zero, but Modelica needs
        0 as start value and additional 24 entries. We add one iteration
        step in the profile.

        Parameters
        ----------
        duration_profile : int
            duration of the profile in seconds (default one day, 86400 s)
        time_step : int
            time step used in the profile in seconds (default one hour, 3600 s)

        Returns
        ---------
        time_line : [[int]]
            list of time steps as preparation for the output of boundary
            conditions
        """
        ass_error_1 = "duration must be a multiple of time_step"

        assert float(duration_profile / time_step).is_integer(), ass_error_1

        time_line = []

        for i in range(int(duration_profile / time_step) + 1):
            time_line.append([i * time_step])
        return time_line

    def modelica_gains_boundary(
            self,
            zone,
            time_line=None,
            path=None):
        """creates .mat file for internal gains boundary conditions

        This function creates a matfile (-v4) for building internal gains
        boundary conditions. It collects internal gain profiles of a specific
        zones and stores them into one file. It also calculates the internal
        gains from relative presence and values for heat output into W for
        direct usage in Annex models.

        Only person (convective and radiative) and machines (convective) are
        used in the simple Annex 60 examples.

        1. Column : time step
        2 Column : profile_persons, radiative
        3 Column : profile_persons, convective
        4 Column : profile_machines, convective

        Note
        ----------
        When time line is created, we need to add a 0 to first element of
        all boundaries. This is due to to expected format in Modelica.

        Parameters
        ----------
        zone : ThermalZone()
            TEASER instance of ThermalZone. As IBPSA computes single models
            for single zones, we need to generate individual files for zones
            and internal gains
        time_line :[[int]]
            list of time steps
        path : str
            optional path, when matfile is exported separately
        """

        if path is None:
            path = utilities.get_default_path()
        else:
            pass

        utilities.create_path(path)
        path = os.path.join(path, self.file_internal_gains)

        if time_line is None:
            duration = len(zone.use_conditions.profile_persons) * \
                3600
            time_line = self.create_profile(duration_profile=duration)

        ass_error_1 = "time line and input have to have the same length"

        assert len(time_line) - 1 == len(
            zone.use_conditions.profile_persons), \
            (ass_error_1 + ",profile_persons")
        assert len(time_line) - 1 == len(
            zone.use_conditions.profile_machines), \
            (ass_error_1 + ",profile_machines")

        for i, time in enumerate(time_line):
            if i == 0:
                time.append(0)
                time.append(0)
                time.append(0)
            else:
                time.append(zone.use_conditions.profile_persons[i - 1] *
                            zone.use_conditions.persons *
                            zone.use_conditions.activity_type_persons * 50 *
                            (1 - zone.use_conditions.ratio_conv_rad_persons))
                time.append(zone.use_conditions.profile_persons[i - 1] *
                            zone.use_conditions.persons *
                            zone.use_conditions.activity_type_persons * 50 *
                            zone.use_conditions.ratio_conv_rad_persons)
                time.append(zone.use_conditions.profile_machines[i - 1] *
                            zone.use_conditions.machines *
                            zone.use_conditions.activity_type_machines * 50)

        internal_boundary = np.array(time_line)

        scipy.io.savemat(
            path,
            mdict={'Internals': internal_boundary},
            appendmat=False,
            format='4')
