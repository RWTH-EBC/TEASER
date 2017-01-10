# ./pyxb/bundles/opengis/raw/_nsgroup.py
# -*- coding: utf-8 -*-
# PyXB bindings for NGM:d16379a067651cb41378191b4775061fa96b7ead
# Generated 2017-01-09 16:11:10.920900 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Group contents:
# Namespace http://www.w3.org/2001/SMIL20/ [xmlns:smil20]
# Namespace http://www.w3.org/2001/SMIL20/Language [xmlns:smil20lang]


from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.utils.utility
import pyxb.utils.six as _six
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:d9a6d838-d67d-11e6-8d7b-100ba9a189d0')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.xml_
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
_Namespace_smil20 = pyxb.namespace.NamespaceForURI('http://www.w3.org/2001/SMIL20/', create_if_missing=True)
_Namespace_smil20.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_smil20lang = pyxb.namespace.NamespaceForURI('http://www.w3.org/2001/SMIL20/Language', create_if_missing=True)
_Namespace_smil20lang.configureCategories(['typeBinding', 'elementBinding'])

# Atomic simple type: {http://www.w3.org/2001/SMIL20/}nonNegativeDecimalType
class nonNegativeDecimalType (pyxb.binding.datatypes.decimal):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20, 'nonNegativeDecimalType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 57, 1)
    _Documentation = None
nonNegativeDecimalType._CF_minInclusive = pyxb.binding.facets.CF_minInclusive(value_datatype=nonNegativeDecimalType, value=pyxb.binding.datatypes.decimal('0.0'))
nonNegativeDecimalType._InitializeFacetMap(nonNegativeDecimalType._CF_minInclusive)
_Namespace_smil20.addCategoryObject('typeBinding', 'nonNegativeDecimalType', nonNegativeDecimalType)
_module_typeBindings.nonNegativeDecimalType = nonNegativeDecimalType

# Atomic simple type: [anonymous]
class STD_ANON (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 74, 3)
    _Documentation = None
STD_ANON._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON, enum_prefix=None)
STD_ANON.XML = STD_ANON._CF_enumeration.addEnumeration(unicode_value='XML', tag='XML')
STD_ANON.CSS = STD_ANON._CF_enumeration.addEnumeration(unicode_value='CSS', tag='CSS')
STD_ANON.auto = STD_ANON._CF_enumeration.addEnumeration(unicode_value='auto', tag='auto')
STD_ANON._InitializeFacetMap(STD_ANON._CF_enumeration)
_module_typeBindings.STD_ANON = STD_ANON

# Atomic simple type: [anonymous]
class STD_ANON_ (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 85, 3)
    _Documentation = None
STD_ANON_._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_, enum_prefix=None)
STD_ANON_.replace = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='replace', tag='replace')
STD_ANON_.sum = STD_ANON_._CF_enumeration.addEnumeration(unicode_value='sum', tag='sum')
STD_ANON_._InitializeFacetMap(STD_ANON_._CF_enumeration)
_module_typeBindings.STD_ANON_ = STD_ANON_

# Atomic simple type: [anonymous]
class STD_ANON_2 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 93, 3)
    _Documentation = None
STD_ANON_2._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_2, enum_prefix=None)
STD_ANON_2.none = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='none', tag='none')
STD_ANON_2.sum = STD_ANON_2._CF_enumeration.addEnumeration(unicode_value='sum', tag='sum')
STD_ANON_2._InitializeFacetMap(STD_ANON_2._CF_enumeration)
_module_typeBindings.STD_ANON_2 = STD_ANON_2

# Atomic simple type: [anonymous]
class STD_ANON_3 (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 115, 3)
    _Documentation = None
STD_ANON_3._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=STD_ANON_3, enum_prefix=None)
STD_ANON_3.discrete = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='discrete', tag='discrete')
STD_ANON_3.linear = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='linear', tag='linear')
STD_ANON_3.paced = STD_ANON_3._CF_enumeration.addEnumeration(unicode_value='paced', tag='paced')
STD_ANON_3._InitializeFacetMap(STD_ANON_3._CF_enumeration)
_module_typeBindings.STD_ANON_3 = STD_ANON_3

# Atomic simple type: {http://www.w3.org/2001/SMIL20/}syncBehaviorType
class syncBehaviorType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20, 'syncBehaviorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 148, 1)
    _Documentation = None
syncBehaviorType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=syncBehaviorType, enum_prefix=None)
syncBehaviorType.canSlip = syncBehaviorType._CF_enumeration.addEnumeration(unicode_value='canSlip', tag='canSlip')
syncBehaviorType.locked = syncBehaviorType._CF_enumeration.addEnumeration(unicode_value='locked', tag='locked')
syncBehaviorType.independent = syncBehaviorType._CF_enumeration.addEnumeration(unicode_value='independent', tag='independent')
syncBehaviorType.default = syncBehaviorType._CF_enumeration.addEnumeration(unicode_value='default', tag='default')
syncBehaviorType._InitializeFacetMap(syncBehaviorType._CF_enumeration)
_Namespace_smil20.addCategoryObject('typeBinding', 'syncBehaviorType', syncBehaviorType)
_module_typeBindings.syncBehaviorType = syncBehaviorType

# Atomic simple type: {http://www.w3.org/2001/SMIL20/}syncBehaviorDefaultType
class syncBehaviorDefaultType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20, 'syncBehaviorDefaultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 160, 1)
    _Documentation = None
syncBehaviorDefaultType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=syncBehaviorDefaultType, enum_prefix=None)
syncBehaviorDefaultType.canSlip = syncBehaviorDefaultType._CF_enumeration.addEnumeration(unicode_value='canSlip', tag='canSlip')
syncBehaviorDefaultType.locked = syncBehaviorDefaultType._CF_enumeration.addEnumeration(unicode_value='locked', tag='locked')
syncBehaviorDefaultType.independent = syncBehaviorDefaultType._CF_enumeration.addEnumeration(unicode_value='independent', tag='independent')
syncBehaviorDefaultType.inherit = syncBehaviorDefaultType._CF_enumeration.addEnumeration(unicode_value='inherit', tag='inherit')
syncBehaviorDefaultType._InitializeFacetMap(syncBehaviorDefaultType._CF_enumeration)
_Namespace_smil20.addCategoryObject('typeBinding', 'syncBehaviorDefaultType', syncBehaviorDefaultType)
_module_typeBindings.syncBehaviorDefaultType = syncBehaviorDefaultType

# Atomic simple type: {http://www.w3.org/2001/SMIL20/}restartTimingType
class restartTimingType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20, 'restartTimingType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 171, 1)
    _Documentation = None
restartTimingType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=restartTimingType, enum_prefix=None)
restartTimingType.never = restartTimingType._CF_enumeration.addEnumeration(unicode_value='never', tag='never')
restartTimingType.always = restartTimingType._CF_enumeration.addEnumeration(unicode_value='always', tag='always')
restartTimingType.whenNotActive = restartTimingType._CF_enumeration.addEnumeration(unicode_value='whenNotActive', tag='whenNotActive')
restartTimingType.default = restartTimingType._CF_enumeration.addEnumeration(unicode_value='default', tag='default')
restartTimingType._InitializeFacetMap(restartTimingType._CF_enumeration)
_Namespace_smil20.addCategoryObject('typeBinding', 'restartTimingType', restartTimingType)
_module_typeBindings.restartTimingType = restartTimingType

# Atomic simple type: {http://www.w3.org/2001/SMIL20/}restartDefaultType
class restartDefaultType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20, 'restartDefaultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 182, 1)
    _Documentation = None
restartDefaultType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=restartDefaultType, enum_prefix=None)
restartDefaultType.never = restartDefaultType._CF_enumeration.addEnumeration(unicode_value='never', tag='never')
restartDefaultType.always = restartDefaultType._CF_enumeration.addEnumeration(unicode_value='always', tag='always')
restartDefaultType.whenNotActive = restartDefaultType._CF_enumeration.addEnumeration(unicode_value='whenNotActive', tag='whenNotActive')
restartDefaultType.inherit = restartDefaultType._CF_enumeration.addEnumeration(unicode_value='inherit', tag='inherit')
restartDefaultType._InitializeFacetMap(restartDefaultType._CF_enumeration)
_Namespace_smil20.addCategoryObject('typeBinding', 'restartDefaultType', restartDefaultType)
_module_typeBindings.restartDefaultType = restartDefaultType

