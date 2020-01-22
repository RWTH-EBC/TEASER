"""This module includes AixLib calculation class."""

import teaser.logic.utilities as utilities
from itertools import cycle, islice
import os
import pandas as pd


class AixLib(object):
    """Class to calculate parameters for AixLib output.

    This class holds functions to sort and partly rewrite zone and building
    attributes specific for AixLib MultizoneEquipped
    simulation. This includes the export of boundary conditions and AHU
    operation values.

    Parameters
    ----------
    parent: Building()
        The parent class of this object, the Building the attributes are
        calculated for. (default: None)


    Attributes
    ----------
    file_set_t : str
        Filename for set temperature file
    file_ahu : str
        Filename for AHU boundary conditions file
    file_internal_gains : str
        Filename for internal gains file
    version : str
        Used AixLib version, default should always be current master version
        of GitHub
    total_surface_area : float [m2]
        This is the total surface area of the building for interior and
        exterior surfaces. That includes: OuterWalls, Rooftops, GroundFloors,
        Windows for exterior surfaces, and InnerWalls, Ceilings, Floors for
        interior walls.
    consider_heat_capacity : bool
        decides whether air capacity is considered or not for all thermal
        zones in the building. Default is True, you need to export your
        model again if changing this value
    use_set_back : bool
        True if night set back should be used. In this case the function
        considers heating_time and temp_set_back defined in
        use_conditions of zone. Default is True, you need to export your
        model again if changing this value
    use_set_point_temperature_profile_heating : bool
        Standard is False. True if the set_point temperature profile heating
        should be used for the export. Then, the night set back and everything
        except the set point profile will be ignored.

    """

    def __init__(self, parent):
        """Construct AixLib."""
        self.parent = parent

        self.file_set_t_heat = "TsetHeat_" + self.parent.name + ".txt"
        self.file_set_t_cool = "TsetCool_" + self.parent.name + ".txt"
        self.file_ahu = "AHU_" + self.parent.name + ".txt"
        self.file_internal_gains = "InternalGains_" + self.parent.name + ".txt"
        self.version = "0.9.1"
        self.total_surface_area = None
        self.consider_heat_capacity = True
        self.use_set_back = True
        self.use_set_point_temperature_profile_heating = False
        self.use_set_back_cool = False

    def calc_auxiliary_attr(self):
        """Call function to calculate all auxiliary attributes for AixLib."""
        self._calc_surface_area()

    def _calc_surface_area(self):
        """Calculate the total surface area of all surfaces."""
        surf_area_temp = 0.0
        for zone in self.parent.thermal_zones:
            if type(zone.model_attr).__name__ == "OneElement":
                surf_area_temp += zone.model_attr.area_ow + zone.model_attr.area_win
            elif type(zone.model_attr).__name__ == "TwoElement":
                surf_area_temp += (
                    zone.model_attr.area_ow
                    + zone.model_attr.area_iw
                    + zone.model_attr.area_win
                )
            elif type(zone.model_attr).__name__ == "ThreeElement":
                surf_area_temp += (
                    zone.model_attr.area_ow
                    + zone.model_attr.area_iw
                    + zone.model_attr.area_gf
                    + zone.model_attr.area_win
                )
            elif type(zone.model_attr).__name__ == "FourElement":
                surf_area_temp += (
                    zone.model_attr.area_ow
                    + zone.model_attr.area_iw
                    + zone.model_attr.area_gf
                    + zone.model_attr.area_rt
                    + zone.model_attr.area_win
                )

        self.total_surface_area = surf_area_temp

    def modelica_set_temp(self, path=None):
        """Create .txt file for set temperatures for heating.

        This function creates a txt for set temperatures of each
        zone, that are all saved into one matrix.

        Parameters
        ----------
        path : str
            optional path, when matfile is exported separately

        """
        if path is None:
            path = utilities.get_default_path()
        else:
            pass

        utilities.create_path(path)
        path = os.path.join(path, self.file_set_t_heat)

        export = pd.DataFrame(
            index=pd.date_range("2019-01-01 00:00:00", periods=8760, freq="H")
            .to_series()
            .dt.strftime("%m-%d %H:%M:%S"),
            columns=[zone.name for zone in self.parent.thermal_zones],
        )

        for zone_count in self.parent.thermal_zones:
            export[zone_count.name] = zone_count.use_conditions.schedules[
                "heating_profile"
            ]

        export.index = [(i + 1) * 3600 for i in range(8760)]
        self._delete_file(path=path)
        with open(path, "a") as f:
            f.write("#1\n")
            f.write(
                "double Tset({}, {})\n".format(8760, len(self.parent.thermal_zones) + 1)
            )
            export.to_csv(f, sep="\t", header=False, index_label=False)

    def modelica_set_temp_cool(self, path=None):
        """Create .txt file for set temperatures cooling.

        This function creates a txt for set temperatures for cooling
        of each zone, that are all saved into one matrix.


        Parameters
        ----------
        path : str
            optional path, when matfile is exported separately

        """
        if path is None:
            path = utilities.get_default_path()
        else:
            pass

        utilities.create_path(path)
        path = os.path.join(path, self.file_set_t_cool)

        export = pd.DataFrame(
            index=pd.date_range("2019-01-01 00:00:00", periods=8760, freq="H")
            .to_series()
            .dt.strftime("%m-%d %H:%M:%S"),
            columns=[zone.name for zone in self.parent.thermal_zones],
        )

        for zone_count in self.parent.thermal_zones:
            export[zone_count.name] = zone_count.use_conditions.schedules[
                "cooling_profile"
            ]

        export.index = [(i + 1) * 3600 for i in range(8760)]
        self._delete_file(path=path)
        with open(path, "a") as f:
            f.write("#1\n")
            f.write(
                "double Tset({}, {})\n".format(8760, len(self.parent.thermal_zones) + 1)
            )
            export.to_csv(f, sep="\t", header=False, index_label=False)

    def modelica_AHU_boundary(self, path=None):
        """Create .txt file for AHU boundary conditions (building).

        This function creates a txt for building AHU boundary
        conditions

        1. Column : time step
        2. Column : desired AHU profile temperature
        3. Column : Desired minimal relative humidity
        4. Column : desired maximal relative humidity
        5. Column : AHU status (On/Off)

        Parameters
        ----------
        path : str
            optional path, when matfile is exported separately

        Attributes
        ----------
        temperature_profile : [float]
            timeline of temperatures requirements for AHU simulation
        min_relative_humidity_profile : [float]
            timeline of relative humidity requirements for AHU simulation
        max_relative_humidity_profile : [float]
            timeline of relative humidity requirements for AHU simulation
        v_flow_profile : [int]
            timeline of desired relative v_flow of the AHU simulation (0..1)

        """
        if path is None:
            path = utilities.get_default_path()
        else:
            pass

        utilities.create_path(path)
        path = os.path.join(path, self.file_ahu)

        if self.parent.with_ahu is True:
            export = self.parent.central_ahu.schedules
        else:  # Dummy values for Input Table
            export = pd.DataFrame(
                index=pd.date_range("2019-01-01 00:00:00", periods=8760, freq="H")
                .to_series()
                .dt.strftime("%m-%d %H:%M:%S")
            )

            export["temperature_profile"] = list(islice(cycle([293.15, 293.15]), 8760))
            export["min_relative_humidity_profile"] = list(islice(cycle([0, 0]), 8760))
            export["max_relative_humidity_profile"] = list(islice(cycle([1, 1]), 8760))
            export["v_flow_profile"] = list(islice(cycle([0, 1]), 8760))

        export.index = [(i + 1) * 3600 for i in range(8760)]
        self._delete_file(path=path)
        with open(path, "a") as f:
            f.write("#1\n")
            f.write("double AHU({}, {})\n".format(8760, 5))
            export.to_csv(f, sep="\t", header=False, index_label=False)

    def modelica_gains_boundary(self, path=None):
        """Create .txt file for internal gains boundary conditions.

        This function creates a matfile (-v4) for building internal gains
        boundary conditions. It collects all internal gain profiles of the
        zones and stores them into one file. The file is extended for each
        zone. Only applicable if zones are defined

        1. Column : time step
        2,5,8,...  Column : profile_persons
        3,6,9,...  Column : profile_machines
        4,7,10,... Column : profile_lighting

        Note
        ----------
        When time line is created, we need to add a 0 to first element of
        all boundaries. This is due to to expected format in Modelica.

        Parameters
        ----------
        path : str
            optional path, when matfile is exported separately

        """
        if path is None:
            path = utilities.get_default_path()
        else:
            pass

        utilities.create_path(path)
        path = os.path.join(path, self.file_internal_gains)

        export = pd.DataFrame(
            index=pd.date_range("2019-01-01 00:00:00", periods=8760, freq="H")
            .to_series()
            .dt.strftime("%m-%d %H:%M:%S")
        )

        for zone_count in self.parent.thermal_zones:
            export[
                "person_{}".format(zone_count.name)
            ] = zone_count.use_conditions.schedules["persons_profile"]
            export[
                "machines_{}".format(zone_count.name)
            ] = zone_count.use_conditions.schedules["machines_profile"]
            export[
                "lighting_{}".format(zone_count.name)
            ] = zone_count.use_conditions.schedules["lighting_profile"]

        export.index = [(i + 1) * 3600 for i in range(8760)]
        self._delete_file(path=path)
        with open(path, "a") as f:
            f.write("#1\n")
            f.write(
                "double Internals({}, {})\n".format(
                    8760, (len(self.parent.thermal_zones) * 3 + 1)
                )
            )
            export.to_csv(f, sep="\t", header=False, index_label=False)

    def _delete_file(self, path):
        """Delete a file before new information is written to it.

        If a building with the exact name and project name is generated, we need to make
        sure to delete the old information in the text files. This helper function is a
        wrapper to delete a file with given filepath.

        Parameters:
        -----------
        path : str
            Absolute path to the file to be deleted.

        """
        try:
            os.remove(path)
        except OSError:
            pass
