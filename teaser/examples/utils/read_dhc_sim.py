import datetime

import dymola
import pandas as pd
import os
import numpy as np
import matplotlib
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
          'axes.grid.axis': 'y',
          'axes.grid': True,
          'grid.color': '#DDDDDD',
          'figure.figsize': (sitewidth, sitewidth / 16 * 9),
          'figure.subplot.hspace': 0.2,
          'axes.ymargin': 0.1,
          }
params2 ={'legend.fontsize': fontsize,
          'xtick.labelsize': fontsize,
          'ytick.labelsize': fontsize,
          'axes.labelsize': fontsize,
          'axes.titlesize': fontsize,
          'axes.grid.axis': 'y',
          'axes.grid': True,
          'grid.color': '#DDDDDD',
          'figure.figsize': (sitewidth, sitewidth / 16 * 12),
          'axes.ymargin': 0.1,}
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

# read simulation result file and returns data frame for list of signals
def read_results(signals, index, results_path, file, csv_path):
    dymola = DymolaInterface()

    dym_res = dymola.readTrajectory(
        fileName=os.path.join(results_path),
        signals=signals,
        rows=dymola.readTrajectorySize(fileName=os.path.join(results_path)))
    results = pd.DataFrame().from_records(dym_res).T
    results = results.rename(
        columns=dict(zip(results.columns.values, signals)))

    # use this code if simulation length is equal to index
    results.index = index
    results.to_csv(os.path.join(csv_path, file + "_res.csv"))

    # use this code if simulation was done with 'store variables at events' active
    """results.index = results['Time']

    res_all = results
    res_all = res_all.groupby(res_all.index).first()
    res_all = res_all[res_all.index.isin(range(0, 31536000 * 2, 3600))]

    res_all.index = res_all.index.astype(int)
    #res_all = res_all.loc[res_all.index[8760:]]
    res_all.index = pd.to_datetime(res_all.index, unit="s", origin="2021", utc=True)

    res_all.to_csv(os.path.join(csv_path, file + "_res.csv"))"""



    dymola.close()

    return results

