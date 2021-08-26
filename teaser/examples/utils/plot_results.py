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

    T = np.array([-10, 0, 15])
    power = np.array([100, 100, 30])
    T_K = np.array([27, 25, 18])
    power_K = np.array([100, 100, 30])

    fig, ax = plt.subplots()
    ax.plot(T, power, linewidth=1, color="r")
    ax.vlines(x=15, ymin=0, ymax=110, colors='r', linestyles='dashed', linewidth=1)
    ax.set_title("Heizen")
    ax.set_ylabel('relative Leistung [%]')
    ax.set_xlabel('gleitender 24 h Mittelwert der Außentemperatur [°C]')
    ax.set_ylim([0, 105])
    ax.set_xlim([-5, 20])
    ax.yaxis.set_major_locator(mticker.MultipleLocator(20))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(10))
    ax.margins(0.5)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(5))
    ax.xaxis.set_minor_locator(mticker.MultipleLocator(1))

    plt.savefig(os.path.join(output_path, "TABS_Heating_Curve.pdf"), dpi=200, bbox_inches="tight")
    plt.cla()

    ax.plot(T_K, power_K, linewidth=1, color="b")
    ax.vlines(x=18, ymin=0, ymax=110, colors='b', linestyles='dashed', linewidth=1)
    ax.set_title("Kühlen")
    ax.set_ylabel('relative Leistung [%]')
    ax.set_xlabel('gleitender 24 h Mittelwert der Außentemperatur [°C]')
    ax.set_ylim([0, 105])
    ax.set_xlim([13, 27])
    ax.yaxis.set_major_locator(mticker.MultipleLocator(20))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(10))
    ax.margins(0.5)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(5))
    ax.xaxis.set_minor_locator(mticker.MultipleLocator(1))

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

    # clear plot lines, keep axes
    for artist in ax1.lines + ax1.collections + ax2.lines + ax2.collections:
        artist.remove()

    r_time = np.array([0, 6.8, 6.85, 7.5, 12, 18, 23, 24])
    r_Trad = np.array([20.25, 19.25, 20.25, 20.35, 20.5, 20.75, 20.85, 20.3])
    r_Tair = np.array([19.75, 18.6, 22, 21.5, 21.45, 21.4, 21.35, 19.75])
    r_power = np.array([10, 0, 100, 70, 55, 46, 40, 10])

    ax1.plot(r_time, r_Trad, linewidth=0.9, color="r", label='Strahlungstemperatur')
    ax1.plot(r_time, r_Tair, linewidth=0.9, color="b", label='Lufttemperatur')
    ax2.plot(r_time, r_power, linewidth=0.9, color="black")

    plt.savefig(os.path.join(output_path, "Radiator.pdf"), dpi=200, )

    # clear plot lines, keep axes
    for artist in ax1.lines + ax1.collections + ax2.lines + ax2.collections:
        artist.remove()

    fhk_time = np.array([0, 6.2, 6.25, 6.3, 8, 12, 18, 23, 23.05, 24])
    fhk_Trad = np.array([20.5, 19.5, 19.5, 21.3, 21.4, 21.5, 21.55, 21.6, 20.6, 20.5])
    fhk_Tair = np.array([19.7, 18.7, 18.7, 20.7, 20.6, 20.5, 20.45, 20.4, 19.8, 19.7])
    fhk_power = np.array([0, 0, 100, 97, 69, 51, 45, 43, 0, 0])

    ax1.plot(fhk_time, fhk_Trad, linewidth=0.9, color="r", label='Strahlungstemperatur')
    ax1.plot(fhk_time, fhk_Tair, linewidth=0.9, color="b", label='Lufttemperatur')
    ax2.plot(fhk_time, fhk_power, linewidth=0.9, color="black")

    plt.savefig(os.path.join(output_path, "RadFHK.pdf"), dpi=200, )

    # clear plot lines, keep axes
    for artist in ax1.lines + ax1.collections + ax2.lines + ax2.collections:
        artist.remove()

    fbh_time = np.array([0, 4, 4.05, 6, 7.5, 8.5, 12, 23, 23.05, 24])
    fbh_Trad = np.array([21.2, 20.6, 20.6, 21.2, 21.3, 21.3, 21.3, 21.3, 21.3, 21.2])
    fbh_Tair = np.array([20.55, 19.9, 19.9, 20.67, 20.72, 20.71, 20.7, 20.7, 20.7, 20.55])
    fbh_power = np.array([28, 20, 20, 33, 42, 40, 38.5, 37, 37, 33])
    fbh_power_to_floor = np.array([0, 0, 100, 70, 46, 34, 37, 37, 0, 0])

    ax1.plot(fbh_time, fbh_Trad, linewidth=0.9, color="r", label='Strahlungstemperatur')
    ax1.plot(fbh_time, fbh_Tair, linewidth=0.9, color="b", label='Lufttemperatur')
    ax2.plot(fbh_time, fbh_power, linewidth=0.9, color="black", label='Wärmestrom \n an den Raum')
    ax2.plot(fbh_time, fbh_power_to_floor, linewidth=0.9, color="r", label='Wärmestrom \n in den Boden')
    ax2.legend(loc='upper right', ncol=1, borderaxespad=0., fontsize='x-small', frameon=False, bbox_to_anchor=(1.0, 0.96))
    # ax1.set_ylim([19.5, 21.5])
    # ax1.yaxis.set_major_locator(mticker.MultipleLocator(0.5))

    plt.savefig(os.path.join(output_path, "FBH.pdf"), dpi=200, )

    # clear plot lines, keep axes
    for artist in ax1.lines + ax1.collections + ax2.lines + ax2.collections:
        artist.remove()

    bkt_time = np.array([0, 1.8, 1.85, 6, 6.05, 8, 21.5, 21.55, 24])
    bkt_Trad = np.array([21.25, 21.2, 21.2, 21.3, 21.3, 21.3, 21.3, 21.3, 21.25])
    bkt_Tair = np.array([20.6, 20.53, 20.53, 20.65, 20.65, 20.7, 20.7, 20.7, 20.65])
    bkt_power = np.array([47, 46, 46, 48.5, 48.5, 50, 49, 49, 47])
    bkt_power_to_floor = np.array([0, 0, 100, 85, 55, 55, 55, 0, 0])

    ax1.plot(bkt_time, bkt_Trad, linewidth=0.9, color="r", label='Strahlungstemperatur')
    ax1.plot(bkt_time, bkt_Tair, linewidth=0.9, color="b", label='Lufttemperatur')
    ax2.plot(bkt_time, bkt_power, linewidth=0.9, color="black", label='Wärmestrom \n an den Raum')
    ax2.plot(bkt_time, bkt_power_to_floor, linewidth=0.9, color="r", label='Wärmestrom \n in den Boden')
    # ax2.legend(loc='upper right', ncol=1, borderaxespad=0., fontsize='x-small', frameon=False)
    # ax1.set_ylim([20.5, 21.5])

    plt.savefig(os.path.join(output_path, "BKT.pdf"), dpi=200, )

