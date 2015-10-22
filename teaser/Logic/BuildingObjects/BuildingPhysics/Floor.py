# created June 2015
# by TEASER4 Development Team


from teaser.Logic.BuildingObjects.BuildingPhysics.InnerWall import InnerWall


class Floor(InnerWall):
    '''This class represents a floor and is a child of InnerWall()
    '''

    def __init__(self, parent=None):
        '''
        '''
        super(Floor, self).__init__(parent)