def calc_and_process_data(res):
    data = pd.DataFrame(index=pd.date_range(
        datetime.datetime(2021, 1, 1), periods=8761, freq="H", ))

    # demand series district (all buildings added up)

    dhc_dem = pd.DataFrame(
        data=res.filter(like="heaDem").sum(axis=1),
        columns=["dhc_heat_dem"], )
    dhc_dem.loc[:, "dhc_cool_dem"] = res.filter(like="cooDem").sum(axis=1)
    dhc_dem.loc[:, "dhc_ele_dem"] = res.filter(like="heaPum.P").sum(axis=1)
    dhc_dem.loc[:, "dhc_net_to_bldg"] = res.filter(like="heaPum.QEva_flow").sum(axis=1)

    # series for plotting
    data.loc[:, "dhc_heat_series"] = dhc_dem.loc[:, "dhc_heat_dem"].values / 1000
    data.loc[:, "dhc_cool_series"] = dhc_dem.loc[:, "dhc_cool_dem"].values / 1000
    data.loc[:, "dhc_ele_series"] = dhc_dem.loc[:, "dhc_ele_dem"].values / 1000
    data.loc[:, "dhc_net_to_bldg_series"] = dhc_dem.loc[:, "dhc_net_to_bldg"].values / 1000

    # KPIs district total demands
    dhc_total_heat_dem = dhc_dem.loc[:, "dhc_heat_dem"].sum() / 1000000
    dhc_max_heat_dem = dhc_dem.loc[:, "dhc_heat_dem"].max() / 1000
    dhc_total_cool_dem = dhc_dem.loc[:, "dhc_cool_dem"].sum() / 1000000
    dhc_max_cool_dem = dhc_dem.loc[:, "dhc_cool_dem"].max() / 1000
    dhc_total_ele_dem = dhc_dem.loc[:, "dhc_ele_dem"].sum() / 1000000
    dhc_max_ele_dem = dhc_dem.loc[:, "dhc_ele_dem"].max() / 1000
    dhc_total_net_to_bldg = -dhc_dem.loc[:, "dhc_net_to_bldg"].sum() / 1000000
    share_net_heat = dhc_total_net_to_bldg / dhc_total_heat_dem * 100

    # EZ demand

    ez_dem = pd.DataFrame(
        data=res.filter(like="hea.Q_flow").sum(axis=1),
        columns=["ez_hea_dem"],
        index=pd.date_range(
            datetime.datetime(2021, 1, 1), periods=8761, freq="H", ))
    ez_dem.loc[:, "ez_coo_dem"] = res.filter(like="coo.Q_flow").sum(axis=1)

    data.loc[:, "EZ_heat"] = ez_dem.loc[:, "ez_hea_dem"].values / 1000
    data.loc[:, "EZ_cool"] = ez_dem.loc[:, "ez_coo_dem"].values / 1000
    data.loc[:, "EZ_m_flow"] = res.loc[:, "networkModel.supplysupply.port_a.m_flow"].values
    data.loc[:, "EZ_m_flow_nominal"] = res.loc[:, "networkModel.supplysupply.m_flow_nominal"].values

    # KPIs EZ
    ez_total_heat = ez_dem.loc[:, "ez_hea_dem"].sum() / 1000000
    ez_total_cool = ez_dem.loc[:, "ez_coo_dem"].sum() / 1000000

    # demand series MFH1
    data.loc[:, "MFH1_heat"] = res.loc[:, "networkModel.demandMFH1.heaDem"].values / 1000
    data.loc[:, "MFH1_cool"] = res.loc[:, "networkModel.demandMFH1.cooDem"].values / 1000
    data.loc[:, "MFH1_ele"] = res.loc[:, "networkModel.demandMFH1.heaPum.P"].values / 1000
    data.loc[:, "MFH1_COP"] = res.loc[:, "networkModel.demandMFH1.heaPum.COP"].values
    data.loc[:, "MFH1_QEva"] = res.loc[:, "networkModel.demandMFH1.heaPum.QEva_flow"].values / 1000
    data.loc[:, "MFH1_m_flow"] = res.loc[:, "networkModel.demandMFH1.port_a.m_flow"].values
    data.loc[:, "MFH1_m_flow_nominal"] = res.loc[:, "networkModel.demandMFH1.m_flow_nominal"].values

    # demand series EFH1
    data.loc[:, "EFH1_heat"] = res.loc[:, "networkModel.demandSFH1.heaDem"].values / 1000
    data.loc[:, "EFH1_cool"] = res.loc[:, "networkModel.demandSFH1.cooDem"].values / 1000
    data.loc[:, "EFH1_ele"] = res.loc[:, "networkModel.demandSFH1.heaPum.P"].values / 1000
    data.loc[:, "EFH1_COP"] = res.loc[:, "networkModel.demandSFH1.heaPum.COP"].values
    data.loc[:, "EFH1_QEva"] = res.loc[:, "networkModel.demandSFH1.heaPum.QEva_flow"].values / 1000
    data.loc[:, "EFH1_m_flow"] = res.loc[:, "networkModel.demandSFH1.port_a.m_flow"].values
    data.loc[:, "EFH1_m_flow_nominal"] = res.loc[:, "networkModel.demandSFH1.m_flow_nominal"].values

    # demand series Office1
    data.loc[:, "Office1_heat"] = res.loc[:, "networkModel.demandOffice1.heaDem"].values / 1000
    data.loc[:, "Office1_cool"] = res.loc[:, "networkModel.demandOffice1.cooDem"].values / 1000
    data.loc[:, "Office1_ele"] = res.loc[:, "networkModel.demandOffice1.heaPum.P"].values / 1000
    data.loc[:, "Office1_COP"] = res.loc[:, "networkModel.demandOffice1.heaPum.COP"].values
    data.loc[:, "Office1_QEva"] = res.loc[:, "networkModel.demandOffice1.heaPum.QEva_flow"].values / 1000
    data.loc[:, "Office1_m_flow"] = res.loc[:, "networkModel.demandOffice1.port_a.m_flow"].values
    data.loc[:, "Office1_m_flow_nominal"] = res.loc[:, "networkModel.demandOffice1.m_flow_nominal"].values

    # print KPIs
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print('Gesamtwärmebedarf in MWh:', round(dhc_total_heat_dem, 1))
    print('Vom Netz zugeführte Wärme in MWh:', round(dhc_total_net_to_bldg, 1))
    print('Anteil am Wärmebedarf in %:', round(share_net_heat, 1))
    print('Spitzenbedarf Wärme in kW:', round(dhc_max_heat_dem, 1))
    print('Gesamtkältebedarf in MWh:', round(dhc_total_cool_dem, 1))
    print('Spitzenbedarf Kälte in kW:', round(dhc_max_cool_dem, 1))
    print('Strombedarf in MWh:', round(dhc_total_ele_dem, 1))
    print('Spitzenbedarf Strom in kW:', round(dhc_max_ele_dem, 1))
    print('Gesamtwärmebedarf EZ in MWh:', round(ez_total_heat, 1))
    print('Gesamtkältebedarf EZ in MWh:', round(ez_total_cool, 1))
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')

    return data

