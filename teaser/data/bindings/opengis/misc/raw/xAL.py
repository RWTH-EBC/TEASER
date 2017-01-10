# ./pyxb/bundles/opengis/misc/raw/xAL.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:28237b706ea7dd7f30e1bac6f6949d1f2f8264f7
# Generated 2017-01-09 16:11:21.843392 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace urn:oasis:names:tc:ciq:xsdschema:xAL:2.0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:e0f982d4-d67d-11e6-8d7b-100ba9a189d0')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('urn:oasis:names:tc:ciq:xsdschema:xAL:2.0', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 313, 3)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.Before = STD_ANON._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON.After = STD_ANON._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 345, 6)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.Before = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_.After = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 553, 6)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.Before = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_2.After = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 589, 7)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.Before = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_3.After = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: [anonymous]
class STD_ANON_4 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 600, 7)
    _Documentation = None
STD_ANON_4._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_4, enum_prefix=None)
STD_ANON_4.Before = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_4.After = STD_ANON_4._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_4._InitializeFacetMap(STD_ANON_4._CF_enumeration)
_module_typeBindings.STD_ANON_4 = STD_ANON_4

# Atomic simple type: [anonymous]
class STD_ANON_5 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 827, 8)
    _Documentation = None
STD_ANON_5._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_5, enum_prefix=None)
STD_ANON_5.Odd = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='Odd', tag='Odd')
STD_ANON_5.Even = STD_ANON_5._CF_enumeration.addEnumeration(unicode_value='Even', tag='Even')
STD_ANON_5._InitializeFacetMap(STD_ANON_5._CF_enumeration)
_module_typeBindings.STD_ANON_5 = STD_ANON_5

# Atomic simple type: [anonymous]
class STD_ANON_6 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 848, 8)
    _Documentation = None
STD_ANON_6._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_6, enum_prefix=None)
STD_ANON_6.Before = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_6.After = STD_ANON_6._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_6._InitializeFacetMap(STD_ANON_6._CF_enumeration)
_module_typeBindings.STD_ANON_6 = STD_ANON_6

# Atomic simple type: [anonymous]
class STD_ANON_7 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 859, 8)
    _Documentation = None
STD_ANON_7._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_7, enum_prefix=None)
STD_ANON_7.BeforeName = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='BeforeName', tag='BeforeName')
STD_ANON_7.AfterName = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='AfterName', tag='AfterName')
STD_ANON_7.BeforeType = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='BeforeType', tag='BeforeType')
STD_ANON_7.AfterType = STD_ANON_7._CF_enumeration.addEnumeration(unicode_value='AfterType', tag='AfterType')
STD_ANON_7._InitializeFacetMap(STD_ANON_7._CF_enumeration)
_module_typeBindings.STD_ANON_7 = STD_ANON_7

# Atomic simple type: [anonymous]
class STD_ANON_8 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 962, 4)
    _Documentation = None
STD_ANON_8._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_8, enum_prefix=None)
STD_ANON_8.Yes = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='Yes', tag='Yes')
STD_ANON_8.No = STD_ANON_8._CF_enumeration.addEnumeration(unicode_value='No', tag='No')
STD_ANON_8._InitializeFacetMap(STD_ANON_8._CF_enumeration)
_module_typeBindings.STD_ANON_8 = STD_ANON_8

# Atomic simple type: [anonymous]
class STD_ANON_9 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1104, 8)
    _Documentation = None
STD_ANON_9._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_9, enum_prefix=None)
STD_ANON_9.Before = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_9.After = STD_ANON_9._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_9._InitializeFacetMap(STD_ANON_9._CF_enumeration)
_module_typeBindings.STD_ANON_9 = STD_ANON_9

# Atomic simple type: [anonymous]
class STD_ANON_10 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1353, 7)
    _Documentation = None
STD_ANON_10._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_10, enum_prefix=None)
STD_ANON_10.Before = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_10.After = STD_ANON_10._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_10._InitializeFacetMap(STD_ANON_10._CF_enumeration)
_module_typeBindings.STD_ANON_10 = STD_ANON_10

# Atomic simple type: [anonymous]
class STD_ANON_11 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1429, 9)
    _Documentation = None
STD_ANON_11._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_11, enum_prefix=None)
STD_ANON_11.Before = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_11.After = STD_ANON_11._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_11._InitializeFacetMap(STD_ANON_11._CF_enumeration)
_module_typeBindings.STD_ANON_11 = STD_ANON_11

# Atomic simple type: [anonymous]
class STD_ANON_12 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1440, 9)
    _Documentation = None
STD_ANON_12._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_12, enum_prefix=None)
STD_ANON_12.BeforeName = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='BeforeName', tag='BeforeName')
STD_ANON_12.AfterName = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='AfterName', tag='AfterName')
STD_ANON_12.BeforeType = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='BeforeType', tag='BeforeType')
STD_ANON_12.AfterType = STD_ANON_12._CF_enumeration.addEnumeration(unicode_value='AfterType', tag='AfterType')
STD_ANON_12._InitializeFacetMap(STD_ANON_12._CF_enumeration)
_module_typeBindings.STD_ANON_12 = STD_ANON_12

# Atomic simple type: [anonymous]
class STD_ANON_13 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1543, 4)
    _Documentation = None
STD_ANON_13._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_13, enum_prefix=None)
STD_ANON_13.Single = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='Single', tag='Single')
STD_ANON_13.Range = STD_ANON_13._CF_enumeration.addEnumeration(unicode_value='Range', tag='Range')
STD_ANON_13._InitializeFacetMap(STD_ANON_13._CF_enumeration)
_module_typeBindings.STD_ANON_13 = STD_ANON_13

# Atomic simple type: [anonymous]
class STD_ANON_14 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1560, 4)
    _Documentation = None
STD_ANON_14._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_14, enum_prefix=None)
STD_ANON_14.Before = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_14.After = STD_ANON_14._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_14._InitializeFacetMap(STD_ANON_14._CF_enumeration)
_module_typeBindings.STD_ANON_14 = STD_ANON_14

# Atomic simple type: [anonymous]
class STD_ANON_15 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1571, 4)
    _Documentation = None
STD_ANON_15._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_15, enum_prefix=None)
STD_ANON_15.BeforeName = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='BeforeName', tag='BeforeName')
STD_ANON_15.AfterName = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='AfterName', tag='AfterName')
STD_ANON_15.BeforeType = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='BeforeType', tag='BeforeType')
STD_ANON_15.AfterType = STD_ANON_15._CF_enumeration.addEnumeration(unicode_value='AfterType', tag='AfterType')
STD_ANON_15._InitializeFacetMap(STD_ANON_15._CF_enumeration)
_module_typeBindings.STD_ANON_15 = STD_ANON_15

# Atomic simple type: [anonymous]
class STD_ANON_16 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1593, 4)
    _Documentation = None
STD_ANON_16._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_16, enum_prefix=None)
STD_ANON_16.Single = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='Single', tag='Single')
STD_ANON_16.Range = STD_ANON_16._CF_enumeration.addEnumeration(unicode_value='Range', tag='Range')
STD_ANON_16._InitializeFacetMap(STD_ANON_16._CF_enumeration)
_module_typeBindings.STD_ANON_16 = STD_ANON_16

# Atomic simple type: [anonymous]
class STD_ANON_17 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1610, 4)
    _Documentation = None
STD_ANON_17._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_17, enum_prefix=None)
STD_ANON_17.Before = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_17.After = STD_ANON_17._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_17._InitializeFacetMap(STD_ANON_17._CF_enumeration)
_module_typeBindings.STD_ANON_17 = STD_ANON_17

# Atomic simple type: [anonymous]
class STD_ANON_18 (pyxb.binding.datatypes.NMTOKEN, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1621, 4)
    _Documentation = None
STD_ANON_18._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_18, enum_prefix=None)
STD_ANON_18.Before = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='Before', tag='Before')
STD_ANON_18.After = STD_ANON_18._CF_enumeration.addEnumeration(unicode_value='After', tag='After')
STD_ANON_18._InitializeFacetMap(STD_ANON_18._CF_enumeration)
_module_typeBindings.STD_ANON_18 = STD_ANON_18

# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Root element for a list of addresses"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 31, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressDetails uses Python identifier AddressDetails
    __AddressDetails = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressDetails'), 'AddressDetails', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_urnoasisnamestcciqxsdschemaxAL2_0AddressDetails', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 44, 1), )

    
    AddressDetails = property(__AddressDetails.value, __AddressDetails.set, None, 'This container defines the details of the address. Can define multiple addresses including tracking address history')

    
    # Attribute Version uses Python identifier Version
    __Version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Version'), 'Version', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_Version', pyxb.binding.datatypes.anySimpleType)
    __Version._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 36, 3)
    __Version._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 36, 3)
    
    Version = property(__Version.value, __Version.set, None, 'Specific to DTD to specify the version number of DTD')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressDetails.name() : __AddressDetails
    })
    _AttributeMap.update({
        __Version.name() : __Version
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressDetails with content type ELEMENT_ONLY
class AddressDetails_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressDetails with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressDetails')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 49, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalServiceElements uses Python identifier PostalServiceElements
    __PostalServiceElements = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalServiceElements'), 'PostalServiceElements', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__urnoasisnamestcciqxsdschemaxAL2_0PostalServiceElements', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 51, 3), )

    
    PostalServiceElements = property(__PostalServiceElements.value, __PostalServiceElements.set, None, 'Postal authorities use specific postal service data to expedient delivery of mail')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Address'), 'Address', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__urnoasisnamestcciqxsdschemaxAL2_0Address', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 210, 4), )

    
    Address = property(__Address.value, __Address.set, None, 'Address as one line of free text')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLines uses Python identifier AddressLines
    __AddressLines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLines'), 'AddressLines', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__urnoasisnamestcciqxsdschemaxAL2_0AddressLines', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 224, 4), )

    
    AddressLines = property(__AddressLines.value, __AddressLines.set, None, 'Container for Address lines')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Country uses Python identifier Country
    __Country = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Country'), 'Country', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__urnoasisnamestcciqxsdschemaxAL2_0Country', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 229, 4), )

    
    Country = property(__Country.value, __Country.set, None, 'Specification of a country')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Locality uses Python identifier Locality
    __Locality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Locality'), 'Locality', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__urnoasisnamestcciqxsdschemaxAL2_0Locality', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 715, 1), )

    
    Locality = property(__Locality.value, __Locality.set, None, 'Locality is one level lower than adminisstrative area. Eg.: cities, reservations and any other built-up areas.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Thoroughfare uses Python identifier Thoroughfare
    __Thoroughfare = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare'), 'Thoroughfare', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__urnoasisnamestcciqxsdschemaxAL2_0Thoroughfare', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 775, 1), )

    
    Thoroughfare = property(__Thoroughfare.value, __Thoroughfare.set, None, 'Specification of a thoroughfare. A thoroughfare could be a rd, street, canal, river, etc.  Note dependentlocality in a street. For example, in some countries, a large street will \nhave many subdivisions with numbers. Normally the subdivision name is the same as the road name, but with a number to identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AdministrativeArea uses Python identifier AdministrativeArea
    __AdministrativeArea = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea'), 'AdministrativeArea', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__urnoasisnamestcciqxsdschemaxAL2_0AdministrativeArea', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 987, 1), )

    
    AdministrativeArea = property(__AdministrativeArea.value, __AdministrativeArea.set, None, 'Examples of administrative areas are provinces counties, special regions (such as "Rijnmond"), etc.')

    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute AddressType uses Python identifier AddressType
    __AddressType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'AddressType'), 'AddressType', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__AddressType', pyxb.binding.datatypes.anySimpleType)
    __AddressType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 267, 2)
    __AddressType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 267, 2)
    
    AddressType = property(__AddressType.value, __AddressType.set, None, 'Type of address. Example: Postal, residential,business, primary, secondary, etc')

    
    # Attribute CurrentStatus uses Python identifier CurrentStatus
    __CurrentStatus = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'CurrentStatus'), 'CurrentStatus', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__CurrentStatus', pyxb.binding.datatypes.anySimpleType)
    __CurrentStatus._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 272, 2)
    __CurrentStatus._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 272, 2)
    
    CurrentStatus = property(__CurrentStatus.value, __CurrentStatus.set, None, 'Moved, Living, Investment, Deceased, etc..')

    
    # Attribute ValidFromDate uses Python identifier ValidFromDate
    __ValidFromDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ValidFromDate'), 'ValidFromDate', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__ValidFromDate', pyxb.binding.datatypes.anySimpleType)
    __ValidFromDate._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 277, 2)
    __ValidFromDate._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 277, 2)
    
    ValidFromDate = property(__ValidFromDate.value, __ValidFromDate.set, None, 'Start Date of the validity of address')

    
    # Attribute ValidToDate uses Python identifier ValidToDate
    __ValidToDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'ValidToDate'), 'ValidToDate', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__ValidToDate', pyxb.binding.datatypes.anySimpleType)
    __ValidToDate._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 282, 2)
    __ValidToDate._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 282, 2)
    
    ValidToDate = property(__ValidToDate.value, __ValidToDate.set, None, 'End date of the validity of address')

    
    # Attribute Usage uses Python identifier Usage
    __Usage = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Usage'), 'Usage', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__Usage', pyxb.binding.datatypes.anySimpleType)
    __Usage._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 287, 2)
    __Usage._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 287, 2)
    
    Usage = property(__Usage.value, __Usage.set, None, 'Communication, Contact, etc.')

    
    # Attribute AddressDetailsKey uses Python identifier AddressDetailsKey
    __AddressDetailsKey = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'AddressDetailsKey'), 'AddressDetailsKey', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressDetails__AddressDetailsKey', pyxb.binding.datatypes.anySimpleType)
    __AddressDetailsKey._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 293, 2)
    __AddressDetailsKey._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 293, 2)
    
    AddressDetailsKey = property(__AddressDetailsKey.value, __AddressDetailsKey.set, None, 'Key identifier for the element for not reinforced references from other elements. Not required to be unique for the document to be valid, but application may get confused if not unique. Extend this schema adding unique contraint if needed.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __PostalServiceElements.name() : __PostalServiceElements,
        __Address.name() : __Address,
        __AddressLines.name() : __AddressLines,
        __Country.name() : __Country,
        __Locality.name() : __Locality,
        __Thoroughfare.name() : __Thoroughfare,
        __AdministrativeArea.name() : __AdministrativeArea
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __AddressType.name() : __AddressType,
        __CurrentStatus.name() : __CurrentStatus,
        __ValidFromDate.name() : __ValidFromDate,
        __ValidToDate.name() : __ValidToDate,
        __Usage.name() : __Usage,
        __AddressDetailsKey.name() : __AddressDetailsKey
    })
_module_typeBindings.AddressDetails_ = AddressDetails_
Namespace.addCategoryObject('typeBinding', 'AddressDetails', AddressDetails_)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_ (pyxb.binding.basis.complexTypeDefinition):
    """Postal authorities use specific postal service data to expedient delivery of mail"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 55, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressIdentifier uses Python identifier AddressIdentifier
    __AddressIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressIdentifier'), 'AddressIdentifier', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON__urnoasisnamestcciqxsdschemaxAL2_0AddressIdentifier', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 57, 6), )

    
    AddressIdentifier = property(__AddressIdentifier.value, __AddressIdentifier.set, None, 'A unique identifier of an address assigned by postal authorities. Example: DPID in Australia')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}EndorsementLineCode uses Python identifier EndorsementLineCode
    __EndorsementLineCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'EndorsementLineCode'), 'EndorsementLineCode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON__urnoasisnamestcciqxsdschemaxAL2_0EndorsementLineCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 72, 6), )

    
    EndorsementLineCode = property(__EndorsementLineCode.value, __EndorsementLineCode.set, None, 'Directly affects postal service distribution')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}KeyLineCode uses Python identifier KeyLineCode
    __KeyLineCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'KeyLineCode'), 'KeyLineCode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON__urnoasisnamestcciqxsdschemaxAL2_0KeyLineCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 86, 6), )

    
    KeyLineCode = property(__KeyLineCode.value, __KeyLineCode.set, None, 'Required for some postal services')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Barcode uses Python identifier Barcode
    __Barcode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Barcode'), 'Barcode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON__urnoasisnamestcciqxsdschemaxAL2_0Barcode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 100, 6), )

    
    Barcode = property(__Barcode.value, __Barcode.set, None, 'Required for some postal services')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SortingCode uses Python identifier SortingCode
    __SortingCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SortingCode'), 'SortingCode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON__urnoasisnamestcciqxsdschemaxAL2_0SortingCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 114, 6), )

    
    SortingCode = property(__SortingCode.value, __SortingCode.set, None, 'Used for sorting addresses. Values may for example be CEDEX 16 (France)')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLatitude uses Python identifier AddressLatitude
    __AddressLatitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLatitude'), 'AddressLatitude', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON__urnoasisnamestcciqxsdschemaxAL2_0AddressLatitude', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 127, 6), )

    
    AddressLatitude = property(__AddressLatitude.value, __AddressLatitude.set, None, 'Latitude of delivery address')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLatitudeDirection uses Python identifier AddressLatitudeDirection
    __AddressLatitudeDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLatitudeDirection'), 'AddressLatitudeDirection', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON__urnoasisnamestcciqxsdschemaxAL2_0AddressLatitudeDirection', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 141, 6), )

    
    AddressLatitudeDirection = property(__AddressLatitudeDirection.value, __AddressLatitudeDirection.set, None, 'Latitude direction of delivery address;N = North and S = South')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLongitude uses Python identifier AddressLongitude
    __AddressLongitude = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLongitude'), 'AddressLongitude', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON__urnoasisnamestcciqxsdschemaxAL2_0AddressLongitude', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 154, 6), )

    
    AddressLongitude = property(__AddressLongitude.value, __AddressLongitude.set, None, 'Longtitude of delivery address')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLongitudeDirection uses Python identifier AddressLongitudeDirection
    __AddressLongitudeDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLongitudeDirection'), 'AddressLongitudeDirection', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON__urnoasisnamestcciqxsdschemaxAL2_0AddressLongitudeDirection', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 168, 6), )

    
    AddressLongitudeDirection = property(__AddressLongitudeDirection.value, __AddressLongitudeDirection.set, None, 'Longtitude direction of delivery address;N=North and S=South')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SupplementaryPostalServiceData uses Python identifier SupplementaryPostalServiceData
    __SupplementaryPostalServiceData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SupplementaryPostalServiceData'), 'SupplementaryPostalServiceData', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON__urnoasisnamestcciqxsdschemaxAL2_0SupplementaryPostalServiceData', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 182, 6), )

    
    SupplementaryPostalServiceData = property(__SupplementaryPostalServiceData.value, __SupplementaryPostalServiceData.set, None, 'any postal service elements not covered by the container can be represented using this element')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON__Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 198, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 198, 5)
    
    Type = property(__Type.value, __Type.set, None, 'USPS, ECMA, UN/PROLIST, etc')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressIdentifier.name() : __AddressIdentifier,
        __EndorsementLineCode.name() : __EndorsementLineCode,
        __KeyLineCode.name() : __KeyLineCode,
        __Barcode.name() : __Barcode,
        __SortingCode.name() : __SortingCode,
        __AddressLatitude.name() : __AddressLatitude,
        __AddressLatitudeDirection.name() : __AddressLatitudeDirection,
        __AddressLongitude.name() : __AddressLongitude,
        __AddressLongitudeDirection.name() : __AddressLongitudeDirection,
        __SupplementaryPostalServiceData.name() : __SupplementaryPostalServiceData
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_ = CTD_ANON_


# Complex type [anonymous] with content type MIXED
class CTD_ANON_2 (pyxb.binding.basis.complexTypeDefinition):
    """A unique identifier of an address assigned by postal authorities. Example: DPID in Australia"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 61, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_2_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute IdentifierType uses Python identifier IdentifierType
    __IdentifierType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IdentifierType'), 'IdentifierType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_2_IdentifierType', pyxb.binding.datatypes.anySimpleType)
    __IdentifierType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 62, 8)
    __IdentifierType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 62, 8)
    
    IdentifierType = property(__IdentifierType.value, __IdentifierType.set, None, 'Type of identifier. eg. DPID as in Australia')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_2_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 67, 8)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 67, 8)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __IdentifierType.name() : __IdentifierType,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_2 = CTD_ANON_2


# Complex type [anonymous] with content type MIXED
class CTD_ANON_3 (pyxb.binding.basis.complexTypeDefinition):
    """Directly affects postal service distribution"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 76, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_3_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_3_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 77, 8)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 77, 8)
    
    Type = property(__Type.value, __Type.set, None, 'Specific to postal service')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_3 = CTD_ANON_3


# Complex type [anonymous] with content type MIXED
class CTD_ANON_4 (pyxb.binding.basis.complexTypeDefinition):
    """Required for some postal services"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 90, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_4_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_4_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 91, 8)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 91, 8)
    
    Type = property(__Type.value, __Type.set, None, 'Specific to postal service')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_4 = CTD_ANON_4


# Complex type [anonymous] with content type MIXED
class CTD_ANON_5 (pyxb.binding.basis.complexTypeDefinition):
    """Required for some postal services"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 104, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_5_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_5_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 105, 8)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 105, 8)
    
    Type = property(__Type.value, __Type.set, None, 'Specific to postal service')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_5 = CTD_ANON_5


# Complex type [anonymous] with content type EMPTY
class CTD_ANON_6 (pyxb.binding.basis.complexTypeDefinition):
    """Used for sorting addresses. Values may for example be CEDEX 16 (France)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 118, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_6_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_6_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 119, 8)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 119, 8)
    
    Type = property(__Type.value, __Type.set, None, 'Specific to postal service')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_6 = CTD_ANON_6


# Complex type [anonymous] with content type MIXED
class CTD_ANON_7 (pyxb.binding.basis.complexTypeDefinition):
    """Latitude of delivery address"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 131, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_7_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_7_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 132, 8)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 132, 8)
    
    Type = property(__Type.value, __Type.set, None, 'Specific to postal service')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_7 = CTD_ANON_7


# Complex type [anonymous] with content type MIXED
class CTD_ANON_8 (pyxb.binding.basis.complexTypeDefinition):
    """Specific to postal service"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 145, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_8_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_8_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 149, 8)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 149, 8)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_8 = CTD_ANON_8


