"""
This module contains functions to read, analyse and plot simulation results from Dymola simulations of TEASER buildings.

Functions currently in use are:
1) read_results(...)
    Read simulation data from .mat file with Dymola Interface and save them into csv.
2) calc_results(...)
    Create csv-file containing KPIs of buildings.
3) plot_results(...)
    Create plots of heating, cooling and temperature time series from .csv
    files with hourly demands created by MA_cwe_2_analyse_results.py

"""

import datetime
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#plt.style.use(os.path.join("D:\\", "tbl-cwe", "Repos", "TEASER", "teaser", "examples", "utils", "ebc.paper.mplstyle"))
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd

from statistics import mean
from dymola.dymola_interface import DymolaInterface


# This module reads simulation results from Dymola simulation of TEASER buildings and
# saves heating, cooling and electricity demand (ventilation) into separate *.csv files
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

        heat = pd.DataFrame(
            data=results.filter(like="PHeat").sum(axis=1)[
                 index_res[0]: index_res[-1]
                 ],
            index=index_res,
            columns=[bldg + " PHeat"],
        )
        heat.loc[:, bldg + " tabsHeatingPower"] = results.filter(like="tabsHeatingPower").sum(axis=1)[
                                                  index_res[0]: index_res[-1]
                                                  ]
        heat.loc[:, bldg + " pITempHeatRem.y"] = results.filter(like="pITempHeatRem.y").sum(axis=1)[
                                                 index_res[0]: index_res[-1]
                                                 ]
        heat.loc[:, bldg + " pITempHeatPanel.y"] = results.filter(like="pITempHeatPanel.y").sum(axis=1)[
                                                   index_res[0]: index_res[-1]
                                                   ]

        cool = pd.DataFrame(
            data=results.filter(like="PCool")
                     .abs()
                     .sum(axis=1)[index_res[0]: index_res[-1]],
            index=index_res,
            columns=[bldg + " PCool"],
        )

        cool.loc[:, bldg + " tabsCoolingPower"] = results.filter(like="tabsCoolingPower").abs().sum(axis=1)[
                                                  index_res[0]: index_res[-1]
                                                  ]
        cool.loc[:, bldg + " pITempCoolRem.y"] = results.filter(like="pITempCoolRem.y").abs().sum(axis=1)[
                                                 index_res[0]: index_res[-1]
                                                 ]
        cool.loc[:, bldg + " pITempCoolPanel.y"] = results.filter(like="pITempCoolPanel.y").abs().sum(axis=1)[
                                                   index_res[0]: index_res[-1]
                                                   ]
        if "Office" in bldg:
            #for i in range(len([bldg.thermal_zones])):
            temp = pd.DataFrame(
                data=results.filter(like="TAir[1]").sum(axis=1)[
                     index_res[0]: index_res[-1]
                     ],
                index=index_res,
                columns=[bldg + " TAir[1]"],
            )
            temp.loc[:, bldg + " TAir[2]"] = results.filter(like="TAir[2]").sum(axis=1)[index_res[0]: index_res[-1]]
            temp.loc[:, bldg + " TAir[3]"] = results.filter(like="TAir[3]").sum(axis=1)[index_res[0]: index_res[-1]]
            temp.loc[:, bldg + " TAir[4]"] = results.filter(like="TAir[4]").sum(axis=1)[index_res[0]: index_res[-1]]
            temp.loc[:, bldg + " TAir[5]"] = results.filter(like="TAir[5]").sum(axis=1)[index_res[0]: index_res[-1]]
            temp.loc[:, bldg + " TAir[6]"] = results.filter(like="TAir[6]").sum(axis=1)[index_res[0]: index_res[-1]]
            temp.loc[:, bldg + " TOpe[1]"] = results.filter(like="TOpe[1]").sum(axis=1)[index_res[0]: index_res[-1]]
            temp.loc[:, bldg + " TOpe[2]"] = results.filter(like="TOpe[2]").sum(axis=1)[index_res[0]: index_res[-1]]
            temp.loc[:, bldg + " TOpe[3]"] = results.filter(like="TOpe[3]").sum(axis=1)[index_res[0]: index_res[-1]]
            temp.loc[:, bldg + " TOpe[4]"] = results.filter(like="TOpe[4]").sum(axis=1)[index_res[0]: index_res[-1]]
            temp.loc[:, bldg + " TOpe[5]"] = results.filter(like="TOpe[5]").sum(axis=1)[index_res[0]: index_res[-1]]
            temp.loc[:, bldg + " TOpe[6]"] = results.filter(like="TOpe[6]").sum(axis=1)[index_res[0]: index_res[-1]]
        else:
            temp = pd.DataFrame(
                data=results.filter(like="TAir").sum(axis=1)[
                     index_res[0]: index_res[-1]
                     ],
                index=index_res,
                columns=[bldg + " TAir"],
            )
            temp.loc[:, bldg + " TOpe"] = results.filter(like="TOpe").sum(axis=1)[
                                          index_res[0]: index_res[-1]
                                          ]

        heat.to_csv(os.path.join(csv_path, bldg + "_heat.csv"))
        cool.to_csv(os.path.join(csv_path, bldg + "_cool.csv"))
        #heat.to_excel(os.path.join(csv_path, bldg + "_excel_heat.xlsx"))
        #cool.to_excel(os.path.join(csv_path, bldg + "_excel_cool.xlsx"))

        temp.to_csv(os.path.join(csv_path, bldg + "_temp.csv"))
        #temp.to_excel(os.path.join(csv_path, bldg + "_excel_temp.xlsx"))

    dymola.close()

