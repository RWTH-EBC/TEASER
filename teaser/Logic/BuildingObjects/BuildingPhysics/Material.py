# created June 2015
# by TEASER4 Development Team


import teaser.Data.SchemaBindings.MaterialBind as mat_bind
import teaser.Logic.Utilis as utilis


class Material(object):
    '''This class represents a Material.


    Parameters
    ----------
    parent : Layer
        The parent class of this object, the layer the material
        belongs to. Allows for better control of hierarchical structures.
        Default is None


    Attributes
    ----------
    name : str
        Individual name

    density : float
        Density of material in kg/m^3

    thermal_conduc : float
        Thermal conductivity of material in W/(m*K)

    heat_capac : float
        Specific heat capacity of material in kJ/(kg*K)

    solar_absorp : float
        Coefficient of absorption of solar short wave

    ir_emissivity : float
        Coefficient of longwave emissivity of material

    transmittance : float
        Coefficient of transmittanve of material

    '''

    def __init__(self, parent=None):
        '''Constructor of Material.


        '''

        self.parent = parent
        self.name = ""
        self.density = 0.0
        self.thermal_conduc = 0.0
        self.heat_capac = 0.0
        self.solar_absorp = 0.0
        self.ir_emissivity = 0.0
        self.transmittance = 0.0

    def load_material_template(self, mat_name):
        '''Material loader.

        Loads Material specified in the XML.

        Parameters
        ----------

        mat_name : str
            Code list for Material

        '''
        ass_error_1 = "You need to specify parents up to project"

        assert self.parent.parent.parent.parent.parent is not None, ass_error_1

        for mat in self.parent.parent.parent.parent.parent.\
                data.material_bind.Material:

            if mat.name == mat_name:

                self.name = mat.name
                self.density = mat.density
                self.thermal_conduc = float(mat.thermal_conduc)
                self.heat_capac = mat.heat_capac

    def save_material_template(self):
        '''Material saver.

        Saves Material specified in the XML.

        '''

        mat_pyxb = mat_bind.MaterialType()
        mat_pyxb.name = self.name
        mat_pyxb.density = self.density
        mat_pyxb.thermal_conduc = self.thermal_conduc
        mat_pyxb.heat_capac = self.heat_capac

        path = utilis.get_full_path("InputData/MaterialTemplates.xml")
        xml_file = open(path, 'r')

        xml_parse = mat_bind.CreateFromDocument(xml_file.read())
        xml_parse.Material.append(mat_pyxb)
        out_file = open(path, 'w')

        out_file.write(xml_parse.toDOM().toprettyxml())

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, value):

        if value is not None:

            ass_error_1 = "Parent has to be an instance of a layer"

            assert type(value).__name__ == "Layer", ass_error_1

            self.__parent = value
            self.__parent.material = self
