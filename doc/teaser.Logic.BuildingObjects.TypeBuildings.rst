TypeBuildings package
==================================================

**Description**

The TEASER4 typebuilding package contains different modules for the creation 
and parametrisation of typebuildings. In TEASER4 these typebuildings are used to 
create usable dataset of buildings out of limited building information. For 
this, the methods are based on the following principles according to Lichtmess 
:cite:`Lichtme.2010`:

#. The building envelopes are based on the building net floor area (net leased area in the following)

#. The building envelopes can automatically assigned to the thermal zones

These principles are mainly used to handle the building envelopes of typebuildings. 
In addition it is necessary to use statistic data for the following Points:

* number of thermal zones

* division of the net leased area into the zone area

* wall constructions

* properties of the used construction materials

With the help of this statistic data above it is possible to create 
the typebuildings with the use of only five parameters:

* type of building

* net leased area

* year of construction

* number of floors

* height of floors

The exact number of zones and their zone area are show in the description of 
each typebuilding. The connection between the building envelope area and the 
building net leased area are based on the BMVBS :cite:`BundesministeriumfurVerkehrBauundStadtentwicklung.December2010` where different administrative 
buildings were investigated. 
In addition to the basic connection between the net leased area and the envelope 
area it is possible to improve the building data with more information about the 
structure of the building based on a method from Kaag :cite:`Kaag.March2008`. 
The used information for the buildings physics are based on typical wall 
structures based on the year of construction. This data is provided by the 
BMVBS :cite:`BundesministeriumfurVerkehrBauundStadtentwicklung.30.07.2009` and 
is improved by data of the materials from DIN 12524 und 
DIN 4108-4 :cite:`DeutschesInstitutfurNormung.Juli2000` :cite:`DeutschesInstitutfurNormung.Februar2013`.

Office module
--------------------------------------------------------

**Description**

The office module contains a multi zone building according to the BMVBS :cite:`BundesministeriumfurVerkehrBauundStadtentwicklung.December2010`. 
In detail the net leased area is divided in the following thermal zone 
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

The residential module contains a single zone building where the envelopes are 
computed based on a method from the IWU :cite:`KurzverfahrenIWU`. 
In detail the net leased area is divided in the following thermal zone 
area:

#. Single dwelling (100% of net leased area)

.. automodule:: teaser.Logic.BuildingObjects.TypeBuildings.Residential
    :members:
    :undoc-members:
    :show-inheritance:
	
Institute module
-----------------------------------------------------------

**Description**

The institute module contains a multi zone building which is based on an office 
building with an additional laboratory zone. The area of the laboratory zone is
based on data from the Forschungszentrum Jülich fixme. In detail the net leased 
area is divided in the following thermal zone areas:

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

The institute type 4 module contains a multi zone building which is based on an office 
building with an additional laboratory zone. The area of the laboratory zone is
based on data from the Forschungszentrum Jülich fixme. In detail the net leased 
area is divided in the following thermal zone areas:

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

The institute type 8 module contains a multi zone building which is based on an office 
building with an additional laboratory zone. The area of the laboratory zone is
based on data from the Forschungszentrum Jülich fixme. In detail the net leased 
area is divided in the following thermal zone areas:

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
typebuildings according to the DIN V 18599 :cite:`DINV1859910` and the SIA 2024 :cite:`SwissSocietyofEngineersandArchitects.March2006`. 
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

Literature
-----------------------------------------------------------------------------

.. bibliography:: Literatur.bib
	:style: unsrt
	:encoding: latex+latin