# Complex type [anonymous] with content type MIXED
class CTD_ANON_9 (pyxb.binding.basis.complexTypeDefinition):
    """Longtitude of delivery address"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 158, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_9_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_9_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 159, 8)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 159, 8)
    
    Type = property(__Type.value, __Type.set, None, 'Specific to postal service')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_9 = CTD_ANON_9


# Complex type [anonymous] with content type MIXED
class CTD_ANON_10 (pyxb.binding.basis.complexTypeDefinition):
    """Longtitude direction of delivery address;N=North and S=South"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 172, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_10_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_10_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 173, 8)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 173, 8)
    
    Type = property(__Type.value, __Type.set, None, 'Specific to postal service')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_10 = CTD_ANON_10


# Complex type [anonymous] with content type MIXED
class CTD_ANON_11 (pyxb.binding.basis.complexTypeDefinition):
    """any postal service elements not covered by the container can be represented using this element"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 186, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_11_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_11_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 187, 8)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 187, 8)
    
    Type = property(__Type.value, __Type.set, None, 'Specific to postal service')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_11 = CTD_ANON_11


# Complex type [anonymous] with content type MIXED
class CTD_ANON_12 (pyxb.binding.basis.complexTypeDefinition):
    """Address as one line of free text"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 214, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_12_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_12_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 215, 6)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 215, 6)
    
    Type = property(__Type.value, __Type.set, None, 'Postal, residential, corporate, etc')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_12 = CTD_ANON_12


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_13 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of a country"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 233, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}CountryNameCode uses Python identifier CountryNameCode
    __CountryNameCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CountryNameCode'), 'CountryNameCode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_13_urnoasisnamestcciqxsdschemaxAL2_0CountryNameCode', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 236, 7), )

    
    CountryNameCode = property(__CountryNameCode.value, __CountryNameCode.set, None, 'A country code according to the specified scheme')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_13_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Locality uses Python identifier Locality
    __Locality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Locality'), 'Locality', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_13_urnoasisnamestcciqxsdschemaxAL2_0Locality', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 715, 1), )

    
    Locality = property(__Locality.value, __Locality.set, None, 'Locality is one level lower than adminisstrative area. Eg.: cities, reservations and any other built-up areas.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Thoroughfare uses Python identifier Thoroughfare
    __Thoroughfare = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare'), 'Thoroughfare', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_13_urnoasisnamestcciqxsdschemaxAL2_0Thoroughfare', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 775, 1), )

    
    Thoroughfare = property(__Thoroughfare.value, __Thoroughfare.set, None, 'Specification of a thoroughfare. A thoroughfare could be a rd, street, canal, river, etc.  Note dependentlocality in a street. For example, in some countries, a large street will \nhave many subdivisions with numbers. Normally the subdivision name is the same as the road name, but with a number to identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AdministrativeArea uses Python identifier AdministrativeArea
    __AdministrativeArea = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea'), 'AdministrativeArea', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_13_urnoasisnamestcciqxsdschemaxAL2_0AdministrativeArea', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 987, 1), )

    
    AdministrativeArea = property(__AdministrativeArea.value, __AdministrativeArea.set, None, 'Examples of administrative areas are provinces counties, special regions (such as "Rijnmond"), etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}CountryName uses Python identifier CountryName
    __CountryName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CountryName'), 'CountryName', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_13_urnoasisnamestcciqxsdschemaxAL2_0CountryName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1666, 1), )

    
    CountryName = property(__CountryName.value, __CountryName.set, None, 'Specification of the name of a country.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __CountryNameCode.name() : __CountryNameCode,
        __AddressLine.name() : __AddressLine,
        __Locality.name() : __Locality,
        __Thoroughfare.name() : __Thoroughfare,
        __AdministrativeArea.name() : __AdministrativeArea,
        __CountryName.name() : __CountryName
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_13 = CTD_ANON_13


# Complex type [anonymous] with content type MIXED
class CTD_ANON_14 (pyxb.binding.basis.complexTypeDefinition):
    """A country code according to the specified scheme"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 240, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_14_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Scheme uses Python identifier Scheme
    __Scheme = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Scheme'), 'Scheme', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_14_Scheme', pyxb.binding.datatypes.anySimpleType)
    __Scheme._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 241, 9)
    __Scheme._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 241, 9)
    
    Scheme = property(__Scheme.value, __Scheme.set, None, 'Country code scheme possible values, but not limited to: iso.3166-2, iso.3166-3 for two and three character country codes.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Scheme.name() : __Scheme
    })
_module_typeBindings.CTD_ANON_14 = CTD_ANON_14


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLinesType with content type ELEMENT_ONLY
class AddressLinesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLinesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AddressLinesType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 300, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_AddressLinesType_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressLine.name() : __AddressLine
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AddressLinesType = AddressLinesType
Namespace.addCategoryObject('typeBinding', 'AddressLinesType', AddressLinesType)


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentLocalityType with content type ELEMENT_ONLY
class DependentLocalityType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentLocalityType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DependentLocalityType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 323, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentLocalityName uses Python identifier DependentLocalityName
    __DependentLocalityName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DependentLocalityName'), 'DependentLocalityName', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_urnoasisnamestcciqxsdschemaxAL2_0DependentLocalityName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 326, 3), )

    
    DependentLocalityName = property(__DependentLocalityName.value, __DependentLocalityName.set, None, 'Name of the dependent locality')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentLocalityNumber uses Python identifier DependentLocalityNumber
    __DependentLocalityNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DependentLocalityNumber'), 'DependentLocalityNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_urnoasisnamestcciqxsdschemaxAL2_0DependentLocalityNumber', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 336, 3), )

    
    DependentLocalityNumber = property(__DependentLocalityNumber.value, __DependentLocalityNumber.set, None, 'Number of the dependent locality. Some areas are numbered. Eg. SECTOR 5 in a Suburb as in India or SOI SUKUMVIT 10 as in Thailand')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}LargeMailUser uses Python identifier LargeMailUser
    __LargeMailUser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LargeMailUser'), 'LargeMailUser', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_urnoasisnamestcciqxsdschemaxAL2_0LargeMailUser', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 358, 4), )

    
    LargeMailUser = property(__LargeMailUser.value, __LargeMailUser.set, None, 'Specification of a large mail user address. Examples of large mail users are postal companies, companies in France with a cedex number, hospitals and airports with their own post code. Large mail user addresses do not have a street name with premise name or premise number in countries like Netherlands. But they have a POBox and street also in countries like France')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalRoute uses Python identifier PostalRoute
    __PostalRoute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalRoute'), 'PostalRoute', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_urnoasisnamestcciqxsdschemaxAL2_0PostalRoute', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 364, 4), )

    
    PostalRoute = property(__PostalRoute.value, __PostalRoute.set, None, ' A Postal van is specific for a route as in Is`rael, Rural route')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentLocality uses Python identifier DependentLocality
    __DependentLocality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DependentLocality'), 'DependentLocality', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_urnoasisnamestcciqxsdschemaxAL2_0DependentLocality', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 372, 3), )

    
    DependentLocality = property(__DependentLocality.value, __DependentLocality.set, None, 'Dependent localities are Districts within cities/towns, locality divisions, postal \ndivisions of cities, suburbs, etc. DependentLocality is a recursive element, but no nesting deeper than two exists (Locality-DependentLocality-DependentLocality).')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Thoroughfare uses Python identifier Thoroughfare
    __Thoroughfare = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare'), 'Thoroughfare', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_urnoasisnamestcciqxsdschemaxAL2_0Thoroughfare', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 775, 1), )

    
    Thoroughfare = property(__Thoroughfare.value, __Thoroughfare.set, None, 'Specification of a thoroughfare. A thoroughfare could be a rd, street, canal, river, etc.  Note dependentlocality in a street. For example, in some countries, a large street will \nhave many subdivisions with numbers. Normally the subdivision name is the same as the road name, but with a number to identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostOffice uses Python identifier PostOffice
    __PostOffice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostOffice'), 'PostOffice', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_urnoasisnamestcciqxsdschemaxAL2_0PostOffice', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1072, 1), )

    
    PostOffice = property(__PostOffice.value, __PostOffice.set, None, 'Specification of a post office. Examples are a rural post office where post is delivered and a post office containing post office boxes.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_urnoasisnamestcciqxsdschemaxAL2_0PostalCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostBox uses Python identifier PostBox
    __PostBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostBox'), 'PostBox', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_urnoasisnamestcciqxsdschemaxAL2_0PostBox', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1223, 1), )

    
    PostBox = property(__PostBox.value, __PostBox.set, None, 'Specification of a postbox like mail delivery point. Only a single postbox number can be specified. Examples of postboxes are POBox, free mail numbers, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Premise uses Python identifier Premise
    __Premise = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Premise'), 'Premise', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_urnoasisnamestcciqxsdschemaxAL2_0Premise', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1335, 1), )

    
    Premise = property(__Premise.value, __Premise.set, None, 'Specification of a single premise, for example a house or a building. The premise as a whole has a unique premise (house) number or a premise name.  There could be more than \none premise in a street referenced in an address. For example a building address near a major shopping centre or raiwlay station')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 381, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 381, 2)
    
    Type = property(__Type.value, __Type.set, None, 'City or IndustrialEstate, etc')

    
    # Attribute UsageType uses Python identifier UsageType
    __UsageType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UsageType'), 'UsageType', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_UsageType', pyxb.binding.datatypes.anySimpleType)
    __UsageType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 386, 2)
    __UsageType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 386, 2)
    
    UsageType = property(__UsageType.value, __UsageType.set, None, 'Postal or Political - Sometimes locations must be distinguished between postal system, and physical locations as defined by a political system')

    
    # Attribute Connector uses Python identifier Connector
    __Connector = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Connector'), 'Connector', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_Connector', pyxb.binding.datatypes.anySimpleType)
    __Connector._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 391, 2)
    __Connector._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 391, 2)
    
    Connector = property(__Connector.value, __Connector.set, None, '"VIA" as in Hill Top VIA Parish where Parish is a locality and Hill Top is a dependent locality')

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_DependentLocalityType_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 396, 2)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 396, 2)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, 'Eg. Erode (Dist) where (Dist) is the Indicator')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __DependentLocalityName.name() : __DependentLocalityName,
        __DependentLocalityNumber.name() : __DependentLocalityNumber,
        __LargeMailUser.name() : __LargeMailUser,
        __PostalRoute.name() : __PostalRoute,
        __DependentLocality.name() : __DependentLocality,
        __AddressLine.name() : __AddressLine,
        __Thoroughfare.name() : __Thoroughfare,
        __PostOffice.name() : __PostOffice,
        __PostalCode.name() : __PostalCode,
        __PostBox.name() : __PostBox,
        __Premise.name() : __Premise
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __UsageType.name() : __UsageType,
        __Connector.name() : __Connector,
        __Indicator.name() : __Indicator
    })
_module_typeBindings.DependentLocalityType = DependentLocalityType
Namespace.addCategoryObject('typeBinding', 'DependentLocalityType', DependentLocalityType)


# Complex type [anonymous] with content type MIXED
class CTD_ANON_15 (pyxb.binding.basis.complexTypeDefinition):
    """Name of the dependent locality"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 330, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_15_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_15_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 331, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 331, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_15 = CTD_ANON_15


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}FirmType with content type ELEMENT_ONLY
class FirmType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}FirmType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FirmType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 403, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}FirmName uses Python identifier FirmName
    __FirmName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FirmName'), 'FirmName', '__urnoasisnamestcciqxsdschemaxAL2_0_FirmType_urnoasisnamestcciqxsdschemaxAL2_0FirmName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 406, 3), )

    
    FirmName = property(__FirmName.value, __FirmName.set, None, 'Name of the firm')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}MailStop uses Python identifier MailStop
    __MailStop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MailStop'), 'MailStop', '__urnoasisnamestcciqxsdschemaxAL2_0_FirmType_urnoasisnamestcciqxsdschemaxAL2_0MailStop', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 417, 3), )

    
    MailStop = property(__MailStop.value, __MailStop.set, None, 'A MailStop is where the the mail is delivered to within a premise/subpremise/firm or a facility.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_FirmType_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__urnoasisnamestcciqxsdschemaxAL2_0_FirmType_urnoasisnamestcciqxsdschemaxAL2_0PostalCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Department uses Python identifier Department
    __Department = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Department'), 'Department', '__urnoasisnamestcciqxsdschemaxAL2_0_FirmType_urnoasisnamestcciqxsdschemaxAL2_0Department', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1302, 1), )

    
    Department = property(__Department.value, __Department.set, None, 'Subdivision in the firm: School of Physics at Victoria University (School of Physics is the department)')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_FirmType_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 425, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 425, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __FirmName.name() : __FirmName,
        __MailStop.name() : __MailStop,
        __AddressLine.name() : __AddressLine,
        __PostalCode.name() : __PostalCode,
        __Department.name() : __Department
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.FirmType = FirmType
Namespace.addCategoryObject('typeBinding', 'FirmType', FirmType)


# Complex type [anonymous] with content type MIXED
class CTD_ANON_16 (pyxb.binding.basis.complexTypeDefinition):
    """Name of the firm"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 410, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_16_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_16_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 411, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 411, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_16 = CTD_ANON_16


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}LargeMailUserType with content type ELEMENT_ONLY
class LargeMailUserType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}LargeMailUserType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LargeMailUserType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 428, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}LargeMailUserName uses Python identifier LargeMailUserName
    __LargeMailUserName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LargeMailUserName'), 'LargeMailUserName', '__urnoasisnamestcciqxsdschemaxAL2_0_LargeMailUserType_urnoasisnamestcciqxsdschemaxAL2_0LargeMailUserName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 431, 3), )

    
    LargeMailUserName = property(__LargeMailUserName.value, __LargeMailUserName.set, None, 'Name of the large mail user. eg. Smith Ford International airport')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}LargeMailUserIdentifier uses Python identifier LargeMailUserIdentifier
    __LargeMailUserIdentifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LargeMailUserIdentifier'), 'LargeMailUserIdentifier', '__urnoasisnamestcciqxsdschemaxAL2_0_LargeMailUserType_urnoasisnamestcciqxsdschemaxAL2_0LargeMailUserIdentifier', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 445, 3), )

    
    LargeMailUserIdentifier = property(__LargeMailUserIdentifier.value, __LargeMailUserIdentifier.set, None, 'Specification of the identification number of a large mail user. An example are the Cedex codes in France.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}BuildingName uses Python identifier BuildingName
    __BuildingName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BuildingName'), 'BuildingName', '__urnoasisnamestcciqxsdschemaxAL2_0_LargeMailUserType_urnoasisnamestcciqxsdschemaxAL2_0BuildingName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 464, 3), )

    
    BuildingName = property(__BuildingName.value, __BuildingName.set, None, 'Name of the building')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_LargeMailUserType_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Thoroughfare uses Python identifier Thoroughfare
    __Thoroughfare = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare'), 'Thoroughfare', '__urnoasisnamestcciqxsdschemaxAL2_0_LargeMailUserType_urnoasisnamestcciqxsdschemaxAL2_0Thoroughfare', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 775, 1), )

    
    Thoroughfare = property(__Thoroughfare.value, __Thoroughfare.set, None, 'Specification of a thoroughfare. A thoroughfare could be a rd, street, canal, river, etc.  Note dependentlocality in a street. For example, in some countries, a large street will \nhave many subdivisions with numbers. Normally the subdivision name is the same as the road name, but with a number to identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__urnoasisnamestcciqxsdschemaxAL2_0_LargeMailUserType_urnoasisnamestcciqxsdschemaxAL2_0PostalCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostBox uses Python identifier PostBox
    __PostBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostBox'), 'PostBox', '__urnoasisnamestcciqxsdschemaxAL2_0_LargeMailUserType_urnoasisnamestcciqxsdschemaxAL2_0PostBox', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1223, 1), )

    
    PostBox = property(__PostBox.value, __PostBox.set, None, 'Specification of a postbox like mail delivery point. Only a single postbox number can be specified. Examples of postboxes are POBox, free mail numbers, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Department uses Python identifier Department
    __Department = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Department'), 'Department', '__urnoasisnamestcciqxsdschemaxAL2_0_LargeMailUserType_urnoasisnamestcciqxsdschemaxAL2_0Department', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1302, 1), )

    
    Department = property(__Department.value, __Department.set, None, 'Subdivision in the firm: School of Physics at Victoria University (School of Physics is the department)')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_LargeMailUserType_Type', pyxb.binding.datatypes.string)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 475, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 475, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __LargeMailUserName.name() : __LargeMailUserName,
        __LargeMailUserIdentifier.name() : __LargeMailUserIdentifier,
        __BuildingName.name() : __BuildingName,
        __AddressLine.name() : __AddressLine,
        __Thoroughfare.name() : __Thoroughfare,
        __PostalCode.name() : __PostalCode,
        __PostBox.name() : __PostBox,
        __Department.name() : __Department
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.LargeMailUserType = LargeMailUserType
Namespace.addCategoryObject('typeBinding', 'LargeMailUserType', LargeMailUserType)


# Complex type [anonymous] with content type MIXED
class CTD_ANON_17 (pyxb.binding.basis.complexTypeDefinition):
    """Name of the large mail user. eg. Smith Ford International airport"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 435, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_17_Type', pyxb.binding.datatypes.string)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 436, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 436, 5)
    
    Type = property(__Type.value, __Type.set, None, 'Airport, Hospital, etc')

    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_17_Code', pyxb.binding.datatypes.string)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 441, 5)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 441, 5)
    
    Code = property(__Code.value, __Code.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Code.name() : __Code
    })
_module_typeBindings.CTD_ANON_17 = CTD_ANON_17


# Complex type [anonymous] with content type MIXED
class CTD_ANON_18 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of the identification number of a large mail user. An example are the Cedex codes in France."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 449, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_18_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_18_Type', pyxb.binding.datatypes.string)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 450, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 450, 5)
    
    Type = property(__Type.value, __Type.set, None, 'CEDEX Code')

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_18_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 455, 5)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 455, 5)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, 'eg. Building 429 in which Building is the Indicator')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type,
        __Indicator.name() : __Indicator
    })
_module_typeBindings.CTD_ANON_18 = CTD_ANON_18


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}MailStopType with content type ELEMENT_ONLY
class MailStopType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}MailStopType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MailStopType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 478, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}MailStopName uses Python identifier MailStopName
    __MailStopName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MailStopName'), 'MailStopName', '__urnoasisnamestcciqxsdschemaxAL2_0_MailStopType_urnoasisnamestcciqxsdschemaxAL2_0MailStopName', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 481, 3), )

    
    MailStopName = property(__MailStopName.value, __MailStopName.set, None, 'Name of the the Mail Stop. eg. MSP, MS, etc')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}MailStopNumber uses Python identifier MailStopNumber
    __MailStopNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MailStopNumber'), 'MailStopNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_MailStopType_urnoasisnamestcciqxsdschemaxAL2_0MailStopNumber', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 491, 3), )

    
    MailStopNumber = property(__MailStopNumber.value, __MailStopNumber.set, None, 'Number of the Mail stop. eg. 123 in MS 123')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_MailStopType_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_MailStopType_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 507, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 507, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __MailStopName.name() : __MailStopName,
        __MailStopNumber.name() : __MailStopNumber,
        __AddressLine.name() : __AddressLine
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.MailStopType = MailStopType
Namespace.addCategoryObject('typeBinding', 'MailStopType', MailStopType)


# Complex type [anonymous] with content type MIXED
class CTD_ANON_19 (pyxb.binding.basis.complexTypeDefinition):
    """Name of the the Mail Stop. eg. MSP, MS, etc"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 485, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_19_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_19_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 486, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 486, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_19 = CTD_ANON_19


# Complex type [anonymous] with content type MIXED
class CTD_ANON_20 (pyxb.binding.basis.complexTypeDefinition):
    """Number of the Mail stop. eg. 123 in MS 123"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 495, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_20_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute NameNumberSeparator uses Python identifier NameNumberSeparator
    __NameNumberSeparator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NameNumberSeparator'), 'NameNumberSeparator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_20_NameNumberSeparator', pyxb.binding.datatypes.anySimpleType)
    __NameNumberSeparator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 496, 5)
    __NameNumberSeparator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 496, 5)
    
    NameNumberSeparator = property(__NameNumberSeparator.value, __NameNumberSeparator.set, None, '"-" in MS-123')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __NameNumberSeparator.name() : __NameNumberSeparator
    })
_module_typeBindings.CTD_ANON_20 = CTD_ANON_20


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalRouteType with content type ELEMENT_ONLY
class PostalRouteType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalRouteType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PostalRouteType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 510, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalRouteName uses Python identifier PostalRouteName
    __PostalRouteName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalRouteName'), 'PostalRouteName', '__urnoasisnamestcciqxsdschemaxAL2_0_PostalRouteType_urnoasisnamestcciqxsdschemaxAL2_0PostalRouteName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 514, 4), )

    
    PostalRouteName = property(__PostalRouteName.value, __PostalRouteName.set, None, ' Name of the Postal Route')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalRouteNumber uses Python identifier PostalRouteNumber
    __PostalRouteNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalRouteNumber'), 'PostalRouteNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_PostalRouteType_urnoasisnamestcciqxsdschemaxAL2_0PostalRouteNumber', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 524, 4), )

    
    PostalRouteNumber = property(__PostalRouteNumber.value, __PostalRouteNumber.set, None, ' Number of the Postal Route')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_PostalRouteType_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostBox uses Python identifier PostBox
    __PostBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostBox'), 'PostBox', '__urnoasisnamestcciqxsdschemaxAL2_0_PostalRouteType_urnoasisnamestcciqxsdschemaxAL2_0PostBox', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1223, 1), )

    
    PostBox = property(__PostBox.value, __PostBox.set, None, 'Specification of a postbox like mail delivery point. Only a single postbox number can be specified. Examples of postboxes are POBox, free mail numbers, etc.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_PostalRouteType_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 537, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 537, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __PostalRouteName.name() : __PostalRouteName,
        __PostalRouteNumber.name() : __PostalRouteNumber,
        __AddressLine.name() : __AddressLine,
        __PostBox.name() : __PostBox
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.PostalRouteType = PostalRouteType
Namespace.addCategoryObject('typeBinding', 'PostalRouteType', PostalRouteType)


# Complex type [anonymous] with content type MIXED
class CTD_ANON_21 (pyxb.binding.basis.complexTypeDefinition):
    """ Name of the Postal Route"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 518, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_21_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_21_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 519, 6)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 519, 6)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_21 = CTD_ANON_21


# Complex type [anonymous] with content type MIXED
class CTD_ANON_22 (pyxb.binding.basis.complexTypeDefinition):
    """ Number of the Postal Route"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 528, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_22_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code
    })
