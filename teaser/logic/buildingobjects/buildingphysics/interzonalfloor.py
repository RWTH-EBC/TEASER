# created April 2023
# by TEASER4 Development Team


from teaser.logic.buildingobjects.buildingphysics.interzonalwall \
    import InterzonalWall


class InterzonalFloor(InterzonalWall):
    """InterzonalFloor (InterzonalWall)

    This class represents an interzonal floor and is a child of InterzonalWall()

    Note that interzonal elements have to be created twice for each zone they
    connect and are not semantically connected afterwards. For an
    InterzonalFloor of one zone, an InterzonalCeiling has to be created for the
    zone on the other side.

    Parameters
    ----------

    parent : ThermalZone()
        The parent class of this object, the ThermalZone the BE belongs to.
        Allows for better control of hierarchical structures. If not None it
        adds this InterzonalFloor to ThermalZone.interzonal_floors.
        Default is None.

    Attributes
    ----------

    internal_id : float
        Random id for the distinction between different elements.
    name : str
        Individual name
    construction_data : str
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
        Tilt against horizontal, default is 0.0
    orientation : float [degree]
        Azimuth direction of building element (0 : north, 90: east, 180: south,
        270: west), default is -2, for horizontal floor
    inner_convection : float [W/(m2*K)]
        Constant heat transfer coefficient of convection inner side (facing
        the zone), default is 1.7
    inner_radiation : float [W/(m2*K)]
        Constant heat transfer coefficient of radiation inner side (facing
        the zone), default is 5.0
    outer_convection : float [W/(m2*K)]
        Constant heat transfer coefficient of convection outer side (facing
        the ambient or adjacent zone). Default 0.0 - if unchanged, 1.7 when
        adding an outside
    outer_radiation : float [W/(m2*K)]
        Constant heat transfer coefficient of radiation outer side (facing
        the ambient or adjacent zone). Default 0.0 - if unchanged, 5.0 when
        adding an outside
    layer : list
        List of all layers of a building element (to be filled with Layer
        objects). Use element.layer = None to delete all layers of the building
        element
    other_side : ThermalZone()
        the thermal zone on the upper side of the interzonal floor
    interzonal_type_material : str
        one of (None (default), 'inner', 'outer_ordered', 'outer_reversed')
        describes as which kind of element the element is treated when loading
        type elements. Caution: Make sure that the complimentary element of
        the other zone is also changed accordingly if this is adapted manually
            None: treatment based on project.method_interzonal_export_enrichment
            'inner': InterzonalWall treated as InnerWall,
                     InterzonalFloor treated as Floor,
                     InterzonalCeiling treated as Ceiling
            'outer_ordered': InterzonalWall treated as Wall,
                             InterzonalFloor treated as GroundFloor,
                             InterzonalCeiling treated as Rooftop
            'outer_reversed': like 'outer_ordered', but with reversed layers,
                              resulting in the reversed sequence of layers as
                              for the complimentary element declared as
                              'outer_ordered'
    interzonal_type_export : str
        one of (None (default), 'inner', 'outer_ordered', 'outer_reversed')
        describes as which kind of element the element is treated when exporting
        to Modelica. Caution: Make sure that the complimentary element of
        the other zone is also changed accordingly if this is adapted manually
            'inner': element will be lumped with InnerWall. No heat flow to the
                     zone on the other side will be modelled.
            'outer_ordered': element will be lumped with OuterWall (OneElement
                             to FourElement export) or treated as border to an
                             adjacent zone (FiveElement export). Borders to the
                             same adjacent zone will be lumped.
            'outer_reversed': like 'outer_ordered', but the lumping follows
                              VDI 6007-1 in reversed order, resulting in the
                              reversed order of resistances and capacitors as
                              for the complimentary element declared as
                              'outer_ordered'

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
    r_outer_comb : float [K/W]
        Combined convective and radiative resistance of building element on
        outer side (facing the ambient or adjacent zone). Currently for all
        InnerWalls and GroundFloors this value is set to 0.0
    wf_out : float
        Weightfactor of building element ua_value/ua_value_zone

    """

    def __init__(self, parent=None, other_side=None):
        """
        """
        super(InterzonalFloor, self).__init__(parent, other_side)

        self._tilt = 0.0
        self._orientation = -2.0

    def retrofit_wall(self,
                      year_of_retrofit,
                      material=None,
                      add_at_position=None):
        """Retrofits wall to German refurbishment standards.

        This function adds an additional layer of insulation and sets the
        thickness of the layer according to the retrofit standard in the
        year of refurbishment. Refurbishment year must be newer then 1977

        Note: To Calculate thickness and U-Value, the standard TEASER
        coefficients for outer and inner heat transfer are used.

        The used Standards are namely the Waermeschutzverordnung (WSVO) and
        Energieeinsparverordnung (EnEv)

        Parameters
        ----------
        material : string
            Type of material, that is used for insulation
        year_of_retrofit : int
            Year of the retrofit of the wall/building
        add_at_position : int
            position at which to insert the insulation layer.
            0 inside, None (default) or -1 outside/other side

        """
        if self.interzonal_type_material == 'inner':
            return
        elif add_at_position is None:
            if self.interzonal_type_material == 'outer_reversed':
                add_at_position = 0
            elif self.interzonal_type_material == 'outer_ordered':
                add_at_position = -1

        material, year_of_retrofit, ins_layer = self.initialize_retrofit(
            material, year_of_retrofit, add_at_position
        )

        calc_u = None

        if 1977 <= year_of_retrofit <= 1981:
            calc_u = 0.8
        elif 1982 <= year_of_retrofit <= 1994:
            calc_u = 0.7
        elif 1995 <= year_of_retrofit <= 2001:
            calc_u = 0.5
        elif 2002 <= year_of_retrofit <= 2008:
            calc_u = 0.4
        elif 2009 <= year_of_retrofit <= 2013:
            calc_u = 0.3
        elif year_of_retrofit >= 2014:
            calc_u = 0.3

        self.set_insulation(material, calc_u, year_of_retrofit,
                            ins_layer_index=ins_layer)
