#Created December 2016
#TEASER 4 Development Team

"""This module includes AixLib calcuation class
"""

import scipy.io
import teaser.logic.utilities as utilitis
import numpy as np
import warnings


class AixLib(object):
    """AixLib Class

    This class holds functions to sort and aprtly rewrite zone and building
    attributes specific for AixLib Multizone and MultizoneEquipped
    simulation. This includes the export of boundary conditions and AHU
    operation values.

    Parameters
    ----------

    parent: Building()
        The parent class of this object, the Building the attributes are
        calculated for. (default: None)


    Attributes
    ----------

    self.file_ahu = None
self.file_internal_gains = None
self.file_set_t = None
self.file_weather = None
self.orientation_bldg = []
self.tilt_bldg = []
self.orient_tilt = []

    """

    def __init__(self, parent):

        self.parent = parent

    def compare_orientation(self):
        """Compares orientation of walls of all zones and sorts them

        Fills the weighfactors of every zone according to orientation and
        tilt of all zones of the buildings. Therefore it compares orientation
        and tilt of all outer building elements and then creates lists for zone
        weightfactors, orientation, tilt, ares and sunblinds.

        Attributes
        ----------

        orient_tilt_help : list of tuples
            List with of all occurring combinations of (orientation, tilt) of
            all outer elements of the building
        """

        orient_tilt_help = []
        self.parent.orient_tilt = []
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
            if i in self.parent.orient_tilt:
                pass
            else:
                self.parent.orient_tilt.append(i)

        self.parent.orient_tilt.sort(key=lambda x: x[0])

        if self.parent.orient_tilt[0][0] == -1:
            self.parent.orient_tilt.insert(
                len(self.parent.orient_tilt),
                self.parent.orient_tilt.pop(0))

        for i in self.parent.orient_tilt:
            self.parent.orientation_bldg.append(i[0])
            self.parent.tilt_bldg.append(i[1])

        for zone in self.parent.thermal_zones:

            groundfloors = zone.find_gfs(-2, 0)
            if not groundfloors:
                zone.model_attr.weightfactor_ground.append(0.0)
            else:
                zone.model_attr.weightfactor_ground.append(
                    sum([groundfl.wf_out for groundfl in groundfloors]))

            for i in self.parent.orient_tilt:
                walls_roofs = zone.find_walls(i[0], i[1]) + \
                              zone.find_rts(i[0], i[1])
                wins = zone.find_wins(i[0], i[1])

                zone.model_attr.tilt_wall.append(i[1])
                zone.model_attr.orientation_wall.append(i[0])

                zone.model_attr.tilt_win.append(i[1])
                zone.model_attr.orientation_win.append(i[0])

                if not walls_roofs:
                    zone.model_attr.weightfactor_ow.append(0.0)
                    zone.model_attr.outer_walls_areas.append(0.0)
                else:
                    zone.model_attr.weightfactor_ow.append(
                        sum([wall.wf_out for wall in walls_roofs]))
                    [zone.model_attr.outer_walls_areas.append(i.area) for i in walls_roofs]
                if not wins:
                    zone.model_attr.weightfactor_win.append(0.0)
                    zone.model_attr.window_area_list.append(0.0)
                    zone.model_attr.g_sunblind_list.append(0.0)
                    zone.model_attr.window_areas.append(0.0)
                else:
                    zone.model_attr.weightfactor_win.append(
                        sum([win.wf_out for win in wins]))
                    zone.model_attr.window_area_list.append(
                        sum([win.area for win in wins]))
                    zone.model_attr.g_sunblind_list.append(
                        sum([win.shading_g_total for win in wins]))
                    # TODO what is this value needed for?
                    [zone.model_attr.window_areas.append(i.area) for i in wins]


    def create_timeline(bldg, duration_profile = 86400, time_step = 3600):
        ''' Creates a timeline for building boundary conditions

        This function creates a list with a equidistant timeline given the
        duration of the profile in seconds (default one day, 86400 s) and the
        time_step in seconds (default one hour, 3600 s). Needed for boundary
        input of the building for Modelica simulation

        Note
        ----------
        As Python starts from counting the range from zero, but Modelica needs
        0 as start value and additional 24 entries. We add one interation
        step in the time line.

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
        '''
        ass_error_1 = "duration musst be a multiple of time_step"

        assert float(duration_profile/time_step).is_integer(), ass_error_1

        time_line = []

        for i in range(int(duration_profile/time_step)+1):
            time_line.append([i*time_step])
        return time_line

    def modelica_set_temp(bldg, path = None):
        '''creates .mat file for set temperatures for each zone

        This function creates a matfile (-v4) for set temperatures of each
        zone

        !AixLib sepcific!

        1. Row: heat set temperature of all zones
        2. Row: cool set temperature of all zones

        Parameters
        ----------
        path : str
            optional path, when matfile is exported seperately

        '''

        if bldg.file_set_t is None:
            bldg.file_set_t = "/Tset_"+bldg.name+".mat"
        else:
            pass

        if path is None:
            path = utilitis.get_default_path()
        else:
            pass

        utilitis.create_path(path)
        path = path + bldg.file_set_t

        t_set_heat = [0]

        for zone_count in bldg.thermal_zones:
            t_set_heat.append(zone_count.use_conditions.set_temp_heat)

        scipy.io.savemat(path,
                         mdict={'Tset': [t_set_heat]},
                         appendmat = False,
                         format = '4')


    def modelica_AHU_boundary(bldg,
                              time_line = None,
                              path = None):
        '''creates .mat file for AHU boundary conditions (building)

        This function creates a matfile (-v4) for building AHU boundary
        conditions

        !AixLib sepcific!

        Known limitation:

        1. Column : time step
        2. Column : desired AHU profile temperature
        3. Column : Desired minimal relative humidity
        4. Column : desired maximal relative humidity
        5. Columb : AHU status (On/Off)

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

        '''

        if bldg.file_ahu is None:
            bldg.file_ahu = "/AHU_"+bldg.name+".mat"
        else:
            pass

        if path is None:
            path = utilitis.get_default_path()
        else:
            pass

        utilitis.create_path(path)
        path = path + bldg.file_ahu

        if time_line is None:
            time_line = create_timeline(bldg)
        if bldg.with_ahu is True:
            profile_temperature = \
                        bldg.central_ahu.profile_temperature
            profile_min_relative_humidity = \
                        bldg.central_ahu.profile_min_relative_humidity
            profile_max_relative_humidity = \
                        bldg.central_ahu.profile_max_relative_humidity
            profile_v_flow = \
                        bldg.central_ahu.profile_v_flow
        else:
            #Dummy values for Input Table (based on discussion with pme)
            time_line = [[0],[3600]]
            profile_temperature = [293.15,293.15]
            profile_min_relative_humidity = [0,0]
            profile_max_relative_humidity = [1,1]
            profile_v_flow = [0,1]


        ass_error_1 = "time line and input have to have the same length"

        assert len(time_line) == len(profile_temperature), \
                            (ass_error_1 + ",profile_temperature_AHU")
        assert len(time_line) == len(profile_min_relative_humidity), \
                            (ass_error_1 + ",profile_min_relative_humidity")
        assert len(time_line) == len(profile_max_relative_humidity), \
                            (ass_error_1 + ",profile_max_relative_humidity")
        assert len(time_line) == len(profile_v_flow), \
                            (ass_error_1 + ",profile_status_AHU")


        for i, time in enumerate(time_line):

            time.append(profile_temperature[i])
            time.append(profile_min_relative_humidity[i])
            time.append(profile_max_relative_humidity[i])
            time.append(profile_v_flow[i])

        ahu_boundary = np.array(time_line)

        scipy.io.savemat(path,
                         mdict={'AHU': ahu_boundary},
                         appendmat = False,
                         format = '4')

    def modelica_gains_boundary(bldg,
                                time_line = None,
                                path = None):
        '''creates .mat file for internal gains boundary conditions (building)

        This function creates a matfile (-v4) for building internal gains
        boundary conditions. It collects all internal gain profiles of the
        zones and stores them into one file. The file is extended for each
        zone. Only applicable if zones are defined

        !AixLib sepcific!

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

        '''

        if bldg.file_internal_gains is None:
            bldg.file_internal_gains = "/InternalGains_"+bldg.name+".mat"
        else:
            pass

        if path is None:
            path = utilitis.get_default_path()
        else:
            pass

        utilitis.create_path(path)
        path = path + bldg.file_internal_gains

        for zone_count in bldg.thermal_zones:
            if time_line is None:
                duration= len(zone_count.use_conditions.profile_persons) * \
                            3600
                time_line = create_timeline(bldg=bldg,
                                            duration_profile = duration)

    #            zone_count.use_conditions.profile_persons.insert(0,0)
    #            zone_count.use_conditions.profile_machines.insert(0,0)
    #            zone_count.use_conditions.profile_lighting.insert(0,0)

            ass_error_1 = "time line and input have to have the same length"

            assert len(time_line)-1 == len(zone_count.use_conditions.profile_persons), \
                                (ass_error_1 + ",profile_persons")
            assert len(time_line)-1 == len(zone_count.use_conditions.profile_machines), \
                                (ass_error_1 + ",profile_machines")
            assert len(time_line)-1 == len(zone_count.use_conditions.profile_lighting), \
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

    #            zone_count.use_conditions.profile_persons.pop(0)
    #            zone_count.use_conditions.profile_machines.pop(0)
    #            zone_count.use_conditions.profile_lighting.pop(0)
        internal_boundary = np.array(time_line)

        scipy.io.savemat(path,
                         mdict={'Internals': internal_boundary},
                         appendmat=False,
                         format='4')
