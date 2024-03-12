from configuration import *

predictors = []
Objectives = []
constraints = []

for zone in range(num_zones):

    predictors.append(load_LinearRegression('T_AirRoom_linreg_'+str(zone)))

    Objectives.append(Objective(feature=T_AirRoom[zone], cost=Quadratic(weight=2, norm=1 / 10)))
    Objectives.append(Objective(feature=T_SetHeat[zone], cost=AbsoluteLinear(weight=0.1)))
    Objectives.append(Objective(feature=T_SetHeat_change[zone], cost=Quadratic(weight=0.1)))

    constraints.append(Constraint(feature=T_SetHeat[zone], lb=273.15 + 10, ub=273.15 + 30))

nlp = NLP(
    model=model,
    N=4 * 4,    # 4 h prediction horizon
    objectives=Objectives,
    constraints=constraints,
)


ThermalZone_MPC = ModelPredictive(
        step_size=one_minute * 15,
        nlp=nlp,
        forecast_callback=system.get_forecast,
        solution_plotter=mpc_plotter,
        show_solution_plot=False,
        save_solution_plot=False
    )

dh = DataHandler()
system.setup(start_time=0)
system.run(duration=24*one_hour, controllers=[]) # warm run to generate values for MPC

#Training with online data
for repetition in range(6):

    ThermalZone_MPC.nlp.build(solver_options={'verbose': False, 'ipopt.print_level': 0}, predictors=predictors)

    online_data = system.run(duration=one_day, controllers=[ThermalZone_MPC])

    dh.add(online_data)

    for zone in range(num_zones):
        T_AirRoom_TrainingData[zone].add(online_data)
        T_AirRoom_TrainingData[zone].split(1, 0, 0)
        T_AirRoom_TrainingData[zone].shuffle()
        predictors[zone].fit(training_data=T_AirRoom_TrainingData[zone])
        predictors[zone].test(training_data=T_AirRoom_TrainingData[zone])


ThermalZone_MPC.nlp.build(solver_options={'verbose': False, 'ipopt.print_level': 0}, predictors=predictors)
online_data = system.run(duration=360*one_day, controllers=[ThermalZone_MPC])
dh.add(online_data)

dh.save(filename='mpc_data',override=True)

#system.setup(start_time=0)
#system.run(duration=12*one_hour, controllers=[]) # warm run to generate first values
#dc = system.run(duration=one_week, controllers=[ThermalZone_MPC])


