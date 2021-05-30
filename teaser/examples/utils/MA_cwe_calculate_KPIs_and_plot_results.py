# Specify path to your simulation workspace
import os
import datetime
import read_results as res
import pandas as pd
from teaser.project import Project
import pickle

if __name__ == '__main__':

    workspace = os.path.join("D:\\", "tbl-cwe", "Simulationsstudie_06_21")
    print("Your workspace is set to: ")
    print(workspace)

    load_pickle = os.path.join(workspace, "building_simulation_pickle.p")

    pickle_prj = pickle.load(open(load_pickle, "rb"))
    print(pickle_prj)

    output_path = os.path.join(workspace, "calc_results")
    print("Your Calculation Results are stored in: ")
    print(output_path)

    plot_path = os.path.join(workspace, "plots")
    print("Your Plots are stored in: ")
    print(plot_path)
    print("##########")
    #for bldg in pickle_prj.buildings:
    res.calc_results(
        buildings=pickle_prj.buildings,
        csv_path=os.path.join(workspace, "csv_results",),
        output_path=os.path.join(output_path),
        plot_path=os.path.join(plot_path))

    print("##########")
    res.plot_results(
        buildings=pickle_prj.buildings,
        csv_path=os.path.join(workspace, "csv_results",),
        output_path=os.path.join(plot_path))