def calc_results(buildings, csv_path, output_path):
    """Create csv-file containing KPIs of buildings.

    Parameters
    ----------
    buildings : prj.buildings
        load TEASER bldgs from a pickle project file
    csv_path : str
        Path where hourly demands created by MA_cwe_2_analyse_results.py are stored
    output_path : str
        Path where output files should be stored

    """
    #output_path2 = os.path.join(output_path, "temp")
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    #if not os.path.exists(output_path2):
    #    os.makedirs(output_path2)

    results = pd.DataFrame()

    for bldg in buildings:
        try:
            print("reading building {}".format(bldg.name))
            # read hourly demands
            heat_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_heat.csv"))
            cool_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_cool.csv"))
            temp_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_temp.csv"))

            # drop the first 4 days of the data
            # you also have to change the index of data = pd.DataFrame (!!)
            """
            heat_data = heat_data.drop(heat_data.index[0:96])
            cool_data = cool_data.drop(cool_data.index[0:96])
            temp_data = temp_data.drop(temp_data.index[0:96])
            """

            # calculate annual heating and cooling demand
            annual_heat = heat_data.loc[:, bldg.name + " PHeat"].sum() / 1000
            annual_cool = cool_data.loc[:, bldg.name + " PCool"].sum() / 1000
            # calculate specific annual heating and cooling demand
            spec_annual_heat = annual_heat / bldg.net_leased_area
            spec_annual_cool = annual_cool / bldg.net_leased_area
            # determine maximum values
            max_heat = heat_data.loc[:, bldg.name + " PHeat"].max() / 1000
            max_cool = cool_data.loc[:, bldg.name + " PCool"].max() / 1000
            # calculate specific maximum values
            spec_max_heat = max_heat * 1000 / bldg.net_leased_area
            spec_max_cool = max_cool * 1000 / bldg.net_leased_area

            # office buildings are divided in 6 zones, the temperature for each zone are multiplied with the
            # zone area factor to calculate one indoor temperature for the whole building
            data = pd.DataFrame(index=pd.date_range(
                        start=datetime.datetime(2021, 1, 1, 0, 0, 0),
                        end=datetime.datetime(2021, 12, 31, 23, 55),
                        freq="H", ))
            if "Office" in bldg.name:
                data.loc[:, "TOpe"] = ((temp_data.loc[:, bldg.name + " TOpe[1]"].values * 0.5 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TOpe[2]"].values * 0.25 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TOpe[3]"].values * 0.15 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TOpe[4]"].values * 0.04 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TOpe[5]"].values * 0.04 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TOpe[6]"].values * 0.02 * bldg.net_leased_area) / bldg.net_leased_area) - 273.15
            else:
                data.loc[:, "TOpe"] = temp_data.loc[:, bldg.name + " TOpe"].values - 273.15

            # calculate mean of indoor operative air temperature during winter (01/10 - 30/04)
            temp_winter = data.drop(data.index[2784:6456])
            temp_winter_mean = temp_winter.loc[:, "TOpe"].sum() / len(temp_winter.index)
            # calculate mean of indoor operative air temperature during summer (01/05 - 30/09)
            temp_summer = data[2784:6456]
            temp_summer_mean = temp_summer.loc[:, "TOpe"].sum() / len(temp_summer.index)

            if "tabsplusair" in bldg.name:
                # calculate TABS heating and cooling demand
                annual_heat_tabs = heat_data.loc[:, bldg.name + " tabsHeatingPower"].sum() / 1000
                annual_cool_tabs = cool_data.loc[:, bldg.name + " tabsCoolingPower"].sum() / 1000
                # calculate specific annual heating and cooling demand
                spec_annual_heat_tabs = annual_heat_tabs / bldg.net_leased_area
                spec_annual_cool_tabs = annual_cool_tabs / bldg.net_leased_area
                # calculate convective heating and cooling demand
                annual_heat_convective = heat_data.loc[:, bldg.name + " pITempHeatRem.y"].sum() / 1000
                annual_cool_convective = cool_data.loc[:, bldg.name + " pITempCoolRem.y"].sum() / 1000
                # calculate specific annual heating and cooling demand
                spec_annual_heat_convective = annual_heat_convective / bldg.net_leased_area
                spec_annual_cool_convective = annual_cool_convective / bldg.net_leased_area
                # calculate share of TABS heating and cooling in relation to convective system
                share_tabs_heating_total = (annual_heat_tabs / annual_heat) * 100  # in %
                share_tabs_cooling_total = (annual_cool_tabs / annual_cool) * 100  # in %
            elif "panel" in bldg.name:
                # calculate Panel heating and cooling demand
                annual_heat_panel = heat_data.loc[:, bldg.name + " pITempHeatPanel.y"].sum() / 1000
                annual_cool_panel = cool_data.loc[:, bldg.name + " pITempCoolPanel.y"].sum() / 1000
                # calculate specific annual heating and cooling demand
                spec_annual_heat_panel = annual_heat_panel / bldg.net_leased_area
                spec_annual_cool_panel = annual_cool_panel / bldg.net_leased_area
            elif "radiator" in bldg.name:
                # calculate Radiator heating and cooling demand
                annual_heat_radiator = heat_data.loc[:, bldg.name + " pITempHeatRem.y"].sum() / 1000
                # calculate specific annual heating and cooling demand
                spec_annual_heat_radiator = annual_heat_radiator / bldg.net_leased_area
            elif "convective" in bldg.name:
                # calculate convective heating and cooling demand
                annual_heat_convective = heat_data.loc[:, bldg.name + " pITempHeatRem.y"].sum() / 1000
                annual_cool_convective = cool_data.loc[:, bldg.name + " pITempCoolRem.y"].sum() / 1000
                # calculate specific annual heating and cooling demand
                spec_annual_heat_convective = annual_heat_convective / bldg.net_leased_area
                spec_annual_cool_convective = annual_cool_convective / bldg.net_leased_area
            elif "tabs" in bldg.name:
                # calculate TABS heating and cooling demand
                annual_heat_tabs = heat_data.loc[:, bldg.name + " tabsHeatingPower"].sum() / 1000
                annual_cool_tabs = cool_data.loc[:, bldg.name + " tabsCoolingPower"].sum() / 1000
                # calculate specific annual heating and cooling demand
                spec_annual_heat_tabs = annual_heat_tabs / bldg.net_leased_area
                spec_annual_cool_tabs = annual_cool_tabs / bldg.net_leased_area

            if "EFH" in bldg.name:
                results.loc[bldg.name, "Type"] = "EFH"
            elif "MFH" in bldg.name:
                results.loc[bldg.name, "Type"] = "MFH"
            elif "Office" in bldg.name:
                results.loc[bldg.name, "Type"] = "Office"
            if "radiator" in bldg.name:
                results.loc[bldg.name, "System"] = "Radiator"
            elif "convective" in bldg.name:
                results.loc[bldg.name, "System"] = "Convective"
            elif "panel" in bldg.name:
                results.loc[bldg.name, "System"] = "Panel"
            elif "tabsplusair" in bldg.name:
                results.loc[bldg.name, "System"] = "TABSplusAir"

            results.loc[bldg.name, "Year of construction"] = bldg.year_of_construction
            results.loc[bldg.name, "Net area"] = bldg.net_leased_area
            #results.loc[bldg.name, "Footprint area"] = bldg.ground_floor_geo["GroundFloor"]["area"]
            #results.loc[bldg.name, "Volume"] = bldg.volume
            results.loc[bldg.name, "A/V"] = bldg.library_attr.total_surface_area / bldg.volume
            results.loc[bldg.name, "Construction type"] = bldg.construction_type

            results.loc[bldg.name, "Annual heating demand [kWh/a]"] = round(annual_heat, 1)
            results.loc[bldg.name, "Specific annual heating demand [kWh/sqm*a]"] = round(spec_annual_heat, 1)
            results.loc[bldg.name, "Maximum heating power [kW]"] = round(max_heat, 1)
            results.loc[bldg.name, "Specific maximum heating power [W/sqm]"] = round(spec_max_heat, 1)
            results.loc[bldg.name, "Annual cooling demand [kWh/a]"] = round(annual_cool, 1)
            results.loc[bldg.name, "Specific annual cooling demand [kWh/sqm*a]"] = round(spec_annual_cool, 1)
            results.loc[bldg.name, "Maximum cooling power [kW]"] = round(max_cool, 1)
            results.loc[bldg.name, "Specific maximum cooling power [W/sqm]"] = round(spec_max_cool, 1)
            results.loc[bldg.name, "Mean winter indoor operative air temperature"] = round(temp_winter_mean, 1)
            results.loc[bldg.name, "Mean summer indoor operative air temperature"] = round(temp_summer_mean, 1)

            if "tabsplusair" in bldg.name:
                results.loc[bldg.name, "Annual tabs heating demand [kWh/a]"] = round(annual_heat_tabs, 1)
                results.loc[bldg.name, "Annual tabs cooling demand [kWh/a]"] = round(annual_cool_tabs, 1)
                results.loc[bldg.name, "Specific annual tabs heating demand [kWh/sqm*a]"] = round(spec_annual_heat_tabs, 1)
                results.loc[bldg.name, "Specific annual tabs cooling demand [kWh/sqm*a]"] = round(spec_annual_cool_tabs, 1)
                results.loc[bldg.name, "Annual convective heating demand [kWh/a]"] = round(annual_heat_convective, 1)
                results.loc[bldg.name, "Annual convective cooling demand [kWh/a]"] = round(annual_cool_convective, 1)
                results.loc[bldg.name, "Specific annual convective heating demand [kWh/sqm*a]"] = round(
                    spec_annual_heat_convective, 1)
                results.loc[bldg.name, "Specific annual convective cooling demand [kWh/sqm*a]"] = round(
                    spec_annual_cool_convective, 1)
                results.loc[bldg.name, "Share of TABS heating of total heating [%]"] = round(share_tabs_heating_total, 1)
                results.loc[bldg.name, "Share of TABS cooling of total cooling [%]"] = round(share_tabs_cooling_total, 1)

        except BaseException:
            # Dymola has strange exceptions
            print(
                "Reading results of building {} failed, "
                "please check result file".format(bldg.name)
            )
            # raise Exception("Results Error!")
            continue

    #temp_winter.to_excel(os.path.join(output_path, "temp", bldg.name + "_temp_winter.xlsx"))
    #temp_summer.to_excel(os.path.join(output_path, "temp", bldg.name + "_temp_summer.xlsx"))

    #results.to_csv(os.path.join(output_path, "buildings_calc.csv"))
    results.to_excel(os.path.join(output_path, "buildings_excel_calc.xlsx"))
    print("Calculations done! :)")

