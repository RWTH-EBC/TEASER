"""
Created June 2015

@author: TEASER 4 Development Team
"""

import random


class UseConditions(object):
    """Base class for all Use Conditions inside a thermal zone.

    All Use Conditions (boundary conditions assigned to user behavior and
    schedules should be inherited from this class)

    Parameters
    ----------

    parent: ThermalZone()
        The parent class of this object, the zone the use conditions belong
        to. Allows for better control of hierarchical structures. If not None it
        adds this UseConditions instance to ThermalZone.use_conditions.
        Default is None

    Attributes
    ----------

    internal_id : float
        random id for the distinction between different use conditions
    """

    def __init__(self, parent=None):
        """Constructor for UseConditions
        """

        self.internal_id = random.random()

        self.parent = parent

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):

        if value is not None:

            ass_error_1 = "Parent has to be an instance of ThermalZone()"

            assert type(value).__name__ == "ThermalZone", ass_error_1

            self._parent = value

        else:

            self._parent = None
