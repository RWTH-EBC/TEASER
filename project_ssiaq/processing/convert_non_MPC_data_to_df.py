from pathlib import Path
import re
import pickle
import pandas as pd
from project_ssiaq.visualization.evaluation import get_bldg_type_from_filename
from project_ssiaq.simulate_scenarios import load_scenarios

if __name__ == '__main__':
    """
    setup_name = "20230803_ddc_rand"
    basepath = Path(r'R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten\02_Bedarfsorientierte_Regelung').joinpath(
        setup_name, "sim_results")
    """
    setup_name = "20230802_referenz_rand"
    basepath = Path(r'R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten\01_Referenzszenarien').joinpath(
        setup_name, "sim_results")

    scenarios = load_scenarios(basepath.parent.joinpath("scenarios_full.xlsx"))
    pathlist = Path(basepath).rglob('*.mat')

    df = pd.DataFrame(columns=['Scenario', 'Building type', 'Num Zones','Heat demand total','Comfort violations','Net area','Construction year'],index=range(10))

    for idx, path in enumerate(pathlist):
        building_type, scenario = get_bldg_type_from_filename(str(path))
        scenario = int(re.findall(r'\d+', scenario)[0])
        net_area = scenarios.loc[scenarios['Scenario_number'] == scenario]["Net_Area"].values[0]
        year_of_construction = scenarios.loc[scenarios['Scenario_number'] == scenario]["Year_of_construction"].values[0]
        filename = str(path.parts[-2])

        #import heat demand
        with open(path.parent.joinpath('heat_demand.pkl'),'rb') as f:
           heat_data = pickle.load(f)
        heat_demand_zonal = heat_data[0]
        heat_demand_total = heat_data[1]
        num_zones = len(heat_demand_zonal)

        #import comfort violations
        with open(path.parent.joinpath('comfort_violations.pkl'),'rb') as f:
           comfort_data = pickle.load(f)
        comfort_violations_zonal = comfort_data[0]
        comfort_violations_total = comfort_data[1]


        df.loc[idx] = {'Scenario': scenario, 'Building type': building_type, 'Num Zones': num_zones,
                       'Heat demand total': heat_demand_total, 'Comfort violations' :comfort_violations_total,
                       'Net area': net_area, 'Construction year': year_of_construction}

    df["Specific heat demand"] = df['Heat demand total']/df['Net area']
    df.to_pickle(basepath.joinpath('dataframe_heat_comfort_total.pkl'))
    print("Saved pickle to:",str(basepath.joinpath('dataframe_heat_comfort_total.pkl')))