# Created July 2015
# TEASER 4 Development Team

"""This module contains an example how to generate archetype buildings using
TEASER API functions.
"""


def example_generate_archetype():
    """"This function demonstrates the generation of residential and
    non-residential archetype buildings using the API function of TEASER"""

    # First step: Import the TEASER API (called Project) into your Python
    # module

    from teaser.project import Project

    # To use the API instantiate the Project class and rename the Project. The
    # parameter load_data=True indicates that we load archetype data into our
    # Project (e.g. for Material properties and typical wall constructions.
    # This can take a few seconds, depending on the size of the used data base.
    # Be careful: Dymola does not like whitespaces in names and filenames,
    # thus we will delete them anyway in TEASER.


    prj = Project(load_data=True)
    prj.name = "ArchetypeExample"

    # There are two different types of archetype groups: residential and
    # non-residential buildings. Two API functions offer the opportunity to
    # generate specific archetypes.

    # To generate residential archetype buildings the function
    # Project.add_residential() is used. Seven parameters are compulsory,
    # additional parameters can be set according to the used method. `method`
    # and `usage` are used to distinguish between different archetype
    # methods. The name, year_of_construction, number and height of floors
    # and net_leased_area need to be set to provide enough information for
    # archetype generation. For specific information on the parameters please
    # read the docs.

    prj.add_residential(
        method='iwu',
        usage='single_family_dwelling',
        name="ResidentialBuilding",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200)

    # To generate non-residential archetype buildings (in this case an
    # office and a laboratory (a.k.a. institute)) the function
    # Project.add_residential() is used. The meaning of compulsory parameters
    # does not differ from the residential archetype building.

    prj.add_non_residential(
        method='bmvbs',
        usage='office',
        name="OfficeBuilding",
        year_of_construction=1988,
        number_of_floors=4,
        height_of_floors=3.5,
        net_leased_area=4500)

    prj.add_non_residential(
        method='bmvbs',
        usage='institute',
        name="InstituteBuilding",
        year_of_construction=1952,
        number_of_floors=5,
        height_of_floors=4.0,
        net_leased_area=3400)

    return prj

if __name__ == '__main__':
    prj = example_generate_archetype()

    print("Example 1: That's it! :)")
