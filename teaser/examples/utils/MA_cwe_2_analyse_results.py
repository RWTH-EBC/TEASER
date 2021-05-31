import os
import datetime
import read_results as res
import pandas as pd
import pickle

if __name__ == '__main__':

    # set path to your workspace here
    workspace = os.path.join("D:\\", "tbl-cwe", "Simulationsstudie_06_21_V2")
    print("Your workspace is set to: " + workspace)

    """
    # Specify the signals you want to read i.e. Modelica naming of parameters PHeater and
    # PCooler for three thermal zones
    # Example:
    #
    # signals = [
    #    "multizoneSimpleHRS.PHeater[{}]".format(i + 1)
    #    for i in range(0,3)
    # ]
    # signals += [
    #    "multizoneSimpleHRS.PCooler[{}]".format(i + 1)
    #    for i in range(len(bldg.thermal_zones))
    #  ]
    """

    load_pickle = os.path.join(workspace, "building_simulation_pickle.p")
    pickle_prj = pickle.load(open(load_pickle, "rb"))

    sim_results_path = os.path.join(workspace, "sim_results", pickle_prj.name)
    print("Your Dymola Results are stored in: " + sim_results_path)

    csv_results_path = os.path.join(workspace, "csv_results")
    print("Your .csv files are stored in: " + csv_results_path)
    print("##########")

    for bldg in pickle_prj.buildings:
        if "panel" in bldg.name:
            signals = ['multizone.TOpe[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TAir[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempHeatPanel.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempCoolPanel.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.PCooler[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]

            res.read_results(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )
        elif "tabsplusair" in bldg.name:
            signals = ['multizone.TOpe[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TAir[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.tabsHeatingPower'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.tabsCoolingPower'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempHeatRem.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempCoolRem.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.PCooler[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]

            res.read_results(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )
        elif "radiator" in bldg.name:
            signals = ['multizone.TOpe[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TAir[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempHeatRem.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]

            res.read_results(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )
        elif "convective" in bldg.name:
            signals = ['multizone.TOpe[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TAir[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempHeatRem.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempCoolRem.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.PCooler[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]

            res.read_results(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )
        """res.read_results(
            buildings=pickle_prj.buildings,
            signals=signals,
            index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
            index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
            results_path=sim_results_path,
            csv_path=csv_results_path,
        )"""

    print("That's it! :)")
