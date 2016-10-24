# created June 2015
# by TEASER4 Development Team


from teaser.logic.buildingobjects.buildingphysics.buildingelement \
    import BuildingElement


class Window(BuildingElement):
    """This class represents a window and is a child of BuildingElement().

    Attributes
    ----------
    g_value : float
        g Value of the window

    a_conv : float
        convective coefficient of inner side of wall according to VDI 6007

    shading_g_total : float
        shaded g value of the window

    shading_max_irr : float
        threshold for automatic shading

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

    def replace_window(self, year_of_refurbishment, window_type=None):
        """Replace a window, with a newer one.

        Replaces all attributes from the window and replaces it with a high
        insultaed one.

        Parameters
        ----------
        year_of_refurbishment: int
            The year, the building was refurbished

        construction: str
            Default: EnEv 2014
        """

        if window_type is None:
            window_type = "EnEv"
        else:
            pass

        self.set_calc_default()
        self.layer = None
        self.load_type_element(year_of_refurbishment,
                               window_type,
                               self.parent.parent.parent.data)

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