# Atomic simple type: {http://www.w3.org/2001/SMIL20/}fillTimingAttrsType
class fillTimingAttrsType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20, 'fillTimingAttrsType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 193, 1)
    _Documentation = None
fillTimingAttrsType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fillTimingAttrsType, enum_prefix=None)
fillTimingAttrsType.remove = fillTimingAttrsType._CF_enumeration.addEnumeration(unicode_value='remove', tag='remove')
fillTimingAttrsType.freeze = fillTimingAttrsType._CF_enumeration.addEnumeration(unicode_value='freeze', tag='freeze')
fillTimingAttrsType.hold = fillTimingAttrsType._CF_enumeration.addEnumeration(unicode_value='hold', tag='hold')
fillTimingAttrsType.auto = fillTimingAttrsType._CF_enumeration.addEnumeration(unicode_value='auto', tag='auto')
fillTimingAttrsType.default = fillTimingAttrsType._CF_enumeration.addEnumeration(unicode_value='default', tag='default')
fillTimingAttrsType.transition = fillTimingAttrsType._CF_enumeration.addEnumeration(unicode_value='transition', tag='transition')
fillTimingAttrsType._InitializeFacetMap(fillTimingAttrsType._CF_enumeration)
_Namespace_smil20.addCategoryObject('typeBinding', 'fillTimingAttrsType', fillTimingAttrsType)
_module_typeBindings.fillTimingAttrsType = fillTimingAttrsType

# Atomic simple type: {http://www.w3.org/2001/SMIL20/}fillDefaultType
class fillDefaultType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20, 'fillDefaultType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 206, 1)
    _Documentation = None
fillDefaultType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=fillDefaultType, enum_prefix=None)
fillDefaultType.remove = fillDefaultType._CF_enumeration.addEnumeration(unicode_value='remove', tag='remove')
fillDefaultType.freeze = fillDefaultType._CF_enumeration.addEnumeration(unicode_value='freeze', tag='freeze')
fillDefaultType.hold = fillDefaultType._CF_enumeration.addEnumeration(unicode_value='hold', tag='hold')
fillDefaultType.auto = fillDefaultType._CF_enumeration.addEnumeration(unicode_value='auto', tag='auto')
fillDefaultType.inherit = fillDefaultType._CF_enumeration.addEnumeration(unicode_value='inherit', tag='inherit')
fillDefaultType.transition = fillDefaultType._CF_enumeration.addEnumeration(unicode_value='transition', tag='transition')
fillDefaultType._InitializeFacetMap(fillDefaultType._CF_enumeration)
_Namespace_smil20.addCategoryObject('typeBinding', 'fillDefaultType', fillDefaultType)
_module_typeBindings.fillDefaultType = fillDefaultType

# Complex type {http://www.w3.org/2001/SMIL20/}animatePrototype with content type EMPTY
class animatePrototype (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2001/SMIL20/}animatePrototype with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20, 'animatePrototype')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 66, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute attributeName uses Python identifier attributeName
    __attributeName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'attributeName'), 'attributeName', '__httpwww_w3_org2001SMIL20_animatePrototype_attributeName', pyxb.binding.datatypes.string, required=True)
    __attributeName._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 72, 2)
    __attributeName._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 72, 2)
    
    attributeName = property(__attributeName.value, __attributeName.set, None, None)

    
    # Attribute attributeType uses Python identifier attributeType
    __attributeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'attributeType'), 'attributeType', '__httpwww_w3_org2001SMIL20_animatePrototype_attributeType', _module_typeBindings.STD_ANON, unicode_default='auto')
    __attributeType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 73, 2)
    __attributeType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 73, 2)
    
    attributeType = property(__attributeType.value, __attributeType.set, None, None)

    
    # Attribute additive uses Python identifier additive
    __additive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'additive'), 'additive', '__httpwww_w3_org2001SMIL20_animatePrototype_additive', _module_typeBindings.STD_ANON_, unicode_default='replace')
    __additive._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 84, 2)
    __additive._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 84, 2)
    
    additive = property(__additive.value, __additive.set, None, None)

    
    # Attribute accumulate uses Python identifier accumulate
    __accumulate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accumulate'), 'accumulate', '__httpwww_w3_org2001SMIL20_animatePrototype_accumulate', _module_typeBindings.STD_ANON_2, unicode_default='none')
    __accumulate._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 92, 2)
    __accumulate._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 92, 2)
    
    accumulate = property(__accumulate.value, __accumulate.set, None, None)

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__httpwww_w3_org2001SMIL20_animatePrototype_from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 103, 2)
    __from._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 103, 2)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute by uses Python identifier by
    __by = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'by'), 'by', '__httpwww_w3_org2001SMIL20_animatePrototype_by', pyxb.binding.datatypes.string)
    __by._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 104, 2)
    __by._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 104, 2)
    
    by = property(__by.value, __by.set, None, None)

    
    # Attribute values uses Python identifier values
    __values = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'values'), 'values', '__httpwww_w3_org2001SMIL20_animatePrototype_values', pyxb.binding.datatypes.string)
    __values._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 105, 2)
    __values._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 105, 2)
    
    values = property(__values.value, __values.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__httpwww_w3_org2001SMIL20_animatePrototype_to', pyxb.binding.datatypes.string)
    __to._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 108, 2)
    __to._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 108, 2)
    
    to = property(__to.value, __to.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __attributeName.name() : __attributeName,
        __attributeType.name() : __attributeType,
        __additive.name() : __additive,
        __accumulate.name() : __accumulate,
        __from.name() : __from,
        __by.name() : __by,
        __values.name() : __values,
        __to.name() : __to
    })
_module_typeBindings.animatePrototype = animatePrototype
_Namespace_smil20.addCategoryObject('typeBinding', 'animatePrototype', animatePrototype)


# Complex type {http://www.w3.org/2001/SMIL20/}animateMotionPrototype with content type EMPTY
class animateMotionPrototype (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2001/SMIL20/}animateMotionPrototype with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20, 'animateMotionPrototype')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 125, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute additive uses Python identifier additive
    __additive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'additive'), 'additive', '__httpwww_w3_org2001SMIL20_animateMotionPrototype_additive', _module_typeBindings.STD_ANON_, unicode_default='replace')
    __additive._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 84, 2)
    __additive._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 84, 2)
    
    additive = property(__additive.value, __additive.set, None, None)

    
    # Attribute accumulate uses Python identifier accumulate
    __accumulate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accumulate'), 'accumulate', '__httpwww_w3_org2001SMIL20_animateMotionPrototype_accumulate', _module_typeBindings.STD_ANON_2, unicode_default='none')
    __accumulate._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 92, 2)
    __accumulate._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 92, 2)
    
    accumulate = property(__accumulate.value, __accumulate.set, None, None)

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__httpwww_w3_org2001SMIL20_animateMotionPrototype_from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 103, 2)
    __from._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 103, 2)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute by uses Python identifier by
    __by = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'by'), 'by', '__httpwww_w3_org2001SMIL20_animateMotionPrototype_by', pyxb.binding.datatypes.string)
    __by._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 104, 2)
    __by._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 104, 2)
    
    by = property(__by.value, __by.set, None, None)

    
    # Attribute values uses Python identifier values
    __values = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'values'), 'values', '__httpwww_w3_org2001SMIL20_animateMotionPrototype_values', pyxb.binding.datatypes.string)
    __values._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 105, 2)
    __values._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 105, 2)
    
    values = property(__values.value, __values.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__httpwww_w3_org2001SMIL20_animateMotionPrototype_to', pyxb.binding.datatypes.string)
    __to._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 108, 2)
    __to._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 108, 2)
    
    to = property(__to.value, __to.set, None, None)

    
    # Attribute origin uses Python identifier origin
    __origin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'origin'), 'origin', '__httpwww_w3_org2001SMIL20_animateMotionPrototype_origin', pyxb.binding.datatypes.string)
    __origin._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 128, 2)
    __origin._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 128, 2)
    
    origin = property(__origin.value, __origin.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __additive.name() : __additive,
        __accumulate.name() : __accumulate,
        __from.name() : __from,
        __by.name() : __by,
        __values.name() : __values,
        __to.name() : __to,
        __origin.name() : __origin
    })
