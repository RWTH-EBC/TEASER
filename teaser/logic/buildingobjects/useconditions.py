"""This module is a container for UseConditions"""
import random
import teaser.data.input.usecond_input as usecond_input
import teaser.data.output.usecond_output as usecond_output
import pandas as pd
from itertools import cycle, islice


class UseConditions(object):
    """UseConditions class contains all zone specific boundary conditions.

    Documentation is missing and needs to be added!
    """

    def __init__(self, parent=None):
        """Constructor for UseConditions
        """
        self.internal_id = random.random()

        self.parent = parent
        self.usage = "Single office"

        self.typical_length = 6.0
        self.typical_width = 6.0

        self.with_heating = True
        self.with_cooling = False

        self.persons = 5.0
        self.ratio_conv_rad_persons = 0.5

        self.machines = 7.0
        self.ratio_conv_rad_machines = 0.75

        self.lighting_power = 15.9
        self.ratio_conv_rad_lighting = 0.4

        self.use_constant_infiltration = False
        self.infiltration_rate = 0.2
        self.max_user_infiltration = 1.0
        self.max_overheating_infiltration = [3.0, 2.0]
        self.max_summer_infiltration = [1.0, 273.15 + 10, 273.15 + 17]
        self.winter_reduction_infiltration = [0.5, 273.15, 273.15 + 10]

        self.min_ahu = 0.0
        self.max_ahu = 2.6
        self.with_ahu = False

        self._heating_profile = [294.15, 294.15, 294.15, 294.15,
                                 294.15, 294.15, 294.15, 294.15,
                                 294.15, 294.15, 294.15, 294.15,
                                 294.15, 294.15, 294.15, 294.15,
                                 294.15, 294.15, 294.15, 294.15,
                                 294.15, 294.15, 294.15, 294.15,
                                 294.15]
        self._cooling_profile = [294.15, 294.15, 294.15, 294.15,
                                 294.15, 294.15, 294.15, 294.15,
                                 294.15, 294.15, 294.15, 294.15,
                                 294.15, 294.15, 294.15, 294.15,
                                 294.15, 294.15, 294.15, 294.15,
                                 294.15, 294.15, 294.15, 294.15,
                                 294.15]
        self._persons_profile = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.4,
                                 0.6, 0.8, 0.8, 0.4, 0.6, 0.8, 0.8, 0.4, 0.2,
                                 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        self._machines_profile = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2, 0.4,
                                  0.6, 0.8, 0.8, 0.4, 0.6, 0.8, 0.8, 0.4, 0.2,
                                  0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
        self._lighting_profile = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0,
                                  1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
                                  0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        self.schedules = pd.DataFrame(
            index=pd.date_range(
                '2019-01-01 00:00:00',
                periods=8760,
                freq='H').to_series().dt.strftime('%m-%d %H:%M:%S'),
            data={
                'heating_profile': list(
                    islice(cycle(self._heating_profile), 8760)),
                'cooling_profile': list(
                    islice(cycle(self._cooling_profile), 8760)),
                'persons_profile': list(
                    islice(cycle(self._persons_profile), 8760)),
                'lighting_profile': list(
                    islice(cycle(self._lighting_profile), 8760)),
                'machines_profile': list(
                    islice(cycle(self._machines_profile), 8760))})

    def load_use_conditions(self,
                            zone_usage,
                            data_class=None):
        """Load typical use conditions from XML data base

        Loads Use conditions specified in the XML.

        Parameters
        ----------
        zone_usage : str
            code list for zone_usage according to 18599 or self defined

        data_class : DataClass()
            DataClass containing the bindings for Use Conditions (typically
            this is the data class stored in prj.data,
            but the user can individually change that. Default is None which
            leads to an automatic setter to self.parent.parent.parent.data (
            which is DataClass in current project)
        """

        if data_class is None:
            data_class = self.parent.parent.parent.data
        else:
            data_class = data_class

        usecond_input.load_use_conditions(
            use_cond=self,
            zone_usage=zone_usage,
            data_class=data_class)

    def save_use_conditions(self,
                            data_class=None):
        """Documentation is missing
        """

        if data_class is None:
            data_class = self.parent.parent.parent.data
        else:
            data_class = data_class

        usecond_output.save_use_conditions(
            use_cond=self,
            data_class=data_class)

    @property
    def heating_profile(self):
        return self._heating_profile

    @heating_profile.setter
    def heating_profile(self, value):
        self._heating_profile = value
        self.schedules["heating_profile"] = list(
            islice(cycle(value), 8760))

    @property
    def cooling_profile(self):
        return self._cooling_profile

    @cooling_profile.setter
    def cooling_profile(self, value):
        self._cooling_profile = value
        self.schedules["cooling_profile"] = list(
            islice(cycle(value), 8760))

    @property
    def persons_profile(self):
        return self._persons_profile

    @persons_profile.setter
    def persons_profile(self, value):
        self._persons_profile = value
        self.schedules["persons_profile"] = list(
            islice(cycle(value), 8760))

    @property
    def machines_profile(self):
        return self._machines_profile

    @machines_profile.setter
    def machines_profile(self, value):
        self._machines_profile = value
        self.schedules["machines_profile"] = list(
            islice(cycle(value), 8760))

    @property
    def lighting_profile(self):
        return self._lighting_profile

    @lighting_profile.setter
    def lighting_profile(self, value):
        self._lighting_profile = value
        self.schedules["lighting_profile"] = list(
            islice(cycle(value), 8760))

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):

        if value is not None:

            ass_error_1 = "Parent has to be an instance of ThermalZone()"

            assert type(value).__name__ == "ThermalZone", ass_error_1

            self._parent = value
            self._parent._use_conditions = self

        else:

            self._parent = None
