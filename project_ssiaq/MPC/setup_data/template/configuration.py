import os
import sys
import re
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
parentdir2 = os.path.dirname(parentdir)
sys.path.append(parentdir2)
# Change working directory temporary
os.chdir(currentdir)
from ddmpc import *

#import csv file with config data
parameter_df = pd.read_csv('parameter.csv', sep =';')
num_zones = parameter_df['Value'][1]
num_zones = int(re.findall(r'\d+', num_zones)[0])
fmu_name = parameter_df['Value'][0]

# ---------------------------------------------- DISTURBANCES -----------------------------------------------

dry_bul = Disturbance(Readable(name='Außentemperatur', read_name='multizone.zone[1].weaBus.TDryBul',
                               plt_opts=PlotOptions(color=blue, line=line_solid, label='Außentemperatur')))
rad_inf = Disturbance(Readable(name='Horizontale globale Strahlung', read_name='multizone.zone[1].weaBus.HGloHor',
                               plt_opts=PlotOptions(color=light_red, line=line_solid, label='Strahlung')))

int_gain_human = Disturbance(Readable(name='Personen', read_name='multizone.zone[1].intGains[1]',
                                      plt_opts=PlotOptions(color=light_grey, line=line_solid,
                                                           label='Interne Gewinne (Personen)')))
int_gain_elect = Disturbance(Readable(name='El. Verbraucher', read_name='multizone.zone[1].intGains[2]',
                                      plt_opts=PlotOptions(color=grey, line=line_dashdot,
                                                           label='Interne Gewinne (El. Verbraucher)')))
int_gain_light = Disturbance(Readable(name='Licht', read_name='multizone.zone[1].intGains[3]',
                                      plt_opts=PlotOptions(color=dark_grey, line=line_dotted,
                                                           label='Interne Gewinne (Licht)')))

# ---------------------------------------------- FEATURES -----------------------------------------------

schedule_path = []
T_AirRoom = []
T_AirRoom_change = []
T_SetHeat = []
T_SetHeat_change = []
T_AirRoom_TrainingData = []
P_Heater = []
P_Heater_sum = []

for zone in range(num_zones):

    schedule_path.append("stored_data/schedules/schedules_"+str(zone)+".pkl")

    T_AirRoom.append(Controlled(
        variable=Readable(
            name='Zone Temperature '+str(zone+1),
            read_name='TAirOutput['+str(zone+1)+']',
            plt_opts=blue_line,
        ),
        mode=Economic_Presence(schedule_path=schedule_path[zone])))

    T_AirRoom_change.append(Connection(Change(base=T_AirRoom[zone])))

    T_SetHeat.append(Control(
        variable=Readable(
            name='Set Temperature '+str(zone+1),
            read_name='TSetHeatInput['+str(zone+1)+']',
            plt_opts=red_line,
        ),
        lb=273.15 + 0,
        ub=273.15 + 40,
        default=273.15 + 22))

    T_SetHeat_change.append(Connection(Change(base=T_SetHeat[zone])))

    P_Heater.append(Tracking(
        variable=Readable(
            name='Energy demand '+str(zone+1),
            read_name='multizone.PHeater['+str(zone+1)+']',
            plt_opts=black_line,
        )))

    T_AirRoom_TrainingData.append(TrainingData(
        inputs=Inputs(
            Input(T_AirRoom[zone], lag=1),
            Input(dry_bul, lag=2),
            Input(rad_inf, lag=1),
            Input(T_SetHeat[zone], lag=4)
        ),
        output=Output(variable=T_AirRoom_change[zone]),
        step_size=60 * 15,
    ))

P_Heater_sum = Tracking(
        variable=Sum(
            name ='Energy sum '+str(zone+1),
            bases=P_Heater[:],
            plt_opts=PlotOptions(fmt.black, fmt.line_solid)
        ))
# ---------------------------------------------- MODEL-FMU-PLOT -----------------------------------------------

model = Model(*Feature.all)
system = FMU(model=model, step_size=60 * 15, name=fmu_name)

pid_plotter = Plotter(
    SubPlot(features=T_AirRoom[:], y_label='Air Temperature', shift=273.15, legend=True),
    SubPlot(
        features=T_SetHeat[:],
        y_label='SetPoints',
        shift=273.15,
        lb=14,
        ub=26,
        step=True,
        legend=True,
    ),
)

mpc_plotter = Plotter(
    SubPlot(features=T_AirRoom[:], y_label='Air Temperature', shift=273.15, legend=True),
    SubPlot(
        features=T_SetHeat[:],
        y_label='SetPoint',
        shift=273.15,
        lb=14,
        ub=26,
        step=True,
        legend=True,
    ),
    SubPlot(features=[dry_bul, rad_inf], y_label='Dist.', normalize=True),
)

result_plotter = Plotter(
    SubPlot(features=T_AirRoom[:], y_label='Air Temperature', shift=273.15, legend=True),
    SubPlot(
        features=T_SetHeat[:],
        y_label='SetPoint',
        shift=273.15,
        lb=14,
        ub=26,
        step=True,
        legend=True,
    ),
    SubPlot(features=P_Heater[:], y_label='Heater Power'),
    SubPlot(features=[P_Heater_sum], y_label='Heater Power cumulative'),
    SubPlot(features=[dry_bul, rad_inf], y_label='Dist.', normalize=True))



