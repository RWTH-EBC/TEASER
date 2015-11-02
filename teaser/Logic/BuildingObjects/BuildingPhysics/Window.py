# created June 2015
# by TEASER4 Development Team


from teaser.Logic.BuildingObjects.BuildingPhysics.BuildingElement \
    import BuildingElement


class Window(BuildingElement):

    '''This class represents a window and is a child of BuildingElement().

    Attributes
    ----------
    g_value : float
        g Value of the window

    a_conv : float
        convective coefficient of inner side of wall according to VDI 6007

    shading : Shading()
        instance of shading type
    '''

    def __init__(self, parent=None):

        super(Window, self).__init__(parent)
        self.g_value = 0.0
        self.a_conv = 0.0
        self.shading_g_total = 0.0
        self.shading_max_irr = 0.0
        self._shading = None

    def calc_equivalent_res(self):
        '''Equivalent resistance VDI 6007

        Calculates the equivalent resistance of a wall according to  VDI
        6007 guideline.

        Parameters
        ----------
        t_bt : int
            time constant according to VDI 6007 (default t_bt = 7)
        '''
        number_of_layer, density, thermal_conduc, heat_capac, thickness = \
            self.gather_element_properties()

        r_layer = thickness/thermal_conduc
        c_layer = heat_capac*density*thickness  # *1000

        for layer_count in r_layer:
            self.r1 += layer_count / self.area

        for layer_count in c_layer:
            self.c1 += layer_count

    def replace_window(self, year_of_retrofit, window_type=None):
        '''Replace a window, with a newer one.

        Replaces all attributes from the window and replaces it with a high
        insultaed one.

        Parameters
        ----------
        year_of_refurbishment: int
            The year, the building was refurbished

        construction: str
            Default: EnEv 2014
        '''

        if window_type is None:
            window_type = "EnEv"
        else:
            pass

        self.set_calc_default()

        self.load_type_element(year_of_retrofit, window_type)
