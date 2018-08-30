# created June 2015
# by TEASER4 Development Team
"""UseConditions18599

This module is a container for UseConditions following 18599 and SIA2024
"""

from teaser.logic.buildingobjects.useconditions import UseConditions
import teaser.data.output.boundcond_output as boundcond_output
import teaser.data.input.boundcond_input as boundcond_input


class BoundaryConditions(UseConditions):
    """Extended Use Conditions from DIN 18599 and SIA2024

    Class that contains the boundary conditions of use for non-residential
    buildings defined in DIN V 18599-10 (
    :cite:`DeutschesInstitutfurNormung.2016`) and
    VDI 2078 (:cite:`VereinDeutscherIngenieure.2015c`). Profiles for internal
    gains (
    persons, lighting, machines) are taken from SIA2024 (
    :cite:`SwissSocietyofEngineersandArchitects.March2006`). In addition
    some
    TEASER specific use conditions have been attached to this class.

    The docstring also contains how the use conditions is used.

    Note: Most attributes description are translations from DIN V 18599-10
    standard

    Attributes
    ----------

    USAGE AND OPERATION TIMES

    usage: str
        usage type
        AixLib usage: String to distinguish usages of a zone
    typical_length : float [m]
        typical length of a room in a usage zone. This value is taken from
        SIA 2024.
        Archetype usage: division of usage zones in rooms
    typical width : float [m]
        typical width of a usage zone. This value is taken from
        SIA 2024.
        Archetype usage: division of usage zones in rooms
    usage_time : list [h]
        usage time [begin, end]
        Currently not used
    daily_usage_hours : int [h]
        daily usage time
        Currently not used
    yearly_usage_days : int [d]
        operating days per year
        Currently not used
    yearly_usage_hours_day : int [h]
        operating hours per year during daytime
        Currently not used
    yearly_usage_hours_night : int [h]
        operating hours per year during nighttime
        Currently not used
    daily_operation_ahu_cooling: int [h]
        operating hours of AHU and cooling
        Currently not used
    yearly_ahu_days : int [d]
       operating days AHU per year
       Currently not used
    yearly_heating_days : int [d]
        operating days heating per year
        Currently not used
    yearly_cooling_days : int [h]
        operating days Cooling per year
        Currently not used
    daily_operation_heating : int [h]
        operating hours of heating
        Currently not used

    LIGHTING

    maintained_illuminance : int [Lx]
        maintained illuminance value (lx)
        Currently not used
    usage_level_height: float [m]
        height of the usage level (m)
        Currently not used
    red_factor_visual : float
       reduction factor for visual task sector
       Currently not used
    rel_absence : float
        relative absence
        Currently not used
    room_index : float
        room index
        Currently not used
    part_load_factor_lighting : float
        part load factor of building usage time for lighting
        Currently not used
    ratio_conv_rad_lighting : float
        describes the ratio between convective and radiative heat transfer
        of the lighting. Default values are derived from
        :cite:`DiLaura.2011`.
        AixLib: Used in Zone record for internal gains, lighting

    ROOM CLIMATE

    set_temp_heat: float [K]
        internal set temperature heating. This value is taken from DIN 18599-10.
        AixLib: Used in simple Heater for set temperature
    set_temp_cool: float [K}
        internal set temperature cooling
        Currently not used
    temp_set_back: float [K]
        set back in reduced operation mode. This value is taken from
        DIN 18599-10.
        AixLib: Used for night set-back for simple heater.
    min_temp_heat : float [K]
        design minimal temperature heating
        Currently not used
    max_temp_cool : float [K]
        design maximal temperature cooling
        Currently not used
    rel_humidity : float
        relative humidity
        Currently not used
    min_air_exchange : float [m3/h]
        required minimal air exchange, due to usage
        Currently not used
    rel_absence_ahu : float
        relative absence for AHU
        Currently not used
    part_load_factor_ahu: float
        part load factor of building usage time for AHU
        Currently not used
    cooling_time : list [h]
      cooling time [begin, end]
        Currently not used
    heating_time : list [h]
        heating time [begin, end]. This value is taken from DIN 18599-10.
        AixLib: Used for night set-back for simple heater.

    INTERNAL GAINS

    persons : float [W/m2]
        Average sensible heat transmission of people at 24 C with specific
        heat transmission of 70 W/person, taken from SIA 2024.
        AixLib: Used in Zone record for internal gains, NrPeople
        Annex: Used for internal gains
    activity_type_persons : float [W/person]
        persons activity (1: light, 2: moderate, 3: high). This value is
        probably from VDI 2078.
        AixLib: currently not used, it is always set to 100 W/person
        Annex: (1: light, 50W/person, 2: moderate 100W/person,
        3: high 150W/person) For Annex models, the heat produced is not
        dependent on zone temperature
    ratio_conv_rad_persons : float
        describes the ratio between convective and radiative heat transfer
        of the persons. Default values are derived from
        :cite:`VereinDeutscherIngenieure.2015c`.
        AixLib: Used in Zone record for internal gains
        Annex: Used for internal gains
    profile_persons : list
        Relative presence of persons 0-1 (e.g. 0.5 means that 50% of the total
        number of persons are currently in the room). Typically given
        for 24h. This value is taken from SIA 2024.
        AixLib: Used for internal gains profile on top-level
        Annex: Used for internal gains
    machines: float [W/m2]
        Specific eletrical load of machines per m2. This value is taken from
        SIA 2024.
        AixLib: Used in Zone record for internal gains
        Annex: Used for internal gains
    activity_type_machines : float [W/machine]
        machines activity (1: light, 50W/machine, 2: moderate 100W/machine,
        3: high 150W/machine). This value is probably from VDI 2078.
        AixLib: currently not used, it is always set to 100 W/machine
        Annex: Used for internal gains
    ratio_conv_rad_machines : float
        describes the ratio between convective and radiative heat transfer
        of the machines. Default values are derived from
        :cite:`Davies.2004`.
        AixLib: Used in Zone record for internal gains
        Annex: Not used, all machines are convective (see Annex examples)
    profile_machines : list
        Relative presence of machines 0-1 (e.g. 0.5 means that 50% of the total
        number of machines are currently used in the room). Typically given
        for 24h. This value is taken from SIA 2024.
        AixLib: Used for internal gains profile on top-level
        Annex: Used for internal gains
    lighting_power : float [W/m2]
        spec. electr. Power for lighting. This value is taken from SIA 2024.
        AixLib: Used in Zone record for internal gains
        Annex: Not used (see Annex examples)
    profile_lighting : [float]
        Relative presence of lighting 0-1 (e.g. 0.5 means that 50% of the total
        lighting power are currently used). Typically given for 24h. This is
        aligned to the user profile.
        AixLib: Used for internal gains profile on top-level
        Annex: Not used (see Annex examples)

    MISC/AHU

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
    use_constant_ach_rate : boolean
        choose if a constant infiltration rate should be used
        AixLib: Used on Zone level for ventilation.
    base_ach : float [1/h]
        base value for the infiltration rate
        AixLib: Used on Zone level for ventilation.
    max_user_ach : float [1/h]
        Additional infiltration rate for maximum persons activity
        AixLib: Used on Zone level for ventilation.
    max_overheating_ach : list [1/h]
        Additional infiltration rate when overheating appears
        AixLib: Used on Zone level for ventilation.
    max_summer_ach : list
        Additional infiltration rate in the summer with
        [infiltration_rate [1/h], Tmin [K], Tmax [K]]. Default values are
        aligned to :cite:`DINV1859910`.
        AixLib: Used on Zone level for ventilation.
    winter_reduction : list
        Reduction factor of userACH for cold weather with
        [infiltration_rate [1/h], Tmin [K], Tmax [K]]
        AixLib: Used on Zone level for ventilation.
        Default values are
        aligned to :cite:`DINV1859910`.
    """

    def __init__(self, parent=None):
        """Constructor UseConditions18599
        """

        super(BoundaryConditions, self).__init__(parent)

        self.usage = "Single office"

        self._typical_length = 123.0
        self._typical_width = 123.0

        self.usage_time = [7, 18]
        self.daily_usage_hours = 11
        self.yearly_usage_days = 250
        self.yearly_usage_hours_day = 2543
        self.yearly_usage_hours_night = 207
        self.daily_operation_ahu_cooling = 13
        self.yearly_ahu_days = 250
        self.yearly_heating_days = 250
        self.yearly_cooling_days = 250
        self.daily_operation_heating = 13

        self.maintained_illuminance = 500
        self.usage_level_height = 0.8
        self.red_factor_visual = 0.84
        self.rel_absence = 0.3
        self.room_index = 0.9
        self.part_load_factor_lighting = 0.7
        self.ratio_conv_rad_lighting = 0.4

        self._set_temp_heat = 294.15
        self._set_temp_cool = 297.15
        self._temp_set_back = 4.0
        self._min_temp_heat = 20.0
        self._max_temp_cool = 26.0
        self._rel_humidity = 45
        self._min_air_exchange = 0.4
        self.rel_absence_ahu = 0.3
        self.part_load_factor_ahu = 1.0
        self.cooling_time = [5, 18]
        self.heating_time = [5, 18]

        self._persons = 5.0
        self.activity_type_persons = 3
        self.ratio_conv_rad_persons = 0.5
        self._profile_persons = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.4,
                                 0.6, 0.8, 0.8, 0.4, 0.6, 0.8, 0.8, 0.4, 0.2,
                                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self._machines = 7.0
        self.activity_type_machines = 2
        self.ratio_conv_rad_machines = 0.75  # 0.75 according to source
        self._profile_machines = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.4,
                                  0.6, 0.8, 0.8, 0.4, 0.6, 0.8, 0.8, 0.4, 0.2,
                                  0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
        self._lighting_power = 15.9
        self._profile_lighting = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0,
                                  1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self._min_ahu = 0.0
        self._max_ahu = 2.6
        self.with_ahu = False

        self.use_constant_ach_rate = False
        self._base_ach = 0.2
        self.max_user_ach = 1.0
        self.max_overheating_ach = [3.0, 2.0]
        self.max_summer_ach = [1.0, 273.15 + 10, 273.15 + 17]
        self.winter_reduction = [0.5, 273.15, 273.15 + 10]

    def load_use_conditions(self,
                            zone_usage,
                            data_class=None):
        """Load typical use conditions from XML data base

        Loads Use conditions specified in the XML.

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

        boundcond_input.load_boundary_conditions(
            bound_cond=self,
            zone_usage=zone_usage,
            data_class=data_class)

    def save_use_conditions(self, data_class):
        """Use conditions saver.

        Saves use conditions according to their usage type in the the XML file
        for use conditions in InputData. If the Project parent is set, it
        automatically saves it to the file given in Project.data. Alternatively
        you can specify a path to a file of UseConditions. If this
        file does not exist, a new file is created. Use Conditions are not
        overwritten if they already exist in XML!

        Parameters
        ----------

        data_class : DataClass()
            DataClass containing the bindings for UseConditions(typically this
            is the data class stored in prj.data,
            but the user can individually change that.Default is
            self.parent.parent.parent.data (which is data_class in current
            project)
        """

        if data_class is None:
            data_class = self.parent.parent.parent.data
        else:
            data_class = data_class

        boundcond_output.save_bound_conditions(
            bound_cond=self,
            data_class=data_class)

    @property
    def typical_length(self):
        return self._typical_length

    @typical_length.setter
    def typical_length(self, value):

        if self.parent is not None:
            self.parent.typical_length = self._typical_length

        self._typical_length = value

    @property
    def typical_width(self):
        return self._typical_width

    @typical_width.setter
    def typical_width(self, value):

        if self.parent is not None:
            self.parent.typical_width = self._typical_width

        self._typical_width = value

    @property
    def profile_persons(self):
        return self._profile_persons

    @profile_persons.setter
    def profile_persons(self, value):

        self._profile_persons = value

    @property
    def profile_machines(self):
        return self._profile_machines

    @profile_machines.setter
    def profile_machines(self, value):

        self._profile_machines = value

    @property
    def profile_lighting(self):

        return self._profile_lighting

    @profile_lighting.setter
    def profile_lighting(self, value):

        self._profile_lighting = value

    @property
    def set_temp_heat(self):
        return self._set_temp_heat

    @set_temp_heat.setter
    def set_temp_heat(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert temperature to float")

        self._set_temp_heat = value

    @property
    def set_temp_cool(self):
        return self._set_temp_cool

    @set_temp_cool.setter
    def set_temp_cool(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert temperature to float")

        self._set_temp_cool = value

    @property
    def temp_set_back(self):
        return self._temp_set_back

    @temp_set_back.setter
    def temp_set_back(self, value):

        if isinstance(value, float):
            self._temp_set_back = value
        elif value is None:
            self._temp_set_back = value
        else:
            try:
                value = float(value)
                self._temp_set_back = value
            except:
                raise ValueError("Can't convert temperature to float")

    @property
    def min_temp_heat(self):
        return self._min_temp_heat

    @min_temp_heat.setter
    def min_temp_heat(self, value):

        if isinstance(value, float):
            self._min_temp_heat = value
        elif value is None:
            self._min_temp_heat = value
        else:
            try:
                value = float(value)
                self._min_temp_heat = value
            except:
                raise ValueError("Can't convert temperature to float")

    @property
    def max_temp_cool(self):
        return self._max_temp_cool

    @max_temp_cool.setter
    def max_temp_cool(self, value):

        if isinstance(value, float):
            self._max_temp_cool = value
        elif value is None:
            self._max_temp_cool = value
        else:
            try:
                value = float(value)
                self._max_temp_cool = value
            except:
                raise ValueError("Can't convert temperature to float")

    @property
    def rel_humidity(self):
        return self._rel_humidity

    @rel_humidity.setter
    def rel_humidity(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert humidity to float")

        self._rel_humidity = value

    @property
    def min_air_exchange(self):
        return self._min_air_exchange

    @min_air_exchange.setter
    def min_air_exchange(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert min_air_exchange to float")

        self._min_air_exchange = value

    @property
    def min_ahu(self):
        return self._min_ahu

    @min_ahu.setter
    def min_ahu(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert AHU airflow to float")

        self._min_ahu = value

    @property
    def max_ahu(self):
        return self._max_ahu

    @max_ahu.setter
    def max_ahu(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert AHU airflow to float")

        self._max_ahu = value

    @property
    def persons(self):
        return self._persons

    @persons.setter
    def persons(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert persons to float")

        self._persons = value

    @property
    def machines(self):
        return self._machines

    @machines.setter
    def machines(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert machines to float")

        self._machines = value

    @property
    def lighting_power(self):
        return self._lighting_power

    @lighting_power.setter
    def lighting_power(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert lighting_power to float")

        self._lighting_power = value

    @property
    def base_ach(self):
        return self._base_ach

    @base_ach.setter
    def base_ach(self, value):

        self._base_ach = value

        if self.parent is not None:
            self.parent.infiltration_rate = value
