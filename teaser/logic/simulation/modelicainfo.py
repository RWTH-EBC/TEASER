# created November 2015
# by TEASER4 Development Team


class ModelicaInfo():
    """ModelicaInfo Class

    This class holds information specific for Modelica Simulation.


    Attributes
    ----------

    runtime_simulation : str [s]
        Total duration of simulation, default 31536000 for one year
    interval_output : str [s]
        Interval for one time step, default 3600 for one hour
    solver : list
        list of available solvers for Modelica, default ["Lsodar", "dassl",
        "Radau"]
    current_solver : str
        solver that should be used in simulation, default 'dassl'
    equidistant_output : bool
        Use of Equidistant time grid flag in Modelica.
    variables_at_events : bool
        Use of events flag in Modelica.
    """
    def __init__(self):
        """Constructor of Simulation Class.
        """

        # Base-Values for the simulation tab
        self.runtime_simulation = "31536000"
        self.interval_output = "3600"
        self.solver = ["Lsodar", "dassl","Radau"]
        self.current_solver = "Radau"
        self.equidistant_output = True
        self.results_at_events = False
