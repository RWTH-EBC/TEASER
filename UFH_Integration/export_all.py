import math

from teaser.project import Project
from teaser.logic.buildingobjects.building import Building
from teaser.logic.buildingobjects.thermalzone import ThermalZone
from teaser.logic.buildingobjects.useconditions import UseConditions
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.logic.buildingobjects.buildingphysics.buildingelement import BuildingElement
from teaser.logic.simulation.modelicainfo import ModelicaInfo
from teaser.logic.buildingobjects.calculation.two_element import TwoElement
from teaser.logic.buildingobjects.buildingphysics.tabs import InnerTABS, OuterTABS


class ExportAll:

    def __init__(self):
        self.tz_instances = []
        self.ufh_instances = []

    def run(self):
        name = 'int_CC_UFH_comparison'
        prj = self.create_project(name)
        prj.modelica_info.stop_time = 604800
        bldg = self.create_building(prj, 'SimpleBuilding ' + name, 2015, 1, 20)
        # Zone 1
        tz = self.create_thermal_zone(bldg, "Bed room", "tz_1", 20, 3)
        self.create_instance(OuterWall, tz, 5, 0, bldg.year_of_construction, "light")
        self.create_instance(OuterWall, tz, 4, 90, bldg.year_of_construction, "light")
        self.create_instance(OuterWall, tz, 5, 180, bldg.year_of_construction, "light")
        self.create_instance(OuterWall, tz, 4, 270, bldg.year_of_construction, "light")
        self.create_instance(Floor, tz, 20, -1, bldg.year_of_construction, "light")
        self.create_instance(Window, tz, 0.001, 0, bldg.year_of_construction, "EnEv")
        # Tabs Representation
        # self.create_instance(Floor, tz, 20, -1, bldg.year_of_construction, "heavy")
        self.create_instance(GroundFloor, tz, 20, -2, bldg.year_of_construction, "heavy")
        tz.calc_zone_parameters()

        # Zone 2
        tz2 = self.create_thermal_zone(bldg, "Bed room", "tz_2", 20, 3)
        self.create_instance(OuterWall, tz2, 5, 0, bldg.year_of_construction, "light")
        self.create_instance(OuterWall, tz2, 4, 90, bldg.year_of_construction, "light")
        self.create_instance(OuterWall, tz2, 5, 180, bldg.year_of_construction, "light")
        self.create_instance(OuterWall, tz2, 4, 270, bldg.year_of_construction, "light")
        self.create_instance(Floor, tz2, 20, -1, bldg.year_of_construction, "light")
        self.create_instance(Window, tz2, 0.001, 0, bldg.year_of_construction, "EnEv")
        # Tabs Representation
        # self.create_instance(InnerTABS, tz2, 20, -1, bldg.year_of_construction, "heavy_CC")
        self.create_instance(OuterTABS, tz2, 20, -2, bldg.year_of_construction, "heavy_CC")
        tz2.calc_zone_parameters()

        bldg.calc_building_parameter()
        prj.export_aixlib(path='D:/dja-dco/Dymola_Exports')
        pass

    @staticmethod
    def create_project(name):
        prj = Project(load_data=True)
        prj.name = name
        prj.data.load_uc_binding()
        prj.number_of_elements_calc = 2
        return prj

    @staticmethod
    def create_building(project, name, year_of_construction, n_floors, net_area):
        bldg = Building(parent=project)
        bldg.used_library_calc = 'AixLib'
        bldg.name = name
        bldg.year_of_construction = year_of_construction
        bldg.number_of_floors = n_floors
        bldg.net_leased_area = net_area
        return bldg

    @staticmethod
    def create_thermal_zone(bldg, use_condition, name, area, height):
        tz = ThermalZone(parent=bldg)
        tz.use_conditions = UseConditions(parent=tz)
        tz.use_conditions.load_use_conditions(use_condition)
        tz.use_conditions.with_heating = False
        tz.name = name
        tz.area = area
        tz.volume = area * height
        tz.number_of_elements = 2
        return tz

    def create_instance(self, class_instance, tz, area, orientation, year_of_construction, construction):
        inst = class_instance(parent=tz)
        inst.load_type_element(year_of_construction, construction)
        inst.area = area
        inst.orientation = orientation
        self.tz_instances.append(inst)

    @classmethod
    def calc_ufh_slab(cls, slabs: list, t_bt: float = 5):
        external_classes = (GroundFloor, Rooftop)
        ufh_parameters = {}
        omega = 2 * math.pi / 86400 / t_bt
        for element in slabs:
            e_type = type(element).__name__
            if e_type not in ufh_parameters:
                ufh_parameters[e_type] = {'instances': [], 'area': 0.0,
                                          'is_external': True if type(element) in external_classes else False}
            ufh_parameters[e_type]['instances'].append(element)
            ufh_parameters[e_type]['area'] += element.area

        for e_type in ufh_parameters:
            r1 = 0.0
            c1 = 0.0
            slabs = ufh_parameters[e_type]['instances']
            area = ufh_parameters[e_type]['area']
            r_conv_inner = 1 / sum(1 / element.r_inner_conv for element in slabs)
            alpha_conv_inner = 1 / (r_conv_inner * area)
            if len(slabs) > 0:
                if len(slabs) == 1:
                    # only one outer wall, no need to calculate chain matrix
                    r1 = slabs[0].r1
                    c1 = slabs[0].c1_korr
                else:
                    # more than one outer wall, calculate chain matrix
                    r1, c1 = cls._calc_parallel_connection(slabs, omega)
                if ufh_parameters[e_type]['is_external']:
                    conduction = 1 / sum(
                        (1 / element.r_conduc) for element in slabs
                    )
                    r_rest = conduction - r1
                    ufh_parameters[e_type]['r_rest'] = r_rest
            ufh_parameters[e_type]['r1'] = r1
            ufh_parameters[e_type]['c1'] = c1
            ufh_parameters[e_type]['alpha_conv_inner'] = alpha_conv_inner

        return ufh_parameters

    @staticmethod
    def _calc_parallel_connection(element_list: list, omega):
        """Parallel connection of walls according to VDI 6007

        Calculates the parallel connection of wall elements according to VDI
        6007, resulting in R1 and C1 (equation 23, 24).

        Parameters
        ----------
        element_list : list
            List of inner or outer walls
        omega : float
            VDI 6007 frequency

        Returns
        ----------
        r1 : float [K/W]
            VDI 6007 resistance for all inner or outer walls
        c1 : float [K/W]
            VDI 6007 capacity all for inner or outer walls
        """

        for wall_count in range(len(element_list) - 1):

            if wall_count == 0:

                r1 = (
                             element_list[wall_count].r1 * element_list[wall_count].c1 ** 2
                             + element_list[wall_count + 1].r1
                             * element_list[wall_count + 1].c1 ** 2
                             + omega ** 2
                             * element_list[wall_count].r1
                             * element_list[wall_count + 1].r1
                             * (element_list[wall_count].r1 + element_list[wall_count + 1].r1)
                             * element_list[wall_count].c1 ** 2
                             * element_list[wall_count + 1].c1 ** 2
                     ) / (
                             (element_list[wall_count].c1 + element_list[wall_count + 1].c1) ** 2
                             + omega ** 2
                             * (element_list[wall_count].r1 + element_list[wall_count + 1].r1)
                             ** 2
                             * element_list[wall_count].c1 ** 2
                             * element_list[wall_count + 1].c1 ** 2
                     )

                c1 = (
                             (element_list[wall_count].c1 + element_list[wall_count + 1].c1) ** 2
                             + omega ** 2
                             * (element_list[wall_count].r1 + element_list[wall_count + 1].r1)
                             ** 2
                             * element_list[wall_count].c1 ** 2
                             * element_list[wall_count + 1].c1 ** 2
                     ) / (
                             element_list[wall_count].c1
                             + element_list[wall_count + 1].c1
                             + omega ** 2
                             * (
                                     element_list[wall_count].r1 ** 2 * element_list[wall_count].c1
                                     + element_list[wall_count + 1].r1 ** 2
                                     * element_list[wall_count + 1].c1
                             )
                             * element_list[wall_count].c1
                             * element_list[wall_count + 1].c1
                     )
            else:
                r1x = r1
                c1x = c1
                r1 = (
                             r1x * c1x ** 2
                             + element_list[wall_count + 1].r1
                             * element_list[wall_count + 1].c1 ** 2
                             + omega ** 2
                             * r1x
                             * element_list[wall_count + 1].r1
                             * (r1x + element_list[wall_count + 1].r1)
                             * c1x ** 2
                             * element_list[wall_count + 1].c1 ** 2
                     ) / (
                             (c1x + element_list[wall_count + 1].c1) ** 2
                             + omega ** 2
                             * (r1x + element_list[wall_count + 1].r1) ** 2
                             * c1x ** 2
                             * element_list[wall_count + 1].c1 ** 2
                     )

                c1 = (
                             (c1x + element_list[wall_count + 1].c1) ** 2
                             + omega ** 2
                             * (r1x + element_list[wall_count + 1].r1) ** 2
                             * c1x ** 2
                             * element_list[wall_count + 1].c1 ** 2
                     ) / (
                             c1x
                             + element_list[wall_count + 1].c1
                             + omega ** 2
                             * (
                                     r1x ** 2 * c1x
                                     + element_list[wall_count + 1].r1 ** 2
                                     * element_list[wall_count + 1].c1
                             )
                             * c1x
                             * element_list[wall_count + 1].c1
                     )
        return r1, c1


if __name__ == "__main__":
    export = ExportAll()
    export.run()