_module_typeBindings.CTD_ANON_22 = CTD_ANON_22


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremiseType with content type ELEMENT_ONLY
class SubPremiseType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremiseType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'SubPremiseType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 540, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremiseName uses Python identifier SubPremiseName
    __SubPremiseName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseName'), 'SubPremiseName', '__urnoasisnamestcciqxsdschemaxAL2_0_SubPremiseType_urnoasisnamestcciqxsdschemaxAL2_0SubPremiseName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 543, 3), )

    
    SubPremiseName = property(__SubPremiseName.value, __SubPremiseName.set, None, ' Name of the SubPremise')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremiseLocation uses Python identifier SubPremiseLocation
    __SubPremiseLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseLocation'), 'SubPremiseLocation', '__urnoasisnamestcciqxsdschemaxAL2_0_SubPremiseType_urnoasisnamestcciqxsdschemaxAL2_0SubPremiseLocation', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 565, 4), )

    
    SubPremiseLocation = property(__SubPremiseLocation.value, __SubPremiseLocation.set, None, ' Name of the SubPremise Location. eg. LOBBY, BASEMENT, GROUND FLOOR, etc...')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremiseNumber uses Python identifier SubPremiseNumber
    __SubPremiseNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseNumber'), 'SubPremiseNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_SubPremiseType_urnoasisnamestcciqxsdschemaxAL2_0SubPremiseNumber', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 573, 4), )

    
    SubPremiseNumber = property(__SubPremiseNumber.value, __SubPremiseNumber.set, None, ' Specification of the identifier of a sub-premise. Examples of sub-premises are apartments and suites. sub-premises in a building are often uniquely identified by means of consecutive\nidentifiers. The identifier can be a number, a letter or any combination of the two. In the latter case, the identifier includes exactly one variable (range) part, which is either a \nnumber or a single letter that is surrounded by fixed parts at the left (prefix) or the right (postfix).')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremiseNumberPrefix uses Python identifier SubPremiseNumberPrefix
    __SubPremiseNumberPrefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseNumberPrefix'), 'SubPremiseNumberPrefix', '__urnoasisnamestcciqxsdschemaxAL2_0_SubPremiseType_urnoasisnamestcciqxsdschemaxAL2_0SubPremiseNumberPrefix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 618, 3), )

    
    SubPremiseNumberPrefix = property(__SubPremiseNumberPrefix.value, __SubPremiseNumberPrefix.set, None, ' Prefix of the sub premise number. eg. A in A-12')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremiseNumberSuffix uses Python identifier SubPremiseNumberSuffix
    __SubPremiseNumberSuffix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseNumberSuffix'), 'SubPremiseNumberSuffix', '__urnoasisnamestcciqxsdschemaxAL2_0_SubPremiseType_urnoasisnamestcciqxsdschemaxAL2_0SubPremiseNumberSuffix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 633, 3), )

    
    SubPremiseNumberSuffix = property(__SubPremiseNumberSuffix.value, __SubPremiseNumberSuffix.set, None, ' Suffix of the sub premise number. eg. A in 12A')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}BuildingName uses Python identifier BuildingName
    __BuildingName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BuildingName'), 'BuildingName', '__urnoasisnamestcciqxsdschemaxAL2_0_SubPremiseType_urnoasisnamestcciqxsdschemaxAL2_0BuildingName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 648, 3), )

    
    BuildingName = property(__BuildingName.value, __BuildingName.set, None, 'Name of the building')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Firm uses Python identifier Firm
    __Firm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Firm'), 'Firm', '__urnoasisnamestcciqxsdschemaxAL2_0_SubPremiseType_urnoasisnamestcciqxsdschemaxAL2_0Firm', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 653, 3), )

    
    Firm = property(__Firm.value, __Firm.set, None, 'Specification of a firm, company, organization, etc. It can be specified as part of an address that contains a street or a postbox. It is therefore different from a large mail user address, which contains no street.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}MailStop uses Python identifier MailStop
    __MailStop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MailStop'), 'MailStop', '__urnoasisnamestcciqxsdschemaxAL2_0_SubPremiseType_urnoasisnamestcciqxsdschemaxAL2_0MailStop', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 658, 3), )

    
    MailStop = property(__MailStop.value, __MailStop.set, None, 'A MailStop is where the the mail is delivered to within a premise/subpremise/firm or a facility.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremise uses Python identifier SubPremise
    __SubPremise = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubPremise'), 'SubPremise', '__urnoasisnamestcciqxsdschemaxAL2_0_SubPremiseType_urnoasisnamestcciqxsdschemaxAL2_0SubPremise', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 664, 3), )

    
    SubPremise = property(__SubPremise.value, __SubPremise.set, None, 'Specification of a single sub-premise. Examples of sub-premises are apartments and suites. \nEach sub-premise should be uniquely identifiable. SubPremiseType: Specification of the name of a sub-premise type. Possible values not limited to: Suite, Appartment, Floor, Unknown\nMultiple levels within a premise by recursively calling SubPremise Eg. Level 4, Suite 2, Block C')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_SubPremiseType_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__urnoasisnamestcciqxsdschemaxAL2_0_SubPremiseType_urnoasisnamestcciqxsdschemaxAL2_0PostalCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_SubPremiseType_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 673, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 673, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __SubPremiseName.name() : __SubPremiseName,
        __SubPremiseLocation.name() : __SubPremiseLocation,
        __SubPremiseNumber.name() : __SubPremiseNumber,
        __SubPremiseNumberPrefix.name() : __SubPremiseNumberPrefix,
        __SubPremiseNumberSuffix.name() : __SubPremiseNumberSuffix,
        __BuildingName.name() : __BuildingName,
        __Firm.name() : __Firm,
        __MailStop.name() : __MailStop,
        __SubPremise.name() : __SubPremise,
        __AddressLine.name() : __AddressLine,
        __PostalCode.name() : __PostalCode
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.SubPremiseType = SubPremiseType
Namespace.addCategoryObject('typeBinding', 'SubPremiseType', SubPremiseType)


# Complex type [anonymous] with content type MIXED
class CTD_ANON_23 (pyxb.binding.basis.complexTypeDefinition):
    """ Name of the SubPremise Location. eg. LOBBY, BASEMENT, GROUND FLOOR, etc..."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 569, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_23_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code
    })
_module_typeBindings.CTD_ANON_23 = CTD_ANON_23


# Complex type [anonymous] with content type MIXED
class CTD_ANON_24 (pyxb.binding.basis.complexTypeDefinition):
    """ Prefix of the sub premise number. eg. A in A-12"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 622, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_24_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute NumberPrefixSeparator uses Python identifier NumberPrefixSeparator
    __NumberPrefixSeparator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberPrefixSeparator'), 'NumberPrefixSeparator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_24_NumberPrefixSeparator', pyxb.binding.datatypes.anySimpleType)
    __NumberPrefixSeparator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 623, 5)
    __NumberPrefixSeparator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 623, 5)
    
    NumberPrefixSeparator = property(__NumberPrefixSeparator.value, __NumberPrefixSeparator.set, None, 'A-12 where 12 is number and A is prefix and "-" is the separator')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_24_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 628, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 628, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __NumberPrefixSeparator.name() : __NumberPrefixSeparator,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_24 = CTD_ANON_24


# Complex type [anonymous] with content type MIXED
class CTD_ANON_25 (pyxb.binding.basis.complexTypeDefinition):
    """ Suffix of the sub premise number. eg. A in 12A"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 637, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_25_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute NumberSuffixSeparator uses Python identifier NumberSuffixSeparator
    __NumberSuffixSeparator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberSuffixSeparator'), 'NumberSuffixSeparator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_25_NumberSuffixSeparator', pyxb.binding.datatypes.anySimpleType)
    __NumberSuffixSeparator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 638, 5)
    __NumberSuffixSeparator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 638, 5)
    
    NumberSuffixSeparator = property(__NumberSuffixSeparator.value, __NumberSuffixSeparator.set, None, '12-A where 12 is number and A is suffix and "-" is the separator')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_25_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 643, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 643, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __NumberSuffixSeparator.name() : __NumberSuffixSeparator,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_25 = CTD_ANON_25


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareLeadingTypeType with content type MIXED
class ThoroughfareLeadingTypeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareLeadingTypeType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareLeadingTypeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 676, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_ThoroughfareLeadingTypeType_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_ThoroughfareLeadingTypeType_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 677, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 677, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.ThoroughfareLeadingTypeType = ThoroughfareLeadingTypeType
Namespace.addCategoryObject('typeBinding', 'ThoroughfareLeadingTypeType', ThoroughfareLeadingTypeType)


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNameType with content type MIXED
class ThoroughfareNameType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNameType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 681, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_ThoroughfareNameType_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_ThoroughfareNameType_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 682, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 682, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.ThoroughfareNameType = ThoroughfareNameType
Namespace.addCategoryObject('typeBinding', 'ThoroughfareNameType', ThoroughfareNameType)


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfarePostDirectionType with content type MIXED
class ThoroughfarePostDirectionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfarePostDirectionType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePostDirectionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 686, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_ThoroughfarePostDirectionType_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_ThoroughfarePostDirectionType_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 687, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 687, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.ThoroughfarePostDirectionType = ThoroughfarePostDirectionType
Namespace.addCategoryObject('typeBinding', 'ThoroughfarePostDirectionType', ThoroughfarePostDirectionType)


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfarePreDirectionType with content type MIXED
class ThoroughfarePreDirectionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfarePreDirectionType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePreDirectionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 691, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_ThoroughfarePreDirectionType_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_ThoroughfarePreDirectionType_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 692, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 692, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.ThoroughfarePreDirectionType = ThoroughfarePreDirectionType
Namespace.addCategoryObject('typeBinding', 'ThoroughfarePreDirectionType', ThoroughfarePreDirectionType)


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareTrailingTypeType with content type MIXED
class ThoroughfareTrailingTypeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareTrailingTypeType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareTrailingTypeType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 696, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_ThoroughfareTrailingTypeType_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_ThoroughfareTrailingTypeType_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 697, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 697, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.ThoroughfareTrailingTypeType = ThoroughfareTrailingTypeType
Namespace.addCategoryObject('typeBinding', 'ThoroughfareTrailingTypeType', ThoroughfareTrailingTypeType)


# Complex type [anonymous] with content type MIXED
class CTD_ANON_26 (pyxb.binding.basis.complexTypeDefinition):
    """Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 705, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_26_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_26_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 706, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 706, 3)
    
    Type = property(__Type.value, __Type.set, None, 'Defines the type of address line. eg. Street, Address Line 1, etc.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_26 = CTD_ANON_26


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_27 (pyxb.binding.basis.complexTypeDefinition):
    """Locality is one level lower than adminisstrative area. Eg.: cities, reservations and any other built-up areas."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 719, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}LocalityName uses Python identifier LocalityName
    __LocalityName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LocalityName'), 'LocalityName', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_urnoasisnamestcciqxsdschemaxAL2_0LocalityName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 722, 4), )

    
    LocalityName = property(__LocalityName.value, __LocalityName.set, None, 'Name of the locality')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}LargeMailUser uses Python identifier LargeMailUser
    __LargeMailUser = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'LargeMailUser'), 'LargeMailUser', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_urnoasisnamestcciqxsdschemaxAL2_0LargeMailUser', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 734, 5), )

    
    LargeMailUser = property(__LargeMailUser.value, __LargeMailUser.set, None, 'Specification of a large mail user address. Examples of large mail users are postal companies, companies in France with a cedex number, hospitals and airports with their own post code. Large mail user addresses do not have a street name with premise name or premise number in countries like Netherlands. But they have a POBox and street also in countries like France')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalRoute uses Python identifier PostalRoute
    __PostalRoute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalRoute'), 'PostalRoute', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_urnoasisnamestcciqxsdschemaxAL2_0PostalRoute', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 740, 5), )

    
    PostalRoute = property(__PostalRoute.value, __PostalRoute.set, None, 'A Postal van is specific for a route as in Is`rael, Rural route')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentLocality uses Python identifier DependentLocality
    __DependentLocality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DependentLocality'), 'DependentLocality', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_urnoasisnamestcciqxsdschemaxAL2_0DependentLocality', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 748, 4), )

    
    DependentLocality = property(__DependentLocality.value, __DependentLocality.set, None, 'Dependent localities are Districts within cities/towns, locality divisions, postal \ndivisions of cities, suburbs, etc. DependentLocality is a recursive element, but no nesting deeper than two exists (Locality-DependentLocality-DependentLocality).')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Thoroughfare uses Python identifier Thoroughfare
    __Thoroughfare = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare'), 'Thoroughfare', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_urnoasisnamestcciqxsdschemaxAL2_0Thoroughfare', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 775, 1), )

    
    Thoroughfare = property(__Thoroughfare.value, __Thoroughfare.set, None, 'Specification of a thoroughfare. A thoroughfare could be a rd, street, canal, river, etc.  Note dependentlocality in a street. For example, in some countries, a large street will \nhave many subdivisions with numbers. Normally the subdivision name is the same as the road name, but with a number to identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostOffice uses Python identifier PostOffice
    __PostOffice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostOffice'), 'PostOffice', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_urnoasisnamestcciqxsdschemaxAL2_0PostOffice', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1072, 1), )

    
    PostOffice = property(__PostOffice.value, __PostOffice.set, None, 'Specification of a post office. Examples are a rural post office where post is delivered and a post office containing post office boxes.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_urnoasisnamestcciqxsdschemaxAL2_0PostalCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostBox uses Python identifier PostBox
    __PostBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostBox'), 'PostBox', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_urnoasisnamestcciqxsdschemaxAL2_0PostBox', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1223, 1), )

    
    PostBox = property(__PostBox.value, __PostBox.set, None, 'Specification of a postbox like mail delivery point. Only a single postbox number can be specified. Examples of postboxes are POBox, free mail numbers, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Premise uses Python identifier Premise
    __Premise = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Premise'), 'Premise', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_urnoasisnamestcciqxsdschemaxAL2_0Premise', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1335, 1), )

    
    Premise = property(__Premise.value, __Premise.set, None, 'Specification of a single premise, for example a house or a building. The premise as a whole has a unique premise (house) number or a premise name.  There could be more than \none premise in a street referenced in an address. For example a building address near a major shopping centre or raiwlay station')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 757, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 757, 3)
    
    Type = property(__Type.value, __Type.set, None, 'Possible values not limited to: City, IndustrialEstate, etc')

    
    # Attribute UsageType uses Python identifier UsageType
    __UsageType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UsageType'), 'UsageType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_UsageType', pyxb.binding.datatypes.anySimpleType)
    __UsageType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 762, 3)
    __UsageType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 762, 3)
    
    UsageType = property(__UsageType.value, __UsageType.set, None, 'Postal or Political - Sometimes locations must be distinguished between postal system, and physical locations as defined by a political system')

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_27_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 767, 3)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 767, 3)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, 'Erode (Dist) where (Dist) is the Indicator')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __LocalityName.name() : __LocalityName,
        __LargeMailUser.name() : __LargeMailUser,
        __PostalRoute.name() : __PostalRoute,
        __DependentLocality.name() : __DependentLocality,
        __Thoroughfare.name() : __Thoroughfare,
        __PostOffice.name() : __PostOffice,
        __PostalCode.name() : __PostalCode,
        __PostBox.name() : __PostBox,
        __Premise.name() : __Premise
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __UsageType.name() : __UsageType,
        __Indicator.name() : __Indicator
    })
_module_typeBindings.CTD_ANON_27 = CTD_ANON_27


# Complex type [anonymous] with content type MIXED
class CTD_ANON_28 (pyxb.binding.basis.complexTypeDefinition):
    """Name of the locality"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 726, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_28_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_28_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 727, 6)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 727, 6)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_28 = CTD_ANON_28


# Complex type [anonymous] with content type MIXED
class CTD_ANON_29 (pyxb.binding.basis.complexTypeDefinition):
    """Starting number in the range"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 796, 9)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_29_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumberPrefix uses Python identifier ThoroughfareNumberPrefix
    __ThoroughfareNumberPrefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberPrefix'), 'ThoroughfareNumberPrefix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_29_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareNumberPrefix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1504, 1), )

    
    ThoroughfareNumberPrefix = property(__ThoroughfareNumberPrefix.value, __ThoroughfareNumberPrefix.set, None, 'Prefix before the number. A in A12 Archer Street')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumberSuffix uses Python identifier ThoroughfareNumberSuffix
    __ThoroughfareNumberSuffix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberSuffix'), 'ThoroughfareNumberSuffix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_29_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareNumberSuffix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1518, 1), )

    
    ThoroughfareNumberSuffix = property(__ThoroughfareNumberSuffix.value, __ThoroughfareNumberSuffix.set, None, 'Suffix after the number. A in 12A Archer Street')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumber uses Python identifier ThoroughfareNumber
    __ThoroughfareNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumber'), 'ThoroughfareNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_29_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareNumber', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1534, 1), )

    
    ThoroughfareNumber = property(__ThoroughfareNumber.value, __ThoroughfareNumber.set, None, 'Eg.: 23 Archer street or 25/15 Zero Avenue, etc')

    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_29_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __ThoroughfareNumberPrefix.name() : __ThoroughfareNumberPrefix,
        __ThoroughfareNumberSuffix.name() : __ThoroughfareNumberSuffix,
        __ThoroughfareNumber.name() : __ThoroughfareNumber
    })
    _AttributeMap.update({
        __Code.name() : __Code
    })
_module_typeBindings.CTD_ANON_29 = CTD_ANON_29


# Complex type [anonymous] with content type MIXED
class CTD_ANON_30 (pyxb.binding.basis.complexTypeDefinition):
    """Ending number in the range"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 811, 9)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_30_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumberPrefix uses Python identifier ThoroughfareNumberPrefix
    __ThoroughfareNumberPrefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberPrefix'), 'ThoroughfareNumberPrefix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_30_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareNumberPrefix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1504, 1), )

    
    ThoroughfareNumberPrefix = property(__ThoroughfareNumberPrefix.value, __ThoroughfareNumberPrefix.set, None, 'Prefix before the number. A in A12 Archer Street')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumberSuffix uses Python identifier ThoroughfareNumberSuffix
    __ThoroughfareNumberSuffix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberSuffix'), 'ThoroughfareNumberSuffix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_30_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareNumberSuffix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1518, 1), )

    
    ThoroughfareNumberSuffix = property(__ThoroughfareNumberSuffix.value, __ThoroughfareNumberSuffix.set, None, 'Suffix after the number. A in 12A Archer Street')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumber uses Python identifier ThoroughfareNumber
    __ThoroughfareNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumber'), 'ThoroughfareNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_30_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareNumber', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1534, 1), )

    
    ThoroughfareNumber = property(__ThoroughfareNumber.value, __ThoroughfareNumber.set, None, 'Eg.: 23 Archer street or 25/15 Zero Avenue, etc')

    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_30_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __ThoroughfareNumberPrefix.name() : __ThoroughfareNumberPrefix,
        __ThoroughfareNumberSuffix.name() : __ThoroughfareNumberSuffix,
        __ThoroughfareNumber.name() : __ThoroughfareNumber
    })
    _AttributeMap.update({
        __Code.name() : __Code
    })
_module_typeBindings.CTD_ANON_30 = CTD_ANON_30


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_31 (pyxb.binding.basis.complexTypeDefinition):
    """DependentThroughfare is related to a street; occurs in GB, IE, ES, PT"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 905, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_31_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfarePreDirection uses Python identifier ThoroughfarePreDirection
    __ThoroughfarePreDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePreDirection'), 'ThoroughfarePreDirection', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_31_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfarePreDirection', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 908, 7), )

    
    ThoroughfarePreDirection = property(__ThoroughfarePreDirection.value, __ThoroughfarePreDirection.set, None, 'North Baker Street, where North is the pre-direction. The direction appears before the name.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareLeadingType uses Python identifier ThoroughfareLeadingType
    __ThoroughfareLeadingType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareLeadingType'), 'ThoroughfareLeadingType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_31_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareLeadingType', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 913, 7), )

    
    ThoroughfareLeadingType = property(__ThoroughfareLeadingType.value, __ThoroughfareLeadingType.set, None, 'Appears before the thoroughfare name. Ed. Spanish: Avenida Aurora, where Avenida is the leading type / French: Rue Moliere, where Rue is the leading type.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareName uses Python identifier ThoroughfareName
    __ThoroughfareName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareName'), 'ThoroughfareName', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_31_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 918, 7), )

    
    ThoroughfareName = property(__ThoroughfareName.value, __ThoroughfareName.set, None, 'Specification of the name of a Thoroughfare (also dependant street name): street name, canal name, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareTrailingType uses Python identifier ThoroughfareTrailingType
    __ThoroughfareTrailingType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareTrailingType'), 'ThoroughfareTrailingType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_31_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareTrailingType', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 923, 7), )

    
    ThoroughfareTrailingType = property(__ThoroughfareTrailingType.value, __ThoroughfareTrailingType.set, None, 'Appears after the thoroughfare name. Ed. British: Baker Lane, where Lane is the trailing type.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfarePostDirection uses Python identifier ThoroughfarePostDirection
    __ThoroughfarePostDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePostDirection'), 'ThoroughfarePostDirection', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_31_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfarePostDirection', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 928, 7), )

    
    ThoroughfarePostDirection = property(__ThoroughfarePostDirection.value, __ThoroughfarePostDirection.set, None, '221-bis Baker Street North, where North is the post-direction. The post-direction appears after the name.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_31_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 935, 6)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 935, 6)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __ThoroughfarePreDirection.name() : __ThoroughfarePreDirection,
        __ThoroughfareLeadingType.name() : __ThoroughfareLeadingType,
        __ThoroughfareName.name() : __ThoroughfareName,
        __ThoroughfareTrailingType.name() : __ThoroughfareTrailingType,
        __ThoroughfarePostDirection.name() : __ThoroughfarePostDirection
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_31 = CTD_ANON_31


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_32 (pyxb.binding.basis.complexTypeDefinition):
    """Examples of administrative areas are provinces counties, special regions (such as "Rijnmond"), etc."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 991, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_32_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Locality uses Python identifier Locality
    __Locality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Locality'), 'Locality', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_32_urnoasisnamestcciqxsdschemaxAL2_0Locality', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 715, 1), )

    
    Locality = property(__Locality.value, __Locality.set, None, 'Locality is one level lower than adminisstrative area. Eg.: cities, reservations and any other built-up areas.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AdministrativeAreaName uses Python identifier AdministrativeAreaName
    __AdministrativeAreaName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeAreaName'), 'AdministrativeAreaName', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_32_urnoasisnamestcciqxsdschemaxAL2_0AdministrativeAreaName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 994, 4), )

    
    AdministrativeAreaName = property(__AdministrativeAreaName.value, __AdministrativeAreaName.set, None, ' Name of the administrative area. eg. MI in USA, NSW in Australia')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubAdministrativeArea uses Python identifier SubAdministrativeArea
    __SubAdministrativeArea = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubAdministrativeArea'), 'SubAdministrativeArea', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_32_urnoasisnamestcciqxsdschemaxAL2_0SubAdministrativeArea', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1004, 4), )

    
    SubAdministrativeArea = property(__SubAdministrativeArea.value, __SubAdministrativeArea.set, None, ' Specification of a sub-administrative area. An example of a sub-administrative areas is a county. There are two places where the name of an administrative \narea can be specified and in this case, one becomes sub-administrative area.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostOffice uses Python identifier PostOffice
    __PostOffice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostOffice'), 'PostOffice', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_32_urnoasisnamestcciqxsdschemaxAL2_0PostOffice', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1072, 1), )

    
    PostOffice = property(__PostOffice.value, __PostOffice.set, None, 'Specification of a post office. Examples are a rural post office where post is delivered and a post office containing post office boxes.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_32_urnoasisnamestcciqxsdschemaxAL2_0PostalCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_32_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1054, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1054, 3)
    
    Type = property(__Type.value, __Type.set, None, 'Province or State or County or Kanton, etc')

    
    # Attribute UsageType uses Python identifier UsageType
    __UsageType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UsageType'), 'UsageType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_32_UsageType', pyxb.binding.datatypes.anySimpleType)
    __UsageType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1059, 3)
    __UsageType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1059, 3)
    
    UsageType = property(__UsageType.value, __UsageType.set, None, 'Postal or Political - Sometimes locations must be distinguished between postal system, and physical locations as defined by a political system')

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_32_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1064, 3)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1064, 3)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, 'Erode (Dist) where (Dist) is the Indicator')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __Locality.name() : __Locality,
        __AdministrativeAreaName.name() : __AdministrativeAreaName,
        __SubAdministrativeArea.name() : __SubAdministrativeArea,
        __PostOffice.name() : __PostOffice,
        __PostalCode.name() : __PostalCode
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __UsageType.name() : __UsageType,
        __Indicator.name() : __Indicator
    })
