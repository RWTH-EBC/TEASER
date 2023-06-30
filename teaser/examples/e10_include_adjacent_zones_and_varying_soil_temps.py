# -*- coding: utf-8 -*-
# @Author: Philip Groesdonk
# @Date:   2019-06-30 09:09:09

"""
This script demonstrates five features of TEASER:
 - how borders between adjacent zones can be modelled
 - in connection to that, the export to a FiveElement AixLib ROM model
 - how elements (here windows) can be newer than the building and get the
   respective typical properties
 - how non-constant soil temperatures are included
 - how custom templates for the Modelica export are used
 - the different estimation approaches for the interior wall area

It features the data presented in a contribution to the 2023 International
Modelica Conference.
"""

from teaser.project import Project
from teaser.data.dataclass import DataClass
from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
import teaser.logic.utilities as utilities
import os
import shutil

# for the conference publication, four variations were calculated
for variation in ['A', 'B', 'C', 'D']:
    # this project is initialized without data class
    prj = Project(False)
    # now, we can set 'tabula_de' manually
    prj.data = DataClass(used_statistic='tabula_de')

    if variation == 'D':
        # this is the variation that represents the actual state of the building
        prj.load_project(utilities.get_full_path(
            f"examples/examplefiles/e10_varD.json"
        ))

        # in the json for variation D, one interzonal element is missing, so we
        # can show in the example how it is manually added
        # Because we want to add the properties manually here, check the
        # generation of variations A to C further below to see how typical
        # element properties are added to interzonal elements

        # Add the interzonal element connecting zone 0 (attic) and zone 2 (main
        # zone)
        attic = prj.buildings[0].thermal_zones[0]
        main_zone = prj.buildings[0].thermal_zones[2]

        # It needs to be as an element of both the attic and the main zone
        # The two elements, although representing the same physical element,
        # are not semantically connected in the TEASER project due to the
        # hierarchical structure project > building > thermal zone > element.
        # Therefore, make sure that changes to one element always have to be
        # implemented also for its counterpart.

        # start with the ceiling of the main zone
        from teaser.logic.buildingobjects.buildingphysics.interzonalceiling\
            import InterzonalCeiling
        main_ceiling = InterzonalCeiling(parent=main_zone, other_side=attic)
        main_ceiling.name = "floor_4C797480FF814849944536D7EDE2A122_2"
        main_ceiling.area = 48.90700957621479
        main_ceiling.orientation = -1
        main_ceiling.tilt = 0.0
        main_ceiling.inner_convection = 5.0
        main_ceiling.outer_convection = 5.0
        main_ceiling.inner_radiation = 5.0
        main_ceiling.outer_radiation = 5.0

        # First layer: concrete
        layer_mc1 = Layer(parent=main_ceiling, id=0)
        layer_mc1.thickness = 0.02
        material_mc1 = Material(layer_mc1)
        material_mc1.name = "Tile"
        material_mc1.density = 2400.0
        material_mc1.heat_capac = 1.0
        material_mc1.thermal_conduc = 2.5
        material_mc1.solar_absorp = 0.7
        material_mc1.ir_emissivity = 0.9

        # Second layer: mineral wool
        layer_mc2 = Layer(parent=main_ceiling, id=1)
        layer_mc2.thickness = 0.13
        material_mc2 = Material(layer_mc2)
        material_mc2.name = "Mineralwolle_13cm"
        material_mc2.density = 1800.0
        material_mc2.heat_capac = 0.95
        material_mc2.thermal_conduc = 0.06
        material_mc2.solar_absorp = 0.7
        material_mc2.ir_emissivity = 0.9

        # now add the attic floor and give it the same properties
        # differences are
        # a) the orientation (-2 instead of -1)
        # b) the layer sequence is inverted - because the sequence always starts
        #    at the inside of the thermal zone the element belongs to
        from teaser.logic.buildingobjects.buildingphysics.interzonalfloor\
            import InterzonalFloor
        attic_floor = InterzonalFloor(parent=attic, other_side=main_zone)
        attic_floor.name = "floor_4C797480FF814849944536D7EDE2A122_2"
        attic_floor.area = 48.90700957621479
        attic_floor.orientation = -2
        attic_floor.tilt = 0.0
        attic_floor.inner_convection = 5.0
        attic_floor.outer_convection = 5.0
        attic_floor.inner_radiation = 5.0
        attic_floor.outer_radiation = 5.0

        # First layer: mineral wool
        layer_af1 = Layer(parent=attic_floor, id=0)
        layer_af1.thickness = 0.13
        material_af1 = Material(layer_af1)
        material_af1.name = "Mineralwolle_13cm"
        material_af1.density = 1800.0
        material_af1.heat_capac = 0.95
        material_af1.thermal_conduc = 0.06
        material_af1.solar_absorp = 0.7
        material_af1.ir_emissivity = 0.9

        # Second layer: concrete
        layer_af2 = Layer(parent=attic_floor, id=1)
        layer_af2.thickness = 0.02
        material_af2 = Material(layer_af2)
        material_af2.name = "Tile"
        material_af2.density = 2400.0
        material_af2.heat_capac = 1.0
        material_af2.thermal_conduc = 2.5
        material_af2.solar_absorp = 0.7
        material_af2.ir_emissivity = 0.9

    elif variation in ('A', 'B', 'C'):
        prj.load_project(utilities.get_full_path(
            f"examples/examplefiles/e10_raw.json"
        ))

        # The default properties from the typology (selected previously by
        # setting the data class) need to be loaded element-wise, replacing all
        # previously set energy-relevant parameters of the elements.
        # Here, we just load the standard existing state for the year of
        # construction for each element. Note that
        for tz in prj.buildings[0].thermal_zones:
            # Note that the windows get a different year of construction (1995)
            # than the rest of the building (1965, from the json import file).
            for el in tz.windows:
                el.load_type_element(1995, 'tabula_standard_1_SFH')
                el.shading_max_irr = 10000
            # rooftops, ground floors and interzonal elements have a clearly
            # associated TABULA standard construction. See the publication
            # mentioned above for details about when which standard construction
            # is used for interzonal elements.
            # (here, typical outer elements are loaded, because
            # tz.use_conditions.with_heating is False for attic and basement
            # and True for the main zone)
            for el in tz.rooftops + tz.ground_floors + tz.interzonal_elements:
                el.load_type_element(el.year_of_construction,
                                     'tabula_standard_1_SFH')
            # There are two different standard constructions for some element
            # types in some TABULA type building, especially outer walls.
            # This is why two outer wall elements are  stored in the JSON file
            # here and why generate_archetype will create similar structures,
            # too. The ratio of their sizes is sourced from the TABULA
            # publications. In total, they sum up to the size of the actual
            # building's wall.
            for el in tz.outer_walls[:4]:
                el.load_type_element(el.year_of_construction,
                                     'tabula_standard_1_SFH')
            for el in tz.outer_walls[4:]:
                el.load_type_element(el.year_of_construction,
                                     'tabula_standard_2_SFH')

    for tz in prj.buildings[0].thermal_zones:
        # In this case, we want to simulate one-directional heat flow. This
        # is why we adapt the respective convection coefficients
        for el in tz.rooftops:
            el.inner_convection = 5.0
        for el in tz.ground_floors:
            el.inner_convection = 0.9
        for el in tz.interzonal_ceilings:
            if el.other_side is prj.buildings[0].thermal_zones[2]:
                # border (from basement) to main zone
                el.inner_convection = 0.9
                el.outer_convection = 0.9
            else:
                # border (from main zone) to attic
                el.inner_convection = 5.0
                el.outer_convection = 5.0
        for el in tz.interzonal_floors:
            if el.other_side is prj.buildings[0].thermal_zones[2]:
                # border (from attic) to main zone
                el.inner_convection = 5.0
                el.outer_convection = 5.0
            else:
                # border (from main zone) to basement
                el.inner_convection = 0.9
                el.outer_convection = 0.9

    # change the project name so exports are clearly recognizable
    prj.name = 'Example_e10_var' + variation

    # three ways for setting the inner wall area
    # if you run the example, you will see the difference in the console output.
    # for both approximation approaches (A and B), it is essential that you
    # set the number of floors per zone before calling tz.set_inner_wall_area().
    # If you don't, the function will assume the zone has the same number of
    # floors as the building.
    if variation == 'A':
        # use the approach that was implemented in TEASER the first version
        prj.buildings[0].inner_wall_approximation_approach = 'teaser_default'
    elif variation == 'B':
        # use the new approach that checks typical room sizes and outer elements
        # in this case, interzonal elements must be created beforehand. They may
        # influence the result of the application.
        prj.buildings[0].inner_wall_approximation_approach \
            = 'typical_minus_outer_extended'
    elif variation == 'C':
        # define the areas manually for each zone
        iw_areas = [0, 81.6764, 132.74215581488374]
        ceil_areas = [0, 0, 66.15407513491138]
        floor_areas = [0, 0, 66.15407513491138]

    # calculate the areas and print the result to the console
    thermal_zone_dict = {0: 'attic', 1: 'basement', 2: 'main zone'}
    print('inner wall sizes for variation ' + variation)
    for tzno, tz in enumerate(prj.buildings[0].thermal_zones):
        print(f'Thermal zone {tzno} ({thermal_zone_dict[tzno]}):')
        if tzno == 0 or tzno == 1:
            tz.number_of_floors = 1
        elif tzno == 2:
            tz.number_of_floors = 2
        if variation in ['A', 'B']:
            tz.set_inner_wall_area()
        elif variation == 'C':
            for iw in tz.inner_walls:
                iw.area = iw_areas[tzno]
            for ceil in tz.ceilings:
                ceil.area = ceil_areas[tzno]
            for floor in tz.floors:
                floor.area = floor_areas[tzno]
        zone_wall_area = 0
        for i, iw in enumerate(tz.inner_walls):
            print(f'inner wall {i}: area {iw.area} m²')
            zone_wall_area += iw.area
        for i, iw in enumerate(tz.floors):
            print(f'floor {i}: area {iw.area} m²')
            zone_wall_area += iw.area
        for i, iw in enumerate(tz.ceilings):
            print(f'ceiling {i}: area {iw.area} m²')
            zone_wall_area += iw.area
        print(f'total interior area for zone {tzno}: {zone_wall_area} m²')

    # for this specific application, we want to simulate the temperature in an
    # unoccupied building which was actually measured during a period in
    # February 2019. This is why the following steps are taken:

    # 1. the soil temperature is set to the temperature measured on the contact
    #    surface between building element and soil
    prj.t_soil_mode = 3
    prj.t_soil_file_path = utilities.get_full_path(
        "data/input/inputdata/weatherdata/t_soil_example_e10.txt"
    )

    # 2. the weather is set to the actual weather at the time
    prj.weather_file_path = utilities.get_full_path(
        "data/input/inputdata/weatherdata/DEU_NW_Morschenich_for_example_e10.mos"
    )

    # 3. we restrict the simulation time to the interesting part of the year
    #    (but leave enough time for the model reaching a steady state before
    #    the measurement starts)
    prj.modelica_info.start_time = 1497600
    prj.modelica_info.stop_time = 5155200

    # 4. we make sure that heaters, coolers, internal gains and automatical
    #    shading do not influence the calculation
    for tz in prj.buildings[0].thermal_zones:
        tz.use_conditions.cooling_profile = 373.15
        tz.use_conditions.heating_profile = 253.15
        tz.use_conditions.lighting_profile = 0
        tz.use_conditions.machines_profile = 0
        tz.use_conditions.persons_profile = 0
        # set the maximum irradiation (above which shading is automatically
        # applied in the simulation) to an unreachable number
        for el in tz.windows:
            el.shading_max_irr = 10000

    # for the calculation, we choose number of elements 5 and library AixLib
    for building in prj.buildings:
        building.calc_building_parameter(
            number_of_elements=5,
            used_library="AixLib"
        )

    # now, we do not want to use the default Multizone template, but a custom
    # template. It has two important features:
    # 1. the Medium DryAirNasa is used because the default SimpleAir cannot
    #    handle interior temperatures below 0 °C, but those will be present in
    #    the unheated attic here
    # 2. additional internal gains are connected to the ports of the Multizone
    export_path = prj.export_aixlib(
        custom_multizone_template_path=utilities.get_full_path(
            "examples/examplefiles/e10_Multizone_template"
        )
    )
    # the additional import source files need to be copied to the export path
    shutil.copyfile(
        utilities.get_full_path("examples/examplefiles/e10_AddIntGains.txt"),
        os.path.join(export_path, prj.buildings[0].name, "e10_AddIntGains.txt")
    )