def plot_comfort_diagrams_Kap_1(output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    sia_outtemp_l = np.array([10, 25, 30, 32])
    sia_roomtemp_l = np.array([21, 21, 22, 22])
    sia_outtemp_u = np.array([10, 16, 23, 32])
    sia_roomtemp_u = np.array([24.5, 24.5, 26.5, 26.5])
    din_outtemp_u = np.array([10, 30])
    din_roomtemp_1_u = np.array([24, 31])
    din_roomtemp_2_u = np.array([25, 32])
    din_roomtemp_3_u = np.array([26, 33])
    din_outtemp_l = np.array([15, 30])
    din_roomtemp_1_l = np.array([22, 27])
    din_roomtemp_2_l = np.array([21, 26])
    din_roomtemp_3_l = np.array([20, 25])

    din_neu_roomtemp_1_l = np.array([19, 26])
    din_neu_roomtemp_2_l = np.array([18, 25])
    din_neu_roomtemp_3_l = np.array([17, 24])
    din_neu_komforttemp = np.array([22, 29])

    fig, ax = plt.subplots()
    ax.plot(sia_outtemp_l, sia_roomtemp_l, linewidth=1, color="black")
    ax.plot(sia_outtemp_u, sia_roomtemp_u, linewidth=1, color="black")
    plt.fill(
        np.append(sia_outtemp_l, sia_outtemp_u[::-1]),
        np.append(sia_roomtemp_l, sia_roomtemp_u[::-1]), color="#DDDDDD"
    )
    # ax.set_title("Heizen")
    ax.set_ylabel('Operative Temperatur [°C]')
    ax.set_xlabel('Tagesmaximum der Außentemperatur [°C]')
    ax.set_ylim([20, 30])
    ax.set_xlim([10, 35])
    ax.yaxis.set_major_locator(mticker.MultipleLocator(2))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(1))
    ax.margins(0.5)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(2))
    # ax.xaxis.set_minor_locator(mticker.MultipleLocator(1))

    plt.savefig(os.path.join(output_path, "SIA382_Komfort.pdf"), dpi=200, bbox_inches="tight")
    plt.close("all")

    fig, ax = plt.subplots()
    ax.plot(din_outtemp_u, din_roomtemp_1_u, linewidth=1, color="black", label="I")
    ax.plot(din_outtemp_u, din_roomtemp_2_u, linewidth=1, color="black", linestyle="dashed", label="II")
    ax.plot(din_outtemp_u, din_roomtemp_3_u, linewidth=1, color="black", linestyle="dotted", label="III")
    ax.plot(din_outtemp_l, din_roomtemp_1_l, linewidth=1, color="black")
    ax.plot(din_outtemp_l, din_roomtemp_2_l, linewidth=1, color="black", linestyle="dashed")
    ax.plot(din_outtemp_l, din_roomtemp_3_l, linewidth=1, color="black", linestyle="dotted")
    # ax.set_title("Heizen")
    ax.set_ylabel('Operative Temperatur [°C]')
    ax.set_xlabel('Gleitender Mittelwert der Außentemperatur [°C]')
    ax.set_ylim([19, 33])
    ax.set_xlim([8, 30])
    ax.yaxis.set_major_locator(mticker.MultipleLocator(2))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(1))
    ax.margins(0.5)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(2))
    # ax.xaxis.set_minor_locator(mticker.MultipleLocator(1))
    ax.legend(loc="best", ncol=1)
    # bbox_to_anchor=(0.5, 1.0,)
    plt.savefig(os.path.join(output_path, "DINEN15251_Komfort.pdf"), dpi=200, bbox_inches="tight")
    plt.close("all")

    fig, ax = plt.subplots()
    ax.plot(din_outtemp_u, din_neu_roomtemp_1_l, linewidth=1, color="black", label="I")
    ax.plot(din_outtemp_u, din_neu_roomtemp_2_l, linewidth=1, color="black", linestyle="dashed", label="II")
    ax.plot(din_outtemp_u, din_neu_roomtemp_3_l, linewidth=1, color="black", linestyle="dotted", label="III")
    ax.plot(din_outtemp_u, din_roomtemp_1_u, linewidth=1, color="black")
    ax.plot(din_outtemp_u, din_roomtemp_2_u, linewidth=1, color="black", linestyle="dashed")
    ax.plot(din_outtemp_u, din_roomtemp_3_u, linewidth=1, color="black", linestyle="dotted")
    # ax.plot(din_outtemp_u, din_neu_komforttemp, linewidth=1, color="black", linestyle="dashdot", label="Komforttemperatur")
    # ax.set_title("Heizen")
    ax.set_ylabel('Operative Temperatur [°C]')
    ax.set_xlabel('Gleitender Mittelwert der Außentemperatur [°C]')
    ax.set_ylim([16, 33])
    ax.set_xlim([8, 30])
    ax.yaxis.set_major_locator(mticker.MultipleLocator(2))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(1))
    ax.margins(0.5)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(2))
    # ax.xaxis.set_minor_locator(mticker.MultipleLocator(1))
    ax.legend(loc="best", ncol=1)
    # bbox_to_anchor=(0.5, 1.0,) , fontsize="small"
    plt.savefig(os.path.join(output_path, "DINEN16798_Komfort.pdf"), dpi=200, bbox_inches="tight")