def plot_dhc_results(data):
    # plot all buildings added up demands
    matplotlib.rcParams.update(params2)

    fig, (ax1, ax2) = plt.subplots(2)

    ax1.plot(data.loc[:, "dhc_heat_series"].resample('D').mean(), linewidth=0.5, color="red", label="Wärmebedarf")
    ax1.plot(data.loc[:, "dhc_cool_series"].resample('D').mean(), linewidth=0.5, color="blue", label="Kältebedarf")
    ax2.plot(data.loc[:, "dhc_ele_series"].resample('D').mean(), linewidth=0.5, color="green", label="Strombedarf")
    ax2.plot(-data.loc[:, "dhc_net_to_bldg_series"].resample('D').mean(), linewidth=0.5, color="black",
             label="zugeführte Wärme")

    # set labels
    ax1.set_ylabel('Leistung [kW]')
    ax2.set_ylabel('Leistung [kW]')

    # set limits
    # ax1.set_ylim([19, 33])
    ax1.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax2.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax1.margins(0)
    ax2.margins(0)
    # ax1.axvspan(datetime.datetime(2021, 2, 7, 23, 55), datetime.datetime(2021, 2, 15, 0, 0, 0), facecolor='#EDEDED')
    # ax1.axvspan(datetime.datetime(2021, 8, 8, 23, 55), datetime.datetime(2021, 8, 16, 0, 0, 0), facecolor='#EDEDED')

    # set xaxis
    ax1.xaxis.set_major_locator(allmonths)
    ax1.xaxis.set_minor_locator(months_locator)
    ax1.xaxis.set_major_formatter(mticker.NullFormatter())
    ax1.xaxis.set_minor_formatter(months_formatter)
    ax1.tick_params(axis="x", which="minor", length=0)

    ax2.xaxis.set_major_locator(allmonths)
    ax2.xaxis.set_minor_locator(months_locator)
    ax2.xaxis.set_major_formatter(mticker.NullFormatter())
    ax2.xaxis.set_minor_formatter(months_formatter)
    ax2.tick_params(axis="x", which="minor", length=0)

    # set yaxis
    # ax1.yaxis.set_major_locator(mticker.MultipleLocator(10))
    # ax1.yaxis.set_minor_locator(mticker.MultipleLocator(5))

    # set legend
    # ax1.legend(loc="upper left", fontsize="x-small", frameon=True, edgecolor="white")
    fig.legend(loc=9, bbox_to_anchor=(0.515, 0.95), ncol=4, fontsize='x-small')
    fig.align_ylabels()

    plt.savefig(os.path.join(plot_path, variante + "_demand_DHC_plot.pdf"), dpi=200, bbox_inches="tight")
    fig.show()
    plt.close("all")

def plot_EFH_results(data):
    # plot single EFH building
    matplotlib.rcParams.update(params2)
    fig, (ax1, ax2, ax3) = plt.subplots(3)

    ax1.plot(data.loc[:, "EFH1_heat"].resample('D').mean(), linewidth=0.5, color="red", label="Wärmebedarf")
    ax1.plot(data.loc[:, "EFH1_cool"].resample('D').mean(), linewidth=0.5, color="blue", label="Kältebedarf")
    ax2.plot(data.loc[:, "EFH1_ele"].resample('D').mean(), linewidth=0.5, color="green", label="Strombedarf")
    ax2.plot(-data.loc[:, "EFH1_QEva"].resample('D').mean(), linewidth=0.5, color="black", label="zugeführte Wärme")
    ax3.plot(data.loc[:, "EFH1_m_flow"].resample('D').mean(), linewidth=0.5, color="purple", label="Massenstrom")
    ax3.plot(data.loc[:, "EFH1_m_flow_nominal"].resample('D').mean(), linewidth=0.5, color="black", label="Massenstrom Auslegung", linestyle="--")

    # set labels
    ax1.set_ylabel('[kW]')
    ax2.set_ylabel('[kW]')
    ax3.set_ylabel('[kg/s]')

    # set limits
    ax1.set_ylim([0, 15])
    ax2.set_ylim([0, 10])
    ax3.set_ylim([-0.2, 0.3])
    ax1.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax2.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax3.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax1.margins(0)
    ax2.margins(0)
    ax3.margins(0)
    # ax1.axvspan(datetime.datetime(2021, 2, 7, 23, 55), datetime.datetime(2021, 2, 15, 0, 0, 0), facecolor='#EDEDED')
    # ax1.axvspan(datetime.datetime(2021, 8, 8, 23, 55), datetime.datetime(2021, 8, 16, 0, 0, 0), facecolor='#EDEDED')

    # set xaxis
    ax1.xaxis.set_major_locator(allmonths)
    ax1.xaxis.set_minor_locator(months_locator)
    ax1.xaxis.set_major_formatter(mticker.NullFormatter())
    ax1.xaxis.set_minor_formatter(months_formatter)
    ax1.tick_params(axis="x", which="minor", length=0)

    ax2.xaxis.set_major_locator(allmonths)
    ax2.xaxis.set_minor_locator(months_locator)
    ax2.xaxis.set_major_formatter(mticker.NullFormatter())
    ax2.xaxis.set_minor_formatter(months_formatter)
    ax2.tick_params(axis="x", which="minor", length=0)

    ax3.xaxis.set_major_locator(allmonths)
    ax3.xaxis.set_minor_locator(months_locator)
    ax3.xaxis.set_major_formatter(mticker.NullFormatter())
    ax3.xaxis.set_minor_formatter(months_formatter)
    ax3.tick_params(axis="x", which="minor", length=0)

    # set yaxis
    # ax1.yaxis.set_major_locator(mticker.MultipleLocator(5))
    # ax1.yaxis.set_minor_locator(mticker.MultipleLocator(2.5))

    # set legend
    # ax1.legend(loc="upper left", fontsize="x-small", frameon=True, edgecolor="white")
    fig.legend(loc=9, bbox_to_anchor=(0.5, 0.98,), ncol=3, fontsize='x-small')
    fig.align_ylabels()

    plt.savefig(os.path.join(plot_path, variante + "_demand_EFH1_plot.pdf"), dpi=200, bbox_inches="tight")
    fig.show()
    # data.loc[:, "MFH1_COP"] = res.loc[:, "networkModel.demandMFH1.heaPum.COP"]
    # data.loc[:, "MFH1_QEva"] = res.loc[:, "networkModel.demandMFH1.heaPum.QEva_flow"]

    plt.close("all")

