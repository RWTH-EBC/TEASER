# created June 2015
# by TEASER4 Development Team


from teaser.logic.buildingobjects.buildingphysics.buildingelement \
    import BuildingElement
import warnings


class Window(BuildingElement):
    """Window class

    This class holds information of a window and is a child of
    BuildingElement().

    Parameters
    ----------

    parent : ThermalZone()
        The parent class of this object, the ThermalZone the BE belongs to.
        Allows for better control of hierarchical structures.  If not None it
        adds this Window to ThermalZone.windows.
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
        Tilt against horizontal, default 90.0
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

    Specific Attributes for Window

    g_value : float
        solar heat gain coefficient of Window
    a_conv : float
        relative convective heat emission because of absorption of short wave
        irradiation of inner side of Window according to VDI 6007
    shading_g_total : float
        shaded g value of the window
    shading_max_irr : float
        threshold for automatic shading

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

        super(Window, self).__init__(parent)
        self._g_value = 0.0
        self._a_conv = 0.0
        self._shading_g_total = 0.0
        self._shading_max_irr = 0.0
        self._tilt = 90.0
        self._inner_convection = 2.7
        self._inner_radiation = 5.0
        self._outer_convection = 20.0
        self._outer_radiation = 5.0

    def calc_equivalent_res(self):
        """Equivalent resistance VDI 6007

        Calculates the equivalent resistance of a wall according to  VDI
        6007 guideline.

        Parameters
        ----------
        t_bt : int
            time constant according to VDI 6007 (default t_bt = 7)
        """
        self.set_calc_default()
        number_of_layer, density, thermal_conduc, heat_capac, thickness = \
            self.gather_element_properties()

        r_layer = thickness / thermal_conduc
        c_layer = heat_capac * density * thickness  # *1000

        for layer_count in r_layer:
            self.r1 += layer_count / self.area

        for layer_count in c_layer:
            self.c1 += layer_count

    def replace_window(self, year_of_retrofit, window_type=None):
        """Replace a window, with a newer one.

        Replaces all attributes from the window and replaces it with a high
        insulated one.

        Parameters
        ----------
        year_of_retrofit: int
            The year, the building was refurbished
        """

        if window_type is None:
            window_type = "EnEv"
        else:
            pass

        if year_of_retrofit < 1995:
            year_of_retrofit = 1995
            warnings.warn("You are using a year of retrofit not supported\
                    by teaser. We will change your year of retrofit to 1995\
                    for the calculation. Be careful!")

        self.set_calc_default()
        self.layer = None
        self.load_type_element(year_of_retrofit,
                               window_type,
                               self.parent.parent.parent.data)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):
        if value is not None:

            ass_error_1 = "Parent has to be an instance of ThermalZone()"

            assert type(value).__name__ == "ThermalZone", ass_error_1

            self.__parent = value

            if type(self).__name__ == "Window":
                self.__parent.windows.append(self)
            else:
                raise ValueError('Instance of Window not known')

            if self.parent.parent is not None:
                self.year_of_construction = \
                    self.parent.parent.year_of_construction
            else:
                pass
        else:

            self.__parent = None

    @property
    def g_value(self):
        return self._g_value

    @g_value.setter
    def g_value(self, value):

        if isinstance(value, float):
            self._g_value = value
        elif value is None:
            self._g_value = value
        else:
            try:
                value = float(value)
                self._g_value = value
            except:
                raise ValueError("Can't convert g value to float")

    @property
    def a_conv(self):
        return self._a_conv

    @a_conv.setter
    def a_conv(self, value):

        if isinstance(value, float):
            self._a_conv = value
        elif value is None:
            self._a_conv = value
        else:
            try:
                value = float(value)
                self._a_conv = value
            except:
                raise ValueError("Can't convert a conv to float")

    @property
    def shading_g_total(self):
        return self._shading_g_total

    @shading_g_total.setter
    def shading_g_total(self, value):

        if isinstance(value, float):
            self._shading_g_total = value
        elif value is None:
            self._shading_g_total = value
        else:
            try:
                value = float(value)
                self._shading_g_total = value
            except:
                raise ValueError("Can't convert shaded g value to float")

    @property
    def shading_max_irr(self):
        return self._shading_max_irr

    @shading_max_irr.setter
    def shading_max_irr(self, value):

        if isinstance(value, float):
            self._shading_max_irr = value
        elif value is None:
            self._shading_max_irr = value
        else:
            try:
                value = float(value)
                self._shading_max_irr = value
            except:
                raise ValueError("Can't convert max irradiation to float")
