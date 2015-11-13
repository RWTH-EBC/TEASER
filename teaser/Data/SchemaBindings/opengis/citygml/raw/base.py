# ./pyxb/bundles/opengis/citygml/raw/base.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:258153f9602467400b4189ab02b751cb737afb6c
# Generated 2015-05-04 11:01:54.885062 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace http://www.opengis.net/citygml/1.0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:358713d4-f23c-11e4-89b3-000c29ce1afb')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes
import pyxb.bundles.common.xlink
import teaser.Data.SchemaBindings.opengis.misc.raw.xAL
import teaser.Data.SchemaBindings.opengis.raw.gml

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/citygml/1.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_gml =teaser.Data.SchemaBindings.opengis.raw.gml.Namespace
_Namespace_gml.configureCategories(['typeBinding', 'elementBinding'])
_Namespace = pyxb.bundles.common.xlink.Namespace
_Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xAL = teaser.Data.SchemaBindings.opengis.misc.raw.xAL.Namespace
_Namespace_xAL.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://www.opengis.net/citygml/1.0}doubleBetween0and1
class doubleBetween0and1 (pyxb.binding.datatypes.double):

    """Type for values, which are greater or equal than 0 and less or equal than 1. Used for color
                encoding, for example. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'doubleBetween0and1')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 243, 4)
    _Documentation = 'Type for values, which are greater or equal than 0 and less or equal than 1. Used for color\n                encoding, for example. '
doubleBetween0and1._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=doubleBetween0and1, value=pyxb.binding.datatypes.double(1.0))
doubleBetween0and1._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=doubleBetween0and1, value=pyxb.binding.datatypes.double(0.0))
doubleBetween0and1._InitializeFacetMap(doubleBetween0and1._CF_maxInclusive,
   doubleBetween0and1._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'doubleBetween0and1', doubleBetween0and1)

# List simple type: {http://www.opengis.net/citygml/1.0}TransformationMatrix4x4Type
# superclasses teaser.Data.SchemaBindings.opengis.raw.gml.doubleList
class TransformationMatrix4x4Type (pyxb.binding.basis.STD_list):

    """Used for implicit geometries. The Transformation matrix is a 4 by 4 matrix, thus it must be a list
                with 16 items. The order the matrix element are represented is row-major, i. e. the first 4 elements represent the
                first row, the fifth to the eight element the second row,... """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransformationMatrix4x4Type')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 262, 4)
    _Documentation = 'Used for implicit geometries. The Transformation matrix is a 4 by 4 matrix, thus it must be a list\n                with 16 items. The order the matrix element are represented is row-major, i. e. the first 4 elements represent the\n                first row, the fifth to the eight element the second row,... '

    _ItemType = pyxb.binding.datatypes.double
TransformationMatrix4x4Type._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(16))
TransformationMatrix4x4Type._InitializeFacetMap(TransformationMatrix4x4Type._CF_length)
Namespace.addCategoryObject('typeBinding', 'TransformationMatrix4x4Type', TransformationMatrix4x4Type)

# List simple type: {http://www.opengis.net/citygml/1.0}TransformationMatrix2x2Type
# superclasses teaser.Data.SchemaBindings.opengis.raw.gml.doubleList
class TransformationMatrix2x2Type (pyxb.binding.basis.STD_list):

    """Used for georeferencing. The Transformation matrix is a 2 by 2 matrix, thus it must be a list with 4
                items. The order the matrix element are represented is row-major, i. e. the first 2 elements represent the first
                row, the fifth to the eight element the second row,... """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransformationMatrix2x2Type')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 273, 4)
    _Documentation = 'Used for georeferencing. The Transformation matrix is a 2 by 2 matrix, thus it must be a list with 4\n                items. The order the matrix element are represented is row-major, i. e. the first 2 elements represent the first\n                row, the fifth to the eight element the second row,... '

    _ItemType = pyxb.binding.datatypes.double
TransformationMatrix2x2Type._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(4))
TransformationMatrix2x2Type._InitializeFacetMap(TransformationMatrix2x2Type._CF_length)
Namespace.addCategoryObject('typeBinding', 'TransformationMatrix2x2Type', TransformationMatrix2x2Type)

# List simple type: {http://www.opengis.net/citygml/1.0}TransformationMatrix3x4Type
# superclasses teaser.Data.SchemaBindings.opengis.raw.gml.doubleList
class TransformationMatrix3x4Type (pyxb.binding.basis.STD_list):

    """Used for texture parameterization. The Transformation matrix is a 3 by 4 matrix, thus it must be a
                list with 12 items. The order the matrix element are represented is row-major, i. e. the first 4 elements
                represent the first row, the fifth to the eight element the second row,... """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TransformationMatrix3x4Type')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 284, 4)
    _Documentation = 'Used for texture parameterization. The Transformation matrix is a 3 by 4 matrix, thus it must be a\n                list with 12 items. The order the matrix element are represented is row-major, i. e. the first 4 elements\n                represent the first row, the fifth to the eight element the second row,... '

    _ItemType = pyxb.binding.datatypes.double
TransformationMatrix3x4Type._CF_length = pyxb.binding.facets.CF_length(value=pyxb.binding.datatypes.nonNegativeInteger(12))
TransformationMatrix3x4Type._InitializeFacetMap(TransformationMatrix3x4Type._CF_length)
Namespace.addCategoryObject('typeBinding', 'TransformationMatrix3x4Type', TransformationMatrix3x4Type)

# Atomic simple type: {http://www.opengis.net/citygml/1.0}integerBetween0and4
class integerBetween0and4 (pyxb.binding.datatypes.integer):

    """Type for integer values, which are greater or equal than 0 and less or equal than 4. Used for
                encoding of the LOD number. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'integerBetween0and4')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 295, 4)
    _Documentation = 'Type for integer values, which are greater or equal than 0 and less or equal than 4. Used for\n                encoding of the LOD number. '
