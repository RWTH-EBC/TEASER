"""Module to read results with DymolaInterface."""

import datetime
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#plt.style.use(os.path.join("D:\\", "tbl-cwe", "Repos", "TEASER", "teaser", "examples", "utils", "ebc.paper.mplstyle"))
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
        # bldg.name
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
        heat.to_excel(os.path.join(csv_path, bldg + "_excel_heat.xlsx"))
        cool.to_excel(os.path.join(csv_path, bldg + "_excel_cool.xlsx"))

        temp.to_csv(os.path.join(csv_path, bldg + "_temp.csv"))
        temp.to_excel(os.path.join(csv_path, bldg + "_excel_temp.xlsx"))

    dymola.close()

def calc_results(buildings, csv_path, output_path):
    """Create csv-file containing KPIs of buildings.

    Parameters
    ----------
    buildings : list of TEASER bldgs
    csv_path : str
        Path where hourly demands created by MA_cwe_2_analyse_results.py are stored
    output_path : str
        Path where output files should be stored

    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    results = pd.DataFrame()

    for bldg in buildings:
        try:
            print("reading building {}".format(bldg.name))
            # read hourly demands
            heat_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_heat.csv"))
            cool_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_cool.csv"))
            # temp_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_temp.csv"))

            # drop the first 4 days of the data
            heat_data = heat_data.drop(heat_data.index[0:96])
            cool_data = cool_data.drop(cool_data.index[0:96])
            #temp_data = temp_data.drop(temp_data.index[0:96])

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

    results.to_csv(os.path.join(output_path, "buildings_calc.csv"))
    results.to_excel(os.path.join(output_path, "buildings_excel_calc.xlsx"))
    print("Calculations done! :)")

def plot_results(buildings, csv_path, output_path):
    """Create plots of heating, cooling and temperature time series from .csv
    files with hourly demands created by MA_cwe_2_analyse_results.py

    Parameters
    ----------
    buildings : pickle_prj.buildings
    csv_path : str
        Path where .csv files are be stored.
    output_path : str
        Path where plots should be stored.

    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)

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

            data.loc[:, "Wärmeleistung"] = heat_data.loc[:, bldg.name + " PHeat"].values / 1000
            data.loc[:, "Kälteleistung"] = -cool_data.loc[:, bldg.name + " PCool"].values / 1000

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

            data = data.drop(data.index[0:96])
            """
            #plot parameters
            sidewidth = 6.224
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
            matplotlib.rcParams.update(params)
            """
            days = mdates.DayLocator(interval=10)
            weeks = mdates.DayLocator(interval=7)
            minormonths = mdates.MonthLocator(interval=1)
            majormonths = mdates.MonthLocator(interval=2)
            format = mdates.DateFormatter("%d-%m")
            format2 = mdates.DateFormatter("%d")

            print("plotting building {}".format(bldg.name))
            fig, (ax1, ax2) = plt.subplots(2)
            #ax1.plot(temp_ope, linewidth=0.3)
            ax1.plot(data.loc[:, "Temperatur"], linewidth=0.3)
            ax1.set_title("Operative Temperatur")
            ax1.set_ylabel('Temperatur in [°C]')
            ax1.margins(0.01)
            ax1.xaxis.set_minor_locator(minormonths)
            ax1.xaxis.set_major_locator(majormonths)
            ax1.xaxis.set_major_formatter(format)
            #ax2.plot(heat_demand, linewidth=0.3, label="Wärmeleistung", color="r")
            #ax2.plot(cool_demand, linewidth=0.3, label="Kälteleistung", color="b")
            ax2.plot(data.loc[:, "Wärmeleistung"], linewidth=0.3, label="Wärmeleistung", color="r")
            ax2.plot(data.loc[:, "Kälteleistung"], linewidth=0.3, label="Kälteleistung", color="b")
            ax2.set_title("Heiz- und Kühllast")
            ax2.set_ylabel('Leistung in [kWh/h]')
            #ax2.set_xlabel('Simulationszeit in h')
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

            if "tabsplusair" in bldg.name:
                #data.loc[:, "tabs_heat_demand"] = heat_data.loc[:, bldg.name + " tabsHeatingPower"].values / 1000
                #tabs_cool_demand = -cool_data.loc[:, bldg.name + " tabsCoolingPower"].values / 1000
                #convective_heat_demand = heat_data.loc[:, bldg.name + " pITempHeatRem.y"].values / 1000
                #convective_cool_demand = -cool_data.loc[:, bldg.name + " pITempCoolRem.y"].values / 1000

                fig2, (ax3, ax4, ax5) = plt.subplots(3)
                ax3.plot(data.loc[:, "Temperatur"], linewidth=0.3)
                ax3.set_title("Operative Temperatur")
                ax3.set_ylabel('Temperatur in [°C]')
                ax3.margins(0.01)
                ax3.xaxis.set_minor_locator(minormonths)
                ax3.xaxis.set_major_locator(majormonths)
                ax3.xaxis.set_major_formatter(format)
                ax4.plot(data.loc[:, "tabs_heat_demand"], linewidth=0.3, label="Wärmeleistung", color="r")
                ax4.plot(data.loc[:, "tabs_cool_demand"], linewidth=0.3, label="Kälteleistung", color="b")
                ax4.set_title("TABS Heiz- und Kühllast")
                ax4.set_ylabel('Leistung in [kWh/h]')
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
                ax5.plot(data.loc[:, "convective_cool_demand"], linewidth=0.3, label="Kälteleistung", color="b")
                ax5.set_title("Zusatz Heiz- und Kühllast")
                ax5.set_ylabel('Leistung in [kWh/h]')
                #ax5.set_xlabel('Simulationszeit in h')
                ax5.set_ylim(auto=True)
                ax5.margins(0.01)
                ax5.xaxis.set_minor_locator(minormonths)
                ax5.xaxis.set_major_locator(majormonths)
                ax5.xaxis.set_major_formatter(format)

                plt.tight_layout()
                plt.savefig(os.path.join(output_path, bldg.name + "TABS+_plot.pdf"), dpi=200)
                plt.close("all")

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
    plt.ylabel("Leistung in [kWh/h]")
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
