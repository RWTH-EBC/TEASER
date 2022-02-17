import math
import os

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
from teaser.logic.archetypebuildings.bmvbs.office import Office
from teaser.logic.archetypebuildings.bmvbs.singlefamilydwelling import SingleFamilyDwelling


class ExportAll:
    tz_instances = []
    ufh_instances = []

    def run(self):
        name = 'testtabs_new_WT'
        prj = self.create_project(name)
        prj.modelica_info.stop_time = 604800
        bldg = self.create_building(prj, 'SimpleBuilding ' + name, 2015, 1, 20)
        # Zone 1

        tz = self.create_thermal_zone(bldg, "Bed room", "tz_3", 20, 3, RoomTypes['TypeL'])
        self.create_instance(Window, tz, 5.13, 180, 2014, "Alu- oder Stahlfenster, Waermeschutzverglasung, zweifach")
        self.create_instance(OuterTABS, tz, 10, -2, bldg.year_of_construction, "up_half_light",
                             TABSTypes['Internal']['UpHalf']['Laminate'])
        self.create_instance(InnerTABS, tz, 10, -1, bldg.year_of_construction, "up_half_light")

        # self.create_instance(OuterTABS, tz, 20, -2, bldg.year_of_construction, "up_half_light",
        #                      TABSTypes['Internal']['LoHalf'])
        tz.calc_zone_parameters()

        bldg.calc_building_parameter()
        prj.export_aixlib(path='D:/dja-dco/Dymola_Exports')
        pass

    @staticmethod
    def replaceTABS(building, cc=False):
        for tz in building.thermal_zones:
            areas_floor = [fa.area for fa in tz.floors]
            areas_gfloor = [gfa.area for gfa in tz.ground_floors]
            selected = 'ground_floors' if sum(areas_gfloor) > sum(areas_floor) else 'floors'
            class_tabs = InnerTABS if selected == 'floors' else OuterTABS
            for floor in getattr(tz, selected):
                ufh = class_tabs(parent=tz)
                ufh.area = floor.area
                ufh.inner_convection = floor.inner_convection
                ufh.inner_radiation = floor.inner_radiation
                ufh.outer_convection = floor.outer_convection
                ufh.outer_radiation = floor.outer_radiation
                if cc:
                    new_layers = floor.layer
                else:
                    new_layers = floor.layer[:-1]
                for layer in new_layers:
                    ufh_layer = Layer(parent=ufh)
                    ufh_layer.thickness = layer.thickness
                    material = Material(parent=ufh_layer)
                    material.load_material_template(layer.material.name)
            if selected == 'ground_floors':
                tz.ground_floors.clear()
            else:
                tz.floors.clear()
            tz.calc_zone_parameters()

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

    @classmethod
    def create_thermal_zone(cls, bldg, use_condition, name, area, height, template=None):
        tz = ThermalZone(parent=bldg)
        tz.use_conditions = UseConditions(parent=tz)
        tz.use_conditions.load_use_conditions(use_condition)
        tz.use_conditions.with_heating = False
        tz.name = name
        tz.area = area
        tz.volume = area * height
        tz.number_of_elements = 2

        if template:
            for instance, properties in template.items():
                instance_class = instance_switcher.get(instance)
                inst = instance_class(parent=tz)
                inst.area = properties['area']
                inst.orientation = properties['orientation']
                for layer_props in properties['layers'].values():
                    layer = Layer(parent=inst)
                    layer.thickness = layer_props['thickness']
                    material = Material(parent=layer)
                    for attr, value in layer_props.items():
                        if attr != 'thickness':
                            setattr(material, attr, value)
        return tz

    @classmethod
    def create_instance(cls, class_instance, tz, area, orientation, year_of_construction, construction,
                        create_layers=None):
        inst = class_instance(parent=tz)
        if not create_layers:
            inst.load_type_element(year_of_construction, construction)
        else:
            for layer_number, items in create_layers.items():
                layer = Layer(parent=inst)
                layer.thickness = items['thickness']
                material = Material(parent=layer)
                for attr, value in items.items():
                    if attr != 'thickness':
                        setattr(material, attr, value)
        inst.area = area
        inst.orientation = orientation
        cls.tz_instances.append(inst)
        return inst