def plot_alpha_k_Kap_1(output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    delta_T = np.linspace(0, 10, 400)
    alpha_vert = 1.6 * delta_T**0.3
    alpha_hor_up = 2 * delta_T**0.31
    alpha_hor_down = 0.54 * delta_T**0.31

    fig, ax = plt.subplots()
    ax.plot(delta_T, alpha_vert, linewidth=0.8, color="black", label="vertikale Fläche [Glück]")
    ax.plot(delta_T, alpha_hor_up, linewidth=0.8, color="blue", label="horizontale Fläche, Wärmestrom nach oben [Glück]")
    ax.plot(delta_T, alpha_hor_down, linewidth=0.8, color="red", label="horizontale Fläche, Wärmestrom nach unten [Glück]")
    ax.hlines(y=6, xmin=0, xmax=10, colors='black', linestyles='dashed', linewidth=0.8, label="vertikale Fläche [VDI]")
    ax.hlines(y=7, xmin=0, xmax=10, colors='blue', linestyles='dashed', linewidth=0.8, label="Fußboden, Wärmestrom nach oben [VDI]")
    ax.hlines(y=5, xmin=0, xmax=10, colors='blue', linestyles='dotted', linewidth=0.8, label="Decke, Wärmestrom nach oben [VDI]")
    ax.hlines(y=1, xmin=0, xmax=10, colors='red', linestyles='dashed', linewidth=0.8, label="horizontale Fläche, Wärmestrom nach unten [VDI]")
    # ax.hlines(y=1, xmin=0, xmax=10, colors='red', linestyles='dotted', linewidth=0.8, label="Decke, Wärmestrom nach unten")

    ax.set_ylabel(r'$ \alpha_K \ [W/(m^2K)]$')
    ax.set_xlabel('Temperaturdifferenz [K]')
    ax.set_ylim([0, 8])
    ax.set_xlim([0, 10])
    ax.yaxis.set_major_locator(mticker.MultipleLocator(1))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(0.5))
    ax.margins(0.5)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(1))

    fig.legend(loc="upper center", ncol=1, fontsize="small", bbox_to_anchor=(0.5, 1.3,))
    #
    plt.savefig(os.path.join(output_path, "Alpha_K_Option_1.pdf"), dpi=200, bbox_inches="tight")
    plt.close("all")

    fig, ax = plt.subplots()
    ax.plot(delta_T, alpha_vert, linewidth=0.8, color="black", label="Glück")
    ax.hlines(y=6, xmin=0, xmax=10, colors='blue', linestyles='dashed', linewidth=0.8, label="VDI 2078")

    # ax.hlines(y=1, xmin=0, xmax=10, colors='red', linestyles='dotted', linewidth=0.8, label="Decke, Wärmestrom nach unten")

    ax.set_ylabel(r'$ \alpha_K \ [W/(m^2K)]$')
    ax.set_xlabel('Temperaturdifferenz [K]')
    ax.set_ylim([0, 8])
    ax.set_xlim([0, 10])
    ax.yaxis.set_major_locator(mticker.MultipleLocator(1))
    ax.yaxis.set_minor_locator(mticker.MultipleLocator(0.5))
    ax.margins(0.5)
    ax.xaxis.set_major_locator(mticker.MultipleLocator(1))

    ax.legend(loc="best")
    plt.savefig(os.path.join(output_path, "Alpha_K_vert.pdf"), dpi=200, bbox_inches="tight")

    # clear plot lines, keep axes
    for artist in ax.lines + ax.collections:
        artist.remove()

    ax.plot(delta_T, alpha_hor_up, linewidth=0.8, color="black",
           label="Glück")
    ax.hlines(y=7, xmin=0, xmax=10, colors='blue', linestyles='dashed', linewidth=0.8,
              label="VDI 2078, Fußboden")
    ax.hlines(y=5, xmin=0, xmax=10, colors='red', linestyles='dashed', linewidth=0.8,
              label="VDI 2078, Decke")
    ax.legend(loc="lower right")

    plt.savefig(os.path.join(output_path, "Alpha_K_hor_up.pdf"), dpi=200, bbox_inches="tight")

    # clear plot lines, keep axes
    for artist in ax.lines + ax.collections:
        artist.remove()

    ax.plot(delta_T, alpha_hor_down, linewidth=0.8, color="black",
            label="Glück")

    ax.hlines(y=1, xmin=0, xmax=10, colors='blue', linestyles='dashed', linewidth=0.8,
              label="VDI 2078")
    ax.legend(loc="best")

    plt.savefig(os.path.join(output_path, "Alpha_K_hor_down.pdf"), dpi=200, bbox_inches="tight")