def plot_results(buildings, csv_path, output_path):
    """Create plots of heating, cooling and temperature time series from .csv
    files with hourly demands created by MA_cwe_2_analyse_results.py

    Parameters
    ----------
    buildings : prj.buildings
        load TEASER bldgs from a pickle project file
    csv_path : str
        Path where .csv files are be stored.
    output_path : str
        Path where plots should be stored.

    """
    output_path2 = os.path.join(output_path, "single")
    output_path3 = os.path.join(output_path, "daily_single")
    output_path4 = os.path.join(output_path, "sliced")

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    if not os.path.exists(output_path2):
        os.makedirs(output_path2)
    if not os.path.exists(output_path3):
        os.makedirs(output_path3)
    if not os.path.exists(output_path4):
        os.makedirs(output_path4)

    for bldg in buildings:
        try:
            print("reading building {}".format(bldg.name))
            # read hourly demands
            heat_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_heat.csv"), index_col=0)
            cool_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_cool.csv"), index_col=0)
            temp_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_temp.csv"), index_col=0)

            data = pd.DataFrame(
                index=pd.date_range(
                    start=datetime.datetime(2021, 1, 1, 0, 0, 0),
                    end=datetime.datetime(2021, 12, 31, 23, 55),
                    freq="H", ),
                columns=["Wärmeleistung", "Kälteleistung", "Temperatur"], )

            # divide demands by 1000 to get kW
            data.loc[:, "Wärmeleistung"] = heat_data.loc[:, bldg.name + " PHeat"].values / 1000
            data.loc[:, "Kälteleistung"] = -cool_data.loc[:, bldg.name + " PCool"].values / 1000

            # office buildings are divided in 6 zones, the temperature for each zone are multiplied with the
            # zone area factor to calculate one indoor temperature for the whole building
            if "Office" in bldg.name:
                data.loc[:, "Temperatur"] = ((temp_data.loc[:, bldg.name + " TOpe[1]"].values*0.5*bldg.net_leased_area
                                             +temp_data.loc[:, bldg.name + " TOpe[2]"].values*0.25*bldg.net_leased_area
                                             +temp_data.loc[:, bldg.name + " TOpe[3]"].values*0.15*bldg.net_leased_area
                                             +temp_data.loc[:, bldg.name + " TOpe[4]"].values*0.04*bldg.net_leased_area
                                             +temp_data.loc[:, bldg.name + " TOpe[5]"].values*0.04*bldg.net_leased_area
                                             +temp_data.loc[:, bldg.name + " TOpe[6]"].values*0.02*bldg.net_leased_area)
                                             /bldg.net_leased_area) - 273.15
            else:
                data.loc[:, "Temperatur"] = temp_data.loc[:, bldg.name + " TOpe"].values - 273.15

            if "tabsplusair" in bldg.name:
                data.loc[:, "tabs_heat_demand"] = heat_data.loc[:, bldg.name + " tabsHeatingPower"].values / 1000
                data.loc[:, "tabs_cool_demand"] = -cool_data.loc[:, bldg.name + " tabsCoolingPower"].values / 1000
                data.loc[:, "convective_heat_demand"] = heat_data.loc[:, bldg.name + " pITempHeatRem.y"].values / 1000
                data.loc[:, "convective_cool_demand"] = -cool_data.loc[:, bldg.name + " pITempCoolRem.y"].values / 1000

            #heat_demand = heat_data.loc[:, bldg.name + " PHeat"].values / 1000
            #cool_demand = -cool_data.loc[:, bldg.name + " PCool"].values / 1000
            #temp_ope = temp_data.loc[:, bldg.name + " TOpe"].values - 273.15

            #start_remove = pd.to_datetime('2021-1-1')
            #end_remove = pd.to_datetime('2021-1-3')
            #sliced_data = data.loc[data.index.difference(data.index[data.index.slice_indexer(start_remove, end_remove)])]

            # Use this to exclude the first hours of your simulation results, e.g. [0:96] to skip the first 4 days
            #data = data.drop(data.index[0:96])

            # plot parameters
            """sidewidth = 6.224
            fontsize = 11
            font = {'family': 'serif',
                    'weight': 'normal',
                    'size': fontsize}
            params = {'legend.fontsize': fontsize,
                      'xtick.labelsize': fontsize,
                      'ytick.labelsize': fontsize,
                      'axes.labelsize': fontsize,
                      'axes.titlesize': fontsize}
            matplotlib.rc('font', **font)
            matplotlib.rcParams.update(params)"""

            # parameters for axis definition
            days = mdates.DayLocator(interval=10)
            weeks = mdates.DayLocator(interval=7)
            minormonths = mdates.MonthLocator(interval=1)
            majormonths = mdates.MonthLocator(interval=2)
            format = mdates.DateFormatter("%d-%m")
            locator = matplotlib.dates.MonthLocator(
                bymonth=None,
                bymonthday=15,
                interval=1,
                tz=None)
            formatter = mdates.DateFormatter("%b")

            # plot the indoor temperature and heating/cooling demand for one year in two subplots
            print("plotting building {}".format(bldg.name))
            fig, (ax1, ax2) = plt.subplots(2)
            ax1.plot(data.loc[:, "Temperatur"], linewidth=0.3)
            ax1.set_title("Operative Temperatur")
            ax1.set_ylabel('Temperatur in [°C]')
            ax1.set_ylim([18, 28])
            ax1.margins(0.01)
            ax1.xaxis.set_minor_locator(minormonths)
            ax1.xaxis.set_major_locator(majormonths)
            ax1.xaxis.set_major_formatter(format)
            #ax2.plot(heat_demand, linewidth=0.3, label="Wärmeleistung", color="r")
            #ax2.plot(cool_demand, linewidth=0.3, label="Kälteleistung")
            ax2.plot(data.loc[:, "Wärmeleistung"], linewidth=0.3, label="Wärmeleistung", color="r")
            ax2.plot(data.loc[:, "Kälteleistung"], linewidth=0.3, label="Kälteleistung")
            ax2.set_title("Heiz- und Kühllast")
            ax2.set_ylabel('Leistung in [kW]')
            ax2.set_xlabel('Zeit')
            #ax2.set_ylim([0, 5000])
            #ax2.set_xlim([5000, 8760])
            #ax2.autoscale()
            ax2.margins(0.01)
            ax2.xaxis.set_minor_locator(minormonths)
            ax2.xaxis.set_major_locator(majormonths)
            ax2.xaxis.set_major_formatter(format)

            #plt.grid(color='green', linestyle='--', linewidth=0.1)
            plt.tight_layout()
            plt.savefig(os.path.join(output_path, bldg.name + "_plot.pdf"), dpi=200)
            plt.close("all")

            # for TABSplusAir buildings additionally plot the TABS and convective demands in separate subplots
            if "tabsplusair" in bldg.name:
                fig2, (ax3, ax4, ax5) = plt.subplots(3)
                ax3.plot(data.loc[:, "Temperatur"], linewidth=0.3)
                ax3.set_title("Operative Temperatur")
                ax3.set_ylabel('Temperatur in [°C]')
                ax3.margins(0.01)
                ax3.set_ylim([18, 28])
                ax3.xaxis.set_minor_locator(minormonths)
                ax3.xaxis.set_major_locator(majormonths)
                ax3.xaxis.set_major_formatter(format)
                ax4.plot(data.loc[:, "tabs_heat_demand"], linewidth=0.3, label="Wärmeleistung", color="r")
                ax4.plot(data.loc[:, "tabs_cool_demand"], linewidth=0.3, label="Kälteleistung")
                ax4.set_title("TABS Heiz- und Kühllast")
                ax4.set_ylabel('Leistung in [kW]')
                #ax4.set_xlabel('Simulationszeit in h')
                ax4.set_ylim(auto=True)
                # ax4.set_ylim([0, 5000])
                # ax4.set_xlim([5000, 8760])
                # ax4.autoscale()
                ax4.margins(0.01)
                ax4.xaxis.set_minor_locator(minormonths)
                ax4.xaxis.set_major_locator(majormonths)
                ax4.xaxis.set_major_formatter(format)
                ax5.plot(data.loc[:, "convective_heat_demand"], linewidth=0.3, label="Wärmeleistung", color="r")
                ax5.plot(data.loc[:, "convective_cool_demand"], linewidth=0.3, label="Kälteleistung")
                ax5.set_title("Zusatz Heiz- und Kühllast")
                ax5.set_ylabel('Leistung in [kW]')
                ax5.set_xlabel('Zeit')
                ax5.set_ylim(auto=True)
                ax5.margins(0.01)
                ax5.xaxis.set_minor_locator(minormonths)
                ax5.xaxis.set_major_locator(majormonths)
                ax5.xaxis.set_major_formatter(format)

                plt.tight_layout()
                plt.savefig(os.path.join(output_path, bldg.name + "_TABS+_plot.pdf"), dpi=200)
                plt.close("all")

            # create single plots
            # operative temperature
            fig3, (ax6) = plt.subplots()
            ax6.plot(data.loc[:, "Temperatur"], linewidth=0.3)
            ax6.set_title("Operative Temperatur")
            ax6.set_ylabel('Temperatur in [°C]')
            ax6.set_xlabel('Zeit')
            ax6.set_ylim([18, 28])
            ax6.margins(0.01)
            ax6.xaxis.set_minor_locator(minormonths)
            ax6.xaxis.set_major_locator(majormonths)
            ax6.xaxis.set_major_formatter(format)

            plt.tight_layout()
            plt.savefig(os.path.join(output_path, "single", bldg.name + "_temp_plot.pdf"), dpi=200)
            plt.close("all")

            # heating and cooling demands
            fig4, (ax7) = plt.subplots()
            ax7.plot(data.loc[:, "Wärmeleistung"], linewidth=0.3, label="Wärmeleistung", color="r")
            ax7.plot(data.loc[:, "Kälteleistung"], linewidth=0.3, label="Kälteleistung")
            ax7.set_title("Heiz- und Kühllast")
            ax7.set_ylabel('Leistung in [kW]')
            ax7.set_xlabel('Zeit')
            # ax7.set_ylim([0, 5000])
            # ax7.set_xlim([5000, 8760])
            ax7.margins(0.01)
            ax7.xaxis.set_minor_locator(minormonths)
            ax7.xaxis.set_major_locator(majormonths)
            ax7.xaxis.set_major_formatter(format)

            plt.tight_layout()
            plt.savefig(os.path.join(output_path, "single", bldg.name + "_demand_plot.pdf"), dpi=200)
            plt.close("all")

            # for TABSplusAir buildings additionally plot the TABS and convective demands in separate subplots
            if "tabsplusair" in bldg.name:
                """# operative temperature
                # eigentlich überflüssig
                fig5, (ax8) = plt.subplots()
                ax8.plot(data.loc[:, "Temperatur"], linewidth=0.3)
                ax8.set_title("Operative Temperatur")
                ax8.set_ylabel('Temperatur in [°C]')
                ax8.set_xlabel('Zeit')
                ax8.set_ylim([18, 28])
                ax8.margins(0.01)
                ax8.xaxis.set_minor_locator(minormonths)
                ax8.xaxis.set_major_locator(majormonths)
                ax8.xaxis.set_major_formatter(format)

                plt.tight_layout()
                plt.savefig(os.path.join(output_path, "single", bldg.name + "_temp_TABS+_plot.pdf"), dpi=200)
                plt.close("all")"""

                # tabs demands
                fig6, (ax9) = plt.subplots()
                ax9.plot(data.loc[:, "tabs_heat_demand"], linewidth=0.3, label="Wärmeleistung", color="r")
                ax9.plot(data.loc[:, "tabs_cool_demand"], linewidth=0.3, label="Kälteleistung")
                ax9.set_title("TABS Heiz- und Kühllast")
                ax9.set_ylabel('Leistung in [kW]')
                ax9.set_xlabel('Zeit')
                ax9.set_ylim(auto=True)
                # ax4.set_ylim([0, 5000])
                # ax4.set_xlim([5000, 8760])
                # ax4.autoscale()
                ax9.margins(0.01)
                ax9.xaxis.set_minor_locator(minormonths)
                ax9.xaxis.set_major_locator(majormonths)
                ax9.xaxis.set_major_formatter(format)

                plt.tight_layout()
                plt.savefig(os.path.join(output_path, "single", bldg.name + "_TABS_demand_TABS+_plot.pdf"), dpi=200)
                plt.close("all")

                # convective demands
                fig7, (ax10) = plt.subplots()
                ax10.plot(data.loc[:, "convective_heat_demand"], linewidth=0.3, label="Wärmeleistung", color="r")
                ax10.plot(data.loc[:, "convective_cool_demand"], linewidth=0.3, label="Kälteleistung")
                ax10.set_title("Zusatz Heiz- und Kühllast")
                ax10.set_ylabel('Leistung in [kW]')
                ax10.set_xlabel('Zeit')
                ax10.set_ylim(auto=True)
                ax10.margins(0.01)
                ax10.xaxis.set_minor_locator(minormonths)
                ax10.xaxis.set_major_locator(majormonths)
                ax10.xaxis.set_major_formatter(format)

                plt.tight_layout()
                plt.savefig(os.path.join(output_path, "single", bldg.name + "_plus_demand_TABS+_plot.pdf"), dpi=200)
                plt.close("all")

            # create single resampled plots
            # operative temperature
            fig8, (ax12) = plt.subplots()
            ax12.plot(data.loc[:, "Temperatur"].resample("D").mean(), linewidth=0.3)
            ax12.set_title("Operative Temperatur")
            ax12.set_ylabel('Temperatur in [°C]')
            # ax12.set_xlabel('Zeit')
            ax12.set_ylim([18, 28])
            ax12.margins(0.01)
            # ax12.xaxis.set_minor_locator(minormonths)
            ax12.xaxis.set_major_locator(locator)
            ax12.xaxis.set_major_formatter(formatter)

            plt.tight_layout()
            plt.savefig(os.path.join(output_path, "daily_single", bldg.name + "_temp_D_plot.pdf"), dpi=200)
            plt.close("all")

            # heating and cooling demands
            fig9, (ax13) = plt.subplots()
            ax13.plot(data.loc[:, "Wärmeleistung"].resample("D").mean(), linewidth=0.3, label="Wärmeleistung", color="r")
            ax13.plot(data.loc[:, "Kälteleistung"].resample("D").mean(), linewidth=0.3, label="Kälteleistung")
            ax13.set_title("Heiz- und Kühllast")
            ax13.set_ylabel('Leistung in [kW]')
            # ax13.set_xlabel('Zeit')
            # ax13.set_ylim([0, 5000])
            # ax13.set_xlim([5000, 8760])
            ax13.margins(0.01)
            # ax13.xaxis.set_minor_locator(minormonths)
            ax13.xaxis.set_major_locator(locator)
            ax13.xaxis.set_major_formatter(formatter)

            plt.tight_layout()
            plt.savefig(os.path.join(output_path, "daily_single", bldg.name + "_demand_D_plot.pdf"), dpi=200)
            plt.close("all")

            # for TABSplusAir buildings additionally plot the TABS and convective demands in separate subplots
            if "tabsplusair" in bldg.name:
                # operative temperature
                # eigentlich überflüssig
                """fig10, (ax14) = plt.subplots()
                ax14.plot(data.loc[:, "Temperatur"].resample("D").mean(), linewidth=0.3)
                ax14.set_title("Operative Temperatur")
                ax14.set_ylabel('Temperatur in [°C]')
                # ax14.set_xlabel('Zeit')
                ax14.set_ylim([18, 28])
                ax14.margins(0.01)
                # ax14.xaxis.set_minor_locator(minormonths)
                ax14.xaxis.set_major_locator(locator)
                ax14.xaxis.set_major_formatter(formatter)

                plt.tight_layout()
                plt.savefig(os.path.join(output_path, "daily_single", bldg.name + "_temp_TABS+_D_plot.pdf"), dpi=200)
                plt.close("all")
                """
                # tabs demands
                fig11, (ax15) = plt.subplots()
                ax15.plot(data.loc[:, "tabs_heat_demand"].resample("D").mean(), linewidth=0.3, label="Wärmeleistung", color="r")
                ax15.plot(data.loc[:, "tabs_cool_demand"].resample("D").mean(), linewidth=0.3, label="Kälteleistung")
                ax15.set_title("TABS Heiz- und Kühllast")
                ax15.set_ylabel('Leistung in [kW]')
                # ax15.set_xlabel('Zeit')
                ax15.set_ylim(auto=True)
                # ax15.set_ylim([0, 5000])
                # ax15.set_xlim([5000, 8760])
                # ax15.autoscale()
                ax15.margins(0.01)
                # ax15.xaxis.set_minor_locator(minormonths)
                ax15.xaxis.set_major_locator(locator)
                ax15.xaxis.set_major_formatter(formatter)

                plt.tight_layout()
                plt.savefig(os.path.join(output_path, "daily_single", bldg.name + "_TABS_demand_TABS+_D_plot.pdf"), dpi=200)
                plt.close("all")

                # convective demands
                fig12, (ax16) = plt.subplots()
                ax16.plot(data.loc[:, "convective_heat_demand"].resample("D").mean(), linewidth=0.3, label="Wärmeleistung", color="r")
                ax16.plot(data.loc[:, "convective_cool_demand"].resample("D").mean(), linewidth=0.3, label="Kälteleistung")
                ax16.set_title("Zusatz Heiz- und Kühllast")
                ax16.set_ylabel('Leistung in [kW]')
                # ax16.set_xlabel('Zeit')
                ax16.set_ylim(auto=True)
                ax16.margins(0.01)
                # ax16.xaxis.set_minor_locator(minormonths)
                ax16.xaxis.set_major_locator(locator)
                ax16.xaxis.set_major_formatter(formatter)

                plt.tight_layout()
                plt.savefig(os.path.join(output_path, "daily_single", bldg.name + "_plus_demand_TABS+_D_plot.pdf"), dpi=200)
                plt.close("all")

            # Use this to slice your simulation results, to the desired timespan
            # data = data.drop(data.index[0:240])
            # data = data.drop(data.index[1200:8760])
            data = data.drop(data.index[0:240])
            data = data.drop(data.index[408:8760])

            # plot the indoor temperature and heating/cooling demand for day 10 to day 50 in two subplots
            fig13, (ax17, ax18) = plt.subplots(2)
            ax17.plot(data.loc[:, "Temperatur"], linewidth=0.3)
            ax17.set_title("Operative Temperatur")
            ax17.set_ylabel('Temperatur in [°C]')
            ax17.set_ylim([19, 25])
            # ax17.set_xlim([10, 50])
            ax17.margins(0.01)
            ax17.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
            ax17.xaxis.set_major_locator(mdates.DayLocator(interval=2))
            ax17.xaxis.set_major_formatter(format)
            ax18.plot(data.loc[:, "Wärmeleistung"], linewidth=0.3, label="Wärmeleistung", color="r")
            ax18.plot(-data.loc[:, "Kälteleistung"], linewidth=0.3, label="Kälteleistung")
            ax18.set_title("Heiz- und Kühllast")
            ax18.set_ylabel('Leistung in [kW]')
            #ax18.set_xlabel('Zeit')
            ax18.set_ylim([0, 45])
            # ax18.set_xlim([10, 50])
            ax18.margins(0.01)
            ax18.xaxis.set_minor_locator(mdates.DayLocator(interval=1))
            ax18.xaxis.set_major_locator(mdates.DayLocator(interval=2))
            ax18.xaxis.set_major_formatter(format)

            # plt.grid(color='green', linestyle='--', linewidth=0.1)
            plt.tight_layout()
            #plt.savefig(os.path.join(output_path4, bldg.name + "_day10-20_plot.pdf"), dpi=200)
            plt.savefig(os.path.join(output_path4, bldg.name + "_day10-20_plot.png"), dpi=200)
            plt.close("all")

            conlocator = mdates.AutoDateLocator(minticks=3, maxticks=7)
            conformatter = mdates.ConciseDateFormatter(conlocator)
            """
            # plot the indoor temperature and heating/cooling demand for day 10 to day 50 in two subplots
            fig14, (ax19, ax20) = plt.subplots(2)
            ax19.plot(data.loc[:, "Temperatur"].resample("D").mean(), linewidth=0.3)
            ax19.set_title("Operative Temperatur")
            ax19.set_ylabel('Temperatur in [°C]')
            ax19.set_ylim([18, 30])
            # ax17.set_xlim([10, 50])
            ax19.margins(0.01)
            # ax19.xaxis.set_minor_locator(mdates.DayLocator(interval=5))
            # ax19.xaxis.set_minor_formatter(mdates.DateFormatter("%d"))
            ax19.xaxis.set_major_locator(conlocator)
            ax19.xaxis.set_major_formatter(conformatter)
            ax20.plot(data.loc[:, "Wärmeleistung"].resample("D").mean(), linewidth=0.3, label="Wärmeleistung", color="r")
            ax20.plot(-data.loc[:, "Kälteleistung"].resample("D").mean(), linewidth=0.3, label="Kälteleistung")
            ax20.set_title("Heiz- und Kühllast")
            ax20.set_ylabel('Leistung in [kW]')
            # ax20.set_xlabel('Zeit')
            # ax18.set_ylim([0, 5000])
            # ax18.set_xlim([10, 50])
            ax20.margins(0.01)
            # ax20.xaxis.set_minor_locator(mdates.DayLocator(interval=5))
            # ax20.xaxis.set_minor_formatter(mdates.DateFormatter("%d"))
            ax20.xaxis.set_major_locator(conlocator)
            ax20.xaxis.set_major_formatter(conformatter)

            # plt.grid(color='green', linestyle='--', linewidth=0.1)
            plt.tight_layout()
            plt.savefig(os.path.join(output_path4, bldg.name + "_sliced_day10-50_plot.pdf"), dpi=200)
            plt.close("all")
            """

        except BaseException:
            # Dymola has strange exceptions
            print(
                "Reading results of building {} failed, "
                "please check result file".format(bldg.name)
            )
            # raise Exception("Results Error!")
            continue

    print("Plots done. That's it! :)")

        #ax.plot(heat_demand, linewidth=0.5, label="Wärme", color='r')
        #ax.plot(cool_demand, linewidth=0.5, label="Kälte", color='b')
        #ax.set_ylim([-5000, 5000])
        #ax.set_xlim([0, 8760])

        #ax.legend(loc=1.0, borderaxespad=0.2)
        #ax.set_title('Bedarfe')
        # ax.plot([0, 8760], [0, 0], linestyle='--', linewidth=0.5, color='black')

        #plt.savefig(bldg.name + 'Bedarf.png', dpi=200, transparent=True)

