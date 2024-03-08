from pathlib import Path
from ebcpy import TimeSeriesData
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pathlib
import os

def import_and_process(path):
    tsd = TimeSeriesData(path)
    tsd.to_datetime_index(origin=datetime.datetime(2022, 1, 1, 0, 0, 0))
    return tsd

def plot_T_Air(tsd, building_type, scenario, zone_map,color_map,save_flag=False):
    plt.figure(dpi=300)

    #start_dt = datetime.datetime.strptime("01/02/22 00:00:00",'%m/%d/%y %H:%M:%S')
    for idx, zone in enumerate(zone_map[building_type]):
        plot_param = "multizone.TAir[" + str(idx + 1) + "]"
        label = "T_air - " + str(zone)
        plt.plot(tsd.loc[:, (plot_param, "raw")]-273.15, label=label, color=color_map[idx])

    plt.xlabel('Time')
    plt.ylabel('Air temperature in °C')
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    #plt.show()
    if save_flag:
        plt.savefig("T_Air"+scenario+".png",bbox_inches="tight")
    plt.close()

def plot_Q_flow(tsd, building_type, scenario, zone_map,color_map,save_flag=False):
    plt.figure(dpi=300)

    #start_dt = datetime.datetime.strptime("01/02/22 00:00:00",'%m/%d/%y %H:%M:%S')
    for idx, zone in enumerate(zone_map[building_type]):
        plot_param_1 = "multizone.PHeater[" + str(idx + 1) + "]"
        plot_param_2 = "multizone.PCooler[" + str(idx + 1) + "]"
        label_1 = "P_Heater - " + str(zone)
        label_2 = "P_Cooler - " + str(zone)
        plt.plot(tsd.loc[:, (plot_param_1, "raw")], label=label_1, color=color_map[idx])
        #plt.plot(-tsd.loc[:, (plot_param_2, "raw")], label=label_2, color=color_map[idx])

    plt.xlabel('Time')
    plt.ylabel('Power in W')
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    #plt.show()
    if save_flag:
        plt.savefig("Q_flow" + scenario + ".png",bbox_inches="tight")
    plt.close()


def plot_presence(tsd, building_type, scenario, zone_map, color_map,save_flag=False):
    plt.figure(dpi=300)

    # start_dt = datetime.datetime.strptime("01/02/22 00:00:00",'%m/%d/%y %H:%M:%S')
    for idx, zone in enumerate(zone_map[building_type]):
        plot_param = "multizone.intGains[" + str(idx + 1) + "]"
        label = "specific people - " + str(zone)
        plt.plot(tsd.loc[:, (plot_param, "raw")], label=label, color=color_map[idx])
    plt.xlim(datetime.datetime(2022, 1, 1, 0, 0, 0),datetime.datetime(2022, 1, 7, 0, 0, 0))
    plt.xlabel('Time')
    plt.ylabel('Specific People')
    plt.legend(bbox_to_anchor=(1.04, 1), loc="upper left")
    #plt.show()
    if save_flag:
        plt.savefig("Specific_People_" + scenario + ".png", bbox_inches="tight")
    print("Figure saved")
    plt.close()

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
    setup_name = "20230428_bedarfsorientiert_nwg"
    basepath = Path('N:/Forschung/EBC0741_ZIM_SmartSenseIAQ_NK/Data/Simulationen/02_Bedarfsorierntierte_Regelung').joinpath(
        setup_name, "sim_results")
    # find all result files in given setup folder

    pathlist = Path(basepath).rglob('*.mat')
    #pathlist = Path("N:\Forschung\EBC0741_ZIM_SmartSenseIAQ_NK\Data\Simulationen/01_Referenzszenarien/20230307_referenz_komplett\sim_results\S157_school").rglob('*.mat')
    # TODO: Configure zone map
    zone_map = dict(office=['Office', 'Floor', 'Storage', 'Meeting', 'Restroom', 'ICT'],
                    school=['Classrooms', 'Floor', 'Storage', 'Office', 'Restroom', 'Further common rooms','Canteen',
                            'Auditorium'],
                    hotel=['Hotelrooms', 'Floor', 'Storage', 'Meeting', 'Office', 'Restaurant','Kitchen', 'Auxiliary',
                           'Restroom', 'Sauna'],
                    single_family_house=['Single zone'], multi_family_house=['Single zone'],
                    terraced_house=['Single zone'], apartment_block=['Single zone'])
    cmap = plt.get_cmap('plasma')

    for path in pathlist:
        path_in_str = str(path)
        building_type, scenario = get_bldg_type_from_filename(path_in_str)
        tsd = import_and_process(path_in_str)
        slicedCM = cmap(np.linspace(0, 1, len(zone_map[building_type])))
        os.chdir(path.parents[0])
        #plot_T_Air(tsd, building_type, scenario, zone_map,slicedCM,save_flag=True)
        #plot_Q_flow(tsd, building_type, scenario, zone_map,slicedCM,save_flag=True)
        plot_presence(tsd, building_type, scenario, zone_map,slicedCM,save_flag=True)