RoomTypes = {
    'TypeL': {
        'Floor': {
            'area': 18.75,
            'orientation': -2,
            'layers': {
                1: {
                    'thickness': 0.004,
                    'thermal_conduc': 0.17,
                    'density': 1200,
                    'heat_capac': 1.4
                },
                2: {
                    'thickness': 0.04,
                    'thermal_conduc': 1.4,
                    'density': 1000,
                    'heat_capac': 2
                },
                3: {
                    'thickness': 0.08,
                    'thermal_conduc': 0.434,
                    'density': 1.2,
                    'heat_capac': 1
                },
                4: {
                    'thickness': 0.14,
                    'thermal_conduc': 2.5,
                    'density': 2400,
                    'heat_capac': 1
                },
                5: {
                    'thickness': 0.3,
                    'thermal_conduc': 1.627,
                    'density': 1.2,
                    'heat_capac': 1
                },
                6: {
                    'thickness': 0.02,
                    'thermal_conduc': 0.04,
                    'density': 75,
                    'heat_capac': 1.03
                },
                7: {
                    'thickness': 0.001,
                    'thermal_conduc': 50,
                    'density': 7800,
                    'heat_capac': 0.45
                }
            }
        },
        'Rooftop': {
            'area': 19.15,
            'orientation': -1,
            'layers': {
                1: {
                    'thickness': 0.001,
                    'thermal_conduc': 50,
                    'density': 7800,
                    'heat_capac': 0.45
                },
                2: {
                    'thickness': 0.02,
                    'thermal_conduc': 0.04,
                    'density': 75,
                    'heat_capac': 1.03
                },
                3: {
                    'thickness': 0.255,
                    'thermal_conduc': 1.627,
                    'density': 1.2,
                    'heat_capac': 1
                },
                4: {
                    'thickness': 0.14,
                    'thermal_conduc': 2.5,
                    'density': 2400,
                    'heat_capac': 1
                },
                5: {
                    'thickness': 0.095,
                    'thermal_conduc': 0.04,
                    'density': 105,
                    'heat_capac': 1
                },
                6: {
                    'thickness': 0.005,
                    'thermal_conduc': 0.23,
                    'density': 1100,
                    'heat_capac': 1
                },
                7: {
                    'thickness': 0.2,
                    'thermal_conduc': 0.7,
                    'density': 1638,
                    'heat_capac': 1
                }
            }
        },
        'InnerWall': {
            'area': 36.51,
            'orientation': 0,
            'layers': {
                1: {
                    'thickness': 0.023,
                    'thermal_conduc': 0.25,
                    'density': 900,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.06,
                    'thermal_conduc': 0.06,
                    'density': 100,
                    'heat_capac': 1.03
                },
                3: {
                    'thickness': 0.035,
                    'thermal_conduc': 0.19,
                    'density': 1.2,
                    'heat_capac': 1
                },
                4: {
                    'thickness': 0.023,
                    'thermal_conduc': 0.25,
                    'density': 900,
                    'heat_capac': 1
                }
            }
        },
        'InnerDoor': {
            'area': 2,
            'orientation': 0,
            'layers': {
                1: {
                    'thickness': 0.025,
                    'thermal_conduc': 0.13,
                    'density': 500,
                    'heat_capac': 1.6
                }
            }
        },
        'OuterWall': {
            'area': 7.39,
            'orientation': 180,
            'layers': {
                1: {
                    'thickness': 0.08,
                    'thermal_conduc': 1.35,
                    'density': 2000,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.08,
                    'thermal_conduc': 0.035,
                    'density': 10,
                    'heat_capac': 1.03
                },
                3: {
                    'thickness': 0.03,
                    'thermal_conduc': 0.163,
                    'density': 1.2,
                    'heat_capac': 1
                },
                4: {
                    'thickness': 0.012,
                    'thermal_conduc': 0.6,
                    'density': 1650,
                    'heat_capac': 1
                }
            }
        }
    },
    'TypeM': {
        'Floor': {
            'area': 18.75,
            'orientation': -2,
            'layers': {
                1: {
                    'thickness': 0.004,
                    'thermal_conduc': 0.17,
                    'density': 1200,
                    'heat_capac': 1.4
                },
                2: {
                    'thickness': 0.04,
                    'thermal_conduc': 1.4,
                    'density': 1000,
                    'heat_capac': 2
                },
                3: {
                    'thickness': 0.08,
                    'thermal_conduc': 0.434,
                    'density': 1.2,
                    'heat_capac': 1
                },
                4: {
                    'thickness': 0.2,
                    'thermal_conduc': 2.3,
                    'density': 2300,
                    'heat_capac': 1
                },
                5: {
                    'thickness': 0.255,
                    'thermal_conduc': 1.627,
                    'density': 1.2,
                    'heat_capac': 1
                },
                6: {
                    'thickness': 0.02,
                    'thermal_conduc': 0.04,
                    'density': 75,
                    'heat_capac': 1.03
                },
                7: {
                    'thickness': 0.001,
                    'thermal_conduc': 50,
                    'density': 7800,
                    'heat_capac': 0.45
                }
            }
        },
        'Rooftop': {
            'area': 19.5,
            'orientation': -1,
            'layers': {
                1: {
                    'thickness': 0.001,
                    'thermal_conduc': 50,
                    'density': 7800,
                    'heat_capac': 0.45
                },
                2: {
                    'thickness': 0.02,
                    'thermal_conduc': 0.04,
                    'density': 75,
                    'heat_capac': 1.03
                },
                3: {
                    'thickness': 0.255,
                    'thermal_conduc': 1.627,
                    'density': 1.2,
                    'heat_capac': 1
                },
                4: {
                    'thickness': 0.2,
                    'thermal_conduc': 2.3,
                    'density': 2300,
                    'heat_capac': 1
                },
                5: {
                    'thickness': 0.095,
                    'thermal_conduc': 0.04,
                    'density': 105,
                    'heat_capac': 1
                },
                6: {
                    'thickness': 0.005,
                    'thermal_conduc': 0.23,
                    'density': 1100,
                    'heat_capac': 1
                },
                7: {
                    'thickness': 0.2,
                    'thermal_conduc': 0.7,
                    'density': 1638,
                    'heat_capac': 1
                }
            }
        },
        'InnerWall': {
            'area': 36.51,
            'orientation': 0,
            'layers': {
                1: {
                    'thickness': 0.015,
                    'thermal_conduc': 0.57,
                    'density': 1300,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.115,
                    'thermal_conduc': 0.58,
                    'density': 1400,
                    'heat_capac': 1
                },
                3: {
                    'thickness': 0.015,
                    'thermal_conduc': 0.57,
                    'density': 1300,
                    'heat_capac': 1
                }
            }
        },
        'InnerDoor': {
            'area': 2,
            'orientation': 0,
            'layers': {
                1: {
                    'thickness': 0.025,
                    'thermal_conduc': 0.2,
                    'density': 800,
                    'heat_capac': 1.6
                }
            }
        },
        'OuterWall': {
            'area': 8.13,
            'orientation': 180,
            'layers': {
                1: {
                    'thickness': 0.08,
                    'thermal_conduc': 1.65,
                    'density': 2200,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.08,
                    'thermal_conduc': 0.035,
                    'density': 10,
                    'heat_capac': 1.03
                },
                3: {
                    'thickness': 0.03,
                    'thermal_conduc': 0.163,
                    'density': 1.2,
                    'heat_capac': 1
                },
                4: {
                    'thickness': 0.012,
                    'thermal_conduc': 0.6,
                    'density': 1650,
                    'heat_capac': 1
                }
            }
        }
    },
    'TypeS': {
        'Floor': {
            'area': 18.75,
            'orientation': -2,
            'layers': {
                1: {
                    'thickness': 0.004,
                    'thermal_conduc': 0.17,
                    'density': 1200,
                    'heat_capac': 1.4
                },
                2: {
                    'thickness': 0.045,
                    'thermal_conduc': 1.4,
                    'density': 2000,
                    'heat_capac': 1
                },
                3: {
                    'thickness': 0.03,
                    'thermal_conduc': 0.045,
                    'density': 135,
                    'heat_capac': 1.03
                },
                4: {
                    'thickness': 0.24,
                    'thermal_conduc': 2.3,
                    'density': 2300,
                    'heat_capac': 1
                },
                5: {
                    'thickness': 0.015,
                    'thermal_conduc': 0.570,
                    'density': 1300,
                    'heat_capac': 1
                }
            }
        },
        'Rooftop': {
            'area': 19.5,
            'orientation': -1,
            'layers': {
                1: {
                    'thickness': 0.015,
                    'thermal_conduc': 0.57,
                    'density': 1300,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.24,
                    'thermal_conduc': 2.3,
                    'density': 2300,
                    'heat_capac': 1
                },
                3: {
                    'thickness': 0.12,
                    'thermal_conduc': 0.04,
                    'density': 105,
                    'heat_capac': 1
                },
                4: {
                    'thickness': 0.005,
                    'thermal_conduc': 0.23,
                    'density': 1100,
                    'heat_capac': 1
                },
                5: {
                    'thickness': 0.2,
                    'thermal_conduc': 0.700,
                    'density': 1638,
                    'heat_capac': 1
                }
            }
        },
        'InnerWall': {
            'area': 36.51,
            'orientation': 0,
            'layers': {
                1: {
                    'thickness': 0.015,
                    'thermal_conduc': 0.57,
                    'density': 1300,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.175,
                    'thermal_conduc': 0.58,
                    'density': 1400,
                    'heat_capac': 1
                },
                3: {
                    'thickness': 0.015,
                    'thermal_conduc': 0.57,
                    'density': 1300,
                    'heat_capac': 1
                }
            }
        },
        'InnerDoor': {
            'area': 2,
            'orientation': 0,
            'layers': {
                1: {
                    'thickness': 0.025,
                    'thermal_conduc': 0.2,
                    'density': 800,
                    'heat_capac': 1.6
                }
            }
        },
        'OuterWall': {
            'area': 7.3,
            'orientation': 180,
            'layers': {
                1: {
                    'thickness': 0.12,
                    'thermal_conduc': 1.65,
                    'density': 2200,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.085,
                    'thermal_conduc': 0.035,
                    'density': 10,
                    'heat_capac': 1.03
                },
                3: {
                    'thickness': 0.012,
                    'thermal_conduc': 0.6,
                    'density': 1650,
                    'heat_capac': 1
                }
            }
        }
    }
}