def excel_export(buildings, csv_path, output_path):
    """Create xlsx-file containing temperatures and demands of buildings.

    Parameters
    ----------
    buildings : prj.buildings
        load TEASER bldgs from a pickle project file
    csv_path : str
        Path where hourly demands created by MA_cwe_2_analyse_results.py are stored
    output_path : str
        Path where output files should be stored

    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    data = pd.DataFrame(index=pd.date_range(
        start=datetime.datetime(2021, 1, 1, 0, 0, 0),
        end=datetime.datetime(2021, 12, 31, 23, 55),
        freq="H", ))

    for bldg in buildings:
        try:
            print("reading building {}".format(bldg.name))
            # read hourly demands
            heat_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_heat.csv"))
            cool_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_cool.csv"))
            temp_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_temp.csv"))

            # drop the first 4 days of the data
            # you also have to change the index of data = pd.DataFrame (!!)
            # heat_data = heat_data.drop(heat_data.index[0:96])
            # cool_data = cool_data.drop(cool_data.index[0:96])
            # temp_data = temp_data.drop(temp_data.index[0:96])

            # office buildings are divided in 6 zones, the temperature for each zone are multiplied with the
            # zone area factor to calculate one indoor temperature for the whole building
            if "Office" in bldg.name:
                data.loc[:, bldg.name + " TOpe"] = ((temp_data.loc[:, bldg.name + " TOpe[1]"].values * 0.5 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TOpe[2]"].values * 0.25 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TOpe[3]"].values * 0.15 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TOpe[4]"].values * 0.04 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TOpe[5]"].values * 0.04 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TOpe[6]"].values * 0.02 * bldg.net_leased_area) / bldg.net_leased_area) - 273.15
            else:
                data.loc[:, bldg.name + " TOpe"] = temp_data.loc[:, bldg.name + " TOpe"].values - 273.15

            data.loc[:, bldg.name + " PHeat"] = heat_data.loc[:, bldg.name + " PHeat"]
            if "tabsplusair" in bldg.name:
                data.loc[:, bldg.name + " TABS_H"] = heat_data.loc[:, bldg.name + " tabsHeatingPower"]
                data.loc[:, bldg.name + " Convective_H"] = heat_data.loc[:, bldg.name + " pITempHeatRem.y"]
            data.loc[:, bldg.name + " PCool"] = cool_data.loc[:, bldg.name + " PCool"]
            if "tabsplusair" in bldg.name:
                data.loc[:, bldg.name + " TABS_C"] = cool_data.loc[:, bldg.name + " tabsCoolingPower"]
                data.loc[:, bldg.name + " Convective_C"] = cool_data.loc[:, bldg.name + " pITempCoolRem.y"]

            """
            if "EFH" in bldg.name:
                results.loc[bldg.name, "Type"] = "EFH"
            elif "MFH" in bldg.name:
                results.loc[bldg.name, "Type"] = "MFH"
            elif "Office" in bldg.name:
                results.loc[bldg.name, "Type"] = "Office"
            if "radiator" in bldg.name:
                results.loc[bldg.name, "System"] = "Radiator"
            elif "convective" in bldg.name:
                results.loc[bldg.name, "System"] = "Convective"
            elif "panel" in bldg.name:
                results.loc[bldg.name, "System"] = "Panel"
            elif "tabsplusair" in bldg.name:
                results.loc[bldg.name, "System"] = "TABSplusAir"
    
            results.loc[bldg.name, "Year of construction"] = bldg.year_of_construction
            results.loc[bldg.name, "Net area"] = bldg.net_leased_area
            #results.loc[bldg.name, "Footprint area"] = bldg.ground_floor_geo["GroundFloor"]["area"]
            #results.loc[bldg.name, "Volume"] = bldg.volume
            results.loc[bldg.name, "A/V"] = bldg.library_attr.total_surface_area / bldg.volume
            results.loc[bldg.name, "Construction type"] = bldg.construction_type
            """

        except BaseException:
            # Dymola has strange exceptions
            print(
                "Reading results of building {} failed, "
                "please check result file".format(bldg.name)
            )
            # raise Exception("Results Error!")
            continue

    data.to_csv(os.path.join(output_path, "buildings_temp_demands.csv"))
    data.to_excel(os.path.join(output_path, "buildings_excel_temp_demands.xlsx"))
    print("Export done! :)")

def boxplot_results(buildings, csv_path, output_path):
    """Create plots of heating, cooling and temperature time series from .csv
    files with hourly demands created by MA_cwe_2_analyse_results.py

    Parameters
    ----------
    buildings : prj.buildings
        load TEASER bldgs from a pickle project file
    csv_path : str
        Path where .csv files are be stored.
    output_path : str
        Path where plots should be stored.

    """
    boxplot_path = os.path.join(output_path, "boxplot")

    if not os.path.exists(boxplot_path):
        os.makedirs(boxplot_path)

    # define data frames for each building type and construction year
    """
    d_resample_heat_EFH_90 = pd.DataFrame()
    d_resample_heat_MFH_90 = pd.DataFrame()
    d_resample_heat_Office_90 = pd.DataFrame()
    d_resample_heat_EFH_10 = pd.DataFrame()
    d_resample_heat_MFH_10 = pd.DataFrame()
    d_resample_heat_Office_10 = pd.DataFrame()
    d_resample_spec_heat_EFH_90 = pd.DataFrame()
    d_resample_spec_heat_MFH_90 = pd.DataFrame()
    d_resample_spec_heat_Office_90 = pd.DataFrame()
    d_resample_spec_heat_EFH_10 = pd.DataFrame()
    d_resample_spec_heat_MFH_10 = pd.DataFrame()
    d_resample_spec_heat_Office_10 = pd.DataFrame()
    """
    d_resample_heat_EFH_1990_100 = pd.DataFrame()
    d_resample_heat_MFH_1990_1000 = pd.DataFrame()
    d_resample_heat_Office_1990_3000 = pd.DataFrame()
    d_resample_heat_EFH_1990_200 = pd.DataFrame()
    d_resample_heat_MFH_1990_2000 = pd.DataFrame()
    d_resample_heat_Office_1990_5000 = pd.DataFrame()
    d_resample_heat_EFH_2010_100 = pd.DataFrame()
    d_resample_heat_MFH_2010_1000 = pd.DataFrame()
    d_resample_heat_Office_2010_3000 = pd.DataFrame()
    d_resample_heat_EFH_2010_200 = pd.DataFrame()
    d_resample_heat_MFH_2010_2000 = pd.DataFrame()
    d_resample_heat_Office_2010_5000 = pd.DataFrame()
    d_resample_spec_heat_EFH_1990_100 = pd.DataFrame()
    d_resample_spec_heat_MFH_1990_1000 = pd.DataFrame()
    d_resample_spec_heat_Office_1990_3000 = pd.DataFrame()
    d_resample_spec_heat_EFH_1990_200 = pd.DataFrame()
    d_resample_spec_heat_MFH_1990_2000 = pd.DataFrame()
    d_resample_spec_heat_Office_1990_5000 = pd.DataFrame()
    d_resample_spec_heat_EFH_2010_100 = pd.DataFrame()
    d_resample_spec_heat_MFH_2010_1000 = pd.DataFrame()
    d_resample_spec_heat_Office_2010_3000 = pd.DataFrame()
    d_resample_spec_heat_EFH_2010_200 = pd.DataFrame()
    d_resample_spec_heat_MFH_2010_2000 = pd.DataFrame()
    d_resample_spec_heat_Office_2010_5000 = pd.DataFrame()

    for bldg in buildings:

        print("reading building {}".format(bldg.name))
        # read hourly demands
        heat_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_heat.csv"), index_col=0)
        cool_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_cool.csv"), index_col=0)

        data = pd.DataFrame(
            index=pd.date_range(
                start=datetime.datetime(2021, 1, 1, 0, 0, 0),
                end=datetime.datetime(2021, 12, 31, 23, 55),
                freq="H", ),
            columns=["Wärmeleistung", "Kälteleistung", "Spez Wärmeleistung"], )

        # divide demands by 1000 to get kW
        data.loc[:, "Wärmeleistung"] = heat_data.loc[:, bldg.name + " PHeat"].values / 1000
        data.loc[:, "Kälteleistung"] = -cool_data.loc[:, bldg.name + " PCool"].values / 1000

        # divide demands by building net leased area to get W/m^2
        data.loc[:, "Spez Wärmeleistung"] = heat_data.loc[:, bldg.name + " PHeat"].values / bldg.net_leased_area

        # resample data to daily mean values and filter out top "x" values
        d_resample_heat = data.loc[:, "Wärmeleistung"].resample('D').max().nlargest(50, keep='all')
        d_resample_spec_heat = data.loc[:, "Spez Wärmeleistung"].resample('D').max().nlargest(50, keep='all')

        # drop datetime index
        d_resample_heat.reset_index(drop=True, inplace=True)
        d_resample_spec_heat.reset_index(drop=True, inplace=True)

        # set parameter for later use in column name
        if "radiator" in bldg.name:
            system = "rad"
        elif "panel" in bldg.name:
            system = "panel"
        elif "convective" in bldg.name:
            system = "conv"
        elif "tabs" in bldg.name:
            system = "tabs+"

        if "heavy" in bldg.name:
            type = "h"
        elif "light" in bldg.name:
            type = "l"

        # group buildings by building types and construction year
        if "EFH" in bldg.name:
            if "1990" in bldg.name:
                if "100" in bldg.name:
                    d_resample_heat_EFH_1990_100.loc[:, system + "_" + type] = d_resample_heat
                    d_resample_spec_heat_EFH_1990_100.loc[:, system + "_" + type] = d_resample_spec_heat
                elif "200" in bldg.name:
                    d_resample_heat_EFH_1990_200.loc[:, system + "_" + type] = d_resample_heat
                    d_resample_spec_heat_EFH_1990_200.loc[:, system + "_" + type] = d_resample_spec_heat
            elif "2010" in bldg.name:
                if "100" in bldg.name:
                    d_resample_heat_EFH_2010_100.loc[:, system + "_" + type] = d_resample_heat
                    d_resample_spec_heat_EFH_2010_100.loc[:, system + "_" + type] = d_resample_spec_heat
                elif "200" in bldg.name:
                    d_resample_heat_EFH_2010_200.loc[:, system + "_" + type] = d_resample_heat
                    d_resample_spec_heat_EFH_2010_200.loc[:, system + "_" + type] = d_resample_spec_heat

        if "MFH" in bldg.name:
            if "1990" in bldg.name:
                if "1000" in bldg.name:
                    d_resample_heat_MFH_1990_1000.loc[:, system + "_" + type] = d_resample_heat
                    d_resample_spec_heat_MFH_1990_1000.loc[:, system + "_" + type] = d_resample_spec_heat
                elif "2000" in bldg.name:
                    d_resample_heat_MFH_1990_2000.loc[:, system + "_" + type] = d_resample_heat
                    d_resample_spec_heat_MFH_1990_2000.loc[:, system + "_" + type] = d_resample_spec_heat
            elif "2010" in bldg.name:
                if "1000" in bldg.name:
                    d_resample_heat_MFH_2010_1000.loc[:, system + "_" + type] = d_resample_heat
                    d_resample_spec_heat_MFH_2010_1000.loc[:, system + "_" + type] = d_resample_spec_heat
                elif "2000" in bldg.name:
                    d_resample_heat_MFH_2010_2000.loc[:, system + "_" + type] = d_resample_heat
                    d_resample_spec_heat_MFH_2010_2000.loc[:, system + "_" + type] = d_resample_spec_heat

        if "Office" in bldg.name:
            if "1990" in bldg.name:
                if "3000" in bldg.name:
                    d_resample_heat_Office_1990_3000.loc[:, system + "_" + type] = d_resample_heat
                    d_resample_spec_heat_Office_1990_3000.loc[:, system + "_" + type] = d_resample_spec_heat
                elif "5000" in bldg.name:
                    d_resample_heat_Office_1990_5000.loc[:, system + "_" + type] = d_resample_heat
                    d_resample_spec_heat_Office_1990_5000.loc[:, system + "_" + type] = d_resample_spec_heat
            elif "2010" in bldg.name:
                if "3000" in bldg.name:
                    d_resample_heat_Office_2010_3000.loc[:, system + "_" + type] = d_resample_heat
                    d_resample_spec_heat_Office_2010_3000.loc[:, system + "_" + type] = d_resample_spec_heat
                elif "5000" in bldg.name:
                    d_resample_heat_Office_2010_5000.loc[:, system + "_" + type] = d_resample_heat
                    d_resample_spec_heat_Office_2010_5000.loc[:, system + "_" + type] = d_resample_spec_heat

        """
        # group buildings by building types and construction year
        if "EFH" in bldg.name:
            if "1990" in bldg.name:
                d_resample_heat_EFH_90.loc[:, system + "_" + type] = d_resample_heat
                d_resample_spec_heat_EFH_90.loc[:, system + "_" + type] = d_resample_spec_heat
            elif "2010" in bldg.name:
                d_resample_heat_EFH_10.loc[:, system + "_" + type] = d_resample_heat
                d_resample_spec_heat_EFH_10.loc[:, system + "_" + type] = d_resample_spec_heat
        if "MFH" in bldg.name:
            if "1990" in bldg.name:
                d_resample_heat_MFH_90.loc[:, system + "_" + type] = d_resample_heat
                d_resample_spec_heat_MFH_90.loc[:, system + "_" + type] = d_resample_spec_heat
            elif "2010" in bldg.name:
                d_resample_heat_MFH_10.loc[:, system + "_" + type] = d_resample_heat
                d_resample_spec_heat_MFH_10.loc[:, system + "_" + type] = d_resample_spec_heat
        if "Office" in bldg.name:
            if "1990" in bldg.name:
                d_resample_heat_Office_90.loc[:, system + "_" + type] = d_resample_heat
                d_resample_spec_heat_Office_90.loc[:, system + "_" + type] = d_resample_spec_heat
            elif "2010" in bldg.name:
                d_resample_heat_Office_10.loc[:, system + "_" + type] = d_resample_heat
                d_resample_spec_heat_Office_10.loc[:, system + "_" + type] = d_resample_spec_heat
        """
    """   
    # rearrange plots to group heavy and light buildings
    #d_resample_heat_EFH_90 = d_resample_heat_EFH_90[["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    #d_resample_spec_heat_EFH_90 = d_resample_spec_heat_EFH_90[["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    #d_resample_heat_EFH_10 = d_resample_heat_EFH_10[["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    #d_resample_spec_heat_EFH_10 = d_resample_spec_heat_EFH_10[["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_MFH_90 = d_resample_heat_MFH_90[["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_MFH_90 = d_resample_spec_heat_MFH_90[["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_MFH_10 = d_resample_heat_MFH_10[["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_MFH_10 = d_resample_spec_heat_MFH_10[["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_Office_90 = d_resample_heat_Office_90[["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_Office_90 = d_resample_spec_heat_Office_90[["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_Office_10 = d_resample_heat_Office_10[["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_Office_10 = d_resample_spec_heat_Office_10[["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    """

    # rearrange plots to group heavy and light buildings
    d_resample_heat_EFH_1990_100 = d_resample_heat_EFH_1990_100[
        ["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_EFH_1990_100 = d_resample_spec_heat_EFH_1990_100[
        ["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_EFH_2010_100 = d_resample_heat_EFH_2010_100[
        ["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_EFH_2010_100 = d_resample_spec_heat_EFH_2010_100[
        ["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_EFH_1990_200 = d_resample_heat_EFH_1990_200[
        ["rad_h", "tabs+_h", "panel_h", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_EFH_1990_200 = d_resample_spec_heat_EFH_1990_200[
        ["rad_h", "tabs+_h", "panel_h", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_EFH_2010_200 = d_resample_heat_EFH_2010_200[
        ["rad_h", "tabs+_h", "panel_h", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_EFH_2010_200 = d_resample_spec_heat_EFH_2010_200[
        ["rad_h", "tabs+_h", "panel_h", "rad_l", "tabs+_l", "panel_l"]]

    d_resample_heat_MFH_1990_1000 = d_resample_heat_MFH_1990_1000[
        ["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_MFH_1990_1000 = d_resample_spec_heat_MFH_1990_1000[
        ["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_MFH_2010_1000 = d_resample_heat_MFH_2010_1000[
        ["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_MFH_2010_1000 = d_resample_spec_heat_MFH_2010_1000[
        ["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_MFH_1990_2000 = d_resample_heat_MFH_1990_2000[
        ["rad_h", "tabs+_h", "panel_h", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_MFH_1990_2000 = d_resample_spec_heat_MFH_1990_2000[
        ["rad_h", "tabs+_h", "panel_h", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_MFH_2010_2000 = d_resample_heat_MFH_2010_2000[
        ["rad_h", "tabs+_h", "panel_h", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_MFH_2010_2000 = d_resample_spec_heat_MFH_2010_2000[
        ["rad_h", "tabs+_h", "panel_h", "rad_l", "tabs+_l", "panel_l"]]

    d_resample_heat_Office_1990_3000 = d_resample_heat_Office_1990_3000[
        ["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_Office_1990_3000 = d_resample_spec_heat_Office_1990_3000[
        ["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_Office_2010_3000 = d_resample_heat_Office_2010_3000[
        ["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_Office_2010_3000 = d_resample_spec_heat_Office_2010_3000[
        ["conv_h", "rad_h", "tabs+_h", "panel_h", "conv_l", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_Office_1990_5000 = d_resample_heat_Office_1990_5000[
        ["rad_h", "tabs+_h", "panel_h", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_Office_1990_5000 = d_resample_spec_heat_Office_1990_5000[
        ["rad_h", "tabs+_h", "panel_h", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_heat_Office_2010_5000 = d_resample_heat_Office_2010_5000[
        ["rad_h", "tabs+_h", "panel_h", "rad_l", "tabs+_l", "panel_l"]]
    d_resample_spec_heat_Office_2010_5000 = d_resample_spec_heat_Office_2010_5000[
        ["rad_h", "tabs+_h", "panel_h", "rad_l", "tabs+_l", "panel_l"]]

    # plot max heat per building type and construction year
    fig, ax = plt.subplots()
    ax.boxplot(d_resample_heat_EFH_1990_100, labels=d_resample_heat_EFH_1990_100.columns)
    ax.set_title("EFH 1990 100 $m^2$")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_1990_100_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_EFH_1990_200, labels=d_resample_heat_EFH_1990_200.columns)
    ax.set_title("EFH 1990 200 $m^2$")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_1990_200_boxplot.pdf"), dpi=200)
    ax.clear()
    # ax.boxplot(d_resample_heat_EFH_10, labels=d_resample_heat_EFH_10.columns)
    ax.boxplot(d_resample_heat_EFH_2010_100, labels=d_resample_heat_EFH_2010_100.columns)
    ax.set_title("EFH 2010 100 $m^2$")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_2010_100_boxplot.pdf"), dpi=200)
    ax.clear()
    # ax.boxplot(d_resample_heat_EFH_10, labels=d_resample_heat_EFH_10.columns)
    ax.boxplot(d_resample_heat_EFH_2010_200, labels=d_resample_heat_EFH_2010_200.columns)
    ax.set_title("EFH 2010 200 $m^2$")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_2010_200_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_MFH_1990_1000, labels=d_resample_heat_MFH_1990_1000.columns)
    ax.set_title("MFH 1990 1000 $m^2$")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "MFH_1990_1000_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_MFH_1990_2000, labels=d_resample_heat_MFH_1990_2000.columns)
    ax.set_title("MFH 1990 2000 $m^2$")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "MFH_1990_2000_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_MFH_2010_1000, labels=d_resample_heat_MFH_2010_1000.columns)
    ax.set_title("MFH 2010 1000 $m^2$")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "MFH_2010_1000_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_MFH_2010_2000, labels=d_resample_heat_MFH_2010_2000.columns)
    ax.set_title("MFH 2010 2000 $m^2$")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "MFH_2010_2000_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_Office_1990_3000, labels=d_resample_heat_Office_1990_3000.columns)
    ax.set_title("Office 1990 3000 $m^2$")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "Office_1990_3000_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_Office_1990_5000, labels=d_resample_heat_Office_1990_5000.columns)
    ax.set_title("Office 1990 5000 $m^2$")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "Office_1990_5000_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_Office_2010_3000, labels=d_resample_heat_Office_2010_3000.columns)
    ax.set_title("Office 2010 3000 $m^2$")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "Office_2010_3000_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_Office_2010_5000, labels=d_resample_heat_Office_2010_5000.columns)
    ax.set_title("Office 2010 5000 $m^2$")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "Office_2010_5000_boxplot.pdf"), dpi=200)
    ax.clear()

    # plot spec max heat per building type and construction year
    fig2, ax2 = plt.subplots()
    ax2.boxplot(d_resample_spec_heat_EFH_1990_100, labels=d_resample_spec_heat_EFH_1990_100.columns)
    ax2.set_title("EFH 1990 100 $m^2$")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_1990_100_spec_boxplot.pdf"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_EFH_1990_200, labels=d_resample_spec_heat_EFH_1990_200.columns)
    ax2.set_title("EFH 1990 200 $m^2$")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_1990_200_spec_boxplot.pdf"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_EFH_2010_100, labels=d_resample_spec_heat_EFH_2010_100.columns)
    ax2.set_title("EFH 2010 100 $m^2$")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_2010_100_spec_boxplot.pdf"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_EFH_2010_200, labels=d_resample_spec_heat_EFH_2010_200.columns)
    ax2.set_title("EFH 2010 200 $m^2$")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_2010_200_spec_boxplot.pdf"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_MFH_1990_1000, labels=d_resample_spec_heat_MFH_1990_1000.columns)
    ax2.set_title("MFH 1990 1000 $m^2$")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "MFH_1990_1000_spec_boxplot.pdf"), dpi=200)
    plt.savefig(os.path.join(boxplot_path, "MFH_1990_1000_spec_boxplot.png"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_MFH_1990_2000, labels=d_resample_spec_heat_MFH_1990_2000.columns)
    ax2.set_title("MFH 1990 2000 $m^2$")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "MFH_1990_2000_spec_boxplot.pdf"), dpi=200)
    plt.savefig(os.path.join(boxplot_path, "MFH_1990_2000_spec_boxplot.png"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_MFH_2010_1000, labels=d_resample_spec_heat_MFH_2010_1000.columns)
    ax2.set_title("MFH 2010 1000 $m^2$")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "MFH_2010_1000_spec_boxplot.pdf"), dpi=200)
    plt.savefig(os.path.join(boxplot_path, "MFH_2010_1000_spec_boxplot.png"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_MFH_2010_2000, labels=d_resample_spec_heat_MFH_2010_2000.columns)
    ax2.set_title("MFH 2010 2000 $m^2$")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "MFH_2010_2000_spec_boxplot.pdf"), dpi=200)
    plt.savefig(os.path.join(boxplot_path, "MFH_2010_2000_spec_boxplot.png"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_Office_1990_3000, labels=d_resample_spec_heat_Office_1990_3000.columns)
    ax2.set_title("Office 1990 3000 $m^2$")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "Office_1990_3000_spec_boxplot.pdf"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_Office_1990_5000, labels=d_resample_spec_heat_Office_1990_5000.columns)
    ax2.set_title("Office 1990 5000 $m^2$")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "Office_1990_5000_spec_boxplot.pdf"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_Office_2010_3000, labels=d_resample_spec_heat_Office_2010_3000.columns)
    ax2.set_title("Office 2010 3000 $m^2$")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "Office_2010_3000_spec_boxplot.pdf"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_Office_2010_5000, labels=d_resample_spec_heat_Office_2010_5000.columns)
    ax2.set_title("Office 2010 5000 $m^2$")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "Office_2010_5000_spec_boxplot.pdf"), dpi=200)
    ax2.clear()

    """
    # plot max heat per building type and construction year
    fig, ax = plt.subplots()
    ax.boxplot(d_resample_heat_EFH_90, labels=d_resample_heat_EFH_90.columns)
    ax.set_title("EFH 1990")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_90_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_EFH_90, labels=d_resample_heat_EFH_90.columns)
    ax.set_title("EFH 1990")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_90_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_EFH_10, labels=d_resample_heat_EFH_10.columns)
    ax.set_title("EFH 2010")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_10_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_EFH_10, labels=d_resample_heat_EFH_10.columns)
    ax.set_title("EFH 2010")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_10_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_MFH_90, labels=d_resample_heat_MFH_90.columns)
    ax.set_title("MFH 1990")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "MFH_90_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_MFH_10, labels=d_resample_heat_MFH_10.columns)
    ax.set_title("MFH 2010")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "MFH_10_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_Office_90, labels=d_resample_heat_Office_90.columns)
    ax.set_title("Office 1990")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "Office_90_boxplot.pdf"), dpi=200)
    ax.clear()
    ax.boxplot(d_resample_heat_Office_10, labels=d_resample_heat_Office_10.columns)
    ax.set_title("Office 2010")
    ax.set_ylabel("Max Heat [kW]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "Office_10_boxplot.pdf"), dpi=200)
    ax.clear()
    
    # plot spec max heat per building type and construction year
    fig2, ax2 = plt.subplots()
    ax2.boxplot(d_resample_spec_heat_EFH_90, labels=d_resample_spec_heat_EFH_90.columns)
    ax2.set_title("EFH 1990")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_90_spec_boxplot.pdf"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_EFH_10, labels=d_resample_spec_heat_EFH_10.columns)
    ax2.set_title("EFH 2010")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "EFH_10_spec_boxplot.pdf"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_MFH_90, labels=d_resample_spec_heat_MFH_90.columns)
    ax2.set_title("MFH 1990")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "MFH_90_spec_boxplot.pdf"), dpi=200)
    plt.savefig(os.path.join(boxplot_path, "MFH_90_spec_boxplot.png"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_MFH_10, labels=d_resample_spec_heat_MFH_10.columns)
    ax2.set_title("MFH 2010")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "MFH_10_spec_boxplot.pdf"), dpi=200)
    plt.savefig(os.path.join(boxplot_path, "MFH_10_spec_boxplot.png"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_Office_90, labels=d_resample_spec_heat_Office_90.columns)
    ax2.set_title("Office 1990")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "Office_90_spec_boxplot.pdf"), dpi=200)
    ax2.clear()
    ax2.boxplot(d_resample_spec_heat_Office_10, labels=d_resample_spec_heat_Office_10.columns)
    ax2.set_title("Office 2010")
    ax2.set_ylabel("Spec Max Heat [W/$m^2$]")
    plt.tight_layout()
    plt.savefig(os.path.join(boxplot_path, "Office_10_spec_boxplot.pdf"), dpi=200)
    ax2.clear()
    #######
    d_resample_heat_EFH_90.plot(kind='box')
    set_title("Operative Temperatur")
    set_ylabel('Temperatur in [°C]')
    plt.savefig(os.path.join(boxplot_path, "EFH_90_boxplot.pdf"), dpi=200)
    plt.clf()
    d_resample_heat_MFH_90.plot(kind='box')
    plt.savefig(os.path.join(boxplot_path, "MFH_90_boxplot.pdf"), dpi=200)
    plt.clf()
    d_resample_heat_Office_90.plot(kind='box')
    plt.savefig(os.path.join(boxplot_path, "Office_90_boxplot.pdf"), dpi=200)
    plt.clf()
    d_resample_heat_EFH_10.plot(kind='box')
    plt.savefig(os.path.join(boxplot_path, "EFH_10_boxplot.pdf"), dpi=200)
    plt.clf()
    d_resample_heat_MFH_10.plot(kind='box')
    plt.savefig(os.path.join(boxplot_path, "MFH_10_boxplot.pdf"), dpi=200)
    plt.clf()
    d_resample_heat_Office_10.plot(kind='box')
    plt.savefig(os.path.join(boxplot_path, "Office_10_boxplot.pdf"), dpi=200)
    plt.close("all")
    """
    # d_resample_heat_EFH_90.to_excel(os.path.join(boxplot_path, "EFH_90.xlsx"))
    # d_resample_heat_EFH_10.to_excel(os.path.join(boxplot_path, "EFH_10.xlsx"))

def old_plot_results(heat, cool, title, output_path):
    # Very simple and basic plotting of heating and cooling time series.
    data = pd.DataFrame(
        index=pd.date_range(
            start=datetime.datetime(2021, 1, 1, 0, 0, 0),
            end=datetime.datetime(2021, 12, 31, 23, 55),
            freq="H",
        ),
        columns=["Wärmeleistung", "Kälteleistung"],
    )
    data["Wärmeleistung"] = heat.iloc[:, 1].values / 1000
    data["Kälteleistung"] = -cool.iloc[:, 1].values / 1000
    # data = data.dropna()
    fig, ax1 = plt.subplots()
    ax = sns.lineplot(
        data=data,
        hue=None,
        palette=["#407FB7", "#646567"],
        linewidth=0.5,
        ax=ax1,
    )

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m"))
    plt.ylabel("Leistung in [kW]")
    fig.tight_layout()
    fig.set_size_inches(5.9, 3.0, forward=True)

    plt.savefig(output_path, dpi=200)
    plt.clf()
    ax = sns.lineplot(
        data=data.resample("D").mean(),
        hue=None,
        palette=["#407FB7", "#646567"],
        linewidth=0.5,
    )
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m"))
    plt.title(title + " D")
    plt.savefig(output_path.replace("plt", "plt_D"), dpi=200)
    plt.close("all")