def plot_results_Kap_4(buildings, csv_path, output_path):
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
            ax1.plot(data.loc[:, "Temperatur"], linewidth=0.5, color="black", )
            # label="Operative Temperatur"
            # ax1.plot(data.loc[:, "TRad"], linewidth=0.5, color="red", label="Strahlungstemperatur")
            # ax1.plot(data.loc[:, "TAir"], linewidth=0.5, color="blue", label="Lufttemperatur")
            # ax1.set_title("Operative Temperatur")
            ax1.set_ylabel('Temperatur [°C]')
            ax1.set_ylim([20, 31])
            ax1.yaxis.set_major_locator(mticker.MultipleLocator(5))
            ax1.yaxis.set_minor_locator(mticker.MultipleLocator(2.5))
            ax1.margins(0)
            # ax1.axvspan(datetime.datetime(2021, 4, 1, 0, 0, 0), datetime.datetime(2021, 4, 30, 23, 55), facecolor='#EDEDED')
            ax1.xaxis.set_major_locator(allmonths)
            ax1.xaxis.set_minor_locator(months_locator)
            ax1.xaxis.set_major_formatter(mticker.NullFormatter())
            # ax1.xaxis.set_minor_formatter(months_formatter)
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
            # ax2.axvspan(datetime.datetime(2021, 4, 1, 0, 0, 0), datetime.datetime(2021, 4, 30, 23, 55),facecolor='#EDEDED')
            ax2.xaxis.set_major_locator(allmonths)
            ax2.xaxis.set_minor_locator(months_locator)
            ax2.xaxis.set_major_formatter(mticker.NullFormatter())
            ax2.xaxis.set_minor_formatter(months_formatter)
            ax2.tick_params(axis="x", which="minor", length=0)
            ax2.legend(loc="best", ncol=2, fontsize="small")

            # fig.legend(loc=9, bbox_to_anchor=(0.5, 1.0,), ncol=2)
            # bbox_to_anchor=(0.5, 1.06,), ncol=1
            # plt.tight_layout()
            plt.savefig(os.path.join(output_path, bldg.name + "_plot.pdf"), dpi=200, bbox_inches="tight")

            ax1.plot(data.loc[:, "TRad"], linewidth=0.5, color="red", label="Strahlungstemperatur")
            ax1.plot(data.loc[:, "TAir"], linewidth=0.5, color="blue", label="Lufttemperatur")
            ax1.set_xlim([18, 32])
            ax1.legend(loc="best", ncol=2, fontsize="small")

            plt.savefig(os.path.join(output_path, bldg.name + "_3T_plot.pdf"), dpi=200, bbox_inches="tight")

            # clear plot lines, keep axes
            for artist in ax1.lines + ax1.collections + ax2.lines + ax2.collections:
                artist.remove()

            # plot daily mean resampled data
            ax1.plot(data.loc[:, "Temperatur"].resample('D').mean(), linewidth=0.5, color="black")
            ax2.plot(data.loc[:, "Wärmeleistung"].resample('D').mean(), linewidth=0.5, label="Heizleistung", color="r")
            ax2.plot(-data.loc[:, "Kälteleistung"].resample('D').mean(), linewidth=0.5, label="Kühlleistung", color="b")
            plt.savefig(os.path.join(output_path, bldg.name + "_daily_mean_plot.pdf"), dpi=200, bbox_inches="tight")

            ax1.plot(data.loc[:, "TRad"].resample('D').mean(), linewidth=0.5, color="red", label="Strahlungstemperatur")
            ax1.plot(data.loc[:, "TAir"].resample('D').mean(), linewidth=0.5, color="blue", label="Lufttemperatur")
            plt.savefig(os.path.join(output_path, bldg.name + "_daily_mean_3T_plot.pdf"), dpi=200, bbox_inches="tight")

            plt.close("all")

            # plot only February
            fig, (ax3, ax4) = plt.subplots(2)
            ax3.plot(data.loc[:, "Temperatur"], linewidth=0.5, color="black")
            ax3.plot(data.loc[:, "TAir"], linewidth=0.5, color="#1058B0", label="Lufttemperatur")
            ax3.plot(data.loc[:, "TRad"], linewidth=0.5, color="#008746", label="Strahlungstemperatur")
            # ax3.set_title("Operative Temperatur")
            ax3.set_ylabel('Temperatur [°C]')
            ax3.set_ylim([20, 25])
            ax3.set_xlim(datetime.datetime(2021, 1, 31, 23, 55), datetime.datetime(2021, 3, 1, 0, 0, 0))
            ax3.margins(0)
            # ax3.axvspan(datetime.datetime(2021, 4, 1, 0, 0, 0), datetime.datetime(2021, 4, 30, 23, 55),facecolor='#EDEDED')
            ax3.yaxis.set_major_locator(mticker.MultipleLocator(5))
            ax3.yaxis.set_minor_locator(mticker.MultipleLocator(1))
            ax3.xaxis.set_minor_locator(minor_days)
            ax3.xaxis.set_major_locator(major_days)
            ax3.xaxis.set_major_formatter(format)

            ax4.plot(data.loc[:, "Wärmeleistung"], linewidth=0.5, color="r", label="Heizleistung")
            # ax4.plot(-data.loc[:, "Kälteleistung"], linewidth=0.5, label="Kühlleistung", color="b")
            # ax4.set_title("Heiz- und Kühllast")
            ax4.set_ylabel('Leistung [kW]')
            ax4.set_ylim([0.0, 45.0])
            ax4.set_xlim(datetime.datetime(2021, 1, 31, 23, 55), datetime.datetime(2021, 3, 1, 0, 0, 0))
            ax4.yaxis.set_major_locator(mticker.MultipleLocator(20))
            ax4.yaxis.set_minor_locator(mticker.MultipleLocator(10))
            ax4.xaxis.set_minor_locator(minor_days)
            ax4.xaxis.set_major_locator(major_days)
            ax4.xaxis.set_major_formatter(format)
            ax4.margins(0)
            # ax4.axvspan(datetime.datetime(2021, 4, 1, 0, 0, 0), datetime.datetime(2021, 4, 30, 23, 55),facecolor='#EDEDED')

            fig.legend(loc=9, bbox_to_anchor=(0.5, 1.0,), ncol=2)
            plt.savefig(os.path.join(output_path, bldg.name + "_zoom_plot_feb.pdf"), dpi=200, bbox_inches="tight")

            # plot only July
            ax4.plot(-data.loc[:, "Kälteleistung"], linewidth=0.5, label="Kühlleistung", color="b")
            ax3.set_xlim(datetime.datetime(2021, 6, 30, 23, 55), datetime.datetime(2021, 8, 1, 0, 0, 0))
            ax4.set_xlim(datetime.datetime(2021, 6, 30, 23, 55), datetime.datetime(2021, 8, 1, 0, 0, 0))
            plt.savefig(os.path.join(output_path, bldg.name + "_zoom_plot_jul.pdf"), dpi=200, bbox_inches="tight")
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

if __name__ == '__main__':
    # set path to your workspace here
    workspace = os.path.join("D:\\", "tbl-cwe", "Final_Simulations")
    print("Your workspace is set to: " + workspace)

    output_path = os.path.join(workspace, "Plots_Kap_3")
    print("Your plots are stored in: " + output_path)

    output_path2 = os.path.join(workspace, "Plots_Kap_1")
    print("Your plots are stored in: " + output_path2)

    output_path4 = os.path.join(workspace, "Plots_Kap_4")
    print("Your plots are stored in: " + output_path4)

    # plot_TABS_curves(output_path)

    # plot_diagrams_Kap_1(output_path2)

    # plot_comfort_diagrams_Kap_1(output_path2)

    # plot_alpha_k_Kap_1(output_path2)

