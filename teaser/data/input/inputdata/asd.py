from teaser.data.dataclass import DataClass
from teaser.logic.buildingobjects.boundaryconditions.boundaryconditions \
    import BoundaryConditions
import teaser.logic.utilities as utilities
import teaser.data.bindings.v_0_6.boundaryconditions_bind as uc_bind
import pyxb

dataclass_new = DataClass()
dataclass_new.path_uc = "D:\\TEST1.xml"
dataclass_new.load_uc_binding()
dataclass_old = DataClass()

for test in dataclass_old.conditions_bind.BoundaryConditions:
    bc = BoundaryConditions()
    bc.load_use_conditions(test.usage,dataclass_old)
    bc.save_use_conditions(dataclass_new)

"""

pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(
        uc_bind.Namespace, 'usecond')
out_file = open(utilities.get_full_path(dataclass_old.path_uc), 'w')

out_file.write(dataclass_old.conditions_bind.toDOM().toprettyxml())
"""