integerBetween0and4._CF_maxInclusive = pyxb.binding.facets.CF_maxInclusive(value_datatype=integerBetween0and4, value=pyxb.binding.datatypes.integer(4))
integerBetween0and4._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=integerBetween0and4, value=pyxb.binding.datatypes.integer(0))
integerBetween0and4._InitializeFacetMap(integerBetween0and4._CF_maxInclusive,
   integerBetween0and4._CF_minInclusive)
Namespace.addCategoryObject('typeBinding', 'integerBetween0and4', integerBetween0and4)

# Atomic simple type: {http://www.opengis.net/citygml/1.0}MimeTypeType
class MimeTypeType (pyxb.binding.datatypes.string):

    """MIME type of a geometry in an external library file. MIME types are defined by the IETF (Internet
                Engineering Task Force). The values of this type are defined in the XML file MimeTypeType.xml, according to the
                dictionary concept of GML3. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MimeTypeType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 306, 4)
    _Documentation = 'MIME type of a geometry in an external library file. MIME types are defined by the IETF (Internet\n                Engineering Task Force). The values of this type are defined in the XML file MimeTypeType.xml, according to the\n                dictionary concept of GML3. '
MimeTypeType._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'MimeTypeType', MimeTypeType)

# List simple type: {http://www.opengis.net/citygml/1.0}doubleBetween0and1List
# superclasses pyxb.binding.datatypes.anySimpleType
class doubleBetween0and1List (pyxb.binding.basis.STD_list):

    """List for double values, which are greater or equal than 0 and less or equal than 1. Used for color
                encoding, for example. """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'doubleBetween0and1List')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 254, 4)
    _Documentation = 'List for double values, which are greater or equal than 0 and less or equal than 1. Used for color\n                encoding, for example. '

    _ItemType = doubleBetween0and1
doubleBetween0and1List._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'doubleBetween0and1List', doubleBetween0and1List)

# Complex type {http://www.opengis.net/citygml/1.0}CityModelType with content type ELEMENT_ONLY
class CityModelType (teaser.Data.SchemaBindings.opengis.raw.gml.AbstractFeatureCollectionType):
    """Type describing the "root" element of any city model file. It is a collection whose members are
                restricted to be features of a city model. All features are included as cityObjectMember. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CityModelType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 19, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AbstractFeatureCollectionType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AbstractFeatureCollectionType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AbstractFeatureCollectionType
    
    # Element {http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityModel uses Python identifier GenericApplicationPropertyOfCityModel
    __GenericApplicationPropertyOfCityModel = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityModel'), 'GenericApplicationPropertyOfCityModel', '__httpwww_opengis_netcitygml1_0_CityModelType_httpwww_opengis_netcitygml1_0_GenericApplicationPropertyOfCityModel', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 35, 4), )

    
    GenericApplicationPropertyOfCityModel = property(__GenericApplicationPropertyOfCityModel.value, __GenericApplicationPropertyOfCityModel.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element featureMember ({http://www.opengis.net/gml}featureMember) inherited from {http://www.opengis.net/gml}AbstractFeatureCollectionType
    
    # Element featureMembers ({http://www.opengis.net/gml}featureMembers) inherited from {http://www.opengis.net/gml}AbstractFeatureCollectionType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfCityModel.name() : __GenericApplicationPropertyOfCityModel
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CityModelType', CityModelType)


# Complex type {http://www.opengis.net/citygml/1.0}AbstractCityObjectType with content type ELEMENT_ONLY
class AbstractCityObjectType (teaser.Data.SchemaBindings.opengis.raw.gml.AbstractFeatureType):
    """Type describing the abstract superclass of most CityGML features. Its purpose is to provide a
                creation and a termination date as well as a reference to corresponding objects in other information systems. A
                generalization relation may be used to relate features, which represent the same real-world object in different
                Levels-of-Detail, i.e. a feature and its generalized counterpart(s). The direction of this relation is from the
                feature to the corresponding generalized feature."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractCityObjectType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 43, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AbstractFeatureType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AbstractFeatureType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AbstractFeatureType
    
    # Element {http://www.opengis.net/citygml/1.0}creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'creationDate'), 'creationDate', '__httpwww_opengis_netcitygml1_0_AbstractCityObjectType_httpwww_opengis_netcitygml1_0creationDate', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20), )

    
    creationDate = property(__creationDate.value, __creationDate.set, None, None)

    
    # Element {http://www.opengis.net/citygml/1.0}terminationDate uses Python identifier terminationDate
    __terminationDate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'terminationDate'), 'terminationDate', '__httpwww_opengis_netcitygml1_0_AbstractCityObjectType_httpwww_opengis_netcitygml1_0terminationDate', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20), )

    
    terminationDate = property(__terminationDate.value, __terminationDate.set, None, None)

    
    # Element {http://www.opengis.net/citygml/1.0}externalReference uses Python identifier externalReference
    __externalReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'externalReference'), 'externalReference', '__httpwww_opengis_netcitygml1_0_AbstractCityObjectType_httpwww_opengis_netcitygml1_0externalReference', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20), )

    
    externalReference = property(__externalReference.value, __externalReference.set, None, None)

    
    # Element {http://www.opengis.net/citygml/1.0}generalizesTo uses Python identifier generalizesTo
    __generalizesTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'generalizesTo'), 'generalizesTo', '__httpwww_opengis_netcitygml1_0_AbstractCityObjectType_httpwww_opengis_netcitygml1_0generalizesTo', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20), )

    
    generalizesTo = property(__generalizesTo.value, __generalizesTo.set, None, None)

    
    # Element {http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject uses Python identifier GenericApplicationPropertyOfCityObject
    __GenericApplicationPropertyOfCityObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityObject'), 'GenericApplicationPropertyOfCityObject', '__httpwww_opengis_netcitygml1_0_AbstractCityObjectType_httpwww_opengis_netcitygml1_0_GenericApplicationPropertyOfCityObject', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 82, 4), )

    
    GenericApplicationPropertyOfCityObject = property(__GenericApplicationPropertyOfCityObject.value, __GenericApplicationPropertyOfCityObject.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __creationDate.name() : __creationDate,
        __terminationDate.name() : __terminationDate,
        __externalReference.name() : __externalReference,
        __generalizesTo.name() : __generalizesTo,
        __GenericApplicationPropertyOfCityObject.name() : __GenericApplicationPropertyOfCityObject
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AbstractCityObjectType', AbstractCityObjectType)


# Complex type {http://www.opengis.net/citygml/1.0}GeneralizationRelationType with content type ELEMENT_ONLY
class GeneralizationRelationType (pyxb.binding.basis.complexTypeDefinition):
    """Denotes the relation of a _CityObject to its corresponding _CityObject in higher LOD, i.e. to the
                _CityObjects representing the same real world object in higher LOD. The GeneralizationRelationType element must
                either carry a reference to a _CityObject object or contain a _CityObject object inline, but neither both nor
                none. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GeneralizationRelationType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 108, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/citygml/1.0}_CityObject uses Python identifier CityObject
    __CityObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_CityObject'), 'CityObject', '__httpwww_opengis_netcitygml1_0_GeneralizationRelationType_httpwww_opengis_netcitygml1_0_CityObject', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 64, 4), )

    
    CityObject = property(__CityObject.value, __CityObject.set, None, None)

    
    # Attribute {http://www.opengis.net/gml}remoteSchema uses Python identifier remoteSchema
    __remoteSchema = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_gml, 'remoteSchema'), 'remoteSchema', '__httpwww_opengis_netcitygml1_0_GeneralizationRelationType_httpwww_opengis_netgmlremoteSchema', pyxb.binding.datatypes.anyURI)
    __remoteSchema._DeclarationLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 258, 1)
    __remoteSchema._UseLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 269, 2)
    
    remoteSchema = property(__remoteSchema.value, __remoteSchema.set, None, 'Reference to an XML Schema fragment that specifies the content model of the propertys value. This is in conformance with the XML Schema Section 4.14 Referencing Schemas from Elsewhere.')

    
    # Attribute {http://www.w3.org/1999/xlink}type uses Python identifier type
    __type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'type'), 'type', '__httpwww_opengis_netcitygml1_0_GeneralizationRelationType_httpwww_w3_org1999xlinktype', pyxb.bundles.common.xlink.typeType, fixed=True, unicode_default='simple')
    __type._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 29, 1)
    __type._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 112, 2)
    
    type = property(__type.value, __type.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}href uses Python identifier href
    __href = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'href'), 'href', '__httpwww_opengis_netcitygml1_0_GeneralizationRelationType_httpwww_w3_org1999xlinkhref', pyxb.bundles.common.xlink.hrefType)
    __href._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 42, 1)
    __href._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 113, 2)
    
    href = property(__href.value, __href.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}role uses Python identifier role
    __role = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'role'), 'role', '__httpwww_opengis_netcitygml1_0_GeneralizationRelationType_httpwww_w3_org1999xlinkrole', pyxb.bundles.common.xlink.roleType)
    __role._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 48, 1)
    __role._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 114, 2)
    
    role = property(__role.value, __role.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}arcrole uses Python identifier arcrole
    __arcrole = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'arcrole'), 'arcrole', '__httpwww_opengis_netcitygml1_0_GeneralizationRelationType_httpwww_w3_org1999xlinkarcrole', pyxb.bundles.common.xlink.arcroleType)
    __arcrole._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 56, 1)
    __arcrole._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 115, 2)
    
    arcrole = property(__arcrole.value, __arcrole.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}title uses Python identifier title
    __title = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'title'), 'title', '__httpwww_opengis_netcitygml1_0_GeneralizationRelationType_httpwww_w3_org1999xlinktitle', pyxb.bundles.common.xlink.titleAttrType)
    __title._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 64, 1)
    __title._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 116, 2)
    
    title = property(__title.value, __title.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}show uses Python identifier show
    __show = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'show'), 'show', '__httpwww_opengis_netcitygml1_0_GeneralizationRelationType_httpwww_w3_org1999xlinkshow', pyxb.bundles.common.xlink.showType)
    __show._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 70, 1)
    __show._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 117, 2)
    
    show = property(__show.value, __show.set, None, None)

    
    # Attribute {http://www.w3.org/1999/xlink}actuate uses Python identifier actuate
    __actuate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace, 'actuate'), 'actuate', '__httpwww_opengis_netcitygml1_0_GeneralizationRelationType_httpwww_w3_org1999xlinkactuate', pyxb.bundles.common.xlink.actuateType)
    __actuate._DeclarationLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 82, 1)
    __actuate._UseLocation = pyxb.utils.utility.Location('/tmp/pyxbdist.mqXn05k/PyXB-1.2.4/pyxb/bundles/common/schemas/xlink.xsd', 118, 2)
    
    actuate = property(__actuate.value, __actuate.set, None, None)

    _ElementMap.update({
        __CityObject.name() : __CityObject
    })
    _AttributeMap.update({
        __remoteSchema.name() : __remoteSchema,
        __type.name() : __type,
        __href.name() : __href,
        __role.name() : __role,
        __arcrole.name() : __arcrole,
        __title.name() : __title,
        __show.name() : __show,
        __actuate.name() : __actuate
    })