_module_typeBindings.CTD_ANON_32 = CTD_ANON_32


# Complex type [anonymous] with content type MIXED
class CTD_ANON_33 (pyxb.binding.basis.complexTypeDefinition):
    """ Name of the administrative area. eg. MI in USA, NSW in Australia"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 998, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_33_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_33_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 999, 6)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 999, 6)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_33 = CTD_ANON_33


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_34 (pyxb.binding.basis.complexTypeDefinition):
    """ Specification of a sub-administrative area. An example of a sub-administrative areas is a county. There are two places where the name of an administrative 
area can be specified and in this case, one becomes sub-administrative area."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1009, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_34_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Locality uses Python identifier Locality
    __Locality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Locality'), 'Locality', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_34_urnoasisnamestcciqxsdschemaxAL2_0Locality', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 715, 1), )

    
    Locality = property(__Locality.value, __Locality.set, None, 'Locality is one level lower than adminisstrative area. Eg.: cities, reservations and any other built-up areas.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubAdministrativeAreaName uses Python identifier SubAdministrativeAreaName
    __SubAdministrativeAreaName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubAdministrativeAreaName'), 'SubAdministrativeAreaName', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_34_urnoasisnamestcciqxsdschemaxAL2_0SubAdministrativeAreaName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1012, 7), )

    
    SubAdministrativeAreaName = property(__SubAdministrativeAreaName.value, __SubAdministrativeAreaName.set, None, ' Name of the sub-administrative area')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostOffice uses Python identifier PostOffice
    __PostOffice = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostOffice'), 'PostOffice', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_34_urnoasisnamestcciqxsdschemaxAL2_0PostOffice', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1072, 1), )

    
    PostOffice = property(__PostOffice.value, __PostOffice.set, None, 'Specification of a post office. Examples are a rural post office where post is delivered and a post office containing post office boxes.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_34_urnoasisnamestcciqxsdschemaxAL2_0PostalCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_34_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1029, 6)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1029, 6)
    
    Type = property(__Type.value, __Type.set, None, 'Province or State or County or Kanton, etc')

    
    # Attribute UsageType uses Python identifier UsageType
    __UsageType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'UsageType'), 'UsageType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_34_UsageType', pyxb.binding.datatypes.anySimpleType)
    __UsageType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1034, 6)
    __UsageType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1034, 6)
    
    UsageType = property(__UsageType.value, __UsageType.set, None, 'Postal or Political - Sometimes locations must be distinguished between postal system, and physical locations as defined by a political system')

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_34_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1039, 6)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1039, 6)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, 'Erode (Dist) where (Dist) is the Indicator')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __Locality.name() : __Locality,
        __SubAdministrativeAreaName.name() : __SubAdministrativeAreaName,
        __PostOffice.name() : __PostOffice,
        __PostalCode.name() : __PostalCode
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __UsageType.name() : __UsageType,
        __Indicator.name() : __Indicator
    })
_module_typeBindings.CTD_ANON_34 = CTD_ANON_34


# Complex type [anonymous] with content type MIXED
class CTD_ANON_35 (pyxb.binding.basis.complexTypeDefinition):
    """ Name of the sub-administrative area"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1016, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_35_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_35_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1017, 9)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1017, 9)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_35 = CTD_ANON_35


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_36 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of a post office. Examples are a rural post office where post is delivered and a post office containing post office boxes."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1076, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_36_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostOfficeName uses Python identifier PostOfficeName
    __PostOfficeName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostOfficeName'), 'PostOfficeName', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_36_urnoasisnamestcciqxsdschemaxAL2_0PostOfficeName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1080, 5), )

    
    PostOfficeName = property(__PostOfficeName.value, __PostOfficeName.set, None, 'Specification of the name of the post office. This can be a rural postoffice where post is delivered or a post office containing post office boxes.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostOfficeNumber uses Python identifier PostOfficeNumber
    __PostOfficeNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostOfficeNumber'), 'PostOfficeNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_36_urnoasisnamestcciqxsdschemaxAL2_0PostOfficeNumber', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1090, 5), )

    
    PostOfficeNumber = property(__PostOfficeNumber.value, __PostOfficeNumber.set, None, 'Specification of the number of the postoffice. Common in rural postoffices')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalRoute uses Python identifier PostalRoute
    __PostalRoute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalRoute'), 'PostalRoute', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_36_urnoasisnamestcciqxsdschemaxAL2_0PostalRoute', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1116, 4), )

    
    PostalRoute = property(__PostalRoute.value, __PostalRoute.set, None, 'A Postal van is specific for a route as in Is`rael, Rural route')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_36_urnoasisnamestcciqxsdschemaxAL2_0PostalCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostBox uses Python identifier PostBox
    __PostBox = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostBox'), 'PostBox', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_36_urnoasisnamestcciqxsdschemaxAL2_0PostBox', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1223, 1), )

    
    PostBox = property(__PostBox.value, __PostBox.set, None, 'Specification of a postbox like mail delivery point. Only a single postbox number can be specified. Examples of postboxes are POBox, free mail numbers, etc.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_36_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1125, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1125, 3)
    
    Type = property(__Type.value, __Type.set, None, 'Could be a Mobile Postoffice Van as in Isreal')

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_36_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1130, 3)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1130, 3)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, 'eg. Kottivakkam (P.O) here (P.O) is the Indicator')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __PostOfficeName.name() : __PostOfficeName,
        __PostOfficeNumber.name() : __PostOfficeNumber,
        __PostalRoute.name() : __PostalRoute,
        __PostalCode.name() : __PostalCode,
        __PostBox.name() : __PostBox
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Indicator.name() : __Indicator
    })
_module_typeBindings.CTD_ANON_36 = CTD_ANON_36


# Complex type [anonymous] with content type MIXED
class CTD_ANON_37 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of the name of the post office. This can be a rural postoffice where post is delivered or a post office containing post office boxes."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1084, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_37_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_37_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1085, 7)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1085, 7)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_37 = CTD_ANON_37


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_38 (pyxb.binding.basis.complexTypeDefinition):
    """PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1142, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_38_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCodeNumber uses Python identifier PostalCodeNumber
    __PostalCodeNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCodeNumber'), 'PostalCodeNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_38_urnoasisnamestcciqxsdschemaxAL2_0PostalCodeNumber', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1145, 4), )

    
    PostalCodeNumber = property(__PostalCodeNumber.value, __PostalCodeNumber.set, None, 'Specification of a postcode. The postcode is formatted according to country-specific rules. Example: SW3 0A8-1A, 600074, 2067')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCodeNumberExtension uses Python identifier PostalCodeNumberExtension
    __PostalCodeNumberExtension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCodeNumberExtension'), 'PostalCodeNumberExtension', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_38_urnoasisnamestcciqxsdschemaxAL2_0PostalCodeNumberExtension', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1159, 4), )

    
    PostalCodeNumberExtension = property(__PostalCodeNumberExtension.value, __PostalCodeNumberExtension.set, None, 'Examples are: 1234 (USA), 1G (UK), etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostTown uses Python identifier PostTown
    __PostTown = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostTown'), 'PostTown', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_38_urnoasisnamestcciqxsdschemaxAL2_0PostTown', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1178, 4), )

    
    PostTown = property(__PostTown.value, __PostTown.set, None, 'A post town is not the same as a locality. A post town can encompass a collection of (small) localities. It can also be a subpart of a locality. An actual post town in Norway is "Bergen".')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_38_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1215, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1215, 3)
    
    Type = property(__Type.value, __Type.set, None, 'Area Code, Postcode, Delivery code as in NZ, etc')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __PostalCodeNumber.name() : __PostalCodeNumber,
        __PostalCodeNumberExtension.name() : __PostalCodeNumberExtension,
        __PostTown.name() : __PostTown
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_38 = CTD_ANON_38


# Complex type [anonymous] with content type MIXED
class CTD_ANON_39 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of a postcode. The postcode is formatted according to country-specific rules. Example: SW3 0A8-1A, 600074, 2067"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1149, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_39_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_39_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1150, 6)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1150, 6)
    
    Type = property(__Type.value, __Type.set, None, 'Old Postal Code, new code, etc')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_39 = CTD_ANON_39


# Complex type [anonymous] with content type MIXED
class CTD_ANON_40 (pyxb.binding.basis.complexTypeDefinition):
    """Examples are: 1234 (USA), 1G (UK), etc."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1163, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_40_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_40_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1164, 6)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1164, 6)
    
    Type = property(__Type.value, __Type.set, None, 'Delivery Point Suffix, New Postal Code, etc..')

    
    # Attribute NumberExtensionSeparator uses Python identifier NumberExtensionSeparator
    __NumberExtensionSeparator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberExtensionSeparator'), 'NumberExtensionSeparator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_40_NumberExtensionSeparator', pyxb.binding.datatypes.anySimpleType)
    __NumberExtensionSeparator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1169, 6)
    __NumberExtensionSeparator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1169, 6)
    
    NumberExtensionSeparator = property(__NumberExtensionSeparator.value, __NumberExtensionSeparator.set, None, 'The separator between postal code number and the extension. Eg. "-"')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type,
        __NumberExtensionSeparator.name() : __NumberExtensionSeparator
    })
_module_typeBindings.CTD_ANON_40 = CTD_ANON_40


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_41 (pyxb.binding.basis.complexTypeDefinition):
    """A post town is not the same as a locality. A post town can encompass a collection of (small) localities. It can also be a subpart of a locality. An actual post town in Norway is "Bergen"."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1182, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_41_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostTownName uses Python identifier PostTownName
    __PostTownName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostTownName'), 'PostTownName', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_41_urnoasisnamestcciqxsdschemaxAL2_0PostTownName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1185, 7), )

    
    PostTownName = property(__PostTownName.value, __PostTownName.set, None, 'Name of the post town')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostTownSuffix uses Python identifier PostTownSuffix
    __PostTownSuffix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostTownSuffix'), 'PostTownSuffix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_41_urnoasisnamestcciqxsdschemaxAL2_0PostTownSuffix', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1195, 7), )

    
    PostTownSuffix = property(__PostTownSuffix.value, __PostTownSuffix.set, None, 'GENERAL PO in MIAMI GENERAL PO')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_41_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1205, 6)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1205, 6)
    
    Type = property(__Type.value, __Type.set, None, 'eg. village, town, suburb, etc')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __PostTownName.name() : __PostTownName,
        __PostTownSuffix.name() : __PostTownSuffix
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_41 = CTD_ANON_41


# Complex type [anonymous] with content type MIXED
class CTD_ANON_42 (pyxb.binding.basis.complexTypeDefinition):
    """Name of the post town"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1189, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_42_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_42_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1190, 9)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1190, 9)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_42 = CTD_ANON_42


# Complex type [anonymous] with content type MIXED
class CTD_ANON_43 (pyxb.binding.basis.complexTypeDefinition):
    """GENERAL PO in MIAMI GENERAL PO"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1199, 8)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_43_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code
    })
_module_typeBindings.CTD_ANON_43 = CTD_ANON_43


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_44 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of a postbox like mail delivery point. Only a single postbox number can be specified. Examples of postboxes are POBox, free mail numbers, etc."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1227, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_44_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_44_urnoasisnamestcciqxsdschemaxAL2_0PostalCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostBoxNumber uses Python identifier PostBoxNumber
    __PostBoxNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostBoxNumber'), 'PostBoxNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_44_urnoasisnamestcciqxsdschemaxAL2_0PostBoxNumber', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1230, 4), )

    
    PostBoxNumber = property(__PostBoxNumber.value, __PostBoxNumber.set, None, 'Specification of the number of a postbox')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostBoxNumberPrefix uses Python identifier PostBoxNumberPrefix
    __PostBoxNumberPrefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostBoxNumberPrefix'), 'PostBoxNumberPrefix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_44_urnoasisnamestcciqxsdschemaxAL2_0PostBoxNumberPrefix', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1239, 4), )

    
    PostBoxNumberPrefix = property(__PostBoxNumberPrefix.value, __PostBoxNumberPrefix.set, None, 'Specification of the prefix of the post box number. eg. A in POBox:A-123')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostBoxNumberSuffix uses Python identifier PostBoxNumberSuffix
    __PostBoxNumberSuffix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostBoxNumberSuffix'), 'PostBoxNumberSuffix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_44_urnoasisnamestcciqxsdschemaxAL2_0PostBoxNumberSuffix', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1253, 4), )

    
    PostBoxNumberSuffix = property(__PostBoxNumberSuffix.value, __PostBoxNumberSuffix.set, None, 'Specification of the suffix of the post box number. eg. A in POBox:123A')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostBoxNumberExtension uses Python identifier PostBoxNumberExtension
    __PostBoxNumberExtension = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostBoxNumberExtension'), 'PostBoxNumberExtension', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_44_urnoasisnamestcciqxsdschemaxAL2_0PostBoxNumberExtension', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1267, 4), )

    
    PostBoxNumberExtension = property(__PostBoxNumberExtension.value, __PostBoxNumberExtension.set, None, 'Some countries like USA have POBox as 12345-123')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Firm uses Python identifier Firm
    __Firm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Firm'), 'Firm', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_44_urnoasisnamestcciqxsdschemaxAL2_0Firm', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1280, 4), )

    
    Firm = property(__Firm.value, __Firm.set, None, 'Specification of a firm, company, organization, etc. It can be specified as part of an address that contains a street or a postbox. It is therefore different from \na large mail user address, which contains no street.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_44_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1289, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1289, 3)
    
    Type = property(__Type.value, __Type.set, None, 'Possible values are, not limited to: POBox and Freepost.')

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_44_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1294, 3)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1294, 3)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, 'LOCKED BAG NO:1234 where the Indicator is NO: and Type is LOCKED BAG')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __PostalCode.name() : __PostalCode,
        __PostBoxNumber.name() : __PostBoxNumber,
        __PostBoxNumberPrefix.name() : __PostBoxNumberPrefix,
        __PostBoxNumberSuffix.name() : __PostBoxNumberSuffix,
        __PostBoxNumberExtension.name() : __PostBoxNumberExtension,
        __Firm.name() : __Firm
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __Indicator.name() : __Indicator
    })
_module_typeBindings.CTD_ANON_44 = CTD_ANON_44


# Complex type [anonymous] with content type MIXED
class CTD_ANON_45 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of the number of a postbox"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1234, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_45_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code
    })
_module_typeBindings.CTD_ANON_45 = CTD_ANON_45


# Complex type [anonymous] with content type MIXED
class CTD_ANON_46 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of the prefix of the post box number. eg. A in POBox:A-123"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1243, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_46_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute NumberPrefixSeparator uses Python identifier NumberPrefixSeparator
    __NumberPrefixSeparator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberPrefixSeparator'), 'NumberPrefixSeparator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_46_NumberPrefixSeparator', pyxb.binding.datatypes.anySimpleType)
    __NumberPrefixSeparator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1244, 6)
    __NumberPrefixSeparator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1244, 6)
    
    NumberPrefixSeparator = property(__NumberPrefixSeparator.value, __NumberPrefixSeparator.set, None, 'A-12 where 12 is number and A is prefix and "-" is the separator')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __NumberPrefixSeparator.name() : __NumberPrefixSeparator
    })
_module_typeBindings.CTD_ANON_46 = CTD_ANON_46


# Complex type [anonymous] with content type MIXED
class CTD_ANON_47 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of the suffix of the post box number. eg. A in POBox:123A"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1257, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_47_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute NumberSuffixSeparator uses Python identifier NumberSuffixSeparator
    __NumberSuffixSeparator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberSuffixSeparator'), 'NumberSuffixSeparator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_47_NumberSuffixSeparator', pyxb.binding.datatypes.anySimpleType)
    __NumberSuffixSeparator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1258, 6)
    __NumberSuffixSeparator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1258, 6)
    
    NumberSuffixSeparator = property(__NumberSuffixSeparator.value, __NumberSuffixSeparator.set, None, '12-A where 12 is number and A is suffix and "-" is the separator')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __NumberSuffixSeparator.name() : __NumberSuffixSeparator
    })
_module_typeBindings.CTD_ANON_47 = CTD_ANON_47


