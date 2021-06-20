import os
import pickle
import pandas as pd

import read_results as res

def calc_power(buildings, csv_path, output_path):
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

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    results = pd.DataFrame()

    for bldg in buildings:
        try:
            print("reading building {}".format(bldg.name))
            # read hourly demands
            power_data = pd.read_csv(os.path.join(csv_path, bldg.name + "_power.csv"))

            # calculate annual heating and cooling demand
            power_heat_tabs = power_data.loc[:, bldg.name + " powerHeatTabs"].max() / 1000
            power_cool_tabs = power_data.loc[:, bldg.name + " powerCoolTabs"].max() / 1000
            power_heat_panel = power_data.loc[:, bldg.name + " hHeatPanel"].max() / 1000
            power_cool_panel = power_data.loc[:, bldg.name + " lCoolPanel"].max() / 1000
            power_heat_rem = power_data.loc[:, bldg.name + " hHeatRem"].max() / 1000
            power_cool_rem = power_data.loc[:, bldg.name + " lCoolRem"].max() / 1000
            power_heat_tabsplus = (power_data.loc[:, bldg.name + " powerHeatTabs"].max() + power_data.loc[:, bldg.name + " hHeatRem"].max()) / 1000
            power_cool_tabsplus = (power_data.loc[:, bldg.name + " powerCoolTabs"].max() + power_data.loc[:, bldg.name + " lCoolRem"].max()) / 1000

            # calculate specific annual heating and cooling demand
            spec_power_heat_tabs = power_heat_tabs *1000 / bldg.net_leased_area
            spec_power_cool_tabs = power_cool_tabs *1000 / bldg.net_leased_area
            spec_power_heat_panel = power_heat_panel *1000 / bldg.net_leased_area
            spec_power_cool_panel = power_cool_panel *1000 / bldg.net_leased_area
            spec_power_heat_rem = power_heat_rem *1000 / bldg.net_leased_area
            spec_power_cool_rem = power_cool_rem *1000 / bldg.net_leased_area
            spec_power_heat_tabsplus = power_heat_tabsplus * 1000 / bldg.net_leased_area
            spec_power_cool_tabsplus = power_cool_tabsplus * 1000 / bldg.net_leased_area

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

            if "radiator" in bldg.name:
                results.loc[bldg.name, "Heating Power Rem [kW]"] = round(power_heat_rem, 1)
                results.loc[bldg.name, "Specific Heating Power Rem [W/sqm]"] = round(spec_power_heat_rem, 1)
            elif "convective" in bldg.name:
                results.loc[bldg.name, "Heating Power Rem [kW]"] = round(power_heat_rem, 1)
                results.loc[bldg.name, "Specific Heating Power Rem [W/sqm]"] = round(spec_power_heat_rem, 1)
                results.loc[bldg.name, "Cooling Power Rem [kW]"] = round(power_cool_rem, 1)
                results.loc[bldg.name, "Specific Cooling Power Rem [W/sqm]"] = round(spec_power_cool_rem, 1)
            elif "panel" in bldg.name:
                results.loc[bldg.name, "Heating Power Panel [kW]"] = round(power_heat_panel, 1)
                results.loc[bldg.name, "Specific Heating Power Panel [W/sqm]"] = round(spec_power_heat_panel, 1)
                results.loc[bldg.name, "Cooling Power Panel [kW]"] = round(power_cool_panel, 1)
                results.loc[bldg.name, "Specific Cooling Power Panel [W/sqm]"] = round(spec_power_cool_panel, 1)
            elif "tabsplusair" in bldg.name:
                results.loc[bldg.name, "Heating Power TABS [kW]"] = round(power_heat_tabs, 1)
                results.loc[bldg.name, "Specific Heating Power TABS [W/sqm]"] = round(spec_power_heat_tabs, 1)
                results.loc[bldg.name, "Cooling Power TABS [kW]"] = round(power_cool_tabs, 1)
                results.loc[bldg.name, "Specific Cooling Power TABS [W/sqm]"] = round(spec_power_cool_tabs, 1)
                results.loc[bldg.name, "Heating Power Rem [kW]"] = round(power_heat_rem, 1)
                results.loc[bldg.name, "Specific Heating Power Rem [W/sqm]"] = round(spec_power_heat_rem, 1)
                results.loc[bldg.name, "Cooling Power Rem [kW]"] = round(power_cool_rem, 1)
                results.loc[bldg.name, "Specific Cooling Power Rem [W/sqm]"] = round(spec_power_cool_rem, 1)
                results.loc[bldg.name, "Heating Power TABSplusAir [kW]"] = round(power_heat_tabsplus, 1)
                results.loc[bldg.name, "Specific Heating Power TABSplusAir [W/sqm]"] = round(spec_power_heat_tabsplus, 1)
                results.loc[bldg.name, "Cooling Power TABSplusAir [kW]"] = round(power_cool_tabsplus, 1)
                results.loc[bldg.name, "Specific Cooling Power TABSplusAir [W/sqm]"] = round(spec_power_cool_tabsplus, 1)


        except BaseException:
            # Dymola has strange exceptions
            print(
                "Reading results of building {} failed, "
                "please check result file".format(bldg.name)
            )
            # raise Exception("Results Error!")
            continue

    results.to_csv(os.path.join(output_path, "systempower_calc.csv"))
    results.to_excel(os.path.join(output_path, "systempower_excel_calc.xlsx"))
    print("Calculations done! :)")

if __name__ == '__main__':

    # set path to your workspace here
    workspace = os.path.join("D:\\", "tbl-cwe", "TABS_power", "Simulationsstudie_TABS_60")
    print("Your workspace is set to: " + workspace)

    load_pickle = os.path.join(workspace, "building_simulation_pickle.p")
    pickle_prj = pickle.load(open(load_pickle, "rb"))

    output_path = os.path.join(workspace, "calc_results")
    print("Your calculation results are stored in: " + output_path)

    csv_results_path = os.path.join(workspace, "csv_results", "power_comparison")
    print("Your .csv  files are stored in: " + csv_results_path)

    print("##########")
    calc_power(
        buildings=pickle_prj.buildings,
        csv_path=csv_results_path,
        output_path=output_path)