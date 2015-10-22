# created June 2015
# by TEASER4 Development Team


from teaser.Logic.BuildingObjects.BuildingPhysics.OuterWall \
    import OuterWall


class GroundFloor(OuterWall):
    '''This class represents a GroundFloor and is a child of OuterWall()
    '''

    def __init__(self, parent=None):
        '''
        '''
        super(GroundFloor, self).__init__(parent)
