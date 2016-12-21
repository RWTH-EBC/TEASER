# created June 2015
# by TEASER4 Development Team


from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall


class Ceiling(InnerWall):
    """Ceiling (InnerWall)

    This class represents a ceiling and is a child of InnerWall()
    """

    def __init__(self, parent=None):
        """Constructor Ceiling (InnerWall)

        """
        super(Ceiling, self).__init__(parent)
        
        self._tilt = 90.0
        self._orientation = -1.0
