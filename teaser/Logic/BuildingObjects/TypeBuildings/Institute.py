# created June 2015
# by TEASER4 Development Team


from teaser.Logic.BuildingObjects.TypeBuildings.Office import Office


class Institute(Office):
    '''Type Institute Building (type 4)
    '''

    def __init__(self, parent=None, name=None, year_of_construction=None,
                 number_of_floors=None, height_of_floors=None,
                 net_leased_area=None, office_layout=None,
                 window_layout=None, construction_type=None):

        '''Constructor of Institute

        Adds an additional zone "Laboratory"

        '''

        super(Institute, self).__init__(parent, name, year_of_construction,
                                        number_of_floors, height_of_floors,
                                        net_leased_area, office_layout,
                                        window_layout, construction_type)

        self.zone_area_factors =\
            {"Meeting": [0.04, "Meeting, Conference, seminar"],
             "Storage": [0.1, "Stock, technical equipment, archives"],
             "Office": [0.4, "Group Office (between 2 and 6 employees)"],
             "Sanitary": [0.04, "WC and sanitary rooms\
              in non-residential buildings"],
             "ICT": [0.02, "Data center"],
             "Floor": [0.25, "Traffic area"],
             "Laboratory": [0.15, "Laboratory"]}

        self.file_ahu = "Institute/AHU_Institute.mat"
        self.file_internal_gains = "Institute/InternalGains_"
        "Institute.mat"
        self.file_set_t = "Institute/Tset_Institute.mat"
        self.file_weather = self.parent.weather_file_name
