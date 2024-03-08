from configuration import *

for zone in range(num_zones):
    pid_data = load_DataHandler('pid_data')
    T_AirRoom_TrainingData[zone].add(pid_data)
    lin_reg = LinearRegression()
    T_AirRoom_TrainingData[zone].split(trainShare=1.0, validShare=0.0, testShare=0.0)
    lin_reg.fit(training_data=T_AirRoom_TrainingData[zone])
    lin_reg.print_coefficients()

    lin_reg.test(training_data=T_AirRoom_TrainingData[zone], show_plot=True, save_plot=True)
    lin_reg.save('T_AirRoom_linreg_'+str(zone), override=True)


