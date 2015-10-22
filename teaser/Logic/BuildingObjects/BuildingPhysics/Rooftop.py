# created June 2015
# by TEASER4 Development Team


from teaser.Logic.BuildingObjects.BuildingPhysics.OuterWall \
    import OuterWall


class Rooftop(OuterWall):
    '''
    This class represents a roof top and is a child of OuterWall()
    '''

    def __init__(self, parent=None):
        '''
        '''
        super(Rooftop, self).__init__(parent)
