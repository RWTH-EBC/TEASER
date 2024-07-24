from teaser.project import Project


def example_adjust_schedules():
    """"This function demonstrates the adjustment of default schedules for
        - adjusted_opening_times
        - first_saturday_of_year
        - profiles_weekend_factor
        - set_back_times
        - heating_set_back
        - cooling_set_back
    for an residential building using calc_adj_schedules function"""

    # First part is only archetype creation, see e1_generate_archetype.py
    prj = Project()
    prj.name = "ArchetypeExample"

    prj.add_residential(
        construction_data='iwu_heavy',
        geometry_data='iwu_single_family_dwelling',
        name="ResidentialBuilding",
        year_of_construction=1988,
        number_of_floors=2,
        height_of_floors=3.2,
        net_leased_area=200.0
    )

    # get the thermalzone of the building (only one exists)
    tz = prj.buildings[0].thermal_zones[0]

    # get the use condition of the thermalzone
    use_cond = tz.use_conditions

    # set attributes for the adjustments. There are adjustments available for
    # heating and cooling profiles, weekends and opening times.

    # lets start with heating and cooling profiles:
    # first set the set back times. First value is the first hour the set back
    # is applied to, last value the last hour.
    use_cond.set_back_times = [5, 22]
    # now the the set back values in kelvin
    use_cond.heating_set_back = -2
    use_cond.cooling_set_back = 3

    # now set adjustments for weekend
    # Set the weekday number of first saturday of the year, this is needed to
    # calc which days of profile should be reduced by profiles_weekend_factor.
    use_cond.first_saturday_of_year = 4
    # set the factor to reduce the weekend profile. For a reduction use
    #         values between [0;1]. Increase is also possible.
    use_cond.profiles_weekend_factor = 0.4

    # now set the adjusted opening times
    # Set the first and last hour of opening. These will cut or extend the
    # existing profiles (machines, lights, persons).
    use_cond.adjusted_opening_times = [10, 15]

    # Finally calculate the adjusted schedules
    use_cond.calc_adj_schedules()

    return prj


if __name__ == '__main__':
    prj = example_adjust_schedules()

    print("Example 10: That's it! :)")