# Complex type [anonymous] with content type MIXED
class CTD_ANON_48 (pyxb.binding.basis.complexTypeDefinition):
    """Some countries like USA have POBox as 12345-123"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1271, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute NumberExtensionSeparator uses Python identifier NumberExtensionSeparator
    __NumberExtensionSeparator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberExtensionSeparator'), 'NumberExtensionSeparator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_48_NumberExtensionSeparator', pyxb.binding.datatypes.anySimpleType)
    __NumberExtensionSeparator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1272, 6)
    __NumberExtensionSeparator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1272, 6)
    
    NumberExtensionSeparator = property(__NumberExtensionSeparator.value, __NumberExtensionSeparator.set, None, '"-" is the NumberExtensionSeparator in POBOX:12345-123')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __NumberExtensionSeparator.name() : __NumberExtensionSeparator
    })
_module_typeBindings.CTD_ANON_48 = CTD_ANON_48


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_49 (pyxb.binding.basis.complexTypeDefinition):
    """Subdivision in the firm: School of Physics at Victoria University (School of Physics is the department)"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1306, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_49_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_49_urnoasisnamestcciqxsdschemaxAL2_0PostalCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DepartmentName uses Python identifier DepartmentName
    __DepartmentName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DepartmentName'), 'DepartmentName', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_49_urnoasisnamestcciqxsdschemaxAL2_0DepartmentName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1309, 4), )

    
    DepartmentName = property(__DepartmentName.value, __DepartmentName.set, None, 'Specification of the name of a department.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}MailStop uses Python identifier MailStop
    __MailStop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MailStop'), 'MailStop', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_49_urnoasisnamestcciqxsdschemaxAL2_0MailStop', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1319, 4), )

    
    MailStop = property(__MailStop.value, __MailStop.set, None, 'A MailStop is where the the mail is delivered to within a premise/subpremise/firm or a facility.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_49_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1327, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1327, 3)
    
    Type = property(__Type.value, __Type.set, None, 'School in Physics School, Division in Radiology division of school of physics')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __PostalCode.name() : __PostalCode,
        __DepartmentName.name() : __DepartmentName,
        __MailStop.name() : __MailStop
    })
    _AttributeMap.update({
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_49 = CTD_ANON_49


# Complex type [anonymous] with content type MIXED
class CTD_ANON_50 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of the name of a department."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1313, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_50_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_50_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1314, 6)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1314, 6)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_50 = CTD_ANON_50


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_51 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of a single premise, for example a house or a building. The premise as a whole has a unique premise (house) number or a premise name.  There could be more than 
one premise in a street referenced in an address. For example a building address near a major shopping centre or raiwlay station"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1340, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0PostalCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Premise uses Python identifier Premise
    __Premise = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Premise'), 'Premise', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0Premise', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1335, 1), )

    
    Premise = property(__Premise.value, __Premise.set, None, 'Specification of a single premise, for example a house or a building. The premise as a whole has a unique premise (house) number or a premise name.  There could be more than \none premise in a street referenced in an address. For example a building address near a major shopping centre or raiwlay station')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseName uses Python identifier PremiseName
    __PremiseName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseName'), 'PremiseName', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0PremiseName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1343, 4), )

    
    PremiseName = property(__PremiseName.value, __PremiseName.set, None, 'Specification of the name of the premise (house, building, park, farm, etc). A premise name is specified when the premise cannot be addressed using a street name plus premise (house) number.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseLocation uses Python identifier PremiseLocation
    __PremiseLocation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseLocation'), 'PremiseLocation', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0PremiseLocation', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1365, 5), )

    
    PremiseLocation = property(__PremiseLocation.value, __PremiseLocation.set, None, 'LOBBY, BASEMENT, GROUND FLOOR, etc...')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberRange uses Python identifier PremiseNumberRange
    __PremiseNumberRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberRange'), 'PremiseNumberRange', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0PremiseNumberRange', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1376, 6), )

    
    PremiseNumberRange = property(__PremiseNumberRange.value, __PremiseNumberRange.set, None, 'Specification for defining the premise number range. Some premises have number as Building C1-C7')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}BuildingName uses Python identifier BuildingName
    __BuildingName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BuildingName'), 'BuildingName', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0BuildingName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1455, 4), )

    
    BuildingName = property(__BuildingName.value, __BuildingName.set, None, 'Specification of the name of a building.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}SubPremise uses Python identifier SubPremise
    __SubPremise = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'SubPremise'), 'SubPremise', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0SubPremise', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1461, 5), )

    
    SubPremise = property(__SubPremise.value, __SubPremise.set, None, 'Specification of a single sub-premise. Examples of sub-premises are apartments and suites. Each sub-premise should be uniquely identifiable.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Firm uses Python identifier Firm
    __Firm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Firm'), 'Firm', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0Firm', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1466, 5), )

    
    Firm = property(__Firm.value, __Firm.set, None, 'Specification of a firm, company, organization, etc. It can be specified as part of an address that contains a street or a postbox. It is therefore different from a large mail user address, which contains no street.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}MailStop uses Python identifier MailStop
    __MailStop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MailStop'), 'MailStop', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0MailStop', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1472, 4), )

    
    MailStop = property(__MailStop.value, __MailStop.set, None, 'A MailStop is where the the mail is delivered to within a premise/subpremise/firm or a facility.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumber uses Python identifier PremiseNumber
    __PremiseNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumber'), 'PremiseNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0PremiseNumber', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1584, 1), )

    
    PremiseNumber = property(__PremiseNumber.value, __PremiseNumber.set, None, 'Specification of the identifier of the premise (house, building, etc). Premises in a street are often uniquely identified by means of consecutive identifiers. The identifier can be a number, a letter or any combination of the two.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberPrefix uses Python identifier PremiseNumberPrefix
    __PremiseNumberPrefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberPrefix'), 'PremiseNumberPrefix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0PremiseNumberPrefix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1632, 1), )

    
    PremiseNumberPrefix = property(__PremiseNumberPrefix.value, __PremiseNumberPrefix.set, None, 'A in A12')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberSuffix uses Python identifier PremiseNumberSuffix
    __PremiseNumberSuffix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberSuffix'), 'PremiseNumberSuffix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_urnoasisnamestcciqxsdschemaxAL2_0PremiseNumberSuffix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1651, 1), )

    
    PremiseNumberSuffix = property(__PremiseNumberSuffix.value, __PremiseNumberSuffix.set, None, 'A in 12A')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1481, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1481, 3)
    
    Type = property(__Type.value, __Type.set, None, 'COMPLEXE in COMPLEX DES JARDINS, A building, station, etc')

    
    # Attribute PremiseDependency uses Python identifier PremiseDependency
    __PremiseDependency = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PremiseDependency'), 'PremiseDependency', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_PremiseDependency', pyxb.binding.datatypes.anySimpleType)
    __PremiseDependency._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1486, 3)
    __PremiseDependency._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1486, 3)
    
    PremiseDependency = property(__PremiseDependency.value, __PremiseDependency.set, None, 'STREET, PREMISE, SUBPREMISE, PARK, FARM, etc')

    
    # Attribute PremiseDependencyType uses Python identifier PremiseDependencyType
    __PremiseDependencyType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PremiseDependencyType'), 'PremiseDependencyType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_PremiseDependencyType', pyxb.binding.datatypes.anySimpleType)
    __PremiseDependencyType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1491, 3)
    __PremiseDependencyType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1491, 3)
    
    PremiseDependencyType = property(__PremiseDependencyType.value, __PremiseDependencyType.set, None, 'NEAR, ADJACENT TO, etc')

    
    # Attribute PremiseThoroughfareConnector uses Python identifier PremiseThoroughfareConnector
    __PremiseThoroughfareConnector = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PremiseThoroughfareConnector'), 'PremiseThoroughfareConnector', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_51_PremiseThoroughfareConnector', pyxb.binding.datatypes.anySimpleType)
    __PremiseThoroughfareConnector._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1496, 3)
    __PremiseThoroughfareConnector._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1496, 3)
    
    PremiseThoroughfareConnector = property(__PremiseThoroughfareConnector.value, __PremiseThoroughfareConnector.set, None, 'DES, DE, LA, LA, DU in RUE DU BOIS. These terms connect a premise/thoroughfare type and premise/thoroughfare name. Terms may appear with names AVE DU BOIS')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __PostalCode.name() : __PostalCode,
        __Premise.name() : __Premise,
        __PremiseName.name() : __PremiseName,
        __PremiseLocation.name() : __PremiseLocation,
        __PremiseNumberRange.name() : __PremiseNumberRange,
        __BuildingName.name() : __BuildingName,
        __SubPremise.name() : __SubPremise,
        __Firm.name() : __Firm,
        __MailStop.name() : __MailStop,
        __PremiseNumber.name() : __PremiseNumber,
        __PremiseNumberPrefix.name() : __PremiseNumberPrefix,
        __PremiseNumberSuffix.name() : __PremiseNumberSuffix
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __PremiseDependency.name() : __PremiseDependency,
        __PremiseDependencyType.name() : __PremiseDependencyType,
        __PremiseThoroughfareConnector.name() : __PremiseThoroughfareConnector
    })
_module_typeBindings.CTD_ANON_51 = CTD_ANON_51


# Complex type [anonymous] with content type MIXED
class CTD_ANON_52 (pyxb.binding.basis.complexTypeDefinition):
    """LOBBY, BASEMENT, GROUND FLOOR, etc..."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1369, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_52_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code
    })
_module_typeBindings.CTD_ANON_52 = CTD_ANON_52


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_53 (pyxb.binding.basis.complexTypeDefinition):
    """Start number details of the premise number range"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1386, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_53_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumber uses Python identifier PremiseNumber
    __PremiseNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumber'), 'PremiseNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_53_urnoasisnamestcciqxsdschemaxAL2_0PremiseNumber', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1584, 1), )

    
    PremiseNumber = property(__PremiseNumber.value, __PremiseNumber.set, None, 'Specification of the identifier of the premise (house, building, etc). Premises in a street are often uniquely identified by means of consecutive identifiers. The identifier can be a number, a letter or any combination of the two.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberPrefix uses Python identifier PremiseNumberPrefix
    __PremiseNumberPrefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberPrefix'), 'PremiseNumberPrefix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_53_urnoasisnamestcciqxsdschemaxAL2_0PremiseNumberPrefix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1632, 1), )

    
    PremiseNumberPrefix = property(__PremiseNumberPrefix.value, __PremiseNumberPrefix.set, None, 'A in A12')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberSuffix uses Python identifier PremiseNumberSuffix
    __PremiseNumberSuffix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberSuffix'), 'PremiseNumberSuffix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_53_urnoasisnamestcciqxsdschemaxAL2_0PremiseNumberSuffix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1651, 1), )

    
    PremiseNumberSuffix = property(__PremiseNumberSuffix.value, __PremiseNumberSuffix.set, None, 'A in 12A')

    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __PremiseNumber.name() : __PremiseNumber,
        __PremiseNumberPrefix.name() : __PremiseNumberPrefix,
        __PremiseNumberSuffix.name() : __PremiseNumberSuffix
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_53 = CTD_ANON_53


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_54 (pyxb.binding.basis.complexTypeDefinition):
    """End number details of the premise number range"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1399, 10)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_54_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumber uses Python identifier PremiseNumber
    __PremiseNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumber'), 'PremiseNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_54_urnoasisnamestcciqxsdschemaxAL2_0PremiseNumber', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1584, 1), )

    
    PremiseNumber = property(__PremiseNumber.value, __PremiseNumber.set, None, 'Specification of the identifier of the premise (house, building, etc). Premises in a street are often uniquely identified by means of consecutive identifiers. The identifier can be a number, a letter or any combination of the two.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberPrefix uses Python identifier PremiseNumberPrefix
    __PremiseNumberPrefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberPrefix'), 'PremiseNumberPrefix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_54_urnoasisnamestcciqxsdschemaxAL2_0PremiseNumberPrefix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1632, 1), )

    
    PremiseNumberPrefix = property(__PremiseNumberPrefix.value, __PremiseNumberPrefix.set, None, 'A in A12')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberSuffix uses Python identifier PremiseNumberSuffix
    __PremiseNumberSuffix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberSuffix'), 'PremiseNumberSuffix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_54_urnoasisnamestcciqxsdschemaxAL2_0PremiseNumberSuffix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1651, 1), )

    
    PremiseNumberSuffix = property(__PremiseNumberSuffix.value, __PremiseNumberSuffix.set, None, 'A in 12A')

    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __PremiseNumber.name() : __PremiseNumber,
        __PremiseNumberPrefix.name() : __PremiseNumberPrefix,
        __PremiseNumberSuffix.name() : __PremiseNumberSuffix
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.CTD_ANON_54 = CTD_ANON_54


# Complex type [anonymous] with content type MIXED
class CTD_ANON_55 (pyxb.binding.basis.complexTypeDefinition):
    """A-12 where 12 is number and A is prefix and "-" is the separator"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1508, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_55_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute NumberPrefixSeparator uses Python identifier NumberPrefixSeparator
    __NumberPrefixSeparator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberPrefixSeparator'), 'NumberPrefixSeparator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_55_NumberPrefixSeparator', pyxb.binding.datatypes.anySimpleType)
    __NumberPrefixSeparator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1512, 3)
    __NumberPrefixSeparator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1512, 3)
    
    NumberPrefixSeparator = property(__NumberPrefixSeparator.value, __NumberPrefixSeparator.set, None, None)

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_55_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1513, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1513, 3)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __NumberPrefixSeparator.name() : __NumberPrefixSeparator,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_55 = CTD_ANON_55


# Complex type [anonymous] with content type MIXED
class CTD_ANON_56 (pyxb.binding.basis.complexTypeDefinition):
    """Suffix after the number. A in 12A Archer Street"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1522, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_56_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute NumberSuffixSeparator uses Python identifier NumberSuffixSeparator
    __NumberSuffixSeparator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberSuffixSeparator'), 'NumberSuffixSeparator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_56_NumberSuffixSeparator', pyxb.binding.datatypes.anySimpleType)
    __NumberSuffixSeparator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1523, 3)
    __NumberSuffixSeparator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1523, 3)
    
    NumberSuffixSeparator = property(__NumberSuffixSeparator.value, __NumberSuffixSeparator.set, None, 'NEAR, ADJACENT TO, etc12-A where 12 is number and A is suffix and "-" is the separator')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_56_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1529, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1529, 3)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __NumberSuffixSeparator.name() : __NumberSuffixSeparator,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_56 = CTD_ANON_56


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON_57 (pyxb.binding.basis.complexTypeDefinition):
    """A in A12"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1636, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_57_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute NumberPrefixSeparator uses Python identifier NumberPrefixSeparator
    __NumberPrefixSeparator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberPrefixSeparator'), 'NumberPrefixSeparator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_57_NumberPrefixSeparator', pyxb.binding.datatypes.anySimpleType)
    __NumberPrefixSeparator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1639, 5)
    __NumberPrefixSeparator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1639, 5)
    
    NumberPrefixSeparator = property(__NumberPrefixSeparator.value, __NumberPrefixSeparator.set, None, 'A-12 where 12 is number and A is prefix and "-" is the separator')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_57_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1644, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1644, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __NumberPrefixSeparator.name() : __NumberPrefixSeparator,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_57 = CTD_ANON_57


# Complex type [anonymous] with content type MIXED
class CTD_ANON_58 (pyxb.binding.basis.complexTypeDefinition):
    """A in 12A"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1655, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_58_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute NumberSuffixSeparator uses Python identifier NumberSuffixSeparator
    __NumberSuffixSeparator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberSuffixSeparator'), 'NumberSuffixSeparator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_58_NumberSuffixSeparator', pyxb.binding.datatypes.anySimpleType)
    __NumberSuffixSeparator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1656, 3)
    __NumberSuffixSeparator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1656, 3)
    
    NumberSuffixSeparator = property(__NumberSuffixSeparator.value, __NumberSuffixSeparator.set, None, '12-A where 12 is number and A is suffix and "-" is the separator')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_58_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1661, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1661, 3)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __NumberSuffixSeparator.name() : __NumberSuffixSeparator,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_58 = CTD_ANON_58


# Complex type [anonymous] with content type MIXED
class CTD_ANON_59 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of the name of a country."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1670, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_59_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_59_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1671, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1671, 3)
    
    Type = property(__Type.value, __Type.set, None, 'Old name, new name, etc')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_59 = CTD_ANON_59


# Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}BuildingNameType with content type MIXED
class BuildingNameType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}BuildingNameType with content type MIXED"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingNameType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 307, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_BuildingNameType_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_BuildingNameType_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 308, 2)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 308, 2)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute TypeOccurrence uses Python identifier TypeOccurrence
    __TypeOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TypeOccurrence'), 'TypeOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_BuildingNameType_TypeOccurrence', _module_typeBindings.STD_ANON)
    __TypeOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 309, 2)
    __TypeOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 309, 2)
    
    TypeOccurrence = property(__TypeOccurrence.value, __TypeOccurrence.set, None, 'Occurrence of the building name before/after the type. eg. EGIS BUILDING where name appears before type')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type,
        __TypeOccurrence.name() : __TypeOccurrence
    })
_module_typeBindings.BuildingNameType = BuildingNameType
Namespace.addCategoryObject('typeBinding', 'BuildingNameType', BuildingNameType)


# Complex type [anonymous] with content type MIXED
class CTD_ANON_60 (pyxb.binding.basis.complexTypeDefinition):
    """Number of the dependent locality. Some areas are numbered. Eg. SECTOR 5 in a Suburb as in India or SOI SUKUMVIT 10 as in Thailand"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 340, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_60_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute NameNumberOccurrence uses Python identifier NameNumberOccurrence
    __NameNumberOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NameNumberOccurrence'), 'NameNumberOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_60_NameNumberOccurrence', _module_typeBindings.STD_ANON_)
    __NameNumberOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 341, 5)
    __NameNumberOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 341, 5)
    
    NameNumberOccurrence = property(__NameNumberOccurrence.value, __NameNumberOccurrence.set, None, 'Eg. SECTOR occurs before 5 in SECTOR 5')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __NameNumberOccurrence.name() : __NameNumberOccurrence
    })
_module_typeBindings.CTD_ANON_60 = CTD_ANON_60


# Complex type [anonymous] with content type MIXED
class CTD_ANON_61 (pyxb.binding.basis.complexTypeDefinition):
    """ Name of the SubPremise"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 547, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_61_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_61_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 548, 5)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 548, 5)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute TypeOccurrence uses Python identifier TypeOccurrence
    __TypeOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TypeOccurrence'), 'TypeOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_61_TypeOccurrence', _module_typeBindings.STD_ANON_2)
    __TypeOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 549, 5)
    __TypeOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 549, 5)
    
    TypeOccurrence = property(__TypeOccurrence.value, __TypeOccurrence.set, None, 'EGIS Building where EGIS occurs before Building')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type,
        __TypeOccurrence.name() : __TypeOccurrence
    })
_module_typeBindings.CTD_ANON_61 = CTD_ANON_61


# Complex type [anonymous] with content type MIXED
class CTD_ANON_62 (pyxb.binding.basis.complexTypeDefinition):
    """ Specification of the identifier of a sub-premise. Examples of sub-premises are apartments and suites. sub-premises in a building are often uniquely identified by means of consecutive
identifiers. The identifier can be a number, a letter or any combination of the two. In the latter case, the identifier includes exactly one variable (range) part, which is either a 
number or a single letter that is surrounded by fixed parts at the left (prefix) or the right (postfix)."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 579, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_62_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_62_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 580, 6)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 580, 6)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, '"TH" in 12TH which is a floor number, "NO." in NO.1, "#" in APT #12, etc.')

    
    # Attribute IndicatorOccurrence uses Python identifier IndicatorOccurrence
    __IndicatorOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IndicatorOccurrence'), 'IndicatorOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_62_IndicatorOccurrence', _module_typeBindings.STD_ANON_3)
    __IndicatorOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 585, 6)
    __IndicatorOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 585, 6)
    
    IndicatorOccurrence = property(__IndicatorOccurrence.value, __IndicatorOccurrence.set, None, '"No." occurs before 1 in No.1, or TH occurs after 12 in 12TH')

    
    # Attribute NumberTypeOccurrence uses Python identifier NumberTypeOccurrence
    __NumberTypeOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberTypeOccurrence'), 'NumberTypeOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_62_NumberTypeOccurrence', _module_typeBindings.STD_ANON_4)
    __NumberTypeOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 596, 6)
    __NumberTypeOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 596, 6)
    
    NumberTypeOccurrence = property(__NumberTypeOccurrence.value, __NumberTypeOccurrence.set, None, '12TH occurs "before" FLOOR (a type of subpremise) in 12TH FLOOR')

    
    # Attribute PremiseNumberSeparator uses Python identifier PremiseNumberSeparator
    __PremiseNumberSeparator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'PremiseNumberSeparator'), 'PremiseNumberSeparator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_62_PremiseNumberSeparator', pyxb.binding.datatypes.anySimpleType)
    __PremiseNumberSeparator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 607, 6)
    __PremiseNumberSeparator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 607, 6)
    
    PremiseNumberSeparator = property(__PremiseNumberSeparator.value, __PremiseNumberSeparator.set, None, '"/" in 12/14 Archer Street where 12 is sub-premise number and 14 is premise number')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_62_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 612, 6)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 612, 6)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Indicator.name() : __Indicator,
        __IndicatorOccurrence.name() : __IndicatorOccurrence,
        __NumberTypeOccurrence.name() : __NumberTypeOccurrence,
        __PremiseNumberSeparator.name() : __PremiseNumberSeparator,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_62 = CTD_ANON_62


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_63 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of a thoroughfare. A thoroughfare could be a rd, street, canal, river, etc.  Note dependentlocality in a street. For example, in some countries, a large street will 
have many subdivisions with numbers. Normally the subdivision name is the same as the road name, but with a number to identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 780, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumberRange uses Python identifier ThoroughfareNumberRange
    __ThoroughfareNumberRange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberRange'), 'ThoroughfareNumberRange', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareNumberRange', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 785, 5), )

    
    ThoroughfareNumberRange = property(__ThoroughfareNumberRange.value, __ThoroughfareNumberRange.set, None, 'A container to represent a range of numbers (from x thru y)for a thoroughfare. eg. 1-2 Albert Av')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfarePreDirection uses Python identifier ThoroughfarePreDirection
    __ThoroughfarePreDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePreDirection'), 'ThoroughfarePreDirection', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfarePreDirection', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 876, 4), )

    
    ThoroughfarePreDirection = property(__ThoroughfarePreDirection.value, __ThoroughfarePreDirection.set, None, 'North Baker Street, where North is the pre-direction. The direction appears before the name.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareLeadingType uses Python identifier ThoroughfareLeadingType
    __ThoroughfareLeadingType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareLeadingType'), 'ThoroughfareLeadingType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareLeadingType', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 881, 4), )

    
    ThoroughfareLeadingType = property(__ThoroughfareLeadingType.value, __ThoroughfareLeadingType.set, None, 'Appears before the thoroughfare name. Ed. Spanish: Avenida Aurora, where Avenida is the leading type / French: Rue Moliere, where Rue is the leading type.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareName uses Python identifier ThoroughfareName
    __ThoroughfareName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareName'), 'ThoroughfareName', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareName', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 886, 4), )

    
    ThoroughfareName = property(__ThoroughfareName.value, __ThoroughfareName.set, None, 'Specification of the name of a Thoroughfare (also dependant street name): street name, canal name, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareTrailingType uses Python identifier ThoroughfareTrailingType
    __ThoroughfareTrailingType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareTrailingType'), 'ThoroughfareTrailingType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareTrailingType', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 891, 4), )

    
    ThoroughfareTrailingType = property(__ThoroughfareTrailingType.value, __ThoroughfareTrailingType.set, None, 'Appears after the thoroughfare name. Ed. British: Baker Lane, where Lane is the trailing type.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfarePostDirection uses Python identifier ThoroughfarePostDirection
    __ThoroughfarePostDirection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePostDirection'), 'ThoroughfarePostDirection', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfarePostDirection', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 896, 4), )

    
    ThoroughfarePostDirection = property(__ThoroughfarePostDirection.value, __ThoroughfarePostDirection.set, None, '221-bis Baker Street North, where North is the post-direction. The post-direction appears after the name.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentThoroughfare uses Python identifier DependentThoroughfare
    __DependentThoroughfare = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DependentThoroughfare'), 'DependentThoroughfare', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0DependentThoroughfare', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 901, 4), )

    
    DependentThoroughfare = property(__DependentThoroughfare.value, __DependentThoroughfare.set, None, 'DependentThroughfare is related to a street; occurs in GB, IE, ES, PT')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}DependentLocality uses Python identifier DependentLocality
    __DependentLocality = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DependentLocality'), 'DependentLocality', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0DependentLocality', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 940, 5), )

    
    DependentLocality = property(__DependentLocality.value, __DependentLocality.set, None, 'Dependent localities are Districts within cities/towns, locality divisions, postal \ndivisions of cities, suburbs, etc. DependentLocality is a recursive element, but no nesting deeper than two exists (Locality-DependentLocality-DependentLocality).')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Firm uses Python identifier Firm
    __Firm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Firm'), 'Firm', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0Firm', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 947, 5), )

    
    Firm = property(__Firm.value, __Firm.set, None, 'Specification of a firm, company, organization, etc. It can be specified as part of an address that contains a street or a postbox. It is therefore different from \na large mail user address, which contains no street.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PostalCode uses Python identifier PostalCode
    __PostalCode = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), 'PostalCode', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0PostalCode', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1), )

    
    PostalCode = property(__PostalCode.value, __PostalCode.set, None, 'PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}Premise uses Python identifier Premise
    __Premise = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Premise'), 'Premise', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0Premise', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1335, 1), )

    
    Premise = property(__Premise.value, __Premise.set, None, 'Specification of a single premise, for example a house or a building. The premise as a whole has a unique premise (house) number or a premise name.  There could be more than \none premise in a street referenced in an address. For example a building address near a major shopping centre or raiwlay station')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumberPrefix uses Python identifier ThoroughfareNumberPrefix
    __ThoroughfareNumberPrefix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberPrefix'), 'ThoroughfareNumberPrefix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareNumberPrefix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1504, 1), )

    
    ThoroughfareNumberPrefix = property(__ThoroughfareNumberPrefix.value, __ThoroughfareNumberPrefix.set, None, 'Prefix before the number. A in A12 Archer Street')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumberSuffix uses Python identifier ThoroughfareNumberSuffix
    __ThoroughfareNumberSuffix = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberSuffix'), 'ThoroughfareNumberSuffix', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareNumberSuffix', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1518, 1), )

    
    ThoroughfareNumberSuffix = property(__ThoroughfareNumberSuffix.value, __ThoroughfareNumberSuffix.set, None, 'Suffix after the number. A in 12A Archer Street')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumber uses Python identifier ThoroughfareNumber
    __ThoroughfareNumber = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumber'), 'ThoroughfareNumber', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareNumber', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1534, 1), )

    
    ThoroughfareNumber = property(__ThoroughfareNumber.value, __ThoroughfareNumber.set, None, 'Eg.: 23 Archer street or 25/15 Zero Avenue, etc')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 957, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 957, 3)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute DependentThoroughfares uses Python identifier DependentThoroughfares
    __DependentThoroughfares = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DependentThoroughfares'), 'DependentThoroughfares', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_DependentThoroughfares', _module_typeBindings.STD_ANON_8)
    __DependentThoroughfares._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 958, 3)
    __DependentThoroughfares._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 958, 3)
    
    DependentThoroughfares = property(__DependentThoroughfares.value, __DependentThoroughfares.set, None, 'Does this thoroughfare have a a dependent thoroughfare? Corner of street X, etc')

    
    # Attribute DependentThoroughfaresIndicator uses Python identifier DependentThoroughfaresIndicator
    __DependentThoroughfaresIndicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DependentThoroughfaresIndicator'), 'DependentThoroughfaresIndicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_DependentThoroughfaresIndicator', pyxb.binding.datatypes.anySimpleType)
    __DependentThoroughfaresIndicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 969, 3)
    __DependentThoroughfaresIndicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 969, 3)
    
    DependentThoroughfaresIndicator = property(__DependentThoroughfaresIndicator.value, __DependentThoroughfaresIndicator.set, None, 'Corner of, Intersection of')

    
    # Attribute DependentThoroughfaresConnector uses Python identifier DependentThoroughfaresConnector
    __DependentThoroughfaresConnector = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DependentThoroughfaresConnector'), 'DependentThoroughfaresConnector', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_DependentThoroughfaresConnector', pyxb.binding.datatypes.anySimpleType)
    __DependentThoroughfaresConnector._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 974, 3)
    __DependentThoroughfaresConnector._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 974, 3)
    
    DependentThoroughfaresConnector = property(__DependentThoroughfaresConnector.value, __DependentThoroughfaresConnector.set, None, 'Corner of Street1 AND Street 2 where AND is the Connector')

    
    # Attribute DependentThoroughfaresType uses Python identifier DependentThoroughfaresType
    __DependentThoroughfaresType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'DependentThoroughfaresType'), 'DependentThoroughfaresType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_63_DependentThoroughfaresType', pyxb.binding.datatypes.anySimpleType)
    __DependentThoroughfaresType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 979, 3)
    __DependentThoroughfaresType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 979, 3)
    
    DependentThoroughfaresType = property(__DependentThoroughfaresType.value, __DependentThoroughfaresType.set, None, 'STS in GEORGE and ADELAIDE STS, RDS IN A and B RDS, etc. Use only when both the street types are the same')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _HasWildcardElement = True
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __ThoroughfareNumberRange.name() : __ThoroughfareNumberRange,
        __ThoroughfarePreDirection.name() : __ThoroughfarePreDirection,
        __ThoroughfareLeadingType.name() : __ThoroughfareLeadingType,
        __ThoroughfareName.name() : __ThoroughfareName,
        __ThoroughfareTrailingType.name() : __ThoroughfareTrailingType,
        __ThoroughfarePostDirection.name() : __ThoroughfarePostDirection,
        __DependentThoroughfare.name() : __DependentThoroughfare,
        __DependentLocality.name() : __DependentLocality,
        __Firm.name() : __Firm,
        __PostalCode.name() : __PostalCode,
        __Premise.name() : __Premise,
        __ThoroughfareNumberPrefix.name() : __ThoroughfareNumberPrefix,
        __ThoroughfareNumberSuffix.name() : __ThoroughfareNumberSuffix,
        __ThoroughfareNumber.name() : __ThoroughfareNumber
    })
    _AttributeMap.update({
        __Type.name() : __Type,
        __DependentThoroughfares.name() : __DependentThoroughfares,
        __DependentThoroughfaresIndicator.name() : __DependentThoroughfaresIndicator,
        __DependentThoroughfaresConnector.name() : __DependentThoroughfaresConnector,
        __DependentThoroughfaresType.name() : __DependentThoroughfaresType
    })
