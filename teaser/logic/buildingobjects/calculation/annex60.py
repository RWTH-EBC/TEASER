# Created December 2016
# TEASER 4 Development Team

"""This module includes Annex60 calcuation class
"""

import scipy.io
import teaser.logic.utilities as utilities
import numpy as np
import warnings
import os

class Annex60(object):
    """Annex60 Class

    This class holds functions to sort and partly rewrite zone and building
    attributes specific for Annex60 simulation. This includes the export of
    boundary coniditons.

    Parameters
    ----------

    parent: Building()
        The parent class of this object, the Building the attributes are
        calculated for. (default: None)
    consider_heat_capacity : bool
        decides whether air capacity is considered or not for all thermal
        zones in the building

    """

    def __init__(self, parent):

        self.parent = parent
        self.file_internal_gains = "InternalGains_" + self.parent.name + ".mat"
        self.version = "0.1"
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
        boundary conditions. It collects all internal gain profiles of the
        zones and stores them into one file. The file is extended for each
        zone. Only applicable if zones are defined

        1. Column : time step
        2,5,8,...  Column : profile_persons
        3,6,9,...  Column : profile_machines
        4,7,10,... Column : profile_lighting

        Note
        ----------
        When time line is created, we need to add a 0 to first element of
        all boundaries. This is due to to expected format in Modelica.

        Parameters
        ----------
        zone : ThermalZone()
            TEASER instance of ThermalZone. As Annex60 computes single models
            for single zones, we need to generate individual files for zones
            and internal gains
        time_line :[[int]]
            list of time steps
        path : str
            optional path, when matfile is exported seperately
        """

        # TODO: calculate from relative to absolut W and pass over exact zone

        if path is None:
            path = utilities.get_default_path()
        else:
            pass

        utilities.create_path(path)
        path = os.path.join(path, self.file_internal_gains)

        zone_count = self.parent.thermal_zones[-1]
        if time_line is None:
            duration = len(zone_count.use_conditions.profile_persons) * \
                        3600
            time_line = self.create_profile(duration_profile=duration)

        ass_error_1 = "time line and input have to have the same length"

        assert len(time_line)-1 == len(
            zone_count.use_conditions.profile_persons), \
            (ass_error_1 + ",profile_persons")
        assert len(time_line)-1 == len(
            zone_count.use_conditions.profile_machines), \
            (ass_error_1 + ",profile_machines")
        assert len(time_line)-1 == len(
            zone_count.use_conditions.profile_lighting), \
            (ass_error_1 + ",profile_lighting")

        for i, time in enumerate(time_line):
            if i == 0:
                time.append(0)
                time.append(0)
                time.append(0)
            else:
                time.append(zone_count.use_conditions.profile_persons[i-1])
                time.append(zone_count.use_conditions.profile_machines[i-1])
                time.append(zone_count.use_conditions.profile_lighting[i-1])

        internal_boundary = np.array(time_line)

        scipy.io.savemat(
            path,
            mdict={'Internals': internal_boundary},
            appendmat=False,
            format='4')

