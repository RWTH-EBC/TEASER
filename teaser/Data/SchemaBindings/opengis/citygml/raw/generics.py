# ./pyxb/bundles/opengis/citygml/raw/generics.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:4d50e2a60871b1f7f72bd15af8e2596f999485f1
# Generated 2015-05-04 11:02:27.487716 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace http://www.opengis.net/citygml/generics/1.0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:48f0aa34-f23c-11e4-97fd-000c29ce1afb')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import teaser.Data.SchemaBindings.opengis.citygml.raw.base
import teaser.Data.SchemaBindings.opengis.raw.gml
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.opengis.net/citygml/generics/1.0', create_if_missing=True)
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


# Complex type {http://www.opengis.net/citygml/generics/1.0}GenericCityObjectType with content type ELEMENT_ONLY
class GenericCityObjectType (teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType):
    """Generic (user defined) city objects may be used to model features which are not covered explicitly
                by the CityGML schema. Generic objects must be used with care; they shall only be used if there is no appropiate
                thematic class available in the overall CityGML schema. Oherwise, problems concerning semantic interoperability
                may arise. As subclass of _CityObject, a generic city object inherits all attributes and relations, in particular
                an id, names, external references, and generalization relations. """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GenericCityObjectType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 19, 4)
    _ElementMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._ElementMap.copy()
    _AttributeMap = teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType._AttributeMap.copy()
    # Base type is teaser.Data.SchemaBindings.opengis.citygml.raw.base.AbstractCityObjectType
    
    # Element creationDate ({http://www.opengis.net/citygml/1.0}creationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element terminationDate ({http://www.opengis.net/citygml/1.0}terminationDate) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element externalReference ({http://www.opengis.net/citygml/1.0}externalReference) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element generalizesTo ({http://www.opengis.net/citygml/1.0}generalizesTo) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element GenericApplicationPropertyOfCityObject ({http://www.opengis.net/citygml/1.0}_GenericApplicationPropertyOfCityObject) inherited from {http://www.opengis.net/citygml/1.0}AbstractCityObjectType
    
    # Element {http://www.opengis.net/citygml/generics/1.0}class uses Python identifier class_
    __class = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'class'), 'class_', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0class', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 30, 20), )

    
    class_ = property(__class.value, __class.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}function uses Python identifier function
    __function = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'function'), 'function', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0function', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 31, 20), )

    
    function = property(__function.value, __function.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}usage uses Python identifier usage
    __usage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usage'), 'usage', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0usage', True, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 32, 20), )

    
    usage = property(__usage.value, __usage.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod0Geometry uses Python identifier lod0Geometry
    __lod0Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod0Geometry'), 'lod0Geometry', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod0Geometry', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 33, 20), )

    
    lod0Geometry = property(__lod0Geometry.value, __lod0Geometry.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod1Geometry uses Python identifier lod1Geometry
    __lod1Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod1Geometry'), 'lod1Geometry', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod1Geometry', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 34, 20), )

    
    lod1Geometry = property(__lod1Geometry.value, __lod1Geometry.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod2Geometry uses Python identifier lod2Geometry
    __lod2Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod2Geometry'), 'lod2Geometry', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod2Geometry', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 35, 20), )

    
    lod2Geometry = property(__lod2Geometry.value, __lod2Geometry.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod3Geometry uses Python identifier lod3Geometry
    __lod3Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod3Geometry'), 'lod3Geometry', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod3Geometry', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 36, 20), )

    
    lod3Geometry = property(__lod3Geometry.value, __lod3Geometry.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod4Geometry uses Python identifier lod4Geometry
    __lod4Geometry = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4Geometry'), 'lod4Geometry', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod4Geometry', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 37, 20), )

    
    lod4Geometry = property(__lod4Geometry.value, __lod4Geometry.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod0TerrainIntersection uses Python identifier lod0TerrainIntersection
    __lod0TerrainIntersection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod0TerrainIntersection'), 'lod0TerrainIntersection', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod0TerrainIntersection', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 38, 20), )

    
    lod0TerrainIntersection = property(__lod0TerrainIntersection.value, __lod0TerrainIntersection.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod1TerrainIntersection uses Python identifier lod1TerrainIntersection
    __lod1TerrainIntersection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod1TerrainIntersection'), 'lod1TerrainIntersection', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod1TerrainIntersection', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 39, 20), )

    
    lod1TerrainIntersection = property(__lod1TerrainIntersection.value, __lod1TerrainIntersection.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod2TerrainIntersection uses Python identifier lod2TerrainIntersection
    __lod2TerrainIntersection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod2TerrainIntersection'), 'lod2TerrainIntersection', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod2TerrainIntersection', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 40, 20), )

    
    lod2TerrainIntersection = property(__lod2TerrainIntersection.value, __lod2TerrainIntersection.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod3TerrainIntersection uses Python identifier lod3TerrainIntersection
    __lod3TerrainIntersection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod3TerrainIntersection'), 'lod3TerrainIntersection', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod3TerrainIntersection', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 41, 20), )

    
    lod3TerrainIntersection = property(__lod3TerrainIntersection.value, __lod3TerrainIntersection.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod4TerrainIntersection uses Python identifier lod4TerrainIntersection
    __lod4TerrainIntersection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4TerrainIntersection'), 'lod4TerrainIntersection', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod4TerrainIntersection', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 42, 20), )

    
    lod4TerrainIntersection = property(__lod4TerrainIntersection.value, __lod4TerrainIntersection.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod0ImplicitRepresentation uses Python identifier lod0ImplicitRepresentation
    __lod0ImplicitRepresentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod0ImplicitRepresentation'), 'lod0ImplicitRepresentation', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod0ImplicitRepresentation', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 43, 20), )

    
    lod0ImplicitRepresentation = property(__lod0ImplicitRepresentation.value, __lod0ImplicitRepresentation.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod1ImplicitRepresentation uses Python identifier lod1ImplicitRepresentation
    __lod1ImplicitRepresentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod1ImplicitRepresentation'), 'lod1ImplicitRepresentation', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod1ImplicitRepresentation', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 44, 20), )

    
    lod1ImplicitRepresentation = property(__lod1ImplicitRepresentation.value, __lod1ImplicitRepresentation.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod2ImplicitRepresentation uses Python identifier lod2ImplicitRepresentation
    __lod2ImplicitRepresentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod2ImplicitRepresentation'), 'lod2ImplicitRepresentation', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod2ImplicitRepresentation', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 45, 20), )

    
    lod2ImplicitRepresentation = property(__lod2ImplicitRepresentation.value, __lod2ImplicitRepresentation.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod3ImplicitRepresentation uses Python identifier lod3ImplicitRepresentation
    __lod3ImplicitRepresentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod3ImplicitRepresentation'), 'lod3ImplicitRepresentation', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod3ImplicitRepresentation', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 46, 20), )

    
    lod3ImplicitRepresentation = property(__lod3ImplicitRepresentation.value, __lod3ImplicitRepresentation.set, None, None)

    
    # Element {http://www.opengis.net/citygml/generics/1.0}lod4ImplicitRepresentation uses Python identifier lod4ImplicitRepresentation
    __lod4ImplicitRepresentation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lod4ImplicitRepresentation'), 'lod4ImplicitRepresentation', '__httpwww_opengis_netcitygmlgenerics1_0_GenericCityObjectType_httpwww_opengis_netcitygmlgenerics1_0lod4ImplicitRepresentation', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 47, 20), )

    
    lod4ImplicitRepresentation = property(__lod4ImplicitRepresentation.value, __lod4ImplicitRepresentation.set, None, None)

    
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
        __lod0Geometry.name() : __lod0Geometry,
        __lod1Geometry.name() : __lod1Geometry,
        __lod2Geometry.name() : __lod2Geometry,
        __lod3Geometry.name() : __lod3Geometry,
        __lod4Geometry.name() : __lod4Geometry,
        __lod0TerrainIntersection.name() : __lod0TerrainIntersection,
        __lod1TerrainIntersection.name() : __lod1TerrainIntersection,
        __lod2TerrainIntersection.name() : __lod2TerrainIntersection,
        __lod3TerrainIntersection.name() : __lod3TerrainIntersection,
        __lod4TerrainIntersection.name() : __lod4TerrainIntersection,
        __lod0ImplicitRepresentation.name() : __lod0ImplicitRepresentation,
        __lod1ImplicitRepresentation.name() : __lod1ImplicitRepresentation,
        __lod2ImplicitRepresentation.name() : __lod2ImplicitRepresentation,
        __lod3ImplicitRepresentation.name() : __lod3ImplicitRepresentation,
        __lod4ImplicitRepresentation.name() : __lod4ImplicitRepresentation
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GenericCityObjectType', GenericCityObjectType)


