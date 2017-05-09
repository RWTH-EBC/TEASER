from teaser.data.dataclass import DataClass
from teaser.logic.buildingobjects.buildingphysics.material import Material
import lxml.etree as et
import os
import pandas as pd

dataclass = DataClass()

path_to_DB = 'N:\Forschung\EBC0301_PtJ_Living_Roadmap_mfu\Students\jsc-tbe\Materialdatenbank\masea-daten'
excel_file = 'N:\Forschung\EBC0301_PtJ_Living_Roadmap_mfu\Students\jsc-tbe\MASEA_TEASER.xlsx'
df = pd.read_excel(io=excel_file, skiprows=2)
df = df.set_index('MASEA Materialien')

# materials that do not exist as single layers
bad_materials = ['Beplankte Schaum-Polystyrol-Platten (Mehrschichtenplatten)_150',
                 'Feuerasche_900',
                 'Flugasche_500',
                 'Gichtstaub_350',
                 'Kieselgur mit Klebstoff_350_100°C',
                 'Kieselgur ungebunden_100_100°C',
                 'Kieselgur ungebunden_200_100°C',
                 'Kieselgur ungebunden_400_100°C',
                 'Kieselgur ungebunden_600_100°C',
                 'Kieselgur ungebunden_800_100°C',
                 'Kieselgur (Coswig)_270',
                 'Kunstharzflocken_18',
                 'Steinkohlenschlacke_790',
                 'Polyamid - Folie mit Flies']

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
    material_name_masea = material_tree.xpath('Material/Name/Text')[0].text
    if material_name_masea in bad_materials:
        continue
    material_name = df.at[material_name_masea, 'Englische Bezeichnung']
    material.name = material_name

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

    # load thickness_default and thickness_list
    material.thickness_default = df.at[material_name_masea, 'Standardschichtdicke']
    try:
        thickness_list = df.at[material_name_masea, 'Schichtdicken'].split(',')
    except:
        thickness_list = []
    material.thickness_list = list(map(float, thickness_list))
    material.save_material_template(dataclass)

## manual insertions ##

# new materials
material = Material()
material.name = 'aluminium'
material.density = 2800
material.thermal_conduc = 237
material.heat_capac = 0.897
material.solar_absorp = 0.5
material.thickness_default = 0.0006
material.thickness_list = [0.0005, 0.0007, 0.0008, 0.0009, 0.001]
material.save_material_template(dataclass)

material = Material()
material.name = 'steel_sheet'
material.density = 7800
material.thermal_conduc = 48
material.heat_capac = 0.477
material.solar_absorp = 0.5
material.thickness_default = 0.0006
material.thickness_list = [0.0005, 0.0007, 0.0008, 0.0009, 0.001]
material.save_material_template(dataclass)

material = Material()
material.name = 'steel'
material.density = 7800
material.thermal_conduc = 48
material.heat_capac = 0.477
material.solar_absorp = 0.5
material.thickness_default = 0.006
material.thickness_list = [0.004, 0.008, 0.01]
material.save_material_template(dataclass)

material = Material()
material.name = 'air'
material.density = 1184
material.thermal_conduc = 0.0261
material.heat_capac = 1.005
material.solar_absorp = 0.5
material.thickness_default = 0.02
material.thickness_list = [0.01, 0.04, 0.06, 0.08, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.25, 0.3]
material.save_material_template(dataclass)

# old special material combinations
material = Material()
material.name = 'Sparschalung'
material.density = 600
material.thermal_conduc = 0.13
material.heat_capac = 1.6
material.solar_absorp = 0.5
material.save_material_template(dataclass)

material = Material()
material.name = 'SparrenundDaemmung'
material.density = 50
material.thermal_conduc = 0.14
material.heat_capac = 1
material.solar_absorp = 0.4
material.save_material_template(dataclass)

material = Material()
material.name = 'HolzbalkenmitDaemmung'
material.density = 50
material.thermal_conduc = 0.12
material.heat_capac = 1
material.solar_absorp = 0.5
material.save_material_template(dataclass)

material = Material()
material.name = 'SparrenmitDaemmung'
material.density = 50
material.thermal_conduc = 0.07
material.heat_capac = 1
material.solar_absorp = 0.5
material.save_material_template(dataclass)

material = Material()
material.name = 'FertigbalkenmitMineralwolleschicht'
material.density = 105
material.thermal_conduc = 0.05
material.heat_capac = 1.06
material.solar_absorp = 0.5
material.save_material_template(dataclass)

material = Material()
material.name = 'HolzbalkenmitLuftschichtundLehmschlag'
material.density = 736
material.thermal_conduc = 0.7
material.heat_capac = 1.06
material.solar_absorp = 0.5
material.save_material_template(dataclass)



