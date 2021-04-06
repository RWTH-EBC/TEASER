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

        self.KRHeatTABS = 0.0
        self.TNHeatTABS = 0.0
        self.powerHeatTABS = 0.0
        self.KRCoolTABS = 0.0
        self.TNCoolTABS = 0.0
        self.powerCoolTABS = 0.0

        self.KRHeatPanel = 0.0
        self.TNHeatPanel = 0.0
        self.powerHeatPanel = 0.0

        self.KRCoolPanel = 0.0
        self.TNCoolPanel = 0.0
        self.powerCoolPanel = 0.0

        self.KRHeatRem = 0.0
        self.TNHeatRem = 0.0
        self.powerHeatRem = 0.0

        self.KRHeatVent = 0.0
        self.TNHeatVent = 0.0
        self.powerHeatVent = 0.0

        self.KRCoolVent = 0.0
        self.TNCoolVent = 0.0
        self.powerCoolVent = 0.0

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
