"""This module contains function to load building element classes."""

from teaser.logic.buildingobjects.buildingphysics.layer import Layer
from teaser.logic.buildingobjects.buildingphysics.material import Material
import teaser.data.input.material_input_json as mat_input
import logging

def load_type_element(element, year, construction, data_class,
                      element_type=None, reverse_layers=False):
    """Load BuildingElement from json.

    Loads typical building elements according to their construction year and
    their construction type from a JSON. The elements are created by using
    building characteristics from
    cite:`BundesministeriumfurVerkehrBauundStadtentwicklung.26.07.2007` and
    :cite:`KurzverfahrenIWU`, which is combined with normative material data
    from :cite:`VereinDeutscherIngenieure.2012b`.

    Most of the elements for the KfW Efficiency House standards (TypeElements_KFW.json) were derived from the respective
    required U-value and the component catalog of the U-value online calculator https://www.ubakus.de/bauteilkatalog/.
    For the respective source of each element, the comment in the json file can be observed.

    Parameters
    ----------
    element : BuildingElement()
        Instance of BuildingElement or inherited Element of TEASER

    year : int
        Year of construction

    construction : str
        Construction type, code list ('iwu_heavy', 'iwu_light', 'tabula_de_standard', 'kfw_40', ...)

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.

    element_type : str
        Element type to load - only to specify if the data_class entry for a
        different type than type(element) is to be loaded, e.g. InnerWall
        instead of OuterWall

    reverse_layers : bool
        defines if layer list should be reversed - this is necessary for zone
        borders to maintain consistency

    """
    element_binding = data_class.element_bind

    if element_type is None:
        element_type = type(element).__name__

    for key, element_in in element_binding.items():
        if (
            element_in["building_age_group"][0]
            <= year
            <= element_in["building_age_group"][1]
            and element_in["construction_data"] == construction
            and key.startswith(element_type)
        ):
            _set_basic_data(element=element, element_in=element_in)
            for id, layer_in in (
                        element_in["layer"].items().__reversed__()
                        if reverse_layers else element_in["layer"].items()
                ):
                layer = Layer(element)
                layer.id = id
                layer.thickness = layer_in["thickness"]
                material = Material(layer)
                mat_input.load_material_id(
                    material, layer_in["material"]["material_id"], data_class
                )
            return
    logging.warning(f"No database entry found for construction={construction}, "
                    f"year{year}, element={type(element).__name__}")


def load_type_element_by_key(element, key_str, data_class,
                             reverse_layers=False):
    """Load BuildingElement from json by key string.

    Loads typical building elements according to their key string from a JSON.
    The elements are created by using building characteristics from
    cite:`BundesministeriumfurVerkehrBauundStadtentwicklung.26.07.2007` and
    :cite:`KurzverfahrenIWU`, which is combined with normative material data
    from :cite:`VereinDeutscherIngenieure.2012b`.

    Parameters
    ----------
    element : BuildingElement()
        Instance of BuildingElement or inherited Element of TEASER

    key_str : str
        key string to the type element of the building characteristics sources

    data_class : DataClass()
        DataClass containing the bindings for TypeBuildingElement and
        Material (typically this is the data class stored in prj.data,
        but the user can individually change that.

    reverse_layers : bool
        defines if layer list should be reversed

    """
    element_binding = data_class.element_bind

    element_in = element_binding[key_str]

    _set_basic_data(element=element, element_in=element_in)
    for id, layer_in in (
            element_in["layer"].items().__reversed__()
            if reverse_layers else element_in["layer"].items()
    ):
        layer = Layer(element)
        layer.id = id
        layer.thickness = layer_in["thickness"]
        material = Material(layer)
        mat_input.load_material_id(
            material, layer_in["material"]["material_id"], data_class
        )


def _set_basic_data(element, element_in):
    """Set basic data for building elements.

    Helper function to set basic data to the BuildingElement class.

    Parameters
    ----------
    element : BuildingElement
        BuildingElement
    element_in :
        json string of input data

    """
    element.building_age_group = element_in["building_age_group"]
    element.construction_data = element_in["construction_data"]
    element.inner_radiation = element_in["inner_radiation"]
    element.inner_convection = element_in["inner_convection"]

    if (
        type(element).__name__ == "OuterWall"
        or type(element).__name__ == "Rooftop"
        or type(element).__name__ == "Door"
    ):
        element.outer_radiation = element_in["outer_radiation"]
        element.outer_convection = element_in["outer_convection"]

    elif type(element).__name__ == "Window":
        element.outer_radiation = element_in["outer_radiation"]
        element.outer_convection = element_in["outer_convection"]
        element.g_value = element_in["g_value"]
        element.a_conv = element_in["a_conv"]
        element.shading_g_total = element_in["shading_g_total"]
        element.shading_max_irr = element_in["shading_max_irr"]

    if type(element).__name__.startswith("Interzonal"):
        element.outer_radiation = element_in["inner_radiation"]
        element.outer_convection = element_in["inner_convection"]
