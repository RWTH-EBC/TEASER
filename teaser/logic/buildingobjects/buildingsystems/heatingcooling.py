"""This module includes a class for heating and cooling systems."""


class HeatingCooling(object):
    """Heating and Cooling Systems.

    This class holds information for a heating and cooling system. It includes
    parameters on the type of system and adds special parameters depending on that type.
    It is attached to each thermal zone.

    Parameters
    ----------

    parent: ThermalZone
        The parent class of this object, the ThermalZone the system belongs to.
        Allows for better control of hierarchical structures.
        (default: None)

    Attributes
    ----------

    heating : boolean
        Heating Function of system (default = True)
    cooling : boolean
        Cooling Function of system (default = False)
    tabs : boolean
        Thermal activated building physics (default = False)
    floor : boolean
        Underfloor, ceiling or wall heating (default = False)
    radiator : boolean
        Radiator system (only heating) (default = True)
    ventilation : boolean
        Pure convective system (default = False)


    """

    def __init__(self, parent=None):
        """Constructor of BuildingAHU Class
        """
        self.parent = parent

        self.heating = True
        self.cooling = False
        self.tabs = False
        self.floor = False
        self.radiator = True
        self.ventilation = False

        self.powerHeatTabs = 0.0
        self.powerCoolTabs = 0.0
        self.TThresholdHeaterTabs = 0.0
        self.TThresholdCoolerTabs = 0.0

        self.KRHeatPanel = 0.0
        self.TNHeatPanel = 0.0
        self.hHeatPanel = 0.0
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 0.0
        self.TNCoolPanel = 0.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = 0.0

        self.KRHeatRem = 0.0
        self.TNHeatRem = 0.0
        self.hHeatRem = 0.0
        self.lHeatRem = 0.0

        self.KRCoolRem = 0.0
        self.TNCoolRem = 0.0
        self.hCoolRem = 0.0
        self.lCoolRem = 0.0

        self.shareHeatTabsExt = 0.0
        self.shareHeatTabsInt = 0.0
        self.shareHeatPanelExt = 0.0
        self.shareHeatPanelInt = 0.0
        self.shareHeatRadExt = 0.0
        self.shareHeatRadInt = 0.0
        self.shareHeatConv = 0.0
        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0
        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0
        self.shareCoolRadExt = 0.0
        self.shareCoolRadInt = 0.0
        self.shareCoolConv = 0.0

    def radiator_heating(self):
        """Set parameter to typical radiator heating system.

        !!!These values are dummy values and need to be set correctly!!!
        """
        self.heating = True
        self.cooling = False
        self.tabs = False
        self.floor = False
        self.radiator = True
        self.ventilation = False

        self.powerHeatTabs = 0.0
        self.powerCoolTabs = 0.0
        self.TThresholdHeaterTabs = 0.0
        self.TThresholdCoolerTabs = 0.0

        self.KRHeatPanel = 0.0
        self.TNHeatPanel = 0.0
        self.hHeatPanel = 0.0
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 0.0
        self.TNCoolPanel = 0.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = 0.0

        self.KRHeatRem = 10000.0
        self.TNHeatRem = 1.0
        self.hHeatRem = self.parent.model_attr.heat_load
        self.lHeatRem = 0.0

        self.KRCoolRem = 0.0
        self.TNCoolRem = 0.0
        self.hCoolRem = 0.0
        self.lCoolRem = 0.0

        self.shareHeatTabsExt = 0.0
        self.shareHeatTabsInt = 0.0

        self.shareHeatPanelExt = 0.0
        self.shareHeatPanelInt = 0.0

        self.shareHeatRadExt = 0.35
        self.shareHeatRadInt = 0.35

        self.shareHeatConv = 0.3

        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0

        self.shareCoolRadExt = 0.0
        self.shareCoolRadInt = 0.0

        self.shareCoolConv = 0.0

    def underfloor_heating(self, specific_power_heat):
        """Set parameter to typical underfloor heating system.

        !!!These values are dummy values and need to be set correctly!!!
        """
        self.heating = True
        self.cooling = False
        self.tabs = False
        self.floor = True
        self.radiator = False
        self.ventilation = False

        self.powerHeatTabs = 0.0
        self.powerCoolTabs = 0.0
        self.TThresholdHeaterTabs = 0.0
        self.TThresholdCoolerTabs = 0.0

        self.KRHeatPanel = 1000.0
        self.TNHeatPanel = 7200.0
        self.hHeatPanel = self.parent.area * specific_power_heat
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 0.0
        self.TNCoolPanel = 0.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = 0.0

        self.KRHeatRem = 0.0
        self.TNHeatRem = 0.0
        self.hHeatRem = 0.0
        self.lHeatRem = 0.0

        self.KRCoolRem = 0.0
        self.TNCoolRem = 0.0
        self.hCoolRem = 0.0
        self.lCoolRem = 0.0

        self.shareHeatTabsExt = 0.0
        self.shareHeatTabsInt = 0.0

        self.shareHeatPanelExt = 0.0
        self.shareHeatPanelInt = 1.0

        self.shareHeatRadExt = 0.0
        self.shareHeatRadInt = 0.0

        self.shareHeatConv = 0.0

        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0

        self.shareCoolRadExt = 0.0
        self.shareCoolRadInt = 0.0

        self.shareCoolConv = 0.0

    def underfloor_heating_cooling(self, specific_power_heat, specific_power_cool):
        """Set parameter to typical underfloor heating and cooling system.

        !!!These values are dummy values and need to be set correctly!!!
        """
        self.heating = True
        self.cooling = True
        self.tabs = False
        self.floor = True
        self.radiator = False
        self.ventilation = False

        self.powerHeatTabs = 0.0
        self.powerCoolTabs = 0.0
        self.TThresholdHeaterTabs = 0.0
        self.TThresholdCoolerTabs = 0.0

        self.KRHeatPanel = 1000.0
        self.TNHeatPanel = 7200.0
        self.hHeatPanel = self.parent.area * specific_power_heat
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 1000.0
        self.TNCoolPanel = 7200.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = -self.parent.area * specific_power_cool

        self.KRHeatRem = 0.0
        self.TNHeatRem = 0.0
        self.hHeatRem = 0.0
        self.lHeatRem = 0.0

        self.KRCoolRem = 0.0
        self.TNCoolRem = 0.0
        self.hCoolRem = 0.0
        self.lCoolRem = 0.0

        self.shareHeatTabsExt = 0.0
        self.shareHeatTabsInt = 0.0

        self.shareHeatPanelExt = 0.0
        self.shareHeatPanelInt = 1.0

        self.shareHeatRadExt = 0.0
        self.shareHeatRadInt = 0.0

        self.shareHeatConv = 0.0

        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 1.0

        self.shareCoolRadExt = 0.0
        self.shareCoolRadInt = 0.0

        self.shareCoolConv = 0.0

    def tabs_heating_cooling(self, specific_power_heat, specific_power_cool):
        """Set parameter to typical tabs heating and cooling system.

        !!!These values are dummy values and need to be set correctly!!!
        """
        self.heating = True
        self.cooling = True
        self.tabs = True
        self.floor = False
        self.radiator = False
        self.ventilation = False

        self.powerHeatTabs = self.parent.area * specific_power_heat
        self.powerCoolTabs = -self.parent.area * specific_power_cool
        self.TThresholdHeaterTabs = 273.15 + 14
        self.TThresholdCoolerTabs = 273.15 + 16

        self.KRHeatPanel = 1000.0
        self.TNHeatPanel = 7200.0
        self.hHeatPanel = 0.0
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 1000.0
        self.TNCoolPanel = 7200.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = 0.0

        self.KRHeatRem = 0.0
        self.TNHeatRem = 0.0
        self.hHeatRem = 0.0
        self.lHeatRem = 0.0

        self.KRCoolRem = 0.0
        self.TNCoolRem = 0.0
        self.hCoolRem = 0.0
        self.lCoolRem = 0.0

        self.shareHeatTabsExt = 0.5
        self.shareHeatTabsInt = 0.5

        self.shareHeatPanelExt = 0.0
        self.shareHeatPanelInt = 0.0

        self.shareHeatRadExt = 0.0
        self.shareHeatRadInt = 0.0

        self.shareHeatConv = 0.0

        self.shareCoolTabsExt = 0.5
        self.shareCoolTabsInt = 0.5

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0

        self.shareCoolRadExt = 0.0
        self.shareCoolRadInt = 0.0

        self.shareCoolConv = 0.0

    def tabs_plus_air_heating_cooling(self, specific_power_heat, specific_power_cool):
        """Set parameter to typical tabs heating and cooling system.

        !!!These values are dummy values and need to be set correctly!!!
        """
        self.heating = True
        self.cooling = True
        self.tabs = True
        self.floor = False
        self.radiator = False
        self.ventilation = True

        self.powerHeatTabs = self.parent.area * specific_power_heat
        self.powerCoolTabs = -self.parent.area * specific_power_cool
        self.TThresholdHeaterTabs = 273.15 + 14
        self.TThresholdCoolerTabs = 273.15 + 16

        self.KRHeatPanel = 1000.0
        self.TNHeatPanel = 7200.0
        self.hHeatPanel = 0.0
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 1000.0
        self.TNCoolPanel = 7200.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = 0.0

        self.KRHeatRem = 1000.0
        self.TNHeatRem = 1.0
        self.hHeatRem = self.parent.model_attr.heat_load - self.powerHeatTabs
        "gesamte von TEASER berechnete Heizlast - self.powerHeatTabs"
        self.lHeatRem = 0.0

        self.KRCoolRem = 0.0
        self.TNCoolRem = 0.0
        self.hCoolRem = 0.0
        self.lCoolRem = 0.0

        self.shareHeatTabsExt = 0.5
        self.shareHeatTabsInt = 0.5

        self.shareHeatPanelExt = 0.0
        self.shareHeatPanelInt = 0.0

        self.shareHeatRadExt = 0.0
        self.shareHeatRadInt = 0.0

        self.shareHeatConv = 1.0

        self.shareCoolTabsExt = 0.5
        self.shareCoolTabsInt = 0.5

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0

        self.shareCoolRadExt = 0.0
        self.shareCoolRadInt = 0.0

        self.shareCoolConv = 0.0
