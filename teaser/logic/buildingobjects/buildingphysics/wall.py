# created June 2015
# by TEASER4 Development Team


from teaser.logic.buildingobjects.buildingphysics.buildingelement \
    import BuildingElement
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
import numpy as np


class Wall(BuildingElement):
    """This class represents a wall and is a child of BuildingElement().
    """

    def __init__(self, parent=None):
        """
        """
        super(Wall, self).__init__(parent)

    def calc_equivalent_res(self, t_bt=7):
        """Equivalent resistance VDI 6007.

        Calculates the equivalent resistance of a wall according to
        VDI 6007 guideline.

        Parameters
        ----------
        t_bt : int
            Time constant according to VDI 6007 (default t_bt = 7)
        """

        nr_of_layer, density, thermal_conduc, heat_capac, thickness = \
            self.gather_element_properties()

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

        # print(self.parent.parent.name)
        # -calculation of equivalent Resistance and capacities of each element
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

        self.c1_korr = (1 / (omega * self.r1)) * ((r_wall * self.area -
                                                   new_mat[0][2] * new_mat[3][
                                                       3] -
                                                   new_mat[0][3] * new_mat[2][
                                                       3]) /
                                                  (new_mat[3][3] * new_mat[0][
                                                      3] -
                                                   new_mat[0][2] * new_mat[2][
                                                       3]))

        if type(self).__name__ == "OuterWall" \
                or type(self).__name__ == "Rooftop" \
                or type(self).__name__ == "GroundFloor":
            self.c1 = self.c1_korr

    def insulate_wall(self,
                      material=None,
                      thickness=None):
        """Retrofit the walls with an additional insulation layer

        Adds an additional layer on the wall, outer sight

        Parameters
        ----------
        material : string
            Type of material, that is used for insulation, default = EPS035

        thickness : float
            thickness of the insulation layer, default = None

        """
        if material is None:
            material = "EPS035"
        else:
            pass

        ext_layer = Layer(self)
        new_material = Material(ext_layer)
        new_material.load_material_template(material,
                                            data_class=self.parent.parent.parent.data)

        if thickness is None:
            pass
        else:
            ext_layer.thickness = thickness

        ext_layer.material = new_material

    def retrofit_wall(self, year_of_retrofit, material=None):
        """This function adds an additional layer of insulation and sets the
        thickness of the layer according to the retrofit standard in the
        year of refurbishment. Refurbishment year must be newer then 1995

        Note: To Calculate thickness and U-Value, the standard TEASER
        coefficients for outer and inner heat transfer are used.

        Parameters
        ----------
        material : string
            Type of material, that is used for insulation

        year_of_refurbishment : int
            Year of the retrofit of the wall/building

        """
        self.set_calc_default()
        self.calc_ua_value()

        if material is None:
            material = "EPS035"
        else:
            pass

        if type(self).__name__ == 'OuterWall':

            if 1995 <= year_of_retrofit <= 2001:
                self.insulate_wall(material)
                calc_u = 0.5 * self.area
            if 2002 <= year_of_retrofit <= 2008:
                self.insulate_wall(material)
                calc_u = 0.45 * self.area
            if 2009 <= year_of_retrofit <= 2013:
                self.insulate_wall(material)
                calc_u = 0.24 * self.area
            if year_of_retrofit >= 2014:
                self.insulate_wall(material)
                calc_u = 0.24 * self.area

        elif type(self).__name__ == 'Rooftop':

            if 1995 <= year_of_retrofit <= 2001:
                self.insulate_wall(material)
                calc_u = 0.3 * self.area
            if 2002 <= year_of_retrofit <= 2008:
                self.insulate_wall(material)
                calc_u = 0.3 * self.area
            if 2009 <= year_of_retrofit <= 2013:
                self.insulate_wall(material)
                calc_u = 0.2 * self.area
            if year_of_retrofit >= 2014:
                self.insulate_wall(material)
                calc_u = 0.2 * self.area

        if type(self).__name__ == 'GroundFloor':

            if 1995 <= year_of_retrofit <= 2001:
                self.insulate_wall(material)
                calc_u = 0.5 * self.area
            if 2002 <= year_of_retrofit <= 2008:
                self.insulate_wall(material)
                calc_u = 0.4 * self.area
            if 2009 <= year_of_retrofit <= 2013:
                self.insulate_wall(material)
                calc_u = 0.3 * self.area
            if year_of_retrofit >= 2014:
                self.insulate_wall(material)
                calc_u = 0.3 * self.area

        r_conduc = 0

        if self.ua_value < calc_u:
            pass
        else:
            for count_layer in self.layer[:-1]:
                r_conduc += (count_layer.thickness /
                             count_layer.material.thermal_conduc)

                self.layer[-1].thickness = \
                    (((
                      1 - calc_u * self.r_inner_comb - calc_u *
                      self.r_outer_comb) /
                      calc_u) * self.area - r_conduc) * \
                    self.layer[-1].material.thermal_conduc

                self.layer[-1].id = len(self.layer)
