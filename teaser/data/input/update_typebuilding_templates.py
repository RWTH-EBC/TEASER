import lxml.etree as et
import pandas as pd
from copy import deepcopy
import teaser.logic.utilities as utils
from teaser.data.dataclass import DataClass
#from teaser.data.dataclass_old import DataClassOld
from teaser.logic.buildingobjects.buildingphysics.material import Material
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.ceiling import Ceiling
from teaser.logic.buildingobjects.buildingphysics.floor import Floor
from teaser.logic.buildingobjects.buildingphysics.groundfloor \
    import GroundFloor
from teaser.logic.buildingobjects.buildingphysics.innerwall import InnerWall
from teaser.logic.buildingobjects.buildingphysics.outerwall import OuterWall
from teaser.logic.buildingobjects.buildingphysics.rooftop import Rooftop
from teaser.logic.buildingobjects.buildingphysics.window import Window

excel_file = 'N:\Forschung\EBC0301_PtJ_Living_Roadmap_mfu\Students\jsc-tbe\MASEA_Typebuildings.xlsx'
df = pd.read_excel(io=excel_file, skiprows=1)
df = df.set_index('Material TEASER Typebuildings')

#file = "D:/jsc-tbe/TEASER/teaser/data/input/inputdata
# /TypeBuildingElements_old.xml"
file = utils.get_full_path(
            "data/input/inputdata/MaterialTemplates_old.xml")
elem_xml = et.parse(file)
elem_tree = elem_xml.getroot()

# load new MaterialTemplates
dataclass_new = DataClass()

# load old MaterialTemplates
dataclass_old = DataClass()
dataclass_old.path_mat = utils.get_full_path(
            "data/input/inputdata/MaterialTemplates_old.xml")
dataclass_old.path_tb = utils.get_full_path(
            "data/input/inputdata/TypeBuildingElements_old.xml")
dataclass_old.load_tb_binding()
dataclass_old.load_mat_binding()

# read TypeBuildingElements XML and list all elements

# load element
element_binding_old = dataclass_old.element_bind
element_binding_new = dataclass_new.element_bind
ow_list = element_binding_old.OuterWall
iw_list = element_binding_old.InnerWall
ce_list = element_binding_old.Ceiling
f_list = element_binding_old.Floor
ft_list = element_binding_old.Rooftop
gf_list = element_binding_old.GroundFloor
w_list = element_binding_old.Window

for ow in element_binding_old.OuterWall:
    # eliminate old annex TypeBuilding
    if 'annex' in ow.construction_type:
        continue
    # load old element
    outer_wall_old = OuterWall()
    outer_wall_old.load_type_element(year=ow.building_age_group[1],
                                 construction=ow.construction_type,
                                 data_class=dataclass_old)
    # create new element and exchange layer list
    outer_wall_new = deepcopy(outer_wall_old)
    outer_wall_new._layer = []
    count_layer = 0
    for layer in outer_wall_old.layer:
        mat_old = layer.material
        mat_name_old = mat_old.name

        if mat_name_old == 'Sandwichpaneel':  # 3 layers
            # layer one (inner covering layer)
            mat_name_new_one = 'sheet_steel'
            mat_new_one = Material()
            mat_new_one.load_material_template(mat_name=mat_name_new_one,
                                               data_class=dataclass_new)
            layer_new_one = Layer(id=count_layer)
            count_layer += 1
            layer_new_one.material = mat_new_one
            layer_new_one.thickness = mat_new_one.thickness_default

            # layer three (plaster)
            mat_name_new_three = 'sheet_steel'
            mat_new_three = Material()
            mat_new_three.load_material_template(mat_name=mat_name_new_three,
                                               data_class=dataclass_new)
            layer_new_three = Layer(id=count_layer)
            count_layer += 1
            layer_new_three.material = mat_new_three
            layer_new_three.thickness = mat_new_three.thickness_default

            # layer two (insulation e.g. XPS)
            mat_name_new_two = 'XPS'
            mat_new_two = Material()
            mat_new_two.load_material_template(mat_name=mat_name_new_two,
                                               data_class=dataclass_new)
            layer_new_two = Layer(id=count_layer)
            count_layer += 1
            layer_new_two.material = mat_new_two
            layer_new_two.thickness = layer.thickness - layer_new_one.thickness - layer_new_three.thickness

            # add layers to wall
            outer_wall_new.add_layer(layer_new_one)
            outer_wall_new.add_layer(layer_new_two)
            outer_wall_new.add_layer(layer_new_three)

        else:
            mat_name_new = df.at[mat_name_old, 'Material MASEA Update']
            mat_new = Material()
            mat_new.load_material_template(mat_name=mat_name_new,
                                       data_class=dataclass_new)
            layer_new = Layer(id=count_layer)
            layer_new.material = mat_new
            layer_new.thickness = layer.thickness
            outer_wall_new.add_layer(layer_new)
            count_layer += 1

    outer_wall_new.save_type_element(data_class=dataclass_new)

