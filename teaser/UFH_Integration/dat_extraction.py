import math
import pathlib
import numpy as np
import matplotlib.pyplot as plt
from ebcpy import TimeSeriesData
from os import walk
import pandas as pd

def is_float(string):
    """ True if given string is float else False"""
    try:
        return float(string)
    except ValueError:
        return False

def main(with_plot=True):
    basepath = pathlib.Path(__file__).parents[4].joinpath("Dymola_results")
    result_files = next(walk(basepath))[2]
    for result_file in result_files:
        if result_file.endswith('.csv'):
            path = basepath.joinpath(result_file)
            with open(path, 'r') as f:
                df = pd.read_csv(f, sep=';')
                print()

    pass


if __name__ == '__main__':
    main()