_module_typeBindings.CTD_ANON_63 = CTD_ANON_63


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_64 (pyxb.binding.basis.complexTypeDefinition):
    """A container to represent a range of numbers (from x thru y)for a thoroughfare. eg. 1-2 Albert Av"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 789, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}AddressLine uses Python identifier AddressLine
    __AddressLine = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), 'AddressLine', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_64_urnoasisnamestcciqxsdschemaxAL2_0AddressLine', True, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1), )

    
    AddressLine = property(__AddressLine.value, __AddressLine.set, None, 'Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumberFrom uses Python identifier ThoroughfareNumberFrom
    __ThoroughfareNumberFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberFrom'), 'ThoroughfareNumberFrom', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_64_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareNumberFrom', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 792, 8), )

    
    ThoroughfareNumberFrom = property(__ThoroughfareNumberFrom.value, __ThoroughfareNumberFrom.set, None, 'Starting number in the range')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}ThoroughfareNumberTo uses Python identifier ThoroughfareNumberTo
    __ThoroughfareNumberTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberTo'), 'ThoroughfareNumberTo', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_64_urnoasisnamestcciqxsdschemaxAL2_0ThoroughfareNumberTo', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 807, 8), )

    
    ThoroughfareNumberTo = property(__ThoroughfareNumberTo.value, __ThoroughfareNumberTo.set, None, 'Ending number in the range')

    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_64_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute RangeType uses Python identifier RangeType
    __RangeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'RangeType'), 'RangeType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_64_RangeType', _module_typeBindings.STD_ANON_5)
    __RangeType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 823, 7)
    __RangeType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 823, 7)
    
    RangeType = property(__RangeType.value, __RangeType.set, None, 'Thoroughfare number ranges are odd or even')

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_64_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 834, 7)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 834, 7)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, '"No." No.12-13')

    
    # Attribute Separator uses Python identifier Separator
    __Separator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Separator'), 'Separator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_64_Separator', pyxb.binding.datatypes.anySimpleType)
    __Separator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 839, 7)
    __Separator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 839, 7)
    
    Separator = property(__Separator.value, __Separator.set, None, '"-" in 12-14  or "Thru" in 12 Thru 14 etc.')

    
    # Attribute IndicatorOccurrence uses Python identifier IndicatorOccurrence
    __IndicatorOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IndicatorOccurrence'), 'IndicatorOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_64_IndicatorOccurrence', _module_typeBindings.STD_ANON_6)
    __IndicatorOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 844, 7)
    __IndicatorOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 844, 7)
    
    IndicatorOccurrence = property(__IndicatorOccurrence.value, __IndicatorOccurrence.set, None, 'No.12-14 where "No." is before actual street number')

    
    # Attribute NumberRangeOccurrence uses Python identifier NumberRangeOccurrence
    __NumberRangeOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberRangeOccurrence'), 'NumberRangeOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_64_NumberRangeOccurrence', _module_typeBindings.STD_ANON_7)
    __NumberRangeOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 855, 7)
    __NumberRangeOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 855, 7)
    
    NumberRangeOccurrence = property(__NumberRangeOccurrence.value, __NumberRangeOccurrence.set, None, '23-25 Archer St, where number appears before name')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_64_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 868, 7)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 868, 7)
    
    Type = property(__Type.value, __Type.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        __AddressLine.name() : __AddressLine,
        __ThoroughfareNumberFrom.name() : __ThoroughfareNumberFrom,
        __ThoroughfareNumberTo.name() : __ThoroughfareNumberTo
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __RangeType.name() : __RangeType,
        __Indicator.name() : __Indicator,
        __Separator.name() : __Separator,
        __IndicatorOccurrence.name() : __IndicatorOccurrence,
        __NumberRangeOccurrence.name() : __NumberRangeOccurrence,
        __Type.name() : __Type
    })
_module_typeBindings.CTD_ANON_64 = CTD_ANON_64


# Complex type [anonymous] with content type MIXED
class CTD_ANON_65 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of the number of the postoffice. Common in rural postoffices"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1094, 6)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_65_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_65_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1095, 7)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1095, 7)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, 'MS in MS 62, # in MS # 12, etc.')

    
    # Attribute IndicatorOccurrence uses Python identifier IndicatorOccurrence
    __IndicatorOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IndicatorOccurrence'), 'IndicatorOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_65_IndicatorOccurrence', _module_typeBindings.STD_ANON_9)
    __IndicatorOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1100, 7)
    __IndicatorOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1100, 7)
    
    IndicatorOccurrence = property(__IndicatorOccurrence.value, __IndicatorOccurrence.set, None, 'MS occurs before 62 in MS 62')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Indicator.name() : __Indicator,
        __IndicatorOccurrence.name() : __IndicatorOccurrence
    })
_module_typeBindings.CTD_ANON_65 = CTD_ANON_65


# Complex type [anonymous] with content type MIXED
class CTD_ANON_66 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of the name of the premise (house, building, park, farm, etc). A premise name is specified when the premise cannot be addressed using a street name plus premise (house) number."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1347, 5)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_66_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_66_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1348, 6)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1348, 6)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute TypeOccurrence uses Python identifier TypeOccurrence
    __TypeOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'TypeOccurrence'), 'TypeOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_66_TypeOccurrence', _module_typeBindings.STD_ANON_10)
    __TypeOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1349, 6)
    __TypeOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1349, 6)
    
    TypeOccurrence = property(__TypeOccurrence.value, __TypeOccurrence.set, None, 'EGIS Building where EGIS occurs before Building, DES JARDINS occurs after COMPLEXE DES JARDINS')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __Type.name() : __Type,
        __TypeOccurrence.name() : __TypeOccurrence
    })
_module_typeBindings.CTD_ANON_66 = CTD_ANON_66


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON_67 (pyxb.binding.basis.complexTypeDefinition):
    """Specification for defining the premise number range. Some premises have number as Building C1-C7"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1380, 7)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberRangeFrom uses Python identifier PremiseNumberRangeFrom
    __PremiseNumberRangeFrom = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberRangeFrom'), 'PremiseNumberRangeFrom', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_67_urnoasisnamestcciqxsdschemaxAL2_0PremiseNumberRangeFrom', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1382, 9), )

    
    PremiseNumberRangeFrom = property(__PremiseNumberRangeFrom.value, __PremiseNumberRangeFrom.set, None, 'Start number details of the premise number range')

    
    # Element {urn:oasis:names:tc:ciq:xsdschema:xAL:2.0}PremiseNumberRangeTo uses Python identifier PremiseNumberRangeTo
    __PremiseNumberRangeTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberRangeTo'), 'PremiseNumberRangeTo', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_67_urnoasisnamestcciqxsdschemaxAL2_0PremiseNumberRangeTo', False, pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1395, 9), )

    
    PremiseNumberRangeTo = property(__PremiseNumberRangeTo.value, __PremiseNumberRangeTo.set, None, 'End number details of the premise number range')

    
    # Attribute RangeType uses Python identifier RangeType
    __RangeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'RangeType'), 'RangeType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_67_RangeType', pyxb.binding.datatypes.anySimpleType)
    __RangeType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1409, 8)
    __RangeType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1409, 8)
    
    RangeType = property(__RangeType.value, __RangeType.set, None, 'Eg. Odd or even number range')

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_67_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1414, 8)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1414, 8)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, 'Eg. No. in Building No:C1-C5')

    
    # Attribute Separator uses Python identifier Separator
    __Separator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Separator'), 'Separator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_67_Separator', pyxb.binding.datatypes.anySimpleType)
    __Separator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1419, 8)
    __Separator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1419, 8)
    
    Separator = property(__Separator.value, __Separator.set, None, '"-" in 12-14  or "Thru" in 12 Thru 14 etc.')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_67_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1424, 8)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1424, 8)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute IndicatorOccurence uses Python identifier IndicatorOccurence
    __IndicatorOccurence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IndicatorOccurence'), 'IndicatorOccurence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_67_IndicatorOccurence', _module_typeBindings.STD_ANON_11)
    __IndicatorOccurence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1425, 8)
    __IndicatorOccurence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1425, 8)
    
    IndicatorOccurence = property(__IndicatorOccurence.value, __IndicatorOccurence.set, None, 'No.12-14 where "No." is before actual street number')

    
    # Attribute NumberRangeOccurence uses Python identifier NumberRangeOccurence
    __NumberRangeOccurence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberRangeOccurence'), 'NumberRangeOccurence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_67_NumberRangeOccurence', _module_typeBindings.STD_ANON_12)
    __NumberRangeOccurence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1436, 8)
    __NumberRangeOccurence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1436, 8)
    
    NumberRangeOccurence = property(__NumberRangeOccurence.value, __NumberRangeOccurence.set, None, 'Building 23-25 where the number occurs after building name')

    _ElementMap.update({
        __PremiseNumberRangeFrom.name() : __PremiseNumberRangeFrom,
        __PremiseNumberRangeTo.name() : __PremiseNumberRangeTo
    })
    _AttributeMap.update({
        __RangeType.name() : __RangeType,
        __Indicator.name() : __Indicator,
        __Separator.name() : __Separator,
        __Type.name() : __Type,
        __IndicatorOccurence.name() : __IndicatorOccurence,
        __NumberRangeOccurence.name() : __NumberRangeOccurence
    })
_module_typeBindings.CTD_ANON_67 = CTD_ANON_67


