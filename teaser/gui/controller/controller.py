'''
Created July 2015

@author: TEASER 4 Development Team

'''
import inspect
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.boundaryconditions.boundaryconditions \
    import BoundaryConditions
from teaser.logic.buildingobjects.building import Building
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.project import Project
import teaser.data.output.teaserxml_output as teaser_xml
import teaser.data.output.citygml_output as city_gml
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor
import teaser.logic.utilities as utilitis


class Controller():
    '''
    Controller class. Manages all interaction
    between the GUI, Logic and Data layers.
    '''

    def __init__(self):
        ''' '''

    @classmethod
    def click_add_new_layer(self, parent, position, thick, name, den, therm,
                            heat, solar, ir, trans):
        '''Add a new Layer

        adds a new layer to the current element or envelope.
        If it is an element then return his parent, if not then return the
        layer.

        Parameters
        ----------

        parent : wall()
            The parent class of a layer this can be a ceiling,
            floor, groundfloor, innerwall, outerwall, rooftop or window.

        position : int
            Adds the layer at specified position.

        thick : float
            Thickness of the layer.

        name : string
            Name of material.

        den : float
            density of material.

        therm : float
            thermal_conduc of material.

        heat : float
            heat_capac of material.

        solar : float
            solar_absorp of material.

        ir : float
            ir_emissivity of material.

        trans : float
            transmittance of material.

        Returns
        ----------

        layer : layer()
        parent : wall()
            If the current element is an envelope then return a layer, but if
            the current element is a wall then return the parent
        '''

        layer = Layer()
        if parent is not None:
            parent.add_layer(layer, position=position)
        mat = Material(layer)
        mat.name = name
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
        parent : building()
            parent class of zone

        name : str
            individual name

        area : float
            area of the zone

        usage : string
            usage type of zone

        Returns
        ----------

        parent : Building()
            parent class of zone
        '''

        zone = ThermalZone(parent)
        zone.use_conditions = BoundaryConditions(zone)
        zone.use_conditions.load_use_conditions(zone_type)
        zone.name = name
        zone.area = area
        return parent

    @classmethod
    def click_add_new_element(self, parent, name, type, area):
        '''
        adds a new element to a zone with specified name, area and type.

        Parameters:
        ----------
        parent : wall()
            parent class of an element

        name : str
            individual name

        type : string
            type of element

        area : float
            area of the element

        Returns
        ----------

        parent : wall()
            parent class of element
        '''

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
    def click_update_building_button(self,
                                     project,
                                     current_building,
                                     name,
                                     year_of_construction,
                                     number_of_floors,
                                     height_of_floors,
                                     net_leased_area,
                                     street,
                                     location,
                                     update_archtertype):  
        for building in project.buildings:
            if building.internal_id == current_building.internal_id:
                building.net_leased_area = net_leased_area
                building.name = name
                building.street_name = street
                building.city = location
                building.year_of_construction = year_of_construction
                building.number_of_floors = number_of_floors
                building.height_of_floors = height_of_floors
                if update_archtertype == True:
                    building._thermal_zones = []
                    building.generate_archetype()
        return project
    
    @classmethod
    def click_update_building(self, project, index):
        """
        Updates all changed attributes of selected building
        """

        last_index = len(project.buildings) - 1
        updated_building = project.buildings[last_index]
        project.buildings.pop(last_index)
        project.buildings.pop(index)
        project.buildings.insert(index, updated_building)

        return project

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
        '''
        Creates a new TypeBuilding. Needs all given attributes and calls
        function in Project module.

        Parameters:
        ----------
        parent : project()
            parent class of a (type)building

        name : str
            individual name

        year_of_construction : float
            construction year of building

        number_of_floors : int
            number of floor in building

        height_of_floors : float
            height of floor in building

        type_of_building : (non)residential()
             building which can be a institute, institute4, institute8,
             office or singlefamilydwelling

        net_leased_area : float
            net leased area of the building

        street : str
            individual street name

        location : string
            individual location name

        type_building_attributes : string

        Returns
        ----------

        parent : project()
            parent class of building

        int_id : int
            internal id of building
        '''

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

        if type_of_building == "Institute 4":
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
    def click_save_button(self, project, path):
        '''
        Saves a project with a given path.

        Parameters:
        ----------
        project : project()
            root class

        path : str
            individual path where the xml file will be saved
        '''

        if path.endswith("teaserXML"):
            teaser_xml.save_teaser_xml(path, project)
            print("Saved under: "+path)
        elif path.endswith("gml"):
            city_gml.save_gml(project, path)
            print("Saved under: "+path)

    @classmethod
    def click_load_button(self, project, path):
        '''
        Returns a project loaded from XML.

        path : str
            individual path where the xml file will be loaded

        Returns
        ----------

        loaded_prj : project()
            project class filled with information from a file
        '''

        if path.endswith(".teaserXML"):
            project.load_project(path)
        elif path.endswith(".gml"):
            project.load_citygml(path)

        return project

    @classmethod
    def get_materials_from_file(self, project):
        '''
        Get a list with material from a file.

        project : project()
            root class

        Returns
        ----------

        mat_list : list
            list with filled material from a file
        '''

        mat_list = []
        for mat in project.data.material_bind.Material:
            mat_list.append(mat)

        return mat_list

    @classmethod
    def get_elements_from_file(self, project):
        '''
        Get a list with material from a file.

        project : project()
            root class

        Returns
        ----------

        wall_list : list
            list with filled wall elements from a file
        '''

        # project.buildings[0].thermal_zones
        # building = Building()
        # zone = ThermalZone(project.buildings[1])
        zone = ThermalZone()

        for outerwall in project.data.element_bind.OuterWall:
                wall = OuterWall()
                wall.name = "OuterWall"
                wall.construction_type = outerwall.construction_type
                wall.year_of_construction = \
                    outerwall.year_of_construction
                wall.building_age_group = outerwall.building_age_group
                wall.inner_convection = outerwall.inner_convection
                wall.inner_radiation = outerwall.inner_radiation
                wall.outer_convection = outerwall.outer_convection
                wall.outer_radiation = outerwall.outer_radiation
                for layerBind in outerwall.Layers.layer:
                    layer = Layer()
                    layer.id = layerBind.id - 1
                    layer.thickness = layerBind.thickness
                    material = Material(layer)
                    material.name = layerBind.Material.name
                    material.density = layerBind.Material.density
                    material.thermal_conduc = layerBind.Material.thermal_conduc
                    material.heat_capac = layerBind.Material.heat_capac
                    wall.add_layer(layer, layer.id)
                zone.add_element(wall)

        for innerwall in project.data.element_bind.InnerWall:
                wall = InnerWall()
                wall.name = "InnerWall"
                wall.construction_type = innerwall.construction_type
                wall.year_of_construction = \
                    innerwall.year_of_construction
                wall.building_age_group = innerwall.building_age_group
                wall.inner_convection = innerwall.inner_convection
                wall.inner_radiation = innerwall.inner_radiation
                for layerBind in innerwall.Layers.layer:
                    layer = Layer()
                    layer.id = layerBind.id - 1
                    layer.thickness = layerBind.thickness
                    material = Material(layer)
                    material.name = layerBind.Material.name
                    material.density = layerBind.Material.density
                    material.thermal_conduc = layerBind.Material.thermal_conduc
                    material.heat_capac = layerBind.Material.heat_capac
                    wall.add_layer(layer, layer.id)
                zone.add_element(wall)

        for rooftop in project.data.element_bind.Rooftop:
                wall = Rooftop()
                wall.name = "Rooftop"
                wall.construction_type = rooftop.construction_type
                wall.year_of_construction = \
                    rooftop.year_of_construction
                wall.building_age_group = rooftop.building_age_group
                wall.inner_convection = rooftop.inner_convection
                wall.inner_radiation = rooftop.inner_radiation
                wall.outer_convection = rooftop.outer_convection
                wall.outer_radiation = rooftop.outer_radiation
                for layerBind in rooftop.Layers.layer:
                    layer = Layer()
                    layer.id = layerBind.id - 1
                    layer.thickness = layerBind.thickness
                    material = Material(layer)
                    material.name = layerBind.Material.name
                    material.density = layerBind.Material.density
                    material.thermal_conduc = layerBind.Material.thermal_conduc
                    material.heat_capac = layerBind.Material.heat_capac
                    wall.add_layer(layer, layer.id)
                zone.add_element(wall)

        for groundfloor in project.data.element_bind.GroundFloor:
                wall = GroundFloor()
                wall.name = "GroundFloor"
                wall.construction_type = groundfloor.construction_type
                wall.year_of_construction = \
                    groundfloor.year_of_construction
                wall.building_age_group = groundfloor.building_age_group
                wall.inner_convection = groundfloor.inner_convection
                wall.inner_radiation = groundfloor.inner_radiation
                for layerBind in groundfloor.Layers.layer:
                    layer = Layer()
                    layer.id = layerBind.id - 1
                    layer.thickness = layerBind.thickness
                    material = Material(layer)
                    material.name = layerBind.Material.name
                    material.density = layerBind.Material.density
                    material.thermal_conduc = layerBind.Material.thermal_conduc
                    material.heat_capac = layerBind.Material.heat_capac
                    wall.add_layer(layer, layer.id)
                zone.add_element(wall)

        for window in project.data.element_bind.Window:
                wall = Window()
                wall.name = "Window"
                wall.construction_type = window.construction_type
                wall.year_of_construction = \
                    window.year_of_construction
                wall.building_age_group = window.building_age_group
                wall.inner_convection = window.inner_convection
                wall.inner_radiation = window.inner_radiation
                wall.outer_convection = window.outer_convection
                wall.outer_radiation = window.outer_radiation
                for layerBind in window.Layers.layer:
                    layer = Layer()
                    layer.id = layerBind.id - 1
                    layer.thickness = layerBind.thickness
                    material = Material(layer)
                    material.name = layerBind.Material.name
                    material.density = layerBind.Material.density
                    material.thermal_conduc = layerBind.Material.thermal_conduc
                    material.heat_capac = layerBind.Material.heat_capac
                    wall.add_layer(layer, layer.id)
                zone.add_element(wall)

        for ceiling in project.data.element_bind.Ceiling:
                wall = Ceiling()
                wall.name = "Ceiling"
                wall.construction_type = ceiling.construction_type
                wall.year_of_construction = \
                    ceiling.year_of_construction
                wall.building_age_group = ceiling.building_age_group
                wall.inner_convection = ceiling.inner_convection
                wall.inner_radiation = ceiling.inner_radiation
                for layerBind in ceiling.Layers.layer:
                    layer = Layer()
                    layer.id = layerBind.id - 1
                    layer.thickness = layerBind.thickness
                    material = Material(layer)
                    material.name = layerBind.Material.name
                    material.density = layerBind.Material.density
                    material.thermal_conduc = layerBind.Material.thermal_conduc
                    material.heat_capac = layerBind.Material.heat_capac
                    wall.add_layer(layer, layer.id)
                zone.add_element(wall)

        for floor in project.data.element_bind.Floor:
                wall = Floor()
                wall.name = "Floor"
                wall.construction_type = floor.construction_type
                wall.year_of_construction = \
                    floor.year_of_construction
                wall.building_age_group = floor.building_age_group
                wall.inner_convection = floor.inner_convection
                wall.inner_radiation = floor.inner_radiation
                for layerBind in floor.Layers.layer:
                    layer = Layer()
                    layer.id = layerBind.id - 1
                    layer.thickness = layerBind.thickness
                    material = Material(layer)
                    material.name = layerBind.Material.name
                    material.density = layerBind.Material.density
                    material.thermal_conduc = layerBind.Material.thermal_conduc
                    material.heat_capac = layerBind.Material.heat_capac
                    wall.add_layer(layer, layer.id)
                zone.add_element(wall)

        wall_list = []
        # print(inspect.getmembers(project.data.element_bind))
        print()
        for mat in project.data.element_bind.OuterWall:
            wall_list.append(mat)
        for mat in project.data.element_bind.InnerWall:
            wall_list.append(mat)
        for mat in project.data.element_bind.Rooftop:
            wall_list.append(mat)
        for mat in project.data.element_bind.GroundFloor:
            wall_list.append(mat)
        for mat in project.data.element_bind.Window:
            wall_list.append(mat)
        for mat in project.data.element_bind.Ceiling:
            wall_list.append(mat)
        for mat in project.data.element_bind.Floor:
            wall_list.append(mat)

        # return wall_list
        return zone

    @classmethod
    def switch_zone_type(self, zone_type, project, zone_id):
        '''
        Switch type of a selected zone, with its internal id.

        zone_type : string
            Type of a zone

        project : project()
            root class

        zone_id : int
            internal id of a zone

        Returns
        ----------

        project : project()
            current project with switched zone type of selected zone
        '''

        for building in project.buildings:
            for zone in building.thermal_zones:
                if zone.internal_id == zone_id:
                    zone.use_conditions.load_use_conditions(zone_type)
                    break
        return project

    @classmethod
    def click_export_button(self, project, building_model, zone_model, corG,
                            internal_id, path_output_folder):
        '''
        Execute an export with Aixlib model.

        project : project()
            root class

        building_model : string
            Model type of export (e.g. Multizone etc.)

        zone_model : string
            Zone type of export (e.g. Thermalzone etc.)

        corG : boolean
            boolean which enables or disables the corG

        internal_id : int
            internal id of (current)building. If the value is none then the
            export will executed for all buildings otherwise the export will
            executed for one building.

        path_output_folder : string
            path of the output location
        '''

        project.export_aixlib(building_model, zone_model, corG,
                              internal_id, path_output_folder)

    @classmethod
    def click_export_button_annex(self, project, num_of_elem, merge_win,
                                  internal_id, path_output_folder):
        '''
        Execute an export with Annex60 model.

        project : project()
            root class

        building_model : string
            Model type of export (e.g. Multizone etc.)

        zone_model : string
            Zone type of export (e.g. Thermalzone etc.)

        corG : boolean
            boolean which enables or disables the corG

        internal_id : int
            internal id of (current)building. If the value is none then the
            export will executed for all buildings otherwise the export will
            executed for one building.

        path_output_folder : string
            path of the output location
        '''

        project.calc_all_buildings(num_of_elem, merge_win, 'Annex60')
        project.export_annex(num_of_elem, merge_win, internal_id,
                             path_output_folder)

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
        '''
        Overwrites all values of selected envelope with inputs

        Parameters:
        ----------
        bldg : building()
            current building

        orientation : string
            orientation of selected envelope

        element_type : string
            shows the element type

        tilt : float
            tilt of the envelope (default: None)

        inner_convection : float
            inner convection of the envelope

        inner_radiation : flaot
            inner radiation of the envelope

        outer_convection : float
            outer convectionof the envelope

        outer_radiation : float
            outer radiation of the envelope

        layer_set : float
            area of the envelope
        '''

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
        '''
        Saves an envelope with specified attributes.

        Parameters:
        ----------
        bldg : building()
            current building

        orientation_old : string
            old orientation of selected envelope

        orientation_new : string
            new orientation of selected envelope

        element_type : string
            type which is needed to specify the element

        area : float
            area of the envelope
        '''

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
        '''
        Get the u value of current element

        current_element : wall()
            Current element this can be a ceiling, floor, groundfloor,
            innerwall, outerwall, rooftop or window.

        Returns
        ----------
        u_value : float
                returns the calculated u value
        '''

        u_value = float(current_element.ua_value)/current_element.area
        return u_value

    @classmethod
    def create_element(self, type_of_element, constr_type, building_age_group,
                       inner_con, outer_con, inner_rad, outer_rad, layer_set):

        if type_of_element == "Outer Wall":
            element = OuterWall()
            element.name = type
            element.construction_type = constr_type
            element.inner_convection = inner_con
            element.inner_radiation = inner_rad
            element.outer_convection = outer_con
            element.outer_radiation = outer_rad
            element.building_age_group = building_age_group
            element.add_layer_list(layer_set)

        elif type_of_element == "Inner Wall":
            element = InnerWall()
            element.name = type_of_element
            element.construction_type = constr_type
            element.inner_convection = inner_con
            element.inner_radiation = inner_rad
            element.outer_convection = outer_con
            element.outer_radiation = outer_rad
            element.building_age_group = building_age_group
            element.add_layer_list(layer_set)

        elif type_of_element == "Window":
            element = Window()
            element.name = type_of_element
            element.construction_type = constr_type
            element.inner_convection = inner_con
            element.inner_radiation = inner_rad
            element.outer_convection = outer_con
            element.outer_radiation = outer_rad
            element.building_age_group = building_age_group
            element.add_layer_list(layer_set)

        elif type_of_element == "GroundFloor":
            element = GroundFloor()
            element.name = type_of_element
            element.construction_type = constr_type
            element.inner_convection = inner_con
            element.inner_radiation = inner_rad
            element.outer_convection = outer_con
            element.outer_radiation = outer_rad
            element.building_age_group = building_age_group
            element.add_layer_list(layer_set)

        elif type_of_element == "Ceiling":
            element = Ceiling()
            element.name = type_of_element
            element.construction_type = constr_type
            element.inner_convection = inner_con
            element.inner_radiation = inner_rad
            element.outer_convection = outer_con
            element.outer_radiation = outer_rad
            element.building_age_group = building_age_group
            element.add_layer_list(layer_set)

        elif type_of_element == "Rooftop":
            element = Rooftop()
            element.name = type_of_element
            element.construction_type = constr_type
            element.inner_convection = inner_con
            element.inner_radiation = inner_rad
            element.outer_convection = outer_con
            element.outer_radiation = outer_rad
            element.building_age_group = building_age_group
            element.add_layer_list(layer_set)

        elif type_of_element == "Floor":
            element = Floor()
            element.name = type_of_element
            element.construction_type = constr_type
            element.inner_convection = inner_con
            element.inner_radiation = inner_rad
            element.outer_convection = outer_con
            element.outer_radiation = outer_rad
            element.building_age_group = building_age_group
            element.add_layer_list(layer_set)

        return element

    @classmethod
    def add_element_to_xml(self, element, path):
        prefix_path, suffix_path = utilitis.split_path(path)
        element.save_type_element(prefix_path, suffix_path)

    @classmethod
    def delete_element_in_xml(self, element, path):
        prefix_path, suffix_path = utilitis.split_path(path)
        element.delete_type_element(prefix_path, suffix_path)
