# ./pyxb/bundles/opengis/citygml/raw/building.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1b4db361dcbc3199fe760558a815e57bc06d92f7
# Generated 2015-05-04 11:02:22.225400 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace http://www.opengis.net/citygml/building/1.0

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:45bed49e-f23c-11e4-8344-000c29ce1afb')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import teaser.Data.SchemaBindings.opengis.citygml.raw.base
import teaser.Data.SchemaBindings.opengis.raw.gml

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/citygml/building/1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml = teaser.Data.SchemaBindings.opengis.raw.gml.Namespace
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_core = teaser.Data.SchemaBindings.opengis.citygml.raw.base.Namespace
_Namespace_core.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}BuildingClassType
class BuildingClassType (pyxb.binding.datatypes.string):

    """ Class of a building. The values of this type are defined in the XML file BuildingClassType.xml,
                according to the dictionary concept of GML3."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingClassType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 83, 4)
    _Documentation = ' Class of a building. The values of this type are defined in the XML file BuildingClassType.xml,\n                according to the dictionary concept of GML3.'
BuildingClassType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BuildingClassType', BuildingClassType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}BuildingFunctionType
class BuildingFunctionType (pyxb.binding.datatypes.string):

    """ Intended function of a building. The values of this type are defined in the XML file
                BuildingFunctionType.xml, according to the dictionary concept of GML3. The values may be adopted from ALKIS, the
                german standard for cadastre modelling. If the cadastre models from other countries differ in the building
                functions, these values may be compiled in another codelist to be used with CityGML. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingFunctionType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 91, 4)
    _Documentation = ' Intended function of a building. The values of this type are defined in the XML file\n                BuildingFunctionType.xml, according to the dictionary concept of GML3. The values may be adopted from ALKIS, the\n                german standard for cadastre modelling. If the cadastre models from other countries differ in the building\n                functions, these values may be compiled in another codelist to be used with CityGML. '
BuildingFunctionType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BuildingFunctionType', BuildingFunctionType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}BuildingUsageType
class BuildingUsageType (pyxb.binding.datatypes.string):

    """ Actual usage of a building. The values of this type are defined in the XML file
                BuildingUsageType.xml, according to the dictionary concept of GML3."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingUsageType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 101, 4)
    _Documentation = ' Actual usage of a building. The values of this type are defined in the XML file\n                BuildingUsageType.xml, according to the dictionary concept of GML3.'
BuildingUsageType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BuildingUsageType', BuildingUsageType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}RoofTypeType
class RoofTypeType (pyxb.binding.datatypes.string):

    """Roof Types. The values of this type are defined in the XML file RoofTypeType.xml, according to the
                dictionary concept of GML3."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoofTypeType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 109, 4)
    _Documentation = 'Roof Types. The values of this type are defined in the XML file RoofTypeType.xml, according to the\n                dictionary concept of GML3.'
RoofTypeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'RoofTypeType', RoofTypeType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}BuildingInstallationClassType
class BuildingInstallationClassType (pyxb.binding.datatypes.string):

    """Class of a building installation. The values of this type are defined in the XML file
                BuildingInstallationClassType.xml, according to the dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingInstallationClassType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 186, 4)
    _Documentation = 'Class of a building installation. The values of this type are defined in the XML file\n                BuildingInstallationClassType.xml, according to the dictionary concept of GML3. '
BuildingInstallationClassType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BuildingInstallationClassType', BuildingInstallationClassType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}BuildingInstallationFunctionType
class BuildingInstallationFunctionType (pyxb.binding.datatypes.string):

    """Function of a building installation. The values of this type are defined in the XML file
                BuildingInstallationFunctionType.xml, according to the dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingInstallationFunctionType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 194, 4)
    _Documentation = 'Function of a building installation. The values of this type are defined in the XML file\n                BuildingInstallationFunctionType.xml, according to the dictionary concept of GML3. '
BuildingInstallationFunctionType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BuildingInstallationFunctionType', BuildingInstallationFunctionType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}BuildingInstallationUsageType
class BuildingInstallationUsageType (pyxb.binding.datatypes.string):

    """Actual usage of a building installation. The values of this type are defined in the XML file
                BuildingInstallationUsageType.xml, according to the dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingInstallationUsageType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 202, 4)
    _Documentation = 'Actual usage of a building installation. The values of this type are defined in the XML file\n                BuildingInstallationUsageType.xml, according to the dictionary concept of GML3. '
BuildingInstallationUsageType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BuildingInstallationUsageType', BuildingInstallationUsageType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}IntBuildingInstallationClassType
class IntBuildingInstallationClassType (pyxb.binding.datatypes.string):

    """Class of an interior building installation. The values of this type are defined in the XML file
                IntBuildingInstallationClassType.xml, according to the dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IntBuildingInstallationClassType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 249, 4)
    _Documentation = 'Class of an interior building installation. The values of this type are defined in the XML file\n                IntBuildingInstallationClassType.xml, according to the dictionary concept of GML3. '
IntBuildingInstallationClassType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'IntBuildingInstallationClassType', IntBuildingInstallationClassType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}IntBuildingInstallationFunctionType
class IntBuildingInstallationFunctionType (pyxb.binding.datatypes.string):

    """Function of an interior building installation. The values of this type are defined in the XML file
                IntBuildingInstallationFunctionType.xml, according to the dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IntBuildingInstallationFunctionType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 257, 4)
    _Documentation = 'Function of an interior building installation. The values of this type are defined in the XML file\n                IntBuildingInstallationFunctionType.xml, according to the dictionary concept of GML3. '
IntBuildingInstallationFunctionType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'IntBuildingInstallationFunctionType', IntBuildingInstallationFunctionType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}IntBuildingInstallationUsageType
class IntBuildingInstallationUsageType (pyxb.binding.datatypes.string):

    """Actual Usage of an interior building installation. The values of this type are defined in the XML
                file IntBuildingInstallationUsageType.xml, according to the dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IntBuildingInstallationUsageType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 265, 4)
    _Documentation = 'Actual Usage of an interior building installation. The values of this type are defined in the XML\n                file IntBuildingInstallationUsageType.xml, according to the dictionary concept of GML3. '
IntBuildingInstallationUsageType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'IntBuildingInstallationUsageType', IntBuildingInstallationUsageType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}RoomClassType
class RoomClassType (pyxb.binding.datatypes.string):

    """Class of a room . The values of this type are defined in the XML file RoomClassType.xml, according
                to the dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoomClassType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 545, 4)
    _Documentation = 'Class of a room . The values of this type are defined in the XML file RoomClassType.xml, according\n                to the dictionary concept of GML3. '
RoomClassType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'RoomClassType', RoomClassType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}RoomFunctionType
class RoomFunctionType (pyxb.binding.datatypes.string):

    """Function of a room. The values of this type are defined in the XML file RoomFunctionType.xml,
                according to the dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoomFunctionType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 553, 4)
    _Documentation = 'Function of a room. The values of this type are defined in the XML file RoomFunctionType.xml,\n                according to the dictionary concept of GML3. '
RoomFunctionType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'RoomFunctionType', RoomFunctionType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}RoomUsageType
class RoomUsageType (pyxb.binding.datatypes.string):

    """Actual Usage of a room. The values of this type are defined in the XML file RoomUsageType.xml,
                according to the dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoomUsageType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 561, 4)
    _Documentation = 'Actual Usage of a room. The values of this type are defined in the XML file RoomUsageType.xml,\n                according to the dictionary concept of GML3. '
RoomUsageType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'RoomUsageType', RoomUsageType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}BuildingFurnitureClassType
class BuildingFurnitureClassType (pyxb.binding.datatypes.string):

    """ Class of a building furniture. The values of this type are defined in the XML file
                BuildingFurnitureClassType.xml, according to the dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingFurnitureClassType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 593, 4)
    _Documentation = ' Class of a building furniture. The values of this type are defined in the XML file\n                BuildingFurnitureClassType.xml, according to the dictionary concept of GML3. '
BuildingFurnitureClassType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BuildingFurnitureClassType', BuildingFurnitureClassType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}BuildingFurnitureFunctionType
class BuildingFurnitureFunctionType (pyxb.binding.datatypes.string):

    """ Function of a building furniture. The values of this type are defined in the XML file
                BuildingFurnitureFunctionType.xml, according to the dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingFurnitureFunctionType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 601, 4)
    _Documentation = ' Function of a building furniture. The values of this type are defined in the XML file\n                BuildingFurnitureFunctionType.xml, according to the dictionary concept of GML3. '
BuildingFurnitureFunctionType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BuildingFurnitureFunctionType', BuildingFurnitureFunctionType)

# Atomic simple type: {http://www.opengis.net/citygml/building/1.0}BuildingFurnitureUsageType
class BuildingFurnitureUsageType (pyxb.binding.datatypes.string):

    """ Actual Usage of a building Furniture. The values of this type are defined in the XML file
                BuildingFurnitureUsageType.xml, according to the dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingFurnitureUsageType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 609, 4)
    _Documentation = ' Actual Usage of a building Furniture. The values of this type are defined in the XML file\n                BuildingFurnitureUsageType.xml, according to the dictionary concept of GML3. '
BuildingFurnitureUsageType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'BuildingFurnitureUsageType', BuildingFurnitureUsageType)

