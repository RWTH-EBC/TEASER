"""This module contains an example how to change time dependent profiles."""

import teaser.examples.e1_generate_archetype as e1


def example_change_boundary_conditions():
    """Demonstrate changes to time dependent profiles."""
    # In e1_generate_archetype we created a Project with three archetype
    # buildings to get this Project we rerun this example

    prj = e1.example_generate_archetype()

    # Now we want to set the ahu profile of the office building with another
    # profil that reduces the ahu during the weekends. First we create the
    # workfay profile and then run a for loop for one week to decrease the
    # value at weekends.

    office = [
        bldg for bldg in prj.buildings if bldg.name == "OfficeBuilding"][0]

    v_flow_workday = [
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0,
    ]

    v_flow_week = []
    for day in range(7):
        for val in v_flow_workday:
            if day < 5:
                ratio = val
            else:
                if val == 1:
                    ratio = 0.2
                else:
                    ratio = 0.0
            v_flow_week.append(ratio)

    # Here we set the new profile to the AHU profile of TEASER. TEASER will
    # automatically copy this profile for a whole year.

    office.central_ahu.v_flow_profile = v_flow_week

    heating_profile_workday = [
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
        293,
    ]

    # We can apply this also to profiles in UseConditions (e.g. set temperature
    # profile for heating (heating_profile)). We assume on weeksends a lower
    # heating setpoint.

    heating_profile_week = []
    for day in range(7):
        for val in heating_profile_workday:
            if day < 5:
                set_point = val
            else:
                set_point = 290.0
            heating_profile_week.append(set_point)
    for zone in office.thermal_zones:
        zone.use_conditions.heating_profile_profile = heating_profile_week


if __name__ == '__main__':

    example_change_boundary_conditions()

    print("Example 8: That's it! :)")
