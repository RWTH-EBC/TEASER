# created November 2015
# by TEASER4 Development Team

class Simulation():


    def __init__(self):
        '''Constructor of Simulation Class.

        '''
        
        # Base-Values for the simulation tab
        self.runtimeSimulation = "31536000"
        self.intervalOutput = "3600"
        self.solver = ["Lsodar", "dassl"]
        self.current_solver = "dassl"
        self.equidistant_output = True
        self.dymolaProject = "Campus.Juelich.Simulations.September3"
        self.avgTempOuter = "-12"
        self.innerTemp = "20"
        self.airchange_rate = ["airtight", "semi pervious to air",
                                           "pervious to air"]
        self.current_airchange_rate = "airtight"
        self.ahuFile = "./Tables/Melaten/AHU_Institut 4.mat"
        self.internalGainsFile = \
            "./Tables/Melaten/InternalGains_Institut 4.mat"
        self.tsetFile = "./Tables/Melaten/Tset_Institut 4.mat"
