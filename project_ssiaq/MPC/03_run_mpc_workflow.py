import sys
import os
import subprocess
import pathlib
from project_ssiaq.simulate_scenarios import *


if __name__ == "__main__":
        setup_name = "20240304_mpc_test2"
        #basepath = pathlib.Path('R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten/03_Modellpraediktive_Regelung').joinpath(
        #        setup_name)
        basepath = pathlib.Path(r'D:\pse\temp_SSIAQ').joinpath(setup_name)
        mpc_path = basepath.joinpath('mpc')
        scenarios = load_scenarios(basepath.joinpath("scenarios_test.xlsx"))

        start_scenario = 2 # row index of excel sheet != actual scenario number
        for index, scenario in scenarios.iterrows():
            if index + 1 < start_scenario:
                continue  # skip scenarios until start_scenario is reached
            scenario_name = "S" + str(scenario['Scenario_number']) + "_" + str(scenario['Building_type'])

            # create folder for each scenario
            scenario_path = mpc_path.joinpath(scenario_name)

            subprocess.run([""+sys.executable, scenario_path.joinpath('2_generate_data.py')])
            subprocess.run([""+sys.executable, scenario_path.joinpath('3_fit_linreg_TAirRoom.py')])
            subprocess.run([""+sys.executable, scenario_path.joinpath('4_mpc.py')])
