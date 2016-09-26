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
    '''Function to construct default path to OutputData folder
    This function constructs the default path to the OutputData folder

    '''

    home_path = os.path.expanduser('~')

    teaser_default_path = os.path.join(home_path, 'TEASEROutput')

    # directory = os.path.dirname(__file__)
    # src = "teaser"
    # last_index = directory.rfind(src)
    # teaser_default_path = os.path.join(directory[:last_index], "teaser", "OutputData")

    return teaser_default_path


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
    src = "teaser"
    last_index = directory.rfind(src)
    first_path = os.path.join(directory[:last_index], "teaser")
    full_path = os.path.join(first_path, rel_path)

    return full_path


def clean_path(rel_path):
    "Helperfunction which replaces all \ with / in a path"

    new_path = ""
    for index in rel_path:
        # 92 is the asci code for \
        if index == "\t":
            new_path += "/t"
        elif index == "\b":
            new_path += "/b"
        elif index == "\n":
            new_path += "/n"
        elif index == "\a":
            new_path += "/a"
        elif index == "\r":
            new_path += "/r"
        elif index == chr(92):
            new_path += "/"
        else:
            new_path += index
    return new_path


def split_path(path):

    path = clean_path(path)
    count = 0
    for index in path:
        if index == "/":
            count += 1

    head = ""
    tail = ""
    count2 = 0
    for index in path:
        if index == "/":
            count2 += 1
        if count2 < count:
            head += index
        elif count2 >= count:
            tail += index

    tailList = tail.split(sep="/")
    tail = tailList[1]
    tailList = tail.split(sep=".")
    tail = tailList[0]

    return head, tail
