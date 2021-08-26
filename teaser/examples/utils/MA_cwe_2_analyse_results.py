import os
import datetime
import read_results as res
import pandas as pd
import pickle
import timing

if __name__ == '__main__':
    timing
    # set path to your workspace here
    workspace = os.path.join("D:\\", "tbl-cwe", "Final_Simulations", "Chapter4_Ref_floor2x")
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
    # you have to change the index of res.read_results() according to your simulation data
    # choose single if only one year was simulated and double if two years were simulated
    single = 8760
    double = 17520

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
            signals += ['multizone.TRad[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempHeatPanel.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempCoolPanel.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.PCooler[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].ROM.extWall.Q_flow'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            """
            res.read_results(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=double, freq="H"),
                index_res=pd.date_range(datetime.datetime(2022, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )"""
        elif "tabsplusair" in bldg.name:
            signals = ['multizone.TOpe[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TAir[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TRad[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
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
            signals += ['multizone.zone[{}].ROM.extWall.Q_flow'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            """
            res.read_results(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=double, freq="H"),
                index_res=pd.date_range(datetime.datetime(2022, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )"""
        elif "TABS" in bldg.name:
            signals = ['multizone.TOpe[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TAir[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TRad[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.tabsHeatingPower'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.tabsCoolingPower'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.PCooler[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].ROM.extWall.Q_flow'.format(i + 1) for i in range(len(bldg.thermal_zones))]
        elif "radiator" in bldg.name:
            signals = ['multizone.TOpe[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TAir[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TRad[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempHeatRem.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].ROM.extWall.Q_flow'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            """
            res.read_results(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=double, freq="H"),
                index_res=pd.date_range(datetime.datetime(2022, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )"""
        elif "convective" in bldg.name:
            signals = ['multizone.TOpe[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TAir[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.TRad[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempHeatRem.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].heaterCoolerWithTabs6007C1.pITempCoolRem.y'.format(i + 1) for i in
                        range(len(bldg.thermal_zones))]
            signals += ['multizone.PHeater[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.PCooler[{}]'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].ROM.extWall.Q_flow'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            """
            res.read_results(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=double, freq="H"),
                index_res=pd.date_range(datetime.datetime(2022, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )"""
        res.read_results(
            buildings=[bldg.name],
            signals=signals,
            index=pd.date_range(datetime.datetime(2021, 1, 1), periods=double, freq="H"),
            index_res=pd.date_range(datetime.datetime(2022, 1, 1), periods=8760, freq="H"),
            results_path=sim_results_path,
            csv_path=csv_results_path,
        )

    print("That's it! :)")
