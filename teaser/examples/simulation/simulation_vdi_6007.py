# -*- coding: utf-8 -*-


class SimulationVDI6007(object):
    """Simulation Class for TEASER VDI 6007 Based Simulations

    This Simulation class provides the handling of the simulation logic used
    in the VDI 6007.

    Parameters
    ----------


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



        """
    def __init__(self, arg):

        self.weather = None
        self.indoor_air_temperature = None
        self.q_flow_heater_cooler = None