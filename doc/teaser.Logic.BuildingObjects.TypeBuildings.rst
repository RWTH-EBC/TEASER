TypeBuildings package
==================================================

**Description**

The TEASER4 typebuilding package contains different modules for the creation 
and parametrisation of typebuildings. In general these typebuildings are use to 
create usable dataset of buildings out of limited building information. For 
this, the methods are based on the following principles according to Lichtmess 
(fixme):

#. The building envelopes are based on the building net floor area (net leased area in the following)

#. The building envelopes can automatically assigned to the thermal zones

In addition (fixme) it is necessary to use statistic data for the following Points:

* number of thermal zones

* division of the net leased area into the zone area

* wall constructions

* properties of the used construction materials

The exact number of zones and their zone area are show in the description of 
each typebuilding. The building envelopes are based on the BMVBS where 
different administrative buildings were investigated. 
The typebuildings themselfes are divided 
into different classes according to the BWZK (fixme)

Office module
--------------------------------------------------------

**Description**

The office module contains a multi zone building according to the BMVBS 2010 
(fixme). In detail the net leased area is divided in the following thermal zone 
areas:

#. Office (50% of net leased area)

#. Floor (25% of net leased area)

#. Storage (15% of net leased area)

#. Meeting (4% of net leased area)

#. Restroom (4% of net leased area)

#. ICT (2% of net leased area)

.. automodule:: teaser.Logic.BuildingObjects.TypeBuildings.Office
    :members:
    :undoc-members:
    :show-inheritance:

Residential module
-------------------------------------------------------------

**Description**

The residential module contains a single zone building according to the BMVBS 
2010. In detail the net leased area is divided in the following thermal zone 
area:

#. Single dwelling (100% of net leased area)

.. automodule:: teaser.Logic.BuildingObjects.TypeBuildings.Residential
    :members:
    :undoc-members:
    :show-inheritance:
	
Institute module
-----------------------------------------------------------

**Description**

The institute module contains a multi zone building according to the data from
(fixme Jülich?). In detail the net leased area is divided in the following 
thermal zone areas:

#. Office (40% of net leased area)

#. Floor (25% of net leased area)

#. Storage (10% of net leased area)

#. Meeting (4% of net leased area)

#. Restroom (4% of net leased area)

#. ICT (2% of net leased area)

#. Laboratory (15% of the net leased area)

.. automodule:: teaser.Logic.BuildingObjects.TypeBuildings.Institute
    :members:
    :undoc-members:
    :show-inheritance:

Institute4 module
------------------------------------------------------------

**Description**

The institute type 4 module contains a multi zone building according to the data from
(fixme Jülich?). In detail the net leased area is divided in the following 
thermal zone areas:

#. Office (37.5% of net leased area)

#. Floor (22.5% of net leased area)

#. Storage (10% of net leased area)

#. Meeting (4% of net leased area)

#. Restroom (4% of net leased area)

#. ICT (2% of net leased area)

#. Laboratory (20% of the net leased area)

.. automodule:: teaser.Logic.BuildingObjects.TypeBuildings.Institute4
    :members:
    :undoc-members:
    :show-inheritance:

Institute8 module
------------------------------------------------------------

**Description**

The institute type 8 module contains a multi zone building according to the data from
(fixme Jülich?). In detail the net leased area is divided in the following 
thermal zone areas:

#. Office (10% of net leased area)

#. Floor (18% of net leased area)

#. Storage (2% of net leased area)

#. Meeting (4% of net leased area)

#. Restroom (4% of net leased area)

#. ICT (2% of net leased area)

#. Laboratory (60% of the net leased area)

.. automodule:: teaser.Logic.BuildingObjects.TypeBuildings.Institute8
    :members:
    :undoc-members:
    :show-inheritance:


TypeBuilding module
--------------------------------------------------------------

.. automodule:: teaser.Logic.BuildingObjects.TypeBuildings.TypeBuilding
    :members:
    :undoc-members:
    :show-inheritance:

UseConditionsOffice18599 module
--------------------------------------------------------------------------

**Description**

The UseConditionsOffice18599 module contains the useconditions for the 
typebuildings according to the DIN V 18599 (fixme) and the SIA 2024 (fixme). 
In detail the attributes are structured in the following sections:

* Usage and operation times

* Lighting

* Room climate

* Internal gains

* Misc


.. automodule:: teaser.Logic.BuildingObjects.TypeBuildings.UseConditionsOffice18599
    :members:
    :undoc-members:
    :show-inheritance:


