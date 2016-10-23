# created June 2015
# by TEASER4 Development Team


from teaser.logic.buildingobjects.building import Building


class Residential(Building):
    """Root Class for each type building.

    Class as parent of specific type buildings. Subclass from Building to
    represent Type Buildings. Superclass for every type building.

    """

    def __init__(self,
                 parent=None,
                 name=None,
                 year_of_construction=None,
                 net_leased_area=None,
                 with_ahu=False):
        """Constructor of TypeBuilding
        """

        super(Residential, self).__init__(parent,
                                          name,
                                          year_of_construction,
                                          net_leased_area,
                                          with_ahu)

        self.file_ahu = "/AHU_"+self.name+".mat"
        self.file_internal_gains = "/InternalGains_"+self.name+".mat"
        self.file_set_t = "/Tset_"+self.name+".mat"
        # self.file_weather = self.parent.weather_file_path

    def generate_archetype(self):
        """Generates an archetype building.

        Define your type of archetype generation.

        """

        pass