TABSTypes = {
    'Internal': {
        'UpHalf': {
            'Linoleum': {
                1: {
                    'thickness': 0.06,
                    'density': 2000,
                    'thermal_conduc': 1.2,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.032,
                    'density': 1160,
                    'thermal_conduc': 0.17,
                    'heat_capac': 1.4
                }
            },
            'WoodenParquet': {
                1: {
                    'thickness': 0.06,
                    'density': 2000,
                    'thermal_conduc': 1.2,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.014,
                    'density': 675,
                    'thermal_conduc': 0.16,
                    'heat_capac': 1.6
                }
            },
            'Laminate': {
                1: {
                    'thickness': 0.06,
                    'density': 2000,
                    'thermal_conduc': 1.2,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.007,
                    'density': 860,
                    'thermal_conduc': 0.13,
                    'heat_capac': 1
                }
            },
            'NaturalStone': {
                1: {
                    'thickness': 0.06,
                    'density': 2000,
                    'thermal_conduc': 1.2,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.02,
                    'density': 2600,
                    'thermal_conduc': 2.3,
                    'heat_capac': 1.3
                }
            },
            'Carpet': {
                1: {
                    'thickness': 0.06,
                    'density': 2000,
                    'thermal_conduc': 1.2,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.0056,
                    'density': 2000,
                    'thermal_conduc': 0.06,
                    'heat_capac': 1.300
                }
            },
            'Elastomer': {
                1: {
                    'thickness': 0.06,
                    'density': 2000,
                    'thermal_conduc': 1.2,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.002,
                    'density': 1700,
                    'thermal_conduc': 0.17,
                    'heat_capac': 1400
                }
            },
        },
        'LoHalf': {
            1: {
                'thickness': 0.035,
                'density': 120,
                'thermal_conduc': 0.045,
                'heat_capac': 1.03
            },
            2: {
                'thickness': 0.16,
                'density': 2300,
                'thermal_conduc': 2.3,
                'heat_capac': 1
            },
            3: {
                'thickness': 0.015,
                'density': 1200,
                'thermal_conduc': 0.51,
                'heat_capac': 1
            }
        }
    },
    'External': {
        'Underfloor': {
            'UpHalf': {
                1: {
                    'thickness': 0.06,
                    'density': 2000,
                    'thermal_conduc': 1.2,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.0045,
                    'density': 140,
                    'thermal_conduc': 0.045,
                    'heat_capac': 1
                }
            },
            'LoHalf': {
                1: {
                    'thickness': 0.045,
                    'density': 120,
                    'thermal_conduc': 0.035,
                    'heat_capac': 1.03
                },
                2: {
                    'thickness': 0.15,
                    'density': 2300,
                    'thermal_conduc': 2.3,
                    'heat_capac': 1
                },
                3: {
                    'thickness': 0.06,
                    'density': 120,
                    'thermal_conduc': 0.04,
                    'heat_capac': 1
                },
                4: {
                    'thickness': 0.1,
                    'density': 2000,
                    'thermal_conduc': 1.4,
                    'heat_capac': 0.84
                }
            }
        },
        'ConcreteCore': {
            'UpHalf': {
                1: {
                    'thickness': 0.15,
                    'density': 2000,
                    'thermal_conduc': 1.2,
                    'heat_capac': 1
                },
                2: {
                    'thickness': 0.0045,
                    'density': 140,
                    'thermal_conduc': 0.045,
                    'heat_capac': 1
                }
            },
            'LoHalf': {
                1: {
                    'thickness': 0.045,
                    'density': 120,
                    'thermal_conduc': 0.035,
                    'heat_capac': 1.03
                },
                2: {
                    'thickness': 0.15,
                    'density': 2300,
                    'thermal_conduc': 2.3,
                    'heat_capac': 1
                },
                3: {
                    'thickness': 0.06,
                    'density': 120,
                    'thermal_conduc': 0.04,
                    'heat_capac': 1
                },
                4: {
                    'thickness': 0.1,
                    'density': 2000,
                    'thermal_conduc': 1.4,
                    'heat_capac': 0.84
                }
            }
        }
    }
}

instance_switcher = {
    'Floor': Floor,
    'Rooftop': Rooftop,
    'InnerWall': InnerWall,
    'InnerDoor': InnerWall,
    'OuterWall': OuterWall
}

if __name__ == "__main__":
    export = ExportAll()
    export.run()
