from teaser.project import Project
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
import uuid
import teaser.data.output.buildingelement_output as be
print(uuid.uuid1())
print(type(str(uuid.uuid1())))

from teaser.data.dataclass import DataClass
from teaser.logic.buildingobjects.buildingphysics.material import Material

dc = DataClass()
dc.path_tb =

material_list = []

for pyxb_wall in dc.element_bind.OuterWall:
    for pyxb_layer in pyxb_wall.Layers.layer:
        print(pyxb_layer)
        mat = Material(parent=None)
        mat.name = pyxb_layer.material.value()
        print(pyxb_layer.material.value())
        mat.save_material_template(data_class=dc)

