"""Module to read results with DymolaInterface."""

import datetime
import os
import collections
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import pandas as pd

from dymola.dymola_interface import DymolaInterface

# This module reads simulation results from Dymola simulation of TEASER
# buidlings and saves heating, cooling and electricity demand (ventilation) into
# seperate *.csv files for further usage. It needs the TEASER projects with the
# exact same naming of the one that was simulated (Project and buildings)

# To use this module: simply copy it into your folder.

# Example
# -------
#
# >>> from teaser.project import Project
# >>> import simulate as sim

# Generate TEASER Project, add buildings, and export models.
# >>> prj = Project()
# >>> prj.add_residential(
#       method='tabula_de',
#       usage='single_family_house',
#       name="ResidentialBuildingTabula",
#       year_of_construction=1988,
#       number_of_floors=3,
#       height_of_floors=3.2,
#       net_leased_area=280,
#       construction_type='tabula_standard')
#
# Specify path to your simulation workspace
# >>> workspace = os.path.join(
#     'D:\\',
#     'workspaces',
#     'YOUR SIMULATION')
# Call read_results function
# >>> read_results(
#       prj=prj,
#       index=pd.date_range(
#           datetime.datetime(2018, 1, 1),
#           periods=8761,
#           freq='H',
#           tz='Europe/Berlin'),
#       results_path=os.path.join(workspace, 'results', prj.name),
#       csv_path=os.path.join(dir_source, 'sim_results'))


