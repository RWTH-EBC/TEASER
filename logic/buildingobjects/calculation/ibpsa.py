"""This module includes IBPSA calculation class."""

import os
import pandas as pd
import teaser.logic.utilities as utilities


class IBPSA(object):
    """Class to calculate parameters for AixLib output.

    This class holds functions to sort and partly rewrite zone and building
    attributes specific for IBPSA simulation. This includes the export of
    boundary conditions.

    Parameters
    ----------
    parent: Building()
        The parent class of this object, the Building the attributes are
        calculated for. (default: None)

    Attributes
    ----------
    file_internal_gains : str
        Filename for internal gains file
    version : dict
        Dictionary with supported libraries and their version numbers
    consider_heat_capacity : bool
        decides whether air capacity is considered or not for all thermal
        zones in the building


    """

    def __init__(self, parent):
        """Construct IBPSA."""
        self.parent = parent
        self.file_internal_gains = "InternalGains_" + self.parent.name + ".mat"
        self.version = {
            "AixLib": "0.9.1",
            "Buildings": "6.0.0",
            "BuildingSystems": "2.0.0-beta2",
            "IDEAS": "2.1.0",
        }
        self.consider_heat_capacity = True

    def modelica_gains_boundary(self, zone, path=None):
        """creates .mat file for internal gains boundary conditions

        This function creates a matfile (-v4) for building internal gains
        boundary conditions. It collects internal gain profiles of a specific
        zones and stores them into one file. It also calculates the internal
        gains from relative presence and values for heat output into W for
        direct usage in Annex models.

        Only person (convective and radiative) and machines (convective) are
        used in the simple Annex 60 examples.

        1. Column : time step
        2 Column : profile_persons, radiative
        3 Column : profile_persons, convective
        4 Column : profile_machines, convective

        Note
        ----------
        When time line is created, we need to add a 0 to first element of
        all boundaries. This is due to to expected format in Modelica.

        Parameters
        ----------
        zone : ThermalZone()
            TEASER instance of ThermalZone. As IBPSA computes single models
            for single zones, we need to generate individual files for zones
            and internal gains
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

        export["person_rad_{}".format(zone.name)] = (
            zone.use_conditions.schedules["persons_profile"]
            * (1 - zone.use_conditions.ratio_conv_rad_persons)
            * zone.use_conditions.fixed_heat_flow_rate_persons
            * zone.use_conditions.persons
            * zone.area
        )
        export["person_conv_{}".format(zone.name)] = (
            zone.use_conditions.schedules["persons_profile"]
            * zone.use_conditions.ratio_conv_rad_persons
            * zone.use_conditions.fixed_heat_flow_rate_persons
            * zone.use_conditions.persons
            * zone.area
        )
        export["machines_conv_{}".format(zone.name)] = (
            zone.use_conditions.schedules["machines_profile"]
            * zone.use_conditions.ratio_conv_rad_machines
            * zone.use_conditions.machines
            * zone.area
        )

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
