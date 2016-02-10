TEASER Doc
==================

Installation
-------------------------
The best option to install TEASER is to clone the repository by using:

`git clone [SSH-Key/Https]`

and then run:

`pip install -e [Path/to/your/Teaser/Clone]`


Dependencies
-------------------------
1. Python 2.7 <= v >=3.3 - WinPython is recommended (includes a lot of packages).
2. Mako: template Engine
   install on a python-enabled command line with `pip install mako`
3. PyXB: XML binding Engine
   install on a python-enabled command line with `pip install pyxb`
4. pytest: Unit Tests engine
   install on a python-enabled command line with `pip install pytest`
   
TEASER Content
-------------------------
The source folder contains different subpackages and one Project module

Project module
`````````````
TEASER API

Data package 
`````````````
This package contains interfaces to different data sources (right now only internal data format is supported) as well as PyXB Data Bindings for XML based data.
    
Examples package 
`````````````
This package contains some examples how to use TEASER in a script based manner, as well as some verification of the calculation core
    
InputData Folder 
`````````````
This folder contains predefined data for typical building elements, different materials, use conditions following DIN 18599 as well as templates for Modelica Records and Boundary condition for the type buildings.	
    
Logic package 
`````````````
This package contains all classes of the internal data model of TEASER, as well as the archetype buildings and parameter calculation.


.. toctree::
	teaser.Project
	teaser.Examples
	teaser.Logic
	teaser.Data
	teaser.InputData
		

Future Developments
-------------------------

- Data interfaces to information models like CityGML.
- Graphical User Interface


	