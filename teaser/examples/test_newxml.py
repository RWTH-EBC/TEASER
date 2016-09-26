from teaser.data.dataclass import DataClass
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.groundfloor import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.window import Window
dc_old = DataClass(type_element_file="TypeBuildingElements_039.xml")
dc_new = DataClass()

material_dict = {}
import re
regex = re.compile('[^a-zA-z0-9]')


def write_dict(pyxb_element, counter=None):
    for pyxb_layer in pyxb_element.Layers.layer:
        mat = Material(parent=None)
        if counter is not None:
            name = regex.sub('', pyxb_layer.Material.name)+str(counter[0])+"_"+str(counter[1])+str(pyxb_element.construction_type)
        else:
            name = regex.sub('', pyxb_layer.Material.name)
        material_dict[name] = [
            mat,
            mat.material_id,
            pyxb_layer.Material.density,
            pyxb_layer.Material.thermal_conduc,
            pyxb_layer.Material.heat_capac]
    return material_dict


for pyxb_wall in dc_old.element_bind.OuterWall:
    material_dict = write_dict(pyxb_wall)

for pyxb_roof in dc_old.element_bind.Rooftop:
    material_dict = write_dict(pyxb_roof)

for pyxb_gf in dc_old.element_bind.GroundFloor:
    material_dict = write_dict(pyxb_gf)

for pyxb_iw in dc_old.element_bind.InnerWall:
    material_dict = write_dict(pyxb_iw)

for pyxb_ce in dc_old.element_bind.Ceiling:
    material_dict = write_dict(pyxb_ce)

for pyxb_fl in dc_old.element_bind.Floor:
    material_dict = write_dict(pyxb_fl)

for pyxb_win in dc_old.element_bind.Window:
    material_dict = write_dict(pyxb_win, pyxb_win.building_age_group)

print(material_dict)

for pyxb_wall in dc_old.element_bind.OuterWall:
    out_wall = OuterWall()
    out_wall.load_type_element(pyxb_wall.building_age_group[0]+2,
                               pyxb_wall.construction_type,
                               dc_old)
    for lay in out_wall.layer:
        lay.material.material_id = material_dict[lay.material.name][1]

    out_wall.save_type_element(data_class=dc_new)

for pyxb_wall in dc_old.element_bind.Rooftop:
    roof = Rooftop()
    roof.load_type_element(pyxb_wall.building_age_group[0] + 2,
                               pyxb_wall.construction_type,
                               dc_old)
    for lay in roof.layer:
        lay.material.material_id = material_dict[lay.material.name][1]

    roof.save_type_element(data_class=dc_new)

for pyxb_wall in dc_old.element_bind.GroundFloor:
    gf = GroundFloor()
    gf.load_type_element(pyxb_wall.building_age_group[0] + 2,
                               pyxb_wall.construction_type,
                               dc_old)
    for lay in gf.layer:
        lay.material.material_id = material_dict[lay.material.name][1]

    gf.save_type_element(data_class=dc_new)

for pyxb_wall in dc_old.element_bind.InnerWall:
    iw = InnerWall()
    iw.load_type_element(pyxb_wall.building_age_group[0] + 2,
                               pyxb_wall.construction_type,
                               dc_old)
    for lay in iw.layer:
        lay.material.material_id = material_dict[lay.material.name][1]

    iw.save_type_element(data_class=dc_new)

for pyxb_wall in dc_old.element_bind.Ceiling:
    print(pyxb_wall.building_age_group[0])
    ce = Ceiling()
    ce.load_type_element(pyxb_wall.building_age_group[0] + 2,
                               pyxb_wall.construction_type,
                               dc_old)
    for lay in ce.layer:
        lay.material.material_id = material_dict[lay.material.name][1]

    ce.save_type_element(data_class=dc_new)

for pyxb_wall in dc_old.element_bind.Floor:
    fl = Floor()
    fl.load_type_element(pyxb_wall.building_age_group[0] + 2,
                               pyxb_wall.construction_type,
                               dc_old)
    for lay in fl.layer:
        lay.material.material_id = material_dict[lay.material.name][1]

    fl.save_type_element(data_class=dc_new)

for pyxb_wall in dc_old.element_bind.Window:
    win = Window()
    win.load_type_element(pyxb_wall.building_age_group[0] + 2,
                               pyxb_wall.construction_type,
                               dc_old)
    counter = pyxb_wall.building_age_group
    for lay in win.layer:
        lay.material.material_id = material_dict[lay.material.name+str(
            counter[0])+"_"+str(counter[1])+str(pyxb_wall.construction_type)][1]
        lay.material.name = lay.material.name+str(
            counter[0])+"_"+str(counter[1])+str(pyxb_wall.construction_type)

    win.save_type_element(data_class=dc_new)

for key, value in material_dict.items():

    value[0].name = key
    value[0].density = value[2]
    value[0].thermal_conduc = value[3]
    value[0].heat_capac = value[4]
    value[0].save_material_template(data_class=dc_new)