_module_typeBindings.animateMotionPrototype = animateMotionPrototype
_Namespace_smil20.addCategoryObject('typeBinding', 'animateMotionPrototype', animateMotionPrototype)


# Complex type {http://www.w3.org/2001/SMIL20/}animateColorPrototype with content type EMPTY
class animateColorPrototype (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2001/SMIL20/}animateColorPrototype with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20, 'animateColorPrototype')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 131, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute attributeName uses Python identifier attributeName
    __attributeName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'attributeName'), 'attributeName', '__httpwww_w3_org2001SMIL20_animateColorPrototype_attributeName', pyxb.binding.datatypes.string, required=True)
    __attributeName._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 72, 2)
    __attributeName._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 72, 2)
    
    attributeName = property(__attributeName.value, __attributeName.set, None, None)

    
    # Attribute attributeType uses Python identifier attributeType
    __attributeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'attributeType'), 'attributeType', '__httpwww_w3_org2001SMIL20_animateColorPrototype_attributeType', _module_typeBindings.STD_ANON, unicode_default='auto')
    __attributeType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 73, 2)
    __attributeType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 73, 2)
    
    attributeType = property(__attributeType.value, __attributeType.set, None, None)

    
    # Attribute additive uses Python identifier additive
    __additive = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'additive'), 'additive', '__httpwww_w3_org2001SMIL20_animateColorPrototype_additive', _module_typeBindings.STD_ANON_, unicode_default='replace')
    __additive._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 84, 2)
    __additive._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 84, 2)
    
    additive = property(__additive.value, __additive.set, None, None)

    
    # Attribute accumulate uses Python identifier accumulate
    __accumulate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'accumulate'), 'accumulate', '__httpwww_w3_org2001SMIL20_animateColorPrototype_accumulate', _module_typeBindings.STD_ANON_2, unicode_default='none')
    __accumulate._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 92, 2)
    __accumulate._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 92, 2)
    
    accumulate = property(__accumulate.value, __accumulate.set, None, None)

    
    # Attribute from uses Python identifier from_
    __from = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'from'), 'from_', '__httpwww_w3_org2001SMIL20_animateColorPrototype_from', pyxb.binding.datatypes.string)
    __from._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 103, 2)
    __from._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 103, 2)
    
    from_ = property(__from.value, __from.set, None, None)

    
    # Attribute by uses Python identifier by
    __by = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'by'), 'by', '__httpwww_w3_org2001SMIL20_animateColorPrototype_by', pyxb.binding.datatypes.string)
    __by._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 104, 2)
    __by._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 104, 2)
    
    by = property(__by.value, __by.set, None, None)

    
    # Attribute values uses Python identifier values
    __values = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'values'), 'values', '__httpwww_w3_org2001SMIL20_animateColorPrototype_values', pyxb.binding.datatypes.string)
    __values._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 105, 2)
    __values._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 105, 2)
    
    values = property(__values.value, __values.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__httpwww_w3_org2001SMIL20_animateColorPrototype_to', pyxb.binding.datatypes.string)
    __to._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 108, 2)
    __to._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 108, 2)
    
    to = property(__to.value, __to.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __attributeName.name() : __attributeName,
        __attributeType.name() : __attributeType,
        __additive.name() : __additive,
        __accumulate.name() : __accumulate,
        __from.name() : __from,
        __by.name() : __by,
        __values.name() : __values,
        __to.name() : __to
    })
_module_typeBindings.animateColorPrototype = animateColorPrototype
_Namespace_smil20.addCategoryObject('typeBinding', 'animateColorPrototype', animateColorPrototype)


# Complex type {http://www.w3.org/2001/SMIL20/}setPrototype with content type EMPTY
class setPrototype (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2001/SMIL20/}setPrototype with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20, 'setPrototype')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 137, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute attributeName uses Python identifier attributeName
    __attributeName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'attributeName'), 'attributeName', '__httpwww_w3_org2001SMIL20_setPrototype_attributeName', pyxb.binding.datatypes.string, required=True)
    __attributeName._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 72, 2)
    __attributeName._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 72, 2)
    
    attributeName = property(__attributeName.value, __attributeName.set, None, None)

    
    # Attribute attributeType uses Python identifier attributeType
    __attributeType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'attributeType'), 'attributeType', '__httpwww_w3_org2001SMIL20_setPrototype_attributeType', _module_typeBindings.STD_ANON, unicode_default='auto')
    __attributeType._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 73, 2)
    __attributeType._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 73, 2)
    
    attributeType = property(__attributeType.value, __attributeType.set, None, None)

    
    # Attribute to uses Python identifier to
    __to = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'to'), 'to', '__httpwww_w3_org2001SMIL20_setPrototype_to', pyxb.binding.datatypes.string)
    __to._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 108, 2)
    __to._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 108, 2)
    
    to = property(__to.value, __to.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __attributeName.name() : __attributeName,
        __attributeType.name() : __attributeType,
        __to.name() : __to
    })
_module_typeBindings.setPrototype = setPrototype
_Namespace_smil20.addCategoryObject('typeBinding', 'setPrototype', setPrototype)


