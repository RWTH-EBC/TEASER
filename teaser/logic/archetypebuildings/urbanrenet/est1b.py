# created June 2015
# by TEASER4 Development Team

from teaser.logic.archetypebuildings.urbanrenet.est1a \
    import EST1a


class EST1b(EST1a):
    """Urban Fabric Type EST1b.

    Subclass from EST1a for urban fabric type EST1b.

    Parameters
    ----------
    parent: Project()
        The parent class of this object, the Project the Building belongs
        to. Allows for better control of hierarchical structures.
        Default is None

    name : str
        individual name

    year_of_construction : int
        year of first construction

    number_of_floors : int
        number of floors above ground

    height_of_floors : float
        average height of the floors

    net_leased_area : float
        total net leased area of building

    with_ahu : boolean
        if building has a central AHU or not

    neighbour_buildings : int
        neighbour (default = 0)

        0: no neighbour
        1: one neighbour
        2: two neighbours

    construction_type : str
        construction type (default = "heavy")

        heavy: heavy construction
        light: light construction

    number_of_apartments : int
        number of apartments (default = 1)
    """

    def __init__(self,
                 parent,
                 name,
                 year_of_construction=None,
                 number_of_floors=None,
                 height_of_floors=None,
                 net_leased_area=None,
                 with_ahu=False,
                 neighbour_buildings=None,
                 construction_type=None,
                 number_of_apartments=None):
        """Constructor of EST1a


        """

        super(EST1b, self).__init__(parent, name, year_of_construction,
                                    number_of_floors, height_of_floors,
                                    net_leased_area, with_ahu,
                                    neighbour_buildings, construction_type)

        self.number_of_apartments = number_of_apartments
        self.est_factor_facade_to_volume = 0.87