for iw in element_binding_old.InnerWall:
    # eliminate old annex TypeBuilding
    if 'annex' in iw.construction_type:
        continue
    # load old element
    inner_wall_old = InnerWall()
    inner_wall_old.load_type_element(year=iw.building_age_group[1],
                                 construction=iw.construction_type,
                                 data_class=dataclass_old)
    # create new element and exchange layer list
    inner_wall_new = deepcopy(inner_wall_old)
    inner_wall_new._layer = []
    count_layer = 0
    for layer in inner_wall_old.layer:
        mat_old = layer.material
        mat_name_old = mat_old.name

        if mat_name_old == 'Sandwichpaneel':  # 3 layers
            # layer one (inner covering layer)
            mat_name_new_one = 'sheet_steel'
            mat_new_one = Material()
            mat_new_one.load_material_template(mat_name=mat_name_new_one)
            layer_new_one = Layer(id=count_layer)
            count_layer += 1
            layer_new_one.material = mat_new_one
            layer_new_one.thickness = mat_new_one.thickness_default

            # layer three (plaster)
            mat_name_new_three = 'sheet_steel'
            mat_new_three = Material()
            mat_new_three.load_material_template(mat_name=mat_name_new_three)
            layer_new_three = Layer(id=count_layer)
            count_layer += 1
            layer_new_three.material = mat_new_three
            layer_new_three.thickness = mat_new_three.thickness_default

            # layer two (insulation e.g. XPS)
            mat_name_new_two = 'XPS'
            mat_new_two = Material()
            mat_new_two.load_material_template(mat_name=mat_name_new_two)
            layer_new_two = Layer(id=count_layer)
            count_layer += 1
            layer_new_two.material = mat_new_two
            layer_new_two.thickness = layer.thickness - layer_new_one.thickness - layer_new_three.thickness

            # add layers to wall
            inner_wall_new.add_layer(layer_new_one)
            inner_wall_new.add_layer(layer_new_two)
            inner_wall_new.add_layer(layer_new_three)

        else:
            mat_name_new = df.at[mat_name_old, 'Material MASEA Update']
            mat_new = Material()
            mat_new.load_material_template(mat_name=mat_name_new,
                                           data_class=dataclass_new)
            layer_new = Layer(id=count_layer)
            layer_new.material = mat_new
            layer_new.thickness = layer.thickness
            inner_wall_new.add_layer(layer_new)
            count_layer += 1

    inner_wall_new.save_type_element(data_class=dataclass_new)

for ce in element_binding_old.Ceiling:
    # eliminate old annex TypeBuilding
    if 'annex' in ce.construction_type:
        continue
    # load old element
    ceiling_old = Ceiling()
    ceiling_old.load_type_element(year=ce.building_age_group[1],
                                 construction=ce.construction_type,
                                 data_class=dataclass_old)
    # create new element and exchange layer list
    ceiling_new = deepcopy(ceiling_old)
    ceiling_new._layer = []
    count_layer = 0
    for layer in ceiling_old.layer:
        mat_old = layer.material
        mat_name_old = mat_old.name
        mat_name_new = df.at[mat_name_old, 'Material MASEA Update']
        mat_new = Material()
        mat_new.load_material_template(mat_name=mat_name_new,
                                       data_class=dataclass_new)
        layer_new = Layer(id=count_layer)
        layer_new.material = mat_new
        layer_new.thickness = layer.thickness
        ceiling_new.add_layer(layer_new)
        count_layer += 1

    ceiling_new.save_type_element(data_class=dataclass_new)

