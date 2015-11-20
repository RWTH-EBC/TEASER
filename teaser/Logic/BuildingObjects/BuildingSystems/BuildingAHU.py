# created November 2015
# by TEASER4 Development Team

"""This module includes a class for central AHU 
"""

class BuildingAHU(object):
    '''Building Class

    This class represents a general building

    Parameters
    ----------

    parent: Project()
        The parent class of this object, the Building the AHU belongs to.
        Allows for better control of hierarchical structures.
        (default: None)
    
    Note: the listed attributes are just the ones that are set by the user
          calculated values are not included in this list

    Attributes
    ----------

    profile_relative_humidity : [float]
        timeline of relative humidity requirements for AHU simulation
    profile_status_AHU : [Boolean]
        timeline of status of the AHU simulation (on/off)
    profile_temeprature_AHU : [float]
        timeline of temperatures requirements for AHU simulation

    '''
    
    def __init__(self, parent=None):
        '''Constructor of BuildingAHU Class
        '''
        self.parent = parent
        self.profile_min_relative_humidity = []
        self.profile_max_relative_humidity = []
        self.profile_status_AHU = []
        self.profile_temperature_AHU = []
        
    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        if value is not None:
            ass_error_1 = "Parent has to be an instance of Building()"

            assert type(value).__name__ == "Building" \
                or type(value).__name__ == "Office"\
                or type(value).__name__ == "Institute"\
                or type(value).__name__ == "Institute4"\
                or type(value).__name__ == "Institute8" \
                or type(value).__name__ == "Residential", ass_error_1

            self.__parent = value

        if type(value).__name__ == "Building" \
           or type(value).__name__ == "Office" \
           or type(value).__name__ == "Institute" \
           or type(value).__name__ == "Institute4" \
           or type(value).__name__ == "Institute8" \
           or type(value).__name__ == "Residential":

            self.__parent.central_ahu.append(self)