import datetime

import dymola
import pandas as pd
import os
import numpy as np
import matplotlib
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import locale
locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
from dymola.dymola_interface import DymolaInterface


# read simulation result file and returns data frame for list of signals
def read_results(signals, index, results_path):

    dymola = DymolaInterface()

    dym_res = dymola.readTrajectory(
        fileName=os.path.join(results_path),
        signals=signals,
        rows=dymola.readTrajectorySize(fileName=os.path.join(results_path)))
    results = pd.DataFrame().from_records(dym_res).T
    results = results.rename(
        columns=dict(zip(results.columns.values, signals))
    )

    dymola.close()

    results = results.drop(results.index[0:8760])
    results.index = pd.date_range(
        datetime.datetime(2021, 1, 1), periods=8760, freq="H")
    return results


if __name__ == '__main__':

    # rcParams
    sitewidth = 6.224
    fontsize = 11
    font = {'family': 'serif',
            'weight': 'normal',
            'size': fontsize}
    params = {'legend.fontsize': fontsize,
              'xtick.labelsize': fontsize,
              'ytick.labelsize': fontsize,
              'axes.labelsize': fontsize,
              'axes.titlesize': fontsize,
              'axes.grid.axis': 'y',
              'axes.grid': True,
              'grid.color': '#DDDDDD',
              'figure.figsize': (sitewidth, sitewidth / 16 * 9)
              }
    matplotlib.rc('font', **font)
    matplotlib.rcParams.update(params)

    # parameters for axis definition
    months_locator = mdates.MonthLocator(
        bymonth=None,
        bymonthday=15,
        interval=1,
        tz=None)
    allmonths = mdates.MonthLocator()
    months_formatter = mdates.DateFormatter("%b")

    #######################################
    ### set path to your workspace here ###
    workspace = os.path.join("D:\\", "tbl-cwe", "Simulation", "TABS_30_mit_RT_control")
    print("Your workspace is set to: " + workspace)

    output_path = os.path.join(workspace, "calc_results")
    print("Your calculation results are stored in: " + output_path)

    plot_path = os.path.join(workspace, "special_plots")
    if not os.path.exists(plot_path):
        os.makedirs(plot_path)
    print("Your plots are stored in: " + plot_path)

    csv_results_path = os.path.join(workspace, "csv_results", )
    print("Your .csv  files are stored in: " + csv_results_path)

    #################################################
    ### set path to desired sim_results_file here ###
    sim_results_file_path = os.path.join(workspace, "sim_results", "Simulationsstudie_TABS_30_mit_RT_control", "EFHconvective1990heavy100.mat")
    print("Your .mat file is stored in: " + sim_results_file_path)

    ###############################################
    ### set list of simulation result variables ###
    res_list = ['weaDat.weaBus.TDryBul',
                'weaDat.weaBus.HGloHor'
                ]

    res = read_results(signals=res_list,
                       index=pd.date_range(
                           datetime.datetime(2021, 1, 1), periods=17520, freq="H",
                       ), results_path=sim_results_file_path )
    """
    res2 = read_results(res_list,
                       index=pd.date_range(
                           datetime.datetime(2021, 1, 1), periods=17520, freq="H"
                       file='222.mat'
                       ))
    """
    # heat_demand = res[''] / 1000
    # cool_demand = res[''] / 1000
    T_outdoor = res.loc[:, 'weaDat.weaBus.TDryBul'] - 273.15
    SolRad = res.loc[:, 'weaDat.weaBus.HGloHor']



    fig, ax = plt.subplots()
    ax.set_ylabel('Außentemperatur in °C')
    # ax2 = ax.twinx()
    # ax.set_xlabel('Simulationszeit in h')
    ax.plot(T_outdoor, linewidth=0.6)
    # ax2.plot(SolRad, linewidth=0.3, color='r')
    # ax.plot(heat_dem.values, linewidth=0.2, label="Wärme", color='r')
    # ax.plot(cool_dem.values, linewidth=0.2, label="Kälte", color='b')
    # ax.plot(ele_dem.values, linewidth=0.2, label="Strom", color='g')
    #ax.set_ylim([-0, 5000])
    #ax.set_xlim([0, 8760])
    #ax.legend(loc=1.0, borderaxespad=0.2)
    #ax.set_title('Bedarfe')
    # ax.plot([0, 8760], [0, 0], linestyle='--', linewidth=0.5, color='black')
    #ax.grid(axis='y')

    ax.margins(0.01)
    ax.xaxis.set_major_locator(allmonths)
    ax.xaxis.set_minor_locator(months_locator)
    ax.xaxis.set_major_formatter(mticker.NullFormatter())
    ax.xaxis.set_minor_formatter(months_formatter)
    ax.tick_params(axis="x", which="minor", length=0)

    plt.tight_layout()
    plt.savefig(os.path.join(plot_path, 'Temperatur.png'), dpi=200, transparent=True)
    plt.savefig(os.path.join(plot_path, 'Temperatur.pdf'), dpi=200)
    ax.clear()

    #################################################################

    ax.plot(T_outdoor.resample('D').mean(), linewidth=0.3)
    # ax2.plot(SolRad.resample('D').mean(), linewidth=0.3, color='r')
    ax.set_ylabel('Außentemperatur in °C')
    ax.margins(0.01)
    ax.xaxis.set_major_locator(allmonths)
    ax.xaxis.set_minor_locator(months_locator)
    ax.xaxis.set_major_formatter(mticker.NullFormatter())
    ax.xaxis.set_minor_formatter(months_formatter)
    ax.tick_params(axis="x", which="minor", length=0)
    plt.tight_layout()
    plt.savefig(os.path.join(plot_path, 'Temperatur_D.png'), dpi=200, transparent=True)
    plt.savefig(os.path.join(plot_path, 'Temperatur_D.pdf'), dpi=200)
    ax.clear()

    ################################################################

    ax.set_ylabel('Solarstrahlung in [W/$m^2$]')
    ax.plot(SolRad, linewidth=0.3)
    ax.margins(0.01)
    ax.xaxis.set_major_locator(allmonths)
    ax.xaxis.set_minor_locator(months_locator)
    ax.xaxis.set_major_formatter(mticker.NullFormatter())
    ax.xaxis.set_minor_formatter(months_formatter)
    ax.tick_params(axis="x", which="minor", length=0)
    plt.tight_layout()
    plt.savefig(os.path.join(plot_path, 'Solarstrahlung.png'), dpi=200, transparent=True)
    plt.savefig(os.path.join(plot_path, 'Solarstrahlung.pdf'), dpi=200)
