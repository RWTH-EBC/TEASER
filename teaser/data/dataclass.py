"""This module holds file paths and bindings for json data."""
import os
import sys
import warnings

import teaser.logic.utilities as utils
import json
import collections

from teaser.data.utilities import ConstructionData
v = sys.version_info
if v >= (2, 7):
    try:
        FileNotFoundError
    except NameError:
        FileNotFoundError = IOError

class DataClass(object):
    """Class for JSON data.

    This class loads all JSON files with statistic or template data needed
    for statistical data enrichment.

    Parameters
    ----------
    construction_data : ConstructionData
        The prefix of this parameter indicates which statistical data about building
        elements should be used. Its type is the enum class ConstructionData.

    Attributes
    ----------
    element_bind : collections.OrderedDict
        Ordered dictionary of the TypeBuildingElements binding.
    path_tb : str
        Full path to TypeElements_IWU.json. Default is
        teaser/data/input/inputdata/TypeElements_IWU.json.
    material_bind : collections.OrderedDict
        Ordered dictionary of the Material binding.
    path_mat : str
        Full path to MaterialTemplates.json. Default is
        teaser/data/input/inputdata/MaterialTemplates.json.
    conditions_bind : collections.OrderedDict
        Ordered dictionary of the UseConditions binding.
    path_uc : str
        Full path to UseConditions.json. Default is
        teaser/data/input/inputdata/UseConditions.json

    """

    def __init__(self, construction_data: ConstructionData) -> object:
        """Construct DataClass."""
        self.element_bind = None
        if construction_data.is_iwu():
            self.path_tb = utils.get_full_path(
                "data/input/inputdata/TypeElements_IWU.json"
            )
            self.load_tb_binding()
        elif construction_data.is_tabula_de():
            self.path_tb = utils.get_full_path(
                os.path.join(
                    "data", "input", "inputdata", "TypeElements_TABULA_DE.json"
                )
            )
            self.load_tb_binding()
        elif construction_data.is_tabula_dk():
            self.path_tb = utils.get_full_path(
                os.path.join(
                    "data", "input", "inputdata", "TypeElements_TABULA_DK.json"
                )
            )
            self.load_tb_binding()
        elif construction_data.is_kfw():
            self.path_tb = utils.get_full_path(
                os.path.join(
                    "data", "input", "inputdata", "TypeElements_KFW.json"
                )
            )
            self.load_tb_binding()
        elif construction_data is None:
            pass
        self.material_bind = None
        self.path_mat = utils.get_full_path(
            "data/input/inputdata/MaterialTemplates.json"
        )
        self.conditions_bind = None
        self.path_uc = utils.get_full_path("data/input/inputdata/UseConditions.json")

        self.load_uc_binding()
        self.load_mat_binding()

    def load_tb_binding(self):
        """Load TypeBuildingElement json into binding classes."""
        if self.path_tb.endswith("json"):
            if os.path.isfile(self.path_tb):
                try:
                    with open(self.path_tb, "r") as f:
                        self.element_bind = json.load(
                            f, object_pairs_hook=collections.OrderedDict
                        )
                except json.decoder.JSONDecodeError:
                    print("Your TypeElements file seems to be broken.")
            else:
                with open(self.path_tb, "w") as f:
                    self.element_bind = collections.OrderedDict()

    def load_uc_binding(self):
        """Load UseConditions json into binding classes."""
        if self.path_uc.endswith("json"):
            if os.path.isfile(self.path_uc):
                try:
                    with open(self.path_uc, "r") as f:
                        self.conditions_bind = json.load(
                            f, object_pairs_hook=collections.OrderedDict
                        )
                except json.decoder.JSONDecodeError:
                    raise IOError("Your UseConditions.json file seems to be broken.")
            else:
                with open(self.path_uc, "w") as f:
                    self.conditions_bind = collections.OrderedDict()

    def load_mat_binding(self):
        """Load MaterialTemplates json into binding classes."""
        if self.path_mat.endswith("json"):
            if os.path.isfile(self.path_mat):
                try:
                    with open(self.path_mat, "r") as f:
                        self.material_bind = json.load(
                            f, object_pairs_hook=collections.OrderedDict
                        )
                except json.decoder.JSONDecodeError:
                    print("Your Materials file seems to be broken.")
            else:
                with open(self.path_mat, "w") as f:
                    self.material_bind = collections.OrderedDict()
