bmvbs package
==================================================

**Description**

The BMVBS package contains different modules for the creation
and parametrisation of typebuildings. In TEASER4 these typebuildings are used to
set up datasets for buildings out of limited building information. For
this, the methods are based on the following principles according to Lichtmess
:cite:`Lichtme.2010`:

#. The building envelope is a function based on the building's net leased area

#. The building envelope can automatically be assigned to the thermal zones

These principles are mainly used to handle the building envelopes.
In addition it is necessary to use statistic data for the following aspects:

* number of thermal zones

* division of net leased area into zone areas

* wall constructions

* properties of construction materials

With the help of such statistical data, it is possible to create archetype
buildings using five parameters:

* type of building

* net leased area

* year of construction

* number of floors

* height of floors

The number of zones and respective zone areas differ for different types of buildings.
Detailed information for specific types are given below.
The connection between the building envelope area and the
building net leased area is based on BMVBS :cite:`BundesministeriumfurVerkehrBauundStadtentwicklung.December2010` where various administrative
buildings were investigated.
In addition to this relationship, it is possible to refine the dataset with further
information about the structure of the building using a method from Kaag :cite:`Kaag.March2008`.
Wall construction is often a function of year of construction. Such relationships are provided by
BMVBS :cite:`BundesministeriumfurVerkehrBauundStadtentwicklung.30.07.2009` and
are enriched by data for materials from DIN 12524 and
DIN 4108-4 :cite:`DeutschesInstitutfurNormung.Juli2000` :cite:`DeutschesInstitutfurNormung.Februar2013`.

Office module
--------------------------------------------------------

**Description**

The office module contains a multi zone building according to BMVBS :cite:`BundesministeriumfurVerkehrBauundStadtentwicklung.December2010`.
In detail the net leased area is divided into the following thermal zone
areas:

#. Office (50% of net leased area)

#. Floor (25% of net leased area)

#. Storage (15% of net leased area)

#. Meeting (4% of net leased area)

#. Restroom (4% of net leased area)

#. ICT (2% of net leased area)

.. automodule:: teaser.Logic.ArchetypeBuildings.BMVBS.Office
    :members:
    :show-inheritance:

SingleFamilyDwelling module
-------------------------------------------------------------

**Description**

The residential module contains a single zone building where the envelopes are
computed based on a method from the IWU :cite:`KurzverfahrenIWU`.
In detail the net leased area is divided into the following thermal zone
area:

#. Single dwelling (100% of net leased area)

.. automodule:: teaser.Logic.ArchetypeBuildings.BMVBS.SingleFamilyDwelling
    :members:
    :show-inheritance:

Institute module
-----------------------------------------------------------

**Description**

The institute module contains a multi zone building which is based on an office
building with an additional laboratory zone. The area of the laboratory zone is
based on the data from the Forschungszentrum Jülich :cite:`Abschlussbericht`.
According to the dataset from Jülich, the typebuilding institute is based on the
buildingsclass of BWZK with the number 2200 which represents all institute
buildings which are not institute type 4 or institute type 8 :cite:`Bauministerkonferenz.Dezember2010`.
In detail the net leased area is divided into the following thermal zone areas:

#. Office (40% of net leased area)

#. Floor (25% of net leased area)

#. Storage (10% of net leased area)

#. Meeting (4% of net leased area)

#. Restroom (4% of net leased area)

#. ICT (2% of net leased area)

#. Laboratory (15% of the net leased area)

.. automodule:: teaser.Logic.ArchetypeBuildings.BMVBS.Custom.Institute
    :members:
    :undoc-members:
    :show-inheritance:

Institute4 module
------------------------------------------------------------

**Description**

The institute type 4 module contains a multi zone building which is based on an office
building with an additional laboratory zone. The area of the laboratory zone is
based on data from the Forschungszentrum Jülich :cite:`Abschlussbericht`.
According to the dataset from Jülich, the typebuilding institute type 4 is based on the
buildingsclass of BWZK with the number 2240 :cite:`Bauministerkonferenz.Dezember2010`.
In detail the net leased
area is divided in the following thermal zone areas:

#. Office (37.5% of net leased area)

#. Floor (22.5% of net leased area)

#. Storage (10% of net leased area)

#. Meeting (4% of net leased area)

#. Restroom (4% of net leased area)

#. ICT (2% of net leased area)

#. Laboratory (20% of the net leased area)

.. automodule:: teaser.Logic.ArchetypeBuildings.BMVBS.Custom.Institute4
    :members:
    :show-inheritance:

Institute8 module
------------------------------------------------------------

**Description**

The institute type 8 module contains a multi zone building which is based on an office
building with an additional laboratory zone. The area of the laboratory zone is
based on data from the Forschungszentrum Jülich :cite:`Abschlussbericht`.
According to the dataset from Jülich, the typebuilding institute type 8 is based on the
buildingsclass of BWZK with the number 2240 :cite:`Bauministerkonferenz.Dezember2010`.
In detail the net leased
area is divided in the following thermal zone areas:

#. Office (10% of net leased area)

#. Floor (18% of net leased area)

#. Storage (2% of net leased area)

#. Meeting (4% of net leased area)

#. Restroom (4% of net leased area)

#. ICT (2% of net leased area)

#. Laboratory (60% of the net leased area)

.. automodule:: teaser.Logic.ArchetypeBuildings.BMVBS.Custom.Institute8
    :members:
    :show-inheritance:


Literature
-----------------------------------------------------------------------------

.. bibliography:: Literatur.bib
	:style: unsrt
	:encoding: latex+latin
