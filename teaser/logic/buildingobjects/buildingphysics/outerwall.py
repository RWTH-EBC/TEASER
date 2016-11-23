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