def plot_MFH_results(data):
    # plot single MFH building
    matplotlib.rcParams.update(params2)
    fig, (ax1, ax2, ax3) = plt.subplots(3)

    ax1.plot(data.loc[:, "MFH1_heat"].resample('D').mean(), linewidth=0.5, color="red", label="Wärmebedarf")
    ax1.plot(data.loc[:, "MFH1_cool"].resample('D').mean(), linewidth=0.5, color="blue", label="Kältebedarf")
    ax2.plot(data.loc[:, "MFH1_ele"].resample('D').mean(), linewidth=0.5, color="green", label="Strombedarf")
    ax2.plot(-data.loc[:, "MFH1_QEva"].resample('D').mean(), linewidth=0.5, color="black", label="zugeführte Wärme")
    ax3.plot(data.loc[:, "MFH1_m_flow"].resample('D').mean(), linewidth=0.5, color="purple", label="Massenstrom")
    ax3.plot(data.loc[:, "MFH1_m_flow_nominal"].resample('D').mean(), linewidth=0.5, color="black", label="Massenstrom Auslegung", linestyle="--")

    # set labels
    ax1.set_ylabel('[kW]')
    ax2.set_ylabel('[kW]')
    ax3.set_ylabel('[kg/s]')

    # set limits
    ax1.set_ylim([0, 35])
    ax2.set_ylim([0, 30])
    ax3.set_ylim([-0.7, 1.2])
    ax1.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax2.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax3.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax1.margins(0)
    ax2.margins(0)
    ax3.margins(0)
    # ax1.axvspan(datetime.datetime(2021, 2, 7, 23, 55), datetime.datetime(2021, 2, 15, 0, 0, 0), facecolor='#EDEDED')
    # ax1.axvspan(datetime.datetime(2021, 8, 8, 23, 55), datetime.datetime(2021, 8, 16, 0, 0, 0), facecolor='#EDEDED')

    # set xaxis
    ax1.xaxis.set_major_locator(allmonths)
    ax1.xaxis.set_minor_locator(months_locator)
    ax1.xaxis.set_major_formatter(mticker.NullFormatter())
    ax1.xaxis.set_minor_formatter(months_formatter)
    ax1.tick_params(axis="x", which="minor", length=0)

    ax2.xaxis.set_major_locator(allmonths)
    ax2.xaxis.set_minor_locator(months_locator)
    ax2.xaxis.set_major_formatter(mticker.NullFormatter())
    ax2.xaxis.set_minor_formatter(months_formatter)
    ax2.tick_params(axis="x", which="minor", length=0)

    ax3.xaxis.set_major_locator(allmonths)
    ax3.xaxis.set_minor_locator(months_locator)
    ax3.xaxis.set_major_formatter(mticker.NullFormatter())
    ax3.xaxis.set_minor_formatter(months_formatter)
    ax3.tick_params(axis="x", which="minor", length=0)

    # set yaxis
    # ax1.yaxis.set_major_locator(mticker.MultipleLocator(5))
    # ax1.yaxis.set_minor_locator(mticker.MultipleLocator(2.5))

    # set legend
    # ax1.legend(loc="upper left", fontsize="x-small", frameon=True, edgecolor="white")
    fig.legend(loc=9, bbox_to_anchor=(0.5, 0.98,), ncol=3, fontsize='x-small')
    # params: 0.97 params2: 0.95
    fig.align_ylabels()

    plt.savefig(os.path.join(plot_path, variante + "_demand_MFH1_plot.pdf"), dpi=200, bbox_inches="tight")
    fig.show()
    #data.loc[:, "MFH1_COP"] = res.loc[:, "networkModel.demandMFH1.heaPum.COP"]
    #data.loc[:, "MFH1_QEva"] = res.loc[:, "networkModel.demandMFH1.heaPum.QEva_flow"]

    plt.close("all")

    # plot mass flow

    """fig, (ax1) = plt.subplots(1)

    ax1.plot(data.loc[:, "MFH1_heat"].resample('D').mean(), linewidth=0.5, color="black", label="Massenstrom MFH")
    ax1.plot(data.loc[:, "MFH1_cool"].resample('D').mean(), linewidth=0.5, color="black")
    #ax2.plot(data.loc[:, "MFH1_ele"].resample('D').mean(), linewidth=0.5, color="green", label="Strombedarf")
    #ax2.plot(-data.loc[:, "MFH1_QEva"].resample('D').mean(), linewidth=0.5, color="black", label="zugeführte Wärme")
    # ax3.plot(data.loc[:, "MFH1_COP"].resample('D').mean(), linewidth=0.5, color="black", label="COP WP")

    # set labels
    ax1.set_ylabel('Massenstrom [kg/s]')
    #ax2.set_ylabel('Leistung [kW]')
    # ax3.set_ylabel('Leistung [kW]')

    # set limits
    #ax1.set_ylim([0, 35])
    #ax2.set_ylim([0, 30])
    ax1.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    #ax2.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    # ax3.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax1.margins(0)
    ax2.margins(0)
    # ax3.margins(0.1)
    # ax1.axvspan(datetime.datetime(2021, 2, 7, 23, 55), datetime.datetime(2021, 2, 15, 0, 0, 0), facecolor='#EDEDED')
    # ax1.axvspan(datetime.datetime(2021, 8, 8, 23, 55), datetime.datetime(2021, 8, 16, 0, 0, 0), facecolor='#EDEDED')

    # set xaxis
    ax1.xaxis.set_major_locator(allmonths)
    ax1.xaxis.set_minor_locator(months_locator)
    ax1.xaxis.set_major_formatter(mticker.NullFormatter())
    ax1.xaxis.set_minor_formatter(months_formatter)
    ax1.tick_params(axis="x", which="minor", length=0)

    #ax2.xaxis.set_major_locator(allmonths)
    #ax2.xaxis.set_minor_locator(months_locator)
    ##ax2.xaxis.set_major_formatter(mticker.NullFormatter())
    #ax2.xaxis.set_minor_formatter(months_formatter)
    #ax2.tick_params(axis="x", which="minor", length=0)

    # ax3.xaxis.set_major_locator(allmonths)
    # ax3.xaxis.set_minor_locator(months_locator)
    # ax3.xaxis.set_major_formatter(mticker.NullFormatter())
    # ax3.xaxis.set_minor_formatter(months_formatter)
    # ax3.tick_params(axis="x", which="minor", length=0)

    # set yaxis
    # ax1.yaxis.set_major_locator(mticker.MultipleLocator(5))
    # ax1.yaxis.set_minor_locator(mticker.MultipleLocator(2.5))

    # set legend
    # ax1.legend(loc="upper left", fontsize="x-small", frameon=True, edgecolor="white")
    fig.legend(loc=9, bbox_to_anchor=(0.5, 0.97,), ncol=4, fontsize='x-small')
    # params: 0.97 params2: 0.95
    fig.align_ylabels()

    plt.savefig(os.path.join(plot_path, "mass_flow_MFH1_plot.pdf"), dpi=200, bbox_inches="tight")
    fig.show()
    # data.loc[:, "MFH1_COP"] = res.loc[:, "networkModel.demandMFH1.heaPum.COP"]
    # data.loc[:, "MFH1_QEva"] = res.loc[:, "networkModel.demandMFH1.heaPum.QEva_flow"]

    plt.close("all")"""