# Complex type {http://www.opengis.net/citygml/generics/1.0}AbstractGenericAttributeType with content type EMPTY
class AbstractGenericAttributeType (pyxb.binding.basis.complexTypeDefinition):
    """ Generic (user defined) attributes may be used to represent attributes which are not covered
                explicitly by the CityGML schema. Generic attributes must be used with care; they shall only be used if there is
                no appropiate attribute available in the overall CityGML schema. Oherwise, problems concerning semantic
                interoperability may arise. A generic attribute has a name and a value, which has further subclasses
                (IntAttrribute, StringAttribute, ...). """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AbstractGenericAttributeType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 57, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_opengis_netcitygmlgenerics1_0_AbstractGenericAttributeType_name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 66, 8)
    __name._UseLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 66, 8)
    
    name = property(__name.value, __name.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __name.name() : __name
    })
Namespace.addCategoryObject('typeBinding', 'AbstractGenericAttributeType', AbstractGenericAttributeType)


# Complex type {http://www.opengis.net/citygml/generics/1.0}StringAttributeType with content type ELEMENT_ONLY
class StringAttributeType (AbstractGenericAttributeType):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'StringAttributeType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 72, 4)
    _ElementMap = AbstractGenericAttributeType._ElementMap.copy()
    _AttributeMap = AbstractGenericAttributeType._AttributeMap.copy()
    # Base type is AbstractGenericAttributeType
    
    # Element {http://www.opengis.net/citygml/generics/1.0}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpwww_opengis_netcitygmlgenerics1_0_StringAttributeType_httpwww_opengis_netcitygmlgenerics1_0value', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 79, 20), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute name inherited from {http://www.opengis.net/citygml/generics/1.0}AbstractGenericAttributeType
    _ElementMap.update({
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'StringAttributeType', StringAttributeType)


# Complex type {http://www.opengis.net/citygml/generics/1.0}IntAttributeType with content type ELEMENT_ONLY
class IntAttributeType (AbstractGenericAttributeType):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'IntAttributeType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 87, 4)
    _ElementMap = AbstractGenericAttributeType._ElementMap.copy()
    _AttributeMap = AbstractGenericAttributeType._AttributeMap.copy()
    # Base type is AbstractGenericAttributeType
    
    # Element {http://www.opengis.net/citygml/generics/1.0}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpwww_opengis_netcitygmlgenerics1_0_IntAttributeType_httpwww_opengis_netcitygmlgenerics1_0value', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 94, 20), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute name inherited from {http://www.opengis.net/citygml/generics/1.0}AbstractGenericAttributeType
    _ElementMap.update({
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'IntAttributeType', IntAttributeType)


# Complex type {http://www.opengis.net/citygml/generics/1.0}DoubleAttributeType with content type ELEMENT_ONLY
class DoubleAttributeType (AbstractGenericAttributeType):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DoubleAttributeType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 102, 4)
    _ElementMap = AbstractGenericAttributeType._ElementMap.copy()
    _AttributeMap = AbstractGenericAttributeType._AttributeMap.copy()
    # Base type is AbstractGenericAttributeType
    
    # Element {http://www.opengis.net/citygml/generics/1.0}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpwww_opengis_netcitygmlgenerics1_0_DoubleAttributeType_httpwww_opengis_netcitygmlgenerics1_0value', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 109, 20), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute name inherited from {http://www.opengis.net/citygml/generics/1.0}AbstractGenericAttributeType
    _ElementMap.update({
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DoubleAttributeType', DoubleAttributeType)


# Complex type {http://www.opengis.net/citygml/generics/1.0}DateAttributeType with content type ELEMENT_ONLY
class DateAttributeType (AbstractGenericAttributeType):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateAttributeType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 117, 4)
    _ElementMap = AbstractGenericAttributeType._ElementMap.copy()
    _AttributeMap = AbstractGenericAttributeType._AttributeMap.copy()
    # Base type is AbstractGenericAttributeType
    
    # Element {http://www.opengis.net/citygml/generics/1.0}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpwww_opengis_netcitygmlgenerics1_0_DateAttributeType_httpwww_opengis_netcitygmlgenerics1_0value', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 124, 20), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute name inherited from {http://www.opengis.net/citygml/generics/1.0}AbstractGenericAttributeType
    _ElementMap.update({
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'DateAttributeType', DateAttributeType)


# Complex type {http://www.opengis.net/citygml/generics/1.0}UriAttributeType with content type ELEMENT_ONLY
class UriAttributeType (AbstractGenericAttributeType):
    """"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UriAttributeType')
    _XSDLocation = pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 132, 4)
    _ElementMap = AbstractGenericAttributeType._ElementMap.copy()
    _AttributeMap = AbstractGenericAttributeType._AttributeMap.copy()
    # Base type is AbstractGenericAttributeType
    
    # Element {http://www.opengis.net/citygml/generics/1.0}value uses Python identifier value_
    __value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'value'), 'value_', '__httpwww_opengis_netcitygmlgenerics1_0_UriAttributeType_httpwww_opengis_netcitygmlgenerics1_0value', False, pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 139, 20), )

    
    value_ = property(__value.value, __value.set, None, None)

    
    # Attribute name inherited from {http://www.opengis.net/citygml/generics/1.0}AbstractGenericAttributeType
    _ElementMap.update({
        __value.name() : __value
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'UriAttributeType', UriAttributeType)


GenericCityObject = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GenericCityObject'), GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 53, 4))
Namespace.addCategoryObject('elementBinding', GenericCityObject.name().localName(), GenericCityObject)

genericAttribute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, '_genericAttribute'), AbstractGenericAttributeType, abstract=pyxb.binding.datatypes.boolean(1), location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 69, 4))
Namespace.addCategoryObject('elementBinding', genericAttribute.name().localName(), genericAttribute)

stringAttribute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'stringAttribute'), StringAttributeType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 85, 4))
Namespace.addCategoryObject('elementBinding', stringAttribute.name().localName(), stringAttribute)

intAttribute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'intAttribute'), IntAttributeType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 100, 4))
Namespace.addCategoryObject('elementBinding', intAttribute.name().localName(), intAttribute)

doubleAttribute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'doubleAttribute'), DoubleAttributeType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 115, 4))
Namespace.addCategoryObject('elementBinding', doubleAttribute.name().localName(), doubleAttribute)

dateAttribute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dateAttribute'), DateAttributeType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 130, 4))
Namespace.addCategoryObject('elementBinding', dateAttribute.name().localName(), dateAttribute)

uriAttribute = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'uriAttribute'), UriAttributeType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 145, 4))
Namespace.addCategoryObject('elementBinding', uriAttribute.name().localName(), uriAttribute)



GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'class'), pyxb.binding.datatypes.string, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 30, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'function'), pyxb.binding.datatypes.string, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 31, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usage'), pyxb.binding.datatypes.string, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 32, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod0Geometry'), teaser.Data.SchemaBindings.opengis.raw.gml.GeometryPropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 33, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod1Geometry'), teaser.Data.SchemaBindings.opengis.raw.gml.GeometryPropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 34, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod2Geometry'), teaser.Data.SchemaBindings.opengis.raw.gml.GeometryPropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 35, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod3Geometry'), teaser.Data.SchemaBindings.opengis.raw.gml.GeometryPropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 36, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4Geometry'), teaser.Data.SchemaBindings.opengis.raw.gml.GeometryPropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 37, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod0TerrainIntersection'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiCurvePropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 38, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod1TerrainIntersection'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiCurvePropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 39, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod2TerrainIntersection'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiCurvePropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 40, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod3TerrainIntersection'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiCurvePropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 41, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4TerrainIntersection'), teaser.Data.SchemaBindings.opengis.raw.gml.MultiCurvePropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 42, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod0ImplicitRepresentation'), teaser.Data.SchemaBindings.opengis.citygml.raw.base.ImplicitRepresentationPropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 43, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod1ImplicitRepresentation'), teaser.Data.SchemaBindings.opengis.citygml.raw.base.ImplicitRepresentationPropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 44, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod2ImplicitRepresentation'), teaser.Data.SchemaBindings.opengis.citygml.raw.base.ImplicitRepresentationPropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 45, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod3ImplicitRepresentation'), teaser.Data.SchemaBindings.opengis.citygml.raw.base.ImplicitRepresentationPropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 46, 20)))

GenericCityObjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lod4ImplicitRepresentation'), teaser.Data.SchemaBindings.opengis.citygml.raw.base.ImplicitRepresentationPropertyType, scope=GenericCityObjectType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 47, 20)))

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
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 30, 20))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 31, 20))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 32, 20))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 33, 20))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 34, 20))
    counters.add(cc_14)
    cc_15 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 35, 20))
    counters.add(cc_15)
    cc_16 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 36, 20))
    counters.add(cc_16)
    cc_17 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 37, 20))
    counters.add(cc_17)
    cc_18 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 38, 20))
    counters.add(cc_18)
    cc_19 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 39, 20))
    counters.add(cc_19)
    cc_20 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 40, 20))
    counters.add(cc_20)
    cc_21 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 41, 20))
    counters.add(cc_21)
    cc_22 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 42, 20))
    counters.add(cc_22)
    cc_23 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 43, 20))
    counters.add(cc_23)
    cc_24 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 44, 20))
    counters.add(cc_24)
    cc_25 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 45, 20))
    counters.add(cc_25)
    cc_26 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 46, 20))
    counters.add(cc_26)
    cc_27 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 47, 20))
    counters.add(cc_27)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'metaDataProperty')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 55, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'description')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 56, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'name')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/gmlBase.xsd', 57, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'boundedBy')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 28, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_gml, 'location')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/gml/3.1.1/base/feature.xsd', 29, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'creationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 54, 20))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'terminationDate')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 55, 20))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'externalReference')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 56, 20))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, 'generalizesTo')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 57, 20))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_core, '_GenericApplicationPropertyOfCityObject')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/1.0/cityGMLBase.xsd', 58, 20))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'class')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 30, 20))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'function')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 31, 20))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 32, 20))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod0Geometry')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 33, 20))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1Geometry')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 34, 20))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_15, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2Geometry')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 35, 20))
    st_15 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_16, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3Geometry')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 36, 20))
    st_16 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_16)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_17, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4Geometry')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 37, 20))
    st_17 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_17)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_18, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod0TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 38, 20))
    st_18 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_18)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_19, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 39, 20))
    st_19 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_19)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_20, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 40, 20))
    st_20 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_20)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_21, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 41, 20))
    st_21 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_21)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_22, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4TerrainIntersection')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 42, 20))
    st_22 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_22)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_23, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod0ImplicitRepresentation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 43, 20))
    st_23 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_23)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_24, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod1ImplicitRepresentation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 44, 20))
    st_24 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_24)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_25, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod2ImplicitRepresentation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 45, 20))
    st_25 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_25)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_26, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod3ImplicitRepresentation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 46, 20))
    st_26 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_26)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_27, False))
    symbol = pyxb.binding.content.ElementUse(GenericCityObjectType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lod4ImplicitRepresentation')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 47, 20))
    st_27 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_27)
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
    st_24._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_25, [
        fac.UpdateInstruction(cc_25, True) ]))
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_25, False) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_25, False) ]))
    st_25._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_26, [
        fac.UpdateInstruction(cc_26, True) ]))
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_26, False) ]))
    st_26._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_27, [
        fac.UpdateInstruction(cc_27, True) ]))
    st_27._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
GenericCityObjectType._Automaton = _BuildAutomaton()




StringAttributeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.string, scope=StringAttributeType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 79, 20)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(StringAttributeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 79, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StringAttributeType._Automaton = _BuildAutomaton_()




IntAttributeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.integer, scope=IntAttributeType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 94, 20)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(IntAttributeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 94, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
IntAttributeType._Automaton = _BuildAutomaton_2()




DoubleAttributeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.double, scope=DoubleAttributeType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 109, 20)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DoubleAttributeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 109, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DoubleAttributeType._Automaton = _BuildAutomaton_3()




DateAttributeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.date, scope=DateAttributeType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 124, 20)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DateAttributeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 124, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
DateAttributeType._Automaton = _BuildAutomaton_4()




UriAttributeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'value'), pyxb.binding.datatypes.anyURI, scope=UriAttributeType, location=pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 139, 20)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(UriAttributeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'value')), pyxb.utils.utility.Location('/root/pyxb/PyXB-1.2.4/pyxb/bundles/opengis/schemas/citygml/generics/1.0/generics.xsd', 139, 20))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
UriAttributeType._Automaton = _BuildAutomaton_5()


GenericCityObject._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.citygml.raw.base.CityObject)

genericAttribute._setSubstitutionGroup(teaser.Data.SchemaBindings.opengis.citygml.raw.base.GenericApplicationPropertyOfCityObject)

stringAttribute._setSubstitutionGroup(genericAttribute)

intAttribute._setSubstitutionGroup(genericAttribute)

doubleAttribute._setSubstitutionGroup(genericAttribute)

dateAttribute._setSubstitutionGroup(genericAttribute)

uriAttribute._setSubstitutionGroup(genericAttribute)
