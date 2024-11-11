import itertools

from teaser.logic.buildingobjects.building import Building
import teaser.data.utilities as datahandling


def generate_buildings_for_all_element_combinations(
        project_add_building_function: callable,
        add_building_function_kwargs: dict,
        elements: list = None,
        retrofit_choices: list = None
):
    """
    Generate buildings for all possible combinations of
    retrofit statuses for specified building elements.

    This function creates multiple variations of a building based
    on different retrofit options for specified building elements.
    It's designed to work with TABULA archetypes.

    Parameters
    ----------
    project_add_building_function : callable
        Function to add a building to the project.
    add_building_function_kwargs : dict
        Keyword arguments for the add_building function.
    elements : list, optional
        List of building elements to consider for retrofit.
        Defaults to ['outer_walls', 'windows', 'rooftops', 'ground_floors'].
    retrofit_choices : list, optional
        List of retrofit options to consider.
        Defaults to ['standard', 'retrofit', 'adv_retrofit'].

    Returns
    -------
        list: A list of names of the generated buildings.

    Raises
    ------
        ValueError: If unsupported elements or retrofit choices are provided, or if the
                    construction data is not from TABULA DE or DK.

    Note
    ----
        This function only works with TABULA DE or DK construction data.
    """
    construction_data = datahandling.ConstructionData(
        add_building_function_kwargs["construction_data"]
    )
    if not construction_data.is_tabula_de() and not construction_data.is_tabula_dk():
        raise ValueError(
            "Given option to retrofit all combinations "
            "is only implemented for TABULA archetypes."
        )

    # Define mapping for later naming
    retrofit_dict = {'standard': 0, 'retrofit': 1, 'adv_retrofit': 2}
    possible_elements = ['outer_walls', 'windows', 'rooftops', "ground_floors"]

    if elements is None:
        elements = ['outer_walls', 'windows', 'rooftops', "ground_floors"]
    if retrofit_choices is None:
        retrofit_choices = list(retrofit_dict.keys())
    unsupported_elements = set(elements).difference(possible_elements)
    if unsupported_elements:
        raise ValueError(
            "The following elements are not supported: " + ", ".join(unsupported_elements)
        )
    unsupported_choices = set(retrofit_choices).difference(retrofit_dict.keys())
    if unsupported_choices:
        raise ValueError(
            "The following retrofit_choices are not supported: " + ", ".join(unsupported_choices)
        )

    # Generate all possible combinations of retrofit statuses for each element
    combinations = itertools.product(retrofit_choices, repeat=len(elements))

    # Create a list to store the resulting dictionaries
    combinations = [
        {
            element: status
            for element, status in zip(elements, combo)
        }
        for combo in combinations
    ]

    generated_building_names = []
    for element_retrofit_stats in combinations:
        # Code for retrofit status OiWiRiGi with i from 0 to 2
        retrofit_code = ''.join(
            f"{element[0]}{retrofit_dict[retrofit_option]}"
            for element, retrofit_option in element_retrofit_stats.items()
        )
        modified_function_kwargs = add_building_function_kwargs.copy()
        modified_function_kwargs["name"] += f"_{retrofit_code}"
        building = project_add_building_function(**modified_function_kwargs)
        component_based_retrofit(building=building, element_retrofit_stats=element_retrofit_stats)
        generated_building_names.append(modified_function_kwargs["name"])
    return generated_building_names


def component_based_retrofit(building: Building, element_retrofit_stats: dict):
    """
    Apply component-based retrofits to a building based on specified retrofit statuses.

    This function applies retrofits to specific building elements (e.g., walls, windows)
    based on the provided retrofit statuses.

    Parameters
    ----------
    building : Building
        The building object to be retrofitted.
    element_retrofit_stats : dict
        A dictionary specifying the retrofit status for each
        building element. Keys are element names (e.g., 'outer_walls'),
        and values are retrofit options (e.g., 'standard', 'retrofit').

    Note
    ----
        This function modifies the building object in-place.
        Only elements with 'standard' retrofit option are processed.
    """
    for zone in building.thermal_zones:
        for element, retrofit_option in element_retrofit_stats.items():
            if retrofit_option == "standard":
                continue
            for wall_count in getattr(zone, element):
                wall_count.load_type_element(
                    year=building.year_of_construction,
                    construction=wall_count.construction_data.replace(
                        "standard",
                        retrofit_option
                    )
                )
