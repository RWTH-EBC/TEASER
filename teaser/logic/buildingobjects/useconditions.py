"""This module contains UseConditions class."""
import random
from builtins import ValueError

import pandas as pd
from itertools import cycle, islice
from collections import OrderedDict

import teaser.data.input.usecond_input as usecond_input
import teaser.data.output.usecond_output as usecond_output
from teaser.logic.utilities import division_from_json
import warnings

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
    use_maintained_illuminance: bool
        decision variable to determine wether lighting_power will be given by
        fixed_lighting_power or by calculation using the variables maintained_illuminance
        and lighting_efficiency_lumen
    lighting_power: float [W/m2]
        spec. electr. Power for lighting
        Determined by use_maintained_illuminance
        Not needed in input json file
        AixLib: Used in Zone record for internal gains
        Annex: Not used (see Annex examples)
    fixed_lighting_power: float [W/m2]
        spec. fixed electrical power for lighting. This value is taken from SIA 2024.
    ratio_conv_rad_lighting : float
        describes the ratio between convective and radiative heat transfer
        of the lighting [convective/radiative]. Default values are derived from
        :cite:`DiLaura.2011`.
        AixLib: Used in Zone record for internal gains, lighting
    maintained_illuminance : float [Lx]
        maintained illuminance value for lighting.
        This value is partially taken from SIA 2024 (2015-10) and partially
        from DIN V EN 18599-10 (2018-09).
    lighting_efficiency_lumen: float [lm/W_el]
        lighting efficiency in lm/W_el, in german: Lichtausbeute
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

        - **Note**: The AixLib parameter "WithProfile" determines whether the
          (v_flow_profile combined with "min_ahu and max_ahu") or the
          (persons_profile combined with "min_ahu and max_ahu")
          is used for the AHU supply flow calculations.
          Per default: (v_flow_profile combined with "min_ahu and max_ahu")

    max_ahu : float [m3/(m2*h)]
        Zone specific maximum specific air flow supplied by the AHU.
        AixLib: Used on Multizone level for central AHU to determine total
        volume flow of each zone.

        - **Note**: The AixLib parameter "WithProfile" determines whether the
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
    normative_infiltration: float [1/h]
        Infiltration rate for static heat load calculation.
        Default is 0.5 based on the DIN EN 12831-1:2017 minimal air exchange rate reference value.
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
        for export (one year in hourly timestamps.) Derived from json.
        Schedules can be adjusted by setting the following parameters:
          - adjusted_opening_times
          - first_saturday_of_year
          - profiles_weekend_factor
          - set_back_times
          - heating_set_back
          - cooling_set_back
        To take adjustments into account you need to call calc_schedules()
        function afterwards.
        Note: python attribute, not customizable by user (derived from Json)
    adjusted_opening_times: list
        Sets the first and last hour of opening. These will cut or extend the
        existing profiles (machines, lights, persons).
        [opening_hour, closing_hour]
    first_saturday_of_year: int
        Weekday number of first saturday of the year [1:monday;7:tuesday].
        Is needed to calc which days of profile should be reduced by
        profiles_weekend_factor.
    profiles_weekend_factor: float
        Factor to scale the existing profiles on weekends. For a reduction use
        values between [0;1]. Increase is also possible.
    set_back_times: list
        Sets the first and last hour outside of which the offset is applied.
         List of two integers [first_hour, last_hour]
    heating_set_back: float [K]
        Set back temperature offset for heating profile. Positive (+) values
         increase the profile, negative (-) decrease.
    cooling_set_back: float [K]
        Set back temperature offset for cooling profile. Positive (+) values
        increase the profile, negative (-) decrease.

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

        self._use_maintained_illuminance = False # Choose wether lighting power will be given by direct input or calculated by maintained illuminance and lighting_efficiency_lumen
        self._lighting_power = 10
        self.fixed_lighting_power = 10
        self.ratio_conv_rad_lighting = 0.4
        self.maintained_illuminance = 500
        self.lighting_efficiency_lumen = 100  # lighting efficiency in lm/W_el

        self.use_constant_infiltration = False
        self.normative_infiltration = 0.5
        self.base_infiltration = 0.2
        self.max_user_infiltration = 1.0
        self.max_overheating_infiltration = [3.0, 2.0]
        self.max_summer_infiltration = [1.0, 273.15 + 10, 273.15 + 17]
        self.winter_reduction_infiltration = [0.5, 273.15, 273.15 + 10]

        self.min_ahu = 0.0
        self.max_ahu = 2.6
        self.with_ahu = False

        self._first_saturday_of_year = 1
        self.profiles_weekend_factor = None

        self._set_back_times = None
        self.heating_set_back = -2
        self.cooling_set_back = 2

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

        self._schedules = None

    def adjust_profile_by_opening(self, profile):
        """Adjusts the given profile by opening times specified for use
        condition with the parameter self.set_back_times.

        Parameters
        ----------
        profile : list
            list with the given profile (lighting, machines, persons)
        """
        new_profile = []
        # split profile into daily profiles
        profile_len = len(profile)
        n_sublists = profile_len // 24
        daily_profiles = (profile[i * 24:(i + 1) * 24] for i in
                          range(n_sublists))
        opening_hour_index = self.adjusted_opening_times[0] - 1
        closing_hour_index = self.adjusted_opening_times[1] - 1

        for profile_day in daily_profiles:
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
                            if (
                                    value2 > baseload and i < (
                                    closing_hour_index - opening_hour_index) / 2
                            ):
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
            return new_profile

    def adjust_profile_by_weekend(self, profile):
        """Scales the given profile on weekends. Factor for scaling is taken
        from self.profiles_weekend_factor.

        Parameters
        ----------
        profile : list
            list with the given profile (lighting, machines, persons)
        """
        new_profile = []
        # check if profile is at least week profile (other cases
        # than 24, 168,8760 are excluded already)
        if len(profile) == 24:
            profile = profile * 7
        n_sublists = len(profile) // 24
        daily_profiles = (profile[i * 24:(i + 1) * 24] for i in
                          range(n_sublists))
        weekend_days = []
        for i in range(self.first_saturday_of_year, 365, 7):
            weekend_days.append(i)
            weekend_days.append(i + 1)
        for day_nr, profile_day in enumerate(daily_profiles, 1):
            if day_nr in weekend_days:
                profile_day = \
                    [round((x * self.profiles_weekend_factor), 3)
                     for x in profile_day]
            new_profile.extend(profile_day)
        return new_profile

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
        if not isinstance(value, list):
            value = [value] * 24
        if self.is_periodic(value):
            self._heating_profile = value
        else:
            raise ValueError(
                f"heating profile should be periodic (24h, 168h pr 8760h), "
                f"but length is {len(value)}"
            )

    @property
    def cooling_profile(self):
        return self._cooling_profile

    @cooling_profile.setter
    def cooling_profile(self, value):
        if not isinstance(value, list):
            value = [value] * 24
        if self.is_periodic(value):
            self._cooling_profile = value
        else:
            raise ValueError(
                f"cooling profile should be periodic (24h, 168h pr 8760h), "
                f"but length is {len(value)}"
            )

    @property
    def persons_profile(self):
        return self._persons_profile

    @persons_profile.setter
    def persons_profile(self, value):
        if not isinstance(value, list):
            value = [value] * 24
        if self.is_periodic(value):
            self._persons_profile = value
        else:
            raise ValueError(
                f"persons profile should be periodic (24h, 168h pr 8760h), "
                f"but length is {len(value)}"
            )

    @property
    def machines_profile(self):
        return self._machines_profile

    @machines_profile.setter
    def machines_profile(self, value):
        if not isinstance(value, list):
            value = [value] * 24
        if self.is_periodic(value):
            self._machines_profile = value
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
        if not isinstance(value, list):
            value = [value] * 24
        if self.is_periodic(value):
            self._lighting_profile = value
        else:
            raise ValueError(
                f"lighting profile should be periodic (24h, 168h pr 8760h), "
                "but length is {len(value)}"
            )

    @property
    def schedules(self):
        self._schedules = pd.DataFrame(
            index=pd.date_range("2019-01-01 00:00:00", periods=8760,
                                freq="h").to_series().dt.strftime(
                "%m-%d %H:%M:%S"),
            data={
                "heating_profile": list(
                    islice(cycle(self._heating_profile), 8760)),
                "cooling_profile": list(
                    islice(cycle(self._cooling_profile), 8760)),
                "persons_profile": list(
                    islice(cycle(self._persons_profile), 8760)),
                "lighting_profile": list(
                    islice(cycle(self._lighting_profile), 8760)),
                "machines_profile": list(
                    islice(cycle(self._machines_profile), 8760)),
            },
        )
        return self._schedules

    @schedules.setter
    def schedules(self, value):
        self._schedules = value

    def calc_adj_schedules(self):
        """calculates adjusted schedules for use conditions. When called the
        profiles get adjusted due to specified conditions. Afterwards the
        existing schedules will be overwritten by the resulting pandas dataframe
        with 8760 h.

        """
        if self.adjusted_opening_times:
            self._machines_profile = self.adjust_profile_by_opening(
                self._machines_profile)
            self._lighting_profile = self.adjust_profile_by_opening(
                self._lighting_profile)
            self._persons_profile = self.adjust_profile_by_opening(
                self._persons_profile)

        if self.profiles_weekend_factor:
            self._machines_profile = self.adjust_profile_by_weekend(
                self._machines_profile)
            self._lighting_profile = self.adjust_profile_by_weekend(
                self._lighting_profile)
            self._persons_profile = self.adjust_profile_by_weekend(
                self._persons_profile)

        if self.set_back_times:
            set_back_index_morning, set_back_index_evening = \
                self.set_back_times[0] - 1, self.set_back_times[1] - 1
            heating_profile, cooling_profile = [], []
            for i, value in enumerate(self._heating_profile):
                if 0 <= i <= set_back_index_morning \
                        or set_back_index_evening <= i <= 24:
                    heating_profile.append(value + self.heating_set_back)
                else:
                    heating_profile.append(value)
            self._heating_profile = heating_profile
            for i, value in enumerate(self._cooling_profile):
                if 0 <= i <= set_back_index_morning \
                        or set_back_index_evening <= i <= 24:
                    cooling_profile.append(value + self.cooling_set_back)
                else:
                    cooling_profile.append(value)
            self._cooling_profile = cooling_profile

    @property
    def adjusted_opening_times(self):
        return self._adjusted_opening_times

    @adjusted_opening_times.setter
    def adjusted_opening_times(self, value):
        if len(value) != 2:
            raise ValueError(f"adjusted_opening_times must be list of length 2,"
                             f" but list of length {len(value)} was provided")
        elif value[0] < 0 or value[0] > 24 or value[1] < 0 or value[1] > 24:
            raise ValueError(f"elements of adjusted_opening_times must be "
                             f"hours between 0 and 24. But are {value[0]} and"
                             f" {value[1]}")
        else:
            self._adjusted_opening_times = value

    @property
    def set_back_times(self):
        return self._set_back_times

    @set_back_times.setter
    def set_back_times(self, value):
        if len(value) != 2:
            raise ValueError(f"set_back_times must be list of length 2,"
                             f" but list of length {len(value)} was provided")
        elif value[0] < 0 or value[0] > 24 or value[1] < 0 or value[1] > 24:
            raise ValueError(f"elements of set_back_times must be "
                             f"hours between 0 and 24. But are {value[0]} and"
                             f" {value[1]}")
        else:
            self._set_back_times = value

    @property
    def first_saturday_of_year(self):
        return self._first_saturday_of_year

    @first_saturday_of_year.setter
    def first_saturday_of_year(self, value):
        if value < 1 or value > 7:
            raise ValueError(f"first_saturday_of_year must be int between "
                             f"[1, 7] but is {value}")
        elif not isinstance(value, int):
            raise ValueError(f"first_saturday_of_year must be int but is "
                             f"{type(value)}")
        else:
            self._first_saturday_of_year = value

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

    @property
    def use_maintained_illuminance(self):
        return self._use_maintained_illuminance

    @use_maintained_illuminance.setter
    def use_maintained_illuminance(self, value):
        if value:
            self._lighting_power = self.maintained_illuminance / self.lighting_efficiency_lumen
        else:
            self._lighting_power = self.fixed_lighting_power
        self._use_maintained_illuminance = value


    @property
    def lighting_power(self):
        return self._lighting_power

    @lighting_power.setter
    def lighting_power(self, value):
        if self.use_maintained_illuminance:
            warnings.warn(
                "Parameter 'use_maintained_illuminance' is 'True'!\n"
                "Parameter 'lighting_power' will be overwritten and 'use_maintained_illuminance' will be set to 'False'.",
            )
        self._use_maintained_illuminance = False
        self._lighting_power = value

    @property
    def infiltration_rate(self):
        warnings.warn(
            "'infiltration_rate' is deprecated and will be removed in a future release. "
            "Use 'base_infiltration' instead.",
            DeprecationWarning,
            stacklevel=2)
        return self.base_infiltration

    @infiltration_rate.setter
    def infiltration_rate(self, value):
        self.base_infiltration = value
        warnings.warn(
            "'infiltration_rate' is deprecated and will be removed in a future release. "
            "Use 'base_infiltration' instead.",
            DeprecationWarning,
            stacklevel=2)

