# created November 2015
# by TEASER4 Development Team

"""This module includes a class for central AHU 
"""

class BuildingAHU(object):
    '''Building Class

    This class represents a BuildingAHU. 
    
    !AixLib sepcific!

    Parameters
    ----------

    parent: Project()
        The parent class of this object, the Building the AHU belongs to.
        Allows for better control of hierarchical structures.
        (default: None)

    Attributes
    ----------
    heating : Boolean (default = True)
        Heating Function of AHU
    cooling : Boolean (default = True)
        Cooling Function of AHU
    dehumidification : Boolean (default = True)
        Dehumidification Function of AHU (Cooling and Heating must be enabled)
    humidification : Boolean (default = True)
        Humidification Function of AHU (Cooling and Heating must be enabled)
    heat_recovery : Boolean (default = True)
        Is a HeatRecoverySystem physically integrated in the AHU? in AixLib:
        "HRS"
    by_pass_dehumidification : float (default = 0.2)
         By-pass factor of cooling coil during dehumidification. Necessary to 
         calculate the real outgoing enthalpy flow of heat exchanger in 
         dehumidification mode taking the surface enthalpy of the cooling 
         coil into account. In AixLib called "BPF_DeHu"
    efficiency_recovery : float (default = 0.8)
        efficiency of HRS in the AHU modes when HRS is enabled. in AixLib:
        "efficiencyHRS_enabled"
    efficiency_revocery_false : float (default = 0.2)
        taking a little heat transfer into account although HRS is disabled 
        (in case that a HRS is physically installed in the AHU) in AixLib:
        "efficiencyHRS_disabled"
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
        
        self.heating = True
        self.cooling = True
        self.dehumidification = True
        self.humidification = True
        self.heat_recovery = True
        self.by_pass_dehumidification = 0.2
        self.efficiency_recovery = 0.8
        self.efficiency_revocery_false = 0.2

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

            self.__parent.central_ahu = self