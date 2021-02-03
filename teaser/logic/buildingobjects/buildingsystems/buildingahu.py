# created November 2015
# by TEASER4 Development Team

"""This module includes a class for central AHU
"""
import pandas as pd
from itertools import cycle, islice


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
    temperature_profile : [float]
        timeline of temperatures requirements for AHU simulation
    min_relative_humidity_profile : [float]
        timeline of relative humidity requirements for AHU simulation
    max_relative_humidity_profile : [float]
        timeline of relative humidity requirements for AHU simulation
    v_flow_profile : [int]
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

        self._temperature_profile = 7 * [293.15] + 12 * [295.15] + 6 * [293.15]
        self._min_relative_humidity_profile = 25 * [0.45]
        self._max_relative_humidity_profile = 25 * [0.65]
        self._v_flow_profile = 7 * [0.0] + 12 * [1.0] + 6 * [0.0]

        self.schedules = pd.DataFrame(
            index=pd.date_range("2019-01-01 00:00:00", periods=8760, freq="H")
            .to_series()
            .dt.strftime("%m-%d %H:%M:%S"),
            data={
                "temperature_profile": list(
                    islice(cycle(self.temperature_profile), 8760)
                ),
                "min_relative_humidity_profile": list(
                    islice(cycle(self.min_relative_humidity_profile), 8760)
                ),
                "max_relative_humidity_profile": list(
                    islice(cycle(self.max_relative_humidity_profile), 8760)
                ),
                "v_flow_profile": list(islice(cycle(self.v_flow_profile), 8760)),
            },
        )

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
    def temperature_profile(self):
        return self._temperature_profile

    @temperature_profile.setter
    def temperature_profile(self, value):
        if not isinstance(value, list):
            value = [value]
        self._temperature_profile = value
        self.schedules["temperature_profile"] = list(islice(cycle(value), 8760))

    @property
    def min_relative_humidity_profile(self):
        return self._min_relative_humidity_profile

    @min_relative_humidity_profile.setter
    def min_relative_humidity_profile(self, value):
        if not isinstance(value, list):
            value = [value]
        self._min_relative_humidity_profile = value
        self.schedules["min_relative_humidity_profile"] = list(
            islice(cycle(value), 8760)
        )

    @property
    def max_relative_humidity_profile(self):
        return self._max_relative_humidity_profile

    @max_relative_humidity_profile.setter
    def max_relative_humidity_profile(self, value):
        if not isinstance(value, list):
            value = [value]
        self._max_relative_humidity_profile = value
        self.schedules["max_relative_humidity_profile"] = list(
            islice(cycle(value), 8760)
        )

    @property
    def v_flow_profile(self):
        return self._v_flow_profile

    @v_flow_profile.setter
    def v_flow_profile(self, value):
        if not isinstance(value, list):
            value = [value]
        self._v_flow_profile = value
        self.schedules["v_flow_profile"] = list(islice(cycle(value), 8760))
