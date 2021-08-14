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
          'axes.grid': True,
          'grid.color': '#DDDDDD',
          'figure.figsize': (sitewidth, sitewidth / 16 * 9),
          'figure.subplot.hspace': 0.3,
          'axes.ymargin': 0.1,
          }
matplotlib.rc('font', **font)
matplotlib.rcParams.update(params)
#'axes.grid.axis': 'y'
# parameters for axis definition
months_locator = mdates.MonthLocator(
    bymonth=None,
    bymonthday=15,
    interval=1,
    tz=None)
allmonths = mdates.MonthLocator()
months_formatter = mdates.DateFormatter("%b")
minor_days = mdates.DayLocator(interval=1)
major_days = mdates.DayLocator(interval=1)
minormonths = mdates.MonthLocator(interval=1)
majormonths = mdates.MonthLocator(interval=2)
majorhour = mdates.HourLocator(interval=24)
minorhour = mdates.HourLocator(interval=12)
format = mdates.DateFormatter("%d")
locator = matplotlib.dates.MonthLocator(
    bymonth=None,
    bymonthday=15,
    interval=1,
    tz=None)

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

    results.index = pd.date_range(
        datetime.datetime(2021, 1, 1), periods=361, freq="H")
    return results


if __name__ == '__main__':

    # set your file_name here
    file_name = "MFHtabs1990heavy1000"

    ### set path to your workspace here ###
    workspace = os.path.join("D:\\", "tbl-cwe", "Plots_Kap_3_step_response", "Sprungantwort_final")
    print("Your workspace is set to: " + workspace)

    plot_path = os.path.join(workspace, "chapter3_step_response")
    if not os.path.exists(plot_path):
        os.makedirs(plot_path)
    print("Your plots are stored in: " + plot_path)

    csv_results_path = os.path.join(workspace, "csv_results", )
    print("Your .csv  files are stored in: " + csv_results_path)

    #################################################
    ### set path to desired sim_results_file here ###
    sim_results_file_path = os.path.join(workspace, file_name + ".mat")
    print("Your .mat file is stored in: " + sim_results_file_path)

    ###############################################
    ### set list of simulation result variables ###
    res_list = ['multizone.TOpe[1]',
                'multizone.TAir[1]',
                'multizone.TRad[1]',
                'multizone.PHeater[1]'
                ]

    res = read_results(signals=res_list,
                       index=pd.date_range(
                           datetime.datetime(2021, 1, 1), periods=361, freq="H",
                       ), results_path=sim_results_file_path)

    heat_demand = res.loc[:, 'multizone.PHeater[1]'] / 1000
    T_ope = res.loc[:, 'multizone.TOpe[1]'] - 273.15
    T_air = res.loc[:, 'multizone.TAir[1]'] - 273.15
    T_rad = res.loc[:, 'multizone.TRad[1]'] - 273.15

    fig, (ax, ax2) = plt.subplots(2)
    ax.set_ylabel('Temperatur in [°C]')
    # ax.set_xlabel('Simulationszeit in h')
    ax.plot(T_ope, linewidth=0.6, color='black')
    ax.plot(T_air, linewidth=0.6, color='blue', label='Lufttemperatur')
    ax.plot(T_rad, linewidth=0.6, color='red', label='Strahlungstemperatur')
    # ax2.plot(SolRad, linewidth=0.3, color='r')
    # ax.plot(heat_dem.values, linewidth=0.2, label="Wärme", color='r')
    # ax.plot(cool_dem.values, linewidth=0.2, label="Kälte", color='b')
    # ax.plot(ele_dem.values, linewidth=0.2, label="Strom", color='g')
    ax.set_ylim([16, 24])
    # ax.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    # ax.legend(loc=1.0, borderaxespad=0.2)
    #ax.set_title('Bedarfe')
    # ax.plot([0, 8760], [0, 0], linestyle='--', linewidth=0.5, color='black')
    #ax.grid(axis='y')

    ax.yaxis.set_major_locator(mticker.MultipleLocator(2))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(1))
    ax.xaxis.set_minor_locator(minor_days)
    ax.xaxis.set_major_locator(major_days)
    ax.xaxis.set_major_formatter(format)
    ax.margins(0)

    ax2.plot(heat_demand, linewidth=0.6, color="black")
    # ax4.plot(-data.loc[:, "Kälteleistung"], linewidth=0.5, label="Kühlleistung", color="b")
    # ax4.set_title("Heiz- und Kühllast")
    ax2.set_ylabel('Leistung [kW]')
    ax2.set_xlabel('Tage')
    ax2.set_ylim([0.0, 50.0])
    # ax2.set_xlim(datetime.datetime(2021, 1, 31, 23, 55), datetime.datetime(2021, 3, 1, 0, 0, 0))
    ax2.yaxis.set_major_locator(mticker.MultipleLocator(10))
    ax2.yaxis.set_minor_locator(mticker.MultipleLocator(5))
    ax2.xaxis.set_minor_locator(minor_days)
    ax2.xaxis.set_major_locator(major_days)
    ax2.xaxis.set_major_formatter(format)
    ax2.margins(0)
    # ax4.axvspan(datetime.datetime(2021, 4, 1, 0, 0, 0), datetime.datetime(2021, 4, 30, 23, 55),facecolor='#EDEDED')

    fig.legend(loc=9, bbox_to_anchor=(0.5, 1.0,), ncol=2)
    plt.savefig(os.path.join(plot_path, file_name + "_step_response.pdf"), dpi=200, bbox_inches="tight")
    """
    # ax.margins(0.01)
    ax.xaxis.set_major_locator(allmonths)
    ax.xaxis.set_minor_locator(months_locator)
    ax.xaxis.set_major_formatter(mticker.NullFormatter())
    ax.xaxis.set_minor_formatter(months_formatter)
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(5))
    ax.tick_params(axis="x", which="minor", length=0)

    plt.tight_layout()
    # plt.savefig(os.path.join(plot_path, 'Temperatur.png'), dpi=200, transparent=True)
    plt.savefig(os.path.join(plot_path, 'Temperatur.pdf'), dpi=200)

    # clear plot lines, keep axes
    for artist in ax.lines + ax.collections:
        artist.remove()

    #################################################################

    ax.plot(T_outdoor.resample('D').mean(), linewidth=0.6, color='black')
    # ax2.plot(SolRad.resample('D').mean(), linewidth=0.3, color='r')
    # ax.set_ylabel('Außentemperatur in °C')
    # ax.margins(0.01)
    # ax.xaxis.set_major_locator(allmonths)
    # ax.xaxis.set_minor_locator(months_locator)
    # ax.xaxis.set_major_formatter(mticker.NullFormatter())
    # ax.xaxis.set_minor_formatter(months_formatter)
    # ax.tick_params(axis="x", which="minor", length=0)
    # plt.tight_layout()
    # plt.savefig(os.path.join(plot_path, 'Temperatur_D.png'), dpi=200, transparent=True)
    plt.savefig(os.path.join(plot_path, 'Temperatur_D.pdf'), dpi=200)
    ax.clear()

    ################################################################

    ax.set_ylabel('Solarstrahlung in [W/m$^2$]')
    ax.plot(SolRad, linewidth=0.3, color="black")
    ax.margins(0.01)
    ax.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax.xaxis.set_major_locator(allmonths)
    ax.xaxis.set_minor_locator(months_locator)
    ax.xaxis.set_major_formatter(mticker.NullFormatter())
    ax.xaxis.set_minor_formatter(months_formatter)
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(100))
    ax.tick_params(axis="x", which="minor", length=0)
    plt.tight_layout()
    # plt.savefig(os.path.join(plot_path, 'Solarstrahlung.png'), dpi=200, transparent=True)
    plt.savefig(os.path.join(plot_path, 'Solarstrahlung.pdf'), dpi=200)

    # clear plot lines, keep axes
    for artist in ax.lines + ax.collections:
        artist.remove()

    ax.plot(SolRad.resample('D').mean(), linewidth=0.6, color="black")
    plt.savefig(os.path.join(plot_path, 'Solarstrahlung_D_mean.pdf'), dpi=200)
    """