for f in element_binding_old.Floor:
    # eliminate old annex TypeBuilding
    if 'annex' in f.construction_type:
        continue
    # load old element
    floor_old = Floor()
    floor_old.load_type_element(year=f.building_age_group[1],
                                 construction=f.construction_type,
                                 data_class=dataclass_old)
    # create new element and exchange layer list
    floor_new = deepcopy(floor_old)
    floor_new._layer = []
    count_layer = 0
    for layer in floor_old.layer:
        mat_old = layer.material
        mat_name_old = mat_old.name
        mat_name_new = df.at[mat_name_old, 'Material MASEA Update']
        mat_new = Material()
        mat_new.load_material_template(mat_name=mat_name_new,
                                       data_class=dataclass_new)
        layer_new = Layer(id=count_layer)
        layer_new.material = mat_new
        layer_new.thickness = layer.thickness
        floor_new.add_layer(layer_new)
        count_layer += 1

    floor_new.save_type_element(data_class=dataclass_new)

for r in element_binding_old.Rooftop:
    # eliminate old annex TypeBuilding
    if 'annex' in r.construction_type:
        continue
    # load old element
    rooftop_old = Rooftop()
    rooftop_old.load_type_element(year=r.building_age_group[1],
                                 construction=r.construction_type,
                                 data_class=dataclass_old)
    # create new element and exchange layer list
    rooftop_new = deepcopy(rooftop_old)
    rooftop_new._layer = []
    count_layer = 0
    for layer in rooftop_old.layer:
        mat_old = layer.material
        mat_name_old = mat_old.name
        mat_name_new = df.at[mat_name_old, 'Material MASEA Update']
        mat_new = Material()
        mat_new.load_material_template(mat_name=mat_name_new,
                                       data_class=dataclass_new)
        layer_new = Layer(id=count_layer)
        layer_new.material = mat_new
        layer_new.thickness = layer.thickness
        rooftop_new.add_layer(layer_new)
        count_layer += 1

    rooftop_new.save_type_element(data_class=dataclass_new)

for gf in element_binding_old.GroundFloor:
    # eliminate old annex TypeBuilding
    if 'annex' in gf.construction_type:
        continue
    # load old element
    ground_floor_old = GroundFloor()
    ground_floor_old.load_type_element(year=gf.building_age_group[1],
                                 construction=gf.construction_type,
                                 data_class=dataclass_old)
    # create new element and exchange layer list
    ground_floor_new = deepcopy(ground_floor_old)
    ground_floor_new._layer = []
    count_layer = 0
    for layer in ground_floor_old.layer:
        mat_old = layer.material
        mat_name_old = mat_old.name
        mat_name_new = df.at[mat_name_old, 'Material MASEA Update']
        mat_new = Material()
        mat_new.load_material_template(mat_name=mat_name_new,
                                       data_class=dataclass_new)
        layer_new = Layer(id=count_layer)
        layer_new.material = mat_new
        layer_new.thickness = layer.thickness
        ground_floor_new.add_layer(layer_new)
        count_layer += 1

    ground_floor_new.save_type_element(data_class=dataclass_new)

for w in element_binding_old.Window:
    # eliminate old annex TypeBuilding
    if 'annex' in w.construction_type:
        continue
    # load old element
    window_old = Window()
    window_old.load_type_element(year=w.building_age_group[1],
                                 construction=w.construction_type,
                                 data_class=dataclass_old)
    # save window templates in new MaterialTemplate
    count_layer = 0
    for layer in window_old.layer:
        mat = layer.material
        mat.save_material_template(data_class=dataclass_new)
    # create new element and exchange layer list
    window_new = deepcopy(window_old)
    window_new._layer = []
    for layer in window_old.layer:
        mat_old = layer.material
        mat_name_new = mat_old.name
        mat_new = Material()
        mat_new.load_material_template(mat_name=mat_name_new,
                                       data_class=dataclass_new)
        layer_new = Layer(id=count_layer)
        layer_new.material = mat_new
        layer_new.thickness = layer.thickness
        window_new.add_layer(layer_new)
        count_layer += 1

    window_new.save_type_element(data_class=dataclass_new)
