import multiprocessing
import os
import pickle
import pandas as pd
import datetime
import timing

"""
Use this script to create heating and cooling demand tables for DHC network simulations.
1. Set your workspace 
"""

if __name__ == '__main__':
    timing
    # set your workspace to your desired path here
    workspace = os.path.join("D:\\", "tbl-cwe", "Final_Simulations", "Complete_04_08")
    sim_results_path = os.path.join(workspace, "sim_results")
    TEASER_output_path = os.path.join(workspace, "TEASEROutput")

    load_pickle = os.path.join(workspace, "building_simulation_pickle.p")
    pickle_prj = pickle.load(open(load_pickle, "rb"))

    sim_results_path = os.path.join(workspace, "sim_results", pickle_prj.name)
    print("Your Dymola Results are stored in: " + sim_results_path)

    csv_results_path = os.path.join(workspace, "csv_results")
    print("Your .csv files are stored in: " + csv_results_path)
    print("##########")

    dhc_demands_path = os.path.join(csv_results_path, "dhc_demand_tables")
    print("Your dhc_demand tables are stored in: " + dhc_demands_path)
    print("##########")

    if not os.path.exists(dhc_demands_path):
        os.makedirs(dhc_demands_path)

    print("Creating demand tables")

    for bldg in pickle_prj.buildings:
        try:
            ma = pd.DataFrame()
            co = pd.DataFrame()
            ma_bldg = pd.DataFrame()
            co_bldg = pd.DataFrame()
            ma = pd.read_csv(os.path.join(csv_results_path, bldg.name + "_heat.csv"))
            co = pd.read_csv(os.path.join(csv_results_path, bldg.name + "_cool.csv"))

            i = 0
            # for comma delimiter choose sep=',' for tab delimiter choose '/t'
            for column in ma.columns[1:]:
                ma.to_csv(os.path.join(dhc_demands_path, column + "_ma.txt"), sep='/t')
                ma.index = [i * 3600 for i in range(8760)]
                ma_bldg = ma[column]

                # ma_bldg = ma_bldg.drop(ma_bldg.index[0:24])
                ma_bldg.to_csv(os.path.join(dhc_demands_path, column + "_ma.txt"), header=False, sep='/t')

                with open(os.path.join(dhc_demands_path, column + "_ma.txt")) as f:
                    lines = f.readlines()

                lines.insert(0, "#1\n")
                lines.insert(1, 'double heatDemand(8760,2)\n')
                # lines.insert(1, 'double heat(8736,2)\n')

                with open(os.path.join(dhc_demands_path, column + "_ma.txt"), "w") as f:
                    f.writelines(lines)

                f.close()

            for column in co.columns[1:]:
                co.to_csv(os.path.join(dhc_demands_path, column + "_co.txt"), sep='/t')
                co.index = [i * 3600 for i in range(8760)]
                co_bldg = co[column]

                # ma_bldg = ma_bldg.drop(ma_bldg.index[0:24])
                co_bldg.to_csv(os.path.join(dhc_demands_path, column + "_co.txt"), header=False, sep='/t')

                with open(os.path.join(dhc_demands_path, column + "_co.txt")) as f:
                    lines = f.readlines()

                lines.insert(0, "#1\n")
                lines.insert(1, 'double coolingDemand(8760,2)\n')
                # lines.insert(1, 'double heat(8736,2)\n')

                with open(os.path.join(dhc_demands_path, column + "_co.txt"), "w") as f:
                    f.writelines(lines)

                f.close()

        except BaseException:
            # Dymola has strange exceptions
            print(
                "Reading results of building {} failed, "
                "please check result file".format(bldg)
            )
            # raise Exception("Results Error!")
            continue

