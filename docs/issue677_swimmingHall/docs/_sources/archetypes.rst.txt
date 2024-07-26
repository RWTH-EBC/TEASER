Archetype Buildings
===================

This section gives a short overview about archetype methodology implemented in
TEASER. For exact meaning of all attributes and usage of archetype buildings,
please read the docs of archetype classes and examples.

TEASER provides archetypes for residential and non-residential buildings. TEASER
is based on three different studies, investigating the German building stocks.

  - non-residential buildings: :cite:`BundesministeriumfurVerkehrBauundStadtentwicklung.December2010` and :cite:`Lichtme.2010`
  - residential buildings: :cite:`KurzverfahrenIWU`.

TEASER methodology uses 5 basic parameters for data enrichment:

  - main usage of building
  - year of construction
  - net leased/used area
  - average height of floors
  - number of floors

Currently five different archetypes are implemented in TEASER. We are planing to
integrate Tabula archetypes soon.


Non-residential
---------------

The BMVBS package contains different modules for the creation and
parametrisation of typebuildings. In TEASER these typebuildings are used to set
up datasets for buildings out of limited building information. For this, the
methods are based on the following principles according to Lichtmess
:cite:`Lichtme.2010`:

#. The building envelope is a function based on the building's net leased area

#. The building envelope can automatically be assigned to the thermal zones

These principles are mainly used to handle the building envelopes.
In addition it is necessary to use statistic data for the following aspects:

* number of thermal zones

* division of net leased area into zone areas

* wall constructions

* properties of construction materials

The number of zones and respective zone areas differ for different types of
buildings. Detailed information for specific types are given below. The
connection between the building envelope area and the building net leased area
is based on BMVBS
:cite:`BundesministeriumfurVerkehrBauundStadtentwicklung.December2010` where
various administrative buildings were investigated. In addition to this
relationship, it is possible to refine the dataset with further information
about the structure of the building using a method from Kaag
:cite:`Kaag.March2008`. Wall construction is often a function of year of
construction. Such relationships are provided by BMVBS
:cite:`BundesministeriumfurVerkehrBauundStadtentwicklung.30.07.2009` and are
enriched by data for materials from DIN 12524 and DIN 4108-4
:cite:`DeutschesInstitutfurNormung.Juli2000`
:cite:`DeutschesInstitutfurNormung.Februar2013`.

Office
------

The office module contains a multi zone building according to BMVBS :cite:`BundesministeriumfurVerkehrBauundStadtentwicklung.December2010`.
In detail the net leased area is divided into the following thermal zone
areas:

#. Office (50% of net leased area)

#. Floor (25% of net leased area)

#. Storage (15% of net leased area)

#. Meeting (4% of net leased area)

#. Restroom (4% of net leased area)

#. ICT (2% of net leased area)

Institute module
----------------


The institute module contains a multi zone building which is based on an office
building with an additional laboratory zone. The area of the laboratory zone is
based on the data from the Forschungszentrum Jülich :cite:`Abschlussbericht`.
According to the dataset from Jülich, the typebuilding institute is based on the
buildingsclass of BWZK with the number 2200 which represents all institute
buildings which are not institute type 4 or institute type 8
:cite:`Bauministerkonferenz.Dezember2010`. Laboratory zones are verntialed using
a central AHU system with humidification and de-humidification. In detail the
net leased area is divided into the following thermal zone areas:

#. Office (40% of net leased area)

#. Floor (25% of net leased area)

#. Storage (10% of net leased area)

#. Meeting (4% of net leased area)

#. Restroom (4% of net leased area)

#. ICT (2% of net leased area)

#. Laboratory (15% of the net leased area)


Institute4 module
-----------------


