# Created December 2016
# TEASER 4 Development Team

"""This module includes AixLib calculation class
"""

import scipy.io
import teaser.logic.utilities as utilities
import numpy as np
import warnings
import os


class AixLib(object):
    """AixLib Class

    This class holds functions to sort and partly rewrite zone and building
    attributes specific for AixLib MultizoneEquipped
    simulation. This includes the export of boundary conditions and AHU
    operation values.

    Parameters
    ----------

    parent: Building()
        The parent class of this object, the Building the attributes are
        calculated for. (default: None)


    Attributes
    ----------

    file_set_t : str
        Filename for set temperature file
    file_ahu : str
        Filename for AHU boundary conditions file
    file_intern_gains:
        Filename for internal gains file
    version : str
        Used AixLib version, default should always be current master version
        of GitHub
    total_surface_area : float [m2]
        This is the total surface area of the building for interior and
        exterior surfaces. That includes: OuterWalls, Rooftops, GroundFloors,
        Windows for exterior surfaces, and InnerWalls, Ceilings, Floors for
        interior walls.
    consider_heat_capacity : bool
        decides whether air capacity is considered or not for all thermal
        zones in the building
    """

    def __init__(self, parent):

        self.parent = parent

        self.file_set_t = "Tset_" + self.parent.name + ".mat"
        self.file_ahu = "AHU_" + self.parent.name + ".mat"
        self.file_internal_gains = "InternalGains_" + self.parent.name + ".mat"
        self.version = "0.4.0"
        self.total_surface_area = None
        self.consider_heat_capacity = True


    def calc_auxiliary_attr(self):
        """Calls function to calculate all auxiliary attributes for AixLib"""

        self._calc_surface_area()

    def _calc_surface_area(self):
        """Calculates the total surface area of all surfaces"""
        surf_area_temp = 0.0
        for zone in self.parent.thermal_zones:
            surf_area_temp += (
                zone.model_attr.area_ow +
                zone.model_attr.area_iw +
                zone.model_attr.area_win)
        self.total_surface_area = surf_area_temp

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
        ass_error_1 = "duration musst be a multiple of time_step"

        assert float(duration_profile/time_step).is_integer(), ass_error_1

        time_line = []

        for i in range(int(duration_profile/time_step)+1):
            time_line.append([i*time_step])
        return time_line

    def modelica_set_temp(self, path=None):
        """creates .mat file for set temperatures

        This function creates a matfile (-v4) for set temperatures of each
        zone, that are all saved into one matrix.

        1. Row: heat set temperature of all zones
        2. Row: cool set temperature of all zones

        Parameters
        ----------
        path : str
            optional path, when matfile is exported seperately
        """

        if path is None:
            path = utilities.get_default_path()
        else:
            pass

        utilities.create_path(path)
        path = os.path.join(path, self.file_set_t)

        t_set_heat = [0]

        for zone_count in self.parent.thermal_zones:
            t_set_heat.append(zone_count.use_conditions.set_temp_heat)

        scipy.io.savemat(
            path,
            mdict={'Tset': [t_set_heat]},
            appendmat=False,
            format='4')

    def modelica_AHU_boundary(self, time_line=None, path=None):
        """creates .mat file for AHU boundary conditions (building)

        This function creates a matfile (-v4) for building AHU boundary
        conditions

        1. Column : time step
        2. Column : desired AHU profile temperature
        3. Column : Desired minimal relative humidity
        4. Column : desired maximal relative humidity
        5. Column : AHU status (On/Off)

        Parameters
        ----------
        time_line :[[int]]
            list of time steps
        path : str
            optional path, when matfile is exported seperately

        Attributes
        ----------
        profile_temperature : [float]
            timeline of temperatures requirements for AHU simulation
        profile_min_relative_humidity : [float]
            timeline of relative humidity requirements for AHU simulation
        profile_max_relative_humidity : [float]
            timeline of relative humidity requirements for AHU simulation
        profile_v_flow : [int]
            timeline of desired relative v_flow of the AHU simulation (0..1)

        """

        if path is None:
            path = utilities.get_default_path()
        else:
            pass

        utilities.create_path(path)
        path = os.path.join(path, self.file_ahu)

        if time_line is None:
            time_line = self.create_profile()

        if self.parent.with_ahu is True:
            profile_temperature = \
                self.parent.central_ahu.profile_temperature
            profile_min_relative_humidity = \
                self.parent.central_ahu.profile_min_relative_humidity
            profile_max_relative_humidity = \
                self.parent.central_ahu.profile_max_relative_humidity
            profile_v_flow = \
                self.parent.central_ahu.profile_v_flow
        else:
            # Dummy values for Input Table
            time_line = [[0], [3600]]
            profile_temperature = [293.15, 293.15]
            profile_min_relative_humidity = [0, 0]
            profile_max_relative_humidity = [1, 1]
            profile_v_flow = [0, 1]

        ass_error_1 = "time line and input have to have the same length"

        assert len(time_line) == len(profile_temperature), \
            (ass_error_1 + ",profile_temperature_AHU")
        assert len(time_line) == len(profile_min_relative_humidity), \
            (ass_error_1 + ",profile_min_relative_humidity")
        assert len(time_line) == len(profile_max_relative_humidity),\
            (ass_error_1 + ",profile_max_relative_humidity")
        assert len(time_line) == len(profile_v_flow), \
            (ass_error_1 + ",profile_status_AHU")

        for i, time in enumerate(time_line):

            time.append(profile_temperature[i])
            time.append(profile_min_relative_humidity[i])
            time.append(profile_max_relative_humidity[i])
            time.append(profile_v_flow[i])

        ahu_boundary = np.array(time_line)

        scipy.io.savemat(
            path,
            mdict={'AHU': ahu_boundary},
            appendmat=False,
            format='4')

    def modelica_gains_boundary(
            self,
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
        time_line :[[int]]
            list of time steps
        path : str
            optional path, when matfile is exported seperately
        """

        if path is None:
            path = utilities.get_default_path()
        else:
            pass

        utilities.create_path(path)
        path = os.path.join(path, self.file_internal_gains)

        for zone_count in self.parent.thermal_zones:
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
