'''
Created July 2015

@author: TEASER 4 Development Team

'''

from PyQt4.QtGui import QMessageBox
from teaser.Logic.BuildingObjects.ThermalZone import ThermalZone
from teaser.Logic.BuildingObjects.Building import Building
from teaser.Project import Project
from teaser.Logic.BuildingObjects.BuildingPhysics.OuterWall import OuterWall
from teaser.Logic.BuildingObjects.BuildingPhysics.InnerWall import InnerWall
from teaser.Logic.BuildingObjects.BuildingPhysics.Window import Window
from teaser.Logic.BuildingObjects.BuildingPhysics.Floor import Floor
from teaser.Logic.BuildingObjects.BuildingPhysics.Rooftop import Rooftop
from teaser.Logic.BuildingObjects.BuildingPhysics.Layer import Layer
from teaser.Logic.BuildingObjects.BuildingPhysics.Material import Material
from teaser.Logic.BuildingObjects.TypeBuildings.UseConditions18599\
    import UseConditions18599
import teaser.Data.TeaserXML as teaser_xml
import teaser.Data.CityGML as city_gml
import teaser.Logic.Utilis as utilis
from PyQt4.uic.Compiler.qtproxies import QtGui


class Controller():
    '''
    Controller class. Manages all interaction
    between the GUI, Logic and Data layers.
    '''

    def __init__(self):
        ''' '''

    @classmethod
    def click_add_new_layer(self, parent, id, thick, mat_nam, den, therm, heat,
                            solar, ir, trans):
        layer = Layer(parent)
        layer.id = id
        mat = Material(layer)
        mat.name = mat_nam
        mat.density = den
        mat.thermal_conduc = therm
        mat.heat_capac = heat
        mat.solar_absorp = solar
        mat.ir_emissivity = ir
        mat.transmittance = trans
        layer.thickness = thick
        return parent

    @classmethod
    def click_add_zone_button(self, parent, name, area, usage):
        '''
        creates a thermal zone with specified area and type and blawnco use
        conditions

        Parameters:
        ----------
        parent : Building()
            parent class of zone

        name : str
            individual name

        area : float
            area of the zone

        usage : string
            usage type of zone

        '''

        zone = ThermalZone(parent)
        usecon = UseConditions18599()
        usecon.usage = usage
        zone.name = name
        zone.area = area
        zone.use_conditions = usecon
        return parent

    @classmethod
    def click_add_new_element(self, parent, name, type, area):
        if type == "Outer Wall":
            element = OuterWall(parent)
            element.name = name
            element.area = area
        if type == "Inner Wall":
            element = InnerWall(parent)
            element.name = name
            element.area = area
        if type == "Window":
            element = Window(parent)
            element.name = name
            element.area = area
        if type == "GroundFloor":
            element = Floor(parent)
            element.name = name
            element.area = area
        if type == "Rooftop":
            element = Rooftop(parent)
            element.name = name
            element.area = area
        return parent

    @classmethod
    def click_add_new_building(self, current_project, openId):
        """
        Lets CalcProject create a new building with the given ID.
        """
        return Building(current_project, openId)

    @classmethod
    def clickBugreportManualButton(self):
        i = 0

    @classmethod
    def click_generate_type_building_button(
        self, parent, name, yearOfConstruction, numberOfFloors, heightOfFloors,
            typeOfBuilding, netLeasedArea, street, location,
            type_building_attributes):
        """
        Creates a new TypeBuilding. Needs all given attributes and uses the
        Classes CalcProject to create a building, CalcBuilding to fill it
        with Zones and the Data.Loader class to get the standard
        type-attributes and returns the building.
        """
        try:
            int(yearOfConstruction)
            int(numberOfFloors)
            float(heightOfFloors)
            float(netLeasedArea)
        except ValueError:
            QMessageBox.warning(self, u"Error!", u"Either the year of "
                                "construction, number of floors, height of "
                                "floors or net leased area are empty or do "
                                "not contain valid values")
        int_id = 0

        if typeOfBuilding == "Office":
            building = parent.type_bldg_office(
                name, int(yearOfConstruction), int(numberOfFloors),
                float(heightOfFloors), float(netLeasedArea),
                type_building_attributes['layoutArea'],
                type_building_attributes['layoutWindowArea'],
                type_building_attributes['constructionType'])
            
            building.street_name = street
            building.city = location
            int_id = building.internal_id
        
        if typeOfBuilding == "Insitute 4":
            building = parent.type_bldg_institute4(
                name, int(yearOfConstruction), int(numberOfFloors),
                float(heightOfFloors), float(netLeasedArea),
                type_building_attributes['layoutArea'],
                type_building_attributes['layoutWindowArea'],
                type_building_attributes['constructionType'])
            
            building.street_name = street
            building.city = location
            int_id = building.internal_id
            
        if typeOfBuilding == "Institute 8":
            building = parent.type_bldg_institute8(
                name, int(yearOfConstruction), int(numberOfFloors),
                float(heightOfFloors), float(netLeasedArea),
                type_building_attributes['layoutArea'],
                type_building_attributes['layoutWindowArea'],
                type_building_attributes['constructionType'])
            
            building.street_name = street
            building.city = location
            int_id = building.internal_id
            
        if typeOfBuilding == "Institute General":
            building = parent.type_bldg_institute(
                name, int(yearOfConstruction), int(numberOfFloors),
                float(heightOfFloors), float(netLeasedArea),
                type_building_attributes['layoutArea'],
                type_building_attributes['layoutWindowArea'],
                type_building_attributes['constructionType'])
            
            building.street_name = street
            building.city = location
            int_id = building.internal_id
            
        if typeOfBuilding == "Residential":
            building = parent.type_bldg_residential(
                name, int(yearOfConstruction), int(numberOfFloors),
                float(heightOfFloors), float(netLeasedArea),
                type_building_attributes['layoutArea'],
                type_building_attributes['neighbour_building'],
                type_building_attributes['layout_attic'],
                type_building_attributes['layout_cellar'],
                type_building_attributes['dormer'],
                type_building_attributes['constructionType'])
            
            building.street_name = street
            building.city = location
            int_id = building.internal_id

        return (parent, int_id)

    @classmethod
    def clickMatrixButton(self):
        i = 0

    @classmethod
    def click_save_button(self, project, path):
        if path.endswith("teaserXML"):
            teaser_xml.save_teaser_xml(path, project)
            print("Saved under: "+path)
        elif path.endswith("gml"):
            city_gml.save_gml(project, path)
            print("Saved under: "+path)

    @classmethod
    def click_load_button(self, path):
        """
        Returns a project loaded from XML.
        """
        loaded_prj = Project()
        if path.endswith(".xml"):
            loaded_prj.load_old_teaser(path)
        if path.endswith(".teaserXML"):
            loaded_prj.load_project(path)

        return loaded_prj

    @classmethod
    def get_materials_from_file(self, project):
        mat_list = []
        for mat in project.data.material_bind.Material:
            mat_list.append(mat)

        return mat_list

    @classmethod
    def clickConstructionYearCatagoryButton(self):
        i = 0
        
    @classmethod
    def switch_zone_type(self, zone_type, project, zone_id):
        for building in project.list_of_buildings:
            for zone in building.thermal_zones:
                if zone.internal_id == zone_id:
                    zone.use_conditions.load_use_conditions(zone_type)
                    break
        return project

    @classmethod
    def save_building_area(self, project, area, orientation):
        prj = project
        for building in prj.list_of_buildings:
            for zone in building.thermal_zones:
                for outerwall in zone.outer_walls:
                    if(outerwall.orientation == orientation):
                        building.set_outer_wall_area(area, orientation)
        return prj
