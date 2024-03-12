from pathlib import Path
from ebcpy import TimeSeriesData, preprocessing
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pathlib
import os
from scipy import integrate
import pickle

def import_and_process(path):
    tsd = TimeSeriesData(path)
    tsd.to_datetime_index(origin=datetime.datetime(2022, 1, 1, 0, 0, 0))
    return tsd

def calculate_heat_demand(tsd, num_zones):
    tsd = preprocessing.convert_datetime_index_to_float_index(tsd)
    heat_demand_zonal = list()
    for zone in range(num_zones):
       heat_demand_zonal.append(integrate.trapezoid(tsd["multizone.PHeater["+str(zone+1)+"]", "raw"], tsd.index.to_series())/3600/1000) # in kWh
    total_heat_demand = sum(heat_demand_zonal)
    return heat_demand_zonal, total_heat_demand
def get_bldg_type_from_filename(filename):
    building_types = ['single_family_house', 'multi_family_house', 'terraced_house', 'apartment_block', 'office',
                      'school', 'hotel']
    for i in building_types:
        if i in filename:
            building_type = i
            scenario = pathlib.Path(filename).parts[-2].split('_')[0]
            break
    return building_type, scenario

if __name__ == '__main__':
    setup_name = "20230803_ddc_rand"
    basepath = Path(r'R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten\02_Bedarfsorientierte_Regelung').joinpath(
        setup_name, "sim_results")
    """
    setup_name = "20230802_referenz_rand"
    basepath = Path(r'R:\EBC0741_ZIM_SmartSenseIAQ_NK\Assistenten\SimDaten\01_Referenzszenarien').joinpath(
        setup_name, "sim_results")
    """
    # find all result files in given setup folder

    pathlist = Path(basepath).rglob('*.mat')
    # TODO: Configure zone map
    zone_map = dict(office=['Office', 'Floor', 'Storage', 'Meeting', 'Restroom', 'ICT'],
                    school=['Classrooms', 'Floor', 'Storage', 'Office', 'Restroom', 'Further common rooms','Canteen',
                            'Auditorium'],
                    hotel=['Hotelrooms', 'Floor', 'Storage', 'Meeting', 'Office', 'Restaurant','Kitchen', 'Auxiliary',
                           'Restroom', 'Sauna'],
                    single_family_house=['Single zone'], multi_family_house=['Single zone'],
                    terraced_house=['Single zone'], apartment_block=['Single zone'])

    for path in pathlist:

        filename = str(path.parts[-2])
        print("Reading:", filename)
        if os.path.exists(path.parent.joinpath('heat_demand.pkl')):
            print("File has already been processed")
            continue
        building_type, scenario = get_bldg_type_from_filename(str(path))
        tsd = import_and_process(path)
        num_zones = len(zone_map[building_type])
        heat_zonal, heat_total = calculate_heat_demand(tsd, num_zones)

        with open(path.parent.joinpath('heat_demand.pkl'),'wb') as f:
            pickle.dump([heat_zonal, heat_total], f)


