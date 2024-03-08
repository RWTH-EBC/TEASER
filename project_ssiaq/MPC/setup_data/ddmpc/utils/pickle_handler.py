import pickle
import os
from pathlib import Path
from typing import Union


def read_pkl(filename: str, directory: Union[str, Path] = None):
    """
    Reads data from a pickle file.
    :param filename: The name of the file.
    :param directory: The directory the file is located.
    :return: Pickle object.
    """

    path: Path = _get_path(filename, directory)

    if path.exists():
        pkl_file = open(path, 'rb')
        pkl_data = pickle.load(pkl_file)
        pkl_file.close()

        if pkl_data is None:
            raise FileNotFoundError(f'No data at {path} found.')

        return pkl_data

    else:
        raise FileNotFoundError(f'The path {path} does not exist.')


def write_pkl(data, filename: str, directory: str = None, override: bool = False):
    """
    Writes data to a pickle file.
    :param data: The object that is supposed to be saved.
    :param filename: The name of the file.
    :param directory: The directory the file will be saved to.
    :param override: Boolean.
    """

    path: Path = _get_path(filename, directory)

    # make sure the directory does exist
    if directory is not None:
        if not os.path.exists(directory):
            os.mkdir(directory)

    # make sure the file does not already exist
    if os.path.exists(path) and not override:
        if not _get_bool(f'The file "{path}" already exists. Do you want to override it?\n'):
            return 0

    # open the path and writhe the file
    pkl_file = open(path, 'wb')
    pickle.dump(data, pkl_file)

    # close file
    pkl_file.close()


def _get_path(filename: Union[str, Path], directory: Union[str, None, Path]) -> Path:
    """
    Returns the full path for a given filename and directory.
    """

    if not str(filename).endswith('.pkl'):
        filename = str(filename) + '.pkl'

    if directory is None:
        return Path(filename)

    if isinstance(directory, str):
        directory = Path(directory)

    return Path(directory, filename)


def _get_bool(message: str, true: list = None, false: list = None):

    if false is None:
        false = ['no', 'nein', 'false', '1', 'n']
    if true is None:
        true = ['yes', 'ja', 'true', 'wahr', '0', 'y']

    val = input(message).lower()
    if val in true:
        return True
    elif val in false:
        return False
    else:
        print('Please try again.')
        print('True:', true)
        print('False:', false)
        _get_bool(message, true, false)

    return val
