import datetime
import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#plt.style.use(os.path.join("D:\\", "tbl-cwe", "Repos", "TEASER", "teaser", "examples", "utils", "ebc.paper.mplstyle"))
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns
import pandas as pd
import locale
locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')
from scipy.interpolate import make_interp_spline, BSpline
from scipy.interpolate import interp1d

from statistics import mean
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
          'axes.grid.axis': 'y',
          'axes.grid': True,
          'grid.color': '#DDDDDD',
          'figure.figsize': (sitewidth, sitewidth / 16 * 9),
          'figure.subplot.hspace': 0.3,
          'axes.ymargin': 0.1,
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

# parameters for axis definition
minor_days = mdates.DayLocator(interval=1)
major_days = mdates.DayLocator(interval=5)
minormonths = mdates.MonthLocator(interval=1)
majormonths = mdates.MonthLocator(interval=2)
format = mdates.DateFormatter("%d. %b")
locator = matplotlib.dates.MonthLocator(
    bymonth=None,
    bymonthday=15,
    interval=1,
    tz=None)
formatter = mdates.DateFormatter("%b")

def plot_results_Kap_3(buildings, csv_path, output_path):
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
              'figure.figsize': (sitewidth, sitewidth / 16 * 9),
              'figure.subplot.hspace': 0.3,
              'axes.ymargin': 0.1,
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

    # parameters for axis definition
    minor_days = mdates.DayLocator(interval=1)
    major_days = mdates.DayLocator(interval=5)
    minormonths = mdates.MonthLocator(interval=1)
    majormonths = mdates.MonthLocator(interval=2)
    format = mdates.DateFormatter("%d. %b")
    locator = matplotlib.dates.MonthLocator(
        bymonth=None,
        bymonthday=15,
        interval=1,
        tz=None)
    formatter = mdates.DateFormatter("%b")

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
                data.loc[:, "TAir"] = ((temp_data.loc[:,
                                              bldg.name + " TAir[1]"].values * 0.5 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TAir[2]"].values * 0.25 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TAir[3]"].values * 0.15 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TAir[4]"].values * 0.04 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TAir[5]"].values * 0.04 * bldg.net_leased_area
                                              + temp_data.loc[:,
                                                bldg.name + " TAir[6]"].values * 0.02 * bldg.net_leased_area)
                                             / bldg.net_leased_area) - 273.15
                data.loc[:, "TRad"] = ((temp_data.loc[:,
                                        bldg.name + " TRad[1]"].values * 0.5 * bldg.net_leased_area
                                        + temp_data.loc[:,
                                          bldg.name + " TRad[2]"].values * 0.25 * bldg.net_leased_area
                                        + temp_data.loc[:,
                                          bldg.name + " TRad[3]"].values * 0.15 * bldg.net_leased_area
                                        + temp_data.loc[:,
                                          bldg.name + " TRad[4]"].values * 0.04 * bldg.net_leased_area
                                        + temp_data.loc[:,
                                          bldg.name + " TRad[5]"].values * 0.04 * bldg.net_leased_area
                                        + temp_data.loc[:,
                                          bldg.name + " TRad[6]"].values * 0.02 * bldg.net_leased_area)
                                       / bldg.net_leased_area) - 273.15
            else:
                data.loc[:, "Temperatur"] = temp_data.loc[:, bldg.name + " TOpe"].values - 273.15
                data.loc[:, "TAir"] = temp_data.loc[:, bldg.name + " TAir"].values - 273.15
                data.loc[:, "TRad"] = temp_data.loc[:, bldg.name + " TRad"].values - 273.15

            if "tabsplusair" in bldg.name:
                data.loc[:, "tabs_heat_demand"] = heat_data.loc[:, bldg.name + " tabsHeatingPower"].values / 1000
                data.loc[:, "tabs_cool_demand"] = -cool_data.loc[:, bldg.name + " tabsCoolingPower"].values / 1000
                data.loc[:, "convective_heat_demand"] = heat_data.loc[:, bldg.name + " pITempHeatRem.y"].values / 1000
                data.loc[:, "convective_cool_demand"] = -cool_data.loc[:, bldg.name + " pITempCoolRem.y"].values / 1000

            # plot the indoor temperature and heating/cooling demand for one year in two subplots
            print("plotting building {}".format(bldg.name))
            fig, (ax1, ax2) = plt.subplots(2)
            ax1.plot(data.loc[:, "Temperatur"], linewidth=0.5, color="black")
            # ax1.set_title("Operative Temperatur")
            ax1.set_ylabel('Temperatur [°C]')
            ax1.set_ylim([20, 31])
            ax1.yaxis.set_major_locator(mticker.MultipleLocator(5))
            ax1.yaxis.set_minor_locator(mticker.MultipleLocator(2.5))
            ax1.margins(0)
            ax1.axvspan(datetime.datetime(2021, 4, 1, 0, 0, 0), datetime.datetime(2021, 4, 30, 23, 55), facecolor='#EDEDED')
            ax1.xaxis.set_major_locator(allmonths)
            ax1.xaxis.set_minor_locator(months_locator)
            ax1.xaxis.set_major_formatter(mticker.NullFormatter())
            ax1.xaxis.set_minor_formatter(months_formatter)
            ax1.tick_params(axis="x", which="minor", length=0)

            ax2.plot(data.loc[:, "Wärmeleistung"], linewidth=0.5, label="Heizleistung", color="r")
            ax2.plot(-data.loc[:, "Kälteleistung"], linewidth=0.5, label="Kühlleistung", color="b")
            # ax2.set_title("Heiz- und Kühllast")
            ax2.set_ylabel('Leistung [kW]')
            ax2.set_ylim([0.0, 45.0])
            # ax2.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            # ax2.yaxis.set_major_locator(mticker.AutoLocator())
            # ax2.yaxis.set_minor_locator(mticker.AutoMinorLocator())
            ax2.yaxis.set_major_locator(mticker.MultipleLocator(20))
            ax2.yaxis.set_minor_locator(mticker.MultipleLocator(10))
            ax2.margins(0)
            ax2.axvspan(datetime.datetime(2021, 4, 1, 0, 0, 0), datetime.datetime(2021, 4, 30, 23, 55),
                        facecolor='#EDEDED')
            ax2.xaxis.set_major_locator(allmonths)
            ax2.xaxis.set_minor_locator(months_locator)
            ax2.xaxis.set_major_formatter(mticker.NullFormatter())
            ax2.xaxis.set_minor_formatter(months_formatter)
            ax2.tick_params(axis="x", which="minor", length=0)

            fig.legend(loc=9, bbox_to_anchor=(0.5, 1.0,), ncol=2)
            # bbox_to_anchor=(0.5, 1.06,), ncol=1
            # plt.tight_layout()
            plt.savefig(os.path.join(output_path, bldg.name + "_plot.pdf"), dpi=200, bbox_inches="tight")

            # clear plot lines, keep axes
            for artist in ax1.lines + ax1.collections + ax2.lines + ax2.collections:
                artist.remove()

            # plot daily mean resampled data
            ax1.plot(data.loc[:, "Temperatur"].resample('D').mean(), linewidth=0.5, color="black")
            ax2.plot(data.loc[:, "Wärmeleistung"].resample('D').mean(), linewidth=0.5, label="Heizleistung", color="r")
            ax2.plot(-data.loc[:, "Kälteleistung"].resample('D').mean(), linewidth=0.5, label="Kühlleistung", color="b")
            plt.savefig(os.path.join(output_path, bldg.name + "_daily_mean_plot.pdf"), dpi=200, bbox_inches="tight")

            plt.close("all")

            # plot only April
            fig, (ax3, ax4) = plt.subplots(2)
            # ax3.plot(data.loc[:, "Temperatur"], linewidth=0.5, color="black")
            ax3.plot(data.loc[:, "TAir"], linewidth=0.5, color="#1058B0", label="Lufttemperatur")
            ax3.plot(data.loc[:, "TRad"], linewidth=0.5, color="#008746", label="Strahlungstemperatur")
            # ax3.set_title("Operative Temperatur")
            ax3.set_ylabel('Temperatur [°C]')
            ax3.set_ylim([20, 25])
            ax3.set_xlim(datetime.datetime(2021, 3, 31, 23, 55), datetime.datetime(2021, 5, 1, 0, 0, 0))
            ax3.margins(0)
            ax3.axvspan(datetime.datetime(2021, 4, 1, 0, 0, 0), datetime.datetime(2021, 4, 30, 23, 55),
                        facecolor='#EDEDED')
            ax3.yaxis.set_major_locator(mticker.MultipleLocator(5))
            ax3.yaxis.set_minor_locator(mticker.MultipleLocator(1))
            ax3.xaxis.set_minor_locator(minor_days)
            ax3.xaxis.set_major_locator(major_days)
            ax3.xaxis.set_major_formatter(format)

            ax4.plot(data.loc[:, "Wärmeleistung"], linewidth=0.5, color="r")
            # ax4.plot(-data.loc[:, "Kälteleistung"], linewidth=0.5, label="Kühlleistung", label="Heizleistung", color="b")
            # ax4.set_title("Heiz- und Kühllast")
            ax4.set_ylabel('Leistung [kW]')
            ax4.set_ylim([0.0, 45.0])
            ax4.set_xlim(datetime.datetime(2021, 3, 31, 23, 55), datetime.datetime(2021, 5, 1, 0, 0, 0))
            ax4.yaxis.set_major_locator(mticker.MultipleLocator(20))
            ax4.yaxis.set_minor_locator(mticker.MultipleLocator(10))
            ax4.xaxis.set_minor_locator(minor_days)
            ax4.xaxis.set_major_locator(major_days)
            ax4.xaxis.set_major_formatter(format)
            ax4.margins(0)
            ax4.axvspan(datetime.datetime(2021, 4, 1, 0, 0, 0), datetime.datetime(2021, 4, 30, 23, 55),
                        facecolor='#EDEDED')

            fig.legend(loc=9, bbox_to_anchor=(0.5, 1.0,), ncol=2)
            plt.savefig(os.path.join(output_path, bldg.name + "_zoom_plot.pdf"), dpi=200, bbox_inches="tight")
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

