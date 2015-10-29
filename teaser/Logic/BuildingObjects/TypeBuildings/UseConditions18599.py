# created June 2015
# by TEASER4 Development Team


from teaser.Logic.BuildingObjects.UseConditions import UseConditions
import teaser.Data.SchemaBindings.UseConditions18599Bind as uc_bind
import teaser.Logic.Utilis as utilis


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
        describes the ratio between convective and radiative heat transer 
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

    profile_persons : [float]
        timeline of internal gains from 0 - 100 - Nutzungsprofil Personen

    machines: float
        number of Machines  - Arbeitshilfen

    profile_machines : [float]
      timeline of internal gains from 0 - 100  -  Nutzungsprofil Geraete

    lighting_power : float
        spec. elektr. Power for lighting - spez. Elektr.
        Leistung-Raumbeleuchtung

    MISC

    min_ahu: float
        min ahu  - minAHU

    max_ahu : float
      max ahu - maxAHU

    with_ahu : boolean
        with ahu - withAHU
    '''

    def __init__(self, parent=None):
        '''Constructor UseConditions18599
        '''

        super(UseConditions18599, self).__init__(parent)

        self.usage = "single office"

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
        
        self.set_temp_heat = 21.0
        self.set_temp_cool = 24.0
        self.temp_set_back = 4.0
        self.min_temp_heat = 20.0
        self.max_temp_cool = 26.0
        self.rel_humidity = 45
        self.min_air_exchange = 0.5
        self.rel_absence_ahu = 0.3
        self.part_load_factor_ahu = 1.0
        self.cooling_time = [5, 18]
        self.heating_time = [5, 18]

        self.persons = 0
        self.profile_persons = []
        self.machines = 0.0
        self.profile_machines = []
        self.lighting_power = 0.0

        self.min_ahu = 0.0
        self.max_ahu = 0.5
        self.with_ahu = False

    def load_use_conditions(self, zone_usage):
        '''load typical use conditions

        loads Use conditions specified in the XML, according to 18599

        Parameters
        ----------
        zone_usage : str
            code list for zone_usage according to 18599
        '''

        ass_error_1 = "you need to specify parents for "
        "use cond and thermal zone"

        assert self.parent.parent.parent is not None, ass_error_1

        for usage in \
            self.parent.parent.parent.data.conditions_bind.\
                UseConditions18599:

            if usage.usage == zone_usage:

                self.typical_length = usage.typical_length
                self.typical_width = usage.typical_width

                self.usage = usage.usage
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
                self.min_ahu = usage.AHU.min_ahu
                self.max_ahu = usage.AHU.max_ahu
                self.with_ahu = usage.AHU.with_ahu

    def save_use_conditions(self):
        '''Saves typical use conditions

        Saves use conditions specified in the XML, according to 18599

        '''

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

        usage_pyxb.Lighting.maintained_illuminace = self.maintained_illuminace
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
        usage_pyxb.RoomClimate.part_load_factor_ahu = self.part_load_factor_ahu

        usage_pyxb.InternalGains.persons = self.persons
        usage_pyxb.InternalGains.profile_persons = self.profile_persons
        usage_pyxb.InternalGains.machines = self.machines
        usage_pyxb.InternalGains.profile_machines = self.profile_machines
        usage_pyxb.InternalGains.lighting_power = self.lighting_power

        usage_pyxb.AHU.min_ahu = self.min_ahu
        usage_pyxb.AHU.max_ahu = self.max_ahu
        usage_pyxb.AHU.with_ahu = self.with_ahu
        usage_pyxb.typical_length = self.typical_length
        usage_pyxb.typical_width = self.typical_width

        path = utilis.get_full_path("InputData/UseConditions.xml")
        xml_file = open(path, 'r')

        xml_parse = uc_bind.CreateFromDocument(xml_file.read())
        xml_parse.append(usage_pyxb)

        out_file = open(path, 'w')

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
