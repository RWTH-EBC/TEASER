# created November 2015
# by TEASER4 Development Team


class ModelicaInfo:
    """ModelicaInfo Class

    This class holds information specific for Modelica Simulation. Some of
    these solver or flags might only be applicable to Dymola.


    Attributes
    ----------

    start_time : int [s]
        Start time for the simulation, default 0
    stop_time : int [s]
        Stop time for the simulation, default 31536000
    interval_output : str [s]
        Interval for one time step, default 3600 for one hour
    solver : list
        list of available solvers for Modelica
    current_solver : str
        solver that should be used in simulation, default 'Radau'
    equidistant_output : bool
        Use of Equidistant time grid flag in Modelica.
    variables_at_events : bool
        Use of events flag in Modelica.
    version : str
        Version of Modelica and Modelica Standard Library
    """

    def __init__(self):
        """Constructor of ModelicaInfo Class.
        """

        # Base-Values for the simulation tab
        self.start_time = 0
        self.stop_time = 31536000
        self.interval_output = "3600"
        self.solver = ["Lsodar", "dassl", "Radau", "Cvode"]
        self.current_solver = "Cvode"
        self.equidistant_output = True
        self.results_at_events = False
        self.version = "4.0.0"
