import os
import pickle

import read_results as res

if __name__ == '__main__':
    # set path to your workspace here
    workspace = os.path.join("D:\\", "tbl-cwe", "Simulationsstudie_06_21")
    print("Your workspace is set to: " + workspace)
    # print(workspace)

    load_pickle = os.path.join(workspace, "building_simulation_pickle.p")
    pickle_prj = pickle.load(open(load_pickle, "rb"))

    output_path = os.path.join(workspace, "calc_results")
    print("Your Calculation Results are stored in: " + output_path)
    # print(output_path)

    plot_path = os.path.join(workspace, "plots")
    print("Your Plots are stored in: " + plot_path)
    # print(plot_path)

    csv_results_path = os.path.join(workspace, "csv_results", )
    print("Your Plots are stored in: " + csv_results_path)

    print("##########")
    res.calc_results(
        buildings=pickle_prj.buildings,
        csv_path=csv_results_path,
        output_path=output_path,
        plot_path=plot_path)

    print("##########")
    res.plot_results(
        buildings=pickle_prj.buildings,
        csv_path=csv_results_path,
        output_path=plot_path)