def plot_TABS_curves(output_path):

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    T = np.array([-10, 0, 15, 25])
    power = np.array([100, 100, 30, 30])
    T_K = np.array([27, 22, 18, 13])
    power_K = np.array([100, 100, 30, 30])

    fig, ax = plt.subplots()
    ax.plot(T, power, linewidth=1, color="r")
    ax.set_title("Heizen")
    ax.set_ylabel('relative Leistung [%]')
    ax.set_xlabel('gleitender 24 h Mittelwert der Außentemperatur [°C]')
    ax.set_ylim([0, 105])
    ax.set_xlim([-5, 20])
    ax.yaxis.set_major_locator(mticker.MultipleLocator(20))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(10))
    ax.margins(0.5)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(5))

    plt.savefig(os.path.join(output_path, "TABS_Heating_Curve.pdf"), dpi=200, bbox_inches="tight")
    plt.cla()

    ax.plot(T_K, power_K, linewidth=1, color="b")
    ax.set_title("Kühlen")
    ax.set_ylabel('relative Leistung [%]')
    ax.set_xlabel('gleitender 24 h Mittelwert der Außentemperatur [°C]')
    ax.set_ylim([0, 105])
    ax.set_xlim([13, 27])
    ax.yaxis.set_major_locator(mticker.MultipleLocator(20))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(10))
    ax.margins(0.5)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(5))

    plt.savefig(os.path.join(output_path, "TABS_Cooling_Curve.pdf"), dpi=200, bbox_inches="tight")
    plt.close("all")

