"""
Created August 2019

@author: TEASER Development Team
"""

from teaser.project import Project


prj = Project(True)


class Simulation_export(object):
    """Unit Tests for TEASER"""

    global prj

    def export_e2_example_export_aixlib(self):
        """Tests the executability of example 2"""
        from teaser.examples import e2_export_aixlib_models as e2

        prj = e2.example_export_aixlib()
