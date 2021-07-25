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

    Heating and Cooling Systems implemented in this class
    ----------

    radiator_heating(self)
    underfloor_heating(self, specific_power_heat)
    panel_heating_cooling(self, specific_power_heat, specific_power_cool)
    tabs_heating_cooling(self, specific_power_heat, specific_power_cool)
    tabs_plus_air_heating_cooling(self, specific_power_heat, specific_power_cool)
    convective_heating_cooling(self)


    """

    def __init__(self, parent=None):
        """Constructor of HeatingCooling Class
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
        self.shareHeatRad = 0.0
        self.shareHeatConv = 0.0
        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0
        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0
        self.shareCoolRad = 0.0
        self.shareCoolConv = 0.0

        self.weighted_convection_inner_cool_ow = 0.0
        self.weighted_convection_inner_cool_iw = 0.0

    def radiator_heating(self):
        """Set parameter to typical radiator heating system.
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
        self.withTabsRoomTempControl = False

        self.KRHeatPanel = 0.0
        self.TNHeatPanel = 0.0
        self.hHeatPanel = 0.0
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 0.0
        self.TNCoolPanel = 0.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = 0.0

        self.KRHeatRem = 1000.0
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

        self.shareHeatRad = 0.5
        self.shareHeatConv = 0.5

        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0

        self.shareCoolRad = 0.0
        self.shareCoolConv = 0.0

    def underfloor_heating(self, specific_power_heat):
        """Set parameter to typical floor heating system. This system is installed
        close to the surface of the corresponding building part.
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
        self.withTabsRoomTempControl = False

        self.KRHeatPanel = 18.0
        self.TNHeatPanel = 2300.0
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

        self.shareHeatPanelExt = 1/self.parent.parent.number_of_floors
        self.shareHeatPanelInt = 1-(1/self.parent.parent.number_of_floors)

        self.shareHeatRad = 0.0
        self.shareHeatConv = 0.0

        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0

        self.shareCoolRad = 0.0
        self.shareCoolConv = 0.0

    def panel_heating_cooling(self, specific_power_heat, specific_power_cool):
        """Set parameter to typical panel heating and cooling system. This system is installed
        close to the surface of the corresponding building part. It is assumed that this system is
        installed in the ground floor (shareHeatPanelExt) and the other floors of the building (shareHeatPanelInt).
        The heat transfer coefficients of the building part where the system is installed have to be adjusted.
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
        self.withTabsRoomTempControl = False

        # KR = 18 TN = 2300
        d = ((0.8 * self.parent.area) * specific_power_heat)
        e = self.parent.model_attr.heat_load
        f = -((0.8 * self.parent.area) * specific_power_cool)
        g = self.parent.model_attr.cool_load

        self.KRHeatPanel = 1000.0
        self.TNHeatPanel = 1.0
        self.hHeatPanel = e if e < d else d
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 1000.0
        self.TNCoolPanel = 1.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = g if g > f else f

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

        self.shareHeatPanelExt = 1/self.parent.parent.number_of_floors
        self.shareHeatPanelInt = 1-(1/self.parent.parent.number_of_floors)

        self.shareHeatRad = 0.0
        self.shareHeatConv = 0.0

        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0

        self.shareCoolPanelExt = 1/self.parent.parent.number_of_floors
        self.shareCoolPanelInt = 1-(1/self.parent.parent.number_of_floors)

        self.shareCoolRad = 0.0
        self.shareCoolConv = 0.0

        # for panel systems heat transfer coefficients are different for heating and cooling case
        # set heat transfer coefficient for groundfloor (outer wall building part)
        for groundfloor in self.parent.ground_floors:
            groundfloor.inner_convection = 7.0
            groundfloor.inner_convection_cool = 1.0
        # set heat transfer coefficient for floor (inner wall building part)
        for floor in self.parent.floors:
            floor.inner_convection = 7.0
            floor.inner_convection_cool = 1.0

        weighted_sum_outer_wall = 0.0
        weighted_sum_inner_wall = 0.0
        area_sum_ow = 0.0
        area_sum_iw = 0.0

        for wall in (self.parent.outer_walls + self.parent.rooftops + self.parent.ground_floors):
            area_sum_ow += wall.area
            try:
                weighted_sum_outer_wall += (wall.area * wall.inner_convection_cool)
            except:
                weighted_sum_outer_wall += (wall.area * wall.inner_convection)

        self.weighted_convection_inner_cool_ow = weighted_sum_outer_wall / area_sum_ow

        for wall in (self.parent.inner_walls + self.parent.ceilings + self.parent.floors):
            area_sum_iw += wall.area
            try:
                weighted_sum_inner_wall += (wall.area * wall.inner_convection_cool)
            except:
                weighted_sum_inner_wall += (wall.area * wall.inner_convection)

        self.weighted_convection_inner_cool_iw = weighted_sum_inner_wall / area_sum_iw

    def tabs_heating_cooling(self, specific_power_heat=30.0, specific_power_cool=30.0, room_temp_control=True):
        """Set parameter to typical tabs heating and cooling system. This system is installed
        at the core of the corresponding building part.
        """
        self.heating = True
        self.cooling = True
        self.tabs = True
        self.floor = False
        self.radiator = False
        self.ventilation = False

        b = ((0.8 * self.parent.area) * specific_power_heat)
        a = self.parent.model_attr.heat_load
        d = -((0.8 * self.parent.area) * specific_power_cool)
        c = self.parent.model_attr.cool_load
        self.powerHeatTabs = a if a < b else b
        self.powerCoolTabs = c if c > d else d
        self.TThresholdHeaterTabs = 273.15 + 14
        self.TThresholdCoolerTabs = 273.15 + 18
        self.withTabsRoomTempControl = room_temp_control

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

        self.shareHeatTabsExt = 1/self.parent.parent.number_of_floors
        self.shareHeatTabsInt = 1-(1/self.parent.parent.number_of_floors)

        self.shareHeatPanelExt = 0.0
        self.shareHeatPanelInt = 0.0

        self.shareHeatRad = 0.0
        self.shareHeatConv = 0.0

        self.shareCoolTabsExt = 1/self.parent.parent.number_of_floors
        self.shareCoolTabsInt = 1-(1/self.parent.parent.number_of_floors)

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0

        self.shareCoolRad = 0.0
        self.shareCoolConv = 0.0

        # for panel systems heat transfer coefficients are different for heating and cooling case
        # set heat transfer coefficient for groundfloor (outer wall building part)
        for groundfloor in self.parent.ground_floors:
            groundfloor.inner_convection = 7.0
            groundfloor.inner_convection_cool = 1.0
        # set heat transfer coefficient for floor (inner wall building part)
        for floor in self.parent.floors:
            floor.inner_convection = 7.0
            floor.inner_convection_cool = 1.0

        weighted_sum_outer_wall = 0.0
        weighted_sum_inner_wall = 0.0
        area_sum_ow = 0.0
        area_sum_iw = 0.0

        for wall in (self.parent.outer_walls + self.parent.rooftops + self.parent.ground_floors):
            area_sum_ow += wall.area
            try:
                weighted_sum_outer_wall += (wall.area * wall.inner_convection_cool)
            except:
                weighted_sum_outer_wall += (wall.area * wall.inner_convection)

        self.weighted_convection_inner_cool_ow = weighted_sum_outer_wall / area_sum_ow

        for wall in (self.parent.inner_walls + self.parent.ceilings + self.parent.floors):
            area_sum_iw += wall.area
            try:
                weighted_sum_inner_wall += (wall.area * wall.inner_convection_cool)
            except:
                weighted_sum_inner_wall += (wall.area * wall.inner_convection)

        self.weighted_convection_inner_cool_iw = weighted_sum_inner_wall / area_sum_iw

    def tabs_plus_air_heating_cooling(self, specific_power_heat=30.0, specific_power_cool=30.0, room_temp_control=True, share_tabs=0.5):
        """Set parameter to typical tabs heating and cooling system.
        """
        self.heating = True
        self.cooling = True
        self.tabs = True
        self.floor = False
        self.radiator = True
        self.ventilation = True

        b = ((0.8 * self.parent.area) * specific_power_heat)
        a = share_tabs * self.parent.model_attr.heat_load
        d = -((0.8 * self.parent.area) * specific_power_cool)
        c = share_tabs * self.parent.model_attr.cool_load
        self.powerHeatTabs = a if a < b else b
        self.powerCoolTabs = c if c > d else d
        self.TThresholdHeaterTabs = 273.15 + 14
        self.TThresholdCoolerTabs = 273.15 + 18
        self.withTabsRoomTempControl = room_temp_control

        self.KRHeatPanel = 0.0
        self.TNHeatPanel = 0.0
        self.hHeatPanel = 0.0
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 0.0
        self.TNCoolPanel = 0.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = 0.0

        self.KRHeatRem = 1000.0
        self.TNHeatRem = 1.0
        self.hHeatRem = (1-share_tabs) * self.parent.model_attr.heat_load
        self.lHeatRem = 0.0
        # (self.parent.model_attr.heat_load - self.powerHeatTabs)

        self.KRCoolRem = 1000.0
        self.TNCoolRem = 1.0
        self.hCoolRem = 0.0
        self.lCoolRem = (1-share_tabs) * self.parent.model_attr.cool_load
        # (self.parent.model_attr.cool_load - self.powerCoolTabs)

        self.shareHeatTabsExt = 1/self.parent.parent.number_of_floors
        self.shareHeatTabsInt = 1-(1/self.parent.parent.number_of_floors)

        self.shareHeatPanelExt = 0.0
        self.shareHeatPanelInt = 0.0

        self.shareHeatRad = 0.0
        self.shareHeatConv = 1.0

        self.shareCoolTabsExt = 1/self.parent.parent.number_of_floors
        self.shareCoolTabsInt = 1-(1/self.parent.parent.number_of_floors)

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0

        self.shareCoolRad = 0.0
        self.shareCoolConv = 1.0

        # for panel systems heat transfer coefficients are different for heating and cooling case
        # set heat transfer coefficient for groundfloor (outer wall building part)
        for groundfloor in self.parent.ground_floors:
            groundfloor.inner_convection = 7.0
            groundfloor.inner_convection_cool = 1.0
        # set heat transfer coefficient for floor (inner wall building part)
        for floor in self.parent.floors:
            floor.inner_convection = 7.0
            floor.inner_convection_cool = 1.0

        weighted_sum_outer_wall = 0.0
        weighted_sum_inner_wall = 0.0
        area_sum_ow = 0.0
        area_sum_iw = 0.0

        for wall in (self.parent.outer_walls + self.parent.rooftops + self.parent.ground_floors):
            area_sum_ow += wall.area
            try:
                weighted_sum_outer_wall += (wall.area * wall.inner_convection_cool)
            except:
                weighted_sum_outer_wall += (wall.area * wall.inner_convection)

        self.weighted_convection_inner_cool_ow = weighted_sum_outer_wall / area_sum_ow

        for wall in (self.parent.inner_walls + self.parent.ceilings + self.parent.floors):
            area_sum_iw += wall.area
            try:
                weighted_sum_inner_wall += (wall.area * wall.inner_convection_cool)
            except:
                weighted_sum_inner_wall += (wall.area * wall.inner_convection)

        self.weighted_convection_inner_cool_iw = weighted_sum_inner_wall / area_sum_iw

    def convective_heating_cooling(self):
        """Set parameter to typical convective heating and cooling system.
        """
        self.heating = True
        self.cooling = True
        self.tabs = False
        self.floor = False
        self.radiator = True
        self.ventilation = True

        self.powerHeatTabs = 0.0
        self.powerCoolTabs = 0.0
        self.TThresholdHeaterTabs = 0.0
        self.TThresholdCoolerTabs = 0.0
        self.withTabsRoomTempControl = False

        self.KRHeatPanel = 0.0
        self.TNHeatPanel = 0.0
        self.hHeatPanel = 0.0
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 0.0
        self.TNCoolPanel = 0.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = 0.0

        self.KRHeatRem = 1000.0
        self.TNHeatRem = 1.0
        self.hHeatRem = self.parent.model_attr.heat_load
        self.lHeatRem = 0.0

        self.KRCoolRem = 1000.0
        self.TNCoolRem = 1.0
        self.hCoolRem = 0.0
        self.lCoolRem = self.parent.model_attr.cool_load

        self.shareHeatTabsExt = 0.0
        self.shareHeatTabsInt = 0.0

        self.shareHeatPanelExt = 0.0
        self.shareHeatPanelInt = 0.0

        self.shareHeatRad = 0.0
        self.shareHeatConv = 1.0

        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0

        self.shareCoolRad = 0.0
        self.shareCoolConv = 1.0

    def test_panel_heating_cooling(self, specific_power_heat, specific_power_cool, KR, TN):
        """Set parameter to typical panel heating and cooling system. This system is installed
        close to the surface of the corresponding building part.
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
        self.withTabsRoomTempControl = False

        d = ((0.8 * self.parent.area) * specific_power_heat)
        e = self.parent.model_attr.heat_load
        f = -((0.8 * self.parent.area) * specific_power_cool)
        g = self.parent.model_attr.cool_load

        self.KRHeatPanel = KR
        self.TNHeatPanel = TN
        self.hHeatPanel = e if e < d else d
        self.lHeatPanel = 0.0

        self.KRCoolPanel = KR
        self.TNCoolPanel = TN
        self.hCoolPanel = 0.0
        self.lCoolPanel = g if g > f else f

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

        self.shareHeatPanelExt = 1/self.parent.parent.number_of_floors
        self.shareHeatPanelInt = 1-(1/self.parent.parent.number_of_floors)

        self.shareHeatRad = 0.0
        self.shareHeatConv = 0.0

        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0

        self.shareCoolPanelExt = 1/self.parent.parent.number_of_floors
        self.shareCoolPanelInt = 1-(1/self.parent.parent.number_of_floors)

        self.shareCoolRad = 0.0
        self.shareCoolConv = 0.0

    def test_radiator_heating(self, KR, TN):
        """Set parameter to typical radiator heating system.
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
        self.withTabsRoomTempControl = False

        self.KRHeatPanel = 0.0
        self.TNHeatPanel = 0.0
        self.hHeatPanel = 0.0
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 0.0
        self.TNCoolPanel = 0.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = 0.0

        self.KRHeatRem = KR
        self.TNHeatRem = TN
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

        self.shareHeatRad = 0.5
        self.shareHeatConv = 0.5

        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0

    def test_convective_heating_cooling(self, KR, TN):
        """Set parameter to typical convective heating and cooling system.
        """
        self.heating = True
        self.cooling = True
        self.tabs = False
        self.floor = False
        self.radiator = True
        self.ventilation = True

        self.powerHeatTabs = 0.0
        self.powerCoolTabs = 0.0
        self.TThresholdHeaterTabs = 0.0
        self.TThresholdCoolerTabs = 0.0
        self.withTabsRoomTempControl = False

        self.KRHeatPanel = 0.0
        self.TNHeatPanel = 0.0
        self.hHeatPanel = 0.0
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 0.0
        self.TNCoolPanel = 0.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = 0.0

        self.KRHeatRem = KR
        self.TNHeatRem = TN
        self.hHeatRem = self.parent.model_attr.heat_load
        self.lHeatRem = 0.0

        self.KRCoolRem = KR
        self.TNCoolRem = TN
        self.hCoolRem = 0.0
        self.lCoolRem = self.parent.model_attr.cool_load

        self.shareHeatTabsExt = 0.0
        self.shareHeatTabsInt = 0.0

        self.shareHeatPanelExt = 0.0
        self.shareHeatPanelInt = 0.0

        self.shareHeatRad = 0.0
        self.shareHeatConv = 1.0

        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0

        self.shareCoolRad = 0.0
        self.shareCoolConv = 1.0

    def no_heating(self):

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
        self.withTabsRoomTempControl = False

        self.KRHeatPanel = 0.0
        self.TNHeatPanel = 0.0
        self.hHeatPanel = 0.0
        self.lHeatPanel = 0.0

        self.KRCoolPanel = 0.0
        self.TNCoolPanel = 0.0
        self.hCoolPanel = 0.0
        self.lCoolPanel = 0.0

        self.KRHeatRem = 1000.0
        self.TNHeatRem = 1.0
        self.hHeatRem = 1.0
        self.lHeatRem = 0.0

        self.KRCoolRem = 0.0
        self.TNCoolRem = 0.0
        self.hCoolRem = 0.0
        self.lCoolRem = 0.0

        self.shareHeatTabsExt = 0.0
        self.shareHeatTabsInt = 0.0

        self.shareHeatPanelExt = 0.0
        self.shareHeatPanelInt = 0.0

        self.shareHeatRad = 0.5
        self.shareHeatConv = 0.5

        self.shareCoolTabsExt = 0.0
        self.shareCoolTabsInt = 0.0

        self.shareCoolPanelExt = 0.0
        self.shareCoolPanelInt = 0.0

        self.shareCoolRad = 0.0
        self.shareCoolConv = 0.0