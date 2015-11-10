#Created July 2015
#TEASER 4 Development Team


import teaser.Logic.Utilis as utilis 
import teaser.Data.SchemaBindings.TypeBuildingBind as tb_bind
import teaser.Data.SchemaBindings.UseConditions18599Bind as uc_bind
import teaser.Data.SchemaBindings.MaterialBind as mat_bind
import codecs

class DataClass(object):
    '''Class for XML data bindings
    
    This class loads all XML files with statistic or template data. It creates 
    the binding automatically. The binding needs the Python Package PyXB.
    
    Parameters
    ----------
    
    type_element_file : string    
        name of the XML file with the project specific type elements
        default: TypeBuildingElements.xml for general investigation
    
    Attributes
    ----------
    
    element_bind : instance of PyXB TypeBuilding elements
        PyXB instance of the TypeBuildingElements binding
    conditions_bind : instance of PyXB UseConditions
        PyXB instance of the UseConditions binding
    material_bind : instance of PyXB Material
        PyXB instance of the Material binding
    
    '''

    def __init__(self, type_element_file= None):
        '''Constructor of DataClass

        '''
        if type_element_file==None:
            self.path_tb = utilis.get_full_path("InputData/TypeBuildingElements.xml")
        else:
            self.path_tb = utilis.get_full_path("InputData/"+str(type_element_file))
           

        __xml_file_tb = open(self.path_tb,'r')
        self.element_bind = tb_bind.CreateFromDocument(__xml_file_tb.read())

        self.path_uc = utilis.get_full_path("InputData/UseConditions.xml")
        __xml_file_uc = open(self.path_uc,'r')
        self.conditions_bind = uc_bind.CreateFromDocument(__xml_file_uc.read())

        __path_mat = utilis.get_full_path("InputData/MaterialTemplates.xml")
        __xml_file_mat = codecs.open(__path_mat, 'r',  encoding='utf-8')
        self.material_bind = mat_bind.CreateFromDocument(__xml_file_mat.read())


