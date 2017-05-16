# created June 2015
# by TEASER4 Development Team
from collections import OrderedDict


class GUIInfo():
    '''
    Storage for a list of values for the GUI
    '''

    def __init__(self):
        '''
        Constructor
        '''

        # Base-Values for the Main Tab and subwindows
        self.hoursInADay = ["00:00", "01:00", "02:00", "03:00", "04:00",
                            "05:00", "06:00", "07:00", "08:00", "09:00",
                            "10:00", "11:00", "12:00", "13:00", "14:00",
                            "15:00", "16:00", "17:00", "18:00", "19:00",
                            "20:00", "21:00", "22:00", "23:00", "24:00", ]
        self.orientations = ["North", "North-East", "East", "South-East",
                             "South", "South-West", "West", "North-West",
                             "Roof", "Floor"]

        self.orientations_numbers = \
            OrderedDict([(0, 'North'), (45, 'North-East'), (90, "East"),
                         (135, "South-East"), (180, "South"),
                         (225, "South-West"), (270, "West"),
                         (315, "North-West"), (- 1, "Roof"),
                         (-2, "Floor")])

        self.orientations_strings = {"North": 0, "North-East": 45,
                                     "East": 90, "South-East": 135,
                                     "South": 180, "South-West": 225,
                                     "West": 270, "North-West": 315,
                                     "Roof": -1, "Floor": -2}
        self.type_buildings = ["Office", "Institute 4",
                               "Institute 8", "Institute General",
                               "SingleFamilyDwelling"]
        self.thermal_zone_types = ["Single office",
                                   "Group Office (between 2 and 6 employees)",
                                   "Open-plan Office (7 or more employees)",
                                   "Meeting, Conference, seminar",
                                   "Main Hall, Reception",
                                   "Retail, department store",
                                   "Retail with cooling",
                                   "Class room (school), group room "
                                   "(kindergarden)",
                                   "Lecture hall, auditorium",
                                   "Bed room", "Hotel room",
                                   "Canteen", "Restaurant",
                                   "Kitchen in non-residential buildings",
                                   "Kitchen - preparations, storage",
                                   "WC and sanitary rooms in non-residential"
                                   " buildings", "Further common rooms",
                                   "Auxiliary areas (without common rooms)",
                                   "Traffic area",
                                   "Stock, technical equipment, archives",
                                   "Data center",
                                   "Commercial and industrial Halls - "
                                   "heavy work, standing activity",
                                   "Commercial and industrial Halls - "
                                   "medium work, standing activity",
                                   "Commercial and industrial Halls - "
                                   "light work, standing activity",
                                   "Spectator area (theater and event venues)",
                                   "Foyer (theater and event venues)",
                                   "Stage (theater and event venues)",
                                   "Exhibition, congress",
                                   "Exhibition room and museum conservational"
                                   " demands",
                                   "Library - reading room",
                                   "Library - open stacks",
                                   "Library - magazine and depot",
                                   "Gym (without spectator area",
                                   "Parking garages (office and private "
                                   "usage)", "Parking garages (public usage)",
                                   "Sauna area", "Exercise room", "Laboratory",
                                   "Examination- or treatment room",
                                   "Special care aera",
                                   "Corridors in the general care area",
                                   "Medical and therapeutic practices",
                                   "Storehouse, logistics building",
                                   "Living"]
        self.building_model = ["AixLib.Building.LowOrder.ThermalZone",
                               "Cities.BuildingPhysics.ThermalZone",
                               "Cities.TypeBuilding",
                               "Cities.TypeBuildingRWin",
                               "Cities.HouseMultizone-Platzhalter"]
        self.ventilation_model = ["Heating", "Heating and Cooling",
                                  "Heating, Cooling and Humidification",
                                  "Heating, Cooling and HRS",
                                  "Heating, Cooling, Humidification and HRS",
                                  "Full AHU System"]