# Complex type [anonymous] with content type MIXED
class CTD_ANON_68 (pyxb.binding.basis.complexTypeDefinition):
    """Eg.: 23 Archer street or 25/15 Zero Avenue, etc"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1538, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_68_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute NumberType uses Python identifier NumberType
    __NumberType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberType'), 'NumberType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_68_NumberType', _module_typeBindings.STD_ANON_13)
    __NumberType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1539, 3)
    __NumberType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1539, 3)
    
    NumberType = property(__NumberType.value, __NumberType.set, None, '12 Archer Street is "Single" and 12-14 Archer Street is "Range"')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_68_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1550, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1550, 3)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_68_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1551, 3)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1551, 3)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, 'No. in Street No.12 or "#" in Street # 12, etc.')

    
    # Attribute IndicatorOccurrence uses Python identifier IndicatorOccurrence
    __IndicatorOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IndicatorOccurrence'), 'IndicatorOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_68_IndicatorOccurrence', _module_typeBindings.STD_ANON_14)
    __IndicatorOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1556, 3)
    __IndicatorOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1556, 3)
    
    IndicatorOccurrence = property(__IndicatorOccurrence.value, __IndicatorOccurrence.set, None, 'No.12 where "No." is before actual street number')

    
    # Attribute NumberOccurrence uses Python identifier NumberOccurrence
    __NumberOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberOccurrence'), 'NumberOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_68_NumberOccurrence', _module_typeBindings.STD_ANON_15)
    __NumberOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1567, 3)
    __NumberOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1567, 3)
    
    NumberOccurrence = property(__NumberOccurrence.value, __NumberOccurrence.set, None, '23 Archer St, Archer Street 23, St Archer 23')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __NumberType.name() : __NumberType,
        __Type.name() : __Type,
        __Indicator.name() : __Indicator,
        __IndicatorOccurrence.name() : __IndicatorOccurrence,
        __NumberOccurrence.name() : __NumberOccurrence
    })
_module_typeBindings.CTD_ANON_68 = CTD_ANON_68


# Complex type [anonymous] with content type MIXED
class CTD_ANON_69 (pyxb.binding.basis.complexTypeDefinition):
    """Specification of the identifier of the premise (house, building, etc). Premises in a street are often uniquely identified by means of consecutive identifiers. The identifier can be a number, a letter or any combination of the two."""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_MIXED
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1588, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Code uses Python identifier Code
    __Code = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Code'), 'Code', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_69_Code', pyxb.binding.datatypes.anySimpleType)
    __Code._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    __Code._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 21, 2)
    
    Code = property(__Code.value, __Code.set, None, 'Used by postal services to encode the name of the element.')

    
    # Attribute NumberType uses Python identifier NumberType
    __NumberType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberType'), 'NumberType', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_69_NumberType', _module_typeBindings.STD_ANON_16)
    __NumberType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1589, 3)
    __NumberType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1589, 3)
    
    NumberType = property(__NumberType.value, __NumberType.set, None, 'Building 12-14 is "Range" and Building 12 is "Single"')

    
    # Attribute Type uses Python identifier Type
    __Type = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Type'), 'Type', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_69_Type', pyxb.binding.datatypes.anySimpleType)
    __Type._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1600, 3)
    __Type._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1600, 3)
    
    Type = property(__Type.value, __Type.set, None, None)

    
    # Attribute Indicator uses Python identifier Indicator
    __Indicator = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'Indicator'), 'Indicator', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_69_Indicator', pyxb.binding.datatypes.anySimpleType)
    __Indicator._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1601, 3)
    __Indicator._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1601, 3)
    
    Indicator = property(__Indicator.value, __Indicator.set, None, 'No. in House No.12, # in #12, etc.')

    
    # Attribute IndicatorOccurrence uses Python identifier IndicatorOccurrence
    __IndicatorOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'IndicatorOccurrence'), 'IndicatorOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_69_IndicatorOccurrence', _module_typeBindings.STD_ANON_17)
    __IndicatorOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1606, 3)
    __IndicatorOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1606, 3)
    
    IndicatorOccurrence = property(__IndicatorOccurrence.value, __IndicatorOccurrence.set, None, 'No. occurs before 12 No.12')

    
    # Attribute NumberTypeOccurrence uses Python identifier NumberTypeOccurrence
    __NumberTypeOccurrence = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'NumberTypeOccurrence'), 'NumberTypeOccurrence', '__urnoasisnamestcciqxsdschemaxAL2_0_CTD_ANON_69_NumberTypeOccurrence', _module_typeBindings.STD_ANON_18)
    __NumberTypeOccurrence._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1617, 3)
    __NumberTypeOccurrence._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1617, 3)
    
    NumberTypeOccurrence = property(__NumberTypeOccurrence.value, __NumberTypeOccurrence.set, None, '12 in BUILDING 12 occurs "after" premise type BUILDING')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Code.name() : __Code,
        __NumberType.name() : __NumberType,
        __Type.name() : __Type,
        __Indicator.name() : __Indicator,
        __IndicatorOccurrence.name() : __IndicatorOccurrence,
        __NumberTypeOccurrence.name() : __NumberTypeOccurrence
    })
_module_typeBindings.CTD_ANON_69 = CTD_ANON_69


xAL = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'xAL'), CTD_ANON, documentation='Root element for a list of addresses', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 27, 1))
Namespace.addCategoryObject('elementBinding', xAL.name().localName(), xAL)

AddressDetails = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressDetails'), AddressDetails_, documentation='This container defines the details of the address. Can define multiple addresses including tracking address history', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 44, 1))
Namespace.addCategoryObject('elementBinding', AddressDetails.name().localName(), AddressDetails)

AddressLine = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1))
Namespace.addCategoryObject('elementBinding', AddressLine.name().localName(), AddressLine)

Locality = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Locality'), CTD_ANON_27, documentation='Locality is one level lower than adminisstrative area. Eg.: cities, reservations and any other built-up areas.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 715, 1))
Namespace.addCategoryObject('elementBinding', Locality.name().localName(), Locality)

AdministrativeArea = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea'), CTD_ANON_32, documentation='Examples of administrative areas are provinces counties, special regions (such as "Rijnmond"), etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 987, 1))
Namespace.addCategoryObject('elementBinding', AdministrativeArea.name().localName(), AdministrativeArea)

PostOffice = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostOffice'), CTD_ANON_36, documentation='Specification of a post office. Examples are a rural post office where post is delivered and a post office containing post office boxes.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1072, 1))
Namespace.addCategoryObject('elementBinding', PostOffice.name().localName(), PostOffice)

PostalCode = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1))
Namespace.addCategoryObject('elementBinding', PostalCode.name().localName(), PostalCode)

PostBox = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostBox'), CTD_ANON_44, documentation='Specification of a postbox like mail delivery point. Only a single postbox number can be specified. Examples of postboxes are POBox, free mail numbers, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1223, 1))
Namespace.addCategoryObject('elementBinding', PostBox.name().localName(), PostBox)

Department = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Department'), CTD_ANON_49, documentation='Subdivision in the firm: School of Physics at Victoria University (School of Physics is the department)', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1302, 1))
Namespace.addCategoryObject('elementBinding', Department.name().localName(), Department)

Premise = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Premise'), CTD_ANON_51, documentation='Specification of a single premise, for example a house or a building. The premise as a whole has a unique premise (house) number or a premise name.  There could be more than \none premise in a street referenced in an address. For example a building address near a major shopping centre or raiwlay station', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1335, 1))
Namespace.addCategoryObject('elementBinding', Premise.name().localName(), Premise)

ThoroughfareNumberPrefix = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberPrefix'), CTD_ANON_55, documentation='Prefix before the number. A in A12 Archer Street', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1504, 1))
Namespace.addCategoryObject('elementBinding', ThoroughfareNumberPrefix.name().localName(), ThoroughfareNumberPrefix)

ThoroughfareNumberSuffix = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberSuffix'), CTD_ANON_56, documentation='Suffix after the number. A in 12A Archer Street', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1518, 1))
Namespace.addCategoryObject('elementBinding', ThoroughfareNumberSuffix.name().localName(), ThoroughfareNumberSuffix)

PremiseNumberPrefix = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberPrefix'), CTD_ANON_57, documentation='A in A12', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1632, 1))
Namespace.addCategoryObject('elementBinding', PremiseNumberPrefix.name().localName(), PremiseNumberPrefix)

PremiseNumberSuffix = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberSuffix'), CTD_ANON_58, documentation='A in 12A', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1651, 1))
Namespace.addCategoryObject('elementBinding', PremiseNumberSuffix.name().localName(), PremiseNumberSuffix)

CountryName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CountryName'), CTD_ANON_59, documentation='Specification of the name of a country.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1666, 1))
Namespace.addCategoryObject('elementBinding', CountryName.name().localName(), CountryName)

Thoroughfare = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare'), CTD_ANON_63, documentation='Specification of a thoroughfare. A thoroughfare could be a rd, street, canal, river, etc.  Note dependentlocality in a street. For example, in some countries, a large street will \nhave many subdivisions with numbers. Normally the subdivision name is the same as the road name, but with a number to identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 775, 1))
Namespace.addCategoryObject('elementBinding', Thoroughfare.name().localName(), Thoroughfare)

ThoroughfareNumber = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumber'), CTD_ANON_68, documentation='Eg.: 23 Archer street or 25/15 Zero Avenue, etc', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1534, 1))
Namespace.addCategoryObject('elementBinding', ThoroughfareNumber.name().localName(), ThoroughfareNumber)

PremiseNumber = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumber'), CTD_ANON_69, documentation='Specification of the identifier of the premise (house, building, etc). Premises in a street are often uniquely identified by means of consecutive identifiers. The identifier can be a number, a letter or any combination of the two.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1584, 1))
Namespace.addCategoryObject('elementBinding', PremiseNumber.name().localName(), PremiseNumber)



CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressDetails'), AddressDetails_, scope=CTD_ANON, documentation='This container defines the details of the address. Can define multiple addresses including tracking address history', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 44, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 34, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressDetails')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 33, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 34, 4))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton()




AddressDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalServiceElements'), CTD_ANON_, scope=AddressDetails_, documentation='Postal authorities use specific postal service data to expedient delivery of mail', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 51, 3)))

AddressDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Address'), CTD_ANON_12, scope=AddressDetails_, documentation='Address as one line of free text', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 210, 4)))

AddressDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLines'), AddressLinesType, scope=AddressDetails_, documentation='Container for Address lines', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 224, 4)))

AddressDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Country'), CTD_ANON_13, scope=AddressDetails_, documentation='Specification of a country', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 229, 4)))

AddressDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Locality'), CTD_ANON_27, scope=AddressDetails_, documentation='Locality is one level lower than adminisstrative area. Eg.: cities, reservations and any other built-up areas.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 715, 1)))

AddressDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare'), CTD_ANON_63, scope=AddressDetails_, documentation='Specification of a thoroughfare. A thoroughfare could be a rd, street, canal, river, etc.  Note dependentlocality in a street. For example, in some countries, a large street will \nhave many subdivisions with numbers. Normally the subdivision name is the same as the road name, but with a number to identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 775, 1)))

AddressDetails_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea'), CTD_ANON_32, scope=AddressDetails_, documentation='Examples of administrative areas are provinces counties, special regions (such as "Rijnmond"), etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 987, 1)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 51, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 206, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 265, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AddressDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalServiceElements')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 51, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AddressDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Address')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 210, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AddressDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLines')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 224, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AddressDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Country')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 229, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AddressDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 261, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AddressDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Locality')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 262, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AddressDetails_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 263, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 265, 3))
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
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AddressDetails_._Automaton = _BuildAutomaton_()




CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressIdentifier'), CTD_ANON_2, scope=CTD_ANON_, documentation='A unique identifier of an address assigned by postal authorities. Example: DPID in Australia', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 57, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'EndorsementLineCode'), CTD_ANON_3, scope=CTD_ANON_, documentation='Directly affects postal service distribution', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 72, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'KeyLineCode'), CTD_ANON_4, scope=CTD_ANON_, documentation='Required for some postal services', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 86, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Barcode'), CTD_ANON_5, scope=CTD_ANON_, documentation='Required for some postal services', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 100, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SortingCode'), CTD_ANON_6, scope=CTD_ANON_, documentation='Used for sorting addresses. Values may for example be CEDEX 16 (France)', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 114, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLatitude'), CTD_ANON_7, scope=CTD_ANON_, documentation='Latitude of delivery address', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 127, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLatitudeDirection'), CTD_ANON_8, scope=CTD_ANON_, documentation='Latitude direction of delivery address;N = North and S = South', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 141, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLongitude'), CTD_ANON_9, scope=CTD_ANON_, documentation='Longtitude of delivery address', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 154, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLongitudeDirection'), CTD_ANON_10, scope=CTD_ANON_, documentation='Longtitude direction of delivery address;N=North and S=South', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 168, 6)))

CTD_ANON_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SupplementaryPostalServiceData'), CTD_ANON_11, scope=CTD_ANON_, documentation='any postal service elements not covered by the container can be represented using this element', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 182, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 57, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 72, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 86, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 100, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 114, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 127, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 141, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 154, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 168, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 182, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 196, 6))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressIdentifier')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 57, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'EndorsementLineCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 72, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'KeyLineCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 86, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Barcode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 100, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SortingCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 114, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLatitude')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 127, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLatitudeDirection')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 141, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLongitude')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 154, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLongitudeDirection')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 168, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SupplementaryPostalServiceData')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 182, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 196, 6))
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
CTD_ANON_._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 61, 7))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_2._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 76, 7))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_3._Automaton = _BuildAutomaton_4()




def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 90, 7))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_4._Automaton = _BuildAutomaton_5()




def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 104, 7))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_5._Automaton = _BuildAutomaton_6()




def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 131, 7))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_7._Automaton = _BuildAutomaton_7()




def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 145, 7))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_8._Automaton = _BuildAutomaton_8()




def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 158, 7))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_9._Automaton = _BuildAutomaton_9()




def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 172, 7))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_10._Automaton = _BuildAutomaton_10()




def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 186, 7))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_11._Automaton = _BuildAutomaton_11()




def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_12._Automaton = _BuildAutomaton_12()




CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CountryNameCode'), CTD_ANON_14, scope=CTD_ANON_13, documentation='A country code according to the specified scheme', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 236, 7)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_13, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Locality'), CTD_ANON_27, scope=CTD_ANON_13, documentation='Locality is one level lower than adminisstrative area. Eg.: cities, reservations and any other built-up areas.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 715, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare'), CTD_ANON_63, scope=CTD_ANON_13, documentation='Specification of a thoroughfare. A thoroughfare could be a rd, street, canal, river, etc.  Note dependentlocality in a street. For example, in some countries, a large street will \nhave many subdivisions with numbers. Normally the subdivision name is the same as the road name, but with a number to identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 775, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea'), CTD_ANON_32, scope=CTD_ANON_13, documentation='Examples of administrative areas are provinces counties, special regions (such as "Rijnmond"), etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 987, 1)))

CTD_ANON_13._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CountryName'), CTD_ANON_59, scope=CTD_ANON_13, documentation='Specification of the name of a country.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1666, 1)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 235, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 236, 7))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 250, 7))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 251, 7))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 256, 7))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 235, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CountryNameCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 236, 7))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CountryName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 250, 7))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeArea')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 252, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Locality')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 253, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_13._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 254, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 256, 7))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_13._Automaton = _BuildAutomaton_13()




def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 240, 8))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_14._Automaton = _BuildAutomaton_14()




AddressLinesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=AddressLinesType, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 303, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AddressLinesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 302, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 303, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AddressLinesType._Automaton = _BuildAutomaton_15()




DependentLocalityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DependentLocalityName'), CTD_ANON_15, scope=DependentLocalityType, documentation='Name of the dependent locality', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 326, 3)))

DependentLocalityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DependentLocalityNumber'), CTD_ANON_60, scope=DependentLocalityType, documentation='Number of the dependent locality. Some areas are numbered. Eg. SECTOR 5 in a Suburb as in India or SOI SUKUMVIT 10 as in Thailand', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 336, 3)))

DependentLocalityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LargeMailUser'), LargeMailUserType, scope=DependentLocalityType, documentation='Specification of a large mail user address. Examples of large mail users are postal companies, companies in France with a cedex number, hospitals and airports with their own post code. Large mail user addresses do not have a street name with premise name or premise number in countries like Netherlands. But they have a POBox and street also in countries like France', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 358, 4)))

DependentLocalityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalRoute'), PostalRouteType, scope=DependentLocalityType, documentation=' A Postal van is specific for a route as in Is`rael, Rural route', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 364, 4)))

DependentLocalityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DependentLocality'), DependentLocalityType, scope=DependentLocalityType, documentation='Dependent localities are Districts within cities/towns, locality divisions, postal \ndivisions of cities, suburbs, etc. DependentLocality is a recursive element, but no nesting deeper than two exists (Locality-DependentLocality-DependentLocality).', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 372, 3)))

DependentLocalityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=DependentLocalityType, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

DependentLocalityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare'), CTD_ANON_63, scope=DependentLocalityType, documentation='Specification of a thoroughfare. A thoroughfare could be a rd, street, canal, river, etc.  Note dependentlocality in a street. For example, in some countries, a large street will \nhave many subdivisions with numbers. Normally the subdivision name is the same as the road name, but with a number to identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 775, 1)))

DependentLocalityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostOffice'), CTD_ANON_36, scope=DependentLocalityType, documentation='Specification of a post office. Examples are a rural post office where post is delivered and a post office containing post office boxes.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1072, 1)))

DependentLocalityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, scope=DependentLocalityType, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1)))

DependentLocalityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostBox'), CTD_ANON_44, scope=DependentLocalityType, documentation='Specification of a postbox like mail delivery point. Only a single postbox number can be specified. Examples of postboxes are POBox, free mail numbers, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1223, 1)))

DependentLocalityType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Premise'), CTD_ANON_51, scope=DependentLocalityType, documentation='Specification of a single premise, for example a house or a building. The premise as a whole has a unique premise (house) number or a premise name.  There could be more than \none premise in a street referenced in an address. For example a building address near a major shopping centre or raiwlay station', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1335, 1)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 325, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 326, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 336, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 356, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 370, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 371, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 372, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 378, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 379, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(DependentLocalityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 325, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(DependentLocalityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DependentLocalityName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 326, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(DependentLocalityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DependentLocalityNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 336, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DependentLocalityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostBox')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 357, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DependentLocalityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LargeMailUser')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 358, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DependentLocalityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostOffice')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 363, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(DependentLocalityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalRoute')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 364, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(DependentLocalityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 370, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(DependentLocalityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Premise')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 371, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(DependentLocalityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DependentLocality')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 372, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(DependentLocalityType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 378, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 379, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
DependentLocalityType._Automaton = _BuildAutomaton_16()




def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 330, 4))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_15._Automaton = _BuildAutomaton_17()




FirmType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FirmName'), CTD_ANON_16, scope=FirmType, documentation='Name of the firm', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 406, 3)))

FirmType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MailStop'), MailStopType, scope=FirmType, documentation='A MailStop is where the the mail is delivered to within a premise/subpremise/firm or a facility.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 417, 3)))

FirmType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=FirmType, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

FirmType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, scope=FirmType, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1)))

FirmType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Department'), CTD_ANON_49, scope=FirmType, documentation='Subdivision in the firm: School of Physics at Victoria University (School of Physics is the department)', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1302, 1)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 405, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 406, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 416, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 417, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 422, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 423, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FirmType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 405, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FirmType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FirmName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 406, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(FirmType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Department')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 416, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(FirmType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MailStop')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 417, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(FirmType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 422, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 423, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FirmType._Automaton = _BuildAutomaton_18()




def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 410, 4))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_16._Automaton = _BuildAutomaton_19()




LargeMailUserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LargeMailUserName'), CTD_ANON_17, scope=LargeMailUserType, documentation='Name of the large mail user. eg. Smith Ford International airport', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 431, 3)))

LargeMailUserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LargeMailUserIdentifier'), CTD_ANON_18, scope=LargeMailUserType, documentation='Specification of the identification number of a large mail user. An example are the Cedex codes in France.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 445, 3)))

LargeMailUserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BuildingName'), BuildingNameType, scope=LargeMailUserType, documentation='Name of the building', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 464, 3)))

LargeMailUserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=LargeMailUserType, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

LargeMailUserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare'), CTD_ANON_63, scope=LargeMailUserType, documentation='Specification of a thoroughfare. A thoroughfare could be a rd, street, canal, river, etc.  Note dependentlocality in a street. For example, in some countries, a large street will \nhave many subdivisions with numbers. Normally the subdivision name is the same as the road name, but with a number to identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 775, 1)))

LargeMailUserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, scope=LargeMailUserType, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1)))

LargeMailUserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostBox'), CTD_ANON_44, scope=LargeMailUserType, documentation='Specification of a postbox like mail delivery point. Only a single postbox number can be specified. Examples of postboxes are POBox, free mail numbers, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1223, 1)))

LargeMailUserType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Department'), CTD_ANON_49, scope=LargeMailUserType, documentation='Subdivision in the firm: School of Physics at Victoria University (School of Physics is the department)', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1302, 1)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 430, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 431, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 445, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 464, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 469, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 470, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 471, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 472, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 473, 3))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LargeMailUserType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 430, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LargeMailUserType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LargeMailUserName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 431, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(LargeMailUserType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LargeMailUserIdentifier')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 445, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(LargeMailUserType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BuildingName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 464, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(LargeMailUserType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Department')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 469, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(LargeMailUserType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostBox')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 470, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(LargeMailUserType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 471, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(LargeMailUserType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 472, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 473, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LargeMailUserType._Automaton = _BuildAutomaton_20()




def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 435, 4))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_17._Automaton = _BuildAutomaton_21()




def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 449, 4))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_18._Automaton = _BuildAutomaton_22()




MailStopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MailStopName'), CTD_ANON_19, scope=MailStopType, documentation='Name of the the Mail Stop. eg. MSP, MS, etc', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 481, 3)))

MailStopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MailStopNumber'), CTD_ANON_20, scope=MailStopType, documentation='Number of the Mail stop. eg. 123 in MS 123', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 491, 3)))

MailStopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=MailStopType, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 480, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 481, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 491, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 505, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MailStopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 480, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MailStopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MailStopName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 481, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(MailStopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MailStopNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 491, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 505, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MailStopType._Automaton = _BuildAutomaton_23()




def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 485, 4))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_19._Automaton = _BuildAutomaton_24()




def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 495, 4))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_20._Automaton = _BuildAutomaton_25()




PostalRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalRouteName'), CTD_ANON_21, scope=PostalRouteType, documentation=' Name of the Postal Route', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 514, 4)))

PostalRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalRouteNumber'), CTD_ANON_22, scope=PostalRouteType, documentation=' Number of the Postal Route', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 524, 4)))

PostalRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=PostalRouteType, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

PostalRouteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostBox'), CTD_ANON_44, scope=PostalRouteType, documentation='Specification of a postbox like mail delivery point. Only a single postbox number can be specified. Examples of postboxes are POBox, free mail numbers, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1223, 1)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 512, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 534, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 535, 3))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PostalRouteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 512, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PostalRouteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalRouteName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 514, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PostalRouteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalRouteNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 524, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(PostalRouteType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostBox')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 534, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 535, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PostalRouteType._Automaton = _BuildAutomaton_26()




def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_21._Automaton = _BuildAutomaton_27()




def _BuildAutomaton_28 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_28
    del _BuildAutomaton_28
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_22._Automaton = _BuildAutomaton_28()




SubPremiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseName'), CTD_ANON_61, scope=SubPremiseType, documentation=' Name of the SubPremise', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 543, 3)))

SubPremiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseLocation'), CTD_ANON_23, scope=SubPremiseType, documentation=' Name of the SubPremise Location. eg. LOBBY, BASEMENT, GROUND FLOOR, etc...', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 565, 4)))

SubPremiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseNumber'), CTD_ANON_62, scope=SubPremiseType, documentation=' Specification of the identifier of a sub-premise. Examples of sub-premises are apartments and suites. sub-premises in a building are often uniquely identified by means of consecutive\nidentifiers. The identifier can be a number, a letter or any combination of the two. In the latter case, the identifier includes exactly one variable (range) part, which is either a \nnumber or a single letter that is surrounded by fixed parts at the left (prefix) or the right (postfix).', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 573, 4)))

SubPremiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseNumberPrefix'), CTD_ANON_24, scope=SubPremiseType, documentation=' Prefix of the sub premise number. eg. A in A-12', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 618, 3)))

SubPremiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseNumberSuffix'), CTD_ANON_25, scope=SubPremiseType, documentation=' Suffix of the sub premise number. eg. A in 12A', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 633, 3)))

SubPremiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BuildingName'), BuildingNameType, scope=SubPremiseType, documentation='Name of the building', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 648, 3)))

SubPremiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Firm'), FirmType, scope=SubPremiseType, documentation='Specification of a firm, company, organization, etc. It can be specified as part of an address that contains a street or a postbox. It is therefore different from a large mail user address, which contains no street.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 653, 3)))

SubPremiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MailStop'), MailStopType, scope=SubPremiseType, documentation='A MailStop is where the the mail is delivered to within a premise/subpremise/firm or a facility.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 658, 3)))

SubPremiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubPremise'), SubPremiseType, scope=SubPremiseType, documentation='Specification of a single sub-premise. Examples of sub-premises are apartments and suites. \nEach sub-premise should be uniquely identifiable. SubPremiseType: Specification of the name of a sub-premise type. Possible values not limited to: Suite, Appartment, Floor, Unknown\nMultiple levels within a premise by recursively calling SubPremise Eg. Level 4, Suite 2, Block C', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 664, 3)))

SubPremiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=SubPremiseType, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

SubPremiseType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, scope=SubPremiseType, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1)))

def _BuildAutomaton_29 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_29
    del _BuildAutomaton_29
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 542, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 543, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 564, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 573, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 618, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 633, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 648, 3))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 653, 3))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 658, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 663, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 664, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 671, 3))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SubPremiseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 542, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SubPremiseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 543, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SubPremiseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseLocation')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 565, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(SubPremiseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 573, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(SubPremiseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseNumberPrefix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 618, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(SubPremiseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubPremiseNumberSuffix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 633, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(SubPremiseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BuildingName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 648, 3))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(SubPremiseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Firm')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 653, 3))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(SubPremiseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MailStop')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 658, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(SubPremiseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 663, 3))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(SubPremiseType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubPremise')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 664, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 671, 3))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False),
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False),
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
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SubPremiseType._Automaton = _BuildAutomaton_29()




def _BuildAutomaton_30 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_30
    del _BuildAutomaton_30
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_23._Automaton = _BuildAutomaton_30()




def _BuildAutomaton_31 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_31
    del _BuildAutomaton_31
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 622, 4))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_24._Automaton = _BuildAutomaton_31()




def _BuildAutomaton_32 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_32
    del _BuildAutomaton_32
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 637, 4))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_25._Automaton = _BuildAutomaton_32()




def _BuildAutomaton_33 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_33
    del _BuildAutomaton_33
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
ThoroughfareLeadingTypeType._Automaton = _BuildAutomaton_33()




def _BuildAutomaton_34 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_34
    del _BuildAutomaton_34
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
ThoroughfareNameType._Automaton = _BuildAutomaton_34()




def _BuildAutomaton_35 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_35
    del _BuildAutomaton_35
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
ThoroughfarePostDirectionType._Automaton = _BuildAutomaton_35()




def _BuildAutomaton_36 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_36
    del _BuildAutomaton_36
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
ThoroughfarePreDirectionType._Automaton = _BuildAutomaton_36()




def _BuildAutomaton_37 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_37
    del _BuildAutomaton_37
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
ThoroughfareTrailingTypeType._Automaton = _BuildAutomaton_37()




def _BuildAutomaton_38 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_38
    del _BuildAutomaton_38
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_26._Automaton = _BuildAutomaton_38()




CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_27, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LocalityName'), CTD_ANON_28, scope=CTD_ANON_27, documentation='Name of the locality', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 722, 4)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'LargeMailUser'), LargeMailUserType, scope=CTD_ANON_27, documentation='Specification of a large mail user address. Examples of large mail users are postal companies, companies in France with a cedex number, hospitals and airports with their own post code. Large mail user addresses do not have a street name with premise name or premise number in countries like Netherlands. But they have a POBox and street also in countries like France', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 734, 5)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalRoute'), PostalRouteType, scope=CTD_ANON_27, documentation='A Postal van is specific for a route as in Is`rael, Rural route', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 740, 5)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DependentLocality'), DependentLocalityType, scope=CTD_ANON_27, documentation='Dependent localities are Districts within cities/towns, locality divisions, postal \ndivisions of cities, suburbs, etc. DependentLocality is a recursive element, but no nesting deeper than two exists (Locality-DependentLocality-DependentLocality).', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 748, 4)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare'), CTD_ANON_63, scope=CTD_ANON_27, documentation='Specification of a thoroughfare. A thoroughfare could be a rd, street, canal, river, etc.  Note dependentlocality in a street. For example, in some countries, a large street will \nhave many subdivisions with numbers. Normally the subdivision name is the same as the road name, but with a number to identifiy it. Eg. SOI SUKUMVIT 3, SUKUMVIT RD, BANGKOK', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 775, 1)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostOffice'), CTD_ANON_36, scope=CTD_ANON_27, documentation='Specification of a post office. Examples are a rural post office where post is delivered and a post office containing post office boxes.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1072, 1)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, scope=CTD_ANON_27, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostBox'), CTD_ANON_44, scope=CTD_ANON_27, documentation='Specification of a postbox like mail delivery point. Only a single postbox number can be specified. Examples of postboxes are POBox, free mail numbers, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1223, 1)))

CTD_ANON_27._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Premise'), CTD_ANON_51, scope=CTD_ANON_27, documentation='Specification of a single premise, for example a house or a building. The premise as a whole has a unique premise (house) number or a premise name.  There could be more than \none premise in a street referenced in an address. For example a building address near a major shopping centre or raiwlay station', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1335, 1)))

def _BuildAutomaton_39 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_39
    del _BuildAutomaton_39
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 721, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 722, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 732, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 746, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 747, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 748, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 754, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 755, 4))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 721, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LocalityName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 722, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostBox')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 733, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'LargeMailUser')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 734, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostOffice')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 739, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalRoute')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 740, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Thoroughfare')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 746, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Premise')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 747, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DependentLocality')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 748, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_27._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 754, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 755, 4))
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
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_27._Automaton = _BuildAutomaton_39()




def _BuildAutomaton_40 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_40
    del _BuildAutomaton_40
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 726, 5))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_28._Automaton = _BuildAutomaton_40()




CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_29, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberPrefix'), CTD_ANON_55, scope=CTD_ANON_29, documentation='Prefix before the number. A in A12 Archer Street', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1504, 1)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberSuffix'), CTD_ANON_56, scope=CTD_ANON_29, documentation='Suffix after the number. A in 12A Archer Street', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1518, 1)))

CTD_ANON_29._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumber'), CTD_ANON_68, scope=CTD_ANON_29, documentation='Eg.: 23 Archer street or 25/15 Zero Avenue, etc', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1534, 1)))

def _BuildAutomaton_41 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_41
    del _BuildAutomaton_41
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 798, 11))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 799, 11))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 801, 11))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 798, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberPrefix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 799, 11))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 800, 11))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_29._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberSuffix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 801, 11))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_29._Automaton = _BuildAutomaton_41()




CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_30, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberPrefix'), CTD_ANON_55, scope=CTD_ANON_30, documentation='Prefix before the number. A in A12 Archer Street', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1504, 1)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberSuffix'), CTD_ANON_56, scope=CTD_ANON_30, documentation='Suffix after the number. A in 12A Archer Street', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1518, 1)))

CTD_ANON_30._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumber'), CTD_ANON_68, scope=CTD_ANON_30, documentation='Eg.: 23 Archer street or 25/15 Zero Avenue, etc', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1534, 1)))

def _BuildAutomaton_42 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_42
    del _BuildAutomaton_42
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 813, 11))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 814, 11))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 816, 11))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 813, 11))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberPrefix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 814, 11))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 815, 11))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_30._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberSuffix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 816, 11))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_30._Automaton = _BuildAutomaton_42()




CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_31, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePreDirection'), ThoroughfarePreDirectionType, scope=CTD_ANON_31, documentation='North Baker Street, where North is the pre-direction. The direction appears before the name.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 908, 7)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareLeadingType'), ThoroughfareLeadingTypeType, scope=CTD_ANON_31, documentation='Appears before the thoroughfare name. Ed. Spanish: Avenida Aurora, where Avenida is the leading type / French: Rue Moliere, where Rue is the leading type.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 913, 7)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareName'), ThoroughfareNameType, scope=CTD_ANON_31, documentation='Specification of the name of a Thoroughfare (also dependant street name): street name, canal name, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 918, 7)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareTrailingType'), ThoroughfareTrailingTypeType, scope=CTD_ANON_31, documentation='Appears after the thoroughfare name. Ed. British: Baker Lane, where Lane is the trailing type.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 923, 7)))

CTD_ANON_31._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePostDirection'), ThoroughfarePostDirectionType, scope=CTD_ANON_31, documentation='221-bis Baker Street North, where North is the post-direction. The post-direction appears after the name.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 928, 7)))

def _BuildAutomaton_43 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_43
    del _BuildAutomaton_43
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 907, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 908, 7))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 913, 7))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 918, 7))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 923, 7))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 928, 7))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 933, 7))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 907, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePreDirection')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 908, 7))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareLeadingType')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 913, 7))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 918, 7))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareTrailingType')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 923, 7))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_31._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePostDirection')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 928, 7))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 933, 7))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_31._Automaton = _BuildAutomaton_43()




CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_32, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Locality'), CTD_ANON_27, scope=CTD_ANON_32, documentation='Locality is one level lower than adminisstrative area. Eg.: cities, reservations and any other built-up areas.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 715, 1)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeAreaName'), CTD_ANON_33, scope=CTD_ANON_32, documentation=' Name of the administrative area. eg. MI in USA, NSW in Australia', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 994, 4)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubAdministrativeArea'), CTD_ANON_34, scope=CTD_ANON_32, documentation=' Specification of a sub-administrative area. An example of a sub-administrative areas is a county. There are two places where the name of an administrative \narea can be specified and in this case, one becomes sub-administrative area.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1004, 4)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostOffice'), CTD_ANON_36, scope=CTD_ANON_32, documentation='Specification of a post office. Examples are a rural post office where post is delivered and a post office containing post office boxes.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1072, 1)))

CTD_ANON_32._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, scope=CTD_ANON_32, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1)))

def _BuildAutomaton_44 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_44
    del _BuildAutomaton_44
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 993, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 994, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1004, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1047, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1052, 4))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 993, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AdministrativeAreaName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 994, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubAdministrativeArea')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1004, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Locality')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1048, 5))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostOffice')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1049, 5))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_32._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1050, 5))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1052, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_32._Automaton = _BuildAutomaton_44()




def _BuildAutomaton_45 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_45
    del _BuildAutomaton_45
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 998, 5))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_33._Automaton = _BuildAutomaton_45()




CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_34, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Locality'), CTD_ANON_27, scope=CTD_ANON_34, documentation='Locality is one level lower than adminisstrative area. Eg.: cities, reservations and any other built-up areas.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 715, 1)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubAdministrativeAreaName'), CTD_ANON_35, scope=CTD_ANON_34, documentation=' Name of the sub-administrative area', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1012, 7)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostOffice'), CTD_ANON_36, scope=CTD_ANON_34, documentation='Specification of a post office. Examples are a rural post office where post is delivered and a post office containing post office boxes.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1072, 1)))

CTD_ANON_34._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, scope=CTD_ANON_34, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1)))

def _BuildAutomaton_46 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_46
    del _BuildAutomaton_46
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1011, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1012, 7))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1022, 7))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1027, 7))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1011, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubAdministrativeAreaName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1012, 7))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Locality')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1023, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostOffice')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1024, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_34._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1025, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1027, 7))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_34._Automaton = _BuildAutomaton_46()




def _BuildAutomaton_47 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_47
    del _BuildAutomaton_47
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1016, 8))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_35._Automaton = _BuildAutomaton_47()




CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_36, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostOfficeName'), CTD_ANON_37, scope=CTD_ANON_36, documentation='Specification of the name of the post office. This can be a rural postoffice where post is delivered or a post office containing post office boxes.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1080, 5)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostOfficeNumber'), CTD_ANON_65, scope=CTD_ANON_36, documentation='Specification of the number of the postoffice. Common in rural postoffices', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1090, 5)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalRoute'), PostalRouteType, scope=CTD_ANON_36, documentation='A Postal van is specific for a route as in Is`rael, Rural route', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1116, 4)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, scope=CTD_ANON_36, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1)))

CTD_ANON_36._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostBox'), CTD_ANON_44, scope=CTD_ANON_36, documentation='Specification of a postbox like mail delivery point. Only a single postbox number can be specified. Examples of postboxes are POBox, free mail numbers, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1223, 1)))

def _BuildAutomaton_48 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_48
    del _BuildAutomaton_48
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1078, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1080, 5))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1090, 5))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1116, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1121, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1122, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1123, 4))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1078, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostOfficeName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1080, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostOfficeNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1090, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalRoute')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1116, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostBox')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1121, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_36._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1122, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1123, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
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
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_36._Automaton = _BuildAutomaton_48()




def _BuildAutomaton_49 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_49
    del _BuildAutomaton_49
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1084, 6))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_37._Automaton = _BuildAutomaton_49()




CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_38, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCodeNumber'), CTD_ANON_39, scope=CTD_ANON_38, documentation='Specification of a postcode. The postcode is formatted according to country-specific rules. Example: SW3 0A8-1A, 600074, 2067', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1145, 4)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCodeNumberExtension'), CTD_ANON_40, scope=CTD_ANON_38, documentation='Examples are: 1234 (USA), 1G (UK), etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1159, 4)))

CTD_ANON_38._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostTown'), CTD_ANON_41, scope=CTD_ANON_38, documentation='A post town is not the same as a locality. A post town can encompass a collection of (small) localities. It can also be a subpart of a locality. An actual post town in Norway is "Bergen".', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1178, 4)))

def _BuildAutomaton_50 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_50
    del _BuildAutomaton_50
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1144, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1145, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1159, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1178, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1213, 4))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1144, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCodeNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1145, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCodeNumberExtension')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1159, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_38._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostTown')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1178, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1213, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_38._Automaton = _BuildAutomaton_50()




def _BuildAutomaton_51 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_51
    del _BuildAutomaton_51
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1149, 5))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_39._Automaton = _BuildAutomaton_51()




def _BuildAutomaton_52 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_52
    del _BuildAutomaton_52
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1163, 5))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_40._Automaton = _BuildAutomaton_52()




CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_41, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostTownName'), CTD_ANON_42, scope=CTD_ANON_41, documentation='Name of the post town', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1185, 7)))

CTD_ANON_41._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostTownSuffix'), CTD_ANON_43, scope=CTD_ANON_41, documentation='GENERAL PO in MIAMI GENERAL PO', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1195, 7)))

def _BuildAutomaton_53 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_53
    del _BuildAutomaton_53
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1184, 7))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1185, 7))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1195, 7))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1184, 7))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostTownName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1185, 7))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_41._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostTownSuffix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1195, 7))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_41._Automaton = _BuildAutomaton_53()




def _BuildAutomaton_54 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_54
    del _BuildAutomaton_54
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1189, 8))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_42._Automaton = _BuildAutomaton_54()




def _BuildAutomaton_55 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_55
    del _BuildAutomaton_55
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1199, 8))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_43._Automaton = _BuildAutomaton_55()




CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_44, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, scope=CTD_ANON_44, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostBoxNumber'), CTD_ANON_45, scope=CTD_ANON_44, documentation='Specification of the number of a postbox', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1230, 4)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostBoxNumberPrefix'), CTD_ANON_46, scope=CTD_ANON_44, documentation='Specification of the prefix of the post box number. eg. A in POBox:A-123', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1239, 4)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostBoxNumberSuffix'), CTD_ANON_47, scope=CTD_ANON_44, documentation='Specification of the suffix of the post box number. eg. A in POBox:123A', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1253, 4)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostBoxNumberExtension'), CTD_ANON_48, scope=CTD_ANON_44, documentation='Some countries like USA have POBox as 12345-123', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1267, 4)))

CTD_ANON_44._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Firm'), FirmType, scope=CTD_ANON_44, documentation='Specification of a firm, company, organization, etc. It can be specified as part of an address that contains a street or a postbox. It is therefore different from \na large mail user address, which contains no street.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1280, 4)))

def _BuildAutomaton_56 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_56
    del _BuildAutomaton_56
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1229, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1239, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1253, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1267, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1280, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1286, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1287, 4))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1229, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostBoxNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1230, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostBoxNumberPrefix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1239, 4))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostBoxNumberSuffix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1253, 4))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostBoxNumberExtension')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1267, 4))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Firm')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1280, 4))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_44._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1286, 4))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1287, 4))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
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
CTD_ANON_44._Automaton = _BuildAutomaton_56()




def _BuildAutomaton_57 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_57
    del _BuildAutomaton_57
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_45._Automaton = _BuildAutomaton_57()




def _BuildAutomaton_58 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_58
    del _BuildAutomaton_58
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1243, 5))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_46._Automaton = _BuildAutomaton_58()




def _BuildAutomaton_59 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_59
    del _BuildAutomaton_59
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1257, 5))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_47._Automaton = _BuildAutomaton_59()




def _BuildAutomaton_60 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_60
    del _BuildAutomaton_60
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1271, 5))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_48._Automaton = _BuildAutomaton_60()




CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_49, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, scope=CTD_ANON_49, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1)))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DepartmentName'), CTD_ANON_50, scope=CTD_ANON_49, documentation='Specification of the name of a department.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1309, 4)))

CTD_ANON_49._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MailStop'), MailStopType, scope=CTD_ANON_49, documentation='A MailStop is where the the mail is delivered to within a premise/subpremise/firm or a facility.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1319, 4)))

def _BuildAutomaton_61 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_61
    del _BuildAutomaton_61
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1308, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1309, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1319, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1324, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1325, 4))
    counters.add(cc_4)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1308, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DepartmentName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1309, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MailStop')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1319, 4))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_49._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1324, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1325, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
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
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_49._Automaton = _BuildAutomaton_61()




def _BuildAutomaton_62 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_62
    del _BuildAutomaton_62
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1313, 5))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_50._Automaton = _BuildAutomaton_62()




CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_51, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, scope=CTD_ANON_51, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Premise'), CTD_ANON_51, scope=CTD_ANON_51, documentation='Specification of a single premise, for example a house or a building. The premise as a whole has a unique premise (house) number or a premise name.  There could be more than \none premise in a street referenced in an address. For example a building address near a major shopping centre or raiwlay station', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1335, 1)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseName'), CTD_ANON_66, scope=CTD_ANON_51, documentation='Specification of the name of the premise (house, building, park, farm, etc). A premise name is specified when the premise cannot be addressed using a street name plus premise (house) number.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1343, 4)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseLocation'), CTD_ANON_52, scope=CTD_ANON_51, documentation='LOBBY, BASEMENT, GROUND FLOOR, etc...', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1365, 5)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberRange'), CTD_ANON_67, scope=CTD_ANON_51, documentation='Specification for defining the premise number range. Some premises have number as Building C1-C7', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1376, 6)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BuildingName'), BuildingNameType, scope=CTD_ANON_51, documentation='Specification of the name of a building.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1455, 4)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SubPremise'), SubPremiseType, scope=CTD_ANON_51, documentation='Specification of a single sub-premise. Examples of sub-premises are apartments and suites. Each sub-premise should be uniquely identifiable.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1461, 5)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Firm'), FirmType, scope=CTD_ANON_51, documentation='Specification of a firm, company, organization, etc. It can be specified as part of an address that contains a street or a postbox. It is therefore different from a large mail user address, which contains no street.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1466, 5)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MailStop'), MailStopType, scope=CTD_ANON_51, documentation='A MailStop is where the the mail is delivered to within a premise/subpremise/firm or a facility.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1472, 4)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumber'), CTD_ANON_69, scope=CTD_ANON_51, documentation='Specification of the identifier of the premise (house, building, etc). Premises in a street are often uniquely identified by means of consecutive identifiers. The identifier can be a number, a letter or any combination of the two.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1584, 1)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberPrefix'), CTD_ANON_57, scope=CTD_ANON_51, documentation='A in A12', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1632, 1)))

CTD_ANON_51._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberSuffix'), CTD_ANON_58, scope=CTD_ANON_51, documentation='A in 12A', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1651, 1)))

def _BuildAutomaton_63 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_63
    del _BuildAutomaton_63
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1342, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1343, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1364, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1453, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1454, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1455, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1461, 5))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1466, 5))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1472, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1477, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1478, 4))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1479, 4))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1342, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1343, 4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseLocation')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1365, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1375, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberRange')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1376, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberPrefix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1453, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberSuffix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1454, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BuildingName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1455, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'SubPremise')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1461, 5))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Firm')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1466, 5))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MailStop')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1472, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1477, 4))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_51._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Premise')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1478, 4))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1479, 4))
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
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_51._Automaton = _BuildAutomaton_63()




def _BuildAutomaton_64 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_64
    del _BuildAutomaton_64
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_52._Automaton = _BuildAutomaton_64()




CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_53, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumber'), CTD_ANON_69, scope=CTD_ANON_53, documentation='Specification of the identifier of the premise (house, building, etc). Premises in a street are often uniquely identified by means of consecutive identifiers. The identifier can be a number, a letter or any combination of the two.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1584, 1)))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberPrefix'), CTD_ANON_57, scope=CTD_ANON_53, documentation='A in A12', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1632, 1)))

CTD_ANON_53._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberSuffix'), CTD_ANON_58, scope=CTD_ANON_53, documentation='A in 12A', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1651, 1)))

def _BuildAutomaton_65 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_65
    del _BuildAutomaton_65
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1388, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1389, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1391, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1388, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberPrefix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1389, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1390, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_53._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberSuffix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1391, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_53._Automaton = _BuildAutomaton_65()




CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_54, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumber'), CTD_ANON_69, scope=CTD_ANON_54, documentation='Specification of the identifier of the premise (house, building, etc). Premises in a street are often uniquely identified by means of consecutive identifiers. The identifier can be a number, a letter or any combination of the two.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1584, 1)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberPrefix'), CTD_ANON_57, scope=CTD_ANON_54, documentation='A in A12', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1632, 1)))

CTD_ANON_54._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberSuffix'), CTD_ANON_58, scope=CTD_ANON_54, documentation='A in 12A', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1651, 1)))

def _BuildAutomaton_66 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_66
    del _BuildAutomaton_66
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1401, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1402, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1404, 12))
    counters.add(cc_2)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1401, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberPrefix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1402, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1403, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_54._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberSuffix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1404, 12))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_54._Automaton = _BuildAutomaton_66()




def _BuildAutomaton_67 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_67
    del _BuildAutomaton_67
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_55._Automaton = _BuildAutomaton_67()




def _BuildAutomaton_68 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_68
    del _BuildAutomaton_68
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_56._Automaton = _BuildAutomaton_68()




def _BuildAutomaton_69 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_69
    del _BuildAutomaton_69
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_58._Automaton = _BuildAutomaton_69()




def _BuildAutomaton_70 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_70
    del _BuildAutomaton_70
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_59._Automaton = _BuildAutomaton_70()




def _BuildAutomaton_71 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_71
    del _BuildAutomaton_71
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
BuildingNameType._Automaton = _BuildAutomaton_71()




def _BuildAutomaton_72 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_72
    del _BuildAutomaton_72
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 340, 4))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_60._Automaton = _BuildAutomaton_72()




def _BuildAutomaton_73 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_73
    del _BuildAutomaton_73
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 547, 4))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_61._Automaton = _BuildAutomaton_73()




def _BuildAutomaton_74 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_74
    del _BuildAutomaton_74
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 579, 5))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_62._Automaton = _BuildAutomaton_74()




CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_63, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberRange'), CTD_ANON_64, scope=CTD_ANON_63, documentation='A container to represent a range of numbers (from x thru y)for a thoroughfare. eg. 1-2 Albert Av', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 785, 5)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePreDirection'), ThoroughfarePreDirectionType, scope=CTD_ANON_63, documentation='North Baker Street, where North is the pre-direction. The direction appears before the name.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 876, 4)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareLeadingType'), ThoroughfareLeadingTypeType, scope=CTD_ANON_63, documentation='Appears before the thoroughfare name. Ed. Spanish: Avenida Aurora, where Avenida is the leading type / French: Rue Moliere, where Rue is the leading type.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 881, 4)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareName'), ThoroughfareNameType, scope=CTD_ANON_63, documentation='Specification of the name of a Thoroughfare (also dependant street name): street name, canal name, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 886, 4)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareTrailingType'), ThoroughfareTrailingTypeType, scope=CTD_ANON_63, documentation='Appears after the thoroughfare name. Ed. British: Baker Lane, where Lane is the trailing type.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 891, 4)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePostDirection'), ThoroughfarePostDirectionType, scope=CTD_ANON_63, documentation='221-bis Baker Street North, where North is the post-direction. The post-direction appears after the name.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 896, 4)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DependentThoroughfare'), CTD_ANON_31, scope=CTD_ANON_63, documentation='DependentThroughfare is related to a street; occurs in GB, IE, ES, PT', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 901, 4)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DependentLocality'), DependentLocalityType, scope=CTD_ANON_63, documentation='Dependent localities are Districts within cities/towns, locality divisions, postal \ndivisions of cities, suburbs, etc. DependentLocality is a recursive element, but no nesting deeper than two exists (Locality-DependentLocality-DependentLocality).', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 940, 5)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Firm'), FirmType, scope=CTD_ANON_63, documentation='Specification of a firm, company, organization, etc. It can be specified as part of an address that contains a street or a postbox. It is therefore different from \na large mail user address, which contains no street.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 947, 5)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PostalCode'), CTD_ANON_38, scope=CTD_ANON_63, documentation='PostalCode is the container element for either simple or complex (extended) postal codes. Type: Area Code, Postcode, etc.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1138, 1)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Premise'), CTD_ANON_51, scope=CTD_ANON_63, documentation='Specification of a single premise, for example a house or a building. The premise as a whole has a unique premise (house) number or a premise name.  There could be more than \none premise in a street referenced in an address. For example a building address near a major shopping centre or raiwlay station', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1335, 1)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberPrefix'), CTD_ANON_55, scope=CTD_ANON_63, documentation='Prefix before the number. A in A12 Archer Street', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1504, 1)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberSuffix'), CTD_ANON_56, scope=CTD_ANON_63, documentation='Suffix after the number. A in 12A Archer Street', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1518, 1)))

CTD_ANON_63._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumber'), CTD_ANON_68, scope=CTD_ANON_63, documentation='Eg.: 23 Archer street or 25/15 Zero Avenue, etc', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1534, 1)))

def _BuildAutomaton_75 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_75
    del _BuildAutomaton_75
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 782, 4))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 783, 4))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 874, 4))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 875, 4))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 876, 4))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 881, 4))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 886, 4))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 891, 4))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 896, 4))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 901, 4))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 939, 4))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 955, 4))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 782, 4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumber')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 784, 5))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberRange')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 785, 5))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberPrefix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 874, 4))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberSuffix')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 875, 4))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePreDirection')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 876, 4))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareLeadingType')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 881, 4))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareName')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 886, 4))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareTrailingType')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 891, 4))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfarePostDirection')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 896, 4))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DependentThoroughfare')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 901, 4))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DependentLocality')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 940, 5))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Premise')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 946, 5))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Firm')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 947, 5))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_63._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PostalCode')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 953, 5))
    st_14 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'urn:oasis:names:tc:ciq:xsdschema:xAL:2.0')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 955, 4))
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
        fac.UpdateInstruction(cc_1, True) ]))
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
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
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
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
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
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, True) ]))
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
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, True) ]))
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
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, True) ]))
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
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, True) ]))
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
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, True) ]))
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
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, True) ]))
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
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_63._Automaton = _BuildAutomaton_75()




CTD_ANON_64._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AddressLine'), CTD_ANON_26, scope=CTD_ANON_64, documentation='Free format address representation. An address can have more than one line. The order of the AddressLine elements must be preserved.', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 701, 1)))

CTD_ANON_64._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberFrom'), CTD_ANON_29, scope=CTD_ANON_64, documentation='Starting number in the range', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 792, 8)))

CTD_ANON_64._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberTo'), CTD_ANON_30, scope=CTD_ANON_64, documentation='Ending number in the range', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 807, 8)))

def _BuildAutomaton_76 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_76
    del _BuildAutomaton_76
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 791, 8))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_64._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AddressLine')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 791, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_64._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberFrom')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 792, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_64._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ThoroughfareNumberTo')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 807, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_64._Automaton = _BuildAutomaton_76()




def _BuildAutomaton_77 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_77
    del _BuildAutomaton_77
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1094, 6))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_65._Automaton = _BuildAutomaton_77()




def _BuildAutomaton_78 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_78
    del _BuildAutomaton_78
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1347, 5))
    counters.add(cc_0)
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_66._Automaton = _BuildAutomaton_78()




CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberRangeFrom'), CTD_ANON_53, scope=CTD_ANON_67, documentation='Start number details of the premise number range', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1382, 9)))

CTD_ANON_67._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberRangeTo'), CTD_ANON_54, scope=CTD_ANON_67, documentation='End number details of the premise number range', location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1395, 9)))

def _BuildAutomaton_79 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_79
    del _BuildAutomaton_79
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberRangeFrom')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1382, 9))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON_67._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PremiseNumberRangeTo')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/citygml/xAL/xAL.xsd', 1395, 9))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON_67._Automaton = _BuildAutomaton_79()




def _BuildAutomaton_80 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_80
    del _BuildAutomaton_80
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_68._Automaton = _BuildAutomaton_80()




def _BuildAutomaton_81 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_81
    del _BuildAutomaton_81
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    return fac.Automaton(states, counters, True, containing_state=None)
CTD_ANON_69._Automaton = _BuildAutomaton_81()

