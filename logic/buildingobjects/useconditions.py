"""This module contains UseConditions class."""
import random
import teaser.data.input.usecond_input as usecond_input
import teaser.data.output.usecond_output as usecond_output
import pandas as pd
from itertools import cycle, islice
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
        Sets if the zone is cooloed by ideal cooler or not.
    with_ideal_thresholds: boolean
        Sets if the threshold temperatures for ideal heater and cooler should
        be used to prevent simultaneous heating from AHU and cooling from
        ideal heater and vice versa. This should only be turned on if an AHU
        exists.
    T_threshold_heating: float [K]
       Threshold temperature below ideal heater is used. Default is 15 °C
       which corresponds to the value for all buildings that are not built
       according to EnEV standard according to DIN EN 18599-5.
    T_threshold_cooling: float [K]
        Threshold temperature above ideal cooler is used. Default is 22 °C ,
        since there are no european standards for cooling degree days this value
        is taken from the following paper: "Heating Degree Days, Cooling
        Degree Days and Precipitation in Europe—analysis for the
        CELECT-project" by Benestad, 2008.
    heating_profile : list [K]
        Heating setpoint for a day or similar. You can set a list of any
        length, TEASER will multiplicate this list for one whole year.
    cooling_profile : list [K]
        Cooling setpoint for a day or similar. You can set a list of any
        length, TEASER will multiplicate this list for one whole year.
    with_cooling: boolean
        Sets if the zone is cooloed or not.
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
        or heat flow rate and moisture gains (internal_gains_mode=3). Both
        are temperature and activity degree depending, calculation based
        on SIA2024.
        Annex: not used, heat flow rate is constant value
        fixed_heat_flow_rate_persons
    ratio_conv_rad_persons: float
        describes the ratio between convective and radiative heat transfer
        of the persons. Default values are derived from
        :cite:`VereinDeutscherIngenieure.2015c`.
        AixLib: Used in Zone record for internal gains
        Annex: Used for internal gains
    persons_profile : list
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
        of the machines. Default values are derived from
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
        of the lighting. Default values are derived from
        :cite:`DiLaura.2011`.
        AixLib: Used in Zone record for internal gains, lighting
    lighting_profil : [float]
        Relative presence of lighting 0-1 (e.g. 0.5 means that 50% of the total
        lighting power are currently used). Typically given for 24h. This is
        aligned to the user profile.
        AixLib: Used for internal gains profile on top-level
        Annex: Not used (see Annex examples)
    min_ahu: float [m3/(m2*h)]
        Zone specific minimum specific air flow supplied by the AHU
        AixLib: Used on Multizone level for central AHU to determine total
        volume flow of all zones.
    max_ahu : float [m3/(m2*h)]
        Zone specific maximum specific air flow supplied by the AHU
        AixLib: Used on Multizone level for central AHU to determine total
        volume flow of all zones.
    with_ahu : boolean
        Zone is connected to central air handling unit or not
        AixLib: Used on Multizone level for central AHU.
    use_constant_infiltration : boolean
        choose if a constant infiltration rate should be used
        AixLib: Used on Zone level for ventilation.
    base_infiltration : float [1/h]
        base value for the infiltration rate
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

        self.schedules = pd.DataFrame(
            index=pd.date_range("2019-01-01 00:00:00", periods=8760, freq="H")
            .to_series()
            .dt.strftime("%m-%d %H:%M:%S"),
            data={
                "heating_profile": list(islice(cycle(self._heating_profile), 8760)),
                "cooling_profile": list(islice(cycle(self._cooling_profile), 8760)),
                "persons_profile": list(islice(cycle(self._persons_profile), 8760)),
                "lighting_profile": list(islice(cycle(self._lighting_profile), 8760)),
                "machines_profile": list(islice(cycle(self._machines_profile), 8760)),
            },
        )

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
            value = [value]
        self._heating_profile = value
        self.schedules["heating_profile"] = list(islice(cycle(value), 8760))

    @property
    def cooling_profile(self):
        return self._cooling_profile

    @cooling_profile.setter
    def cooling_profile(self, value):
        if not isinstance(value, list):
            value = [value]
        self._cooling_profile = value
        self.schedules["cooling_profile"] = list(islice(cycle(value), 8760))

    @property
    def persons_profile(self):
        return self._persons_profile

    @persons_profile.setter
    def persons_profile(self, value):
        if not isinstance(value, list):
            value = [value]
        self._persons_profile = value
        self.schedules["persons_profile"] = list(islice(cycle(value), 8760))

    @property
    def machines_profile(self):
        return self._machines_profile

    @machines_profile.setter
    def machines_profile(self, value):
        if not isinstance(value, list):
            value = [value]
        self._machines_profile = value
        self.schedules["machines_profile"] = list(islice(cycle(value), 8760))

    @property
    def lighting_profile(self):
        return self._lighting_profile

    @lighting_profile.setter
    def lighting_profile(self, value):
        if not isinstance(value, list):
            value = [value]
        self._lighting_profile = value
        self.schedules["lighting_profile"] = list(islice(cycle(value), 8760))

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
