from configuration import *

Zone_PID = []
for zone in range(num_zones):

    T_AirRoom[zone].mode = Identification()
    # PID controller
    Zone_PID.append(PID(
        y=T_AirRoom[zone],
        u=T_SetHeat[zone],
        step_size=60 * 15,
        Kp=1,
        Ti=600,
        Td=0
    ))

system.setup(start_time=one_week)
dh = DataHandler(
    system.run(controllers=(Zone_PID), duration=7 * one_day),
)

for dc in dh:
    filepath = file_manager.plot_filepath(name='ZonePID', sub_folder='PID', include_time=True)
    pid_plotter.plot(df=dc.df, save_plot=True, filepath=filepath)

dh.save(filename='pid_data', override=True)
