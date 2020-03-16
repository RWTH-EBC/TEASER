# created June 2015
# by TEASER4 Development Team


import random


class Layer(object):
    """Layer class

    This class holds information of a layer of a specific building element.

    Parameters
    ----------
    parent : BuildingElement
        The parent class of this object, the Building Element the layer
        belongs to. Allows for better control of hierarchical structures. If
        not None this adds the Layer to BuildingElement.layers.
        Default is None


    Attributes
    ----------
    id : int
        Position (starting from 0 and the inner side)
    material : Material()
        Material class of TEASER
    thickness : float [m]
        Thickness of the layer
    """

    def __init__(self, parent=None, id=0):
        """Constructor of Layer.


        """
        self.parent = parent
        self.internal_id = random.random()
        self.id = id
        self._material = None
        self._thickness = 0.0

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):

        if value is not None:

            ass_error_1 = "Parent has to be an instance of a BE"

            assert type(value).__name__ == "OuterWall" \
                or type(value).__name__ == "Rooftop" \
                or type(value).__name__ == "GroundFloor" \
                or type(value).__name__ == "InnerWall" \
                or type(value).__name__ == "Ceiling" \
                or type(value).__name__ == "Floor" \
                or type(value).__name__ == "Door" \
                or type(value).__name__ == "Window", ass_error_1

            self.__parent = value
            self.__parent.layer.append(self)

        else:
            self.__parent = None

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        ass_error_1 = "Material has to be an instance of Material()"

        assert type(value).__name__ == ("Material"), ass_error_1

        self._material = value

    @property
    def thickness(self):
        return self._thickness

    @thickness.setter
    def thickness(self, value):

        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert thickness to float")

        if value is not None:
            self._thickness = float(value)

        if self.material is not None and self.parent is not None:
            if vars(self.material)['_thermal_conduc'] != 0:
                self.parent.calc_ua_value()
