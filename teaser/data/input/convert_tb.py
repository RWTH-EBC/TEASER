from teaser.data.dataclass import DataClass
import teaser.data.input.buildingelement_input as be_input
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.door import Door
from teaser.logic.buildingobjects.buildingphysics.window import Window
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
import teaser.logic.utilities as utils
import os

data_class_old = DataClass()
data_class_old.path_tb = utils.get_full_path(
    "data/input/inputdata/TypeElements_TABULA_DE.xml")
data_class_old.load_tb_binding()
data_class_old.path_mat = utils.get_full_path(
    "data/input/inputdata/MaterialTemplates.xml")
data_class_old.load_tb_binding()
data_class_old.load_mat_binding()

# os.remove(utils.get_full_path(
#     "data/input/inputdata/TypeElements_TABULA_DE.json"))

data_class_new = DataClass(used_statistic='tabula_de')

for out_wall in data_class_old.element_bind.OuterWall:
    wall = OuterWall()
    be_input.load_type_element(
        element=wall,
        year=out_wall.building_age_group[0] + 1,
        construction=out_wall.construction_type,
        data_class=data_class_old)
    wall.save_type_element(
        data_class=data_class_new)
for out_wall in data_class_old.element_bind.Door:
    wall = Door()
    be_input.load_type_element(
        element=wall,
        year=out_wall.building_age_group[0] + 1,
        construction=out_wall.construction_type,
        data_class=data_class_old)
    wall.save_type_element(
        data_class=data_class_new)
for out_wall in data_class_old.element_bind.Window:
    wall = Window()
    be_input.load_type_element(
        element=wall,
        year=out_wall.building_age_group[0] + 1,
        construction=out_wall.construction_type,
        data_class=data_class_old)
    wall.save_type_element(
        data_class=data_class_new)
for out_wall in data_class_old.element_bind.Rooftop:
    wall = Rooftop()
    be_input.load_type_element(
        element=wall,
        year=out_wall.building_age_group[0] + 1,
        construction=out_wall.construction_type,
        data_class=data_class_old)
    wall.save_type_element(
        data_class=data_class_new)
for out_wall in data_class_old.element_bind.GroundFloor:
    wall = GroundFloor()
    be_input.load_type_element(
        element=wall,
        year=out_wall.building_age_group[0] + 1,
        construction=out_wall.construction_type,
        data_class=data_class_old)
    wall.save_type_element(
        data_class=data_class_new)
for out_wall in data_class_old.element_bind.InnerWall:
    wall = InnerWall()
    be_input.load_type_element(
        element=wall,
        year=out_wall.building_age_group[0] + 1,
        construction=out_wall.construction_type,
        data_class=data_class_old)
    wall.save_type_element(
        data_class=data_class_new)
for out_wall in data_class_old.element_bind.Ceiling:
    wall = Ceiling()
    be_input.load_type_element(
        element=wall,
        year=out_wall.building_age_group[0] + 1,
        construction=out_wall.construction_type,
        data_class=data_class_old)
    wall.save_type_element(
        data_class=data_class_new)
for out_wall in data_class_old.element_bind.Floor:
    wall = Floor()
    be_input.load_type_element(
        element=wall,
        year=out_wall.building_age_group[0] + 1,
        construction=out_wall.construction_type,
        data_class=data_class_old)
    wall.save_type_element(
        data_class=data_class_new)
