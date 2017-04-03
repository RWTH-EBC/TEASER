# created June 2015
# by TEASER4 Development Team


from teaser.logic.buildingobjects.building import Building


class NonResidential(Building):
    """Base class for each non-residential archetype.

    This is the base class for all non-residential archetype buildings (BMVBS,
    UrbanReNet, Tabula, etc.). It is a subclass of Building and introduces
    several parameters to be obligatory (parent, name, year_of_construction,
    net_leased_area).

    Please use this class to create new archetype methodologies.

    Parameters
    ----------

    parent: Project()
        The parent class of this object, the Project the Building belongs to.
        Allows for better control of hierarchical structures. If not None it
        adds this Building instance to Project.buildings.
        (default: None)
    name : str
        Individual name
    year_of_construction : int
        Year of first construction
    net_leased_area : float [m2]
        Total net leased area of building. This is area is NOT the footprint
        of a building
    with_ahu : Boolean
        If set to True, an empty instance of BuildingAHU is instantiated and
        assigned to attribute central_ahu. This instance holds information for
        central Air Handling units. Default is False.

    Attributes
    ----------
    central_ahu : instance of BuildingAHU
        Teaser Instance of BuildingAHU if a central AHU is embedded into the
        building (currently mostly needed for AixLib simulation).
    number_of_floors : int
        number of floors above ground (default: None)
    height_of_floors : float [m]
        Average height of the floors (default: None)
    internal_id : float
        Random id for the distinction between different buildings.
    year_of_retrofit : int
        Year of last retrofit.
    type_of_building : string
        Type of a Building (e.g. Building (unspecified), Office etc.).
    building_id : None
        ID of building, can be set by the user to keep track of a building
        even outside of TEASER, e.g. in a simulation or in post-processing.
        This is not the same as internal_id, as internal_id is e.g. not
        exported to Modelica models!
    street_name : string
        Name of the street the building is located at. (optional)
    city : string
        Name of the city the building is located at. (optional)
    longitude : float [degree]
        Longitude of building location.
    latitude : float [degree]
        Latitude of building location.
    thermal_zones : list
        List with instances of ThermalZone(), that are located in this building.
    gml_surfaces : list
        List of all containing surfaces described by CityGML, the list
        should be filled with SurfaceGML class from Data.Input.citygml_input.
        This list is only used if this instance of a building was instantiated
        the CityGML Loader module.
    outer_area : dict [degree: m2]
        Dictionary with orientation as key and sum of outer wall areas of
        that direction as value.
    window_area : dict [degree: m2]
        Dictionary with orientation as key and sum of window areas of
        that direction as value.
    bldg_height : float [m]
        Total building height.
    volume : float [m3]
        Total volume of all thermal zones.
    sum_heat_load : float [W]
        Total heating load of all thermal zones.
    sum_cooling_load : float [W]
        Total heating load of all thermal zones. (currently not supported)
    number_of_elements_calc : int
        Number of elements that are used for thermal zone calculation in this
        building.
        1: OneElement
        2: TwoElement
        3: ThreeElement
        4: FourElement
    merge_windows_calc : boolean
        True for merging the windows into the outer wall's RC-combination,
        False for separate resistance for window, default is False
    used_library_calc : str
        'AixLib' for https://github.com/RWTH-EBC/AixLib
        'IBPSA' for https://github.com/ibpsa/modelica
    library_attr : Annex() or AixLib() instance
        Classes with specific functions and attributes for building models in
        IBPSA and AixLib. Python classes can be found in calculation package.

    """

    def __init__(
            self,
            parent,
            name,
            year_of_construction,
            net_leased_area,
            with_ahu=False):
        """Constructor of NonResidential archetype building
        """

        super(NonResidential, self).__init__(
            parent,
            name,
            year_of_construction,
            net_leased_area,
            with_ahu)

    def generate_archetype(self):
        """Generates an archetype building.

        If you want to define you own archetype methodology please use this
        function call to do so.

        """

        pass