def read_results(
    prj,
    buildings,
    signals,
    index=pd.date_range(
        datetime.datetime(2021, 1, 1), periods=8760, freq="H", tz="Europe/Berlin"
    ),
    results_path=None,
    csv_path=None,
    indoor_air=False,
):
    """Read simulation data from .mat file and save them into csv.

    Reads Dymola result files and saves them as time series in csv. Naming
    convention of time series follows proposed naming schema of Team GA. It
    assumes that all thermal_zones in PostgreSQL database are modeled as a
    thermal zone in Modelica. Thus this approach is not yet ready to be used
    with archetypes.

    Parameters
    ----------
    prj : TEASER Project() instance
        TEASER Project with all buildings that have been simulated. Names need
        to be identical.
    buidlings : list
        List of buildings whose results should be read.
    signals : list
            List of signals to be read from the results file.
    index : Pandas date_range
        Pandas date range of the simulation data. Must fit the length of
        simulation data. (default: hourly for year 2015)
    results_path : str
        Path where Dymola results are  stored.
    csv_path : str
        Path where csv results should be stored.
    indoor_air : boolean
        If true, output csv-file contains dataframe with one column for each given
        signal. If false, Heater and Cooler signals are expected and seperate output
        csv-files are created for both signals.

    """

    if not os.path.exists(csv_path):
        os.makedirs(csv_path)
    dymola = DymolaInterface()

    for bldg in buildings:
        print("reading building {}".format(bldg.name))

        if not (bldg.name + "_heat.csv") in os.listdir(csv_path):
            try:
                print(os.path.join(results_path, bldg.name + ".mat"))

                dym_res = dymola.readTrajectory(
                    fileName=os.path.join(results_path, bldg.name + ".mat"),
                    signals=signals,
                    rows=dymola.readTrajectorySize(
                        fileName=os.path.join(results_path, bldg.name + ".mat")
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
                    "please check result file".format(bldg.name)
                )
                raise Exception("Results Error!")
                continue
            try:
                results.index = index
            except ValueError:
                print(
                    "Simulation results of building {} are most likely "
                    "faulty (series is shorter then one year), please check "
                    "result file".format(bldg.name)
                )
                raise Exception("Completion Error!")

            if indoor_air is False:
                heat = pd.DataFrame(
                    data=results.filter(like="PHeat").sum(axis=1),
                    index=results.index,
                    columns=[bldg.name + " heat"],
                )

                cool = pd.DataFrame(
                    data=results.filter(like="PCool").abs().sum(axis=1),
                    index=results.index,
                    columns=[bldg.name + " cool"],
                )

                heat.to_csv(os.path.join(csv_path, bldg.name + "_heat.csv"))
                cool.to_csv(os.path.join(csv_path, bldg.name + "_cool.csv"))
                
                
                heat.index = [(i ) * 3600 for i in range(8760)]
                heat.to_csv(os.path.join(csv_path, bldg.name + "_heat.txt"), header=False)
#                heat_bldg = heat[bldg.name + " heat"]
#                heat_bldg.to_csv(bldg.name + "_heat.txt", header=False)

                with open(os.path.join(csv_path, bldg.name + "_heat.txt")) as f:
                    lines = f.readlines()
    
                    lines.insert(0, "#1\n")
                    lines.insert(1,'double heat(35037,2)\n')
      
                with open(os.path.join(csv_path, bldg.name + "_heat.txt"), "w") as f:
                    f.writelines(lines)
        
                f.close()    
                    
                
                cool.index = [(i ) * 3600 for i in range(8760)]
                cool.to_csv(os.path.join(csv_path, bldg.name + "_cool.txt"), header=False)
#                cool_bldg = cool[bldg.name + " cool"]
#                cool_bldg.to_csv(bldg.name + "_cool.txt", header=False)

                with open(os.path.join(csv_path, bldg.name + "_cool.txt")) as f:
                    lines = f.readlines()
    
                    lines.insert(0, "#1\n")
                    lines.insert(1,'double cool(35037,2)\n')
      
                with open(os.path.join(csv_path, bldg.name + "_cool.txt"), "w") as f:
                    f.writelines(lines)
        
                f.close()   
                                 

            else:
                results.to_csv(os.path.join(csv_path, bldg.name + "_indoor_air.csv"))

    dymola.close()


def compact_results(buildings, csv_path, output_path):
    """Create json-file containing KPIs of buildings.

    Parameters
    ----------
    buildings : list of TEASER bldgs
    csv_path : str
        Path where hourly demands created by read_results.py are stored.
    output_path : str
        Path where output files should be stored.

    """
    results = collections.OrderedDict()
    for bldg in buildings:
        # read hourly demands
        heat_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_heat.csv"))
        cool_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_cool.csv"))
        plot_results(
            heat=heat_data,
            cool=cool_data,
            title=bldg.name,
            output_path=os.path.join(csv_path, bldg.name + "_plt.pdf"),
        )
        # calculate annual heating and cooling demand
        # for 15 minutes resolution this needs to be divided by 4
        annual_heat_data = heat_data.sum()
        annual_cool_data = cool_data.sum()
        annual_heat = annual_heat_data.iloc[1] / 1000 / 4
        annual_cool = annual_cool_data.iloc[1] / 1000 / 4
        # calculate specific annual heating and cooling demand
        spec_annual_heat = annual_heat / bldg.net_leased_area
        spec_annual_cool = annual_cool / bldg.net_leased_area
        # determine maximum values
        max_heat = heat_data.iloc[:, 1].max() / 1000
        max_cool = cool_data.iloc[:, 1].max() / 1000
        # calculate specific maximum values
        spec_max_heat = max_heat * 1000 / bldg.net_leased_area
        spec_max_cool = max_cool * 1000 / bldg.net_leased_area

        results[bldg.name] = collections.OrderedDict(
            {
                "Year of construction": bldg.year_of_construction,
                "Net area": bldg.net_leased_area,
                "Footprint area": bldg.ground_floor_geo["GroundFloor"]["area"],
                "Volume": bldg.volume,
                "A/V": bldg.library_attr.total_surface_area / bldg.volume,
                "Annual heating demand [kWh/a]": round(annual_heat, 1),
                "Annual cooling demand [kWh/a]": round(annual_cool, 1),
                "Specific annual heating demand [kWh/sqm*a]": round(
                    spec_annual_heat, 1
                ),
                "Specific annual cooling demand [kWh/sqm*a]": round(
                    spec_annual_cool, 1
                ),
                "Maximum heating power [kW]": round(max_heat, 1),
                "Maximum cooling power [kW]": round(max_cool, 1),
                "Specific maximum heating power [W/sqm]": round(spec_max_heat, 1),
                "Specific maximum cooling power [W/sqm]": round(spec_max_cool, 1),
            }
        )
    with open(
        os.path.join(output_path, buildings[0].parent.name + "_results.json"), "w"
    ) as file:
        file.write(json.dumps(results, indent=4, separators=(",", ": ")))
    return results


def compact_results_heatbeat(buildings, csv_path, output_path):
    """Create json-file containing KPIs of buildings.

    Parameters
    ----------
    buildings : list of TEASER bldgs
    csv_path : str
        Path where hourly demands created by read_results.py are stored.
    output_path : str
        Path where output files should be stored.

    """
    results = collections.OrderedDict()
    for bldg in buildings:
        # read hourly demands
        heat_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_heat.csv"))
        cool_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_cool.csv"))
        plot_results(
            heat=heat_data,
            cool=cool_data,
            title=bldg.name,
            output_path=os.path.join(csv_path, bldg.name + "_plt.pdf"),
        )
        # calculate annual heating and cooling demand
        annual_heat_data = heat_data.sum()
        annual_cool_data = cool_data.sum()
        annual_heat = annual_heat_data.iloc[1] / 1000
        annual_cool = annual_cool_data.iloc[1] / 1000
        # calculate specific annual heating and cooling demand
        spec_annual_heat = annual_heat / bldg.net_leased_area
        spec_annual_cool = annual_cool / bldg.net_leased_area
        # determine maximum values
        max_heat = heat_data.iloc[:, 1].max() / 1000
        max_cool = cool_data.iloc[:, 1].max() / 1000
        # calculate specific maximum values
        spec_max_heat = max_heat * 1000 / bldg.net_leased_area
        spec_max_cool = max_cool * 1000 / bldg.net_leased_area

        results[bldg.name] = collections.OrderedDict(
            {
                "Year of construction": bldg.year_of_construction,
                "Net area": bldg.net_leased_area,
                "Volume": bldg.volume,
                "A/V": bldg.library_attr.total_surface_area / bldg.volume,
                "Annual heating demand [kWh/a]": round(annual_heat, 1),
                "Annual cooling demand [kWh/a]": round(annual_cool, 1),
                "Specific annual heating demand [kWh/sqm*a]": round(
                    spec_annual_heat, 1
                ),
                "Specific annual cooling demand [kWh/sqm*a]": round(
                    spec_annual_cool, 1
                ),
                "Maximum heating power [kW]": round(max_heat, 1),
                "Maximum cooling power [kW]": round(max_cool, 1),
                "Specific maximum heating power [W/sqm]": round(spec_max_heat, 1),
                "Specific maximum cooling power [W/sqm]": round(spec_max_cool, 1),
            }
        )
    with open(
        os.path.join(output_path, buildings[0].parent.name + "_results.json"), "w"
    ) as file:
        file.write(json.dumps(results, indent=4, separators=(",", ": ")))
    return results


def plot_results(heat, cool, title, output_path):
    """Very simple and basic plotting of heating and cooling time series."""
    data = pd.DataFrame(
        index=pd.date_range(
            start=datetime.datetime(2021, 1, 1, 0, 0, 0),
            end=datetime.datetime(2021, 12, 31, 23, 00),
            freq="15min",
        ),
        columns=["Wärmeleistung", "Kälteleistung"],
    )
    data["Wärmeleistung"] = heat.iloc[:, 1].values / 1000
    data["Kälteleistung"] = -cool.iloc[:, 1].values / 1000
    # data = data.dropna()

    ax = sns.lineplot(
        data=data,
        hue={"ls": ["-", "--"]},
        palette=["#407FB7", "#646567"],
        linewidth=1.5,
    )

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m"))
    plt.title(title)
    plt.savefig(output_path, dpi=200)
    plt.clf()
    ax = sns.lineplot(
        data=data.resample("D").mean(),
        hue={"ls": ["-", "--"]},
        palette=["#407FB7", "#646567"],
        linewidth=1.5,
    )
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%d-%m"))
    plt.title(title + " D")
    plt.savefig(output_path.replace("plt", "plt_D"), dpi=200)
    plt.clf()
