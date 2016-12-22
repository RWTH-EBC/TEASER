.. teaser documentation master file, created by
   sphinx-quickstart on Thu Sep 10 10:48:49 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

teaser
==================================

TEASER (Tool for Energy Analysis and Simulation for Efficient Retrofit)
allows the creation of archetype buildings as well as the
representation of existing buildings and the calculation of simulation
parameters for reduced oder models. It is being developed at the `RWTH Aachen
University, E.ON Energy Research Center, Institute for Energy Efficient
Buildings and Indoor Climate,
<https://www.ebc.eonerc.rwth-aachen.de/cms/~dmzz/E-ON-ERC-EBC/?lidx=1>`_.


This software is work-in-progress. Documentation will be incomplete or missing
and the software may not run properly. In particular the Grahpical User
Interface is a beta release and not fully tested. If you find any bugs, please
report them (see `How to contribute to TEASER`_)

If you have any questions regarding TEASER feel free to contact us at
`ebc-teaser@eonerc.rwth-aachen.de <ebc-teaser@eonerc.rwth-aachen.de>`_.


License
==================

TEASER is released by RWTH Aachen University, E.ON Energy Research Center,
Institute for Energy Efficient Buildings and Indoor Climate, under the
`MIT License <https://github.com/RWTH-EBC/TEASER/blob/master/License.md>`_.

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
models for `AixLib <https://github.com/RWTH-EBC/AixLib>`_ and
IEA-EBC `Annex60 <https://github.com/iea-annex60/modelica-annex60>`_.

Version
==================

The current version is 0.4.4, which is a pre-release.

How to cite TEASER
==================

A Journal Paper presenting TEASER is already submitted an is in review.

How to contribute to TEASER
==================

You are invited to contribute to the development of TEASER. You may report any
issues by using the `Issues <https://github.com/RWTH-EBC/TEASER/issues>`_ button.
Furthermore, you are welcome to contribute via Pull
`Requests <https://github.com/RWTH-EBC/TEASER/pulls>`_. The workflow for changes is
described in our `Wiki <https://github.com/RWTH-EBC/TEASER/wiki>`_.

Contents
==================

.. toctree::
   :maxdepth: 1

   install_teaser
   teaser.Examples
   teaser

People
==================
The following people have directly contributed to the implementation of
TEASER:

   - Michael Mans
   - Moritz Lauster
   - Marcus Fuchs
   - Yasin Goerguelue
   - Christoph Gingter
   - Peter Remmen

 Special thanks goes to Gregor Hillebrand, who created the basis of TEASER (Retrofit Matrix).

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
