# created June 2015
# by TEASER4 Development Team


from teaser.logic.buildingobjects.buildingphysics.wall\
     import Wall


class InnerWall(Wall):
    """This class represents an inner wall and is a child of Wall()
    """

    def __init__(self, parent=None):
        """
        """
        super(InnerWall, self).__init__(parent)

        self._tilt = 90.0
        self._inner_convection = 1.7
        self._inner_radiation = 5.0
        self._outer_convection = 1.7
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

            if type(self).__name__ == "InnerWall":
                self.__parent.inner_walls.append(self)
            elif type(self).__name__ == "Ceiling":
                self.__parent.ceilings.append(self)
            elif type(self).__name__ == "Floor":
                self.__parent.floors.append(self)
            else:
                raise ValueError('Instance of InnerWall not known')

            if self.parent.parent is not None:
                self.year_of_construction = \
                    self.parent.parent.year_of_construction
            else:
                pass
        else:

            self.__parent = None
