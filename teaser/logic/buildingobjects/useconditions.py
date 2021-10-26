"""This module contains UseConditions class."""
import random
from builtins import ValueError

import teaser.data.input.usecond_input as usecond_input
import teaser.data.output.usecond_output as usecond_output
import pandas as pd
from itertools import cycle, islice, chain
from collections import OrderedDict
from teaser.logic.utilities import division_from_json


class UseConditions(object):
    """UseConditions class contains all zone specific boundary conditions.

    Class that contains the boundary conditions of use for buildings defined in
    DIN V 18599-10 ( :cite:`DeutschesInstitutfurNormung.2016`) and VDI 2078
    (:cite:`VereinDeutscherIngenieure.2015c`). Profiles for internal gains (
    persons, lighting, machines) are taken from SIA2024 (
    :cite:`SwissSocietyofEngineersandArchitects.March2006`). In addition some
    TEASER specific use conditions have been attached to this class. The
    docstring also contains how the use conditions is used.

    Note: Most attributes description are translations from DIN V 18599-10
    standard
    Attributes
    ----------
    usage: str
        usage type
        AixLib usage: String to distinguish usages of a zone
    typical_length: float [m]
        typical length of a room in a usage zone. This value is taken from
        SIA 2024. Archetype usage: division of usage zones in rooms
    typical width: float [m]
        typical width of a usage zone. This value is taken from
        SIA 2024. Archetype usage: division of usage zones in rooms
    with_heating: boolean
        Sets if the zone is heated by ideal heater or not.
    with_cooling: boolean
        Sets if the zone is cooled by ideal cooler or not.
    with_ideal_thresholds: boolean
        Sets if the threshold temperatures for ideal heater and cooler are
        used.
        True = T_threshold_heating and T_threshold_cooling are used.
        This can, in most cases, prevent simultaneous heating from AHU and
        cooling from ideal heater and vice versa. This should only be turned
        on if an AHU exists.
    T_threshold_heating: float [K]
       Threshold for the outside temperature above which the ideal heater is
       permanently shut down regardless the inside temperature.
       Default is 15 °C which corresponds to the value for all buildings
       that are not built
       according to EnEV standard according to DIN EN 18599-5.
    T_threshold_cooling: float [K]
        Threshold for the outside temperature below which the ideal cooler is
        permanently shut down regardless the inside temperature.
        Default is 22 °C, since there are no european standards
        for cooling degree days this value is taken from the following paper:
        "Heating Degree Days, Cooling Degree Days and Precipitation in Europe
        —analysis for the CELECT-project" by Benestad, 2008.
    heating_profile : list [K]
        Heating setpoint, regarding the zone temperature, of ideal static
        heating for a day or similar. You can set a list of any
        length, TEASER will multiplicate this list for one whole year.
    cooling_profile : list [K]
        Cooling setpoint, regarding the zone temperature, of ideal static
        cooling for a day or similar. You can set a list of any
        length, TEASER will multiplicate this list for one whole year.
    fixed_heat_flow_rate_persons: float [W/person]
        fixed heat flow rate for one person in case of temperature
        independent calculation. Default value is 70
        W/person and describes
        the maximum heat flow rate depending on the schedule.
    persons : float [Persons/m2]
        Specific number of persons per square area.
        Annex: Used for internal gains
    internal_gains_moisture_no_people : float [g/(h m²)]
        internal moisture production of plants, etc. except from people.
    activity_degree_persons : float [met]
        default value is 1.2 met
        AixLib: used for heat flow rate calculation (internal_gains_mode=1)
        or heat flow rate, moisture and co2 gains (internal_gains_mode=3). Both
        are temperature and activity degree depending, calculation based
        on SIA2024 (2015) and Engineering ToolBox (2004).
        Annex: not used, heat flow rate is constant value
        fixed_heat_flow_rate_persons
    ratio_conv_rad_persons: float
        describes the ratio between convective and radiative heat transfer
        of the persons [convective/radiative]. Default values are derived from
        :cite:`VereinDeutscherIngenieure.2015c`.
        AixLib: Used in Zone record for internal gains
        Annex: Used for internal gains
    persons_profile: list
        Relative presence of persons 0-1 (e.g. 0.5 means that 50% of the total
        number of persons are currently in the room). Given
        for 24h. This value is taken from SIA 2024. You can set a list of any
        length, TEASER will multiplicate this list for one whole year.
        AixLib: Used for internal gains profile on top-level
        Annex: Used for internal gains
    adjusted_opening_times: list
        Opening hour to which the opening times should be shifted.
        ... # todo
        the regular profile starting time. E.g. for -2 the first profile value
        which is not equal to the first value (non first value) will be copied
        for the two hours before first non first value.
    machines: float [W/m2]
        area specific eletrical load of machines per m2. This value is taken
        from SIA 2024 and DIN V 18599-10 for medium occupancy.
        AixLib: Used in Zone record for internal gains,
        internalGainsMachinesSpecific
        Annex: Used for internal gains
    ratio_conv_rad_machines: float
        describes the ratio between convective and radiative heat transfer
        of the machines [convective/radiative]. Default values are derived from
        :cite:`Davies.2004`.
        AixLib: Used in Zone record for internal gains
        Annex: Not used, all machines are convective (see Annex examples)
    machines_profile: list
        Relative presence of machines 0-1 (e.g. 0.5 means that 50% of the total
        number of machines are currently used in the room). Given
        for 24h. This value is taken from SIA 2024. You can set a list of any
        length, TEASER will multiplicate this list for one whole year.
        AixLib: Used for internal gains profile on top-level
        Annex: Used for internal gains
    lighting_power: float [W/m2]
        spec. electr. Power for lighting. This value is taken from SIA 2024.
        AixLib: Used in Zone record for internal gains
        Annex: Not used (see Annex examples)
    ratio_conv_rad_lighting : float
        describes the ratio between convective and radiative heat transfer
        of the lighting [convective/radiative]. Default values are derived from
        :cite:`DiLaura.2011`.
        AixLib: Used in Zone record for internal gains, lighting
    lighting_profil : [float]
        Relative presence of lighting 0-1 (e.g. 0.5 means that 50% of the total
        lighting power are currently used). Typically given for 24h. This is
        aligned to the user profile.
        AixLib: Used for internal gains profile on top-level
        Annex: Not used (see Annex examples)
    min_ahu: float [m3/(m2*h)]
        Zone specific minimum specific air flow supplied by the AHU.
        AixLib: Used on Multizone level for central AHU to determine total
        volume flow of each zone.
            Note: The AixLib parameter "WithProfile" determines whether the
            (v_flow_profile combined with "min_ahu and max_ahu") or the
            (persons_profile combined with "min_ahu and max_ahu")
            is used for the AHU supply flow calculations.
            Per default: (v_flow_profile combined with "min_ahu and max_ahu")
    max_ahu : float [m3/(m2*h)]
        Zone specific maximum specific air flow supplied by the AHU.
        AixLib: Used on Multizone level for central AHU to determine total
        volume flow of each zone.
            Note: The AixLib parameter "WithProfile" determines whether the
            (v_flow_profile combined with "min_ahu and max_ahu") or the
            (persons_profile combined with "min_ahu and max_ahu")
            is used for the AHU supply flow calculations.
            Per default: (v_flow_profile combined with "min_ahu and max_ahu")
    with_ahu : boolean
        Zone is connected to central air handling unit or not
        AixLib: Used on Multizone level for central AHU.
    use_constant_infiltration : boolean
        choose whether window opening should be regarded.
        true = natural infiltration + ventilation due to a AHU
        false = natural infiltration + ventilation due to a AHU
            + window infiltration calculated by window opening model
        AixLib: Used on Zone level for ventilation.
    base_infiltration : float [1/h]
        base value for the natural infiltration without window openings
        AixLib: Used on Zone level for ventilation.
    max_user_infiltration : float [1/h]
        Additional infiltration rate for maximum persons activity
        AixLib: Used on Zone level for ventilation.
    max_overheating_infiltration : list [1/h]
        Additional infiltration rate when overheating appears
        AixLib: Used on Zone level for ventilation.
    max_summer_infiltration : list
        Additional infiltration rate in the summer with
        [infiltration_rate [1/h], Tmin [K], Tmax [K]]. Default values are
        aligned to :cite:`DINV1859910`.
        AixLib: Used on Zone level for ventilation.
    winter_reduction_infiltration : list
        Reduction factor of userACH for cold weather with
        [infiltration_rate [1/h], Tmin [K], Tmax [K]]
        AixLib: Used on Zone level for ventilation.
        Default values are
        aligned to :cite:`DINV1859910`.
    schedules: pandas.DataFrame
        All time dependent boundary attributes in one pandas DataFrame, used
        for export (one year in hourly timestep.)
        Note: python attribute, not customizable by user (derived from Json)


    """

    def __init__(self, parent=None):
        """Construct UseConditions."""
        self.internal_id = random.random()

        self.parent = parent
        self.usage = "Single office"

        self.typical_length = 6.0
        self.typical_width = 6.0

        self.with_heating = True
        self.with_cooling = False
        self.T_threshold_heating = 288.15
        self.T_threshold_cooling = 295.15

        self.fixed_heat_flow_rate_persons = 70
        self.activity_degree_persons = 1.2
        self._persons = 1 / 14
        self.internal_gains_moisture_no_people = 0.5
        self.ratio_conv_rad_persons = 0.5

        self.machines = 7.0
        self.ratio_conv_rad_machines = 0.75

        self.lighting_power = 15.9
        self.ratio_conv_rad_lighting = 0.4

        self.use_constant_infiltration = False
        self.infiltration_rate = 0.2
        self.max_user_infiltration = 1.0
        self.max_overheating_infiltration = [3.0, 2.0]
        self.max_summer_infiltration = [1.0, 273.15 + 10, 273.15 + 17]
        self.winter_reduction_infiltration = [0.5, 273.15, 273.15 + 10]

        self.min_ahu = 0.0
        self.max_ahu = 2.6
        self.with_ahu = False

        self.first_saturday_of_year = 1
        self.profiles_weekend_factor = None

        self.heating_set_back = None
        self.cooling_set_back = None

        self._adjusted_opening_times = None

        self._with_ideal_thresholds = False

        self._heating_profile = [
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
        ]
        self._cooling_profile = [
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
            294.15,
        ]
        self._persons_profile = [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.2,
            0.4,
            0.6,
            0.8,
            0.8,
            0.4,
            0.6,
            0.8,
            0.8,
            0.4,
            0.2,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]
        self._machines_profile = [
            0.1,
            0.1,
            0.1,
            0.1,
            0.1,
            0.1,
            0.1,
            0.2,
            0.4,
            0.6,
            0.8,
            0.8,
            0.4,
            0.6,
            0.8,
            0.8,
            0.4,
            0.2,
            0.1,
            0.1,
            0.1,
            0.1,
            0.1,
            0.1,
        ]
        self._lighting_profile = [
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            1.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
        ]

        # todo
        self._schedules = None

    def adjust_gains_profile_by_opening_hour(
            self, profile_name, weekend_days, weekend_profile, delta_open, delta_close,
            specific_profile=None):

        """
        Changes the profiles (lighting, machines, persons) by taking the
        opening hours into account.

        profile_name: profile
            profile that should be adjusted.
            Valid inputs are: heating_profile, machines_profile, persons_profile
        delta_open: int
            offset for opening hours during week (negative means earlier start,
            positive later start)
        delta_close: int
            offset for closing hours during week(negative means earlier closing,
            positive later closing)
        weekend_days: list of str
            list of days where weekend profile should be applied.
            Valid inputs are [mon, tue, wed, thu, fri, sat, sun]
            e.g. [san, sat]
        weekend_profile: list of float
            24 h profile for weekend to apply. Must hold values [0;1]

        """



    def _adjust_profile_by_opening_hour(self, profile_day_asset, opening_hours):
        """
        Change the given profile by taking the opening hours into account.

        profile_day_asset: profile for one day for one of the three assets (
        lighting, persons, machines)
        delta_open: int
            Hours to start before(-) or after(+) the regular opening
            time
        delta_close: int
            Hours to end before(-) or after(+) the regular closing time
        """

        # todo: solve -1 hour problem, doku
        Weekdays = OrderedDict(
            [
                ("monday", [0, 24]),
                ("tuesday", [24, 48]),
                ("wednesday", [48, 72]),
                ("thursday", [72, 96]),
                ("friday", [96, 120]),
                ("saturday", [120, 144]),
                ("sunday", [144, 168]),
            ]
        )
        # get first value which is used as baseload/threshold value
        profile_week = []
        for weekday, indexofweek in Weekdays.items():
            # for weekly profiles split profile into single days
            if len(profile_day_asset) == 168:
                profile_day = profile_day_asset[indexofweek[0]: indexofweek[1]]
            else:
                profile_day = profile_day_asset
            baseload = profile_day[0]
            opening_hour = int(
                getattr(opening_hours, weekday + "_open").split(":")[0])
            closing_hour = int(
                getattr(opening_hours, weekday + "_close").split(":")[0])

            for i, value in enumerate(profile_day):
                # check if runtime variable(time) is inside opening times
                #  +/- delta times
                if opening_hour <= i <= closing_hour:
                    if value == baseload:
                        # start new iteration of profile_day from beginning
                        for j, value2 in enumerate(profile_day):
                            # search first value which is > baseload
                            # if
                            if value2 > baseload and i < (
                                    closing_hour - opening_hour) / 2:
                                profile_day[i] = profile_day[j]
                                break
                            elif (
                                    value2 > baseload and i >= (
                                    closing_hour - opening_hour) / 2
                            ):
                                # value is overwritten every time,
                                # so that last value that is > baseload
                                # is used
                                profile_day[i] = value2
                            else:
                                pass
                    else:
                        pass
                elif not (
                        opening_hour <= i <= closing_hour) and value != baseload:
                    # if time is not inside opening times, set value to
                    # baseload
                    profile_day[i] = baseload
            profile_week += profile_day
        return profile_week

    def load_use_conditions(self, zone_usage, data_class=None):
        """Load typical use conditions from JSON data base.

        Loads Use conditions specified in the JSON.

        Parameters
        ----------
        zone_usage : str
            code list for zone_usage according to 18599 or self defined

        data_class : DataClass()
            DataClass containing the bindings for Use Conditions (typically
            this is the data class stored in prj.data,
            but the user can individually change that. Default is None which
            leads to an automatic setter to self.parent.parent.parent.data (
            which is DataClass in current project)

        """
        if data_class is None:
            data_class = self.parent.parent.parent.data
        else:
            data_class = data_class

        usecond_input.load_use_conditions(
            use_cond=self, zone_usage=zone_usage, data_class=data_class
        )

    def save_use_conditions(self, data_class=None):
        """Documentation is missing."""
        if data_class is None:
            data_class = self.parent.parent.parent.data
        else:
            data_class = data_class

        usecond_output.save_use_conditions(use_cond=self, data_class=data_class)

    @staticmethod
    def is_periodic(profile_list):
        """Checks if the given profile list is periodic.
         Allowed periods are: 24h, 168h (7 days), 8760h (1year).

        Parameters
        ----------
        profile_list: list
            given profile as list of hourly values.
        """
        if not isinstance(profile_list, list):
            profile_list = list(profile_list)
        profile_len = len(profile_list)
        if profile_len in [24, 168, 8760]:
            return True
        else:
            return False

    @property
    def persons(self):
        return self._persons

    @persons.setter
    def persons(self, value):
        if isinstance(value, OrderedDict):
            self._persons = division_from_json(value)
        else:
            self._persons = value

    @property
    def with_ideal_thresholds(self):
        return self._with_ideal_thresholds

    @with_ideal_thresholds.setter
    def with_ideal_thresholds(self, value):
        if self.with_ahu is False and value is True:
            raise ValueError(
                "Threshold for ideal heaters should only be used"
                " when AHU is used in this zone"
            )
        else:
            self._with_ideal_thresholds = value

    @property
    def heating_profile(self):
        return self._heating_profile

    @heating_profile.setter
    def heating_profile(self, value):
        if self.is_periodic(value):
            if not isinstance(value, list):
                value = [value]
            self._heating_profile = value
            # self.schedules["heating_profile"] = list(
            #     islice(cycle(value), 8760))
        else:
            raise ValueError(
                f"heating profile should be periodic (24h, 168h pr 8760h), "
                "but length is {len(value)}"
            )
    @property
    def cooling_profile(self):
        return self._cooling_profile

    @cooling_profile.setter
    def cooling_profile(self, value):
        if self.is_periodic(value):
            if not isinstance(value, list):
                value = [value]
            self._cooling_profile = value
            # self.schedules["cooling_profile"] = list(
            #     islice(cycle(value), 8760))
        else:
            raise ValueError(
                f"cooling profile should be periodic (24h, 168h pr 8760h), "
                "but length is {len(value)}"
            )
    @property
    def persons_profile(self):
        return self._persons_profile

    @persons_profile.setter
    def persons_profile(self, value):
        if self.is_periodic(value):
            if not isinstance(value, list):
                value = [value]
            self._persons_profile = value
            # self.schedules["persons_profile"] = list(
            #     islice(cycle(value), 8760))
        else:
            raise ValueError(
               f"persons profile should be periodic (24h, 168h pr 8760h), "
                "but length is {len(value)}"
            )

    @property
    def machines_profile(self):
        return self._machines_profile

    @machines_profile.setter
    def machines_profile(self, value):
        if self.is_periodic(value):
            if not isinstance(value, list):
                value = [value]
            self._machines_profile = value
            # self.schedules["machines_profile"] = list(
            #     islice(cycle(value), 8760))
        else:
            raise ValueError(
                f"machines profile should be periodic (24h, 168h pr 8760h), "
                "but length is {len(value)}"
            )

    @property
    def lighting_profile(self):
        return self._lighting_profile

    @lighting_profile.setter
    def lighting_profile(self, value):
        if self.is_periodic(value):
            if not isinstance(value, list):
                value = [value]
            self._lighting_profile = value
            # self.schedules["lighting_profile"] = list(
            #     islice(cycle(value), 8760))
        else:
            raise ValueError(
                f"lighting profile should be periodic (24h, 168h pr 8760h), "
                "but length is {len(value)}"
            )




    @property
    def schedules(self):
        profile = self.persons_profile
        profile_len = len(profile)
        n_sublists = profile_len // 24
        new_profile = []
        if self.adjusted_opening_times:
            # split profile into daily profiles
            daily_profiles = (profile[i * 24:(i + 1) * 24] for i in
                              range(n_sublists))
            opening_hour_index = self.adjusted_opening_times[0] - 1
            closing_hour_index = self.adjusted_opening_times[1] - 1

            for profile_day in daily_profiles:
                test = profile_day.copy()
                baseload = profile_day[0]
                for i, value in enumerate(profile_day):
                    # check if runtime variable(time) is inside opening times
                    #  +/- delta times
                    if opening_hour_index <= i <= closing_hour_index:
                        if value == baseload:
                            # start new iteration of profile_day from beginning
                            for j, value2 in enumerate(profile_day):
                                # search first value which is > baseload
                                # if
                                if value2 > baseload and i < (
                                        closing_hour_index - opening_hour_index) / 2:
                                    profile_day[i] = profile_day[j]
                                    break
                                elif (
                                        value2 > baseload and i >= (
                                        closing_hour_index - opening_hour_index) / 2
                                ):
                                    # value is overwritten every time,
                                    # so that last value that is > baseload
                                    # is used
                                    profile_day[i] = value2
                                else:
                                    pass
                        else:
                            pass
                    elif not (
                            opening_hour_index <= i <= closing_hour_index) and \
                            value != baseload:
                        # if time is not inside opening times, set value to
                        # baseload
                        profile_day[i] = baseload
                new_profile.extend(profile_day)
        if not new_profile:
            new_profile = profile
        final_profil = []
        if self.profiles_weekend_factor:
            # check if minimum week profile (other cases
            # than 24, 168,8760 are excluded already)
            if profile_len == 24:
                new_profile = new_profile * 7
            profile_len = len(new_profile)
            # devide against in daily
            n_sublists = profile_len // 24
            daily_profiles = (new_profile[i * 24:(i + 1) * 24] for i in
                              range(n_sublists))
            weekend_days = []
            for i in range(self.first_saturday_of_year, 365, 7):
                weekend_days.append(i)
                weekend_days.append(i + 1)
            for day_nr, profile_day in enumerate(daily_profiles, 1):
                if day_nr in weekend_days:
                    profile_day = \
                        [round(x * self.profiles_weekend_factor, 2)
                         for x in profile_day]
                final_profil.extend(profile_day)
        print('test')









            # for day_profile in daily_profiles:
            #     daily_profile_new = []
            #     first_daily_val = profile[0]
            #     last_daily_val = profile[-1]
            #     for i, val in enumerate(day_profile):
            #         if val != first_daily_val:
            #             start_index = i
            #             cor_start_index = int(i + self.profiles_delta_start)
            #             first_daily_changed_val = val
            #             break
            #     for i, val in enumerate(reversed(day_profile)):
            #         if val != last_daily_val:
            #             end_index = int( 23 - i)
            #             cor_end_index = int(23 - i + self.profiles_delta_stop)
            #             last_daily_changed_val = val
            #             break
            #     #todo continue
            #     daily_profile_new[0:cor_start_index] = \
            #         [first_daily_val] * (cor_start_index +1)
            #     if cor_start_index < start_index:
            #         daily_profile_new[cor_start_index+1:start_index] =\
            #             [first_daily_changed_val] * \
            #             (start_index-cor_start_index + 1)
            #     start_index = max(cor_start_index, start_index)
            #     # else:
            #         # daily_profile_new[cor_start_index+1:cor_end_index] = \
            #         #     day_profile[cor_start_index+1:cor_end_index]
            #     if cor_end_index > end_index:
            #         daily_profile_new[start_index + 1:end_index] = \
            #             day_profile[start_index + 1:end_index]
            #         daily_profile_new[end_index + 1:cor_end_index] = \
            #             [last_daily_changed_val] * \
            #             (cor_end_index + 1 - end_index)
            #     else:
            #         daily_profile_new[start_index + 1:cor_end_index] = \
            #             day_profile[start_index + 1:cor_end_index]
            #     daily_profile_new[cor_end_index + 1:23] = \
            #         [last_daily_val] * (23 - cor_end_index)
            #     new_profile.append(daily_profile_new)


        #
        #
        #     print('test')
        # pd.DataFrame(
        #     index=pd.date_range("2019-01-01 00:00:00", periods=8760, freq="H")
        #         .to_series()
        #         .dt.strftime("%m-%d %H:%M:%S"),
        #     data={
        #         "heating_profile": list(
        #             islice(cycle(self._heating_profile), 8760)),
        #         "cooling_profile": list(
        #             islice(cycle(self._cooling_profile), 8760)),
        #         "persons_profile": list(
        #             islice(cycle(self._persons_profile), 8760)),
        #         "lighting_profile": list(
        #             islice(cycle(self._lighting_profile), 8760)),
        #         "machines_profile": list(
        #             islice(cycle(self._machines_profile), 8760)),
        #     },
        #         )
        # return self._schedules

    @schedules.setter
    def schedules(self, value):
        self._schedules = value

    # @property
    # def profiles_delta_open(self):
    #     return self._profiles_delta_open
    #
    # @profiles_delta_open.setter
    # def profile_delta_open(self, value):
    #     if 0 <= value <=

    @property
    def adjusted_opening_times(self):
        return self._adjusted_opening_times

    @adjusted_opening_times.setter
    def adjusted_opening_times(self, value):
        if len(value) != 2:
            raise ValueError(f"adjusted_opening_times must be list of length 2,"
                             f" but list of length {len(value)} was provided")
        else:
            self._adjusted_opening_times = value

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):

        if value is not None:

            ass_error_1 = "Parent has to be an instance of ThermalZone()"

            assert type(value).__name__ == "ThermalZone", ass_error_1

            self._parent = value
            self._parent._use_conditions = self

        else:

            self._parent = None


