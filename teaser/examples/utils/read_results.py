"""Module to read results with DymolaInterface."""
# from Peter Remmen

import datetime
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd

from dymola.dymola_interface import DymolaInterface

# This module reads simulation results from Dymola simulation of TEASER buidlings and
# saves heating, cooling and electricity demand (ventilation) into seperate *.csv files
# for further usage. It needs exact same naming of the one that was simulated

# To use this module: simply copy it into your folder.

# Example
# -------
#
# Specify path to your simulation workspace
# >>> workspace = os.path.join(
#     'D:\\',
#     'workspaces',
#     'YOUR SIMULATION')
# Specify the signals you want to read i.e. Modelica naming of parameters PHeater and
# PCooler for three thermal zones
# >>> signals = [
#     "multizoneSimpleHRS.PHeater[{}]".format(i + 1)
#     for i in range(0,3)
# ]
# >>> signals += [
#     "multizoneSimpleHRS.PCooler[{}]".format(i + 1)
#     for i in range(len(bldg.thermal_zones))
# ]
# Call read_results function
# >>> read_results(
#       buildings=["Bldg_1", "Bldg_2"],
#       signals=signals,
#       index=pd.date_range(
#           datetime.datetime(2019, 1, 1),
#           periods=8761,
#           freq='H',
#           tz='Europe/Berlin'),
#       index_res=pd.date_range(
#           datetime.datetime(2019, 1, 1),
#           periods=8761,
#           freq='H',
#           tz='Europe/Berlin'),
#       results_path=os.path.join(workspace, 'results', prj.name),
#       csv_path=os.path.join(workspace, 'sim_results'))


def read_results(
    buildings,
    signals,
    index=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
    index_res=pd.date_range(datetime.datetime(2021, 1, 1), periods=8760, freq="H"),
    results_path=None,
    csv_path=None,
    ):
    """Read simulation data from .mat file and save them into csv.

    Reads Dymola result files and saves them as time series in csv.  It assumes that all
    thermal_zones as a MultiZone (TEASER Export) in Modelica.

    Parameters
    ----------
    buildings : list
        List of building names (i. e. name of *.mat file) whose results should be read.
    signals : list
            List of signals to be read from the results file.
    index : Pandas date_range
        Pandas date range of the simulation data. Must fit the length of
        simulation data. (default: hourly for year 2019)
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
        #bldg.name
        if not (bldg + "_heat.csv") in os.listdir(csv_path):
            try:
                print(os.path.join(results_path, bldg + ".mat"))
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
                raise Exception("Results Error!")
                continue
            try:
                results.index = index
            except ValueError:
                print(
                    "Simulation results of building {} are most likely "
                    "faulty (series is shorter then one year), please check "
                    "result file".format(bldg)
                )
                raise Exception("Completion Error!")

            if indoor_air is False:
                if tabs is not None:
                    results = results.rolling(tabs).mean().shift(int(-tabs / 2))

                heat = pd.DataFrame(
                    data=results.filter(like="PHeat").sum(axis=1)[
                        index_res[0] : index_res[-1]
                    ],
                    index=index_res,
                    columns=[bldg + " heat"],
                )
                """
                heat.loc[:, bldg + " tabsHeatingPower"] = results.filter(like="tabsHeatingPower").sum(axis=1)[
                        index_res[0] : index_res[-1]
                    ]
                heat.loc[:, bldg + " pITempHeatRem.y"] = results.filter(like="pITempHeatRem.y").sum(axis=1)[
                        index_res[0] : index_res[-1]
                    ]        
                heat.loc[:, bldg + " pITempHeatPanel.y"] = results.filter(like="pITempHeatPanel.y").sum(axis=1)[
                        index_res[0] : index_res[-1]
                    ]        
                """

                cool = pd.DataFrame(
                    data=results.filter(like="PCool")
                    .abs()
                    .sum(axis=1)[index_res[0] : index_res[-1]],
                    index=index_res,
                    columns=[bldg + " cool"],
                )
                """
                cool.loc[:, bldg + " tabsCoolingPower"] = results.filter(like="tabsCoolingPower").abs().sum(axis=1)[
                        index_res[0] : index_res[-1]
                    ]
                cool.loc[:, bldg + " pITempCoolRem.y"] = results.filter(like="pITempCoolRem.y").abs().sum(axis=1)[
                        index_res[0] : index_res[-1]
                    ]  
                cool.loc[:, bldg + " pITempCoolPanel.y"] = results.filter(like="pITempCoolPanel.y").abs().sum(axis=1)[
                        index_res[0] : index_res[-1]
                    ]        
                """
                """
                temp = pd.DataFrame(
                    data=results.filter(like="TAir").sum(axis=1)[
                         index_res[0]: index_res[-1]
                         ],
                    index=index_res,
                    columns=[bldg + " TAir"],
                )
                temp.loc[:, bldg + " TOpe"] = results.filter(like="TOpe").sum(axis=1)[
                        index_res[0] : index_res[-1]
                    ] 
                """

                heat.to_csv(os.path.join(csv_path, bldg + "_heat.csv"))
                cool.to_csv(os.path.join(csv_path, bldg + "_cool.csv"))
                heat.to_excel(os.path.join(csv_path, bldg + "_excel_heat.xlsx"))
                cool.to_excel(os.path.join(csv_path, bldg + "_excel_cool.xlsx"))
                """
                temp.to_csv(os.path.join(csv_path, bldg + "_temp.csv"))
                temp.to_csv(os.path.join(csv_path, bldg + "_excel_temp.xlsx"))
                """
    dymola.close()


def plot_results(heat, cool, title, output_path):
    """Very simple and basic plotting of heating and cooling time series."""
    data = pd.DataFrame(
        index=pd.date_range(
            start=datetime.datetime(2021, 1, 1, 0, 0, 0),
            end=datetime.datetime(2021, 12, 31, 23, 55),
            freq="H",
        ),
        columns=["Wärmeleistung", "Kälteleistung"],
    )
    data["Wärmeleistung"] = heat.iloc[:, 0].values / 1000
    data["Kälteleistung"] = -cool.iloc[:, 0].values / 1000
    # data = data.dropna()
    fig, ax1 = plt.subplots()
    ax = sns.lineplot(
        data=data,
        hue={"ls": ["-", "-"]},
        palette=["#407FB7", "#646567"],
        linewidth=0.5,
        ax=ax1,
    )

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m"))
    plt.ylabel("Leistung in [kWh/h]")
    fig.tight_layout()
    fig.set_size_inches(5.9, 3.0, forward=True)

    plt.savefig(output_path, dpi=200)
    plt.clf()
    ax = sns.lineplot(
        data=data.resample("D").mean(),
        hue={"ls": ["-", "--"]},
        palette=["#407FB7", "#646567"],
        linewidth=0.5,
    )
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m"))
    plt.title(title + " D")
    plt.savefig(output_path.replace("plt", "plt_D"), dpi=200)
    plt.clf()