# Complex type {http://www.w3.org/2001/SMIL20/Language}animateType with content type ELEMENT_ONLY
class animateType (animatePrototype):
    """Complex type {http://www.w3.org/2001/SMIL20/Language}animateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20lang, 'animateType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 35, 1)
    _ElementMap = animatePrototype._ElementMap.copy()
    _AttributeMap = animatePrototype._AttributeMap.copy()
    # Base type is animatePrototype
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_w3_org2001SMIL20Language_animateType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 37, 2)
    __id._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 37, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__httpwww_w3_org2001SMIL20Language_animateType_class', pyxb.binding.datatypes.string)
    __class._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 38, 2)
    __class._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 38, 2)
    
    class_ = property(__class.value, __class.set, None, None)

    
    # Attribute skip-content uses Python identifier skip_content
    __skip_content = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'skip-content'), 'skip_content', '__httpwww_w3_org2001SMIL20Language_animateType_skip_content', pyxb.binding.datatypes.boolean, unicode_default='true')
    __skip_content._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 45, 2)
    __skip_content._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 45, 2)
    
    skip_content = property(__skip_content.value, __skip_content.set, None, None)

    
    # Attribute alt uses Python identifier alt
    __alt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alt'), 'alt', '__httpwww_w3_org2001SMIL20Language_animateType_alt', pyxb.binding.datatypes.string)
    __alt._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 51, 2)
    __alt._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 51, 2)
    
    alt = property(__alt.value, __alt.set, None, None)

    
    # Attribute longdesc uses Python identifier longdesc
    __longdesc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'longdesc'), 'longdesc', '__httpwww_w3_org2001SMIL20Language_animateType_longdesc', pyxb.binding.datatypes.anyURI)
    __longdesc._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 52, 2)
    __longdesc._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 52, 2)
    
    longdesc = property(__longdesc.value, __longdesc.set, None, None)

    
    # Attribute attributeName inherited from {http://www.w3.org/2001/SMIL20/}animatePrototype
    
    # Attribute attributeType inherited from {http://www.w3.org/2001/SMIL20/}animatePrototype
    
    # Attribute additive inherited from {http://www.w3.org/2001/SMIL20/}animatePrototype
    
    # Attribute accumulate inherited from {http://www.w3.org/2001/SMIL20/}animatePrototype
    
    # Attribute from_ inherited from {http://www.w3.org/2001/SMIL20/}animatePrototype
    
    # Attribute by inherited from {http://www.w3.org/2001/SMIL20/}animatePrototype
    
    # Attribute values inherited from {http://www.w3.org/2001/SMIL20/}animatePrototype
    
    # Attribute to inherited from {http://www.w3.org/2001/SMIL20/}animatePrototype
    
    # Attribute targetElement uses Python identifier targetElement
    __targetElement = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targetElement'), 'targetElement', '__httpwww_w3_org2001SMIL20Language_animateType_targetElement', pyxb.binding.datatypes.IDREF)
    __targetElement._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 111, 2)
    __targetElement._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 111, 2)
    
    targetElement = property(__targetElement.value, __targetElement.set, None, None)

    
    # Attribute calcMode uses Python identifier calcMode
    __calcMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'calcMode'), 'calcMode', '__httpwww_w3_org2001SMIL20Language_animateType_calcMode', _module_typeBindings.STD_ANON_3, unicode_default='linear')
    __calcMode._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 114, 2)
    __calcMode._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 114, 2)
    
    calcMode = property(__calcMode.value, __calcMode.set, None, None)

    
    # Attribute syncBehavior uses Python identifier syncBehavior
    __syncBehavior = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncBehavior'), 'syncBehavior', '__httpwww_w3_org2001SMIL20Language_animateType_syncBehavior', _module_typeBindings.syncBehaviorType, unicode_default='default')
    __syncBehavior._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 145, 2)
    __syncBehavior._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 145, 2)
    
    syncBehavior = property(__syncBehavior.value, __syncBehavior.set, None, None)

    
    # Attribute syncTolerance uses Python identifier syncTolerance
    __syncTolerance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncTolerance'), 'syncTolerance', '__httpwww_w3_org2001SMIL20Language_animateType_syncTolerance', pyxb.binding.datatypes.string)
    __syncTolerance._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 146, 2)
    __syncTolerance._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 146, 2)
    
    syncTolerance = property(__syncTolerance.value, __syncTolerance.set, None, None)

    
    # Attribute syncBehaviorDefault uses Python identifier syncBehaviorDefault
    __syncBehaviorDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncBehaviorDefault'), 'syncBehaviorDefault', '__httpwww_w3_org2001SMIL20Language_animateType_syncBehaviorDefault', _module_typeBindings.syncBehaviorDefaultType, unicode_default='inherit')
    __syncBehaviorDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 157, 2)
    __syncBehaviorDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 157, 2)
    
    syncBehaviorDefault = property(__syncBehaviorDefault.value, __syncBehaviorDefault.set, None, None)

    
    # Attribute syncToleranceDefault uses Python identifier syncToleranceDefault
    __syncToleranceDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncToleranceDefault'), 'syncToleranceDefault', '__httpwww_w3_org2001SMIL20Language_animateType_syncToleranceDefault', pyxb.binding.datatypes.string, unicode_default='inherit')
    __syncToleranceDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 158, 2)
    __syncToleranceDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 158, 2)
    
    syncToleranceDefault = property(__syncToleranceDefault.value, __syncToleranceDefault.set, None, None)

    
    # Attribute restart uses Python identifier restart
    __restart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'restart'), 'restart', '__httpwww_w3_org2001SMIL20Language_animateType_restart', _module_typeBindings.restartTimingType, unicode_default='default')
    __restart._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 169, 2)
    __restart._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 169, 2)
    
    restart = property(__restart.value, __restart.set, None, None)

    
    # Attribute restartDefault uses Python identifier restartDefault
    __restartDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'restartDefault'), 'restartDefault', '__httpwww_w3_org2001SMIL20Language_animateType_restartDefault', _module_typeBindings.restartDefaultType, unicode_default='inherit')
    __restartDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 180, 2)
    __restartDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 180, 2)
    
    restartDefault = property(__restartDefault.value, __restartDefault.set, None, None)

    
    # Attribute fill uses Python identifier fill
    __fill = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fill'), 'fill', '__httpwww_w3_org2001SMIL20Language_animateType_fill', _module_typeBindings.fillTimingAttrsType, unicode_default='default')
    __fill._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 191, 2)
    __fill._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 191, 2)
    
    fill = property(__fill.value, __fill.set, None, None)

    
    # Attribute fillDefault uses Python identifier fillDefault
    __fillDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fillDefault'), 'fillDefault', '__httpwww_w3_org2001SMIL20Language_animateType_fillDefault', _module_typeBindings.fillDefaultType, unicode_default='inherit')
    __fillDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 204, 2)
    __fillDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 204, 2)
    
    fillDefault = property(__fillDefault.value, __fillDefault.set, None, None)

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_w3_org2001SMIL20Language_animateType_begin', pyxb.binding.datatypes.string)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 217, 2)
    __begin._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 217, 2)
    
    begin = property(__begin.value, __begin.set, None, None)

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_w3_org2001SMIL20Language_animateType_end', pyxb.binding.datatypes.string)
    __end._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 218, 2)
    __end._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 218, 2)
    
    end = property(__end.value, __end.set, None, None)

    
    # Attribute dur uses Python identifier dur
    __dur = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dur'), 'dur', '__httpwww_w3_org2001SMIL20Language_animateType_dur', pyxb.binding.datatypes.string)
    __dur._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 221, 2)
    __dur._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 221, 2)
    
    dur = property(__dur.value, __dur.set, None, None)

    
    # Attribute repeatDur uses Python identifier repeatDur
    __repeatDur = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'repeatDur'), 'repeatDur', '__httpwww_w3_org2001SMIL20Language_animateType_repeatDur', pyxb.binding.datatypes.string)
    __repeatDur._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 224, 2)
    __repeatDur._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 224, 2)
    
    repeatDur = property(__repeatDur.value, __repeatDur.set, None, None)

    
    # Attribute repeatCount uses Python identifier repeatCount
    __repeatCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'repeatCount'), 'repeatCount', '__httpwww_w3_org2001SMIL20Language_animateType_repeatCount', _module_typeBindings.nonNegativeDecimalType)
    __repeatCount._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 225, 2)
    __repeatCount._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 225, 2)
    
    repeatCount = property(__repeatCount.value, __repeatCount.set, None, None)

    
    # Attribute repeat uses Python identifier repeat
    __repeat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'repeat'), 'repeat', '__httpwww_w3_org2001SMIL20Language_animateType_repeat', pyxb.binding.datatypes.nonNegativeInteger)
    __repeat._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 228, 2)
    __repeat._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 228, 2)
    
    repeat = property(__repeat.value, __repeat.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__httpwww_w3_org2001SMIL20Language_animateType_min', pyxb.binding.datatypes.string)
    __min._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 231, 2)
    __min._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 231, 2)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__httpwww_w3_org2001SMIL20Language_animateType_max', pyxb.binding.datatypes.string)
    __max._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 232, 2)
    __max._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 232, 2)
    
    max = property(__max.value, __max.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2001SMIL20Language_animateType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 39, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __class.name() : __class,
        __skip_content.name() : __skip_content,
        __alt.name() : __alt,
        __longdesc.name() : __longdesc,
        __targetElement.name() : __targetElement,
        __calcMode.name() : __calcMode,
        __syncBehavior.name() : __syncBehavior,
        __syncTolerance.name() : __syncTolerance,
        __syncBehaviorDefault.name() : __syncBehaviorDefault,
        __syncToleranceDefault.name() : __syncToleranceDefault,
        __restart.name() : __restart,
        __restartDefault.name() : __restartDefault,
        __fill.name() : __fill,
        __fillDefault.name() : __fillDefault,
        __begin.name() : __begin,
        __end.name() : __end,
        __dur.name() : __dur,
        __repeatDur.name() : __repeatDur,
        __repeatCount.name() : __repeatCount,
        __repeat.name() : __repeat,
        __min.name() : __min,
        __max.name() : __max,
        __lang.name() : __lang
    })
_module_typeBindings.animateType = animateType
_Namespace_smil20lang.addCategoryObject('typeBinding', 'animateType', animateType)


# Complex type {http://www.w3.org/2001/SMIL20/Language}animateMotionType with content type ELEMENT_ONLY
class animateMotionType (animateMotionPrototype):
    """Complex type {http://www.w3.org/2001/SMIL20/Language}animateMotionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20lang, 'animateMotionType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 71, 1)
    _ElementMap = animateMotionPrototype._ElementMap.copy()
    _AttributeMap = animateMotionPrototype._AttributeMap.copy()
    # Base type is animateMotionPrototype
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_w3_org2001SMIL20Language_animateMotionType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 37, 2)
    __id._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 37, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__httpwww_w3_org2001SMIL20Language_animateMotionType_class', pyxb.binding.datatypes.string)
    __class._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 38, 2)
    __class._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 38, 2)
    
    class_ = property(__class.value, __class.set, None, None)

    
    # Attribute skip-content uses Python identifier skip_content
    __skip_content = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'skip-content'), 'skip_content', '__httpwww_w3_org2001SMIL20Language_animateMotionType_skip_content', pyxb.binding.datatypes.boolean, unicode_default='true')
    __skip_content._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 45, 2)
    __skip_content._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 45, 2)
    
    skip_content = property(__skip_content.value, __skip_content.set, None, None)

    
    # Attribute alt uses Python identifier alt
    __alt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alt'), 'alt', '__httpwww_w3_org2001SMIL20Language_animateMotionType_alt', pyxb.binding.datatypes.string)
    __alt._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 51, 2)
    __alt._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 51, 2)
    
    alt = property(__alt.value, __alt.set, None, None)

    
    # Attribute longdesc uses Python identifier longdesc
    __longdesc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'longdesc'), 'longdesc', '__httpwww_w3_org2001SMIL20Language_animateMotionType_longdesc', pyxb.binding.datatypes.anyURI)
    __longdesc._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 52, 2)
    __longdesc._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 52, 2)
    
    longdesc = property(__longdesc.value, __longdesc.set, None, None)

    
    # Attribute additive inherited from {http://www.w3.org/2001/SMIL20/}animateMotionPrototype
    
    # Attribute accumulate inherited from {http://www.w3.org/2001/SMIL20/}animateMotionPrototype
    
    # Attribute from_ inherited from {http://www.w3.org/2001/SMIL20/}animateMotionPrototype
    
    # Attribute by inherited from {http://www.w3.org/2001/SMIL20/}animateMotionPrototype
    
    # Attribute values inherited from {http://www.w3.org/2001/SMIL20/}animateMotionPrototype
    
    # Attribute to inherited from {http://www.w3.org/2001/SMIL20/}animateMotionPrototype
    
    # Attribute targetElement uses Python identifier targetElement
    __targetElement = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targetElement'), 'targetElement', '__httpwww_w3_org2001SMIL20Language_animateMotionType_targetElement', pyxb.binding.datatypes.IDREF)
    __targetElement._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 111, 2)
    __targetElement._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 111, 2)
    
    targetElement = property(__targetElement.value, __targetElement.set, None, None)

    
    # Attribute calcMode uses Python identifier calcMode
    __calcMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'calcMode'), 'calcMode', '__httpwww_w3_org2001SMIL20Language_animateMotionType_calcMode', _module_typeBindings.STD_ANON_3, unicode_default='linear')
    __calcMode._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 114, 2)
    __calcMode._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 114, 2)
    
    calcMode = property(__calcMode.value, __calcMode.set, None, None)

    
    # Attribute origin inherited from {http://www.w3.org/2001/SMIL20/}animateMotionPrototype
    
    # Attribute syncBehavior uses Python identifier syncBehavior
    __syncBehavior = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncBehavior'), 'syncBehavior', '__httpwww_w3_org2001SMIL20Language_animateMotionType_syncBehavior', _module_typeBindings.syncBehaviorType, unicode_default='default')
    __syncBehavior._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 145, 2)
    __syncBehavior._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 145, 2)
    
    syncBehavior = property(__syncBehavior.value, __syncBehavior.set, None, None)

    
    # Attribute syncTolerance uses Python identifier syncTolerance
    __syncTolerance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncTolerance'), 'syncTolerance', '__httpwww_w3_org2001SMIL20Language_animateMotionType_syncTolerance', pyxb.binding.datatypes.string)
    __syncTolerance._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 146, 2)
    __syncTolerance._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 146, 2)
    
    syncTolerance = property(__syncTolerance.value, __syncTolerance.set, None, None)

    
    # Attribute syncBehaviorDefault uses Python identifier syncBehaviorDefault
    __syncBehaviorDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncBehaviorDefault'), 'syncBehaviorDefault', '__httpwww_w3_org2001SMIL20Language_animateMotionType_syncBehaviorDefault', _module_typeBindings.syncBehaviorDefaultType, unicode_default='inherit')
    __syncBehaviorDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 157, 2)
    __syncBehaviorDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 157, 2)
    
    syncBehaviorDefault = property(__syncBehaviorDefault.value, __syncBehaviorDefault.set, None, None)

    
    # Attribute syncToleranceDefault uses Python identifier syncToleranceDefault
    __syncToleranceDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncToleranceDefault'), 'syncToleranceDefault', '__httpwww_w3_org2001SMIL20Language_animateMotionType_syncToleranceDefault', pyxb.binding.datatypes.string, unicode_default='inherit')
    __syncToleranceDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 158, 2)
    __syncToleranceDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 158, 2)
    
    syncToleranceDefault = property(__syncToleranceDefault.value, __syncToleranceDefault.set, None, None)

    
    # Attribute restart uses Python identifier restart
    __restart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'restart'), 'restart', '__httpwww_w3_org2001SMIL20Language_animateMotionType_restart', _module_typeBindings.restartTimingType, unicode_default='default')
    __restart._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 169, 2)
    __restart._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 169, 2)
    
    restart = property(__restart.value, __restart.set, None, None)

    
    # Attribute restartDefault uses Python identifier restartDefault
    __restartDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'restartDefault'), 'restartDefault', '__httpwww_w3_org2001SMIL20Language_animateMotionType_restartDefault', _module_typeBindings.restartDefaultType, unicode_default='inherit')
    __restartDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 180, 2)
    __restartDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 180, 2)
    
    restartDefault = property(__restartDefault.value, __restartDefault.set, None, None)

    
    # Attribute fill uses Python identifier fill
    __fill = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fill'), 'fill', '__httpwww_w3_org2001SMIL20Language_animateMotionType_fill', _module_typeBindings.fillTimingAttrsType, unicode_default='default')
    __fill._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 191, 2)
    __fill._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 191, 2)
    
    fill = property(__fill.value, __fill.set, None, None)

    
    # Attribute fillDefault uses Python identifier fillDefault
    __fillDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fillDefault'), 'fillDefault', '__httpwww_w3_org2001SMIL20Language_animateMotionType_fillDefault', _module_typeBindings.fillDefaultType, unicode_default='inherit')
    __fillDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 204, 2)
    __fillDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 204, 2)
    
    fillDefault = property(__fillDefault.value, __fillDefault.set, None, None)

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_w3_org2001SMIL20Language_animateMotionType_begin', pyxb.binding.datatypes.string)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 217, 2)
    __begin._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 217, 2)
    
    begin = property(__begin.value, __begin.set, None, None)

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_w3_org2001SMIL20Language_animateMotionType_end', pyxb.binding.datatypes.string)
    __end._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 218, 2)
    __end._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 218, 2)
    
    end = property(__end.value, __end.set, None, None)

    
    # Attribute dur uses Python identifier dur
    __dur = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dur'), 'dur', '__httpwww_w3_org2001SMIL20Language_animateMotionType_dur', pyxb.binding.datatypes.string)
    __dur._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 221, 2)
    __dur._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 221, 2)
    
    dur = property(__dur.value, __dur.set, None, None)

    
    # Attribute repeatDur uses Python identifier repeatDur
    __repeatDur = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'repeatDur'), 'repeatDur', '__httpwww_w3_org2001SMIL20Language_animateMotionType_repeatDur', pyxb.binding.datatypes.string)
    __repeatDur._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 224, 2)
    __repeatDur._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 224, 2)
    
    repeatDur = property(__repeatDur.value, __repeatDur.set, None, None)

    
    # Attribute repeatCount uses Python identifier repeatCount
    __repeatCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'repeatCount'), 'repeatCount', '__httpwww_w3_org2001SMIL20Language_animateMotionType_repeatCount', _module_typeBindings.nonNegativeDecimalType)
    __repeatCount._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 225, 2)
    __repeatCount._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 225, 2)
    
    repeatCount = property(__repeatCount.value, __repeatCount.set, None, None)

    
    # Attribute repeat uses Python identifier repeat
    __repeat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'repeat'), 'repeat', '__httpwww_w3_org2001SMIL20Language_animateMotionType_repeat', pyxb.binding.datatypes.nonNegativeInteger)
    __repeat._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 228, 2)
    __repeat._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 228, 2)
    
    repeat = property(__repeat.value, __repeat.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__httpwww_w3_org2001SMIL20Language_animateMotionType_min', pyxb.binding.datatypes.string)
    __min._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 231, 2)
    __min._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 231, 2)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__httpwww_w3_org2001SMIL20Language_animateMotionType_max', pyxb.binding.datatypes.string)
    __max._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 232, 2)
    __max._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 232, 2)
    
    max = property(__max.value, __max.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2001SMIL20Language_animateMotionType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 39, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __class.name() : __class,
        __skip_content.name() : __skip_content,
        __alt.name() : __alt,
        __longdesc.name() : __longdesc,
        __targetElement.name() : __targetElement,
        __calcMode.name() : __calcMode,
        __syncBehavior.name() : __syncBehavior,
        __syncTolerance.name() : __syncTolerance,
        __syncBehaviorDefault.name() : __syncBehaviorDefault,
        __syncToleranceDefault.name() : __syncToleranceDefault,
        __restart.name() : __restart,
        __restartDefault.name() : __restartDefault,
        __fill.name() : __fill,
        __fillDefault.name() : __fillDefault,
        __begin.name() : __begin,
        __end.name() : __end,
        __dur.name() : __dur,
        __repeatDur.name() : __repeatDur,
        __repeatCount.name() : __repeatCount,
        __repeat.name() : __repeat,
        __min.name() : __min,
        __max.name() : __max,
        __lang.name() : __lang
    })
