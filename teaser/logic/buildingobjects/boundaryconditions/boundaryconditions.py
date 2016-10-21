# created June 2015
# by TEASER4 Development Team
"""UseConditions18599

This module is a container for UseConditions following 18599 and SIA
"""

from teaser.logic.buildingobjects.useconditions import UseConditions
import teaser.data.output.boundcond_output as boundcond_output
import teaser.data.input.boundcond_input as boundcond_input



class BoundaryConditions(UseConditions):

    '''Use Conditions DIN 18599

    Class that contains the boundary conditions of use for non-residential
    buildings defined in DIN V 18599-10


    Attributes
    ----------

    Note: the attributes description are translations from DIN V 18599-10
            standard

    USAGE AND OPERATION TIMES

    usage: str
        usage type - Nutzungsart

    typical_length:
        typical length of a usage zone - typische Zonenlaenge

    typical width:
        typical width of a usage zone - typische Zonenbreite

    usage_time : [int]
        usage time [begin, end] (h) -  Nutzungszeit

    daily_usage_hours : int
        daily usage time (h) - taegliche Nutzungsstunden

    yearly_usage_days : int
        operating days per year (d) - jaehrliche Nutzungstage

    yearly_usage_hours_day : int
        operating hours per year during daytime (h) -
        jaehrliche Nutzungsstunden zur Tagzeit

    yearly_usage_hours_night : int
        operating hours per year during nighttime (h) - jaehrliche
        Nutzungsstunden zur Nachtzeit

    daily_operation_ahu_cooling: int
        operating hours of AHU and cooling  - taegliche Betriebsstunden RLT und
        Kuehlung

    yearly_ahu_days : int
       operating days AHU per year (d) -  jaehrliche Betriebstage fuer RLT

    yearly_heating_days : int
        operating days heating per year - jaehrliche Betriebstage fuer Heizung

    yearly_cooling_days : int
        operating days Cooling per year (h) - jaehrliche Betriebstage
        fuer Kuehlung

    daily_operation_heating : int
        operating hours of heating (h) - taegliche Betriebsstunden Heizung

    LIGHTING

    maintained_illuminace : int
        maintained illuminance value (lx) - Wartungswert der
        Beleuchtungsstaerke

    usage_level_height: float
        height of the usage level (m)  - Hoehe der Nutzebene

    red_factor_visual : float
       reduction factor for visual task sector -  Minderungsfaktor Bereich
       Sehaufgabe

    rel_absence : float
        relative absence - Raumindex

    room_index : float
        room index - jaehrliche Betriebstage fuer Kuehlung

    part_load_factor_lighting : float
        part load factor of building usage time for lighting -
        Teilbetriebsfaktor der Gebaeudebetriebszeit fuer Beleuchtung

    ratio_conv_rad_lighting : float
        describes the ratio between convective and radiative heat transfer
        of the lighting

    ROOM CLIMATE

    set_temp_heat: float
        internal set temperature heating - Raum-Solltemperatur Heizung

    set_temp_cool: float
        internal set temperature cooling - Raum-Solltemperatur Kuehlung

    temp_set_back: float
        set back in reduced operation mode - Temperaturabsenkung reduzierter
        Betrieb

    min_temp_heat : float
        design minimal temperature heating -  Minimaltemperatur
        Auslegung Heizung

    max_temp_cool : float
        design maximal temperature cooling - Maximaltemperatur
        Auslegung Kuehlung

    rel_humidity : float
        relative humidity - Feuchteanforderung d

    min_air_exchange : float
        required minimal air exchange, due to usage -
        Mindestaussenluftvolumenstrom

    rel_absence_ahu : float
        relative absence for AHU - Relative Abwesenheit RLT

    part_load_factor_ahu: float
        part load factor of building usage time for AHU  - Teilbetriebsfaktor
        der Gebaeudebetriebszeit RLT

    cooling_time : [int]
      cooling time [begin, end] -  Beginn/Ende Betriebszeit RLT und Kuehlung

    heating_time : [int]
        heating time [begin, end] - Beginn/End Betriebszeit Heizung

    INTERNAL GAINS

    persons : int
        number of persons - Personen

    activity_type_persons : int
        persons activity

    ratio_conv_rad_persons : float
        describes the ratio between convective and radiative heat transfer
        of the persons

    profile_persons : [float]
        timeline of internal gains (persons) from 0 - 100 - Nutzungsprofil
        Personen

    machines: float
        number of Machines  - Arbeitshilfen

    activity_type_machines : int
        machines activity

    ratio_conv_rad_machines : float
        describes the ratio between convective and radiative heat transfer
        of the lighting

    profile_machines : [float]
      timeline of internal gains (machines) from 0 - 100  -  Nutzungsprofil
      Geraete

    lighting_power : float
        spec. electr. Power for lighting - spez. Elektr.
        Leistung-Raumbeleuchtung

    profile_lighting : [float]
      timeline of internal gains (lighting) from 0 - 100  -  Nutzungsprofil
      Licht

    MISC/AHU

    min_ahu: float
        min ahu  - minAHU

    max_ahu : float
      max ahu - maxAHU

    with_ahu : boolean
        with ahu - withAHU

    use_constant_ach_rate : boolean
        choose if a constant ACH rate should be used

    base_ach : float
        base value for the infiltration rate

    max_user_ach : float
        additional infiltration rate for maximum persons activity

    max_overheating_ach : list
        additional infiltration rate when overheating appears

    max_summer_ach : list
        additional infiltration rate in the summer with
        [infiltration_rate, Tmin, Tmax]

    winter_reduction : list
        reduction factor of userACH for cold weather with
        [infiltration_rate, Tmin, Tmax]
    '''

    def __init__(self, parent=None):
        '''Constructor UseConditions18599
        '''

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
        self.ratio_conv_rad_lighting = 0.5

        self._set_temp_heat = 294.15
        self._set_temp_cool = 297.15
        self._temp_set_back = 4.0
        self._min_temp_heat = 20.0
        self._max_temp_cool = 26.0
        self._rel_humidity = 45
        self._min_air_exchange = 0.5
        self.rel_absence_ahu = 0.3
        self.part_load_factor_ahu = 1.0
        self.cooling_time = [5, 18]
        self.heating_time = [5, 18]

        self._persons = 5.0
        self.activity_type_persons = 3  # physical activity
        self.ratio_conv_rad_persons = 0.5
        self._profile_persons = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.4,
                                 0.6, 0.8, 0.8, 0.4, 0.6, 0.8, 0.8, 0.4, 0.2,
                                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self._machines = 7.0
        self.activity_type_machines = 2
        self.ratio_conv_rad_machines = 0.5
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
        self.base_ach = 0.2
        self.max_user_ach = 1.0
        self.max_overheating_ach = [3.0, 2.0]
        self.max_summer_ach = [1.0, 273.15 + 10, 273.15 + 17]
        self.winter_reduction = [0.2, 273.15, 273.15 + 10]

    def load_use_conditions(self,
                            zone_usage,
                            data_class=None):
        '''load typical use conditions

        loads Use conditions specified in the XML, according to 18599

        Parameters
        ----------
        zone_usage : str
            code list for zone_usage according to 18599

        data_class : DataClass()
            DataClass containing the bindings for Use Conditions (typically
            this is the data class stored in prj.data,
            but the user can individually change that. Default is
            self.parent.parent.parent.data (which is data_class in current
            project)
        '''

        if data_class is None:
            data_class = self.parent.parent.parent.data
        else:
            data_class = data_class

        boundcond_input.load_boundary_conditions(bound_cond=self,
                                                 zone_usage=zone_usage,
                                                 data_class=data_class)

    def save_use_conditions(self, data_class):
        '''Use conditions saver.

        Saves use conditions according to their usage type in the the XML file
        for use conditions in InputData. If the Project parent is set, it
        automatically saves it to the file given in Project.data. Alternatively
        you can specify a path to a file of UseConditions. If this
        file does not exist, a new file is created.

        Parameters
        ----------

        data_class : DataClass()
            DataClass containing the bindings for UseConditions(typically this
            is the data class stored in prj.data,
            but the user can individually change that.Default is
            self.parent.parent.parent.data (which is data_class in current
            project)
        '''

        if data_class is None:
            data_class = self.parent.parent.parent.data
        else:
            data_class = data_class

        boundcond_output.save_bound_conditions(bound_cond=self,
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

        if self._profile_persons is None:
            pass
        else:
            if self.parent.parent.file_internal_gains is None:
                self.parent.parent.file_internal_gains = ("/InternalGains_" +
                                               self.parent.parent.name +
                                               ".mat")
        self._profile_persons = value

    @property
    def profile_machines(self):
        return self._profile_machines

    @profile_machines.setter
    def profile_machines(self, value):

        if self._profile_machines is None:
            pass
        else:
            if self.parent.parent.file_internal_gains is None:
                self.parent.parent.file_internal_gains = ("/InternalGains_" +
                                               self.parent.parent.name +
                                               ".mat")
        self._profile_machines = value

    @property
    def profile_lighting(self):

        return self._profile_lighting

    @profile_lighting.setter
    def profile_lighting(self, value):

        if self._profile_lighting is None:
            pass
        else:
            if self.parent.parent.file_internal_gains is None:
                self.parent.parent.file_internal_gains = ("/InternalGains_" +
                                               self.parent.parent.name +
                                               ".mat")

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

        if self._set_temp_heat is None:
            pass
        else:
            if self.parent is not None:
                if self.parent.parent.file_set_t is None:
                    self.parent.parent.file_set_t = ("/TSet" +
                                                   self.parent.parent.name +
                                                   ".mat")
            else:
                pass

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

        if self._set_temp_cool is None:
            pass
        else:
            if self.parent is not None:
                if self.parent.parent.file_set_t is None:
                    self.parent.parent.file_set_t = ("/TSet_" +
                                                   self.parent.parent.name +
                                                   ".mat")
                else:
                    pass
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

        if self._rel_humidity is None:
            pass
        else:
            if self.parent.parent.file_ahu is None:
                self.parent.parent.file_ahu = ("/AHU_" +
                                               self.parent.parent.name +
                                               ".mat")
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

        if self._min_air_exchange is None:
            pass
        else:
            if self.parent.parent.file_ahu is None:
                self.parent.parent.file_ahu = ("/AHU_" +
                                               self.parent.parent.name +
                                               ".mat")
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

        if self._min_ahu is None:
            pass
        else:
            if self.parent.parent.file_ahu is None:
                self.parent.parent.file_ahu = ("/AHU_" +
                                               self.parent.parent.name +
                                               ".mat")
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

        if self._max_ahu is None:
            pass
        else:
            if self.parent.parent.file_ahu is None:
                self.parent.parent.file_ahu = ("/AHU_" +
                                               self.parent.parent.name +
                                               ".mat")
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

        if self._persons is None:
            pass
        else:
            if self.parent.parent.file_internal_gains is None:
                self.parent.parent.file_internal_gains = ("/InternalGains_" +
                                               self.parent.parent.name +
                                               ".mat")
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

        if self._machines is None:
            pass
        else:
            if self.parent.parent.file_internal_gains is None:
                self.parent.parent.file_internal_gains = ("/InternalGains_" +
                                               self.parent.parent.name +
                                               ".mat")
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

        if self._lighting_power is None:
            pass
        else:
            if self.parent.parent.file_internal_gains is None:
                self.parent.parent.file_internal_gains = ("/InternalGains_" +
                                               self.parent.parent.name +
                                               ".mat")
        self._lighting_power = value
