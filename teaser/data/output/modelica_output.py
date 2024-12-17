"""This module contains functions for all modelica model generations with AixLib, IBPSA and BESMod"""

import os
import shutil
from mako.template import Template
import teaser.logic.utilities as utilities


def create_package(path, name, uses=None, within=None):
    """creates a package.mo file

    private function, do not call

    Parameters
    ----------

    path : string
        path of where the package.mo should be placed
    name : string
        name of the Modelica package
    uses : [string]
        list of used versions for the package in the form 'Library_name(version="x.x.x")'
    within : string
        path of Modelica package containing this package

    """

    package_template = Template(filename=utilities.get_full_path(
        "data/output/modelicatemplate/package"))
    with open(utilities.get_full_path(os.path.join(
            path, "package.mo")), 'w') as out_file:

        out_file.write(package_template.render_unicode(
            name=name,
            within=within,
            uses=uses))
        out_file.close()


def create_package_order(path, package_list, addition=None, extra=None):
    """creates a package.order file

    private function, do not call

    Parameters
    ----------

    path : string
        path of where the package.order should be placed
    package_list : [buildings or thermal_zones]
        objects with the attribute name of all models or packages contained in the package
    addition : string
        if there should be a prefix of package_list.string it can
        be specified
    extra : [string]
        list of extra packages or models not contained in package_list can be
        specified

    """

    order_template = Template(filename=utilities.get_full_path(
        "data/output/modelicatemplate/package_order"))
    with open(utilities.get_full_path(
            path + "/" + "package" + ".order"), 'w') as out_file:

        out_file.write(order_template.render_unicode
                       (list=package_list, addition=addition, extra=extra))
        out_file.close()


def copy_weather_data(source_path, destination_path):
    """Copies the imported .mos weather file to the results folder.

    Parameters
    ----------
    source_path : str
        path of local weather file
    destination_path : str
        path of where the weather file should be placed
    """

    shutil.copy2(source_path, destination_path)
