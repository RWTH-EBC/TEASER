# -*- coding: utf-8 -*-


class SimulationVDI6007(object):
    """Simulation Class for TEASER VDI 6007 Based Simulations

    This Simulation class provides the handling of the simulation logic used
    in the VDI 6007.

    Parameters
    ----------

    thermal_zone : instance of ThermalZone()
        This parameter contains the ThermalZone object related to the
        simulation

    transparent_areastributes
    ----------

    weather : object
        Weather class containing weather informations and VDI required weather
        calculations like equal air temperatures

    indoor_air_temperature = array [K]
        This array contains the indoor_air_temperature values after the
        simulation

    q_flow_heater_cooler = array
        This array contains the heat load of after the simulation with
        positive (Heating) and negative (Cooling) values

    heater_limit : list
        The heater limit list sets the maximum heat flow value for the heater
        ToDo: we should think of standard values calculated by the normative
        heat load

    cooler_limit : list
        The cooler limit list sets the maximum heat flow value for the cooler


        """
    def __init__(self, thermal_zone):

        self.thermal_zone = thermal_zone

        self.weather = None
        self.indoor_air_temperature = None
        self.q_flow_heater_cooler = None

        self.heater_limit = [1e10, 1e10, 1e10]
        self.cooler_limit = [-1e10, -1e10, -1e10]

        self.initial_air_temp = 295.15
        self.initial_inner_wall_temp = 295.15
        self.initial_outer_wall_temp = 295.15

    def calc_reduced_order_model(
            weather_temperature,
            solar_rad_in,
            equal_air_temp,
            alpha_rad,
            q_internal_gains_conv,
            q_internal_gains_rad,
            internal_gains_convective_radiative_split_factor,
            t_set_heating,
            t_set_cooling,
            heater_order,
            cooler_order):

        """Compute indoor air temperature and necessary (convective) heat gains
        from an ideal heater/cooler based on the VDI 6007-1 model.

        Parameters
        ----------

        weatherTemperature : List of Float [K]
            Environment temperatures

        solar_rad_in : 2d-array (float) [W/m2]
            Solar radiation input on each external area

        equal_air_temp : List of floats [K]
            Equal air temperature based on the vdi

        alpha_rad : List of floats [W/m2K]
            Radiative heat transfer coefficient between inner and outer walls

        q_internal_gains_conv : List if floats [W]
            convective internal gains

        q_interal_gains_rad : List of floats [W]
            radiative internal gains

        internal_gains_convective_radiative_split_factor : float
            split factor between convective and radiative internal gains

        t_set_heating : list of floats [K] (Move to Init?)
            Heating set temperatures. If the air temperature without heating
            drops below this temperature, a heating load that just
            fulfills this temperature is computed

        t_set_cooling : list of floats [K] (Move to Init?)
            Cooling set temperatures. If the air temperature without heating
            rises above this temperature, a cooling load that just fulfills
            this temperature is computed

        heater_order : list of int
            describes in which order the different heating devices are turned
            on

        cooler_order : list of int
            describes in which order the different cooling devices are turned
            on
        """

        timesteps = len(alphaRad)

        # calculation Parameters
        r1_iw = thermal_zone.model_attr.r1_iw
        c1_iw = thermal_zone.model_attr.c1_iw
        area_iw = thermal_zone.model_attr.area_iw
        r_rest_ow = thermal_zone.model_attr.r_rest_ow
        r1_ow = thermal_zone.model_attr.r1_ow
        c1_ow = thermal_zone.model_attr.c1_ow
        area_ow = [thermal_zone.model_attr.area_ow]
        window_areas = thermal_zone.model_attr.window_areas
        transparent_areas = thermal_zone.model_attr.transparent_areas
        volume = thermal_zone.volume
        density_air = thermal_zone.density_air
        heat_capac_air = thermal_zone.heat_capac_air
        ratio_conv_rad_inner_win =\
            thermal_zone.model_attr.ratio_conv_rad_inner_win
        weighted_g_value = thermal_zone.model_attr.weighted_g_value
        alpha_comb_inner_iw = thermal_zone.model_attr.alpha_comb_inner_iw
        alpha_comb_inner_ow = thermal_zone.model_attr.alpha_comb_inner_ow
        alpha_wall = thermal_zone.model_attr.alpha_comb_outer_ow *\
            thermal_zone.model_attr.area_ow

        A_win_tot = sum(window_areas)
        Ao_tot = sum(area_ow)
        A_ar = [Ao_tot, A_win_tot, area_iw]

        r_rest_ow = r_rest_ow + 1 / alpha_wall

        e_solar_conv = np.zeros((timesteps, len(transparent_areas)))

        for i in range(len(transparent_areas)):
            e_solar_conv[:, i] = solarRad_in[:, i] *\
                ratio_conv_rad_inner_win * weighted_g_value *\
                transparent_areas[i]
        q_solar_conv = np.sum(e_solar_conv, axis=1)

        # splitters:
        # on each splitter: one output goes to outer wall, one goes to inner
        # wall therefore dimension is 2 if inner walls exist => 2 outgoing
        # signals
        split_fac_solar = self.calc_splitfactors(
            len(area_ow), A_ar, area_ow, window_areas)

        # therm. splitter solar radiative:
        e_solar_rad = np.zeros((timesteps, len(transparent_areas)))
        for i in range(len(transparent_areas)):
            e_solar_rad[:, i] = solarRad_in[:, i] * (
                ratio_conv_rad_inner_win - 1) * weighted_g_value *\
                transparent_areas[i]
        q_solar_rad = np.zeros((
            timesteps,
            len(area_ow),
            split_fac_solar.shape[0]))
        for i in range(len(area_ow)):
            for j in range(split_fac_solar.shape[0]):
                q_solar_rad[:, i, j] = -e_solar_rad[:, i] * split_fac_solar[
                    j, i]

        q_solarRadToInnerWall = np.sum(q_solar_rad[:, :, 1], axis=1)
        q_solarRadToOuterWalli = np.sum(q_solar_rad[:, :, 0], axis=1)

        # Results' initialization
        t_ow = []
        t_owi = []
        t_iw = []
        t_iwi = []
        t_air = []
        q_air = []
        q_air_hc = []
        q_iw_hc = []
        q_ow_hc = []

        # Initial temperatures
        t_ow_prev = t_ow_init
        t_iw_prev = t_iw_init
        t_air_prev = t_air_init

        for t in range(timesteps):
            # Common equations
            A = np.zeros((9, 9))
            rhs = np.zeros(A.shape[0])

            # Fill matrix coefficients
            A[0, 0] = c1_ow / dt + 1 / r_rest_ow + 1 / r1_ow
            A[0, 1] = -1 / r1_ow
            A[1, 0] = 1 / r1_ow
            A[1, 1] = - min(Ao_tot, area_iw) * alphaRad[t] - Ao_tot *\
                alpha_comb_inner_ow - 1 / r1_ow
            A[1, 3] = min(Ao_tot, area_iw) * alphaRad[t]
            A[1, 4] = Ao_tot * alpha_comb_inner_ow
            A[1, 8] = 1
            A[2, 2] = c1_iw / dt + 1 / r1_iw
            A[2, 3] = -1 / r1_iw
            A[3, 1] = min(Ao_tot, area_iw) * alphaRad[t]
            A[3, 2] = 1 / r1_iw
            A[3, 3] = -min(Ao_tot, area_iw) * alphaRad[t] - area_iw *\
                alpha_comb_inner_iw - 1 / r1_iw
            A[3, 4] = area_iw * alpha_comb_inner_iw
            A[3, 7] = 1
            A[4, 1] = Ao_tot * alpha_comb_inner_ow
            A[4, 3] = area_iw * alpha_comb_inner_iw
            A[4, 4] = -Ao_tot * alpha_comb_inner_ow - area_iw *\
                alpha_comb_inner_iw - ventRate[t] * heat_capac_air *\
                density_air
            A[4, 5] = -1
            A[4, 6] = 1
            A[5, 4] = volume * heat_capac_air * density_air / dt
            A[5, 5] = -1

            # Fill right hand side
            rhs[0] = equalAirTemp[t] / r_rest_ow + c1_ow * t_ow_prev / dt
            rhs[1] = -q_solarRadToOuterWalli[t] - Q_loadsToOuterWalli[t]
            rhs[2] = c1_iw * t_iw_prev / dt
            rhs[3] = -q_solarRadToInnerWall[t] - Q_loadsToInnerWall[t]
            rhs[4] = -ventRate[t] * heat_capac_air * density_air *\
                weatherTemperature[t] - q_solar_conv[t] - Q_ig[t]
            rhs[5] = density_air * heat_capac_air * volume * t_air_prev / dt

            # Calculate current time step
            x = self.calc_timestep(
                A,
                rhs,
                t_set_heating[t],
                t_set_cooling[t],
                heater_limit[t, :],
                cooler_limit[t, :],
                heater_order,
                cooler_order)

            # Retrieve results
            t_ow.append(x[0])
            t_owi.append(x[1])
            t_iw.append(x[2])
            t_iwi.append(x[3])
            t_air.append(x[4])
            q_air.append(x[5])
            q_air_hc.append(x[6])
            q_iw_hc.append(x[7])
            q_ow_hc.append(x[8])

            # Update initial temperatures
            t_ow_prev = x[0]
            t_iw_prev = x[2]
            t_air_prev = x[4]

            self.indoor_air_temperature = np.array(t_air)
            self.q_flow_heater_cooler = np.array(q_air_hc)

        return (np.array(t_air), np.array(q_air_hc))

    def calc_splitfactors(cols, a_array, a_ext, a_win):
        """
        This function calculates the split factors

        Parameters
        ----------
        cols : int
            Number of orientations
        a_array : list
            [ATotExt, ATotWin]
        a_ext : list
            Vector of exterior wall areas
        a_win : list
            Vector of window areas

        Example
        -------
        >>> # Define areas
        >>> a_ext = [10.5]
        >>> a_win = [0]
        >>> A_int = 75.5
        >>> A_ar = [sum(a_ext), sum(a_win), A_int]
        >>> # Calculate split factors for inner walls and outside walls
        >>> splitFac_IW = _calc_splitfactors(dim, 1, A_ar, [0], [0])
        >>> splitFac_OW = _calc_splitfactors(dim, len(a_ext), A_ar, a_ext,
        a_win)
        """

        a_tot = sum(a_array)  # total area

        rows = sum([1 if a > 0 else 0 for a in a_array])
        rows = len(a_array)

        # Counters
        i = 0  # a_array
        j = 0  # Row
        k = 0  # Column

        result = np.zeros((rows, cols))

        for a in a_array:
            if a > 0:
                k = 0
                if i == 0:
                    for a_wall in a_ext:
                        result[j, k] = (a - a_wall) / (
                            a_tot - a_wall - a_win[k])
                        k += 1
                elif i == 1:
                    for a_wall in a_ext:
                        result[j, k] = (a - a_win[k]) / (
                            a_tot - a_wall - a_win[k])
                        k += 1
                else:
                    for a_wall in a_ext:
                        result[j, k] = a / (a_tot - a_wall - a_win[k])
                        k += 1
                j += 1
            i += 1

        return result

    def calc_timestep(
        A,
        rhs,
        t_set_heating=291.15,
        t_set_cooling=300.15,
        heater_order=np.array([1, 2, 3]),
        cooler_order=np.array([1, 2, 3])):

        """
        Calculate the temperatures and heat flow rate for the current time step

        Parameters
        ----------
        A : 2d array of floats
            Coefficients describing the VDI model
        rhs : Array of floats
            Right hand side of these equations
        t_set_heating : Float (Move to Init?)
            Temperature below which heating demand is computed (in Kelvin)
        t_set_cooling : Float (Move to Init?)
            Temperature above which cooling demand is computed (in Kelvin)
        """
        # Calculate without further heat inputs to determine if heating 
        # or cooling is needed
        # x = [T_ow, T_owi, T_iw, T_iwi, T_air, Q_air, Q_HC]
        x_noHeat = _calc_temperatue(
            A, rhs, q_air_fix=0, q_iw_fix=0, q_ow_fix=0)

        if x_noHeat[4] < t_set_heating:
            # Indoor air temperature below heating set temperature

            # Use primary heater
            if np.argmax(heater_order == 1) == 0 and heater_limit[0] > 0:
                x_heating_1 = _calc_heatflow(
                    A,
                    rhs,
                    t_air_set=t_set_heating,
                    q_air_fix=None,
                    q_iw_fix=0,
                    q_ow_fix=0)

                if x_heating_1[6] > heater_limit[0]:
                    x_maxheat_1 = _calc_temperatue(
                        A,
                        rhs,
                        q_air_fix=heater_limit[0],
                        q_iw_fix=0,
                        q_ow_fix=0)

                    if x_maxheat_1[4] < t_set_heating:
                        if np.argmax(heater_order == 2) == 1 and\
                           heater_limit[1] > 0:
                            x_heating_2 = _calc_heatflow(
                                A, rhs,
                                t_air_set=t_set_heating,
                                q_air_fix=heater_limit[0],
                                q_iw_fix=None, q_ow_fix=0)

                            if x_heating_2[7] > heater_limit[1]:
                                x_maxheat_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=heater_limit[0],
                                    q_iw_fix=heater_limit[1],
                                    q_ow_fix=0)

                                if x_maxheat_2[4] < t_set_heating and\
                                   heater_limit[2] > 0:
                                    x_heating_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_heating,
                                        q_air_fix=heater_limit[0],
                                        q_iw_fix=heater_limit[1],
                                        q_ow_fix=None)

                                    if x_heating_3[8] > heater_limit[2]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=heater_limit[0],
                                            q_iw_fix=heater_limit[1],
                                            q_ow_fix=heater_limit[2])
                                    else:
                                        return x_heating_3
                                else:
                                    return x_maxheat_2
                            else:
                                return x_heating_2
                        elif np.argmax(heater_order == 2) == 2 and\
                             heater_limit[2] > 0:
                            x_heating_2 = _calc_heatflow(
                                A,
                                rhs,
                                 t_air_set=t_set_heating,
                                 q_air_fix=heater_limit[0],
                                 q_iw_fix=0, q_ow_fix=None)

                            if x_heating_2[8] > heater_limit[2]:
                                x_maxheat_2 = _calc_temperatue(
                                    A,
                                    rhs,
                                    q_air_fix=heater_limit[0],
                                    q_iw_fix=0,
                                    q_ow_fix=heater_limit[2])

                                if x_maxheat_2[4] < t_set_heating and\
                                   heater_limit[1] > 0:
                                    x_heating_3 = _calc_heatflow(
                                        A,
                                        rhs,
                                        t_air_set=t_set_heating,
                                        q_air_fix=heater_limit[0],
                                        q_iw_fix=None,
                                        q_ow_fix=heater_limit[2])

                                    if x_heating_3[7] > heater_limit[1]:
                                        return _calc_temperatue(
                                            A,
                                            rhs,
                                            q_air_fix=heater_limit[0],
                                            q_iw_fix=heater_limit[1],
                                            q_ow_fix=heater_limit[2])
                                    else:
                                        return x_heating_3
                                else:
                                    return x_maxheat_2
                            else:
                                return x_heating_2
                        else:
                            return x_maxheat_1
                else:
                    return x_heating_1
