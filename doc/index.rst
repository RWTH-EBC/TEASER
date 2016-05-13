.. teaser documentation master file, created by
   sphinx-quickstart on Thu Sep 10 10:48:49 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

TEASER - Tool for Energy Analysis and Simulation for Efficient Retrofit
==================================

The TEASER tool allows the creation of archetpye buidlings as well as the
representation of existing buildings and the calculation of simulation
parameters for reduced oder models. It is being developed at the E.ON Energy
Research center, Institute for Energy Efficient Buildings and Indoor Climate,
RWTH Aachen University.

If you have any questions regarding TEASER feel free to contact us at
teaser@eonerc.rwth-aachen.de.

Warning:
This software is work-in-progress. Documentation will be incomplete or missing
and the software may not run properly.

License
==================

TEASER is released by E.ON Energy Research center, Institute for Energy
Efficient Buildings and Indoor Climate, RWTH Aachen University under the
MIT License(http://opensource.org/licenses/MIT).

Acknowledgements
==================

Parts of TEASER have been developed within public funded projects and with
financial support by BMWi (German Federal Ministry for Economic Affairs and
Energy).

Description
==================

Energy supply of buildings in urban context currently undergoes significant
changes. The increase of renewable energy sources for electrical and thermal
energy generation will require flexible and secure energy storage and
distribution systems. To reflect and consider these changes in energy systems
and buildings, dynamic simulation is one key element, in particular when it
comes to thermal energy demand on minutely or hourly scale.
Sparse and limited access to detailed building information as well as computing
times are challenges for building simulation on urban scale. In addition,
data acquisition and modelling for Building Performance Simulation (BPS) are
time consuming and error-prone. To enable the use of BPS on urban scale we
present the TEASER tool, an open framework for urban energy modelling of
building stocks. TEASER provides an easy interface for multiple data sources,
data enrichment, where necessary and export of ready-to-run Modelica simulation
models for AixLib(https://github.com/RWTH-EBC/AixLib) and
IEA-EBC Annex60(https://github.com/iea-annex60/modelica-annex60).

Version
==================

The current version is 0.2.8, which is a pre-release.


How to contribute to TEASER
==================

You are invited to contribute to the development of TEASER. You may report any
issues by using the Issues(https://github.com/RWTH-EBC/TEASER/issues) button.
Furthermore, you are welcome to contribute via Pull
Requests(https://github.com/RWTH-EBC/TEASER/pulls). The workflow for changes is
described in our Wiki(https://github.com/RWTH-EBC/TEASER/wiki).


Contents:
==================

.. toctree::
   :maxdepth: 1

   install_teaser
   teaser_start
   teaser


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
