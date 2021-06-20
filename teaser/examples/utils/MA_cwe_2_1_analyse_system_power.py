import os
import datetime
#import read_results as res
import pandas as pd
import pickle
from dymola.dymola_interface import DymolaInterface

def read_results_power(
        buildings,
        signals,
        index=pd.date_range(datetime.datetime(2021, 1, 1), periods=1, freq="H"),
        index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=1, freq="H"),
        results_path=None,
        csv_path=None,
):
    """Read simulation data from .mat file and save them into csv.

    Reads Dymola result files and saves them as time series in csv. It assumes that all
    thermal_zones are a MultiZone (TEASER Export) in Modelica.

    Parameters
    ----------
    buildings : list
        List of TEASER bldgs
    signals : list
        List of signals to be read from the results file.
    index : Pandas date_range
        Pandas date range of the simulation data. Must fit the length of
        simulation data. (Beware of leap years! every 4 years, e.g. 2020) (default: hourly for year 2019)
    index_res : Pandas date_range
        Pandas date range  if slice should be picked e. g. only january of the simulation data. Must fit the length of
        simulation data. (default: hourly for year 2015)
    results_path : str
        Path where Dymola results are  stored.
    csv_path : str
        Path where csv results should be stored.

    """

    if not os.path.exists(csv_path):
        os.makedirs(csv_path)
    dymola = DymolaInterface()

    for bldg in buildings:
        print("reading building {}".format(bldg))
        # bldg.name # bldg
        #if not (bldg + "_heat.csv") in os.listdir(csv_path):
        try:
            #print(os.path.join(results_path, bldg + ".mat"))
            dym_res = dymola.readTrajectory(
                fileName=os.path.join(results_path, bldg + ".mat"),
                signals=signals,
                rows=dymola.readTrajectorySize(
                    fileName=os.path.join(results_path, bldg + ".mat")
                ),
            )
            results = pd.DataFrame().from_records(dym_res).T
            results = results.rename(
                columns=dict(zip(results.columns.values, signals))
            )
        except BaseException:
            # Dymola has strange exceptions
            print(
                "Reading results of building {} failed, "
                "please check result file".format(bldg)
            )
            # raise Exception("Results Error!")
            continue
        try:
            results.index = index
        except ValueError:
            print(
                "Simulation results of building {} are most likely "
                "faulty (series is shorter then one year), please check "
                "result file".format(bldg)
            )
            # raise Exception("Completion Error!")
            continue

        power = pd.DataFrame(
            data=results.filter(like="hHeatPanel").sum(axis=1)[
                 index_res[0]: index_res[-1]
                 ],
            index=index_res,
            columns=[bldg + " hHeatPanel"],
        )
        power.loc[:, bldg + " lCoolPanel"] = results.filter(like="lCoolPanel").sum(axis=1)[
                                                  index_res[0]: index_res[-1]
                                                  ]
        power.loc[:, bldg + " powerHeatTabs"] = results.filter(like="powerHeatTabs").sum(axis=1)[
                                                 index_res[0]: index_res[-1]
                                                 ]
        power.loc[:, bldg + " powerCoolTabs"] = results.filter(like="powerCoolTabs").sum(axis=1)[
                                                   index_res[0]: index_res[-1]
                                                   ]
        power.loc[:, bldg + " hHeatRem"] = results.filter(like="hHeatRem").sum(axis=1)[
                                                index_res[0]: index_res[-1]
                                                ]
        power.loc[:, bldg + " lCoolRem"] = results.filter(like="lCoolRem").sum(axis=1)[
                                                index_res[0]: index_res[-1]
                                                ]

        power.to_csv(os.path.join(csv_path, bldg + "_power.csv"))
        #power.to_excel(os.path.join(csv_path, bldg + "_power.xlsx"))

    dymola.close()


if __name__ == '__main__':

    # set path to your workspace here
    workspace = os.path.join("D:\\", "tbl-cwe", "TABS_power", "Simulationsstudie_TABS_60")
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

    csv_results_path = os.path.join(workspace, "csv_results", "power_comparison")
    print("Your .csv files are stored in: " + csv_results_path)
    print("##########")

    for bldg in pickle_prj.buildings:
        if "panel" in bldg.name:
            signals = ['multizone.zone[{}].zoneParam.hHeatPanel'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].zoneParam.lCoolPanel'.format(i + 1) for i in range(len(bldg.thermal_zones))]

            read_results_power(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )
        elif "tabsplusair" in bldg.name:
            signals = ['multizone.zone[{}].zoneParam.powerHeatTabs'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].zoneParam.powerCoolTabs'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].zoneParam.hHeatRem'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].zoneParam.lCoolRem'.format(i + 1) for i in range(len(bldg.thermal_zones))]

            read_results_power(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )
        elif "radiator" in bldg.name:
            signals = ['multizone.zone[{}].zoneParam.hHeatRem'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].zoneParam.lCoolRem'.format(i + 1) for i in range(len(bldg.thermal_zones))]

            read_results_power(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )
        elif "convective" in bldg.name:
            signals = ['multizone.zone[{}].zoneParam.hHeatRem'.format(i + 1) for i in range(len(bldg.thermal_zones))]
            signals += ['multizone.zone[{}].zoneParam.lCoolRem'.format(i + 1) for i in range(len(bldg.thermal_zones))]

            read_results_power(
                buildings=[bldg.name],
                signals=signals,
                index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
                results_path=sim_results_path,
                csv_path=csv_results_path,
            )

    print("That's it! :)")
