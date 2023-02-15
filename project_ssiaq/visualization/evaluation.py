from pathlib import Path
from ebcpy import TimeSeriesData
import datetime
import matplotlib.pyplot as plt


def import_and_process(path):
    tsd = TimeSeriesData(path)
    tsd.to_datetime_index(origin=datetime.datetime(2022, 1, 1, 0, 0, 0))
    return tsd

def plot_T_Air(tsd, building_type,zone_map):
    plt.figure()
    color_map = ['blue', 'red', 'green', 'orange', 'pink', 'black']

    for idx, zone in enumerate(zone_map[building_type]):
        plot_param = "multizone.TAir[" + str(idx + 1) + "]"
        label = "T_air - " + str(zone)
        plt.plot(tsd.loc[:, (plot_param, "raw")]-273.15, label=label, color=color_map[idx])

    plt.xlabel('Time')
    plt.ylabel('Air temperature in °C')
    plt.legend()
    plt.show()


def plot_Q_flow(tsd, building_type,zone_map):
    plt.figure()
    color_map = ['blue', 'red', 'green', 'orange', 'pink', 'black']

    for idx, zone in enumerate(zone_map[building_type]):
        plot_param_1 = "multizone.PHeater[" + str(idx + 1) + "]"
        plot_param_2 = "multizone.PCooler[" + str(idx + 1) + "]"
        label_1 = "P_Heater - " + str(zone)
        label_2 = "P_Cooler - " + str(zone)
        plt.plot(tsd.loc[:, (plot_param_1, "raw")], label=label_1, color=color_map[idx])
        plt.plot(tsd.loc[:, (plot_param_2, "raw")], label=label_2, color=color_map[idx])

    plt.xlabel('Time')
    plt.ylabel('Power in W')
    plt.legend()
    plt.show()


def get_bldg_type_from_filename(filename):
    building_types = ['single_family_house', 'multi_family_house', 'terraced_house', 'apartment_block', 'office',
                      'school', 'hotel']
    for i in building_types:
        if i in path_in_str:
            building_type = i
            break
    return building_type


if __name__ == '__main__':
    setup_name = "20220209_test_setup"
    basepath = Path('N:/Forschung/EBC0741_ZIM_SmartSenseIAQ_NK/Data/Simulationen/Referenzszenarien').joinpath(
        setup_name, "sim_results")
    # find all result files in given setup folder
    pathlist = Path(basepath).rglob('*.mat')

    # TODO: Configure zone map
    zone_map = dict(office=['Office', 'Floor', 'Storage', 'Meeting', 'Restroom', 'ICT'],
                    school=['Office', 'Floor', 'Storage', 'Meeting', 'Restroom', 'ICT'],
                    hotel=['Office', 'Floor', 'Storage', 'Meeting', 'Restroom', 'ICT'],
                    single_family_house=['Single zone'], multi_family_house=['Single zone'],
                    terraced_house=['Single zone'], apartment_block=['Single zone'])

    for path in pathlist:
        path_in_str = str(path)
        building_type = get_bldg_type_from_filename(path_in_str)
        tsd = import_and_process(path_in_str)
        plot_T_Air(tsd, building_type,zone_map)
        plot_Q_flow(tsd, building_type,zone_map)
