# created June 2015
# by TEASER4 Development Team
"""UseConditions18599

This module is a container for UseConditions following 18599 and SIA
"""

from teaser.Logic.BuildingObjects.UseConditions import UseConditions
import teaser.Data.SchemaBindings.UseConditions18599Bind as uc_bind
import teaser.Logic.Utilis as utilis
import warnings


class UseConditions18599(UseConditions):

    '''Use Conditions DIN 18599

    CLass that contains the boundary conditions of use for non-residential
    buildings defined in DIN V 18599-10


    Attributes
    ----------

    Note: the attributes description are the translation from DIN guideline

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

    usage_level_hight: float
        hight of the usage level (m)  - Hoehe der Nutzebene

    red_factor_visual : float
       reduction factor for visual task Sector -  Minderungsfaktor Bereich
       Sehaufgabe

    rel_absence : float
        relative absence - Raumindex

    room_index : float
        room Index - jaehrliche Betriebstage fuer Kuehlung

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
        set back in reduced operation - Temperaturabsenkung reduzierter Betrieb

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
        spec. elektr. Power for lighting - spez. Elektr.
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

        super(UseConditions18599, self).__init__(parent)

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

        self.maintained_illuminace = 500
        self.usage_level_hight = 0.8
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

        self._persons = 0
        self.activity_type_persons = 3  # physical activity
        self.ratio_conv_rad_persons = 0.5
        self._profile_persons = []
        self._machines = 0.0
        self.activity_type_machines = 2
        self.ratio_conv_rad_machines = 0.5
        self._profile_machines = []
        self._lighting_power = 0.0
        self._profile_lighting = None

        self._min_ahu = 0.0
        self._max_ahu = 0.5
        self.with_ahu = False

        self.use_constant_ach_rate = False
        self.base_ach = 0.2
        self.max_user_ach = 1.0
        self.max_overheating_ach = [3.0, 2.0]
        self.max_summer_ach = [1.0, 273.15 + 10, 273.15 + 17]
        self.winter_reduction = [0.2, 273.15, 273.15 + 10]

    def load_use_conditions(self, zone_usage):
        '''load typical use conditions

        loads Use conditions specified in the XML, according to 18599

        Parameters
        ----------
        zone_usage : str
            code list for zone_usage according to 18599
        '''

        ass_error_1 = ("you need to specify parents for "
                       "use cond and thermal zone")

        assert self.parent.parent.parent is not None, ass_error_1

        for usage in \
            self.parent.parent.parent.data.conditions_bind.\
                UseConditions18599:

            if usage.usage == zone_usage:

                self.typical_length = usage.typical_length
                self.typical_width = usage.typical_width

                self.usage = usage.usage
                self.usage_time = usage.UsageOperationTime.usage_time
                self.daily_usage_hours = \
                    usage.UsageOperationTime.daily_usage_hours
                self.yearly_usage_days = \
                    usage.UsageOperationTime.yearly_usage_days
                self.yearly_usage_hours_day = \
                    usage.UsageOperationTime.yearly_usage_hours_day
                self.yearly_usage_hours_night = \
                    usage.UsageOperationTime.yearly_usage_hours_night
                self.daily_operation_ahu_cooling = \
                    usage.UsageOperationTime.daily_operation_ahu_cooling
                self.yearly_heating_days = \
                    usage.UsageOperationTime.yearly_heating_days
                self.yearly_ahu_days = \
                    usage.UsageOperationTime.yearly_ahu_days
                self.yearly_cooling_days = \
                    usage.UsageOperationTime.yearly_cooling_days
                self.daily_operation_heating = \
                    usage.UsageOperationTime.daily_operation_heating

                self.maintained_illuminace = \
                    usage.Lighting.maintained_illuminace
                self.usage_level_hight = usage.Lighting.usage_level_hight
                self.red_factor_visual = usage.Lighting.red_factor_visual
                self.rel_absence = usage.Lighting.rel_absence
                self.room_index = usage.Lighting.room_index
                self.part_load_factor_lighting = \
                    usage.Lighting.part_load_factor_lighting
                self.ratio_conv_rad_lighting = \
                    usage.Lighting.ratio_conv_rad_lighting

                self.set_temp_heat = usage.RoomClimate.set_temp_heat
                self.set_temp_cool = usage.RoomClimate.set_temp_cool
                self.temp_set_back = usage.RoomClimate.temp_set_back
                self.min_temp_heat = usage.RoomClimate.min_temp_heat
                self.max_temp_cool = usage.RoomClimate.max_temp_cool
                self.rel_humidity = usage.RoomClimate.rel_humidity
                self.cooling_time = usage.RoomClimate.cooling_time
                self.heating_time = usage.RoomClimate.heating_time
                self.min_air_exchange = usage.RoomClimate.min_air_exchange
                self.rel_absence_ahu = usage.RoomClimate.rel_absence_ahu
                self.part_load_factor_ahu = \
                    usage.RoomClimate.part_load_factor_ahu

                self.persons = usage.InternalGains.persons
                self.profile_persons = usage.InternalGains.profile_persons
                self.machines = usage.InternalGains.machines
                self.profile_machines = usage.InternalGains.profile_machines
                self.lighting_power = usage.InternalGains.lighting_power
                self.profile_lighting = usage.InternalGains.profile_lighting
                self.min_ahu = usage.AHU.min_ahu
                self.max_ahu = usage.AHU.max_ahu
                self.with_ahu = usage.AHU.with_ahu

    def save_use_conditions(self, path=None, file_name=None):
        '''Use conditions saver.

        Saves use conditions according to their usage type in the the XML file
        for use conditions in InputData. If the Project parent is set, it
        automatically saves it to the file given in Project.data. Alternatively
        you can specify a path to a file of UseConditions. If this
        file does not exist, a new file is created.

        Parameters
        ----------

        path : str
            path where unique file should be stored
        name : str
            name of of unique file
        '''

        if self.parent is not None:
            path = self.parent.parent.parent.data.path_uc
            xml_parse = self.parent.parent.parent.data.conditions_bind
        else:
            path = path + "\\" + file_name + ".xml"
            try:
                xml_file = open(utilis.get_full_path(path))
                xml_parse = uc_bind.CreateFromDocument(xml_file.read())
            except:
                xml_parse = uc_bind.UseConditions()

        add_to_xml = True

        for check in xml_parse.UseConditions18599:
            if check.usage == self.usage:
                warnings.warn("Usage already exist in this XML, consider " +
                              "revising your inputs. The UseConditions is  " +
                              "NOT saved into XML")
                add_to_xml = False
                break

        if add_to_xml is True:

            usage_pyxb = uc_bind.UseConditions18599Type()
            usage_pyxb.UsageOperationTime = uc_bind.UsageOperationTimeType()
            usage_pyxb.Lighting = uc_bind.LightingType()
            usage_pyxb.RoomClimate = uc_bind.RoomClimateType()
            usage_pyxb.InternalGains = uc_bind.InternalGainsType()
            usage_pyxb.AHU = uc_bind.AHUType()

            usage_pyxb.usage = self.usage

            usage_pyxb.UsageOperationTime.usage_time =\
                self.usage_time
            usage_pyxb.UsageOperationTime.daily_usage_hours = \
                self.daily_usage_hours
            usage_pyxb.UsageOperationTime.yearly_usage_days = \
                self.yearly_usage_days
            usage_pyxb.UsageOperationTime.yearly_usage_hours_day = \
                self.yearly_usage_hours_day
            usage_pyxb.UsageOperationTime.yearly_usage_hours_night = \
                self.yearly_usage_hours_night
            usage_pyxb.UsageOperationTime.daily_operation_ahu_cooling = \
                self.daily_operation_ahu_cooling
            usage_pyxb.UsageOperationTime.yearly_heating_days = \
                self.yearly_heating_days
            usage_pyxb.UsageOperationTime.yearly_ahu_days = \
                self.yearly_ahu_days
            usage_pyxb.UsageOperationTime.yearly_cooling_days = \
                self.yearly_cooling_days
            usage_pyxb.UsageOperationTime.daily_operation_heating = \
                self.daily_operation_heating

            usage_pyxb.Lighting.maintained_illuminace = \
                self.maintained_illuminace
            usage_pyxb.Lighting.usage_level_hight = self.usage_level_hight
            usage_pyxb.Lighting.red_factor_visual = self.red_factor_visual
            usage_pyxb.Lighting.rel_absence = self.rel_absence
            usage_pyxb.Lighting.room_index = self.room_index
            usage_pyxb.Lighting.part_load_factor_lighting = \
                self.part_load_factor_lighting
            usage_pyxb.Lighting.ratio_conv_rad_lighting = \
                self.ratio_conv_rad_lighting

            usage_pyxb.RoomClimate.set_temp_heat = self.set_temp_heat
            usage_pyxb.RoomClimate.set_temp_cool = self.set_temp_cool
            usage_pyxb.RoomClimate.temp_set_back = self.temp_set_back
            usage_pyxb.RoomClimate.min_temp_heat = self.min_temp_heat
            usage_pyxb.RoomClimate.max_temp_cool = self.max_temp_cool
            usage_pyxb.RoomClimate.rel_humidity = self.rel_humidity
            usage_pyxb.RoomClimate.cooling_time = self.cooling_time
            usage_pyxb.RoomClimate.heating_time = self.heating_time
            usage_pyxb.RoomClimate.min_air_exchange = self.min_air_exchange
            usage_pyxb.RoomClimate.rel_absence_ahu = self.rel_absence_ahu
            usage_pyxb.RoomClimate.part_load_factor_ahu = \
                self.part_load_factor_ahu

            usage_pyxb.InternalGains.persons = self.persons
            usage_pyxb.InternalGains.profile_persons = self.profile_persons
            usage_pyxb.InternalGains.machines = self.machines
            usage_pyxb.InternalGains.profile_machines = self.profile_machines
            usage_pyxb.InternalGains.lighting_power = self.lighting_power
            usage_pyxb.InternalGains.profile_lighting = self.profile_lighting
            
            usage_pyxb.AHU.min_ahu = self.min_ahu
            usage_pyxb.AHU.max_ahu = self.max_ahu
            usage_pyxb.AHU.with_ahu = self.with_ahu
            usage_pyxb.typical_length = self.typical_length
            usage_pyxb.typical_width = self.typical_width

            xml_parse.append(usage_pyxb)

            out_file = open(utilis.get_full_path(path), 'w')

            out_file.write(xml_parse.toDOM().toprettyxml())

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
            if self.parent is not None:
                self.parent.parent.file_internal_gains = ("\\InternalGains_" +
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
            if self.parent is not None:
                self.parent.parent.file_internal_gains = ("\\InternalGains_" +
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
            if self.parent is not None:
                self.parent.parent.file_internal_gains = ("\\InternalGains_" +
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
                self.parent.parent.file_set_t = ("\\TSet" +
                                               self.parent.parent.name +
                                               ".mat")
                                           
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
                self.parent.parent.file_set_t = ("\\TSet_" +
                                               self.parent.parent.name +
                                               ".mat")
                                           
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
            self._rel_humidity = value
        elif value is None:
            self._rel_humidity = value
        else:
            try:
                value = float(value)
                self._rel_humidity = value
            except:
                raise ValueError("Can't convert humidity to float")
                
    @property
    def min_air_exchange(self):
        return self._min_air_exchange

    @min_air_exchange.setter
    def min_air_exchange(self, value):

        if isinstance(value, float):
            self._min_air_exchange = value
        elif value is None:
            self._min_air_exchange = value
        else:
            try:
                value = float(value)
                self._min_air_exchange = value
            except:
                raise ValueError("Can't convert air exchange to float")
                
    @property
    def min_ahu(self):
        return self._min_ahu

    @min_ahu.setter
    def min_ahu(self, value):

        if isinstance(value, float):
            self._min_ahu = value
        elif value is None:
            self._min_ahu = value
        else:
            try:
                value = float(value)
                self._min_ahu = value
            except:
                raise ValueError("Can't convert AHU airflow to float")
                
    @property
    def max_ahu(self):
        return self._max_ahu

    @max_ahu.setter
    def max_ahu(self, value):

        if isinstance(value, float):
            self._max_ahu = value
        elif value is None:
            self._max_ahu = value
        else:
            try:
                value = float(value)
                self._max_ahu = value
            except:
                raise ValueError("Can't convert AHU airflow to float")
                
    @property
    def persons(self):
        return self._persons

    @persons.setter
    def persons(self, value):

        if isinstance(value, float):
            self._persons = value
        elif value is None:
            self._persons = value
        else:
            try:
                value = float(value)
                self._persons = value
            except:
                raise ValueError("Can't convert persons to float")
                
    @property
    def machines(self):
        return self._machines

    @machines.setter
    def machines(self, value):

        if isinstance(value, float):
            self._machines = value
        elif value is None:
            self._machines = value
        else:
            try:
                value = float(value)
                self._machines = value
            except:
                raise ValueError("Can't convert machines to float")
                
    @property
    def lighting_power(self):
        return self._lighting_power

    @lighting_power.setter
    def lighting_power(self, value):

        if isinstance(value, float):
            self._lighting_power = value
        elif value is None:
            self._lighting_power = value
        else:
            try:
                value = float(value)
                self._lighting_power = value
            except:
                raise ValueError("Can't convert lighting power to float")