# Complex type {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType with content type ELEMENT_ONLY
class AbstractBuildingType (teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractSiteType):
    """Type describing the thematic and geometric attributes and the associations of buildings. It is an
                abstract type, only its subclasses Building and BuildingPart can be instantiated. An _AbstractBuilding may consist
                of BuildingParts, which are again _AbstractBuildings by inheritance. Thus an aggregation hierarchy between
                _AbstractBuildings of arbitrary depth may be specified. In such an hierarchy, top elements are Buildings, while
                all other elements are BuildingParts. Each element of such a hierarchy may have all attributes and geometries of
                _AbstractBuildings. It must, however, be assured than no inconsistencies occur (for example, if the geometry of a
                Building does not correspond to the geometries of its parts, or if the roof type of a Building is saddle roof,
                while its parts have an hip roof). As subclass of _CityObject, an _AbstractBuilding inherits all attributes and
                relations, in particular an id, names, external references, and generalization relations. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractBuildingType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 17, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractSiteType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractSiteType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractSiteType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfSite ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfSite) inherited from {http://www.opengis.net/citygml/1.0}AbstractSiteType
    
    # Element {http://www.opengis.net/citygml/building/1.0}class uses Python identifier class_
    __class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'class'), 'class_', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0class', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 39, 20), )

    
    class_ = property(__class.value, __class.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}function uses Python identifier function
    __function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'function'), 'function', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0function', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 40, 20), )

    
    function = property(__function.value, __function.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}usage uses Python identifier usage
    __usage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usage'), 'usage', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0usage', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 41, 20), )

    
    usage = property(__usage.value, __usage.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}yearOfConstruction uses Python identifier yearOfConstruction
    __yearOfConstruction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'yearOfConstruction'), 'yearOfConstruction', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0yearOfConstruction', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 42, 20), )

    
    yearOfConstruction = property(__yearOfConstruction.value, __yearOfConstruction.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}yearOfDemolition uses Python identifier yearOfDemolition
    __yearOfDemolition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'yearOfDemolition'), 'yearOfDemolition', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0yearOfDemolition', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 43, 20), )

    
    yearOfDemolition = property(__yearOfDemolition.value, __yearOfDemolition.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}roofType uses Python identifier roofType
    __roofType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'roofType'), 'roofType', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0roofType', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 44, 20), )

    
    roofType = property(__roofType.value, __roofType.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}measuredHeight uses Python identifier measuredHeight
    __measuredHeight = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'measuredHeight'), 'measuredHeight', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0measuredHeight', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 45, 20), )

    
    measuredHeight = property(__measuredHeight.value, __measuredHeight.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}storeysAboveGround uses Python identifier storeysAboveGround
    __storeysAboveGround = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'storeysAboveGround'), 'storeysAboveGround', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0storeysAboveGround', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 46, 20), )

    
    storeysAboveGround = property(__storeysAboveGround.value, __storeysAboveGround.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}storeysBelowGround uses Python identifier storeysBelowGround
    __storeysBelowGround = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'storeysBelowGround'), 'storeysBelowGround', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0storeysBelowGround', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 47, 20), )

    
    storeysBelowGround = property(__storeysBelowGround.value, __storeysBelowGround.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}storeyHeightsAboveGround uses Python identifier storeyHeightsAboveGround
    __storeyHeightsAboveGround = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'storeyHeightsAboveGround'), 'storeyHeightsAboveGround', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0storeyHeightsAboveGround', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 48, 20), )

    
    storeyHeightsAboveGround = property(__storeyHeightsAboveGround.value, __storeyHeightsAboveGround.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}storeyHeightsBelowGround uses Python identifier storeyHeightsBelowGround
    __storeyHeightsBelowGround = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'storeyHeightsBelowGround'), 'storeyHeightsBelowGround', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0storeyHeightsBelowGround', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 49, 20), )

    
    storeyHeightsBelowGround = property(__storeyHeightsBelowGround.value, __storeyHeightsBelowGround.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod1Solid uses Python identifier lod1Solid
    __lod1Solid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod1Solid'), 'lod1Solid', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod1Solid', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 50, 20), )

    
    lod1Solid = property(__lod1Solid.value, __lod1Solid.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod1MultiSurface uses Python identifier lod1MultiSurface
    __lod1MultiSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod1MultiSurface'), 'lod1MultiSurface', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod1MultiSurface', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 51, 20), )

    
    lod1MultiSurface = property(__lod1MultiSurface.value, __lod1MultiSurface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod1TerrainIntersection uses Python identifier lod1TerrainIntersection
    __lod1TerrainIntersection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod1TerrainIntersection'), 'lod1TerrainIntersection', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod1TerrainIntersection', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 52, 20), )

    
    lod1TerrainIntersection = property(__lod1TerrainIntersection.value, __lod1TerrainIntersection.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod2Solid uses Python identifier lod2Solid
    __lod2Solid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod2Solid'), 'lod2Solid', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod2Solid', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 53, 20), )

    
    lod2Solid = property(__lod2Solid.value, __lod2Solid.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod2MultiSurface uses Python identifier lod2MultiSurface
    __lod2MultiSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface'), 'lod2MultiSurface', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod2MultiSurface', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 54, 20), )

    
    lod2MultiSurface = property(__lod2MultiSurface.value, __lod2MultiSurface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod2MultiCurve uses Python identifier lod2MultiCurve
    __lod2MultiCurve = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiCurve'), 'lod2MultiCurve', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod2MultiCurve', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 55, 20), )

    
    lod2MultiCurve = property(__lod2MultiCurve.value, __lod2MultiCurve.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod2TerrainIntersection uses Python identifier lod2TerrainIntersection
    __lod2TerrainIntersection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod2TerrainIntersection'), 'lod2TerrainIntersection', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod2TerrainIntersection', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 56, 20), )

    
    lod2TerrainIntersection = property(__lod2TerrainIntersection.value, __lod2TerrainIntersection.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}outerBuildingInstallation uses Python identifier outerBuildingInstallation
    __outerBuildingInstallation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outerBuildingInstallation'), 'outerBuildingInstallation', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0outerBuildingInstallation', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 57, 20), )

    
    outerBuildingInstallation = property(__outerBuildingInstallation.value, __outerBuildingInstallation.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}interiorBuildingInstallation uses Python identifier interiorBuildingInstallation
    __interiorBuildingInstallation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'interiorBuildingInstallation'), 'interiorBuildingInstallation', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0interiorBuildingInstallation', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 59, 20), )

    
    interiorBuildingInstallation = property(__interiorBuildingInstallation.value, __interiorBuildingInstallation.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}boundedBy uses Python identifier boundedBy_
    __boundedBy_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'boundedBy'), 'boundedBy_', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0boundedBy', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 61, 20), )

    
    boundedBy_ = property(__boundedBy_.value, __boundedBy_.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod3Solid uses Python identifier lod3Solid
    __lod3Solid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod3Solid'), 'lod3Solid', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod3Solid', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 62, 20), )

    
    lod3Solid = property(__lod3Solid.value, __lod3Solid.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod3MultiSurface uses Python identifier lod3MultiSurface
    __lod3MultiSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface'), 'lod3MultiSurface', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod3MultiSurface', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 63, 20), )

    
    lod3MultiSurface = property(__lod3MultiSurface.value, __lod3MultiSurface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod3MultiCurve uses Python identifier lod3MultiCurve
    __lod3MultiCurve = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiCurve'), 'lod3MultiCurve', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod3MultiCurve', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 64, 20), )

    
    lod3MultiCurve = property(__lod3MultiCurve.value, __lod3MultiCurve.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod3TerrainIntersection uses Python identifier lod3TerrainIntersection
    __lod3TerrainIntersection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod3TerrainIntersection'), 'lod3TerrainIntersection', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod3TerrainIntersection', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 65, 20), )

    
    lod3TerrainIntersection = property(__lod3TerrainIntersection.value, __lod3TerrainIntersection.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod4Solid uses Python identifier lod4Solid
    __lod4Solid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4Solid'), 'lod4Solid', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod4Solid', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 66, 20), )

    
    lod4Solid = property(__lod4Solid.value, __lod4Solid.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod4MultiSurface uses Python identifier lod4MultiSurface
    __lod4MultiSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface'), 'lod4MultiSurface', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod4MultiSurface', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 67, 20), )

    
    lod4MultiSurface = property(__lod4MultiSurface.value, __lod4MultiSurface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod4MultiCurve uses Python identifier lod4MultiCurve
    __lod4MultiCurve = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiCurve'), 'lod4MultiCurve', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod4MultiCurve', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 68, 20), )

    
    lod4MultiCurve = property(__lod4MultiCurve.value, __lod4MultiCurve.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod4TerrainIntersection uses Python identifier lod4TerrainIntersection
    __lod4TerrainIntersection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4TerrainIntersection'), 'lod4TerrainIntersection', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0lod4TerrainIntersection', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 69, 20), )

    
    lod4TerrainIntersection = property(__lod4TerrainIntersection.value, __lod4TerrainIntersection.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}interiorRoom uses Python identifier interiorRoom
    __interiorRoom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'interiorRoom'), 'interiorRoom', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0interiorRoom', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 70, 20), )

    
    interiorRoom = property(__interiorRoom.value, __interiorRoom.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}consistsOfBuildingPart uses Python identifier consistsOfBuildingPart
    __consistsOfBuildingPart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'consistsOfBuildingPart'), 'consistsOfBuildingPart', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0consistsOfBuildingPart', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 71, 20), )

    
    consistsOfBuildingPart = property(__consistsOfBuildingPart.value, __consistsOfBuildingPart.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'address'), 'address', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0address', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 72, 20), )

    
    address = property(__address.value, __address.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfAbstractBuilding uses Python identifier GenericApplicationPropertyOfAbstractBuilding
    __GenericApplicationPropertyOfAbstractBuilding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfAbstractBuilding'), 'GenericApplicationPropertyOfAbstractBuilding', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBuildingType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfAbstractBuilding', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 81, 4), )

    
    GenericApplicationPropertyOfAbstractBuilding = property(__GenericApplicationPropertyOfAbstractBuilding.value, __GenericApplicationPropertyOfAbstractBuilding.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __class.name() : __class,
        __function.name() : __function,
        __usage.name() : __usage,
        __yearOfConstruction.name() : __yearOfConstruction,
        __yearOfDemolition.name() : __yearOfDemolition,
        __roofType.name() : __roofType,
        __measuredHeight.name() : __measuredHeight,
        __storeysAboveGround.name() : __storeysAboveGround,
        __storeysBelowGround.name() : __storeysBelowGround,
        __storeyHeightsAboveGround.name() : __storeyHeightsAboveGround,
        __storeyHeightsBelowGround.name() : __storeyHeightsBelowGround,
        __lod1Solid.name() : __lod1Solid,
        __lod1MultiSurface.name() : __lod1MultiSurface,
        __lod1TerrainIntersection.name() : __lod1TerrainIntersection,
        __lod2Solid.name() : __lod2Solid,
        __lod2MultiSurface.name() : __lod2MultiSurface,
        __lod2MultiCurve.name() : __lod2MultiCurve,
        __lod2TerrainIntersection.name() : __lod2TerrainIntersection,
        __outerBuildingInstallation.name() : __outerBuildingInstallation,
        __interiorBuildingInstallation.name() : __interiorBuildingInstallation,
        __boundedBy_.name() : __boundedBy_,
        __lod3Solid.name() : __lod3Solid,
        __lod3MultiSurface.name() : __lod3MultiSurface,
        __lod3MultiCurve.name() : __lod3MultiCurve,
        __lod3TerrainIntersection.name() : __lod3TerrainIntersection,
        __lod4Solid.name() : __lod4Solid,
        __lod4MultiSurface.name() : __lod4MultiSurface,
        __lod4MultiCurve.name() : __lod4MultiCurve,
        __lod4TerrainIntersection.name() : __lod4TerrainIntersection,
        __interiorRoom.name() : __interiorRoom,
        __consistsOfBuildingPart.name() : __consistsOfBuildingPart,
        __address.name() : __address,
        __GenericApplicationPropertyOfAbstractBuilding.name() : __GenericApplicationPropertyOfAbstractBuilding
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AbstractBuildingType', AbstractBuildingType)


# Complex type {http://www.opengis.net/citygml/building/1.0}BuildingPartPropertyType with content type ELEMENT_ONLY
class BuildingPartPropertyType (teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType):
    """Denotes the relation of an _AbstractBuilding to its building parts. The BuildingPartPropertyType
                element must either carry a reference to a BuildingPart object or contain a BuildingPart object inline, but
                neither both nor none."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingPartPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 145, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType
    
    # Element {http://www.opengis.net/citygml/building/1.0}BuildingPart uses Python identifier BuildingPart
    __BuildingPart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BuildingPart'), 'BuildingPart', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingPartPropertyType_httpwww_opengis_netcitygmlbuilding1_0BuildingPart', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 141, 4), )

    
    BuildingPart = property(__BuildingPart.value, __BuildingPart.set, None, None)

    
    # Attribute remoteSchema inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute type inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute href inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute role inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute arcrole inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute title inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute show inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute actuate inherited from {http://www.opengis.net/gml}AssociationType
    _ElementMap.update({
        __BuildingPart.name() : __BuildingPart
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BuildingPartPropertyType', BuildingPartPropertyType)


# Complex type {http://www.opengis.net/citygml/building/1.0}BuildingInstallationType with content type ELEMENT_ONLY
class BuildingInstallationType (teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType):
    """A BuildingInstallation is a part of a Building which has not the significance of a BuildingPart.
                Examples are stairs, antennas, balconies or small roofs. As subclass of _CityObject, a BuildingInstallation
                inherits all attributes and relations, in particular an id, names, external references, and generalization
                relations. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingInstallationType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 160, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element {http://www.opengis.net/citygml/building/1.0}class uses Python identifier class_
    __class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'class'), 'class_', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingInstallationType_httpwww_opengis_netcitygmlbuilding1_0class', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 170, 20), )

    
    class_ = property(__class.value, __class.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}function uses Python identifier function
    __function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'function'), 'function', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingInstallationType_httpwww_opengis_netcitygmlbuilding1_0function', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 171, 20), )

    
    function = property(__function.value, __function.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}usage uses Python identifier usage
    __usage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usage'), 'usage', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingInstallationType_httpwww_opengis_netcitygmlbuilding1_0usage', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 172, 20), )

    
    usage = property(__usage.value, __usage.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod2Geometry uses Python identifier lod2Geometry
    __lod2Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod2Geometry'), 'lod2Geometry', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingInstallationType_httpwww_opengis_netcitygmlbuilding1_0lod2Geometry', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 173, 20), )

    
    lod2Geometry = property(__lod2Geometry.value, __lod2Geometry.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod3Geometry uses Python identifier lod3Geometry
    __lod3Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod3Geometry'), 'lod3Geometry', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingInstallationType_httpwww_opengis_netcitygmlbuilding1_0lod3Geometry', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 174, 20), )

    
    lod3Geometry = property(__lod3Geometry.value, __lod3Geometry.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod4Geometry uses Python identifier lod4Geometry
    __lod4Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4Geometry'), 'lod4Geometry', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingInstallationType_httpwww_opengis_netcitygmlbuilding1_0lod4Geometry', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 175, 20), )

    
    lod4Geometry = property(__lod4Geometry.value, __lod4Geometry.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfBuildingInstallation uses Python identifier GenericApplicationPropertyOfBuildingInstallation
    __GenericApplicationPropertyOfBuildingInstallation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuildingInstallation'), 'GenericApplicationPropertyOfBuildingInstallation', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingInstallationType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfBuildingInstallation', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 184, 4), )

    
    GenericApplicationPropertyOfBuildingInstallation = property(__GenericApplicationPropertyOfBuildingInstallation.value, __GenericApplicationPropertyOfBuildingInstallation.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __class.name() : __class,
        __function.name() : __function,
        __usage.name() : __usage,
        __lod2Geometry.name() : __lod2Geometry,
        __lod3Geometry.name() : __lod3Geometry,
        __lod4Geometry.name() : __lod4Geometry,
        __GenericApplicationPropertyOfBuildingInstallation.name() : __GenericApplicationPropertyOfBuildingInstallation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BuildingInstallationType', BuildingInstallationType)


# Complex type {http://www.opengis.net/citygml/building/1.0}BuildingInstallationPropertyType with content type ELEMENT_ONLY
class BuildingInstallationPropertyType (teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType):
    """Denotes the relation of an _AbstractBuilding to its building installations. The
                BuildingInstallationPropertyType element must either carry a reference to a BuildingInstallation object or contain
                a BuildingInstallation object inline, but neither both nor none. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingInstallationPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 210, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType
    
    # Element {http://www.opengis.net/citygml/building/1.0}BuildingInstallation uses Python identifier BuildingInstallation
    __BuildingInstallation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BuildingInstallation'), 'BuildingInstallation', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingInstallationPropertyType_httpwww_opengis_netcitygmlbuilding1_0BuildingInstallation', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 182, 4), )

    
    BuildingInstallation = property(__BuildingInstallation.value, __BuildingInstallation.set, None, None)

    
    # Attribute remoteSchema inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute type inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute href inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute role inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute arcrole inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute title inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute show inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute actuate inherited from {http://www.opengis.net/gml}AssociationType
    _ElementMap.update({
        __BuildingInstallation.name() : __BuildingInstallation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BuildingInstallationPropertyType', BuildingInstallationPropertyType)


# Complex type {http://www.opengis.net/citygml/building/1.0}IntBuildingInstallationType with content type ELEMENT_ONLY
class IntBuildingInstallationType (teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType):
    """An IntBuildingInstallation is an interior part of a Building which has a specific function or
                semantical meaning. Examples are interior stairs, railings, radiators or pipes. As subclass of _CityObject, a
                nIntBuildingInstallation inherits all attributes and relations, in particular an id, names, external references,
                and generalization relations. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IntBuildingInstallationType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 225, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element {http://www.opengis.net/citygml/building/1.0}class uses Python identifier class_
    __class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'class'), 'class_', '__httpwww_opengis_netcitygmlbuilding1_0_IntBuildingInstallationType_httpwww_opengis_netcitygmlbuilding1_0class', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 235, 20), )

    
    class_ = property(__class.value, __class.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}function uses Python identifier function
    __function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'function'), 'function', '__httpwww_opengis_netcitygmlbuilding1_0_IntBuildingInstallationType_httpwww_opengis_netcitygmlbuilding1_0function', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 236, 20), )

    
    function = property(__function.value, __function.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}usage uses Python identifier usage
    __usage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usage'), 'usage', '__httpwww_opengis_netcitygmlbuilding1_0_IntBuildingInstallationType_httpwww_opengis_netcitygmlbuilding1_0usage', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 237, 20), )

    
    usage = property(__usage.value, __usage.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod4Geometry uses Python identifier lod4Geometry
    __lod4Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4Geometry'), 'lod4Geometry', '__httpwww_opengis_netcitygmlbuilding1_0_IntBuildingInstallationType_httpwww_opengis_netcitygmlbuilding1_0lod4Geometry', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 238, 20), )

    
    lod4Geometry = property(__lod4Geometry.value, __lod4Geometry.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfIntBuildingInstallation uses Python identifier GenericApplicationPropertyOfIntBuildingInstallation
    __GenericApplicationPropertyOfIntBuildingInstallation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfIntBuildingInstallation'), 'GenericApplicationPropertyOfIntBuildingInstallation', '__httpwww_opengis_netcitygmlbuilding1_0_IntBuildingInstallationType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfIntBuildingInstallation', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 247, 4), )

    
    GenericApplicationPropertyOfIntBuildingInstallation = property(__GenericApplicationPropertyOfIntBuildingInstallation.value, __GenericApplicationPropertyOfIntBuildingInstallation.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __class.name() : __class,
        __function.name() : __function,
        __usage.name() : __usage,
        __lod4Geometry.name() : __lod4Geometry,
        __GenericApplicationPropertyOfIntBuildingInstallation.name() : __GenericApplicationPropertyOfIntBuildingInstallation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'IntBuildingInstallationType', IntBuildingInstallationType)


# Complex type {http://www.opengis.net/citygml/building/1.0}IntBuildingInstallationPropertyType with content type ELEMENT_ONLY
class IntBuildingInstallationPropertyType (teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType):
    """Denotes the relation of an _AbstractBuilding to its interior building installations. The
                IntBuildingInstallationPropertyType element must either carry a reference to a IntBuildingInstallation object or
                contain a IntBuildingInstallation object inline, but neither both nor none. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IntBuildingInstallationPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 273, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType
    
    # Element {http://www.opengis.net/citygml/building/1.0}IntBuildingInstallation uses Python identifier IntBuildingInstallation
    __IntBuildingInstallation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'IntBuildingInstallation'), 'IntBuildingInstallation', '__httpwww_opengis_netcitygmlbuilding1_0_IntBuildingInstallationPropertyType_httpwww_opengis_netcitygmlbuilding1_0IntBuildingInstallation', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 245, 4), )

    
    IntBuildingInstallation = property(__IntBuildingInstallation.value, __IntBuildingInstallation.set, None, None)

    
    # Attribute remoteSchema inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute type inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute href inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute role inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute arcrole inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute title inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute show inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute actuate inherited from {http://www.opengis.net/gml}AssociationType
    _ElementMap.update({
        __IntBuildingInstallation.name() : __IntBuildingInstallation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'IntBuildingInstallationPropertyType', IntBuildingInstallationPropertyType)


# Complex type {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType with content type ELEMENT_ONLY
class AbstractBoundarySurfaceType (teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType):
    """A BoundarySurface is a thematic object which classifies surfaces bounding a building or a room. The
                geometry of a BoundarySurface is given by MultiSurfaces. As it is a subclass of _CityObject, it inherits all
                atributes and relations, in particular the external references, and the generalization relations.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractBoundarySurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 290, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element {http://www.opengis.net/citygml/building/1.0}lod2MultiSurface uses Python identifier lod2MultiSurface
    __lod2MultiSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface'), 'lod2MultiSurface', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBoundarySurfaceType_httpwww_opengis_netcitygmlbuilding1_0lod2MultiSurface', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20), )

    
    lod2MultiSurface = property(__lod2MultiSurface.value, __lod2MultiSurface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod3MultiSurface uses Python identifier lod3MultiSurface
    __lod3MultiSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface'), 'lod3MultiSurface', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBoundarySurfaceType_httpwww_opengis_netcitygmlbuilding1_0lod3MultiSurface', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20), )

    
    lod3MultiSurface = property(__lod3MultiSurface.value, __lod3MultiSurface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod4MultiSurface uses Python identifier lod4MultiSurface
    __lod4MultiSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface'), 'lod4MultiSurface', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBoundarySurfaceType_httpwww_opengis_netcitygmlbuilding1_0lod4MultiSurface', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20), )

    
    lod4MultiSurface = property(__lod4MultiSurface.value, __lod4MultiSurface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}opening uses Python identifier opening
    __opening = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'opening'), 'opening', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBoundarySurfaceType_httpwww_opengis_netcitygmlbuilding1_0opening', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20), )

    
    opening = property(__opening.value, __opening.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfBoundarySurface uses Python identifier GenericApplicationPropertyOfBoundarySurface
    __GenericApplicationPropertyOfBoundarySurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBoundarySurface'), 'GenericApplicationPropertyOfBoundarySurface', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractBoundarySurfaceType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfBoundarySurface', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 312, 4), )

    
    GenericApplicationPropertyOfBoundarySurface = property(__GenericApplicationPropertyOfBoundarySurface.value, __GenericApplicationPropertyOfBoundarySurface.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __lod2MultiSurface.name() : __lod2MultiSurface,
        __lod3MultiSurface.name() : __lod3MultiSurface,
        __lod4MultiSurface.name() : __lod4MultiSurface,
        __opening.name() : __opening,
        __GenericApplicationPropertyOfBoundarySurface.name() : __GenericApplicationPropertyOfBoundarySurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AbstractBoundarySurfaceType', AbstractBoundarySurfaceType)


# Complex type {http://www.opengis.net/citygml/building/1.0}BoundarySurfacePropertyType with content type ELEMENT_ONLY
class BoundarySurfacePropertyType (teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType):
    """Denotes the relation of an _AbstractBuilding to its bounding thematic surfaces (walls, roofs, ..).
                The BoundarySurfacePropertyType element must either carry a reference to a _BoundarySurface object or contain a
                _BoundarySurface object inline, but neither both nor none. There is no differentiation between interior surfaces
                bounding rooms and outer ones bounding buildings (one reason is, that ClosureSurfaces belong to both types). It
                has to be made sure by additional integrity constraints that, e.g. an _AbstractBuilding is not related to
                CeilingSurfaces or a room not to RoofSurfaces. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoundarySurfacePropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 416, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType
    
    # Element {http://www.opengis.net/citygml/building/1.0}_BoundarySurface uses Python identifier BoundarySurface
    __BoundarySurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_BoundarySurface'), 'BoundarySurface', '__httpwww_opengis_netcitygmlbuilding1_0_BoundarySurfacePropertyType_httpwww_opengis_netcitygmlbuilding1_0_BoundarySurface', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 310, 4), )

    
    BoundarySurface = property(__BoundarySurface.value, __BoundarySurface.set, None, None)

    
    # Attribute remoteSchema inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute type inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute href inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute role inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute arcrole inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute title inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute show inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute actuate inherited from {http://www.opengis.net/gml}AssociationType
    _ElementMap.update({
        __BoundarySurface.name() : __BoundarySurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BoundarySurfacePropertyType', BoundarySurfacePropertyType)


# Complex type {http://www.opengis.net/citygml/building/1.0}OpeningPropertyType with content type ELEMENT_ONLY
class OpeningPropertyType (teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType):
    """Denotes the relation of an _BondarySurface to its openings (doors, windows). The OpeningPropertyType
                element must either carry a reference to an _Opening object or contain an _Opening object inline, but neither both
                nor none. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OpeningPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 436, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType
    
    # Element {http://www.opengis.net/citygml/building/1.0}_Opening uses Python identifier Opening
    __Opening = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_Opening'), 'Opening', '__httpwww_opengis_netcitygmlbuilding1_0_OpeningPropertyType_httpwww_opengis_netcitygmlbuilding1_0_Opening', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 468, 4), )

    
    Opening = property(__Opening.value, __Opening.set, None, None)

    
    # Attribute remoteSchema inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute type inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute href inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute role inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute arcrole inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute title inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute show inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute actuate inherited from {http://www.opengis.net/gml}AssociationType
    _ElementMap.update({
        __Opening.name() : __Opening
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'OpeningPropertyType', OpeningPropertyType)


# Complex type {http://www.opengis.net/citygml/building/1.0}AbstractOpeningType with content type ELEMENT_ONLY
class AbstractOpeningType (teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType):
    """ Type for openings (doors, windows) in walls. Used in LOD3 and LOD4 only. As subclass of
                _CityObject, an _Opening inherits all attributes and relations, in particular an id, names, external references,
                and generalization relations. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractOpeningType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 451, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element {http://www.opengis.net/citygml/building/1.0}lod3MultiSurface uses Python identifier lod3MultiSurface
    __lod3MultiSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface'), 'lod3MultiSurface', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractOpeningType_httpwww_opengis_netcitygmlbuilding1_0lod3MultiSurface', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 460, 20), )

    
    lod3MultiSurface = property(__lod3MultiSurface.value, __lod3MultiSurface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod4MultiSurface uses Python identifier lod4MultiSurface
    __lod4MultiSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface'), 'lod4MultiSurface', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractOpeningType_httpwww_opengis_netcitygmlbuilding1_0lod4MultiSurface', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 461, 20), )

    
    lod4MultiSurface = property(__lod4MultiSurface.value, __lod4MultiSurface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfOpening uses Python identifier GenericApplicationPropertyOfOpening
    __GenericApplicationPropertyOfOpening = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfOpening'), 'GenericApplicationPropertyOfOpening', '__httpwww_opengis_netcitygmlbuilding1_0_AbstractOpeningType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfOpening', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 470, 4), )

    
    GenericApplicationPropertyOfOpening = property(__GenericApplicationPropertyOfOpening.value, __GenericApplicationPropertyOfOpening.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __lod3MultiSurface.name() : __lod3MultiSurface,
        __lod4MultiSurface.name() : __lod4MultiSurface,
        __GenericApplicationPropertyOfOpening.name() : __GenericApplicationPropertyOfOpening
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AbstractOpeningType', AbstractOpeningType)


# Complex type {http://www.opengis.net/citygml/building/1.0}RoomType with content type ELEMENT_ONLY
class RoomType (teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType):
    """A Room is a thematic object for modelling the closed parts inside a building. It has to be closed,
                if necessary by using closure surfaces. The geometry may be either a solid, or a MultiSurface if the boundary is
                not topologically clean. The room connectivity may be derived by detecting shared thematic openings or closure
                surfaces: two rooms are connected if both use the same opening object or the same closure surface. The thematic
                surfaces bounding a room are referenced by the boundedBy property. As subclass of _CityObject, a Room inherits all
                attributes and relations, in particular an id, names, external references, and generalization relations.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoomType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 513, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element {http://www.opengis.net/citygml/building/1.0}class uses Python identifier class_
    __class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'class'), 'class_', '__httpwww_opengis_netcitygmlbuilding1_0_RoomType_httpwww_opengis_netcitygmlbuilding1_0class', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 526, 20), )

    
    class_ = property(__class.value, __class.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}function uses Python identifier function
    __function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'function'), 'function', '__httpwww_opengis_netcitygmlbuilding1_0_RoomType_httpwww_opengis_netcitygmlbuilding1_0function', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 527, 20), )

    
    function = property(__function.value, __function.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}usage uses Python identifier usage
    __usage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usage'), 'usage', '__httpwww_opengis_netcitygmlbuilding1_0_RoomType_httpwww_opengis_netcitygmlbuilding1_0usage', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 528, 20), )

    
    usage = property(__usage.value, __usage.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod4Solid uses Python identifier lod4Solid
    __lod4Solid = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4Solid'), 'lod4Solid', '__httpwww_opengis_netcitygmlbuilding1_0_RoomType_httpwww_opengis_netcitygmlbuilding1_0lod4Solid', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 529, 20), )

    
    lod4Solid = property(__lod4Solid.value, __lod4Solid.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod4MultiSurface uses Python identifier lod4MultiSurface
    __lod4MultiSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface'), 'lod4MultiSurface', '__httpwww_opengis_netcitygmlbuilding1_0_RoomType_httpwww_opengis_netcitygmlbuilding1_0lod4MultiSurface', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 530, 20), )

    
    lod4MultiSurface = property(__lod4MultiSurface.value, __lod4MultiSurface.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}boundedBy uses Python identifier boundedBy_
    __boundedBy_ = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'boundedBy'), 'boundedBy_', '__httpwww_opengis_netcitygmlbuilding1_0_RoomType_httpwww_opengis_netcitygmlbuilding1_0boundedBy', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 531, 20), )

    
    boundedBy_ = property(__boundedBy_.value, __boundedBy_.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}interiorFurniture uses Python identifier interiorFurniture
    __interiorFurniture = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'interiorFurniture'), 'interiorFurniture', '__httpwww_opengis_netcitygmlbuilding1_0_RoomType_httpwww_opengis_netcitygmlbuilding1_0interiorFurniture', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 532, 20), )

    
    interiorFurniture = property(__interiorFurniture.value, __interiorFurniture.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}roomInstallation uses Python identifier roomInstallation
    __roomInstallation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'roomInstallation'), 'roomInstallation', '__httpwww_opengis_netcitygmlbuilding1_0_RoomType_httpwww_opengis_netcitygmlbuilding1_0roomInstallation', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 533, 20), )

    
    roomInstallation = property(__roomInstallation.value, __roomInstallation.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfRoom uses Python identifier GenericApplicationPropertyOfRoom
    __GenericApplicationPropertyOfRoom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfRoom'), 'GenericApplicationPropertyOfRoom', '__httpwww_opengis_netcitygmlbuilding1_0_RoomType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfRoom', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 543, 4), )

    
    GenericApplicationPropertyOfRoom = property(__GenericApplicationPropertyOfRoom.value, __GenericApplicationPropertyOfRoom.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __class.name() : __class,
        __function.name() : __function,
        __usage.name() : __usage,
        __lod4Solid.name() : __lod4Solid,
        __lod4MultiSurface.name() : __lod4MultiSurface,
        __boundedBy_.name() : __boundedBy_,
        __interiorFurniture.name() : __interiorFurniture,
        __roomInstallation.name() : __roomInstallation,
        __GenericApplicationPropertyOfRoom.name() : __GenericApplicationPropertyOfRoom
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RoomType', RoomType)


# Complex type {http://www.opengis.net/citygml/building/1.0}BuildingFurnitureType with content type ELEMENT_ONLY
class BuildingFurnitureType (teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType):
    """Type for building furnitures. As subclass of _CityObject, a BuildingFurniture inherits all
                attributes and relations, in particular an id, names, external references, and generalization relations.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingFurnitureType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 569, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element {http://www.opengis.net/citygml/building/1.0}class uses Python identifier class_
    __class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'class'), 'class_', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingFurnitureType_httpwww_opengis_netcitygmlbuilding1_0class', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 578, 20), )

    
    class_ = property(__class.value, __class.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}function uses Python identifier function
    __function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'function'), 'function', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingFurnitureType_httpwww_opengis_netcitygmlbuilding1_0function', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 579, 20), )

    
    function = property(__function.value, __function.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}usage uses Python identifier usage
    __usage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usage'), 'usage', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingFurnitureType_httpwww_opengis_netcitygmlbuilding1_0usage', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 580, 20), )

    
    usage = property(__usage.value, __usage.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod4Geometry uses Python identifier lod4Geometry
    __lod4Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4Geometry'), 'lod4Geometry', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingFurnitureType_httpwww_opengis_netcitygmlbuilding1_0lod4Geometry', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 581, 20), )

    
    lod4Geometry = property(__lod4Geometry.value, __lod4Geometry.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}lod4ImplicitRepresentation uses Python identifier lod4ImplicitRepresentation
    __lod4ImplicitRepresentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4ImplicitRepresentation'), 'lod4ImplicitRepresentation', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingFurnitureType_httpwww_opengis_netcitygmlbuilding1_0lod4ImplicitRepresentation', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 582, 20), )

    
    lod4ImplicitRepresentation = property(__lod4ImplicitRepresentation.value, __lod4ImplicitRepresentation.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfBuildingFurniture uses Python identifier GenericApplicationPropertyOfBuildingFurniture
    __GenericApplicationPropertyOfBuildingFurniture = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuildingFurniture'), 'GenericApplicationPropertyOfBuildingFurniture', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingFurnitureType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfBuildingFurniture', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 591, 4), )

    
    GenericApplicationPropertyOfBuildingFurniture = property(__GenericApplicationPropertyOfBuildingFurniture.value, __GenericApplicationPropertyOfBuildingFurniture.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __class.name() : __class,
        __function.name() : __function,
        __usage.name() : __usage,
        __lod4Geometry.name() : __lod4Geometry,
        __lod4ImplicitRepresentation.name() : __lod4ImplicitRepresentation,
        __GenericApplicationPropertyOfBuildingFurniture.name() : __GenericApplicationPropertyOfBuildingFurniture
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BuildingFurnitureType', BuildingFurnitureType)


# Complex type {http://www.opengis.net/citygml/building/1.0}InteriorRoomPropertyType with content type ELEMENT_ONLY
class InteriorRoomPropertyType (teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType):
    """Denotes the relation of an _AbstractBuilding to its rooms. The InteriorRoomPropertyType element must
                either carry a reference to a Room object or contain a Room object inline, but neither both nor none.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InteriorRoomPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 619, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType
    
    # Element {http://www.opengis.net/citygml/building/1.0}Room uses Python identifier Room
    __Room = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Room'), 'Room', '__httpwww_opengis_netcitygmlbuilding1_0_InteriorRoomPropertyType_httpwww_opengis_netcitygmlbuilding1_0Room', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 541, 4), )

    
    Room = property(__Room.value, __Room.set, None, None)

    
    # Attribute remoteSchema inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute type inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute href inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute role inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute arcrole inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute title inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute show inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute actuate inherited from {http://www.opengis.net/gml}AssociationType
    _ElementMap.update({
        __Room.name() : __Room
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'InteriorRoomPropertyType', InteriorRoomPropertyType)


# Complex type {http://www.opengis.net/citygml/building/1.0}InteriorFurniturePropertyType with content type ELEMENT_ONLY
class InteriorFurniturePropertyType (teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType):
    """Denotes the relation of a Room to its interior furnitures (movable). The
                InteriorFurniturePropertyType element must either carry a reference to a BuildingFurniture object or contain a
                BuildingFurniture object inline, but neither both nor none. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InteriorFurniturePropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 634, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType
    
    # Element {http://www.opengis.net/citygml/building/1.0}BuildingFurniture uses Python identifier BuildingFurniture
    __BuildingFurniture = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BuildingFurniture'), 'BuildingFurniture', '__httpwww_opengis_netcitygmlbuilding1_0_InteriorFurniturePropertyType_httpwww_opengis_netcitygmlbuilding1_0BuildingFurniture', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 589, 4), )

    
    BuildingFurniture = property(__BuildingFurniture.value, __BuildingFurniture.set, None, None)

    
    # Attribute remoteSchema inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute type inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute href inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute role inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute arcrole inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute title inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute show inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute actuate inherited from {http://www.opengis.net/gml}AssociationType
    _ElementMap.update({
        __BuildingFurniture.name() : __BuildingFurniture
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'InteriorFurniturePropertyType', InteriorFurniturePropertyType)


# Complex type {http://www.opengis.net/citygml/building/1.0}BuildingType with content type ELEMENT_ONLY
class BuildingType (AbstractBuildingType):
    """Complex type {http://www.opengis.net/citygml/building/1.0}BuildingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 117, 4)
    _ElementMap = AbstractBuildingType._ElementMap.copy()
    _AttributeMap = AbstractBuildingType._AttributeMap.copy()
    # Base type is AbstractBuildingType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfSite ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfSite) inherited from {http://www.opengis.net/citygml/1.0}AbstractSiteType
    
    # Element class_ ({http://www.opengis.net/citygml/building/1.0}class) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element function ({http://www.opengis.net/citygml/building/1.0}function) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element usage ({http://www.opengis.net/citygml/building/1.0}usage) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element yearOfConstruction ({http://www.opengis.net/citygml/building/1.0}yearOfConstruction) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element yearOfDemolition ({http://www.opengis.net/citygml/building/1.0}yearOfDemolition) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element roofType ({http://www.opengis.net/citygml/building/1.0}roofType) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element measuredHeight ({http://www.opengis.net/citygml/building/1.0}measuredHeight) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element storeysAboveGround ({http://www.opengis.net/citygml/building/1.0}storeysAboveGround) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element storeysBelowGround ({http://www.opengis.net/citygml/building/1.0}storeysBelowGround) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element storeyHeightsAboveGround ({http://www.opengis.net/citygml/building/1.0}storeyHeightsAboveGround) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element storeyHeightsBelowGround ({http://www.opengis.net/citygml/building/1.0}storeyHeightsBelowGround) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod1Solid ({http://www.opengis.net/citygml/building/1.0}lod1Solid) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod1MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod1MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod1TerrainIntersection ({http://www.opengis.net/citygml/building/1.0}lod1TerrainIntersection) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod2Solid ({http://www.opengis.net/citygml/building/1.0}lod2Solid) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod2MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod2MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod2MultiCurve ({http://www.opengis.net/citygml/building/1.0}lod2MultiCurve) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod2TerrainIntersection ({http://www.opengis.net/citygml/building/1.0}lod2TerrainIntersection) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element outerBuildingInstallation ({http://www.opengis.net/citygml/building/1.0}outerBuildingInstallation) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element interiorBuildingInstallation ({http://www.opengis.net/citygml/building/1.0}interiorBuildingInstallation) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element boundedBy_ ({http://www.opengis.net/citygml/building/1.0}boundedBy) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod3Solid ({http://www.opengis.net/citygml/building/1.0}lod3Solid) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod3MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod3MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod3MultiCurve ({http://www.opengis.net/citygml/building/1.0}lod3MultiCurve) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod3TerrainIntersection ({http://www.opengis.net/citygml/building/1.0}lod3TerrainIntersection) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod4Solid ({http://www.opengis.net/citygml/building/1.0}lod4Solid) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod4MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod4MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod4MultiCurve ({http://www.opengis.net/citygml/building/1.0}lod4MultiCurve) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod4TerrainIntersection ({http://www.opengis.net/citygml/building/1.0}lod4TerrainIntersection) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element interiorRoom ({http://www.opengis.net/citygml/building/1.0}interiorRoom) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element consistsOfBuildingPart ({http://www.opengis.net/citygml/building/1.0}consistsOfBuildingPart) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element address ({http://www.opengis.net/citygml/building/1.0}address) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element GenericApplicationPropertyOfAbstractBuilding ({http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfAbstractBuilding) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfBuilding uses Python identifier GenericApplicationPropertyOfBuilding
    __GenericApplicationPropertyOfBuilding = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuilding'), 'GenericApplicationPropertyOfBuilding', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfBuilding', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 129, 4), )

    
    GenericApplicationPropertyOfBuilding = property(__GenericApplicationPropertyOfBuilding.value, __GenericApplicationPropertyOfBuilding.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfBuilding.name() : __GenericApplicationPropertyOfBuilding
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BuildingType', BuildingType)


# Complex type {http://www.opengis.net/citygml/building/1.0}BuildingPartType with content type ELEMENT_ONLY
class BuildingPartType (AbstractBuildingType):
    """Complex type {http://www.opengis.net/citygml/building/1.0}BuildingPartType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingPartType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 131, 4)
    _ElementMap = AbstractBuildingType._ElementMap.copy()
    _AttributeMap = AbstractBuildingType._AttributeMap.copy()
    # Base type is AbstractBuildingType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfSite ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfSite) inherited from {http://www.opengis.net/citygml/1.0}AbstractSiteType
    
    # Element class_ ({http://www.opengis.net/citygml/building/1.0}class) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element function ({http://www.opengis.net/citygml/building/1.0}function) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element usage ({http://www.opengis.net/citygml/building/1.0}usage) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element yearOfConstruction ({http://www.opengis.net/citygml/building/1.0}yearOfConstruction) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element yearOfDemolition ({http://www.opengis.net/citygml/building/1.0}yearOfDemolition) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element roofType ({http://www.opengis.net/citygml/building/1.0}roofType) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element measuredHeight ({http://www.opengis.net/citygml/building/1.0}measuredHeight) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element storeysAboveGround ({http://www.opengis.net/citygml/building/1.0}storeysAboveGround) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element storeysBelowGround ({http://www.opengis.net/citygml/building/1.0}storeysBelowGround) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element storeyHeightsAboveGround ({http://www.opengis.net/citygml/building/1.0}storeyHeightsAboveGround) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element storeyHeightsBelowGround ({http://www.opengis.net/citygml/building/1.0}storeyHeightsBelowGround) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod1Solid ({http://www.opengis.net/citygml/building/1.0}lod1Solid) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod1MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod1MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod1TerrainIntersection ({http://www.opengis.net/citygml/building/1.0}lod1TerrainIntersection) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod2Solid ({http://www.opengis.net/citygml/building/1.0}lod2Solid) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod2MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod2MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod2MultiCurve ({http://www.opengis.net/citygml/building/1.0}lod2MultiCurve) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod2TerrainIntersection ({http://www.opengis.net/citygml/building/1.0}lod2TerrainIntersection) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element outerBuildingInstallation ({http://www.opengis.net/citygml/building/1.0}outerBuildingInstallation) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element interiorBuildingInstallation ({http://www.opengis.net/citygml/building/1.0}interiorBuildingInstallation) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element boundedBy_ ({http://www.opengis.net/citygml/building/1.0}boundedBy) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod3Solid ({http://www.opengis.net/citygml/building/1.0}lod3Solid) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod3MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod3MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod3MultiCurve ({http://www.opengis.net/citygml/building/1.0}lod3MultiCurve) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod3TerrainIntersection ({http://www.opengis.net/citygml/building/1.0}lod3TerrainIntersection) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod4Solid ({http://www.opengis.net/citygml/building/1.0}lod4Solid) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod4MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod4MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod4MultiCurve ({http://www.opengis.net/citygml/building/1.0}lod4MultiCurve) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element lod4TerrainIntersection ({http://www.opengis.net/citygml/building/1.0}lod4TerrainIntersection) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element interiorRoom ({http://www.opengis.net/citygml/building/1.0}interiorRoom) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element consistsOfBuildingPart ({http://www.opengis.net/citygml/building/1.0}consistsOfBuildingPart) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element address ({http://www.opengis.net/citygml/building/1.0}address) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element GenericApplicationPropertyOfAbstractBuilding ({http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfAbstractBuilding) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBuildingType
    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfBuildingPart uses Python identifier GenericApplicationPropertyOfBuildingPart
    __GenericApplicationPropertyOfBuildingPart = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuildingPart'), 'GenericApplicationPropertyOfBuildingPart', '__httpwww_opengis_netcitygmlbuilding1_0_BuildingPartType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfBuildingPart', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 143, 4), )

    
    GenericApplicationPropertyOfBuildingPart = property(__GenericApplicationPropertyOfBuildingPart.value, __GenericApplicationPropertyOfBuildingPart.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfBuildingPart.name() : __GenericApplicationPropertyOfBuildingPart
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BuildingPartType', BuildingPartType)


# Complex type {http://www.opengis.net/citygml/building/1.0}RoofSurfaceType with content type ELEMENT_ONLY
class RoofSurfaceType (AbstractBoundarySurfaceType):
    """Complex type {http://www.opengis.net/citygml/building/1.0}RoofSurfaceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoofSurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 314, 4)
    _ElementMap = AbstractBoundarySurfaceType._ElementMap.copy()
    _AttributeMap = AbstractBoundarySurfaceType._AttributeMap.copy()
    # Base type is AbstractBoundarySurfaceType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element lod2MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod2MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod3MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod3MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod4MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod4MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element opening ({http://www.opengis.net/citygml/building/1.0}opening) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element GenericApplicationPropertyOfBoundarySurface ({http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfBoundarySurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfRoofSurface uses Python identifier GenericApplicationPropertyOfRoofSurface
    __GenericApplicationPropertyOfRoofSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfRoofSurface'), 'GenericApplicationPropertyOfRoofSurface', '__httpwww_opengis_netcitygmlbuilding1_0_RoofSurfaceType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfRoofSurface', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 326, 4), )

    
    GenericApplicationPropertyOfRoofSurface = property(__GenericApplicationPropertyOfRoofSurface.value, __GenericApplicationPropertyOfRoofSurface.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfRoofSurface.name() : __GenericApplicationPropertyOfRoofSurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RoofSurfaceType', RoofSurfaceType)


# Complex type {http://www.opengis.net/citygml/building/1.0}WallSurfaceType with content type ELEMENT_ONLY
class WallSurfaceType (AbstractBoundarySurfaceType):
    """Complex type {http://www.opengis.net/citygml/building/1.0}WallSurfaceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WallSurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 328, 4)
    _ElementMap = AbstractBoundarySurfaceType._ElementMap.copy()
    _AttributeMap = AbstractBoundarySurfaceType._AttributeMap.copy()
    # Base type is AbstractBoundarySurfaceType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element lod2MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod2MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod3MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod3MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod4MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod4MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element opening ({http://www.opengis.net/citygml/building/1.0}opening) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element GenericApplicationPropertyOfBoundarySurface ({http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfBoundarySurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfWallSurface uses Python identifier GenericApplicationPropertyOfWallSurface
    __GenericApplicationPropertyOfWallSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWallSurface'), 'GenericApplicationPropertyOfWallSurface', '__httpwww_opengis_netcitygmlbuilding1_0_WallSurfaceType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfWallSurface', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 340, 4), )

    
    GenericApplicationPropertyOfWallSurface = property(__GenericApplicationPropertyOfWallSurface.value, __GenericApplicationPropertyOfWallSurface.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfWallSurface.name() : __GenericApplicationPropertyOfWallSurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'WallSurfaceType', WallSurfaceType)


# Complex type {http://www.opengis.net/citygml/building/1.0}GroundSurfaceType with content type ELEMENT_ONLY
class GroundSurfaceType (AbstractBoundarySurfaceType):
    """Complex type {http://www.opengis.net/citygml/building/1.0}GroundSurfaceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroundSurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 342, 4)
    _ElementMap = AbstractBoundarySurfaceType._ElementMap.copy()
    _AttributeMap = AbstractBoundarySurfaceType._AttributeMap.copy()
    # Base type is AbstractBoundarySurfaceType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element lod2MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod2MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod3MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod3MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod4MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod4MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element opening ({http://www.opengis.net/citygml/building/1.0}opening) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element GenericApplicationPropertyOfBoundarySurface ({http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfBoundarySurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfGroundSurface uses Python identifier GenericApplicationPropertyOfGroundSurface
    __GenericApplicationPropertyOfGroundSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfGroundSurface'), 'GenericApplicationPropertyOfGroundSurface', '__httpwww_opengis_netcitygmlbuilding1_0_GroundSurfaceType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfGroundSurface', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 354, 4), )

    
    GenericApplicationPropertyOfGroundSurface = property(__GenericApplicationPropertyOfGroundSurface.value, __GenericApplicationPropertyOfGroundSurface.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfGroundSurface.name() : __GenericApplicationPropertyOfGroundSurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GroundSurfaceType', GroundSurfaceType)


# Complex type {http://www.opengis.net/citygml/building/1.0}ClosureSurfaceType with content type ELEMENT_ONLY
class ClosureSurfaceType (AbstractBoundarySurfaceType):
    """Complex type {http://www.opengis.net/citygml/building/1.0}ClosureSurfaceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ClosureSurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 356, 4)
    _ElementMap = AbstractBoundarySurfaceType._ElementMap.copy()
    _AttributeMap = AbstractBoundarySurfaceType._AttributeMap.copy()
    # Base type is AbstractBoundarySurfaceType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element lod2MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod2MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod3MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod3MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod4MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod4MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element opening ({http://www.opengis.net/citygml/building/1.0}opening) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element GenericApplicationPropertyOfBoundarySurface ({http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfBoundarySurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfClosureSurface uses Python identifier GenericApplicationPropertyOfClosureSurface
    __GenericApplicationPropertyOfClosureSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfClosureSurface'), 'GenericApplicationPropertyOfClosureSurface', '__httpwww_opengis_netcitygmlbuilding1_0_ClosureSurfaceType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfClosureSurface', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 368, 4), )

    
    GenericApplicationPropertyOfClosureSurface = property(__GenericApplicationPropertyOfClosureSurface.value, __GenericApplicationPropertyOfClosureSurface.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfClosureSurface.name() : __GenericApplicationPropertyOfClosureSurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ClosureSurfaceType', ClosureSurfaceType)


# Complex type {http://www.opengis.net/citygml/building/1.0}FloorSurfaceType with content type ELEMENT_ONLY
class FloorSurfaceType (AbstractBoundarySurfaceType):
    """Complex type {http://www.opengis.net/citygml/building/1.0}FloorSurfaceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FloorSurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 372, 4)
    _ElementMap = AbstractBoundarySurfaceType._ElementMap.copy()
    _AttributeMap = AbstractBoundarySurfaceType._AttributeMap.copy()
    # Base type is AbstractBoundarySurfaceType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element lod2MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod2MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod3MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod3MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod4MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod4MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element opening ({http://www.opengis.net/citygml/building/1.0}opening) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element GenericApplicationPropertyOfBoundarySurface ({http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfBoundarySurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfFloorSurface uses Python identifier GenericApplicationPropertyOfFloorSurface
    __GenericApplicationPropertyOfFloorSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfFloorSurface'), 'GenericApplicationPropertyOfFloorSurface', '__httpwww_opengis_netcitygmlbuilding1_0_FloorSurfaceType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfFloorSurface', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 384, 4), )

    
    GenericApplicationPropertyOfFloorSurface = property(__GenericApplicationPropertyOfFloorSurface.value, __GenericApplicationPropertyOfFloorSurface.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfFloorSurface.name() : __GenericApplicationPropertyOfFloorSurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'FloorSurfaceType', FloorSurfaceType)


# Complex type {http://www.opengis.net/citygml/building/1.0}InteriorWallSurfaceType with content type ELEMENT_ONLY
class InteriorWallSurfaceType (AbstractBoundarySurfaceType):
    """Complex type {http://www.opengis.net/citygml/building/1.0}InteriorWallSurfaceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InteriorWallSurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 386, 4)
    _ElementMap = AbstractBoundarySurfaceType._ElementMap.copy()
    _AttributeMap = AbstractBoundarySurfaceType._AttributeMap.copy()
    # Base type is AbstractBoundarySurfaceType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element lod2MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod2MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod3MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod3MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod4MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod4MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element opening ({http://www.opengis.net/citygml/building/1.0}opening) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element GenericApplicationPropertyOfBoundarySurface ({http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfBoundarySurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfInteriorWallSurface uses Python identifier GenericApplicationPropertyOfInteriorWallSurface
    __GenericApplicationPropertyOfInteriorWallSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfInteriorWallSurface'), 'GenericApplicationPropertyOfInteriorWallSurface', '__httpwww_opengis_netcitygmlbuilding1_0_InteriorWallSurfaceType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfInteriorWallSurface', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 398, 4), )

    
    GenericApplicationPropertyOfInteriorWallSurface = property(__GenericApplicationPropertyOfInteriorWallSurface.value, __GenericApplicationPropertyOfInteriorWallSurface.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfInteriorWallSurface.name() : __GenericApplicationPropertyOfInteriorWallSurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'InteriorWallSurfaceType', InteriorWallSurfaceType)


# Complex type {http://www.opengis.net/citygml/building/1.0}CeilingSurfaceType with content type ELEMENT_ONLY
class CeilingSurfaceType (AbstractBoundarySurfaceType):
    """Complex type {http://www.opengis.net/citygml/building/1.0}CeilingSurfaceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CeilingSurfaceType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 400, 4)
    _ElementMap = AbstractBoundarySurfaceType._ElementMap.copy()
    _AttributeMap = AbstractBoundarySurfaceType._AttributeMap.copy()
    # Base type is AbstractBoundarySurfaceType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element lod2MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod2MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod3MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod3MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element lod4MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod4MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element opening ({http://www.opengis.net/citygml/building/1.0}opening) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element GenericApplicationPropertyOfBoundarySurface ({http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfBoundarySurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractBoundarySurfaceType
    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfCeilingSurface uses Python identifier GenericApplicationPropertyOfCeilingSurface
    __GenericApplicationPropertyOfCeilingSurface = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCeilingSurface'), 'GenericApplicationPropertyOfCeilingSurface', '__httpwww_opengis_netcitygmlbuilding1_0_CeilingSurfaceType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfCeilingSurface', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 412, 4), )

    
    GenericApplicationPropertyOfCeilingSurface = property(__GenericApplicationPropertyOfCeilingSurface.value, __GenericApplicationPropertyOfCeilingSurface.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfCeilingSurface.name() : __GenericApplicationPropertyOfCeilingSurface
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CeilingSurfaceType', CeilingSurfaceType)


# Complex type {http://www.opengis.net/citygml/building/1.0}WindowType with content type ELEMENT_ONLY
class WindowType (AbstractOpeningType):
    """ Type for windows in walls. Used in LOD3 and LOD4 only . As subclass of _CityObject, a window
                inherits all attributes and relations, in particular an id, names, external references, and generalization
                relations. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WindowType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 472, 4)
    _ElementMap = AbstractOpeningType._ElementMap.copy()
    _AttributeMap = AbstractOpeningType._AttributeMap.copy()
    # Base type is AbstractOpeningType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element lod3MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod3MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractOpeningType
    
    # Element lod4MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod4MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractOpeningType
    
    # Element GenericApplicationPropertyOfOpening ({http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfOpening) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractOpeningType
    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfWindow uses Python identifier GenericApplicationPropertyOfWindow
    __GenericApplicationPropertyOfWindow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWindow'), 'GenericApplicationPropertyOfWindow', '__httpwww_opengis_netcitygmlbuilding1_0_WindowType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfWindow', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 489, 4), )

    
    GenericApplicationPropertyOfWindow = property(__GenericApplicationPropertyOfWindow.value, __GenericApplicationPropertyOfWindow.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfWindow.name() : __GenericApplicationPropertyOfWindow
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'WindowType', WindowType)


# Complex type {http://www.opengis.net/citygml/building/1.0}DoorType with content type ELEMENT_ONLY
class DoorType (AbstractOpeningType):
    """ Type for doors in walls. Used in LOD3 and LOD4 only . As subclass of _CityObject, a Door inherits
                all attributes and relations, in particular an id, names, external references, and generalization relations.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DoorType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 491, 4)
    _ElementMap = AbstractOpeningType._ElementMap.copy()
    _AttributeMap = AbstractOpeningType._AttributeMap.copy()
    # Base type is AbstractOpeningType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element lod3MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod3MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractOpeningType
    
    # Element lod4MultiSurface ({http://www.opengis.net/citygml/building/1.0}lod4MultiSurface) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractOpeningType
    
    # Element GenericApplicationPropertyOfOpening ({http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfOpening) inherited from {http://www.opengis.net/citygml/building/1.0}AbstractOpeningType
    
    # Element {http://www.opengis.net/citygml/building/1.0}address uses Python identifier address
    __address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'address'), 'address', '__httpwww_opengis_netcitygmlbuilding1_0_DoorType_httpwww_opengis_netcitygmlbuilding1_0address', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 500, 20), )

    
    address = property(__address.value, __address.set, None, None)

    
    # Element {http://www.opengis.net/citygml/building/1.0}_GenericApplicationPropertyOfDoor uses Python identifier GenericApplicationPropertyOfDoor
    __GenericApplicationPropertyOfDoor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfDoor'), 'GenericApplicationPropertyOfDoor', '__httpwww_opengis_netcitygmlbuilding1_0_DoorType_httpwww_opengis_netcitygmlbuilding1_0_GenericApplicationPropertyOfDoor', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 509, 4), )

    
    GenericApplicationPropertyOfDoor = property(__GenericApplicationPropertyOfDoor.value, __GenericApplicationPropertyOfDoor.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __address.name() : __address,
        __GenericApplicationPropertyOfDoor.name() : __GenericApplicationPropertyOfDoor
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DoorType', DoorType)


GenericApplicationPropertyOfAbstractBuilding = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfAbstractBuilding'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 81, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfAbstractBuilding.name().localName(), GenericApplicationPropertyOfAbstractBuilding)

GenericApplicationPropertyOfBuilding = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuilding'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 129, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfBuilding.name().localName(), GenericApplicationPropertyOfBuilding)

GenericApplicationPropertyOfBuildingPart = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuildingPart'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 143, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfBuildingPart.name().localName(), GenericApplicationPropertyOfBuildingPart)

GenericApplicationPropertyOfBuildingInstallation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuildingInstallation'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 184, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfBuildingInstallation.name().localName(), GenericApplicationPropertyOfBuildingInstallation)

GenericApplicationPropertyOfIntBuildingInstallation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfIntBuildingInstallation'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 247, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfIntBuildingInstallation.name().localName(), GenericApplicationPropertyOfIntBuildingInstallation)

GenericApplicationPropertyOfBoundarySurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBoundarySurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 312, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfBoundarySurface.name().localName(), GenericApplicationPropertyOfBoundarySurface)

GenericApplicationPropertyOfRoofSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfRoofSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 326, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfRoofSurface.name().localName(), GenericApplicationPropertyOfRoofSurface)

GenericApplicationPropertyOfWallSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWallSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 340, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfWallSurface.name().localName(), GenericApplicationPropertyOfWallSurface)

GenericApplicationPropertyOfGroundSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfGroundSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 354, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfGroundSurface.name().localName(), GenericApplicationPropertyOfGroundSurface)

GenericApplicationPropertyOfClosureSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfClosureSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 368, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfClosureSurface.name().localName(), GenericApplicationPropertyOfClosureSurface)

GenericApplicationPropertyOfFloorSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfFloorSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 384, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfFloorSurface.name().localName(), GenericApplicationPropertyOfFloorSurface)

GenericApplicationPropertyOfInteriorWallSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfInteriorWallSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 398, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfInteriorWallSurface.name().localName(), GenericApplicationPropertyOfInteriorWallSurface)

GenericApplicationPropertyOfCeilingSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCeilingSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 412, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfCeilingSurface.name().localName(), GenericApplicationPropertyOfCeilingSurface)

GenericApplicationPropertyOfOpening = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfOpening'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 470, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfOpening.name().localName(), GenericApplicationPropertyOfOpening)

GenericApplicationPropertyOfWindow = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWindow'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 489, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfWindow.name().localName(), GenericApplicationPropertyOfWindow)

GenericApplicationPropertyOfDoor = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfDoor'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 509, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfDoor.name().localName(), GenericApplicationPropertyOfDoor)

GenericApplicationPropertyOfRoom = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfRoom'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 543, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfRoom.name().localName(), GenericApplicationPropertyOfRoom)

GenericApplicationPropertyOfBuildingFurniture = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuildingFurniture'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 591, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfBuildingFurniture.name().localName(), GenericApplicationPropertyOfBuildingFurniture)

AbstractBuilding = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_AbstractBuilding'), AbstractBuildingType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 79, 4))
Namespace.addCategoryObject('elementBinding', AbstractBuilding.name().localName(), AbstractBuilding)

BuildingInstallation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BuildingInstallation'), BuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 182, 4))
Namespace.addCategoryObject('elementBinding', BuildingInstallation.name().localName(), BuildingInstallation)

IntBuildingInstallation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IntBuildingInstallation'), IntBuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 245, 4))
Namespace.addCategoryObject('elementBinding', IntBuildingInstallation.name().localName(), IntBuildingInstallation)

BoundarySurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_BoundarySurface'), AbstractBoundarySurfaceType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 310, 4))
Namespace.addCategoryObject('elementBinding', BoundarySurface.name().localName(), BoundarySurface)

Opening = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Opening'), AbstractOpeningType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 468, 4))
Namespace.addCategoryObject('elementBinding', Opening.name().localName(), Opening)

Room = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Room'), RoomType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 541, 4))
Namespace.addCategoryObject('elementBinding', Room.name().localName(), Room)

BuildingFurniture = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BuildingFurniture'), BuildingFurnitureType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 589, 4))
Namespace.addCategoryObject('elementBinding', BuildingFurniture.name().localName(), BuildingFurniture)

Building = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Building'), BuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 127, 4))
Namespace.addCategoryObject('elementBinding', Building.name().localName(), Building)

BuildingPart = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BuildingPart'), BuildingPartType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 141, 4))
Namespace.addCategoryObject('elementBinding', BuildingPart.name().localName(), BuildingPart)

RoofSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RoofSurface'), RoofSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 324, 4))
Namespace.addCategoryObject('elementBinding', RoofSurface.name().localName(), RoofSurface)

WallSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'WallSurface'), WallSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 338, 4))
Namespace.addCategoryObject('elementBinding', WallSurface.name().localName(), WallSurface)

GroundSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GroundSurface'), GroundSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 352, 4))
Namespace.addCategoryObject('elementBinding', GroundSurface.name().localName(), GroundSurface)

ClosureSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ClosureSurface'), ClosureSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 366, 4))
Namespace.addCategoryObject('elementBinding', ClosureSurface.name().localName(), ClosureSurface)

FloorSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FloorSurface'), FloorSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 382, 4))
Namespace.addCategoryObject('elementBinding', FloorSurface.name().localName(), FloorSurface)

InteriorWallSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InteriorWallSurface'), InteriorWallSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 396, 4))
Namespace.addCategoryObject('elementBinding', InteriorWallSurface.name().localName(), InteriorWallSurface)

CeilingSurface = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CeilingSurface'), CeilingSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 410, 4))
Namespace.addCategoryObject('elementBinding', CeilingSurface.name().localName(), CeilingSurface)

Window = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Window'), WindowType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 487, 4))
Namespace.addCategoryObject('elementBinding', Window.name().localName(), Window)

Door = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Door'), DoorType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 507, 4))
Namespace.addCategoryObject('elementBinding', Door.name().localName(), Door)



AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'class'), BuildingClassType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 39, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'function'), BuildingFunctionType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 40, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usage'), BuildingUsageType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 41, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'yearOfConstruction'), pyxb.binding.datatypes.gYear, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 42, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'yearOfDemolition'), pyxb.binding.datatypes.gYear, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 43, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'roofType'), RoofTypeType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 44, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'measuredHeight'), teaser.Data.SchemaBindings.opengis.raw.gml.LengthType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 45, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'storeysAboveGround'), pyxb.binding.datatypes.nonNegativeInteger, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 46, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'storeysBelowGround'), pyxb.binding.datatypes.nonNegativeInteger, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 47, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'storeyHeightsAboveGround'), teaser.Data.SchemaBindings.opengis.raw.gml.MeasureOrNullListType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 48, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'storeyHeightsBelowGround'), teaser.Data.SchemaBindings.opengis.raw.gml.MeasureOrNullListType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 49, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod1Solid'), teaser.Data.SchemaBindings.opengis.raw.gml.SolidPropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 50, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod1MultiSurface'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiSurfacePropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 51, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod1TerrainIntersection'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiCurvePropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 52, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod2Solid'), teaser.Data.SchemaBindings.opengis.raw.gml.SolidPropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 53, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiSurfacePropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 54, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiCurve'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiCurvePropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 55, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod2TerrainIntersection'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiCurvePropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 56, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outerBuildingInstallation'), BuildingInstallationPropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 57, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'interiorBuildingInstallation'), IntBuildingInstallationPropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 59, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'boundedBy'), BoundarySurfacePropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 61, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod3Solid'), teaser.Data.SchemaBindings.opengis.raw.gml.SolidPropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 62, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiSurfacePropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 63, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiCurve'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiCurvePropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 64, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod3TerrainIntersection'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiCurvePropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 65, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4Solid'), teaser.Data.SchemaBindings.opengis.raw.gml.SolidPropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 66, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiSurfacePropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 67, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiCurve'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiCurvePropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 68, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4TerrainIntersection'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiCurvePropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 69, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'interiorRoom'), InteriorRoomPropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 70, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'consistsOfBuildingPart'), BuildingPartPropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 71, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'address'), teaser.Data.SchemaBindings.opengis.citygml.raw.base.AddressPropertyType, scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 72, 20)))

AbstractBuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfAbstractBuilding'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=AbstractBuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 81, 4)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 96, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 39, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 40, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 41, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 42, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 43, 20))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 44, 20))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 45, 20))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 46, 20))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 47, 20))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 48, 20))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 49, 20))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 50, 20))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 51, 20))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 52, 20))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 53, 20))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 54, 20))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 55, 20))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 56, 20))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 57, 20))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 59, 20))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 61, 20))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 62, 20))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 63, 20))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 64, 20))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 65, 20))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 66, 20))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 67, 20))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 68, 20))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 69, 20))
    counters.add(cc_39)
    cc_40 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 70, 20))
    counters.add(cc_40)
    cc_41 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 71, 20))
    counters.add(cc_41)
    cc_42 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 72, 20))
    counters.add(cc_42)
    cc_43 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 73, 20))
    counters.add(cc_43)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfSite')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 96, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'class')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 39, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'function')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 40, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 41, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearOfConstruction')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 42, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearOfDemolition')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 43, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'roofType')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 44, 20))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measuredHeight')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 45, 20))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'storeysAboveGround')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 46, 20))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'storeysBelowGround')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 47, 20))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'storeyHeightsAboveGround')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 48, 20))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'storeyHeightsBelowGround')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 49, 20))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 50, 20))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 51, 20))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 52, 20))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 53, 20))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 54, 20))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiCurve')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 55, 20))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 56, 20))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outerBuildingInstallation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 57, 20))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'interiorBuildingInstallation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 59, 20))
    st_30 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_31, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 61, 20))
    st_31 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_32, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 62, 20))
    st_32 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_33, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 63, 20))
    st_33 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_34, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiCurve')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 64, 20))
    st_34 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_35, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 65, 20))
    st_35 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_36, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 66, 20))
    st_36 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_37, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 67, 20))
    st_37 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_38, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiCurve')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 68, 20))
    st_38 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_39, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 69, 20))
    st_39 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_40, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'interiorRoom')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 70, 20))
    st_40 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_41, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'consistsOfBuildingPart')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 71, 20))
    st_41 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_42, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 72, 20))
    st_42 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_43, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfAbstractBuilding')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 73, 20))
    st_43 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_32, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_38, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_38, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_39, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_39, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_40, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_40, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_41, True) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_41, False) ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_42, True) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_42, False) ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_43, True) ]))
    st_43._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractBuildingType._Automaton = _BuildAutomaton()




BuildingPartPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BuildingPart'), BuildingPartType, scope=BuildingPartPropertyType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 141, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 153, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BuildingPart')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 154, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BuildingPartPropertyType._Automaton = _BuildAutomaton_()




BuildingInstallationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'class'), BuildingInstallationClassType, scope=BuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 170, 20)))

BuildingInstallationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'function'), BuildingInstallationFunctionType, scope=BuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 171, 20)))

BuildingInstallationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usage'), BuildingInstallationUsageType, scope=BuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 172, 20)))

BuildingInstallationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod2Geometry'), teaser.Data.SchemaBindings.opengis.raw.gml.GeometryPropertyType, scope=BuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 173, 20)))

BuildingInstallationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod3Geometry'), teaser.Data.SchemaBindings.opengis.raw.gml.GeometryPropertyType, scope=BuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 174, 20)))

BuildingInstallationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4Geometry'), teaser.Data.SchemaBindings.opengis.raw.gml.GeometryPropertyType, scope=BuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 175, 20)))

BuildingInstallationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuildingInstallation'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=BuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 184, 4)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 170, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 171, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 172, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 173, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 174, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 175, 20))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 176, 20))
    counters.add(cc_16)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'class')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 170, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'function')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 171, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 172, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2Geometry')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 173, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3Geometry')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 174, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Geometry')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 175, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuildingInstallation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 176, 20))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    st_16._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BuildingInstallationType._Automaton = _BuildAutomaton_2()




BuildingInstallationPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BuildingInstallation'), BuildingInstallationType, scope=BuildingInstallationPropertyType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 182, 4)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 218, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BuildingInstallationPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BuildingInstallation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 219, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BuildingInstallationPropertyType._Automaton = _BuildAutomaton_3()




IntBuildingInstallationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'class'), IntBuildingInstallationClassType, scope=IntBuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 235, 20)))

IntBuildingInstallationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'function'), IntBuildingInstallationFunctionType, scope=IntBuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 236, 20)))

IntBuildingInstallationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usage'), IntBuildingInstallationUsageType, scope=IntBuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 237, 20)))

IntBuildingInstallationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4Geometry'), teaser.Data.SchemaBindings.opengis.raw.gml.GeometryPropertyType, scope=IntBuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 238, 20)))

IntBuildingInstallationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfIntBuildingInstallation'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=IntBuildingInstallationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 247, 4)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 235, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 236, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 237, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 238, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 239, 20))
    counters.add(cc_14)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'class')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 235, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'function')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 236, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 237, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Geometry')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 238, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfIntBuildingInstallation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 239, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IntBuildingInstallationType._Automaton = _BuildAutomaton_4()




IntBuildingInstallationPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'IntBuildingInstallation'), IntBuildingInstallationType, scope=IntBuildingInstallationPropertyType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 245, 4)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 281, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(IntBuildingInstallationPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'IntBuildingInstallation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 282, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
IntBuildingInstallationPropertyType._Automaton = _BuildAutomaton_5()




AbstractBoundarySurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiSurfacePropertyType, scope=AbstractBoundarySurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20)))

AbstractBoundarySurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiSurfacePropertyType, scope=AbstractBoundarySurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20)))

AbstractBoundarySurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiSurfacePropertyType, scope=AbstractBoundarySurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20)))

AbstractBoundarySurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'opening'), OpeningPropertyType, scope=AbstractBoundarySurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20)))

AbstractBoundarySurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBoundarySurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=AbstractBoundarySurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 312, 4)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    counters.add(cc_14)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opening')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(AbstractBoundarySurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBoundarySurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractBoundarySurfaceType._Automaton = _BuildAutomaton_6()




BoundarySurfacePropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_BoundarySurface'), AbstractBoundarySurfaceType, abstract=pyxb.binding.datatypes.boolean(1), scope=BoundarySurfacePropertyType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 310, 4)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 427, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BoundarySurfacePropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_BoundarySurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 428, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BoundarySurfacePropertyType._Automaton = _BuildAutomaton_7()




OpeningPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Opening'), AbstractOpeningType, abstract=pyxb.binding.datatypes.boolean(1), scope=OpeningPropertyType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 468, 4)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 444, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OpeningPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_Opening')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 445, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
OpeningPropertyType._Automaton = _BuildAutomaton_8()




AbstractOpeningType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiSurfacePropertyType, scope=AbstractOpeningType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 460, 20)))

AbstractOpeningType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiSurfacePropertyType, scope=AbstractOpeningType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 461, 20)))

AbstractOpeningType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfOpening'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=AbstractOpeningType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 470, 4)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 460, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 461, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 462, 20))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 460, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 461, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(AbstractOpeningType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfOpening')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 462, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractOpeningType._Automaton = _BuildAutomaton_9()




RoomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'class'), RoomClassType, scope=RoomType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 526, 20)))

RoomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'function'), RoomFunctionType, scope=RoomType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 527, 20)))

RoomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usage'), RoomUsageType, scope=RoomType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 528, 20)))

RoomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4Solid'), teaser.Data.SchemaBindings.opengis.raw.gml.SolidPropertyType, scope=RoomType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 529, 20)))

RoomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiSurfacePropertyType, scope=RoomType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 530, 20)))

RoomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'boundedBy'), BoundarySurfacePropertyType, scope=RoomType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 531, 20)))

RoomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'interiorFurniture'), InteriorFurniturePropertyType, scope=RoomType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 532, 20)))

RoomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'roomInstallation'), IntBuildingInstallationPropertyType, scope=RoomType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 533, 20)))

RoomType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfRoom'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=RoomType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 543, 4)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 526, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 527, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 528, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 529, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 530, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 531, 20))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 532, 20))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 533, 20))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 535, 20))
    counters.add(cc_18)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'class')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 526, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'function')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 527, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 528, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 529, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 530, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 531, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'interiorFurniture')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 532, 20))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'roomInstallation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 533, 20))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(RoomType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfRoom')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 535, 20))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    st_18._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RoomType._Automaton = _BuildAutomaton_10()




BuildingFurnitureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'class'), BuildingFurnitureClassType, scope=BuildingFurnitureType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 578, 20)))

BuildingFurnitureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'function'), BuildingFurnitureFunctionType, scope=BuildingFurnitureType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 579, 20)))

BuildingFurnitureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usage'), BuildingFurnitureUsageType, scope=BuildingFurnitureType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 580, 20)))

BuildingFurnitureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4Geometry'), teaser.Data.SchemaBindings.opengis.raw.gml.GeometryPropertyType, scope=BuildingFurnitureType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 581, 20)))

BuildingFurnitureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4ImplicitRepresentation'), teaser.Data.SchemaBindings.opengis.citygml.raw.base.ImplicitRepresentationPropertyType, scope=BuildingFurnitureType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 582, 20)))

BuildingFurnitureType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuildingFurniture'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=BuildingFurnitureType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 591, 4)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 578, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 579, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 580, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 581, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 582, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 583, 20))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'class')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 578, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'function')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 579, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 580, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Geometry')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 581, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4ImplicitRepresentation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 582, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(BuildingFurnitureType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuildingFurniture')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 583, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BuildingFurnitureType._Automaton = _BuildAutomaton_11()




InteriorRoomPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Room'), RoomType, scope=InteriorRoomPropertyType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 541, 4)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 627, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InteriorRoomPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Room')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 628, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InteriorRoomPropertyType._Automaton = _BuildAutomaton_12()




InteriorFurniturePropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BuildingFurniture'), BuildingFurnitureType, scope=InteriorFurniturePropertyType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 589, 4)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 642, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InteriorFurniturePropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BuildingFurniture')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 643, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InteriorFurniturePropertyType._Automaton = _BuildAutomaton_13()




BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuilding'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=BuildingType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 129, 4)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 96, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 39, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 40, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 41, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 42, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 43, 20))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 44, 20))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 45, 20))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 46, 20))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 47, 20))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 48, 20))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 49, 20))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 50, 20))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 51, 20))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 52, 20))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 53, 20))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 54, 20))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 55, 20))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 56, 20))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 57, 20))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 59, 20))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 61, 20))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 62, 20))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 63, 20))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 64, 20))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 65, 20))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 66, 20))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 67, 20))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 68, 20))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 69, 20))
    counters.add(cc_39)
    cc_40 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 70, 20))
    counters.add(cc_40)
    cc_41 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 71, 20))
    counters.add(cc_41)
    cc_42 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 72, 20))
    counters.add(cc_42)
    cc_43 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 73, 20))
    counters.add(cc_43)
    cc_44 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 121, 20))
    counters.add(cc_44)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfSite')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 96, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'class')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 39, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'function')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 40, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 41, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearOfConstruction')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 42, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearOfDemolition')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 43, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'roofType')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 44, 20))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measuredHeight')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 45, 20))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'storeysAboveGround')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 46, 20))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'storeysBelowGround')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 47, 20))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'storeyHeightsAboveGround')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 48, 20))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'storeyHeightsBelowGround')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 49, 20))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 50, 20))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 51, 20))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 52, 20))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 53, 20))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 54, 20))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiCurve')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 55, 20))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 56, 20))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outerBuildingInstallation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 57, 20))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'interiorBuildingInstallation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 59, 20))
    st_30 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_31, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 61, 20))
    st_31 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_32, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 62, 20))
    st_32 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_33, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 63, 20))
    st_33 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_34, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiCurve')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 64, 20))
    st_34 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_35, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 65, 20))
    st_35 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_36, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 66, 20))
    st_36 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_37, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 67, 20))
    st_37 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_38, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiCurve')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 68, 20))
    st_38 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_39, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 69, 20))
    st_39 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_40, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'interiorRoom')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 70, 20))
    st_40 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_41, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'consistsOfBuildingPart')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 71, 20))
    st_41 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_42, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 72, 20))
    st_42 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_43, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfAbstractBuilding')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 73, 20))
    st_43 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_44, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuilding')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 121, 20))
    st_44 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_44)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_32, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_38, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_38, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_39, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_39, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_40, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_40, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_41, True) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_41, False) ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_42, True) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_42, False) ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_43, True) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_43, False) ]))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_44, True) ]))
    st_44._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BuildingType._Automaton = _BuildAutomaton_14()




BuildingPartType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuildingPart'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=BuildingPartType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 143, 4)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 96, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 39, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 40, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 41, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 42, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 43, 20))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 44, 20))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 45, 20))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 46, 20))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 47, 20))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 48, 20))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 49, 20))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 50, 20))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 51, 20))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 52, 20))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 53, 20))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 54, 20))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 55, 20))
    counters.add(cc_27)
    cc_28 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 56, 20))
    counters.add(cc_28)
    cc_29 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 57, 20))
    counters.add(cc_29)
    cc_30 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 59, 20))
    counters.add(cc_30)
    cc_31 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 61, 20))
    counters.add(cc_31)
    cc_32 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 62, 20))
    counters.add(cc_32)
    cc_33 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 63, 20))
    counters.add(cc_33)
    cc_34 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 64, 20))
    counters.add(cc_34)
    cc_35 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 65, 20))
    counters.add(cc_35)
    cc_36 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 66, 20))
    counters.add(cc_36)
    cc_37 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 67, 20))
    counters.add(cc_37)
    cc_38 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 68, 20))
    counters.add(cc_38)
    cc_39 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 69, 20))
    counters.add(cc_39)
    cc_40 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 70, 20))
    counters.add(cc_40)
    cc_41 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 71, 20))
    counters.add(cc_41)
    cc_42 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 72, 20))
    counters.add(cc_42)
    cc_43 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 73, 20))
    counters.add(cc_43)
    cc_44 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 135, 20))
    counters.add(cc_44)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfSite')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 96, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'class')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 39, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'function')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 40, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 41, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearOfConstruction')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 42, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearOfDemolition')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 43, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'roofType')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 44, 20))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'measuredHeight')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 45, 20))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'storeysAboveGround')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 46, 20))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'storeysBelowGround')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 47, 20))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'storeyHeightsAboveGround')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 48, 20))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'storeyHeightsBelowGround')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 49, 20))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 50, 20))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 51, 20))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 52, 20))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 53, 20))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 54, 20))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiCurve')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 55, 20))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_28, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 56, 20))
    st_28 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_28)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_29, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outerBuildingInstallation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 57, 20))
    st_29 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_29)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_30, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'interiorBuildingInstallation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 59, 20))
    st_30 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_30)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_31, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 61, 20))
    st_31 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_31)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_32, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 62, 20))
    st_32 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_32)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_33, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 63, 20))
    st_33 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_33)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_34, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiCurve')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 64, 20))
    st_34 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_34)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_35, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 65, 20))
    st_35 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_35)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_36, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Solid')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 66, 20))
    st_36 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_36)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_37, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 67, 20))
    st_37 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_37)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_38, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiCurve')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 68, 20))
    st_38 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_38)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_39, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 69, 20))
    st_39 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_39)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_40, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'interiorRoom')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 70, 20))
    st_40 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_40)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_41, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'consistsOfBuildingPart')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 71, 20))
    st_41 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_41)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_42, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 72, 20))
    st_42 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_42)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_43, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfAbstractBuilding')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 73, 20))
    st_43 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_43)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_44, False))
    symbol = pyxb.binding.content.ElementUse(BuildingPartType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBuildingPart')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 135, 20))
    st_44 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_44)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_14, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_15, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_15, False) ]))
    st_15._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_16, [
        fac.UpdateInstruction(cc_16, True) ]))
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_16, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_16, False) ]))
    st_16._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_17, [
        fac.UpdateInstruction(cc_17, True) ]))
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_17, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_17, False) ]))
    st_17._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_18, [
        fac.UpdateInstruction(cc_18, True) ]))
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_18, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_18, False) ]))
    st_18._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_19, [
        fac.UpdateInstruction(cc_19, True) ]))
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_19, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_19, False) ]))
    st_19._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_20, [
        fac.UpdateInstruction(cc_20, True) ]))
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_20, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_20, False) ]))
    st_20._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_21, [
        fac.UpdateInstruction(cc_21, True) ]))
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_21, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_21, False) ]))
    st_21._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_22, [
        fac.UpdateInstruction(cc_22, True) ]))
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_22, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_22, False) ]))
    st_22._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_23, [
        fac.UpdateInstruction(cc_23, True) ]))
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_23, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_23, False) ]))
    st_23._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_24, [
        fac.UpdateInstruction(cc_24, True) ]))
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_24, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_24, False) ]))
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_26, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_27, True) ]))
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_27, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_27, False) ]))
    st_27._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_28, [
        fac.UpdateInstruction(cc_28, True) ]))
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_28, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_28, False) ]))
    st_28._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_29, [
        fac.UpdateInstruction(cc_29, True) ]))
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_29, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_29, False) ]))
    st_29._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_30, [
        fac.UpdateInstruction(cc_30, True) ]))
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_30, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_30, False) ]))
    st_30._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_31, [
        fac.UpdateInstruction(cc_31, True) ]))
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_31, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_31, False) ]))
    st_31._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_32, [
        fac.UpdateInstruction(cc_32, True) ]))
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_32, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_32, False) ]))
    st_32._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_33, [
        fac.UpdateInstruction(cc_33, True) ]))
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_33, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_33, False) ]))
    st_33._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_34, [
        fac.UpdateInstruction(cc_34, True) ]))
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_34, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_34, False) ]))
    st_34._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_35, [
        fac.UpdateInstruction(cc_35, True) ]))
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_35, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_35, False) ]))
    st_35._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_36, [
        fac.UpdateInstruction(cc_36, True) ]))
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_36, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_36, False) ]))
    st_36._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_37, [
        fac.UpdateInstruction(cc_37, True) ]))
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_37, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_37, False) ]))
    st_37._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_38, [
        fac.UpdateInstruction(cc_38, True) ]))
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_38, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_38, False) ]))
    st_38._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_39, [
        fac.UpdateInstruction(cc_39, True) ]))
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_39, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_39, False) ]))
    st_39._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_40, [
        fac.UpdateInstruction(cc_40, True) ]))
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_40, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_40, False) ]))
    st_40._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_41, [
        fac.UpdateInstruction(cc_41, True) ]))
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_41, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_41, False) ]))
    st_41._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_42, [
        fac.UpdateInstruction(cc_42, True) ]))
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_42, False) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_42, False) ]))
    st_42._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_43, [
        fac.UpdateInstruction(cc_43, True) ]))
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_43, False) ]))
    st_43._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_44, [
        fac.UpdateInstruction(cc_44, True) ]))
    st_44._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
BuildingPartType._Automaton = _BuildAutomaton_15()




RoofSurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfRoofSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=RoofSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 326, 4)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 318, 20))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opening')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBoundarySurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(RoofSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfRoofSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 318, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RoofSurfaceType._Automaton = _BuildAutomaton_16()




WallSurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWallSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=WallSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 340, 4)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 332, 20))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opening')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBoundarySurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(WallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWallSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 332, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
WallSurfaceType._Automaton = _BuildAutomaton_17()




GroundSurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfGroundSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=GroundSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 354, 4)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 346, 20))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opening')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBoundarySurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(GroundSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfGroundSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 346, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GroundSurfaceType._Automaton = _BuildAutomaton_18()




ClosureSurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfClosureSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=ClosureSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 368, 4)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 360, 20))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opening')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBoundarySurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(ClosureSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfClosureSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 360, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ClosureSurfaceType._Automaton = _BuildAutomaton_19()




FloorSurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfFloorSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=FloorSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 384, 4)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 376, 20))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opening')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBoundarySurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(FloorSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfFloorSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 376, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FloorSurfaceType._Automaton = _BuildAutomaton_20()




InteriorWallSurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfInteriorWallSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=InteriorWallSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 398, 4)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 390, 20))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opening')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBoundarySurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(InteriorWallSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfInteriorWallSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 390, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
InteriorWallSurfaceType._Automaton = _BuildAutomaton_21()




CeilingSurfaceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCeilingSurface'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=CeilingSurfaceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 412, 4)))

def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 404, 20))
    counters.add(cc_15)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 300, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 301, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 302, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'opening')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 303, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfBoundarySurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 304, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(CeilingSurfaceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCeilingSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 404, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_15, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CeilingSurfaceType._Automaton = _BuildAutomaton_22()




WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWindow'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=WindowType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 489, 4)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 460, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 461, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 462, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 481, 20))
    counters.add(cc_13)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 460, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 461, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfOpening')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 462, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfWindow')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 481, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
WindowType._Automaton = _BuildAutomaton_23()




DoorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'address'), teaser.Data.SchemaBindings.opengis.citygml.raw.base.AddressPropertyType, scope=DoorType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 500, 20)))

DoorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfDoor'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=DoorType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 509, 4)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 460, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 461, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 462, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 500, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 501, 20))
    counters.add(cc_14)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 460, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4MultiSurface')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 461, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfOpening')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 462, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'address')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 500, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfDoor')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/building/1.0/building.xsd', 501, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DoorType._Automaton = _BuildAutomaton_24()


AbstractBuilding._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.citygml.raw.base.Site)

BuildingInstallation._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.citygml.raw.base.CityObject)

IntBuildingInstallation._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.citygml.raw.base.CityObject)

BoundarySurface._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.citygml.raw.base.CityObject)

Opening._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.citygml.raw.base.CityObject)

Room._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.citygml.raw.base.CityObject)

BuildingFurniture._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.citygml.raw.base.CityObject)

Building._setSubstitutionGroup(AbstractBuilding)

BuildingPart._setSubstitutionGroup(AbstractBuilding)

RoofSurface._setSubstitutionGroup(BoundarySurface)

WallSurface._setSubstitutionGroup(BoundarySurface)

GroundSurface._setSubstitutionGroup(BoundarySurface)

ClosureSurface._setSubstitutionGroup(BoundarySurface)

FloorSurface._setSubstitutionGroup(BoundarySurface)

InteriorWallSurface._setSubstitutionGroup(BoundarySurface)

CeilingSurface._setSubstitutionGroup(BoundarySurface)

Window._setSubstitutionGroup(Opening)

Door._setSubstitutionGroup(Opening)
