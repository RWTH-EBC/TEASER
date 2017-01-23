Install TEASER
===============

The best option to install TEASER is to use pip::

		pip install teaser

If you actively develop TEASER you can clone this repository by using::

	git clone [SSH-Key/Https]

and then run::

		pip install -e [Path/to/your/Teaser/Clone]

which will install the local version of TEASER.


TEASER uses Python 2.7 <= v >=3.3. Further using a Python distribution is
recommended as they already contain (or easily support installation of) many
Python packages (e.g. SciPy, NumPy, pip, PyQT, etc.) that are used in the
TEASER code. Two examples of those distributions are:

	- https://winpython.github.io/ WinPython comes along with a lot of Python packages (e.g. SciPy, NumPy, pip, PyQT, etc.).

	- http://conda.pydata.org/miniconda.html Conda is an open source package management  system and environment management system for installing multiple versions of software  packages and their dependencies and switching easily between them.

In addition, TEASER requires some specific Python packages:

1. Mako: template Engine::

		pip install-U mako

2. PyXB: XML binding Engine::

		pip install -U pyxb

3. pytest: Unit Tests engine::

		pip install -U pytest