The institute type 4 module contains a multi zone building which is based on an
office building with an additional laboratory zone. The area of the laboratory
zone is based on data from the Forschungszentrum Jülich
:cite:`Abschlussbericht`. According to the dataset from Jülich, the typebuilding
institute type 4 is based on the buildingsclass of BWZK with the number 2240
:cite:`Bauministerkonferenz.Dezember2010`. Laboratory zones are verntialed using
a central AHU system with humidification and de-humidification. In detail the
net leased area is divided in the following thermal zone areas:

#. Office (37.5% of net leased area)

#. Floor (22.5% of net leased area)

#. Storage (10% of net leased area)

#. Meeting (4% of net leased area)

#. Restroom (4% of net leased area)

#. ICT (2% of net leased area)

#. Laboratory (20% of the net leased area)


Institute8 module
-----------------


The institute type 8 module contains a multi zone building which is based on an
office building with an additional laboratory zone. The area of the laboratory
zone is based on data from the Forschungszentrum Jülich
:cite:`Abschlussbericht`. According to the dataset from Jülich, the typebuilding
institute type 8 is based on the buildingsclass of BWZK with the number 2240
:cite:`Bauministerkonferenz.Dezember2010`. Laboratory zones are verntialed using
a central AHU system with humidification and de-humidification. In detail the
net leased area is divided in the following thermal zone areas:

#. Office (10% of net leased area)

#. Floor (18% of net leased area)

#. Storage (2% of net leased area)

#. Meeting (4% of net leased area)

#. Restroom (4% of net leased area)

#. ICT (2% of net leased area)

#. Laboratory (60% of the net leased area)

Residential
------------

IWU
----

SingleFamilyDwelling
--------------------

  The residential module contains a single zone building where the envelopes are
  computed based on a method from the IWU :cite:`KurzverfahrenIWU`.
  In detail the net leased area is divided into the following thermal zone
  area:

  #. Living (100% of net leased area)

Tabula
-------

    This is an archetype building for german single family house according to
    TABULA building typology (http://webtool.building-typology.eu/#bm). As
    TABULA defines one reference building, whereas TEASER wants to provide a
    methodology to generate individual building information, this archetype
    underlies some assumptions. The made assumptions are explained in the
    following:

    Each building has four orientations for outer walls and windows (north,
    east, south and west), two orientations for rooftops (south and north), with
    tilt of 35 degree and one orientation for ground floors and one door (
    default
    orientation is west). The area of each surface is calculated using the
    product of the given net_leased_area and specific estimation factors. These
    estimation factors where build by dividing the given 'surface area' by the
    'reference floor area' in TABULA. The estimation factors are calculated for
    each building period ('construction year class'). Please note that the
    number and height of the floors given in TEASER does not have any effect on
    the surface area for heat transmission, but is only used to calculate the
    interior wall area, which is not specified in TABULA at all. Further, TABULA
    does not specify any specific user profile, by default the SingleFamilyHouse
    class has exactly one usage zone, which is 'Living'. TABULA also does not
    always specify the exact construction of building elements, but always
    provides a prescribed U-Value. We used the U-Value and the given material
    information to determine thickness of each layer and implemented it into
    elements XML ('teaser.data.input.inputdata.TypeElements_TABULA_DE.xml'). The
    material properties have been taken from MASEA Material data base
    (http://www.masea-ensan.de/). As there might be some differences in the
    assumptions for material properties from TABULA and MASEA the U-Value might
    not always be exactly the same as in TABULA but is always in an acceptable
    range. The U-Value has been calculated using combined constant values for
    interior and exterior heat transmission, we used a resistance of 0.17
    (m2*K)/W for outer walls, windows, flat roofs and doors; 0.34 (m2*K)/W  for
    ground floors to unheated cellars and 0.17 (m2*K)/W  to direct ground
    coupled floors, 0.21 (m2*K)/W  was taken for pitched roofs.

singlefamilyhouse
-----------------

apartmentblock
-----------------

multifamilyhouse
-----------------

terracedhouse
-----------------

  
Literature
-----------

  .. bibliography::
  	:style: unsrt
