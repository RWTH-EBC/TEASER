"""asd"""
from teaser.logic.buildingobjects.buildingphysics.buildingelement \
    import BuildingElement
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
import numpy as np
import warnings


class Wall(BuildingElement):
    """Wall class

    This class holds functions and information for walls. It inherits for
    BuildingElement() and is a base class for all inner and outer walls.

    Parameters
    ----------

    parent : ThermalZone()
        The parent class of this object, the ThermalZone the BE belongs to.
        Allows for better control of hierarchical structures.
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
        Tilt against horizontal
    orientation : float [degree]
        Azimuth direction of building element (0 : north, 90: east, 180: south,
        270: west)
    inner_convection : float [W/(m2*K)]
        Constant heat transfer coefficient of convection inner side (facing
        the zone)
    inner_radiation : float [W/(m2*K)]
        Constant heat transfer coefficient of radiation inner side (facing
        the zone)
    outer_convection : float [W/(m2*K)]
        Constant heat transfer coefficient of convection outer side (facing
        the ambient or adjacent zone). Currently for all InnerWalls and
        GroundFloors this value is set to 0.0
    outer_radiation : float [W/(m2*K)]
        Constant heat transfer coefficient of radiation outer side (facing
        the ambient or adjacent zone). Currently for all InnerWalls and
        GroundFloors this value is set to 0.0
    layer : list
        List of all layers of a building element (to be filled with Layer
        objects). Use element.layer = None to delete all layers of the building
        element
    other_side : ThermalZone()
        the thermal zone on the other side of the building element (only for
        interzonal elements)
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
            'outer_reversed': InterzonalWall treated as Wall,
                              InterzonalFloor treated as Rooftop,
                              InterzonalCeiling treated as GroundFloor, but with
                              reversed layers, resulting in the reversed
                              sequence of layers as for the complimentary
                              element declared as 'outer_ordered'
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
        """Constructor of Wall
        """
        self.other_side = other_side
        self.interzonal_type_material = None
        self.interzonal_type_export = None
        super(Wall, self).__init__(parent)

    def calc_equivalent_res(self, t_bt=7):
        """Equivalent resistance according to VDI 6007.

        Calculates the equivalent resistance and capacity of a wall according
        to VDI 6007 guideline. (Analogous model).

        Parameters
        ----------
        t_bt : int
            Time constant according to VDI 6007 (default t_bt = 7)
        """

        nr_of_layer, density, thermal_conduc, heat_capac, thickness = \
            self.gather_element_properties()

        if type(self).__name__.startswith("Interzonal") \
                and self.other_side is not None:
            if (not self.parent.use_conditions.with_heating and
                    self.other_side.use_conditions.with_heating):
                density = density[-1::-1]
                thermal_conduc = thermal_conduc[-1::-1]
                heat_capac = heat_capac[-1::-1]
                thickness = thickness[-1::-1]

        omega = 2 * np.pi / (86400 * t_bt)

        r_layer = thickness / thermal_conduc
        c_layer = heat_capac * density * thickness * 1000

        re11 = np.cosh(np.sqrt(0.5 * omega * r_layer * c_layer)) * \
            np.cos(np.sqrt(0.5 * omega * r_layer * c_layer))
        im11 = np.sinh(np.sqrt(0.5 * omega * r_layer * c_layer)) * \
            np.sin(np.sqrt(0.5 * omega * r_layer * c_layer))
        re12 = r_layer * np.sqrt(1 / (2 * omega * r_layer * c_layer)) * \
            (np.cosh(np.sqrt(0.5 * omega * r_layer * c_layer)) *
                np.sin(np.sqrt(0.5 * omega * r_layer * c_layer)) +
                np.sinh(np.sqrt(0.5 * omega * r_layer * c_layer)) *
                np.cos(np.sqrt(0.5 * omega * r_layer * c_layer)))
        im12 = r_layer * np.sqrt(1 / (2 * omega * r_layer * c_layer)) * \
            (np.cosh(np.sqrt(0.5 * omega * r_layer * c_layer)) *
                np.sin(np.sqrt(0.5 * omega * r_layer * c_layer)) -
                np.sinh(np.sqrt(0.5 * omega * r_layer * c_layer)) *
                np.cos(np.sqrt(0.5 * omega * r_layer * c_layer)))
        re21 = (-1 / r_layer) * (np.sqrt(0.5 * omega * r_layer * c_layer)) * \
            (np.cosh(np.sqrt(0.5 * omega * r_layer * c_layer)) *
                np.sin(np.sqrt(0.5 * omega * r_layer * c_layer)) -
                np.sinh(np.sqrt(0.5 * omega * r_layer * c_layer)) *
                np.cos(np.sqrt(0.5 * omega * r_layer * c_layer)))
        im21 = (1 / r_layer) * (np.sqrt(0.5 * omega * r_layer * c_layer)) * \
            (np.cosh(np.sqrt(0.5 * omega * r_layer * c_layer)) *
                np.sin(np.sqrt(0.5 * omega * r_layer * c_layer)) +
                np.sinh(np.sqrt(0.5 * omega * r_layer * c_layer)) *
                np.cos(np.sqrt(0.5 * omega * r_layer * c_layer)))
        re22 = re11
        im22 = im11

        # -----setting up the matrix for each layer
        a_layer = np.zeros((nr_of_layer, 4, 4))

        for i, r in enumerate(re11):
            a_layer[i][0][0] = r
            a_layer[i][0][1] = im11[i]
            a_layer[i][0][2] = re12[i]
            a_layer[i][0][3] = im12[i]
            a_layer[i][1][0] = -im11[i]
            a_layer[i][1][1] = re11[i]
            a_layer[i][1][2] = -im12[i]
            a_layer[i][1][3] = re12[i]
            a_layer[i][2][0] = re21[i]
            a_layer[i][2][1] = im21[i]
            a_layer[i][2][2] = re22[i]
            a_layer[i][2][3] = im22[i]
            a_layer[i][3][0] = -im21[i]
            a_layer[i][3][1] = re21[i]
            a_layer[i][3][2] = -im22[i]
            a_layer[i][3][3] = re22[i]

        # -----multiplication of the matrix
        new_mat = np.diag(np.ones(4))

        for count_layer in a_layer:
            new_mat = np.dot(new_mat, count_layer)

        # calculation of equivalent Resistance and capacities of each element
        self.r1 = (1 / self.area) * ((new_mat[3][3] - 1) *
                                     new_mat[0][2] + new_mat[2][3] *
                                     new_mat[0][3]) / \
                  ((new_mat[3][3] - 1) ** 2 + new_mat[2][3] ** 2)
        self.r2 = (1 / self.area) * ((new_mat[0][0] - 1) *
                                     new_mat[0][2] + new_mat[0][1] *
                                     new_mat[0][3]) / \
                  ((new_mat[0][0] - 1) ** 2 + new_mat[0][1] ** 2)
        self.c1 = self.area * ((new_mat[3][3] - 1) ** 2 +
                               (new_mat[2][3]) ** 2) / \
            (omega * (new_mat[0][2] * new_mat[2][3] -
                      (new_mat[3][3] - 1) * new_mat[0][3]))
        self.c2 = self.area * ((new_mat[0][0] - 1) ** 2 +
                               (new_mat[0][1]) ** 2) / (
            omega * (new_mat[0][2] *
                     new_mat[0][1] -
                     (new_mat[0][0] - 1) *
                     new_mat[0][3]))
        self.r3 = (1 / self.area) * (np.sum(r_layer)) - self.r1 - self.r2

        r_wall = self.r1 + self.r2 + self.r3

        # if type(self).__name__.startswith("Interzonal") \
        #         and self.other_side is not None:
        #     if (not self.parent.use_conditions.with_heating and
        #             self.other_side.use_conditions.with_heating):
        #         r_for_c1_korr = self.r2
        #     else:
        #         r_for_c1_korr = self.r1
        # else:
        #     r_for_c1_korr = self.r1
        r_for_c1_korr = self.r1

        self.c1_korr = (1 / (omega * r_for_c1_korr)) \
                       * ((r_wall * self.area
                           - new_mat[0][2] * new_mat[3][3]
                           - new_mat[0][3] * new_mat[2][3])
                          / (new_mat[3][3] * new_mat[0][3]
                             - new_mat[0][2] * new_mat[2][3]))

        if type(self).__name__ == "OuterWall" \
                or type(self).__name__ == "Rooftop" \
                or type(self).__name__ == "GroundFloor":
            self.c1 = self.c1_korr

    def insulate_wall(
            self,
            material=None,
            thickness=None,
            add_at_position=None,
            add_plaster_material=None,
            add_plaster_thickness=None):
        """Retrofit the walls with an additional insulation layer

        Adds an additional layer on the wall, outer sight

        Parameters
        ----------
        material : string
            Type of material, that is used for insulation, default = EPS035
        thickness : float
            thickness of the insulation layer, default = None
        add_at_position : int
            position at which to insert the insulation layer.
            0 inside, None (default) or -1 outside/other side
        add_plaster_material : int
            material of plaster to add, default = None. Is only applied if
            add_plaster_thickness is not None
            can only be applied if add_at_position is 0 or None
        add_plaster_thickness : float
            thickness of the plaster layer, default = None

        Returns
        -------
        insulation_index : int
            index of the insulation layer in the layer list

        """
        if material is None:
            material = "EPS035"
        else:
            pass

        if add_at_position == -1:
            add_at_position = None

        ext_layer = Layer(self, parent_position=add_at_position)
        new_material = Material(ext_layer)
        new_material.load_material_template(
            material,
            data_class=self.parent.parent.parent.data)

        if thickness is None:
            pass
        else:
            ext_layer.thickness = thickness

        ext_layer.material = new_material

        insulation_index = len(self.layer) - 1 if add_at_position is None \
            else add_at_position

        if add_plaster_thickness is not None:
            ass_error_1 = "If plaster is added, insulation must be applied at" \
                          " inside or outside"

            assert add_at_position is None or add_at_position == 0, ass_error_1
            if add_plaster_material is None:
                add_plaster_material = 'insulating_plaster'
            plaster_layer = Layer(self, parent_position=add_at_position)
            plaster_material = Material(plaster_layer)
            plaster_material.load_material_template(
                add_plaster_material,
                data_class=self.parent.parent.parent.data)
            plaster_layer.thickness = add_plaster_thickness
            if add_at_position == 0:
                insulation_index = 1

        return insulation_index

    def retrofit_wall(self, year_of_retrofit, material=None,
                      add_at_position=None):
        """Retrofits wall to German refurbishment standards.

        This function adds an additional layer of insulation and sets the
        thickness of the layer according to the retrofit standard in the
        year of refurbishment. Refurbishment year must be newer then 1977.
        Refurbishment layers are added on the unheated/outside of outer walls,
        rooftops, ground floors and interzonal elements between heated and
        unheated zones if not otherwise specified.

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
        self.set_calc_default()
        self.calc_ua_value()

        if material is None:
            material = "EPS_perimeter_insulation_top_layer"
        else:
            pass

        if year_of_retrofit < 1977:
            year_of_retrofit = 1977
            warnings.warn("You are using a year of retrofit not supported\
                    by teaser. We will change your year of retrofit to 1977\
                    for the calculation. Be careful!")

        if add_at_position is None:
            insulation_layer_index = -1  # default: outside
        else:
            insulation_layer_index = add_at_position

        use_u_value_standards_of = type(self).__name__
        if type(self).__name__.startswith("Interzonal") \
                and self.other_side is not None:
            if (self.parent.use_conditions.with_heating is
                    self.other_side.use_conditions.with_heating):
                use_u_value_standards_of = "InnerWall"
            elif (not self.parent.use_conditions.with_heating and
                  self.other_side.use_conditions.with_heating):
                if add_at_position is None:
                    insulation_layer_index = 0
                if (type(self)).__name__ == 'InterzonalWall':
                    use_u_value_standards_of = 'OuterWall'
                elif (type(self)).__name__ == 'InterzonalFloor':
                    use_u_value_standards_of = 'Rooftop'
                else:
                    use_u_value_standards_of = 'GroundFloor'
            else:
                if (type(self)).__name__ == 'InterzonalWall':
                    use_u_value_standards_of = 'OuterWall'
                elif (type(self)).__name__ == 'InterzonalFloor':
                    use_u_value_standards_of = 'GroundFloor'
                else:
                    use_u_value_standards_of = 'Rooftop'

        if use_u_value_standards_of == "InnerWall":
            calc_u = np.inf

        elif use_u_value_standards_of == 'OuterWall':

            if 1977 <= year_of_retrofit <= 1981:
                calc_u = 1.06 * self.area
            elif 1982 <= year_of_retrofit <= 1994:
                calc_u = 0.6 * self.area
            elif 1995 <= year_of_retrofit <= 2001:
                calc_u = 0.5 * self.area
            elif 2002 <= year_of_retrofit <= 2008:
                calc_u = 0.45 * self.area
            elif 2009 <= year_of_retrofit <= 2013:
                calc_u = 0.24 * self.area
            elif year_of_retrofit >= 2014:
                calc_u = 0.24 * self.area

        elif use_u_value_standards_of == 'Rooftop':

            if 1977 <= year_of_retrofit <= 1981:
                calc_u = 0.45 * self.area
            elif 1982 <= year_of_retrofit <= 1994:
                calc_u = 0.45 * self.area
            elif 1995 <= year_of_retrofit <= 2001:
                calc_u = 0.3 * self.area
            elif 2002 <= year_of_retrofit <= 2008:
                calc_u = 0.3 * self.area
            elif 2009 <= year_of_retrofit <= 2013:
                calc_u = 0.2 * self.area
            elif year_of_retrofit >= 2014:
                calc_u = 0.2 * self.area

        elif use_u_value_standards_of == 'GroundFloor':

            if 1977 <= year_of_retrofit <= 1981:
                calc_u = 0.8 * self.area
            elif 1982 <= year_of_retrofit <= 1994:
                calc_u = 0.7 * self.area
            elif 1995 <= year_of_retrofit <= 2001:
                calc_u = 0.5 * self.area
            elif 2002 <= year_of_retrofit <= 2008:
                calc_u = 0.4 * self.area
            elif 2009 <= year_of_retrofit <= 2013:
                calc_u = 0.3 * self.area
            elif year_of_retrofit >= 2014:
                calc_u = 0.3 * self.area

        else:
            calc_u = np.inf

        if self.ua_value > calc_u:
            self.insulate_wall(material, add_at_position=insulation_layer_index)

            r_conduc = 0

            for layer_index, count_layer in enumerate(self.layer):
                if layer_index == insulation_layer_index:
                    pass
                else:
                    r_conduc += (count_layer.thickness /
                                 count_layer.material.thermal_conduc)

            self.layer[insulation_layer_index].thickness = \
                (((
                  1 - calc_u * self.r_inner_comb - calc_u *
                  self.r_outer_comb) /
                  calc_u) * self.area - r_conduc) * \
                self.layer[insulation_layer_index].material.thermal_conduc

            self.layer[insulation_layer_index].id = len(self.layer)

    def _interzonal_type_standard_value(self, method):
        """return the standard value for the treatment of interzonal elements

        Refer to the documentation of project for details

        Parameters
        ----------
        method : str
            a valid value of project.method_interzonal_material_enrichment or
            project.method_interzonal_export

        Returns
        -------
        value : str
            'inner', 'outer_ordered', or 'outer_reversed'

        """
        this_use = self.parent.use_conditions
        other_use = self.other_side.use_conditions
        if method == 'heating_difference':
            if ((other_use.with_heating and this_use.with_heating)
                    or (not other_use.with_heating
                        and not this_use.with_heating)):
                value = 'inner'
            elif this_use.with_heating is True:
                value = 'outer_ordered'
            else:  # this_use.with_heating is False:
                value = 'outer_reversed'
        if (method == 'heating_cooling_difference'
                or method.startswith('setpoint_difference_')):
            # first decision: different heating conditions?
            if this_use.with_heating and not other_use.with_heating:
                value = 'outer_ordered'
            elif not this_use.with_heating and other_use.with_heating:
                value = 'outer_reversed'
            # second decision: different cooling conditions?
            elif this_use.with_cooling and not other_use.with_cooling:
                value = 'outer_ordered'
            elif not this_use.with_cooling and other_use.with_cooling:
                value = 'outer_reversed'
            elif not method.startswith('setpoint_difference_'):
                value = 'inner'
            else:
                # third decision: compare setpoints
                max_setpoint_diff = float(
                    method.lstrip('setpoint_difference_')
                )

                setpoint_diff_heating = np.subtract(
                    this_use.schedules["heating_profile"],
                    other_use.schedules["heating_profile"]
                )
                this_warmer = any(setpoint_diff_heating > max_setpoint_diff)
                other_warmer = any(setpoint_diff_heating < -max_setpoint_diff)

                setpoint_diff_cooling = np.subtract(
                    this_use.schedules["cooling_profile"],
                    other_use.schedules["cooling_profile"]
                )
                this_colder = any(setpoint_diff_cooling < -max_setpoint_diff)
                other_colder = any(setpoint_diff_cooling > max_setpoint_diff)

                if this_warmer and not other_warmer:
                    value = 'outer_ordered'
                elif other_warmer and not this_warmer:
                    value = 'outer_reversed'
                elif this_colder and not other_colder:
                    value = 'outer_ordered'
                elif other_colder and not this_colder:
                    value = 'outer_reversed'
                else:
                    value = 'inner'

        return value

    @property
    def other_side(self):
        return self._other_side

    @other_side.setter
    def other_side(self, value):
        if value is not None:
            ass_error_1 = "Other side has to be an instance of ThermalZone()"
            assert type(value).__name__ == "ThermalZone", ass_error_1
            ass_error_2 = "Other side can only be set for interzonal elements"
            assert type(self).__name__ in ("InterzonalWall", "InterzonalFloor",
                                           "InterzonalCeiling"), ass_error_2
            self._other_side = value
        else:
            self._other_side = None

    @property
    def interzonal_type_material(self):
        if self._interzonal_type_material is not None:
            return self._interzonal_type_material
        else:
            return self._interzonal_type_standard_value(
                method=self.parent.parent.parent.method_interzonal_material_enrichment
            )

    @interzonal_type_material.setter
    def interzonal_type_material(self, value):
        allowed_values = (None, 'inner', 'outer_ordered', 'outer_reversed')
        assert value in allowed_values
        self._interzonal_type_material = value

    @property
    def interzonal_type_export(self):
        if self._interzonal_type_export is not None:
            return self._interzonal_type_export
        else:
            return self._interzonal_type_standard_value(
                method=self.parent.parent.parent.method_interzonal_export
            )
        return value

    @interzonal_type_export.setter
    def interzonal_type_export(self, value):
        allowed_values = (None, 'inner', 'outer_ordered', 'outer_reversed')
        assert value in allowed_values
        self._interzonal_type_export = value
