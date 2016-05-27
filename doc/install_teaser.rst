How to install TEASER
==================

Installation
-------------------------
The best option to install TEASER is to use pip::

	pip install teaser

If you actively want to develop TEASER you can clone the repository by using::

	git clone [SSH-Key/Https]

and then run::

	pip install -e [Path/to/your/Teaser/Clone]

which will install the local version of TEASER.

You need to have pip installed (see dependencies).

Deinstallation
-------------------------
The best option is not to uninstall TEASER at all:-). However, if you want to
uninstall it, just use::

 pip uninstall teaser


Dependencies
-------------------------
TEASER uses Python 2.7 <= v >=3.3. Further using a WinPython distribution is
recommended (https://winpython.github.io/). WinPython comes along with a lot of
Python packages (e.g. SciPy, NumPy, pip, PyQT, etc.) that are used in the
TEASER code.

In addition, TEASER requires some specific Python packages:

1. Mako: template Engine
   install on a python-enabled command line with `pip install -U mako`
2. PyXB: XML binding Engine
   install on a python-enabled command line with `pip install -U pyxb`
3. pytest: Unit Tests engine
   install on a python-enabled command line with `pip install -U pytest`
