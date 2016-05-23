'''
Created July 2015

@author: TEASER 4 Development Team

'''

from teaser.Logic.BuildingObjects.ThermalZone import ThermalZone
from teaser.Logic.BuildingObjects.BoundaryConditions.BoundaryConditions \
    import UseConditions
from teaser.Logic.BuildingObjects.Building import Building
from teaser.Logic.BuildingObjects.BuildingPhysics.OuterWall import OuterWall
from teaser.Logic.BuildingObjects.BuildingPhysics.Floor import Floor
from teaser.Logic.BuildingObjects.BuildingPhysics.InnerWall import InnerWall
from teaser.Logic.BuildingObjects.BuildingPhysics.Layer import Layer
from teaser.Logic.BuildingObjects.BuildingPhysics.Material import Material
from teaser.Logic.BuildingObjects.BuildingPhysics.GroundFloor import GroundFloor
from teaser.Logic.BuildingObjects.BuildingPhysics.OuterWall import OuterWall
from teaser.Logic.BuildingObjects.BuildingPhysics.Rooftop import Rooftop
from teaser.Logic.BuildingObjects.BuildingPhysics.Window import Window
from teaser.project import Project
import teaser.data.output.teaserxml_output as teaser_xml
import teaser.data.output.citygML_output as city_gml
from teaser.Logic.BuildingObjects.BuildingPhysics.Ceiling import Ceiling
from teaser.Logic.BuildingObjects.BuildingPhysics.GroundFloor import GroundFloor


class Controller():
    '''
    Controller class. Manages all interaction
    between the GUI, Logic and Data layers.
    '''

    def __init__(self):
        ''' '''

    @classmethod
    def click_add_new_layer(self, parent, position, thick, mat_nam, den, therm,
                            heat, solar, ir, trans):
        layer = Layer()
        if parent is not None:
            parent.add_layer(layer, position=position)
        mat = Material(layer)
        mat.name = mat_nam
        mat.density = den
        mat.thermal_conduc = therm
        mat.heat_capac = heat
        mat.solar_absorp = solar
        mat.ir_emissivity = ir
        mat.transmittance = trans
        layer.thickness = thick
        if parent is None:
            return layer
        else:
            return parent

    @classmethod
    def click_add_zone_button(self, parent, name, area, zone_type):
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
        zone.use_conditions = UseConditions(zone)
        zone.use_conditions.load_use_conditions(zone_type)
        zone.name = name
        zone.area = area
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
            element = GroundFloor(parent)
            element.name = name
            element.area = area
        if type == "Ceiling":
            element = Ceiling(parent)
            element.name = name
            element.area = area
        if type == "Rooftop":
            element = Rooftop(parent)
            element.name = name
            element.area = area
        if type == "Floor":
            element = Floor(parent)
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
    def click_generate_type_building_button(self,
                                            parent,
                                            name,
                                            year_of_construction,
                                            number_of_floors,
                                            height_of_floors,
                                            type_of_building,
                                            net_leased_area,
                                            street,
                                            location,
                                            type_building_attributes):
        """
        Creates a new TypeBuilding. Needs all given attributes and calls
        function in Project module. Returns the building.
        """

        int_id = 0

        if type_of_building == "Office":

            building = parent.type_bldg_office(
                name=name,
                year_of_construction=year_of_construction,
                number_of_floors=number_of_floors,
                height_of_floors=height_of_floors,
                net_leased_area=net_leased_area,
                office_layout=type_building_attributes['layoutArea'],
                window_layout=type_building_attributes['layoutWindowArea'],
                construction_type=type_building_attributes['constructionType'])




            building.street_name = street
            building.city = location
            int_id = building.internal_id
        if type_of_building == "Insitute 4":
            building = parent.type_bldg_institute4(
                name=name,
                year_of_construction=year_of_construction,
                number_of_floors=number_of_floors,
                height_of_floors=height_of_floors,
                net_leased_area=net_leased_area,
                office_layout=type_building_attributes['layoutArea'],
                window_layout=type_building_attributes['layoutWindowArea'],
                construction_type=type_building_attributes['constructionType'])

            building.street_name = street
            building.city = location
            int_id = building.internal_id

        if type_of_building == "Institute 8":
            building = parent.type_bldg_institute8(
                name=name,
                year_of_construction=year_of_construction,
                number_of_floors=number_of_floors,
                height_of_floors=height_of_floors,
                net_leased_area=net_leased_area,
                office_layout=type_building_attributes['layoutArea'],
                window_layout=type_building_attributes['layoutWindowArea'],
                construction_type=type_building_attributes['constructionType'])

            building.street_name = street
            building.city = location
            int_id = building.internal_id

        if type_of_building == "Institute General":
            building = parent.type_bldg_institute(
                name=name,
                year_of_construction=year_of_construction,
                number_of_floors=number_of_floors,
                height_of_floors=height_of_floors,
                net_leased_area=net_leased_area,
                office_layout=type_building_attributes['layoutArea'],
                window_layout=type_building_attributes['layoutWindowArea'],
                construction_type=type_building_attributes['constructionType'])

            building.street_name = street
            building.city = location
            int_id = building.internal_id

        if type_of_building == "SingleFamilyDwelling":
            building = parent.type_bldg_residential(
                name=name,
                year_of_construction=year_of_construction,
                number_of_floors=number_of_floors,
                height_of_floors=height_of_floors,
                net_leased_area=net_leased_area,
                residential_layout=type_building_attributes['layoutArea'],
                neighbour_buildings=type_building_attributes[
                    'neighbour_building'],
                attic=type_building_attributes['layout_attic'],
                cellar=type_building_attributes['layout_cellar'],
                dormer=type_building_attributes['dormer'],
                construction_type=type_building_attributes['constructionType'])

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
        for building in project.buildings:
            for zone in building.thermal_zones:
                if zone.internal_id == zone_id:
                    zone.use_conditions.load_use_conditions(zone_type)
                    break
        return project

    @classmethod
    def click_export_button(self, project, building_model, zone_model, corG,
                            internal_id, path_output_folder):
               project.export_record(building_model, zone_model, corG,
                              internal_id, path_output_folder)

    @classmethod
    def click_change_all_constr(self,
                                bldg,
                                orientation,
                                element_type,
                                tilt,
                                inner_convection,
                                inner_radiation,
                                outer_convection,
                                outer_radiation,
                                layer_set):
        for zone in bldg.thermal_zones:
            for wall in zone.outer_walls:
                if element_type == "OuterWall" or element_type == "Rooftop":
                    if wall.orientation == orientation:
                        wall.tilt = tilt
                        wall.inner_convection = inner_convection
                        wall.inner_radiation = inner_radiation
                        wall.outer_convection = outer_convection
                        wall.outer_radiation = outer_radiation
                        wall.layer = None
                        for lay_count in layer_set:
                            wall.add_layer(lay_count, lay_count.position)

                else:
                    if wall.orientation == orientation:
                        wall.tilt = tilt
                        wall.inner_convection = inner_convection
                        wall.inner_radiation = inner_radiation
                        wall.layer = None
                        for lay_count in layer_set:
                            wall.add_layer(lay_count, lay_count.position)

            for win in zone.windows:
                if element_type == "Window":
                    if win.orientation == orientation:
                        win.tilt = tilt
                        win.inner_convection = inner_convection
                        win.inner_radiation = inner_radiation
                        win.outer_convection = outer_convection
                        win.outer_radiation = outer_radiation
                        win.layer = None
                        for lay_count in layer_set:
                            win.add_layer(lay_count, lay_count.position)

    @classmethod
    def click_save_envelopes(self, bldg, orientation_old,
                             orientation_new, element_type, area):

        if element_type == "Window":
            # new_window_area = bldg.get_window_area(orientation_new) + area
            for zone in bldg.thermal_zones:
                for win in zone.windows:
                    if element_type == "Window":
                        if win.orientation == orientation_old:
                            win.orientation = orientation_new
            # bldg.set_window_area(new_window_area, orientation_new)
        else:
            # new_outer_wall_area = bldg.get_outer_wall_area(orientation_new)
            # + area
            for zone in bldg.thermal_zones:
                for wall in zone.outer_walls:
                    if element_type == "Outer Wall":
                        if wall.orientation == orientation_old:
                            wall.orientation = orientation_new

                    elif element_type == "Rooftop":
                        if wall.orientation == orientation_old:
                            wall.orientation = orientation_new

                    elif element_type == "Ground Floor":
                        if wall.orientation == orientation_old:
                            wall.orientation = orientation_new
            # bldg.set_outer_wall_area(new_outer_wall_area, orientation_new)

    @classmethod
    def get_u_value(self, current_element):

        u_value = float(current_element.ua_value)/current_element.area
        return u_value
