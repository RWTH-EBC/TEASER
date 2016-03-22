# created June 2015
# by TEASER4 Development Team



from teaser.Logic.BuildingObjects.Building import Building


class ArchetypeBuilding(Building):
    '''Root Class for each type building.

    Class as parent of specific type buildings. Subclass from Building to
    represent Type Buildings. Superclass for every type building.

    '''

    def __init__(self,
                 parent=None,
                 name=None,
                 year_of_construction=None,
                 number_of_floors=None,
                 height_of_floors=None,
                 net_leased_area=None,
                 with_ahu=False):
        '''Constructor of TypeBuilding
        '''

        super(ArchetypeBuilding, self).__init__(parent,
                                                name,
                                                year_of_construction,
                                                number_of_floors,
                                                height_of_floors,
                                                net_leased_area,
                                                with_ahu)
        
        self.file_ahu = "\\AHU_"+self.name+".mat"
        self.file_internal_gains = "\\InternalGains_"+self.name+".mat"
        self.file_set_t = "\\Tset_"+self.name+".mat"
        self.file_weather = self.parent.weather_file_name		
        