_module_typeBindings.animateMotionType = animateMotionType
_Namespace_smil20lang.addCategoryObject('typeBinding', 'animateMotionType', animateMotionType)


# Complex type {http://www.w3.org/2001/SMIL20/Language}animateColorType with content type ELEMENT_ONLY
class animateColorType (animateColorPrototype):
    """Complex type {http://www.w3.org/2001/SMIL20/Language}animateColorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20lang, 'animateColorType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 87, 1)
    _ElementMap = animateColorPrototype._ElementMap.copy()
    _AttributeMap = animateColorPrototype._AttributeMap.copy()
    # Base type is animateColorPrototype
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_w3_org2001SMIL20Language_animateColorType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 37, 2)
    __id._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 37, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__httpwww_w3_org2001SMIL20Language_animateColorType_class', pyxb.binding.datatypes.string)
    __class._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 38, 2)
    __class._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 38, 2)
    
    class_ = property(__class.value, __class.set, None, None)

    
    # Attribute skip-content uses Python identifier skip_content
    __skip_content = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'skip-content'), 'skip_content', '__httpwww_w3_org2001SMIL20Language_animateColorType_skip_content', pyxb.binding.datatypes.boolean, unicode_default='true')
    __skip_content._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 45, 2)
    __skip_content._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 45, 2)
    
    skip_content = property(__skip_content.value, __skip_content.set, None, None)

    
    # Attribute alt uses Python identifier alt
    __alt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alt'), 'alt', '__httpwww_w3_org2001SMIL20Language_animateColorType_alt', pyxb.binding.datatypes.string)
    __alt._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 51, 2)
    __alt._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 51, 2)
    
    alt = property(__alt.value, __alt.set, None, None)

    
    # Attribute longdesc uses Python identifier longdesc
    __longdesc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'longdesc'), 'longdesc', '__httpwww_w3_org2001SMIL20Language_animateColorType_longdesc', pyxb.binding.datatypes.anyURI)
    __longdesc._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 52, 2)
    __longdesc._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 52, 2)
    
    longdesc = property(__longdesc.value, __longdesc.set, None, None)

    
    # Attribute attributeName inherited from {http://www.w3.org/2001/SMIL20/}animateColorPrototype
    
    # Attribute attributeType inherited from {http://www.w3.org/2001/SMIL20/}animateColorPrototype
    
    # Attribute additive inherited from {http://www.w3.org/2001/SMIL20/}animateColorPrototype
    
    # Attribute accumulate inherited from {http://www.w3.org/2001/SMIL20/}animateColorPrototype
    
    # Attribute from_ inherited from {http://www.w3.org/2001/SMIL20/}animateColorPrototype
    
    # Attribute by inherited from {http://www.w3.org/2001/SMIL20/}animateColorPrototype
    
    # Attribute values inherited from {http://www.w3.org/2001/SMIL20/}animateColorPrototype
    
    # Attribute to inherited from {http://www.w3.org/2001/SMIL20/}animateColorPrototype
    
    # Attribute targetElement uses Python identifier targetElement
    __targetElement = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targetElement'), 'targetElement', '__httpwww_w3_org2001SMIL20Language_animateColorType_targetElement', pyxb.binding.datatypes.IDREF)
    __targetElement._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 111, 2)
    __targetElement._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 111, 2)
    
    targetElement = property(__targetElement.value, __targetElement.set, None, None)

    
    # Attribute calcMode uses Python identifier calcMode
    __calcMode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'calcMode'), 'calcMode', '__httpwww_w3_org2001SMIL20Language_animateColorType_calcMode', _module_typeBindings.STD_ANON_3, unicode_default='linear')
    __calcMode._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 114, 2)
    __calcMode._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 114, 2)
    
    calcMode = property(__calcMode.value, __calcMode.set, None, None)

    
    # Attribute syncBehavior uses Python identifier syncBehavior
    __syncBehavior = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncBehavior'), 'syncBehavior', '__httpwww_w3_org2001SMIL20Language_animateColorType_syncBehavior', _module_typeBindings.syncBehaviorType, unicode_default='default')
    __syncBehavior._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 145, 2)
    __syncBehavior._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 145, 2)
    
    syncBehavior = property(__syncBehavior.value, __syncBehavior.set, None, None)

    
    # Attribute syncTolerance uses Python identifier syncTolerance
    __syncTolerance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncTolerance'), 'syncTolerance', '__httpwww_w3_org2001SMIL20Language_animateColorType_syncTolerance', pyxb.binding.datatypes.string)
    __syncTolerance._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 146, 2)
    __syncTolerance._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 146, 2)
    
    syncTolerance = property(__syncTolerance.value, __syncTolerance.set, None, None)

    
    # Attribute syncBehaviorDefault uses Python identifier syncBehaviorDefault
    __syncBehaviorDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncBehaviorDefault'), 'syncBehaviorDefault', '__httpwww_w3_org2001SMIL20Language_animateColorType_syncBehaviorDefault', _module_typeBindings.syncBehaviorDefaultType, unicode_default='inherit')
    __syncBehaviorDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 157, 2)
    __syncBehaviorDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 157, 2)
    
    syncBehaviorDefault = property(__syncBehaviorDefault.value, __syncBehaviorDefault.set, None, None)

    
    # Attribute syncToleranceDefault uses Python identifier syncToleranceDefault
    __syncToleranceDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncToleranceDefault'), 'syncToleranceDefault', '__httpwww_w3_org2001SMIL20Language_animateColorType_syncToleranceDefault', pyxb.binding.datatypes.string, unicode_default='inherit')
    __syncToleranceDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 158, 2)
    __syncToleranceDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 158, 2)
    
    syncToleranceDefault = property(__syncToleranceDefault.value, __syncToleranceDefault.set, None, None)

    
    # Attribute restart uses Python identifier restart
    __restart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'restart'), 'restart', '__httpwww_w3_org2001SMIL20Language_animateColorType_restart', _module_typeBindings.restartTimingType, unicode_default='default')
    __restart._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 169, 2)
    __restart._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 169, 2)
    
    restart = property(__restart.value, __restart.set, None, None)

    
    # Attribute restartDefault uses Python identifier restartDefault
    __restartDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'restartDefault'), 'restartDefault', '__httpwww_w3_org2001SMIL20Language_animateColorType_restartDefault', _module_typeBindings.restartDefaultType, unicode_default='inherit')
    __restartDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 180, 2)
    __restartDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 180, 2)
    
    restartDefault = property(__restartDefault.value, __restartDefault.set, None, None)

    
    # Attribute fill uses Python identifier fill
    __fill = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fill'), 'fill', '__httpwww_w3_org2001SMIL20Language_animateColorType_fill', _module_typeBindings.fillTimingAttrsType, unicode_default='default')
    __fill._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 191, 2)
    __fill._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 191, 2)
    
    fill = property(__fill.value, __fill.set, None, None)

    
    # Attribute fillDefault uses Python identifier fillDefault
    __fillDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fillDefault'), 'fillDefault', '__httpwww_w3_org2001SMIL20Language_animateColorType_fillDefault', _module_typeBindings.fillDefaultType, unicode_default='inherit')
    __fillDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 204, 2)
    __fillDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 204, 2)
    
    fillDefault = property(__fillDefault.value, __fillDefault.set, None, None)

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_w3_org2001SMIL20Language_animateColorType_begin', pyxb.binding.datatypes.string)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 217, 2)
    __begin._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 217, 2)
    
    begin = property(__begin.value, __begin.set, None, None)

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_w3_org2001SMIL20Language_animateColorType_end', pyxb.binding.datatypes.string)
    __end._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 218, 2)
    __end._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 218, 2)
    
    end = property(__end.value, __end.set, None, None)

    
    # Attribute dur uses Python identifier dur
    __dur = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dur'), 'dur', '__httpwww_w3_org2001SMIL20Language_animateColorType_dur', pyxb.binding.datatypes.string)
    __dur._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 221, 2)
    __dur._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 221, 2)
    
    dur = property(__dur.value, __dur.set, None, None)

    
    # Attribute repeatDur uses Python identifier repeatDur
    __repeatDur = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'repeatDur'), 'repeatDur', '__httpwww_w3_org2001SMIL20Language_animateColorType_repeatDur', pyxb.binding.datatypes.string)
    __repeatDur._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 224, 2)
    __repeatDur._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 224, 2)
    
    repeatDur = property(__repeatDur.value, __repeatDur.set, None, None)

    
    # Attribute repeatCount uses Python identifier repeatCount
    __repeatCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'repeatCount'), 'repeatCount', '__httpwww_w3_org2001SMIL20Language_animateColorType_repeatCount', _module_typeBindings.nonNegativeDecimalType)
    __repeatCount._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 225, 2)
    __repeatCount._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 225, 2)
    
    repeatCount = property(__repeatCount.value, __repeatCount.set, None, None)

    
    # Attribute repeat uses Python identifier repeat
    __repeat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'repeat'), 'repeat', '__httpwww_w3_org2001SMIL20Language_animateColorType_repeat', pyxb.binding.datatypes.nonNegativeInteger)
    __repeat._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 228, 2)
    __repeat._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 228, 2)
    
    repeat = property(__repeat.value, __repeat.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__httpwww_w3_org2001SMIL20Language_animateColorType_min', pyxb.binding.datatypes.string)
    __min._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 231, 2)
    __min._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 231, 2)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__httpwww_w3_org2001SMIL20Language_animateColorType_max', pyxb.binding.datatypes.string)
    __max._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 232, 2)
    __max._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 232, 2)
    
    max = property(__max.value, __max.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2001SMIL20Language_animateColorType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 39, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __class.name() : __class,
        __skip_content.name() : __skip_content,
        __alt.name() : __alt,
        __longdesc.name() : __longdesc,
        __targetElement.name() : __targetElement,
        __calcMode.name() : __calcMode,
        __syncBehavior.name() : __syncBehavior,
        __syncTolerance.name() : __syncTolerance,
        __syncBehaviorDefault.name() : __syncBehaviorDefault,
        __syncToleranceDefault.name() : __syncToleranceDefault,
        __restart.name() : __restart,
        __restartDefault.name() : __restartDefault,
        __fill.name() : __fill,
        __fillDefault.name() : __fillDefault,
        __begin.name() : __begin,
        __end.name() : __end,
        __dur.name() : __dur,
        __repeatDur.name() : __repeatDur,
        __repeatCount.name() : __repeatCount,
        __repeat.name() : __repeat,
        __min.name() : __min,
        __max.name() : __max,
        __lang.name() : __lang
    })
_module_typeBindings.animateColorType = animateColorType
_Namespace_smil20lang.addCategoryObject('typeBinding', 'animateColorType', animateColorType)


# Complex type {http://www.w3.org/2001/SMIL20/Language}setType with content type ELEMENT_ONLY
class setType (setPrototype):
    """Complex type {http://www.w3.org/2001/SMIL20/Language}setType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(_Namespace_smil20lang, 'setType')
    _XSDLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 103, 1)
    _ElementMap = setPrototype._ElementMap.copy()
    _AttributeMap = setPrototype._AttributeMap.copy()
    # Base type is setPrototype
    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_w3_org2001SMIL20Language_setType_id', pyxb.binding.datatypes.ID)
    __id._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 37, 2)
    __id._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 37, 2)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute class uses Python identifier class_
    __class = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'class'), 'class_', '__httpwww_w3_org2001SMIL20Language_setType_class', pyxb.binding.datatypes.string)
    __class._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 38, 2)
    __class._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 38, 2)
    
    class_ = property(__class.value, __class.set, None, None)

    
    # Attribute skip-content uses Python identifier skip_content
    __skip_content = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'skip-content'), 'skip_content', '__httpwww_w3_org2001SMIL20Language_setType_skip_content', pyxb.binding.datatypes.boolean, unicode_default='true')
    __skip_content._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 45, 2)
    __skip_content._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 45, 2)
    
    skip_content = property(__skip_content.value, __skip_content.set, None, None)

    
    # Attribute alt uses Python identifier alt
    __alt = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'alt'), 'alt', '__httpwww_w3_org2001SMIL20Language_setType_alt', pyxb.binding.datatypes.string)
    __alt._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 51, 2)
    __alt._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 51, 2)
    
    alt = property(__alt.value, __alt.set, None, None)

    
    # Attribute longdesc uses Python identifier longdesc
    __longdesc = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'longdesc'), 'longdesc', '__httpwww_w3_org2001SMIL20Language_setType_longdesc', pyxb.binding.datatypes.anyURI)
    __longdesc._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 52, 2)
    __longdesc._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 52, 2)
    
    longdesc = property(__longdesc.value, __longdesc.set, None, None)

    
    # Attribute attributeName inherited from {http://www.w3.org/2001/SMIL20/}setPrototype
    
    # Attribute attributeType inherited from {http://www.w3.org/2001/SMIL20/}setPrototype
    
    # Attribute to inherited from {http://www.w3.org/2001/SMIL20/}setPrototype
    
    # Attribute targetElement uses Python identifier targetElement
    __targetElement = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'targetElement'), 'targetElement', '__httpwww_w3_org2001SMIL20Language_setType_targetElement', pyxb.binding.datatypes.IDREF)
    __targetElement._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 111, 2)
    __targetElement._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 111, 2)
    
    targetElement = property(__targetElement.value, __targetElement.set, None, None)

    
    # Attribute syncBehavior uses Python identifier syncBehavior
    __syncBehavior = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncBehavior'), 'syncBehavior', '__httpwww_w3_org2001SMIL20Language_setType_syncBehavior', _module_typeBindings.syncBehaviorType, unicode_default='default')
    __syncBehavior._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 145, 2)
    __syncBehavior._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 145, 2)
    
    syncBehavior = property(__syncBehavior.value, __syncBehavior.set, None, None)

    
    # Attribute syncTolerance uses Python identifier syncTolerance
    __syncTolerance = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncTolerance'), 'syncTolerance', '__httpwww_w3_org2001SMIL20Language_setType_syncTolerance', pyxb.binding.datatypes.string)
    __syncTolerance._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 146, 2)
    __syncTolerance._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 146, 2)
    
    syncTolerance = property(__syncTolerance.value, __syncTolerance.set, None, None)

    
    # Attribute syncBehaviorDefault uses Python identifier syncBehaviorDefault
    __syncBehaviorDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncBehaviorDefault'), 'syncBehaviorDefault', '__httpwww_w3_org2001SMIL20Language_setType_syncBehaviorDefault', _module_typeBindings.syncBehaviorDefaultType, unicode_default='inherit')
    __syncBehaviorDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 157, 2)
    __syncBehaviorDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 157, 2)
    
    syncBehaviorDefault = property(__syncBehaviorDefault.value, __syncBehaviorDefault.set, None, None)

    
    # Attribute syncToleranceDefault uses Python identifier syncToleranceDefault
    __syncToleranceDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'syncToleranceDefault'), 'syncToleranceDefault', '__httpwww_w3_org2001SMIL20Language_setType_syncToleranceDefault', pyxb.binding.datatypes.string, unicode_default='inherit')
    __syncToleranceDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 158, 2)
    __syncToleranceDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 158, 2)
    
    syncToleranceDefault = property(__syncToleranceDefault.value, __syncToleranceDefault.set, None, None)

    
    # Attribute restart uses Python identifier restart
    __restart = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'restart'), 'restart', '__httpwww_w3_org2001SMIL20Language_setType_restart', _module_typeBindings.restartTimingType, unicode_default='default')
    __restart._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 169, 2)
    __restart._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 169, 2)
    
    restart = property(__restart.value, __restart.set, None, None)

    
    # Attribute restartDefault uses Python identifier restartDefault
    __restartDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'restartDefault'), 'restartDefault', '__httpwww_w3_org2001SMIL20Language_setType_restartDefault', _module_typeBindings.restartDefaultType, unicode_default='inherit')
    __restartDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 180, 2)
    __restartDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 180, 2)
    
    restartDefault = property(__restartDefault.value, __restartDefault.set, None, None)

    
    # Attribute fill uses Python identifier fill
    __fill = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fill'), 'fill', '__httpwww_w3_org2001SMIL20Language_setType_fill', _module_typeBindings.fillTimingAttrsType, unicode_default='default')
    __fill._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 191, 2)
    __fill._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 191, 2)
    
    fill = property(__fill.value, __fill.set, None, None)

    
    # Attribute fillDefault uses Python identifier fillDefault
    __fillDefault = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'fillDefault'), 'fillDefault', '__httpwww_w3_org2001SMIL20Language_setType_fillDefault', _module_typeBindings.fillDefaultType, unicode_default='inherit')
    __fillDefault._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 204, 2)
    __fillDefault._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 204, 2)
    
    fillDefault = property(__fillDefault.value, __fillDefault.set, None, None)

    
    # Attribute begin uses Python identifier begin
    __begin = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'begin'), 'begin', '__httpwww_w3_org2001SMIL20Language_setType_begin', pyxb.binding.datatypes.string)
    __begin._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 217, 2)
    __begin._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 217, 2)
    
    begin = property(__begin.value, __begin.set, None, None)

    
    # Attribute end uses Python identifier end
    __end = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'end'), 'end', '__httpwww_w3_org2001SMIL20Language_setType_end', pyxb.binding.datatypes.string)
    __end._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 218, 2)
    __end._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 218, 2)
    
    end = property(__end.value, __end.set, None, None)

    
    # Attribute dur uses Python identifier dur
    __dur = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dur'), 'dur', '__httpwww_w3_org2001SMIL20Language_setType_dur', pyxb.binding.datatypes.string)
    __dur._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 221, 2)
    __dur._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 221, 2)
    
    dur = property(__dur.value, __dur.set, None, None)

    
    # Attribute repeatDur uses Python identifier repeatDur
    __repeatDur = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'repeatDur'), 'repeatDur', '__httpwww_w3_org2001SMIL20Language_setType_repeatDur', pyxb.binding.datatypes.string)
    __repeatDur._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 224, 2)
    __repeatDur._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 224, 2)
    
    repeatDur = property(__repeatDur.value, __repeatDur.set, None, None)

    
    # Attribute repeatCount uses Python identifier repeatCount
    __repeatCount = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'repeatCount'), 'repeatCount', '__httpwww_w3_org2001SMIL20Language_setType_repeatCount', _module_typeBindings.nonNegativeDecimalType)
    __repeatCount._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 225, 2)
    __repeatCount._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 225, 2)
    
    repeatCount = property(__repeatCount.value, __repeatCount.set, None, None)

    
    # Attribute repeat uses Python identifier repeat
    __repeat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'repeat'), 'repeat', '__httpwww_w3_org2001SMIL20Language_setType_repeat', pyxb.binding.datatypes.nonNegativeInteger)
    __repeat._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 228, 2)
    __repeat._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 228, 2)
    
    repeat = property(__repeat.value, __repeat.set, None, None)

    
    # Attribute min uses Python identifier min
    __min = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'min'), 'min', '__httpwww_w3_org2001SMIL20Language_setType_min', pyxb.binding.datatypes.string)
    __min._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 231, 2)
    __min._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 231, 2)
    
    min = property(__min.value, __min.set, None, None)

    
    # Attribute max uses Python identifier max
    __max = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'max'), 'max', '__httpwww_w3_org2001SMIL20Language_setType_max', pyxb.binding.datatypes.string)
    __max._DeclarationLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 232, 2)
    __max._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 232, 2)
    
    max = property(__max.value, __max.set, None, None)

    
    # Attribute {http://www.w3.org/XML/1998/namespace}lang uses Python identifier lang
    __lang = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(pyxb.namespace.XML, 'lang'), 'lang', '__httpwww_w3_org2001SMIL20Language_setType_httpwww_w3_orgXML1998namespacelang', pyxb.binding.xml_.STD_ANON_lang)
    __lang._DeclarationLocation = None
    __lang._UseLocation = pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 39, 2)
    
    lang = property(__lang.value, __lang.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __id.name() : __id,
        __class.name() : __class,
        __skip_content.name() : __skip_content,
        __alt.name() : __alt,
        __longdesc.name() : __longdesc,
        __targetElement.name() : __targetElement,
        __syncBehavior.name() : __syncBehavior,
        __syncTolerance.name() : __syncTolerance,
        __syncBehaviorDefault.name() : __syncBehaviorDefault,
        __syncToleranceDefault.name() : __syncToleranceDefault,
        __restart.name() : __restart,
        __restartDefault.name() : __restartDefault,
        __fill.name() : __fill,
        __fillDefault.name() : __fillDefault,
        __begin.name() : __begin,
        __end.name() : __end,
        __dur.name() : __dur,
        __repeatDur.name() : __repeatDur,
        __repeatCount.name() : __repeatCount,
        __repeat.name() : __repeat,
        __min.name() : __min,
        __max.name() : __max,
        __lang.name() : __lang
    })
