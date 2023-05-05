# created April 2023
# by TEASER4 Development Team


from teaser.logic.buildingobjects.buildingphysics.wall\
    import Wall
from teaser.logic.buildingobjects.buildingphysics.buildingelement\
    import BuildingElement


class InterzonalWall(Wall):
    """InterzonalWall class

    This class holds information for an interzonal wall and is a child of Wall()

    Note that interzonal elements have to be created twice for each zone they
    connect and are not semantically connected afterwards. For an
    InterzonalWall of one zone, an InterzonalWall has to be created for the
    zone on the other side.

    Parameters
    ----------

    parent : ThermalZone()
        The parent class of this object, the ThermalZone the BE belongs to.
        Allows for better control of hierarchical structures. If not None it
        adds this InterzonalWall to ThermalZone.interzonal_walls.
        Default is None.

    Attributes
    ----------

    internal_id : float
        Random id for the distinction between different elements.
    name : str
        Individual name
    construction_type : str
        Type of construction (e.g. "heavy" or "light"). Needed for
        distinction between different constructions types in the same
        building age period.
    year_of_retrofit : int
        Year of last retrofit
    year_of_construction : int
        Year of first construction
    building_age_group : list
        Determines the building age period that this building
        element belongs to [begin, end], e.g. [1984, 1994]
    area : float [m2]
        Area of building element
    tilt : float [degree]
        Tilt against horizontal, default is 90.0
    orientation : float [degree]
        Azimuth direction of building element (0 : north, 90: east, 180: south,
        270: west)
    inner_convection : float [W/(m2*K)]
        Constant heat transfer coefficient of convection inner side (facing
        the zone), default 1.7
    inner_radiation : float [W/(m2*K)]
        Constant heat transfer coefficient of radiation inner side (facing
        the zone), default 5.0
    outer_convection : float [W/(m2*K)]
        Constant heat transfer coefficient of convection outer side (facing
        the ambient or adjacent zone), default 1.7
    outer_radiation : float [W/(m2*K)]
        Constant heat transfer coefficient of radiation outer side (facing
        the ambient or adjacent zone), default 5.0
    layer : list
        List of all layers of a building element (to be filled with Layer
        objects). Use element.layer = None to delete all layers of the building
        element
    other_side : ThermalZone()
        the thermal zone on the other side of the interzonal wall

    Calculated Attributes

    r1 : float [K/W]
        equivalent resistance R1 of the analogous model given in VDI 6007
    r2 : float [K/W]
        equivalent resistance R2 of the analogous model given in VDI 6007
    r3 : float [K/W]
        equivalent resistance R3 of the analogous model given in VDI 6007
    c1 : float [J/K]
        equivalent capacity C1 of the analogous model given in VDI 6007
    c2 : float [J/K]
        equivalent capacity C2 of the analogous model given in VDI 6007
    c1_korr : float [J/K]
        corrected capacity C1,korr for building elements in the case of
        asymmetrical thermal load given in VDI 6007
    ua_value : float [W/K]
        UA-Value of building element (Area times U-Value)
    r_inner_conv : float [K/W]
        Convective resistance of building element on inner side (facing the
        zone)
    r_inner_rad : float [K/W]
        Radiative resistance of building element on inner side (facing the
        zone)
    r_inner_conv : float [K/W]
        Combined convective and radiative resistance of building element on
        inner side (facing the zone)
    r_outer_conv : float [K/W]
        Convective resistance of building element on outer side (facing
        the ambient or adjacent zone). Currently for all InnerWalls and
        GroundFloors this value is set to 0.0
    r_outer_rad : float [K/W]
        Radiative resistance of building element on outer side (facing
        the ambient or adjacent zone). Currently for all InnerWalls and
        GroundFloors this value is set to 0.0
    r_outer_conv : float [K/W]
        Combined convective and radiative resistance of building element on
        outer side (facing the ambient or adjacent zone). Currently for all
        InnerWalls and GroundFloors this value is set to 0.0
    wf_out : float
        Weightfactor of building element ua_value/ua_value_zone
    """

    def __init__(self, parent=None, other_side=None):
        """
        """
        super(InterzonalWall, self).__init__(parent, other_side)

        self._tilt = 90.0
        self._inner_convection = 1.7
        self._inner_radiation = 5.0
        self._outer_convection = 1.7
        self._outer_radiation = 5.0

    def load_type_element(
            self,
            year,
            construction,
            data_class=None,
            element_type=None,
            reverse_layers=False,
            type_element_key=None
    ):
        """Typical element loader.

        Loads typical interzonal wall elements according to their construction
        year and their construction type from a json.

        This function will only work if the parents to Building are set.

        Parameters
        ----------
        year : int
            Year of construction

        construction : str
            Construction type, code list ('heavy', 'light')

        data_class : DataClass()
            DataClass containing the bindings for TypeBuildingElement and
            Material (typically this is the data class stored in prj.data,
            but the user can individually change that. Default is
            self.parent.parent.parent.data (which is data_class in current
            project)

        element_type : str
            Element type to load - only to specify if the json entry for a
            different type than type(element) is to be loaded, e.g. InnerWall
            instead of OuterWall. Default: For interzonal walls between two
            heated or two unheated zones, typical inner walls will be  loaded.
            For interzonal walls between a heated and an unheated zone,
            typical outer wall will be loaded (if element_type is not specified)

        reverse_layers : bool
            defines if layer list should be reversed

        type_element_key : str
            Element to load - specify the full json entry

        """
        if element_type is None:
            if (self.other_side.use_conditions.with_heating is True
                and self.parent.use_conditions.with_heating is True) \
                or (self.other_side.use_conditions.with_heating is False
                    and self.parent.use_conditions.with_heating is False):
                if type(self).__name__ == "InterzonalWall":
                    element_type = 'InnerWall'
                elif type(self).__name__ == "InterzonalCeiling":
                    element_type = 'Ceiling'
                elif type(self).__name__ == "InterzonalFloor":
                    element_type = 'Floor'
                else:
                    raise ValueError('Instance of InterzonalWall not known')
            else:
                if type(self).__name__ == "InterzonalWall":
                    if self.other_side.use_conditions.with_heating is True:
                        reverse_layers = True
                    element_type = 'OuterWall'
                elif type(self).__name__ == "InterzonalCeiling":
                    if self.other_side.use_conditions.with_heating is True:
                        reverse_layers = True
                        element_type = 'GroundFloor'
                    else:
                        element_type = 'Rooftop'
                elif type(self).__name__ == "InterzonalFloor":
                    if self.other_side.use_conditions.with_heating is True:
                        reverse_layers = True
                        element_type = 'Rooftop'
                    else:
                        element_type = 'GroundFloor'
                else:
                    raise ValueError('Instance of InterzonalWall not known')
        BuildingElement.load_type_element(
            self,
            year=year,
            construction=construction,
            data_class=data_class,
            element_type=element_type,
            reverse_layers=reverse_layers,
            type_element_key=type_element_key
        )

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        if value is not None:

            ass_error_1 = "Parent has to be an instance of ThermalZone()"

            assert type(value).__name__ == "ThermalZone", ass_error_1

            self.__parent = value

            if type(self).__name__ == "InterzonalWall":
                self.__parent.interzonal_walls.append(self)
            elif type(self).__name__ == "InterzonalCeiling":
                self.__parent.interzonal_ceilings.append(self)
            elif type(self).__name__ == "InterzonalFloor":
                self.__parent.interzonal_floors.append(self)
            else:
                raise ValueError('Instance of InterzonalWall not known')

            if self.parent.parent is not None:
                self.year_of_construction = \
                    self.parent.parent.year_of_construction
            else:
                pass
        else:

            self.__parent = None