def plot_diagrams_Kap_1(output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    time = np.array([0, 6, 6.05, 7, 12, 23, 23.05, 24])
    Trad = np.array([20, 19, 19, 19.5, 20, 20.3, 20.3, 19.8])
    Tair = np.array([18.5, 17.5, 22, 22.5, 22, 21.8, 18.8, 18.5])
    power = np.array([0, 0, 100, 100, 66, 60, 0, 0])

    time_new = np.linspace(0, 24, num=24, endpoint=True)
    spl1 = make_interp_spline(time, power, k=3)  # type: BSpline
    power_smooth = spl1(time_new)

    spl2 = make_interp_spline(time, Trad, k=3)
    Trad_smooth = spl2(time_new)

    spl3 = make_interp_spline(time, Tair, k=3)
    Tair_smooth = spl3(time_new)

    df = pd.DataFrame(data = {'time': time, 'power': power})

    plot = sns.lmplot(x='time', y='power', data=df, ci=None, order=4, truncate=False)
    plot2 = sns.lmplot(x='time', y='power', data=df, ci=None, lowess=True, truncate=False)
    plot.savefig(os.path.join(output_path, "RLT2.pdf"), dpi=200)


    fig, (ax1, ax2) = plt.subplots(1, 2)
    # ax1.plot(time_new, Trad_smooth, linewidth=0.5, color="r")
    # ax1.plot(time_new, Tair_smooth, linewidth=0.5, color="b")
    ax1.plot(time, Trad, linewidth=0.9, color="r", label='Strahlungstemperatur')
    ax1.plot(time, Tair, linewidth=0.9, color="b", label='Lufttemperatur')
    ax1.set_ylabel('Temperatur [°C]')
    ax1.set_xlabel('Uhrzeit [h]')
    ax1.set_ylim([17, 23])
    ax1.set_xlim([0, 24])
    ax1.yaxis.set_major_locator(mticker.MultipleLocator(1))
    # ax1.yaxis.set_minor_locator(mticker.MultipleLocator(10))
    ax1.margins(0.5)
    ax1.xaxis.set_major_locator(mticker.MultipleLocator(6))
    ax1.legend(loc='lower right', ncol=1, borderaxespad=0., fontsize='x-small', frameon=False)

    # ax2.plot(time_new, power_smooth, linewidth=0.5, color="r")
    ax2.plot(time, power, linewidth=0.9, color="black")
    ax2.set_ylabel('Leistung [%]')
    ax2.set_xlabel('Uhrzeit [h]')
    ax2.set_ylim([0, 105])
    ax2.set_xlim([0, 24])
    ax2.yaxis.set_major_locator(mticker.MultipleLocator(10))
    # ax2.yaxis.set_minor_locator(mticker.MultipleLocator(10))
    ax2.margins(0.5)
    ax2.xaxis.set_major_locator(mticker.MultipleLocator(6))
    plt.tight_layout()

    # fig.legend(loc=9, bbox_to_anchor=(0.5, 1.05,), ncol=2)
    plt.savefig(os.path.join(output_path, "RLT.pdf"), dpi=200, )
    # bbox_inches="tight"


if __name__ == '__main__':
    # set path to your workspace here
    workspace = os.path.join("D:\\", "tbl-cwe")
    print("Your workspace is set to: " + workspace)

    output_path = os.path.join(workspace, "Plots_Kap_3")
    print("Your plots are stored in: " + output_path)

    output_path2 = os.path.join(workspace, "Plots_Kap_1")
    print("Your plots are stored in: " + output_path2)

    # plot_TABS_curves(output_path)

    plot_diagrams_Kap_1(output_path2)