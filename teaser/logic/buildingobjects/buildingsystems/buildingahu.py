# created November 2015
# by TEASER4 Development Team

"""This module includes a class for central AHU
"""


class BuildingAHU(object):
    """BuildingAHU Class

    This class holds information for a central Air Handling Unit (AHU). This
    class is very AixLib specific and holds some parameters that are only
    applicable to AixLib Central AHU model. If you are using other models
    these values might have no effect.

    Parameters
    ----------

    parent: Building()
        The parent class of this object, the Building the AHU belongs to.
        Allows for better control of hierarchical structures.
        (default: None)

    Attributes
    ----------
    heating : boolean
        Heating Function of AHU (default = True)
    cooling : boolean
        Cooling Function of AHU (default = True)
    dehumidification : boolean
        Dehumidification Function of AHU (Cooling and Heating must be enabled)
        (default = True)
    humidification : boolean
        Humidification Function of AHU (Cooling and Heating must be enabled)
        (default = True)
    heat_recovery : boolean
        Is a HeatRecoverySystem physically integrated in the AHU
        AixLib: 'HRS'
        (default = True)
    by_pass_dehumidification : float
         By-pass factor of cooling coil during dehumidification. Necessary to
         calculate the real outgoing enthalpy flow of heat exchanger in
         dehumidification mode taking the surface enthalpy of the cooling
         coil into account. In AixLib called "BPF_DeHu" (default = 0.2,
         according to :cite:`Lindeburg.2013`)
    efficiency_recovery : float
        efficiency of HRS in the AHU modes if HRS is enabled.
        AixLib: "efficiencyHRS_enabled" (default = 0.65, according to
        :cite:`.20012001`)
    efficiency_recovery_false : float
        taking a little heat transfer into account although HRS is disabled
        (in case that a HRS is physically installed in the AHU) in AixLib:
        "efficiencyHRS_disabled" (default = 0.2, according to
        :cite:`Mehrfeld.2014`)
    sample_rate : int
        sample rate of state machines in AHU model. Default is set to half
        an hour as typical input is hourly (default = 1800)
    efficiency_fan_supply : float
        Efficiency of supply fan (default = 0.7)
    efficiency_fan_return: float
        Efficiency of return fan (default = 0.7)
    pressure_drop_fan_supply: float (default 800)
        Pressure drop assigned to supply fan in Pascal
    pressure_drop_fan_return: float (default 800)
        Pressure drop assigned to return fan in Pascal
    profile_temperature : [float]
        timeline of temperatures requirements for AHU simulation
    profile_min_relative_humidity : [float]
        timeline of relative humidity requirements for AHU simulation
    profile_max_relative_humidity : [float]
        timeline of relative humidity requirements for AHU simulation
    profile_v_flow : [int]
        timeline of desired relative v_flow of the AHU simulation (0..1)

    """

    def __init__(self, parent=None):
        """Constructor of BuildingAHU Class
        """
        self.parent = parent

        self.heating = True
        self.cooling = True
        self.dehumidification = True
        self.humidification = True
        self.heat_recovery = True
        self.by_pass_dehumidification = 0.2
        self.efficiency_recovery = 0.65
        self.efficiency_recovery_false = 0.2
        self.sample_rate = 1800
        self.efficiency_fan_supply = 0.7
        self.efficiency_fan_return = 0.7
        self.pressure_drop_fan_supply = 800
        self.pressure_drop_fan_return = 800

        self._profile_min_relative_humidity = None
        self._profile_max_relative_humidity = None
        self._profile_v_flow = None
        self._profile_temperature = None

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        from teaser.logic.buildingobjects.building import Building
        import inspect
        if inspect.isclass(Building):
            self.__parent = value
            self.__parent.central_ahu = self

    @property
    def profile_min_relative_humidity(self):
        return self._profile_min_relative_humidity

    @profile_min_relative_humidity.setter
    def profile_min_relative_humidity(self, value):

        if self._profile_min_relative_humidity is None:
            pass
        else:
            self.parent.file_ahu = (
                "/AHU_" + self.parent.name + ".mat")

        self._profile_min_relative_humidity = value

    @property
    def profile_max_relative_humidity(self):
        return self._profile_max_relative_humidity

    @profile_max_relative_humidity.setter
    def profile_max_relative_humidity(self, value):

        if self._profile_max_relative_humidity is None:
            pass
        else:
            self.parent.file_ahu = (
                "/AHU_" + self.parent.name + ".mat")
        self._profile_max_relative_humidity = value

    @property
    def profile_v_flow(self):
        return self._profile_v_flow

    @profile_v_flow.setter
    def profile_v_flow(self, value):

        if self._profile_v_flow is None:
            pass
        else:
            self.parent.file_ahu = (
                "/AHU_" + self.parent.name + ".mat")

        self._profile_v_flow = value

    @property
    def profile_temperature(self):
        return self._profile_temperature

    @profile_temperature.setter
    def profile_temperature(self, value):

        if self._profile_temperature is None:
            pass
        else:
            self.parent.file_ahu = (
                "/AHU_" + self.parent.name + ".mat")
        self._profile_temperature = value