def plot_Office_results(data):
    # plot single EFH building
    matplotlib.rcParams.update(params2)
    fig, (ax1, ax2, ax3) = plt.subplots(3)

    ax1.plot(data.loc[:, "Office1_heat"].resample('D').mean(), linewidth=0.5, color="red", label="Wärmebedarf")
    ax1.plot(data.loc[:, "Office1_cool"].resample('D').mean(), linewidth=0.5, color="blue", label="Kältebedarf")
    ax2.plot(data.loc[:, "Office1_ele"].resample('D').mean(), linewidth=0.5, color="green", label="Strombedarf")
    ax2.plot(-data.loc[:, "Office1_QEva"].resample('D').mean(), linewidth=0.5, color="black", label="zugeführte Wärme")
    ax3.plot(data.loc[:, "Office1_m_flow"].resample('D').mean(), linewidth=0.5, color="purple", label="Massenstrom")
    ax3.plot(data.loc[:, "Office1_m_flow_nominal"].resample('D').mean(), linewidth=0.5, color="black", label="Massenstrom Auslegung", linestyle="--")

    # set labels
    ax1.set_ylabel('Leistung [kW]')
    ax2.set_ylabel('Leistung [kW]')
    ax3.set_ylabel('Leistung [kW]')

    # set limits
    ax1.set_ylim([0, 80])
    ax2.set_ylim([0, 80])
    ax3.set_ylim([-1, 2.8])
    ax1.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax2.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax3.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax1.margins(0)
    ax2.margins(0)
    ax3.margins(0)
    # ax1.axvspan(datetime.datetime(2021, 2, 7, 23, 55), datetime.datetime(2021, 2, 15, 0, 0, 0), facecolor='#EDEDED')
    # ax1.axvspan(datetime.datetime(2021, 8, 8, 23, 55), datetime.datetime(2021, 8, 16, 0, 0, 0), facecolor='#EDEDED')

    # set xaxis
    ax1.xaxis.set_major_locator(allmonths)
    ax1.xaxis.set_minor_locator(months_locator)
    ax1.xaxis.set_major_formatter(mticker.NullFormatter())
    ax1.xaxis.set_minor_formatter(months_formatter)
    ax1.tick_params(axis="x", which="minor", length=0)

    ax2.xaxis.set_major_locator(allmonths)
    ax2.xaxis.set_minor_locator(months_locator)
    ax2.xaxis.set_major_formatter(mticker.NullFormatter())
    ax2.xaxis.set_minor_formatter(months_formatter)
    ax2.tick_params(axis="x", which="minor", length=0)

    ax3.xaxis.set_major_locator(allmonths)
    ax3.xaxis.set_minor_locator(months_locator)
    ax3.xaxis.set_major_formatter(mticker.NullFormatter())
    ax3.xaxis.set_minor_formatter(months_formatter)
    ax3.tick_params(axis="x", which="minor", length=0)

    # set yaxis
    # ax1.yaxis.set_major_locator(mticker.MultipleLocator(5))
    # ax1.yaxis.set_minor_locator(mticker.MultipleLocator(2.5))

    # set legend
    # ax1.legend(loc="upper left", fontsize="x-small", frameon=True, edgecolor="white")
    fig.legend(loc=9, bbox_to_anchor=(0.5, 0.98,), ncol=3, fontsize='x-small')
    fig.align_ylabels()

    plt.savefig(os.path.join(plot_path, variante + "_demand_Office1_plot.pdf"), dpi=200, bbox_inches="tight")
    fig.show()
    # data.loc[:, "MFH1_COP"] = res.loc[:, "networkModel.demandMFH1.heaPum.COP"]
    # data.loc[:, "MFH1_QEva"] = res.loc[:, "networkModel.demandMFH1.heaPum.QEva_flow"]

    plt.close("all")

