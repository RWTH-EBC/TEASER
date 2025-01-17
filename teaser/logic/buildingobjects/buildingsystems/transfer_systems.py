"""The here named transfer systems are simply using a PT 1 element to delay
the heat transfer into the zone. The PT 1 is modeled in the
AixLib.Utilities.Sources.HeaterCooler.HeaterCoolerPIFraRadDamped class in
Modelica."""
from enum import Enum, auto


class TransferSystems(Enum):
    """Enum for transfer systems.

    Ideal heater uses no PT 1, Radiator, UnderFloorHeating and
    ConcreteCoreActivation use different PT 1 parameters, that delay the heat
    transfer into the zone. The model parameters can be found in AixLib under:
    AixLib.Utilities.Sources.HeaterCooler.SimplifiedTransferSystems
    """
    IdealHeater = auto()
    Radiator = auto()
    UnderFloorHeating = auto()
    ConcreteCoreActivation = auto()
