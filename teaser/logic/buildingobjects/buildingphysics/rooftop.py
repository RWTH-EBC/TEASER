# created June 2015
# by TEASER4 Development Team


from teaser.logic.buildingobjects.buildingphysics.outerwall \
    import OuterWall


class Rooftop(OuterWall):
    """
    This class represents a roof top and is a child of OuterWall()
    """

    def __init__(self, parent=None):
        """
        """
        super(Rooftop, self).__init__(parent)

        self._tilt = 0.0
        self._orientation = -1.0
        self._inner_convection = 1.7
        self._inner_radiation = 5.0
        self._outer_convection = 20.0
        self._outer_radiation = 5.0
