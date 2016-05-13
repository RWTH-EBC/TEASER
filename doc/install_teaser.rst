How to install TEASER
==================

Installation
-------------------------
The best option to install TEASER is to clone the repository by using:

`git clone [SSH-Key/Https]`

and then run:

`pip install -e [Path/to/your/Teaser/Clone]`

using  pip(https://pip.pypa.io/en/latest/).

Deinstallation
-------------------------
The best option is not to uninstall TEASER :-). However, if you want to
uninstall it, just use:

`pip uninstall teaser`


Dependencies
-------------------------
TEASER requires some specific Python packages and versions.

1. Python 2.7 <= v >=3.3 - WinPython 3.4 is recommended (comes along with a lot
   of Python packages, including PyQt, which is needed for the GUI).
2. Mako: template Engine
   install on a python-enabled command line with `pip install mako`
3. PyXB: XML binding Engine
   install on a python-enabled command line with `pip install pyxb`
4. pytest: Unit Tests engine
   install on a python-enabled command line with `pip install pytest`
