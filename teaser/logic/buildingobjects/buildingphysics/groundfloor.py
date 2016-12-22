# created June 2015
# by TEASER4 Development Team


from teaser.logic.buildingobjects.buildingphysics.outerwall \
    import OuterWall


class GroundFloor(OuterWall):
    """This class represents a GroundFloor and is a child of OuterWall()
    """

    def __init__(self, parent=None):
        """
        """
        super(GroundFloor, self).__init__(parent)

        self._tilt = 0.0
        self._orientation = -2.0
        self._inner_convection = 1.7
        self._inner_radiation = 5.0
        self._outer_convection = None
        self._outer_radiation = None
