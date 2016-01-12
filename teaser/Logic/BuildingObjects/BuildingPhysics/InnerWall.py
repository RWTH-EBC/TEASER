# created June 2015
# by TEASER4 Development Team


from teaser.Logic.BuildingObjects.BuildingPhysics.Wall\
     import Wall


class InnerWall(Wall):
    '''This class represents an inner wall and is a child of Wall()
    '''

    def __init__(self, parent=None):
        '''
        '''
        super(InnerWall, self).__init__(parent)

        self._tilt = 90.0
        self._inner_convection = 1.7
        self._inner_radiation = 5.0
