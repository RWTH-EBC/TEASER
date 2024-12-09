# # Example 1: Generate archetype buildings using TEASER API
# This module contains an example how to generate archetype buildings
# using TEASER API functions.
# You can run this example using the [jupyter-notebook](https://mybinder.org/v2/gh/RWTH-EBC/TEASER/main?labpath=docs%2Fjupyter_notebooks)


def example_generate_archetype():
    """This function demonstrates the generation of residential and
    non-residential archetype buildings using the API function of TEASER"""

    # First step: Import the TEASER API (called Project) into your Python
    # module

    from teaser.project import Project

    # To use the API, instantiate the Project class and rename the project.
    # Be careful: Dymola does not like whitespaces in names and filenames, thus we will delete them anyway in TEASER.

    prj = Project()
    prj.name = "ArchetypeExample"

    # There are two different types of archetype groups: residential and
    # non-residential buildings. Two API functions offer the opportunity to
    # generate specific archetypes.

    # To generate residential archetype buildings the function
    # Project.add_residential() is used. Seven parameters are compulsory,
    # additional parameters can be set according to the used method. `construction_data`
    # and `geometry_data` are used to distinguish between different construction and archetype
    # methods. The name, year_of_construction, number and height of floors
    # and net_leased_area need to be set to provide enough information for
    # archetype generation. For specific information on the parameters please
    # read the docs.

    prj.add_residential(
        construction_data='iwu_heavy',
        geometry_data='iwu_single_family_dwelling',
        name="ResidentialBuilding",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0)

    # To generate non-residential archetype buildings (in this case an
    # office and a laboratory (a.k.a. institute)) the function
    # Project.add_residential() is used. The meaning of compulsory parameters
    # does not differ from the residential archetype building.

    prj.add_non_residential(
        construction_data='iwu_heavy',
        geometry_data='bmvbs_office',
        name="OfficeBuilding",
        year_of_construction=1988,
        number_of_floors=4,
        height_of_floors=3.5,
        net_leased_area=4500.0)

    prj.add_non_residential(
        construction_data='iwu_heavy',
        geometry_data='bmvbs_institute',
        name="InstituteBuilding",
        year_of_construction=1952,
        number_of_floors=5,
        height_of_floors=4.0,
        net_leased_area=3400.0)

    prj.add_non_residential(
        construction_data='iwu_heavy',
        geometry_data='bmvbs_institute',
        name="InstituteBuildingMoisture",
        year_of_construction=1980,
        number_of_floors=3,
        height_of_floors=4.2,
        net_leased_area=3600.0,
        internal_gains_mode=3)

    # Besides `iwu` and `bmvbs` there is a third option for archetype
    # generation. We integrated the typology of TABULA Germany
    # (http://webtool.building-typology.eu/#bm) and other countries are about to
    # follow. To use TABULA archetype simple choose the default `tabula_de_standard` as the construction_data
    # and `tabula_de_single_family_house`, `tabula_de_multi_family_house`, `tabula_de_terraced_house` or
    # `tabula_de_apartment_block` as the geometry_data. In addition you can specify the
    # construction type of TABULA, chose between `tabula_de_standard` (default),
    # `tabula_de_retrofit` or `tabula_de_adv_retrofit`. In this case we generate one
    # single and one multi family house with TABULA typology.

    # Please not: as we need to load the construction information which are
    # rather big for TABULA, switching from one typology to another in the same
    # Project takes some seconds. If you know from beginning you will only use
    # TABULA typology you should instantiate you Project class without loading
    # data. Project(load_data=False).

    prj.add_residential(
        construction_data='tabula_de_standard',
        geometry_data='tabula_de_single_family_house',
        name="ResidentialBuildingTabula",
        year_of_construction=1988,
        number_of_floors=3,
        height_of_floors=3.2,
        net_leased_area=280.0)

    prj.add_residential(
        construction_data='tabula_de_retrofit',
        geometry_data='tabula_de_multi_family_house',
        name="ResidentialBuildingTabulaMulti",
        year_of_construction=1960,
        number_of_floors=4,
        height_of_floors=3.2,
        net_leased_area=600.0)

    return prj


if __name__ == '__main__':
    prj = example_generate_archetype()

    print("Example 1: That's it! :)")
