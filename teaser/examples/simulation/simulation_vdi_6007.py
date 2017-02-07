# -*- coding: utf-8 -*-


class SimulationVDI6007(object):
    """Simulation Class for TEASER VDI 6007 Based Simulations

    This Simulation class provides the handling of the simulation logic used
    in the VDI 6007.

    Parameters
    ----------

    thermal_zone : instance of ThermalZone()
        This parameter contains the ThermalZone object related to the
        simulation

    Attributes
    ----------

    weather : object
        Weather class containing weather informations and VDI required weather
        calculations like equal air temperatures

    indoor_air_temperature = array [K]
        This array contains the indoor_air_temperature values after the
        simulation

    q_flow_heater_cooler = array
        This array contains the heat load of after the simulation with
        positive (Heating) and negative (Cooling) values

    heater_limit : list
        The heater limit list sets the maximum heat flow value for the heater
        ToDo: we should think of standard values calculated by the normative
        heat load

    cooler_limit : list
        The cooler limit list sets the maximum heat flow value for the cooler


        """
    def __init__(self, thermal_zone):

        self.thermal_zone = thermal_zone

        self.weather = None
        self.indoor_air_temperature = None
        self.q_flow_heater_cooler = None

        self.heater_limit = [1e10, 1e10, 1e10]
        self.cooler_limit = [-1e10, -1e10, -1e10]

        self.initial_air_temp
        self.initial_inner_wall_temp
        self.initial_outer_wall_temp

    def calc_reduced_order_model(
            weather_temperature,
            solar_rad_in,
            equal_air_temp,
            alpha_rad,
            q_internal_gains_conv,
            q_internal_gains_rad,
            convective_radiative_split_factor,
            t_set_heating,
            t_set_cooling,
            heater_order,
            cooler_order):

        pass