def plot_EZ_results(data):
    # plot EZ demands
    matplotlib.rcParams.update(params2)

    fig, (ax1, ax2) = plt.subplots(2)

    ax1.plot(data.loc[:, "EZ_heat"].resample('D').mean(), linewidth=0.5, color="red", label="Wärmebedarf")
    ax1.plot(-data.loc[:, "EZ_cool"].resample('D').mean(), linewidth=0.5, color="blue", label="Kältebedarf")
    ax2.plot(data.loc[:, "EZ_m_flow"].resample('D').mean(), linewidth=0.5, color="purple", label="Massenstrom")
    ax2.plot(data.loc[:, "EZ_m_flow_nominal"].resample('D').mean(), linewidth=0.5, color="black", label="Massenstrom Auslegung", linestyle="--")

    # set labels
    ax1.set_ylabel('[kW]')
    ax2.set_ylabel('[kg/s]')

    # set limits
    # ax1.set_ylim([19, 33])
    ax2.set_ylim([-4, 12])
    ax1.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax2.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax1.margins(0)
    ax2.margins(0)
    # ax1.axvspan(datetime.datetime(2021, 2, 7, 23, 55), datetime.datetime(2021, 2, 15, 0, 0, 0), facecolor='#EDEDED')
    # ax1.axvspan(datetime.datetime(2021, 8, 8, 23, 55), datetime.datetime(2021, 8, 16, 0, 0, 0), facecolor='#EDEDED')

    # set xaxis
    ax1.xaxis.set_major_locator(allmonths)
    ax1.xaxis.set_minor_locator(months_locator)
    ax1.xaxis.set_major_formatter(mticker.NullFormatter())
    ax1.xaxis.set_minor_formatter(months_formatter)
    ax1.tick_params(axis="x", which="minor", length=0)

    ax2.xaxis.set_major_locator(allmonths)
    ax2.xaxis.set_minor_locator(months_locator)
    ax2.xaxis.set_major_formatter(mticker.NullFormatter())
    ax2.xaxis.set_minor_formatter(months_formatter)
    ax2.tick_params(axis="x", which="minor", length=0)

    # set yaxis
    ax2.yaxis.set_major_locator(mticker.MultipleLocator(4))
    ax2.yaxis.set_minor_locator(mticker.MultipleLocator(2))

    # set legend
    # ax1.legend(loc="upper left", fontsize="x-small", frameon=True, edgecolor="white")
    fig.legend(loc=9, bbox_to_anchor=(0.5, 0.95), ncol=4, fontsize='x-small')
    fig.align_ylabels()

    plt.savefig(os.path.join(plot_path, variante + "_demand_EZ_plot.pdf"), dpi=200, bbox_inches="tight")
    fig.show()
    plt.close("all")

