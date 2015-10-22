# created June 2015
# by TEASER4 Development Team


from teaser.Logic.BuildingObjects.BuildingPhysics.Wall \
    import Wall


class OuterWall(Wall):
    '''
    This class represents an outer wall and is a child of Wall()
    '''

    def __init__(self, parent=None):
        '''
        '''
        super(OuterWall, self).__init__(parent)