# work beginning here
            elif np.argmax(heater_order == 1) == 1 and heater_limit[1] > 0:
                x_heating_1 = _calc_heatflow(A, rhs, t_air_set=t_set_heating,
                                             q_air_fix=0, q_iw_fix=None,
                                             q_ow_fix=0)
                if x_heating_1[7] > heater_limit[1]:
                    x_maxheat_1 = _calc_temperatue(A, rhs, q_air_fix=0,
                                                   q_iw_fix=heater_limit[1],
                                                   q_ow_fix=0)

                    if x_maxheat_1[4] < t_set_heating:
                        if np.argmax(heater_order == 2) == 0 and heater_limit[
                            0] > 0:
                            x_heating_2 = _calc_heatflow(A, rhs,
                                                         t_air_set=t_set_heating,
                                                         q_air_fix=None,
                                                         q_iw_fix=heater_limit[1],
                                                         q_ow_fix=0)

                            if x_heating_2[6] > heater_limit[0]:
                                x_maxheat_2 = _calc_temperatue(A, rhs, q_air_fix=
                                heater_limit[0], q_iw_fix=heater_limit[1],
                                                               q_ow_fix=0)

                                if x_maxheat_2[4] < t_set_heating and heater_limit[
                                    2] > 0:
                                    x_heating_3 = _calc_heatflow(A, rhs,
                                                                 t_air_set=t_set_heating,
                                                                 q_air_fix=
                                                                 heater_limit[0],
                                                                 q_iw_fix=
                                                                 heater_limit[1],
                                                                 q_ow_fix=None)

                                    if x_heating_3[8] > heater_limit[2]:
                                        return _calc_temperatue(A, rhs, q_air_fix=
                                        heater_limit[0], q_iw_fix=heater_limit[1],
                                                                q_ow_fix=
                                                                heater_limit[2])
                                    else:
                                        return x_heating_3
                                else:
                                    return x_maxheat_2
                            else:
                                return x_heating_2
                        elif np.argmax(heater_order == 2) == 2 and heater_limit[
                            2] > 0:
                            x_heating_2 = _calc_heatflow(A, rhs,
                                                         t_air_set=t_set_heating,
                                                         q_air_fix=0,
                                                         q_iw_fix=heater_limit[1],
                                                         q_ow_fix=None)

                            if x_heating_2[8] > heater_limit[2]:
                                x_maxheat_2 = _calc_temperatue(A, rhs, q_air_fix=0,
                                                               q_iw_fix=
                                                               heater_limit[1],
                                                               q_ow_fix=
                                                               heater_limit[2])

                                if x_maxheat_2[4] < t_set_heating and heater_limit[
                                    0] > 0:
                                    x_heating_3 = _calc_heatflow(A, rhs,
                                                                 t_air_set=t_set_heating,
                                                                 q_air_fix=None,
                                                                 q_iw_fix=
                                                                 heater_limit[1],
                                                                 q_ow_fix=
                                                                 heater_limit[2])

                                    if x_heating_3[6] > heater_limit[0]:
                                        return _calc_temperatue(A, rhs, q_air_fix=
                                        heater_limit[0], q_iw_fix=heater_limit[1],
                                                                q_ow_fix=
                                                                heater_limit[2])
                                    else:
                                        return x_heating_3
                                else:
                                    return x_maxheat_2
                            else:
                                return x_heating_2
                        else:
                            return x_maxheat_1
                else:
                    return x_heating_1
            elif np.argmax(heater_order == 1) == 2 and heater_limit[
                2] > 0:  # no else
                x_heating_1 = _calc_heatflow(A, rhs, t_air_set=t_set_heating,
                                             q_air_fix=0, q_iw_fix=0,
                                             q_ow_fix=None)
                if x_heating_1[8] > heater_limit[2]:
                    x_maxheat_1 = _calc_temperatue(A, rhs, q_air_fix=0, q_iw_fix=0,
                                                   q_ow_fix=heater_limit[2])

                    if x_maxheat_1[4] < t_set_heating:
                        if np.argmax(heater_order == 2) == 0 and heater_limit[
                            0] > 0:
                            x_heating_2 = _calc_heatflow(A, rhs,
                                                         t_air_set=t_set_heating,
                                                         q_air_fix=None,
                                                         q_iw_fix=0,
                                                         q_ow_fix=heater_limit[2])

                            if x_heating_2[6] > heater_limit[0]:
                                x_maxheat_2 = _calc_temperatue(A, rhs, q_air_fix=
                                heater_limit[0], q_iw_fix=0, q_ow_fix=heater_limit[
                                    1])

                                if x_maxheat_2[4] < t_set_heating and heater_limit[
                                    1] > 0:
                                    x_heating_3 = _calc_heatflow(A, rhs,
                                                                 t_air_set=t_set_heating,
                                                                 q_air_fix=
                                                                 heater_limit[0],
                                                                 q_iw_fix=None,
                                                                 q_ow_fix=
                                                                 heater_limit[2])

                                    if x_heating_3[7] > heater_limit[1]:
                                        return _calc_temperatue(A, rhs, q_air_fix=
                                        heater_limit[0], q_iw_fix=heater_limit[1],
                                                                q_ow_fix=
                                                                heater_limit[2])
                                    else:
                                        return x_heating_3
                                else:
                                    return x_maxheat_2
                            else:
                                return x_heating_2
                        elif np.argmax(heater_order == 2) == 1 and heater_limit[
                            1] > 0:
                            x_heating_2 = _calc_heatflow(A, rhs,
                                                         t_air_set=t_set_heating,
                                                         q_air_fix=0,
                                                         q_iw_fix=None,
                                                         q_ow_fix=heater_limit[2])

                            if x_heating_2[7] > heater_limit[1]:
                                x_maxheat_2 = _calc_temperatue(A, rhs, q_air_fix=0,
                                                               q_iw_fix=
                                                               heater_limit[1],
                                                               q_ow_fix=
                                                               heater_limit[2])

                                if x_maxheat_2[4] < t_set_heating and heater_limit[
                                    0] > 0:
                                    x_heating_3 = _calc_heatflow(A, rhs,
                                                                 t_air_set=t_set_heating,
                                                                 q_air_fix=None,
                                                                 q_iw_fix=
                                                                 heater_limit[1],
                                                                 q_ow_fix=
                                                                 heater_limit[2])

                                    if x_heating_3[6] > heater_limit[0]:
                                        return _calc_temperatue(A, rhs, q_air_fix=
                                        heater_limit[0], q_iw_fix=heater_limit[1],
                                                                q_ow_fix=
                                                                heater_limit[2])
                                    else:
                                        return x_heating_3
                                else:
                                    return x_maxheat_2
                            else:
                                return x_heating_2
                        else:
                            return x_maxheat_1
                else:
                    return x_heating_1

        elif x_noHeat[4] > t_set_cooling:
            # Indoor air temperature above cooling set temperature

            if np.argmax(cooler_order == 1) == 0 and cooler_limit[0] < 0:
                x_cooling_1 = _calc_heatflow(A, rhs, t_air_set=t_set_cooling,
                                             q_air_fix=None, q_iw_fix=0,
                                             q_ow_fix=0)
                if x_cooling_1[6] < cooler_limit[0]:
                    x_maxcool_1 = _calc_temperatue(A, rhs,
                                                   q_air_fix=cooler_limit[0],
                                                   q_iw_fix=0, q_ow_fix=0)

                    if x_maxcool_1[4] > t_set_cooling:
                        if np.argmax(cooler_order == 2) == 1 and cooler_limit[
                            1] < 0:
                            x_cooling_2 = _calc_heatflow(A, rhs,
                                                         t_air_set=t_set_cooling,
                                                         q_air_fix=cooler_limit[0],
                                                         q_iw_fix=None, q_ow_fix=0)

                            if x_cooling_2[7] < cooler_limit[1]:
                                x_maxcool_2 = _calc_temperatue(A, rhs, q_air_fix=
                                cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                               q_ow_fix=0)

                                if x_maxcool_2[4] > t_set_cooling and cooler_limit[
                                    2] < 0:
                                    x_cooling_3 = _calc_heatflow(A, rhs,
                                                                 t_air_set=t_set_cooling,
                                                                 q_air_fix=
                                                                 cooler_limit[0],
                                                                 q_iw_fix=
                                                                 cooler_limit[1],
                                                                 q_ow_fix=None)

                                    if x_cooling_3[8] < cooler_limit[2]:
                                        return _calc_temperatue(A, rhs, q_air_fix=
                                        cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                                q_ow_fix=
                                                                cooler_limit[2])
                                    else:
                                        return x_cooling_3
                                else:
                                    return x_maxcool_2
                            else:
                                return x_cooling_2
                        elif np.argmax(cooler_order == 2) == 2 and cooler_limit[
                            2] < 0:
                            x_cooling_2 = _calc_heatflow(A, rhs,
                                                         t_air_set=t_set_cooling,
                                                         q_air_fix=cooler_limit[0],
                                                         q_iw_fix=0, q_ow_fix=None)

                            if x_cooling_2[8] < cooler_limit[2]:
                                x_maxcool_2 = _calc_temperatue(A, rhs, q_air_fix=
                                cooler_limit[0], q_iw_fix=0, q_ow_fix=cooler_limit[
                                    2])

                                if x_maxcool_2[4] > t_set_cooling and cooler_limit[
                                    1] < 0:
                                    x_cooling_3 = _calc_heatflow(A, rhs,
                                                                 t_air_set=t_set_cooling,
                                                                 q_air_fix=
                                                                 cooler_limit[0],
                                                                 q_iw_fix=None,
                                                                 q_ow_fix=
                                                                 cooler_limit[2])

                                    if x_cooling_3[7] < cooler_limit[1]:
                                        return _calc_temperatue(A, rhs, q_air_fix=
                                        cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                                q_ow_fix=
                                                                cooler_limit[2])
                                    else:
                                        return x_cooling_3
                                else:
                                    return x_maxcool_2
                            else:
                                return x_cooling_2
                        else:
                            return x_maxcool_1
                else:
                    return x_cooling_1
            elif np.argmax(cooler_order == 1) == 1 and cooler_limit[1] < 0:
                x_cooling_1 = _calc_heatflow(A, rhs, t_air_set=t_set_cooling,
                                             q_air_fix=0, q_iw_fix=None,
                                             q_ow_fix=0)
                if x_cooling_1[7] < cooler_limit[1]:
                    x_maxcool_1 = _calc_temperatue(A, rhs, q_air_fix=0,
                                                   q_iw_fix=cooler_limit[1],
                                                   q_ow_fix=0)

                    if x_maxcool_1[4] > t_set_cooling:
                        if np.argmax(cooler_order == 2) == 0 and cooler_limit[
                            0] < 0:
                            x_cooling_2 = _calc_heatflow(A, rhs,
                                                         t_air_set=t_set_cooling,
                                                         q_air_fix=None,
                                                         q_iw_fix=cooler_limit[1],
                                                         q_ow_fix=0)

                            if x_cooling_2[6] < cooler_limit[0]:
                                x_maxcool_2 = _calc_temperatue(A, rhs, q_air_fix=
                                cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                               q_ow_fix=0)

                                if x_maxcool_2[4] > t_set_cooling and cooler_limit[
                                    2] < 0:
                                    x_cooling_3 = _calc_heatflow(A, rhs,
                                                                 t_air_set=t_set_cooling,
                                                                 q_air_fix=
                                                                 cooler_limit[0],
                                                                 q_iw_fix=
                                                                 cooler_limit[1],
                                                                 q_ow_fix=None)

                                    if x_cooling_3[8] < cooler_limit[2]:
                                        return _calc_temperatue(A, rhs, q_air_fix=
                                        cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                                q_ow_fix=
                                                                cooler_limit[2])
                                    else:
                                        return x_cooling_3
                                else:
                                    return x_maxcool_2
                            else:
                                return x_cooling_2
                        elif np.argmax(cooler_order == 2) == 2 and cooler_limit[
                            2] < 0:
                            x_cooling_2 = _calc_heatflow(A, rhs,
                                                         t_air_set=t_set_cooling,
                                                         q_air_fix=0,
                                                         q_iw_fix=cooler_limit[1],
                                                         q_ow_fix=None)

                            if x_cooling_2[8] < cooler_limit[2]:
                                x_maxcool_2 = _calc_temperatue(A, rhs, q_air_fix=0,
                                                               q_iw_fix=
                                                               cooler_limit[1],
                                                               q_ow_fix=
                                                               cooler_limit[2])

                                if x_maxcool_2[4] > t_set_cooling and cooler_limit[
                                    0] < 0:
                                    x_cooling_3 = _calc_heatflow(A, rhs,
                                                                 t_air_set=t_set_cooling,
                                                                 q_air_fix=None,
                                                                 q_iw_fix=
                                                                 cooler_limit[1],
                                                                 q_ow_fix=
                                                                 cooler_limit[2])

                                    if x_cooling_3[6] < cooler_limit[0]:
                                        return _calc_temperatue(A, rhs, q_air_fix=
                                        cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                                q_ow_fix=
                                                                cooler_limit[2])
                                    else:
                                        return x_cooling_3
                                else:
                                    return x_maxcool_2
                            else:
                                return x_cooling_2
                        else:
                            return x_maxcool_1
                else:
                    return x_cooling_1

            elif np.argmax(cooler_order == 1) == 2 and cooler_limit[2] < 0:
                x_cooling_1 = _calc_heatflow(A, rhs, t_air_set=t_set_cooling,
                                             q_air_fix=0, q_iw_fix=0,
                                             q_ow_fix=None)
                if x_cooling_1[8] < cooler_limit[2]:
                    x_maxcool_1 = _calc_temperatue(A, rhs, q_air_fix=0, q_iw_fix=0,
                                                   q_ow_fix=cooler_limit[2])

                    if x_maxcool_1[4] > t_set_cooling:
                        if np.argmax(cooler_order == 2) == 0 and cooler_limit[
                            0] < 0:
                            x_cooling_2 = _calc_heatflow(A, rhs,
                                                         t_air_set=t_set_cooling,
                                                         q_air_fix=None,
                                                         q_iw_fix=0,
                                                         q_ow_fix=cooler_limit[2])

                            if x_cooling_2[6] < cooler_limit[0]:
                                x_maxcool_2 = _calc_temperatue(A, rhs, q_air_fix=
                                cooler_limit[0], q_iw_fix=0, q_ow_fix=cooler_limit[
                                    2])

                                if x_maxcool_2[4] > t_set_cooling and cooler_limit[
                                    1] < 0:
                                    x_cooling_3 = _calc_heatflow(A, rhs,
                                                                 t_air_set=t_set_cooling,
                                                                 q_air_fix=
                                                                 cooler_limit[0],
                                                                 q_iw_fix=None,
                                                                 q_ow_fix=
                                                                 cooler_limit[2])

                                    if x_cooling_3[7] < cooler_limit[1]:
                                        return _calc_temperatue(A, rhs, q_air_fix=
                                        cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                                q_ow_fix=
                                                                cooler_limit[2])
                                    else:
                                        return x_cooling_3
                                else:
                                    return x_maxcool_2
                            else:
                                return x_cooling_2
                        elif np.argmax(cooler_order == 2) == 1 and cooler_limit[
                            1] < 0:
                            x_cooling_2 = _calc_heatflow(A, rhs,
                                                         t_air_set=t_set_cooling,
                                                         q_air_fix=0,
                                                         q_iw_fix=None,
                                                         q_ow_fix=cooler_limit[2])

                            if x_cooling_2[7] < cooler_limit[1]:
                                x_maxcool_2 = _calc_temperatue(A, rhs, q_air_fix=0,
                                                               q_iw_fix=
                                                               cooler_limit[1],
                                                               q_ow_fix=
                                                               cooler_limit[2])

                                if x_maxcool_2[4] > t_set_cooling and cooler_limit[
                                    0] < 0:
                                    x_cooling_3 = _calc_heatflow(A, rhs,
                                                                 t_air_set=t_set_cooling,
                                                                 q_air_fix=None,
                                                                 q_iw_fix=
                                                                 cooler_limit[1],
                                                                 q_ow_fix=
                                                                 cooler_limit[2])

                                    if x_cooling_3[6] < cooler_limit[0]:
                                        return _calc_temperatue(A, rhs, q_air_fix=
                                        cooler_limit[0], q_iw_fix=cooler_limit[1],
                                                                q_ow_fix=
                                                                cooler_limit[2])
                                    else:
                                        return x_cooling_3
                                else:
                                    return x_maxcool_2
                            else:
                                return x_cooling_2
                        else:
                            return x_maxcool_1
                else:
                    return x_cooling_1

        else:
            # Indoor air temperature between both set temperature -> no further 
            # action required
            return x_noHeat