Namespace.addCategoryObject('typeBinding', 'GeneralizationRelationType', GeneralizationRelationType)


# Complex type {http://www.opengis.net/citygml/1.0}ExternalReferenceType with content type ELEMENT_ONLY
class ExternalReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Type describing the reference to an corresponding object in an other information system, for example
                in the german cadastre ALKIS, the german topographic information system or ATKIS, or the OS MasterMap. The
                reference consists of the name of the external information system, represented by an URI, and the reference of the
                external object, given either by a string or by an URI. If the informationSystem element is missing in the
                ExternalReference, the ExternalObjectReference must be an URI, which contains an indication of the
                informationSystem."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 123, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/citygml/1.0}informationSystem uses Python identifier informationSystem
    __informationSystem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'informationSystem'), 'informationSystem', '__httpwww_opengis_netcitygml1_0_ExternalReferenceType_httpwww_opengis_netcitygml1_0informationSystem', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 133, 12), )

    
    informationSystem = property(__informationSystem.value, __informationSystem.set, None, None)

    
    # Element {http://www.opengis.net/citygml/1.0}externalObject uses Python identifier externalObject
    __externalObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'externalObject'), 'externalObject', '__httpwww_opengis_netcitygml1_0_ExternalReferenceType_httpwww_opengis_netcitygml1_0externalObject', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 134, 12), )

    
    externalObject = property(__externalObject.value, __externalObject.set, None, None)

    _ElementMap.update({
        __informationSystem.name() : __informationSystem,
        __externalObject.name() : __externalObject
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ExternalReferenceType', ExternalReferenceType)


# Complex type {http://www.opengis.net/citygml/1.0}ExternalObjectReferenceType with content type ELEMENT_ONLY
class ExternalObjectReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.opengis.net/citygml/1.0}ExternalObjectReferenceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ExternalObjectReferenceType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 138, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.opengis.net/citygml/1.0}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpwww_opengis_netcitygml1_0_ExternalObjectReferenceType_httpwww_opengis_netcitygml1_0name', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 140, 12), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element {http://www.opengis.net/citygml/1.0}uri uses Python identifier uri
    __uri = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'uri'), 'uri', '__httpwww_opengis_netcitygml1_0_ExternalObjectReferenceType_httpwww_opengis_netcitygml1_0uri', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 141, 12), )

    
    uri = property(__uri.value, __uri.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __uri.name() : __uri
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ExternalObjectReferenceType', ExternalObjectReferenceType)


# Complex type {http://www.opengis.net/citygml/1.0}AddressPropertyType with content type ELEMENT_ONLY
class AddressPropertyType (teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType):
    """Denotes the relation of an _CityObject to its addresses. The AddressPropertyType element must either
                carry a reference to an Address object or contain an Address object inline, but neither both nor none.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 148, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType
    
    # Element {http://www.opengis.net/citygml/1.0}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Address'), 'Address', '__httpwww_opengis_netcitygml1_0_AddressPropertyType_httpwww_opengis_netcitygml1_0Address', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 180, 4), )

    
    Address = property(__Address.value, __Address.set, None, None)

    
    # Attribute remoteSchema inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute type inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute href inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute role inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute arcrole inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute title inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute show inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute actuate inherited from {http://www.opengis.net/gml}AssociationType
    _ElementMap.update({
        __Address.name() : __Address
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AddressPropertyType', AddressPropertyType)


# Complex type {http://www.opengis.net/citygml/1.0}AddressType with content type ELEMENT_ONLY
class AddressType (teaser.Data.SchemaBindings.opengis.raw.gml.AbstractFeatureType):
    """Type for addresses. It references the xAL address standard issued by the OASIS consortium. Please
                note, that addresses are modelled as GML features. Every address can be assigned zero or more 2D or 3D point
                geometries (one gml:MultiPoint geometry) locating the entrance(s). """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 163, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AbstractFeatureType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AbstractFeatureType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AbstractFeatureType
    
    # Element {http://www.opengis.net/citygml/1.0}xalAddress uses Python identifier xalAddress
    __xalAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'xalAddress'), 'xalAddress', '__httpwww_opengis_netcitygml1_0_AddressType_httpwww_opengis_netcitygml1_0xalAddress', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 172, 20), )

    
    xalAddress = property(__xalAddress.value, __xalAddress.set, None, None)

    
    # Element {http://www.opengis.net/citygml/1.0}multiPoint uses Python identifier multiPoint
    __multiPoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'multiPoint'), 'multiPoint', '__httpwww_opengis_netcitygml1_0_AddressType_httpwww_opengis_netcitygml1_0multiPoint', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 173, 20), )

    
    multiPoint = property(__multiPoint.value, __multiPoint.set, None, None)

    
    # Element {http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfAddress uses Python identifier GenericApplicationPropertyOfAddress
    __GenericApplicationPropertyOfAddress = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfAddress'), 'GenericApplicationPropertyOfAddress', '__httpwww_opengis_netcitygml1_0_AddressType_httpwww_opengis_netcitygml1_0_GenericApplicationPropertyOfAddress', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 182, 4), )

    
    GenericApplicationPropertyOfAddress = property(__GenericApplicationPropertyOfAddress.value, __GenericApplicationPropertyOfAddress.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __xalAddress.name() : __xalAddress,
        __multiPoint.name() : __multiPoint,
        __GenericApplicationPropertyOfAddress.name() : __GenericApplicationPropertyOfAddress
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AddressType', AddressType)


# Complex type {http://www.opengis.net/citygml/1.0}xalAddressPropertyType with content type ELEMENT_ONLY
class xalAddressPropertyType (pyxb.binding.basis.complexTypeDefinition):
    """Denotes the relation of an Address feature to the xAL address element."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'xalAddressPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 184, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressDetails uses Python identifier AddressDetails
    __AddressDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_xAL, 'AddressDetails'), 'AddressDetails', '__httpwww_opengis_netcitygml1_0_xalAddressPropertyType_urnoasisnamestcciqxsdschemaxAL2_0AddressDetails', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 44, 1), )

    
    AddressDetails = property(__AddressDetails.value, __AddressDetails.set, None, 'This container defines the details of the address. Can define multiple addresses including tracking address history')

    _ElementMap.update({
        __AddressDetails.name() : __AddressDetails
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'xalAddressPropertyType', xalAddressPropertyType)


# Complex type {http://www.opengis.net/citygml/1.0}ImplicitGeometryType with content type ELEMENT_ONLY
class ImplicitGeometryType (teaser.Data.SchemaBindings.opengis.raw.gml.AbstractGMLType):
    """ Type for the implicit representation of a geometry. An implicit geometry is a geometric object,
                where the shape is stored only once as a prototypical geometry, e.g. a tree or other vegetation object, a traffic
                light or a traffic sign. This prototypic geometry object is re-used or referenced many times, wherever the
                corresponding feature occurs in the 3D city model. Each occurrence is represented by a link to the prototypic
                shape geometry (in a local cartesian coordinate system), by a transforma-tion matrix that is multiplied with each
                3D coordinate tuple of the prototype, and by an anchor point denoting the base point of the object in the world
                coordinate reference system. In order to determine the absolute coordinates of an implicit geometry, the anchor
                point coordinates have to be added to the matrix multiplication results. The transformation matrix accounts for
                the intended rotation, scaling, and local translation of the prototype. It is a 4x4 matrix that is multiplied with
                the prototype coordinates using homogeneous coordinates, i.e. (x,y,z,1). This way even a projection might be
                modelled by the transformation matrix. The concept of implicit geometries is an enhancement of the geometry model
                of GML3. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ImplicitGeometryType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 195, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AbstractGMLType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AbstractGMLType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AbstractGMLType
    
    # Element {http://www.opengis.net/citygml/1.0}mimeType uses Python identifier mimeType
    __mimeType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'mimeType'), 'mimeType', '__httpwww_opengis_netcitygml1_0_ImplicitGeometryType_httpwww_opengis_netcitygml1_0mimeType', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 213, 20), )

    
    mimeType = property(__mimeType.value, __mimeType.set, None, None)

    
    # Element {http://www.opengis.net/citygml/1.0}transformationMatrix uses Python identifier transformationMatrix
    __transformationMatrix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'transformationMatrix'), 'transformationMatrix', '__httpwww_opengis_netcitygml1_0_ImplicitGeometryType_httpwww_opengis_netcitygml1_0transformationMatrix', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 214, 20), )

    
    transformationMatrix = property(__transformationMatrix.value, __transformationMatrix.set, None, None)

    
    # Element {http://www.opengis.net/citygml/1.0}libraryObject uses Python identifier libraryObject
    __libraryObject = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'libraryObject'), 'libraryObject', '__httpwww_opengis_netcitygml1_0_ImplicitGeometryType_httpwww_opengis_netcitygml1_0libraryObject', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 215, 20), )

    
    libraryObject = property(__libraryObject.value, __libraryObject.set, None, None)

    
    # Element {http://www.opengis.net/citygml/1.0}relativeGMLGeometry uses Python identifier relativeGMLGeometry
    __relativeGMLGeometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'relativeGMLGeometry'), 'relativeGMLGeometry', '__httpwww_opengis_netcitygml1_0_ImplicitGeometryType_httpwww_opengis_netcitygml1_0relativeGMLGeometry', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 216, 20), )

    
    relativeGMLGeometry = property(__relativeGMLGeometry.value, __relativeGMLGeometry.set, None, None)

    
    # Element {http://www.opengis.net/citygml/1.0}referencePoint uses Python identifier referencePoint
    __referencePoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'referencePoint'), 'referencePoint', '__httpwww_opengis_netcitygml1_0_ImplicitGeometryType_httpwww_opengis_netcitygml1_0referencePoint', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 217, 20), )

    
    referencePoint = property(__referencePoint.value, __referencePoint.set, None, None)

    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __mimeType.name() : __mimeType,
        __transformationMatrix.name() : __transformationMatrix,
        __libraryObject.name() : __libraryObject,
        __relativeGMLGeometry.name() : __relativeGMLGeometry,
        __referencePoint.name() : __referencePoint
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ImplicitGeometryType', ImplicitGeometryType)


# Complex type {http://www.opengis.net/citygml/1.0}ImplicitRepresentationPropertyType with content type ELEMENT_ONLY
class ImplicitRepresentationPropertyType (teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType):
    """Denotes the relation of a _CityObject to its implicit geometry representation, which is a
                representation of a geometry by referencing a prototype and transforming it to its real position in space. The
                ImplicitRepresentationPropertyType element must either carry a reference to a ImplicitGeometry object or contain a
                ImplicitGeometry object inline, but neither both nor none. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ImplicitRepresentationPropertyType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 225, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.raw.gml.AssociationType
    
    # Element {http://www.opengis.net/citygml/1.0}ImplicitGeometry uses Python identifier ImplicitGeometry
    __ImplicitGeometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ImplicitGeometry'), 'ImplicitGeometry', '__httpwww_opengis_netcitygml1_0_ImplicitRepresentationPropertyType_httpwww_opengis_netcitygml1_0ImplicitGeometry', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 223, 4), )

    
    ImplicitGeometry = property(__ImplicitGeometry.value, __ImplicitGeometry.set, None, None)

    
    # Attribute remoteSchema inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute type inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute href inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute role inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute arcrole inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute title inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute show inherited from {http://www.opengis.net/gml}AssociationType
    
    # Attribute actuate inherited from {http://www.opengis.net/gml}AssociationType
    _ElementMap.update({
        __ImplicitGeometry.name() : __ImplicitGeometry
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ImplicitRepresentationPropertyType', ImplicitRepresentationPropertyType)


# Complex type {http://www.opengis.net/citygml/1.0}AbstractSiteType with content type ELEMENT_ONLY
class AbstractSiteType (AbstractCityObjectType):
    """Type describing the abstract superclass for buildings, facilities, etc. Future extensions of CityGML
                like bridges and tunnels would be modelled as subclasses of _Site. As subclass of _CityObject, a _Site inherits
                all attributes and relations, in particular an id, names, external references, and generalization relations.
            """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractSiteType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 86, 4)
    _ElementMap = AbstractCityObjectType._ElementMap.copy()
    _AttributeMap = AbstractCityObjectType._AttributeMap.copy()
    # Base type is AbstractCityObjectType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element {http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfSite uses Python identifier GenericApplicationPropertyOfSite
    __GenericApplicationPropertyOfSite = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfSite'), 'GenericApplicationPropertyOfSite', '__httpwww_opengis_netcitygml1_0_AbstractSiteType_httpwww_opengis_netcitygml1_0_GenericApplicationPropertyOfSite', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 104, 4), )

    
    GenericApplicationPropertyOfSite = property(__GenericApplicationPropertyOfSite.value, __GenericApplicationPropertyOfSite.set, None, None)

    
    # Element boundedBy ({http://www.opengis.net/gml}boundedBy) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element location ({http://www.opengis.net/gml}location) inherited from {http://www.opengis.net/gml}AbstractFeatureType
    
    # Element metaDataProperty ({http://www.opengis.net/gml}metaDataProperty) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element name ({http://www.opengis.net/gml}name) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Element description ({http://www.opengis.net/gml}description) inherited from {http://www.opengis.net/gml}AbstractGMLType
    
    # Attribute id inherited from {http://www.opengis.net/gml}AbstractGMLType
    _ElementMap.update({
        __GenericApplicationPropertyOfSite.name() : __GenericApplicationPropertyOfSite
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AbstractSiteType', AbstractSiteType)


GenericApplicationPropertyOfCityModel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityModel'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 35, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfCityModel.name().localName(), GenericApplicationPropertyOfCityModel)

cityObjectMember = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cityObjectMember'), teaser.Data.SchemaBindings.opengis.raw.gml.FeaturePropertyType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 39, 4))
Namespace.addCategoryObject('elementBinding', cityObjectMember.name().localName(), cityObjectMember)

GenericApplicationPropertyOfCityObject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityObject'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 82, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfCityObject.name().localName(), GenericApplicationPropertyOfCityObject)

GenericApplicationPropertyOfSite = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfSite'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 104, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfSite.name().localName(), GenericApplicationPropertyOfSite)

GenericApplicationPropertyOfAddress = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfAddress'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 182, 4))
Namespace.addCategoryObject('elementBinding', GenericApplicationPropertyOfAddress.name().localName(), GenericApplicationPropertyOfAddress)

CityModel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CityModel'), CityModelType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 33, 4))
Namespace.addCategoryObject('elementBinding', CityModel.name().localName(), CityModel)

CityObject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_CityObject'), AbstractCityObjectType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 64, 4))
Namespace.addCategoryObject('elementBinding', CityObject.name().localName(), CityObject)

Address = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Address'), AddressType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 180, 4))
Namespace.addCategoryObject('elementBinding', Address.name().localName(), Address)

ImplicitGeometry = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImplicitGeometry'), ImplicitGeometryType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 223, 4))
Namespace.addCategoryObject('elementBinding', ImplicitGeometry.name().localName(), ImplicitGeometry)

Site = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_Site'), AbstractSiteType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 102, 4))
Namespace.addCategoryObject('elementBinding', Site.name().localName(), Site)



CityModelType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityModel'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=CityModelType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 35, 4)))

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
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 108, 5))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 109, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 27, 20))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CityModelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CityModelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CityModelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CityModelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CityModelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CityModelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'featureMember')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 108, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CityModelType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'featureMembers')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 109, 5))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CityModelType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityModel')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 27, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CityModelType._Automaton = _BuildAutomaton()




AbstractCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'creationDate'), pyxb.binding.datatypes.date, scope=AbstractCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20)))

AbstractCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'terminationDate'), pyxb.binding.datatypes.date, scope=AbstractCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20)))

AbstractCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'externalReference'), ExternalReferenceType, scope=AbstractCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20)))

AbstractCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'generalizesTo'), GeneralizationRelationType, scope=AbstractCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20)))

AbstractCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityObject'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=AbstractCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 82, 4)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
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
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AbstractCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractCityObjectType._Automaton = _BuildAutomaton_()




GeneralizationRelationType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_CityObject'), AbstractCityObjectType, abstract=pyxb.binding.datatypes.boolean(1), scope=GeneralizationRelationType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 64, 4)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 115, 8))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GeneralizationRelationType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_CityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 116, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GeneralizationRelationType._Automaton = _BuildAutomaton_2()




ExternalReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'informationSystem'), pyxb.binding.datatypes.anyURI, scope=ExternalReferenceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 133, 12)))

ExternalReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'externalObject'), ExternalObjectReferenceType, scope=ExternalReferenceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 134, 12)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 133, 12))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ExternalReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'informationSystem')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 133, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ExternalReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'externalObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 134, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ExternalReferenceType._Automaton = _BuildAutomaton_3()




ExternalObjectReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=ExternalObjectReferenceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 140, 12)))

ExternalObjectReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uri'), pyxb.binding.datatypes.anyURI, scope=ExternalObjectReferenceType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 141, 12)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ExternalObjectReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 140, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ExternalObjectReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'uri')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 141, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ExternalObjectReferenceType._Automaton = _BuildAutomaton_4()




AddressPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Address'), AddressType, scope=AddressPropertyType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 180, 4)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 156, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AddressPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Address')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 157, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AddressPropertyType._Automaton = _BuildAutomaton_5()




AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xalAddress'), xalAddressPropertyType, scope=AddressType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 172, 20)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'multiPoint'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiPointPropertyType, scope=AddressType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 173, 20)))

AddressType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfAddress'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=AddressType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 182, 4)))

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
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 173, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 174, 20))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'xalAddress')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 172, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'multiPoint')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 173, 20))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AddressType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfAddress')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 174, 20))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AddressType._Automaton = _BuildAutomaton_6()




xalAddressPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_xAL, 'AddressDetails'), teaser.Data.SchemaBindings.opengis.misc.raw.xAL.AddressDetails_, scope=xalAddressPropertyType, documentation='This container defines the details of the address. Can define multiple addresses including tracking address history', location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 44, 1)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(xalAddressPropertyType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xAL, 'AddressDetails')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 189, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
xalAddressPropertyType._Automaton = _BuildAutomaton_7()




ImplicitGeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'mimeType'), MimeTypeType, scope=ImplicitGeometryType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 213, 20)))

ImplicitGeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'transformationMatrix'), TransformationMatrix4x4Type, scope=ImplicitGeometryType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 214, 20)))

ImplicitGeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'libraryObject'), pyxb.binding.datatypes.anyURI, scope=ImplicitGeometryType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 215, 20)))

ImplicitGeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'relativeGMLGeometry'), teaser.Data.SchemaBindings.opengis.raw.gml.GeometryPropertyType, scope=ImplicitGeometryType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 216, 20)))

ImplicitGeometryType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'referencePoint'), teaser.Data.SchemaBindings.opengis.raw.gml.PointPropertyType, scope=ImplicitGeometryType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 217, 20)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 213, 20))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 214, 20))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 215, 20))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 216, 20))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImplicitGeometryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImplicitGeometryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImplicitGeometryType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImplicitGeometryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'mimeType')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 213, 20))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImplicitGeometryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'transformationMatrix')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 214, 20))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImplicitGeometryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'libraryObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 215, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ImplicitGeometryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'relativeGMLGeometry')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 216, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ImplicitGeometryType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'referencePoint')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 217, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ImplicitGeometryType._Automaton = _BuildAutomaton_8()




ImplicitRepresentationPropertyType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ImplicitGeometry'), ImplicitGeometryType, scope=ImplicitRepresentationPropertyType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 223, 4)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 234, 16))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ImplicitRepresentationPropertyType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ImplicitGeometry')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 235, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ImplicitRepresentationPropertyType._Automaton = _BuildAutomaton_9()




AbstractSiteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfSite'), pyxb.binding.datatypes.anyType, abstract=pyxb.binding.datatypes.boolean(1), scope=AbstractSiteType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 104, 4)))

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
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 96, 20))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AbstractSiteType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AbstractSiteType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AbstractSiteType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AbstractSiteType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AbstractSiteType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AbstractSiteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AbstractSiteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AbstractSiteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AbstractSiteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(AbstractSiteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(AbstractSiteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, '_GenericApplicationPropertyOfSite')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 96, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AbstractSiteType._Automaton = _BuildAutomaton_10()


cityObjectMember._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.raw.gml.featureMember)

CityModel._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.raw.gml.FeatureCollection)

CityObject._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.raw.gml.Feature)

Address._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.raw.gml.Feature)

ImplicitGeometry._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.raw.gml.GML)

Site._setSubstitutionGroup(CityObject)
