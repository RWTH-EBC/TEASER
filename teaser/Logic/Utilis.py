# created June 2015
# by TEASER4 Development Team

"""Utilis: Collection of all utility functions that are useful in several
classes
"""

import os


def celsius_to_kelvin(value):
    try:
        f_value = float(value)
    except TypeError:
        f_value = 0
    return f_value+273.15

def create_path(path):
    '''Create a folder.

    Creates a new folder.

    Parameters
    ----------
    path : str

    '''

    # if directory exists change into that directory
    if(os.path.isdir(path)):
        os.chdir(path)
        return path
    else:
        if not os.path.exists(path):
            l = []
            p = "\\"
            l = path.split("\\")
            i = 1
            while i < len(l):
                p = p + l[i] + "\\"
                i = i + 1
                if not os.path.exists(p):
                    os.mkdir(p)

        os.chdir(p)
    
    return p

def get_default_path():
    '''Function to construct default path to OutputData folder
    
    This function constructs the default path to the OutputData folder

    '''

    directory = os.path.dirname(__file__)
    src = "\\teaser"
    last_index = directory.rfind(src)
    default_path = directory[:last_index] + "\\teaser\\OutputData"

    return default_path


def get_full_path(rel_path):
    '''Helperfunction to construct pathes to files within teaser.

    Parameters
    ----------
    rel_path : str
        Relative path beginning from teaser source folder including
        filename

    Returns
    ----------
    full_path : str

    '''

    directory = os.path.dirname(__file__)
    src = "\\teaser"
    last_index = directory.rfind(src)
    first_path = directory[:last_index]+"\\teaser\\"
    full_path = os.path.join(first_path, rel_path)

    return full_path