def compare_dhc_results(data1, data2, title, linestyles="dotted"):
    # plot all buildings added up demands
    matplotlib.rcParams.update(params2)

    fig, (ax1, ax2) = plt.subplots(2)

    ax1.plot(data1.loc[:, "dhc_heat_series"].resample('D').mean(), linewidth=0.5, color="red", label="Wärmebedarf")
    ax1.plot(data1.loc[:, "dhc_cool_series"].resample('D').mean(), linewidth=0.5, color="blue", label="Kältebedarf")
    ax2.plot(data1.loc[:, "dhc_ele_series"].resample('D').mean(), linewidth=0.5, color="green", label="Strombedarf")
    ax2.plot(-data1.loc[:, "dhc_net_to_bldg_series"].resample('D').mean(), linewidth=0.5, color="black",
             label="zugeführte Wärme")

    ax1.plot(data2.loc[:, "dhc_heat_series"].resample('D').mean(), linewidth=0.5, color="red", linestyle=linestyles)
    ax1.plot(data2.loc[:, "dhc_cool_series"].resample('D').mean(), linewidth=0.5, color="blue", linestyle=linestyles)
    ax2.plot(data2.loc[:, "dhc_ele_series"].resample('D').mean(), linewidth=0.5, color="green", linestyle=linestyles)
    ax2.plot(-data2.loc[:, "dhc_net_to_bldg_series"].resample('D').mean(), linewidth=0.5, color="black",
             linestyle=linestyles)

    # set labels
    ax1.set_ylabel('Leistung [kW]')
    ax2.set_ylabel('Leistung [kW]')

    # set limits
    # ax1.set_ylim([19, 33])
    ax1.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax2.set_xlim(datetime.datetime(2021, 1, 1, 0, 0, 0), datetime.datetime(2021, 12, 31, 23, 55))
    ax1.margins(0)
    ax2.margins(0)
    # ax1.axvspan(datetime.datetime(2021, 2, 7, 23, 55), datetime.datetime(2021, 2, 15, 0, 0, 0), facecolor='#EDEDED')
    # ax1.axvspan(datetime.datetime(2021, 8, 8, 23, 55), datetime.datetime(2021, 8, 16, 0, 0, 0), facecolor='#EDEDED')

    # set xaxis
    ax1.xaxis.set_major_locator(allmonths)
    ax1.xaxis.set_minor_locator(months_locator)
    ax1.xaxis.set_major_formatter(mticker.NullFormatter())
    ax1.xaxis.set_minor_formatter(months_formatter)
    ax1.tick_params(axis="x", which="minor", length=0)

    ax2.xaxis.set_major_locator(allmonths)
    ax2.xaxis.set_minor_locator(months_locator)
    ax2.xaxis.set_major_formatter(mticker.NullFormatter())
    ax2.xaxis.set_minor_formatter(months_formatter)
    ax2.tick_params(axis="x", which="minor", length=0)

    # set yaxis
    # ax1.yaxis.set_major_locator(mticker.MultipleLocator(10))
    # ax1.yaxis.set_minor_locator(mticker.MultipleLocator(5))

    # set legend
    # ax1.legend(loc="upper left", fontsize="x-small", frameon=True, edgecolor="white")
    fig.suptitle(title, fontsize="small")
    fig.legend(loc=9, bbox_to_anchor=(0.515, 0.95), ncol=4, fontsize='x-small')
    fig.align_ylabels()

    plt.savefig(os.path.join(plot_path, variante + "_compare_to_Ref_DHC_plot.pdf"), dpi=200, bbox_inches="tight")
    fig.show()
    plt.close("all")

