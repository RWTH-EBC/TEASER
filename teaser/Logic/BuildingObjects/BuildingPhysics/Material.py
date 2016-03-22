# created June 2015
# by TEASER4 Development Team


import teaser.Data.SchemaBindings.MaterialBind as mat_bind
import teaser.Logic.Utilis as utilis
import re


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
        self._name = ""
        self._density = 0.0
        self._thermal_conduc = 0.0
        self._heat_capac = 0.0
        self._solar_absorp = 0.0
        if type(self.parent.parent).__name__ != "Window":
            self._solar_absorp = 0.7
        self._ir_emissivity = 0.9
        self._transmittance = 0.0

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

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            regex = re.compile('[^a-zA-z0-9]')
            self._name = regex.sub('', value)
        else:
            try:
                value = str(value)
                regex = re.compile('[^a-zA-z0-9]')
                self._name = regex.sub('', value)
            except ValueError:
                print("Can't convert name to string")

    @property
    def thermal_conduc(self):
        return self._thermal_conduc

    @thermal_conduc.setter
    def thermal_conduc(self, value):
        
        if isinstance(value, float):
            pass
        elif value is None:
            pass
        else:
            try:
                value = float(value)
            except:
                raise ValueError("Can't convert thermal conduction to float")           
        
        if value is not None:
            self._thermal_conduc = float(value)
            if self.parent.thickness is not None and\
               self.parent.parent.inner_convection is not None and\
               self.parent.parent.inner_radiation is not None and\
               self.parent.parent.area is not None:
                self.parent.parent.calc_ua_value()

    @property
    def density(self):        
        return self._density

    @density.setter
    def density(self, value):

        if isinstance(value, float):
            self._density = value
        elif value is None:
            self._density = value
        else:
            try:
                value = float(value)
                self._density = value
            except:
                raise ValueError("Can't convert density to float")
    @property
    def heat_capac(self):        
        return self._heat_capac

    @heat_capac.setter
    def heat_capac(self, value):

        if isinstance(value, float):
            self._heat_capac = value
        elif value is None:
            self._heat_capac = value
        else:
            try:
                value = float(value)
                self._heat_capac = value
            except:
                raise ValueError("Can't convert heat capacity to float")

    @property
    def solar_absorp(self):        
        return self._solar_absorp

    @solar_absorp.setter
    def solar_absorp(self, value):

        if isinstance(value, float):
            self._solar_absorp = value
        elif value is None:
            self._solar_absorp = value
        else:
            try:
                value = float(value)
                self._solar_absorp = value
            except:
                raise ValueError("Can't convert solar absorption to float")
                
    @property
    def ir_emissivity(self):        
        return self._ir_emissivity

    @ir_emissivity.setter
    def ir_emissivity(self, value):

        if isinstance(value, float):
            self._ir_emissivity = value
        elif value is None:
            self._ir_emissivity = value
        else:
            try:
                value = float(value)
                self._ir_emissivity = value
            except:
                raise ValueError("Can't convert emissivity to float")
                
    @property
    def transmittance(self):        
        return self._transmittance

    @transmittance.setter
    def transmittance(self, value):

        if isinstance(value, float):
            self._transmittance = value
        elif value is None:
            self._transmittance = value
        else:
            try:
                value = float(value)
                self._transmittance = value
            except:
                raise ValueError("Can't convert transmittance to float")