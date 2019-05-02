from teaser.data.dataclass import DataClass
from teaser.logic.buildingobjects.buildingphysics.material import Material
import teaser.logic.utilities as utils
import os

data_class_old = DataClass()
data_class_old.path_mat = utils.get_full_path(
    "data/input/inputdata/MaterialTemplates.xml")
data_class_old.load_mat_binding()

os.remove(utils.get_full_path(
    "data/input/inputdata/MaterialTemplates.json"))

data_class_new = DataClass()

for out_wall in data_class_old.material_bind.Material:
    wall = Material()
    wall.load_material_template(
        mat_name=out_wall.name,
        data_class=data_class_old)

    wall.save_material_template(
        data_class=data_class_new)
