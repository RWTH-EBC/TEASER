from teaser.data.dataclass import DataClass
from teaser.logic.buildingobjects.buildingphysics.material import Material
import lxml.etree as et
import os

dataclass = DataClass()

path_to_DB = 'N:\Forschung\EBC0301_PtJ_Living_Roadmap_mfu\Students\jsc-tbe\Materialdatenbank\masea-daten'


# load all XML files
for xml_file in os.listdir(path_to_DB):
    if not xml_file.endswith('.xml'):
        continue
    file = os.path.join(path_to_DB, xml_file)
    material_xml = et.parse(file)

    material = Material()
    material_tree = material_xml.getroot()
    phys_quant = material_tree.xpath('//Scalar/PhysQuantity/Name/Text')     # get all "PhysQuantity"

    # material name
    material_name = material_tree.xpath('Material/Name/Text')[0].text
    material.name = material_name

    count_mat = 0
    for elem in phys_quant:
        if elem.text == 'Rohdichte':
            material.density = elem.getparent().getparent().getparent().attrib['value']
        elif elem.text == 'Spezifische Wärmekapazität':
            material.heat_capac = elem.getparent().getparent().getparent().attrib['value']
        elif elem.text == 'Wärmeleitfähigkeit':
            material.thermal_conduc = elem.getparent().getparent().getparent().attrib['value']

    if material_tree.xpath('//Material/Name/Text')[0].text == 'Anstriche':
        material.solar_absorp = 0.5
    elif material_tree.xpath('//Material/Name/Text')[0].text == 'Erden und Böden':
        material.solar_absorp = 0.7
    elif material_tree.xpath('//Material/Name/Text')[0].text == 'Zementhaltige Baustoffe':
        material.solar_absorp = 0.5
    elif material_tree.xpath('//Material/Name/Text')[0].text == 'Mauersteine':
        if 'Porenbeton' in material.name():
            material.solar_absorp = 0.5
        else:
            material.solar_absorp = 0.7
    elif material_tree.xpath('//Material/Name/Text')[0].text == 'Natursteine':
        material.solar_absorp = 0.5
    elif len(material_tree.xpath('//Material/Name/Text')) > 1:
        if material_tree.xpath('//Material/Name/Text')[1].text == 'Fassadenbekleidungen, Bodenbeläge und Einkleidungen':
            material.solar_absorp = 0.5
    elif material_tree.xpath('//Material/Name/Text')[0].text == 'Putze, Mörtel und Ausfachungen':
        material.solar_absorp = 0.5
    elif material_tree.xpath('//Material/Name/Text')[0].text == 'Bauplatten':
        material.solar_absorp = 0.5
    elif material_tree.xpath('//Material/Name/Text')[0].text == 'Folien und Abdichtungsstoffe':
        material.solar_absorp = 0.7
    elif material_tree.xpath('//Material/Name/Text')[0].text == 'Sonstige':
        material.solar_absorp = 0.5
    elif material_tree.xpath('//Material/Name/Text')[0].text == 'Naturstoffe':
        material.solar_absorp = 0.7
    elif material_tree.xpath('//Material/Name/Text')[0].text == 'Holz':
        material.solar_absorp = 0.7
    elif material_tree.xpath('//Material/Name/Text')[0].text == 'Dämmstoffe':
        material.solar_absorp = 0.5
    else:
        material.solar_absorp = 0.5
        count_mat += 1
    material.save_material_template(dataclass)
print(count_mat)


