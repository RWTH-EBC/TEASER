# created November 2015
# by TEASER4 Development Team


class ModelicaInfo():

    def __init__(self):
        '''Constructor of Simulation Class.

        '''

        # Base-Values for the simulation tab
        self.runtime_simulation = "31536000"
        self.interval_output = "3600"
        self.solver = ["Lsodar", "dassl"]
        self.current_solver = "dassl"
        self.equidistant_output = True