if __name__ == '__main__':

    # set your simulation variant here
    variante = "v1"

    # set your file_name and folder here
    if variante == "v1":
        file_name = "Sim20210708142806GenericNetwork_inputs1"
        folder = "Variante_1_ChristianKonvektiv_bei40Grad"
    elif variante == "v2":
        file_name = "Sim20210708142806GenericNetwork_inputs2"
        folder = "Variante_2_ChristianRadiator"
    elif variante == "v3":
        file_name = "Sim20210708142806GenericNetwork_inputs3"
        folder = "Variante_3_ChristianTABS+_bei25Grad"
    elif variante == "v4":
        file_name = "Sim20210708142806GenericNetwork_inputs4"
        folder = "Variante_4_Radiator_TABS+"
    elif variante == "v5":
        file_name = "Sim20210708142806GenericNetwork_inputs5"
        folder = "Variante_5_FHK_TABS+"

    # set path to your workspace here
    workspace = os.path.join("D:\\", "tbl-cwe", "Final_Simulations", "DHC")
    print("Your workspace is set to: " + workspace)

    # set path to desired sim_results_file here
    sim_results_file_path = os.path.join("T:\\", "tbl-cwe", "Netzmodell Christian", "Dymola", folder,
                                         file_name + ".mat")
    print("Your .mat file is stored in: " + sim_results_file_path)

    output_path = os.path.join(workspace, folder)
    print("Your calculation results are stored in: " + output_path)

    plot_path = os.path.join(workspace, folder, "DHC_plots")
    if not os.path.exists(plot_path):
        os.makedirs(plot_path)
    print("Your plots are stored in: " + plot_path)

    ##########################
    # set list of simulation result variables
    res_list = ['Time']
    res_list += ['networkModel.demandMFH{}.heaDem'.format(i + 1) for i in range(5)]
    res_list += ['networkModel.demandSFH{}.heaDem'.format(i + 1) for i in range(20)]
    res_list += ['networkModel.demandOffice{}.heaDem'.format(i + 1) for i in range(2)]
    res_list += ['networkModel.demandMFH{}.cooDem'.format(i + 1) for i in range(5)]
    res_list += ['networkModel.demandSFH{}.cooDem'.format(i + 1) for i in range(20)]
    res_list += ['networkModel.demandOffice{}.cooDem'.format(i + 1) for i in range(2)]
    res_list += ['networkModel.demandMFH{}.heaPum.P'.format(i + 1) for i in range(5)]
    res_list += ['networkModel.demandSFH{}.heaPum.P'.format(i + 1) for i in range(20)]
    res_list += ['networkModel.demandOffice{}.heaPum.P'.format(i + 1) for i in range(2)]
    res_list += ['networkModel.demandMFH{}.heaPum.COP'.format(i + 1) for i in range(5)]
    res_list += ['networkModel.demandSFH{}.heaPum.COP'.format(i + 1) for i in range(20)]
    res_list += ['networkModel.demandOffice{}.heaPum.COP'.format(i + 1) for i in range(2)]
    res_list += ['networkModel.demandMFH{}.heaPum.QEva_flow'.format(i + 1) for i in range(5)]
    res_list += ['networkModel.demandSFH{}.heaPum.QEva_flow'.format(i + 1) for i in range(20)]
    res_list += ['networkModel.demandOffice{}.heaPum.QEva_flow'.format(i + 1) for i in range(2)]
    res_list += ['networkModel.demandMFH{}.port_a.m_flow'.format(i + 1) for i in range(5)]
    res_list += ['networkModel.demandMFH{}.m_flow_nominal'.format(i + 1) for i in range(5)]
    res_list += ['networkModel.demandSFH{}.port_a.m_flow'.format(i + 1) for i in range(20)]
    res_list += ['networkModel.demandSFH{}.m_flow_nominal'.format(i + 1) for i in range(20)]
    res_list += ['networkModel.demandOffice{}.port_a.m_flow'.format(i + 1) for i in range(2)]
    res_list += ['networkModel.demandOffice{}.m_flow_nominal'.format(i + 1) for i in range(2)]
    res_list += ['networkModel.supplysupply.hea.Q_flow']
    res_list += ['networkModel.supplysupply.coo.Q_flow']
    res_list += ['networkModel.supplysupply.port_a.m_flow']
    res_list += ['networkModel.supplysupply.m_flow_nominal']

    """print("reading data")
    res = read_results(signals=res_list,
                       index=pd.date_range(
                           datetime.datetime(2021, 1, 1), periods=8761, freq="H",
                       ), results_path=sim_results_file_path,
                        file=file_name,
                       csv_path=output_path)"""

    # read hourly demands
    res = pd.read_csv(os.path.join(output_path, file_name + "_res.csv"), index_col=0)
    res_ref = pd.read_csv(os.path.join(workspace, "Variante_1_ChristianKonvektiv_bei40Grad", "Sim20210708142806GenericNetwork_inputs1_res.csv"), index_col=0)

    # calculate KPIs and process data for plotting
    data = calc_and_process_data(res)
    data_ref = calc_and_process_data(res_ref)


    # plot results

    #plot_dhc_results(data_ref)
    #plot_EZ_results(data)
    plot_EFH_results(data)
    plot_MFH_results(data)
    #plot_Office_results(data)
    #compare_dhc_results(data, data_ref, title="Variante 1 (gestrichelt) im Vergleich zu Variante 5", linestyles="--")


    # clear plot lines, keep axes
    #for artist in ax1.lines + ax1.collections + ax2.lines + ax2.collections:
    #    artist.remove()"""
