"""Module contains class to calculate a thermal zone with VDI core"""


class VDICore(object):
    """Class to handle VDI simulation directly in Python.

    Contains function and classes to simulate according to VDI core directly in
    python.

    Parameters
    ----------
    thermal_zone: instance of ThermalZone
        TEASER instance of ThermalZone
    weather_data:  instance of WeatherData class
        TEASER isntance of WeatherData class containing TRY weather data.
    building: instance of Building
        TEASER instance of Building
    room_air_temperature: np.array or pd.series
        simulation results for room air temperature
    ...
    """

    def __init__(
            self,
            thermal_zone):
        """Constructor of DataClass
        """
        self.thermal_zone = thermal_zone
        self.weather_data = self.thermal_zone.parent.parent.weather_data
        self.building = self.thermal_zone.parent
        self.room_air_temperature = None

    def simulate(self):
        """Simulates the given thermal_zone

        corresponds to function: calc_reduced_order_model from
        simulation_vdi_6007 """

    def _eq_air_temp(self):
        """Calculates equal air temperature

        corresponds to function eqAirTemp from eqAirTemp"""

    def _solar_radiation(self):
        """Calculates solar radiation on tilted surface

        corresponds to function calc_sun_rad from weather"""
