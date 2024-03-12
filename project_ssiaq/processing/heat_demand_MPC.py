import os
import sys
# Add ddmpc directory to path and change back to current path
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
ddmpc_dir = os.path.join(parentdir, 'MPC\setup_data')
sys.path.append(ddmpc_dir)
os.chdir(currentdir)
from ddmpc.data_handling.storing_data import load_DataHandler
from scipy import integrate
from pathlib import Path
from project_ssiaq.simulate_scenarios import load_scenarios
import matplotlib.pyplot as plt
import pandas as pd

def get_zone_number(building_class, building_type):
    """
    Returns number of zones for defined building classes and types
    """
    #TODO: get zone number directly from building type instances
    building_type_dict = {'office': 6,
                          'school': 8,
                          'hotel': 9}
    if building_class == "residential":
        return 1
    else:
        return building_type_dict[building_type]

def plot_Q_flow(df, zone_nr,color_map):
    plt.figure(dpi=300)

    for idx in range(zone_nr):
        plot_param_1 = "multizone.PHeater[" + str(idx + 1) + "]"
        label_1 = "P_Heater - " + str(idx)
        plt.plot(df.loc[:, plot_param_1], label=label_1, color=color_map[idx])

    plt.xlabel('Time')
    plt.ylabel('Power in W')
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.show()
    plt.close()

def plot_T_Air(df, zone_nr,color_map):
    plt.figure(dpi=300)

    for idx in range(zone_nr):
        plot_param = "TAirOutput[" + str(idx + 1) + "]"
        label = "T_air - " + str(idx)
        plt.plot(df.loc[:, plot_param]-273.15, label=label, color=color_map[idx])

    plt.xlabel('Time')
    plt.ylabel('Air temperature in °C')
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    plt.show()
    plt.close()


if __name__ == '__main__':

    setup_name = "20240310_reduced_scenarios"
    basepath = Path(r'R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten\03_Modellpraediktive_Regelung').joinpath(
        setup_name, "mpc")
    scenarios = load_scenarios(basepath.parent.joinpath("scenarios.xlsx"))

    start_row = 1  # row index of excel sheet != actual scenario number
    end_row = 3

    result_df = pd.DataFrame(
        columns=['Scenario', 'Building type', 'Num Zones', 'Heat demand total', 'Net area', 'Construction year'],
        index=range(end_row))

    for index, scenario in scenarios.iterrows():
        if index + 1 < start_row or index + 1 > end_row:
            continue  # skip scenarios until start_scenario is reached
        scenario_name = "S" + str(scenario['Scenario_number']) + "_" + str(scenario['Building_type'])
        filefolder = basepath.joinpath(scenario_name, "stored_data\data")
        num_zones = get_zone_number(scenario['Building_class'], scenario['Building_type'])

        dh = load_DataHandler(filename='mpc_data',folder=filefolder)
        dh.merge()
        df = dh.containers[0].df
        heat_demand_zonal = list()
        for zone in range(num_zones):
            heat_demand_zonal.append(integrate.trapezoid(df["multizone.PHeater["+str(zone+1)+"]"], df["SimTime"]/3600/1000)) # in kWh
        heat_demand_total = sum(heat_demand_zonal)
        result_df.loc[index] = {'Scenario': scenario['Scenario_number'], 'Building type': scenario['Building_type'], 'Num Zones': num_zones,
                       'Heat demand total': heat_demand_total, 'Net area': scenario["Net_Area"],
                       'Construction year': scenario["Year_of_construction"]}
        # cmap = plt.get_cmap('plasma')
        # slicedCM = cmap(np.linspace(0, 1, num_zones))
        # plot_Q_flow(df, num_zones,slicedCM)
        # plot_T_Air(df, num_zones,slicedCM)

    result_df["Specific heat demand"] = result_df['Heat demand total'] / result_df['Net area']
    result_df.to_pickle(basepath.joinpath('dataframe_heat_demand_total.pkl'))
    print("Saved pickle to:",str(basepath.joinpath('dataframe_heat_demand_total.pkl')))
