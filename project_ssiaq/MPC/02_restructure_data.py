'''

In this file folders are generated to prepare the ddmpc workflow.
Files are copied from the folder setup_data to the building folders in 'BuildingsSimulation'.

'''

import glob
import shutil
import pandas as pd
import os
import pathlib
from project_ssiaq.simulate_scenarios import *

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

if __name__ == "__main__":
        setup_name = "20240310_reduced_scenarios"
        #basepath = pathlib.Path('R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten/03_Modellpraediktive_Regelung').joinpath(
        #        setup_name)
        basepath = pathlib.Path(r'D:\pse\temp_SSIAQ').joinpath(setup_name)

        mpc_path = basepath.joinpath('mpc')
        if not os.path.exists(basepath.joinpath('ddmpc')):
            shutil.copytree('setup_data/ddmpc', basepath.joinpath('ddmpc'))

        scenarios = load_scenarios(basepath.joinpath("scenarios.xlsx"))

        start_row = 1  # row index of excel sheet != actual scenario number
        end_row = 3
        for index, scenario in scenarios.iterrows():
                if index + 1 < start_row or index + 1 > end_row:
                    continue  # skip scenarios until start_scenario is reached
                scenario_name = "S" + str(scenario['Scenario_number']) + "_" + str(scenario['Building_type'])

                # create folder for each scenario
                scenario_path = mpc_path.joinpath(scenario_name)

                os.makedirs(scenario_path, exist_ok=True)

                # create stored_data, fmu and schedules folder for each scenario
                os.makedirs(scenario_path.joinpath('stored_data','fmus'), exist_ok=True)
                os.makedirs(scenario_path.joinpath('stored_data', 'schedules'), exist_ok=True)

                # copy FMUs
                source_folder = basepath.joinpath('fmus',scenario_name)
                destination_folder = scenario_path.joinpath('stored_data','FMUs')
                file_type = ".fmu"
                if os.path.exists(basepath.joinpath('fmus',scenario_name)):
                    for file in os.listdir(source_folder):
                        if file.endswith(file_type):
                            source_path = source_folder.joinpath(file)
                            destination_path = destination_folder.joinpath(file)
                            shutil.copy(source_path,destination_path)
                else:
                    print("Please check if FMU path is correct")


                # copy schedules
                source_folder = basepath.joinpath('schedules', scenario_name)
                destination_folder = scenario_path.joinpath('stored_data', 'schedules')
                file_type = ".pkl"
                if os.path.exists(basepath.joinpath('schedules', scenario_name)):
                    for file in os.listdir(source_folder):
                        if file.endswith(file_type):
                            source_path = source_folder.joinpath(file)
                            destination_path = destination_folder.joinpath(file)
                            shutil.copy(source_path, destination_path)
                else:
                    print("Please check if schedules path is correct")

                # copy configuration, generate_data, ... file from setup_data folder to building folders
                destination_folder = scenario_path
                num_zones = get_zone_number(scenario['Building_class'], scenario['Building_type'])
                if scenario['Building_class'] == 'residential':
                    source_folder = 'setup_data/residential'
                    for file_name in os.listdir(source_folder):
                        # construct full file path
                        source = source_folder +'/'+ file_name
                        destination = destination_folder.joinpath(file_name)
                        # copy only files
                        if os.path.isfile(source):
                            shutil.copy(source, destination)
                            print('copied', file_name)

                elif scenario['Building_class'] == 'non_residential':
                    if scenario['Building_type'] == 'office':
                        source_folder = 'setup_data/template'
                    elif scenario['Building_type'] == 'school':
                        source_folder = 'setup_data/template'
                    elif scenario['Building_type'] == 'hotel':
                        source_folder = 'setup_data/template'
                    else:
                        print("No valid building type")
                    for file_name in os.listdir(source_folder):
                        # construct full file path
                        source = source_folder +'/'+ file_name
                        destination = destination_folder.joinpath(file_name)
                        # copy only files
                        if os.path.isfile(source):
                            shutil.copy(source, destination)
                            print('copied', file_name)
                else:
                    print("No valid building class")

                # saves FMU-name and number of zones in csv file
                for fmu_name in os.listdir(scenario_path.joinpath('stored_data','FMUs')):
                    if fmu_name.endswith('.fmu'):
                        file_name = fmu_name

                data = [['fmu_name', file_name],
                        ['num_zones', str(num_zones)]]
                df_temp = pd.DataFrame(data, columns=['Name', 'Value'])
                def flatten_cell(cell):
                    if isinstance(cell, list):
                        return ','.join(cell)
                    else:
                        return cell
                df_temp = df_temp.applymap(flatten_cell)
                df_temp.to_csv(scenario_path.joinpath('parameter.csv'), sep=';')