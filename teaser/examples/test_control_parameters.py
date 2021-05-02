import teaser.logic.utilities as utilities
import os

def test_generate_archetype():
    from teaser.project import Project

    prj = Project(load_data=True)
    prj.name = "ArchetypeEFH"

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="ResidentialBuilding",
        year_of_construction=1990,
        number_of_floors=1,
        height_of_floors=3.0,
        net_leased_area=200.0,
        construction_type="heavy")

    return prj

def test_export_aixlib():
    prj = test_generate_archetype()

    prj.dir_reference_results = utilities.get_full_path(
        os.path.join(
            "examples",
            "examplefiles",
            "ReferenceResults",
            "Dymola"))

    print(prj.dir_reference_results)

    prj.used_library_calc = 'AixLib'
    prj.number_of_elements_calc = 2
    prj.weather_file_path = utilities.get_full_path(
        os.path.join(
            "data",
            "input",
            "inputdata",
            "weatherdata",
            "DEU_BW_Mannheim_107290_TRY2010_12_Jahr_BBSR.mos"))

    prj.calc_all_buildings()

    path = prj.export_aixlib(
        internal_id=None,
        path=None)

    return path

if __name__ == '__main__':
    test_export_aixlib()

    print("That's it! :)")