_module_typeBindings.setType = setType
_Namespace_smil20lang.addCategoryObject('typeBinding', 'setType', setType)


animate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_smil20, 'animate'), animateType, location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 65, 1))
_Namespace_smil20.addCategoryObject('elementBinding', animate.name().localName(), animate)

animateMotion = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_smil20, 'animateMotion'), animateMotionType, location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 124, 1))
_Namespace_smil20.addCategoryObject('elementBinding', animateMotion.name().localName(), animateMotion)

animateColor = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_smil20, 'animateColor'), animateColorType, location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 130, 1))
_Namespace_smil20.addCategoryObject('elementBinding', animateColor.name().localName(), animateColor)

set_ = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_smil20, 'set'), setType, location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20.xsd', 136, 1))
_Namespace_smil20.addCategoryObject('elementBinding', set_.name().localName(), set_)

animate_ = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_smil20lang, 'animate'), animateType, location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 34, 1))
_Namespace_smil20lang.addCategoryObject('elementBinding', animate_.name().localName(), animate_)

animateMotion_ = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_smil20lang, 'animateMotion'), animateMotionType, location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 70, 1))
_Namespace_smil20lang.addCategoryObject('elementBinding', animateMotion_.name().localName(), animateMotion_)

animateColor_ = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_smil20lang, 'animateColor'), animateColorType, location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 86, 1))
_Namespace_smil20lang.addCategoryObject('elementBinding', animateColor_.name().localName(), animateColor_)

set_2 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_smil20lang, 'set'), setType, location=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 102, 1))
_Namespace_smil20lang.addCategoryObject('elementBinding', set_2.name().localName(), set_2)



def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 38, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2001/SMIL20/Language')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 39, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
animateType._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 74, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2001/SMIL20/Language')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 75, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
animateMotionType._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 90, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2001/SMIL20/Language')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 91, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
animateColorType._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 106, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, 'http://www.w3.org/2001/SMIL20/Language')), pyxb.utils.utility.Location('/home/micha/GIT/pyxb/pyxb/bundles/opengis/schemas/gml/3.1.1/smil/smil20-language.xsd', 107, 5))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
setType._Automaton = _BuildAutomaton_3()


animate._setSubstitutionGroup(animate_)

animateMotion._setSubstitutionGroup(animateMotion_)

animateColor._setSubstitutionGroup(animateColor_)

set_._setSubstitutionGroup(set_2)
