teaser package structure
==================

The following docs will guide you through the structure of the Python package
TEASER. This will help to understand the functionality in order to integrate
TEASER in your workflow.

teaser content
-------------------------
TEASER provides modules, classes and functions to collect data, execute
calculations for reduced order models and generate ready-to-run code for
Modelica libraries AixLib and Annex 60.
The package itself is subdivided into the following
four packages:

.. toctree::
  :maxdepth: 2

  teaser.Data

.. toctree::
  :maxdepth: 2

  teaser.Examples

.. toctree::
    :maxdepth: 2

    teaser.Logic

.. toctree::
    :maxdepth: 2

    teaser.GUI


In TEASERS root package there are two additional Python modules:

.. toctree::
    :maxdepth: 2

    teaser.Project
    teaser.GuiStart


Future Developments
-------------------------

TEASER is still under development, future implementations will include extended
CityGML support and improvement of the graphical user interface.
