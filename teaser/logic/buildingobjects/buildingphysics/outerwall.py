# created June 2015
# by TEASER4 Development Team
import warnings

from teaser.logic.buildingobjects.buildingphysics.wall \
    import Wall


class OuterWall(Wall):
    """OuterWall class

    This class holds information of an outer wall and is a child of Wall()

    Parameters
    ----------

    parent : ThermalZone()
        The parent class of this object, the ThermalZone the BE belongs to.
        Allows for better control of hierarchical structures. If not None it
        adds this OuterWall to ThermalZone.outer_walls.
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
        Area of building element. This is always the net area (without windows).
        Windows will be handled separately. See also merge_windows_calc
        documentation in project.py.
    tilt : float [degree]
        Tilt against horizontal, default is 90.0
    orientation : float [degree]
        Azimuth direction of building element (0 : north, 90: east, 180: south,
        270: west)
    inner_convection : float [W/(m2*K)]
        Constant heat transfer coefficient of convection inner side (facing
        the zone), default 2.7
    inner_radiation : float [W/(m2*K)]
        Constant heat transfer coefficient of radiation inner side (facing
        the zone), default 5.0
    outer_convection : float [W/(m2*K)]
        Constant heat transfer coefficient of convection outer side (facing
        the ambient or adjacent zone), default 20.0
    outer_radiation : float [W/(m2*K)]
        Constant heat transfer coefficient of radiation outer side (facing
        the ambient or adjacent zone), default 5.0
    layer : list
        List of all layers of a building element (to be filled with Layer
        objects). Use element.layer = None to delete all layers of the building
        element

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

    def __init__(self, parent=None):
        """
        """
        super(OuterWall, self).__init__(parent)

        self._tilt = 90.0
        self._inner_convection = 2.7
        self._inner_radiation = 5.0
        self._outer_convection = 20.0
        self._outer_radiation = 5.0

    def retrofit_wall(self, retrofit_type, material=None):
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

        """
        self.set_calc_default()
        self.calc_ua_value()

        if material is None:
            material = "EPS_perimeter_insulation_top_layer"
        else:
            pass

        calc_u = None

        if retrofit_type == 'WSVO 1977':
            calc_u = 1.06
        elif retrofit_type == 'WSVO 1982':
            calc_u = 0.6
        elif retrofit_type == 'WSVO 1995':
            calc_u = 0.5
        elif retrofit_type == 'EnEV 2002':
            calc_u = 0.45
        elif retrofit_type == 'EnEV 2009':
            calc_u = 0.24
        # 115 % of GEG Reference building transmission loss
        elif retrofit_type == 'KfW Effizienzhaus 100':
            calc_u = 0.322
        # 100 % of GEG Reference building transmission loss
        elif retrofit_type == 'KfW Effizienzhaus 85':
            calc_u = 0.28
        # 85 % of GEG Reference building transmission loss
        elif retrofit_type == 'KfW Effizienzhaus 70':
            calc_u = 0.24
        # 70 % of GEG Reference building transmission loss
        elif retrofit_type == 'KfW Effizienzhaus 55':
            calc_u = 0.196
        # 55 % of GEG Reference building transmission loss
        elif retrofit_type == 'KfW Effizienzhaus 40':
            calc_u = 0.154


        self.set_insulation(material, calc_u, retrofit_type)

    def set_insulation(self, material, calc_u, retrofit_type):
        if calc_u:
            if self.u_value < calc_u:
                warnings.warn(f'No retrofit needed for {self.name} as u value '
                              f'is already lower than needed.')
            else:
                self.insulate_wall(material)
                self.set_ins_layer_thickness(calc_u)
        else:
            warnings.warn(f'No fitting retrofit type found for {retrofit_type}')


    def set_ins_layer_thickness(self, calc_u):
        """Sets the thickness of the fresh insulated layer from retrofit"""
        r_conduc_rem = 0
        for count_layer in self.layer[:-1]:
            r_conduc_rem += (count_layer.thickness /
                         count_layer.material.thermal_conduc)

        lambda_ins = self.layer[-1].material.thermal_conduc

        d_ins = lambda_ins * (1 / calc_u - self.r_outer_comb * self.area -
                              self.r_inner_comb * self.area - r_conduc_rem)
        self.layer[-1].thickness = d_ins
        self.layer[-1].id = len(self.layer)

            # old original (not correct)
            # for count_layer in self.layer[:-1]:
            #     r_conduc += (count_layer.thickness /
            #                  count_layer.material.thermal_conduc)
            #
            #     self.layer[-1].thickness = \
            #         (((
            #                   1 - calc_u * self.r_inner_comb - calc_u *
            #                   self.r_outer_comb) /
            #           calc_u) * self.area - r_conduc) * \
            #         self.layer[-1].material.thermal_conduc
            #
            #     self.layer[-1].id = len(self.layer)
            #
            # print(self.layer[-1].thickness)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        if value is not None:

            ass_error_1 = "Parent has to be an instance of ThermalZone()"

            assert type(value).__name__ == "ThermalZone", ass_error_1

            self.__parent = value

            if type(self).__name__ == "OuterWall":
                self.__parent.outer_walls.append(self)
            elif type(self).__name__ == "Rooftop":
                self.__parent.rooftops.append(self)
            elif type(self).__name__ == "GroundFloor":
                self.__parent.ground_floors.append(self)
            else:
                raise ValueError('Instance of OuterWall not known')

            if self.parent.parent is not None:
                self.year_of_construction = \
                    self.parent.parent.year_of_construction
            else:
                pass
        else:

            self.__parent = None
