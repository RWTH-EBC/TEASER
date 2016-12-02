# created June 2015
# by TEASER4 Development Team


from teaser.logic.buildingobjects.buildingphysics.wall \
    import Wall


class OuterWall(Wall):
    """
    This class represents an outer wall and is a child of Wall()
    """

    def __init__(self, parent=None):
        """
        """
        super(OuterWall, self).__init__(parent)

        self._tilt = 90.0
        self._inner_convection = 2.7
        self._inner_radiation = 5.0
        self._outer_convection = 20.0
        self._outer_radiation = 5.0

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        if value is not None:

            ass_error_1 = "Parent has to be an instance of ThermalZone()"

            assert type(value).__name__ == "ThermalZone", ass_error_1

            self.__parent = value

            if type(self).__name__ == "OuterWall":
                self.__parent.outer_walls.append(self)
            elif type(self).__name__ == "Rooftop":
                self.__parent.rooftops.append(self)
            elif type(self).__name__ == "GroundFloor":
                self.__parent.ground_floors.append(self)
            else:
                raise ValueError('Instance of OuterWall not known')

            if self.parent.parent is not None:
                self.year_of_construction = \
                    self.parent.parent.year_of_construction
            else:
                pass
        else:

            self.__parent = None

