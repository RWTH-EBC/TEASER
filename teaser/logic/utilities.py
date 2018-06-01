# created June 2015
# by TEASER4 Development Team

"""Utilis: Collection of all utility functions that are useful in several
classes
"""

import os
import shutil


def celsius_to_kelvin(value):
    try:
        f_value = float(value)
    except TypeError:
        f_value = 0
    return f_value + 273.15


def create_path(path):
    """Create a folder.

    Creates a new folder.

    Parameters
    ----------
    path : str

    """
    path = os.path.normpath(path)
    # if directory exists change into that directory
    if(os.path.isdir(path)):
        os.chdir(path)
        return path
    else:
        if not os.path.exists(path):
            os.makedirs(path)

        os.chdir(path)
    return path


def get_default_path():
    """Function to construct default path to OutputData folder
    This function constructs the default path to the OutputData folder

    """

    home_path = os.path.expanduser('~')

    teaser_default_path = os.path.join(home_path, 'TEASEROutput')

    # directory = os.path.dirname(__file__)
    # src = "teaser"
    # last_index = directory.rfind(src)
    # teaser_default_path = os.path.join(directory[:last_index], "teaser",
    # "OutputData")

    return teaser_default_path


def get_full_path(rel_path):
    """Helperfunction to construct pathes to files within teaser.

    Parameters
    ----------
    rel_path : str
        Relative path beginning from teaser source folder including
        filename

    Returns
    ----------
    full_path : str

    """

    directory = os.path.dirname(__file__)
    src = "teaser"
    last_index = directory.rfind(src)
    first_path = os.path.join(directory[:last_index], "teaser")
    full_path = os.path.join(first_path, rel_path)

    return full_path


def clear_directory(dir_path=None):
    """Function to delete all files inside a directory.

    Parameters
    ----------
    dir_path : str
        Path of directory to be deleted. By default the teaser default
        directory is cleared

    """

    if dir_path is None:
        dir_path = get_default_path()
    else:
        pass

    if os.path.exists(dir_path):
        for file in os.listdir(path=dir_path):
            file_path = os.path.join(dir_path, file)
            if os.path.isfile(file_path):
                os.remove(os.path.join(dir_path, file))
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
    else:
        print('The directory path does not exist.')
