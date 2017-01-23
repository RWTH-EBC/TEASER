# .\boundaryconditions_bind.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:d789d1de16c05aa7dbcf7132bd9fe56c59a877fd
# Generated 2017-01-09 16:21:06.286007 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace http://teaser.boundary

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:3d72c026-d67f-11e6-bbb9-2cd444b2e704')

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
Namespace = pyxb.namespace.NamespaceForURI('http://teaser.boundary', create_if_missing=True)
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


# List simple type: {http://teaser.boundary}integerList
# superclasses pyxb.binding.datatypes.anySimpleType
class integerList (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'integerList')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 86, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.integer
integerList._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'integerList', integerList)
_module_typeBindings.integerList = integerList

# List simple type: {http://teaser.boundary}floatList
# superclasses pyxb.binding.datatypes.anySimpleType
class floatList (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.float."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'floatList')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 89, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.float
floatList._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'floatList', floatList)
_module_typeBindings.floatList = floatList

# Complex type {http://teaser.boundary}UsageOperationTimeType with content type ELEMENT_ONLY
class UsageOperationTimeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.boundary}UsageOperationTimeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UsageOperationTimeType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 5, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.boundary}usage_time uses Python identifier usage_time
    __usage_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usage_time'), 'usage_time', '__httpteaser_boundary_UsageOperationTimeType_httpteaser_boundaryusage_time', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 7, 6), )

    
    usage_time = property(__usage_time.value, __usage_time.set, None, None)

    
    # Element {http://teaser.boundary}daily_usage_hours uses Python identifier daily_usage_hours
    __daily_usage_hours = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'daily_usage_hours'), 'daily_usage_hours', '__httpteaser_boundary_UsageOperationTimeType_httpteaser_boundarydaily_usage_hours', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 8, 6), )

    
    daily_usage_hours = property(__daily_usage_hours.value, __daily_usage_hours.set, None, None)

    
    # Element {http://teaser.boundary}yearly_usage_days uses Python identifier yearly_usage_days
    __yearly_usage_days = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'yearly_usage_days'), 'yearly_usage_days', '__httpteaser_boundary_UsageOperationTimeType_httpteaser_boundaryyearly_usage_days', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 9, 6), )

    
    yearly_usage_days = property(__yearly_usage_days.value, __yearly_usage_days.set, None, None)

    
    # Element {http://teaser.boundary}yearly_usage_hours_day uses Python identifier yearly_usage_hours_day
    __yearly_usage_hours_day = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'yearly_usage_hours_day'), 'yearly_usage_hours_day', '__httpteaser_boundary_UsageOperationTimeType_httpteaser_boundaryyearly_usage_hours_day', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 10, 6), )

    
    yearly_usage_hours_day = property(__yearly_usage_hours_day.value, __yearly_usage_hours_day.set, None, None)

    
    # Element {http://teaser.boundary}yearly_usage_hours_night uses Python identifier yearly_usage_hours_night
    __yearly_usage_hours_night = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'yearly_usage_hours_night'), 'yearly_usage_hours_night', '__httpteaser_boundary_UsageOperationTimeType_httpteaser_boundaryyearly_usage_hours_night', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 11, 6), )

    
    yearly_usage_hours_night = property(__yearly_usage_hours_night.value, __yearly_usage_hours_night.set, None, None)

    
    # Element {http://teaser.boundary}daily_operation_ahu_cooling uses Python identifier daily_operation_ahu_cooling
    __daily_operation_ahu_cooling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'daily_operation_ahu_cooling'), 'daily_operation_ahu_cooling', '__httpteaser_boundary_UsageOperationTimeType_httpteaser_boundarydaily_operation_ahu_cooling', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 12, 6), )

    
    daily_operation_ahu_cooling = property(__daily_operation_ahu_cooling.value, __daily_operation_ahu_cooling.set, None, None)

    
    # Element {http://teaser.boundary}yearly_heating_days uses Python identifier yearly_heating_days
    __yearly_heating_days = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'yearly_heating_days'), 'yearly_heating_days', '__httpteaser_boundary_UsageOperationTimeType_httpteaser_boundaryyearly_heating_days', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 13, 6), )

    
    yearly_heating_days = property(__yearly_heating_days.value, __yearly_heating_days.set, None, None)

    
    # Element {http://teaser.boundary}yearly_ahu_days uses Python identifier yearly_ahu_days
    __yearly_ahu_days = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'yearly_ahu_days'), 'yearly_ahu_days', '__httpteaser_boundary_UsageOperationTimeType_httpteaser_boundaryyearly_ahu_days', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 14, 6), )

    
    yearly_ahu_days = property(__yearly_ahu_days.value, __yearly_ahu_days.set, None, None)

    
    # Element {http://teaser.boundary}yearly_cooling_days uses Python identifier yearly_cooling_days
    __yearly_cooling_days = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'yearly_cooling_days'), 'yearly_cooling_days', '__httpteaser_boundary_UsageOperationTimeType_httpteaser_boundaryyearly_cooling_days', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 15, 6), )

    
    yearly_cooling_days = property(__yearly_cooling_days.value, __yearly_cooling_days.set, None, None)

    
    # Element {http://teaser.boundary}daily_operation_heating uses Python identifier daily_operation_heating
    __daily_operation_heating = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'daily_operation_heating'), 'daily_operation_heating', '__httpteaser_boundary_UsageOperationTimeType_httpteaser_boundarydaily_operation_heating', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 16, 6), )

    
    daily_operation_heating = property(__daily_operation_heating.value, __daily_operation_heating.set, None, None)

    _ElementMap.update({
        __usage_time.name() : __usage_time,
        __daily_usage_hours.name() : __daily_usage_hours,
        __yearly_usage_days.name() : __yearly_usage_days,
        __yearly_usage_hours_day.name() : __yearly_usage_hours_day,
        __yearly_usage_hours_night.name() : __yearly_usage_hours_night,
        __daily_operation_ahu_cooling.name() : __daily_operation_ahu_cooling,
        __yearly_heating_days.name() : __yearly_heating_days,
        __yearly_ahu_days.name() : __yearly_ahu_days,
        __yearly_cooling_days.name() : __yearly_cooling_days,
        __daily_operation_heating.name() : __daily_operation_heating
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.UsageOperationTimeType = UsageOperationTimeType
Namespace.addCategoryObject('typeBinding', 'UsageOperationTimeType', UsageOperationTimeType)


# Complex type {http://teaser.boundary}LightingType with content type ELEMENT_ONLY
class LightingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.boundary}LightingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LightingType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 19, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.boundary}maintained_illuminance uses Python identifier maintained_illuminance
    __maintained_illuminance = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'maintained_illuminance'), 'maintained_illuminance', '__httpteaser_boundary_LightingType_httpteaser_boundarymaintained_illuminance', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 21, 6), )

    
    maintained_illuminance = property(__maintained_illuminance.value, __maintained_illuminance.set, None, None)

    
    # Element {http://teaser.boundary}usage_level_height uses Python identifier usage_level_height
    __usage_level_height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usage_level_height'), 'usage_level_height', '__httpteaser_boundary_LightingType_httpteaser_boundaryusage_level_height', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 22, 6), )

    
    usage_level_height = property(__usage_level_height.value, __usage_level_height.set, None, None)

    
    # Element {http://teaser.boundary}red_factor_visual uses Python identifier red_factor_visual
    __red_factor_visual = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'red_factor_visual'), 'red_factor_visual', '__httpteaser_boundary_LightingType_httpteaser_boundaryred_factor_visual', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 23, 6), )

    
    red_factor_visual = property(__red_factor_visual.value, __red_factor_visual.set, None, None)

    
    # Element {http://teaser.boundary}rel_absence uses Python identifier rel_absence
    __rel_absence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rel_absence'), 'rel_absence', '__httpteaser_boundary_LightingType_httpteaser_boundaryrel_absence', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 24, 6), )

    
    rel_absence = property(__rel_absence.value, __rel_absence.set, None, None)

    
    # Element {http://teaser.boundary}room_index uses Python identifier room_index
    __room_index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'room_index'), 'room_index', '__httpteaser_boundary_LightingType_httpteaser_boundaryroom_index', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 25, 6), )

    
    room_index = property(__room_index.value, __room_index.set, None, None)

    
    # Element {http://teaser.boundary}part_load_factor_lighting uses Python identifier part_load_factor_lighting
    __part_load_factor_lighting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'part_load_factor_lighting'), 'part_load_factor_lighting', '__httpteaser_boundary_LightingType_httpteaser_boundarypart_load_factor_lighting', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 26, 6), )

    
    part_load_factor_lighting = property(__part_load_factor_lighting.value, __part_load_factor_lighting.set, None, None)

    
    # Element {http://teaser.boundary}ratio_conv_rad_lighting uses Python identifier ratio_conv_rad_lighting
    __ratio_conv_rad_lighting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ratio_conv_rad_lighting'), 'ratio_conv_rad_lighting', '__httpteaser_boundary_LightingType_httpteaser_boundaryratio_conv_rad_lighting', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 27, 3), )

    
    ratio_conv_rad_lighting = property(__ratio_conv_rad_lighting.value, __ratio_conv_rad_lighting.set, None, None)

    _ElementMap.update({
        __maintained_illuminance.name() : __maintained_illuminance,
        __usage_level_height.name() : __usage_level_height,
        __red_factor_visual.name() : __red_factor_visual,
        __rel_absence.name() : __rel_absence,
        __room_index.name() : __room_index,
        __part_load_factor_lighting.name() : __part_load_factor_lighting,
        __ratio_conv_rad_lighting.name() : __ratio_conv_rad_lighting
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LightingType = LightingType
Namespace.addCategoryObject('typeBinding', 'LightingType', LightingType)


# Complex type {http://teaser.boundary}RoomClimateType with content type ELEMENT_ONLY
class RoomClimateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.boundary}RoomClimateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoomClimateType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 30, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.boundary}set_temp_heat uses Python identifier set_temp_heat
    __set_temp_heat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'set_temp_heat'), 'set_temp_heat', '__httpteaser_boundary_RoomClimateType_httpteaser_boundaryset_temp_heat', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 32, 6), )

    
    set_temp_heat = property(__set_temp_heat.value, __set_temp_heat.set, None, None)

    
    # Element {http://teaser.boundary}set_temp_cool uses Python identifier set_temp_cool
    __set_temp_cool = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'set_temp_cool'), 'set_temp_cool', '__httpteaser_boundary_RoomClimateType_httpteaser_boundaryset_temp_cool', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 33, 6), )

    
    set_temp_cool = property(__set_temp_cool.value, __set_temp_cool.set, None, None)

    
    # Element {http://teaser.boundary}temp_set_back uses Python identifier temp_set_back
    __temp_set_back = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'temp_set_back'), 'temp_set_back', '__httpteaser_boundary_RoomClimateType_httpteaser_boundarytemp_set_back', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 34, 6), )

    
    temp_set_back = property(__temp_set_back.value, __temp_set_back.set, None, None)

    
    # Element {http://teaser.boundary}min_temp_heat uses Python identifier min_temp_heat
    __min_temp_heat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'min_temp_heat'), 'min_temp_heat', '__httpteaser_boundary_RoomClimateType_httpteaser_boundarymin_temp_heat', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 35, 6), )

    
    min_temp_heat = property(__min_temp_heat.value, __min_temp_heat.set, None, None)

    
    # Element {http://teaser.boundary}max_temp_cool uses Python identifier max_temp_cool
    __max_temp_cool = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'max_temp_cool'), 'max_temp_cool', '__httpteaser_boundary_RoomClimateType_httpteaser_boundarymax_temp_cool', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 36, 6), )

    
    max_temp_cool = property(__max_temp_cool.value, __max_temp_cool.set, None, None)

    
    # Element {http://teaser.boundary}rel_humidity uses Python identifier rel_humidity
    __rel_humidity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rel_humidity'), 'rel_humidity', '__httpteaser_boundary_RoomClimateType_httpteaser_boundaryrel_humidity', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 37, 6), )

    
    rel_humidity = property(__rel_humidity.value, __rel_humidity.set, None, None)

    
    # Element {http://teaser.boundary}cooling_time uses Python identifier cooling_time
    __cooling_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cooling_time'), 'cooling_time', '__httpteaser_boundary_RoomClimateType_httpteaser_boundarycooling_time', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 38, 6), )

    
    cooling_time = property(__cooling_time.value, __cooling_time.set, None, None)

    
    # Element {http://teaser.boundary}heating_time uses Python identifier heating_time
    __heating_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heating_time'), 'heating_time', '__httpteaser_boundary_RoomClimateType_httpteaser_boundaryheating_time', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 39, 6), )

    
    heating_time = property(__heating_time.value, __heating_time.set, None, None)

    
    # Element {http://teaser.boundary}min_air_exchange uses Python identifier min_air_exchange
    __min_air_exchange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'min_air_exchange'), 'min_air_exchange', '__httpteaser_boundary_RoomClimateType_httpteaser_boundarymin_air_exchange', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 40, 6), )

    
    min_air_exchange = property(__min_air_exchange.value, __min_air_exchange.set, None, None)

    
    # Element {http://teaser.boundary}rel_absence_ahu uses Python identifier rel_absence_ahu
    __rel_absence_ahu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'rel_absence_ahu'), 'rel_absence_ahu', '__httpteaser_boundary_RoomClimateType_httpteaser_boundaryrel_absence_ahu', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 41, 6), )

    
    rel_absence_ahu = property(__rel_absence_ahu.value, __rel_absence_ahu.set, None, None)

    
    # Element {http://teaser.boundary}part_load_factor_ahu uses Python identifier part_load_factor_ahu
    __part_load_factor_ahu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'part_load_factor_ahu'), 'part_load_factor_ahu', '__httpteaser_boundary_RoomClimateType_httpteaser_boundarypart_load_factor_ahu', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 42, 6), )

    
    part_load_factor_ahu = property(__part_load_factor_ahu.value, __part_load_factor_ahu.set, None, None)

    _ElementMap.update({
        __set_temp_heat.name() : __set_temp_heat,
        __set_temp_cool.name() : __set_temp_cool,
        __temp_set_back.name() : __temp_set_back,
        __min_temp_heat.name() : __min_temp_heat,
        __max_temp_cool.name() : __max_temp_cool,
        __rel_humidity.name() : __rel_humidity,
        __cooling_time.name() : __cooling_time,
        __heating_time.name() : __heating_time,
        __min_air_exchange.name() : __min_air_exchange,
        __rel_absence_ahu.name() : __rel_absence_ahu,
        __part_load_factor_ahu.name() : __part_load_factor_ahu
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.RoomClimateType = RoomClimateType
Namespace.addCategoryObject('typeBinding', 'RoomClimateType', RoomClimateType)


# Complex type {http://teaser.boundary}InternalGainsType with content type ELEMENT_ONLY
class InternalGainsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.boundary}InternalGainsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InternalGainsType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 45, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.boundary}persons uses Python identifier persons
    __persons = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'persons'), 'persons', '__httpteaser_boundary_InternalGainsType_httpteaser_boundarypersons', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 47, 6), )

    
    persons = property(__persons.value, __persons.set, None, None)

    
    # Element {http://teaser.boundary}profile_persons uses Python identifier profile_persons
    __profile_persons = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'profile_persons'), 'profile_persons', '__httpteaser_boundary_InternalGainsType_httpteaser_boundaryprofile_persons', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 48, 6), )

    
    profile_persons = property(__profile_persons.value, __profile_persons.set, None, None)

    
    # Element {http://teaser.boundary}machines uses Python identifier machines
    __machines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'machines'), 'machines', '__httpteaser_boundary_InternalGainsType_httpteaser_boundarymachines', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 49, 6), )

    
    machines = property(__machines.value, __machines.set, None, None)

    
    # Element {http://teaser.boundary}profile_machines uses Python identifier profile_machines
    __profile_machines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'profile_machines'), 'profile_machines', '__httpteaser_boundary_InternalGainsType_httpteaser_boundaryprofile_machines', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 50, 6), )

    
    profile_machines = property(__profile_machines.value, __profile_machines.set, None, None)

    
    # Element {http://teaser.boundary}lighting_power uses Python identifier lighting_power
    __lighting_power = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'lighting_power'), 'lighting_power', '__httpteaser_boundary_InternalGainsType_httpteaser_boundarylighting_power', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 51, 3), )

    
    lighting_power = property(__lighting_power.value, __lighting_power.set, None, None)

    
    # Element {http://teaser.boundary}profile_lighting uses Python identifier profile_lighting
    __profile_lighting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'profile_lighting'), 'profile_lighting', '__httpteaser_boundary_InternalGainsType_httpteaser_boundaryprofile_lighting', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 52, 3), )

    
    profile_lighting = property(__profile_lighting.value, __profile_lighting.set, None, None)

    _ElementMap.update({
        __persons.name() : __persons,
        __profile_persons.name() : __profile_persons,
        __machines.name() : __machines,
        __profile_machines.name() : __profile_machines,
        __lighting_power.name() : __lighting_power,
        __profile_lighting.name() : __profile_lighting
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.InternalGainsType = InternalGainsType
Namespace.addCategoryObject('typeBinding', 'InternalGainsType', InternalGainsType)


# Complex type {http://teaser.boundary}AHUType with content type ELEMENT_ONLY
class AHUType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.boundary}AHUType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AHUType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 55, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.boundary}min_ahu uses Python identifier min_ahu
    __min_ahu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'min_ahu'), 'min_ahu', '__httpteaser_boundary_AHUType_httpteaser_boundarymin_ahu', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 57, 6), )

    
    min_ahu = property(__min_ahu.value, __min_ahu.set, None, None)

    
    # Element {http://teaser.boundary}max_ahu uses Python identifier max_ahu
    __max_ahu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'max_ahu'), 'max_ahu', '__httpteaser_boundary_AHUType_httpteaser_boundarymax_ahu', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 58, 6), )

    
    max_ahu = property(__max_ahu.value, __max_ahu.set, None, None)

    
    # Element {http://teaser.boundary}with_ahu uses Python identifier with_ahu
    __with_ahu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'with_ahu'), 'with_ahu', '__httpteaser_boundary_AHUType_httpteaser_boundarywith_ahu', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 59, 6), )

    
    with_ahu = property(__with_ahu.value, __with_ahu.set, None, None)

    
    # Element {http://teaser.boundary}use_constant_ach_rate uses Python identifier use_constant_ach_rate
    __use_constant_ach_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'use_constant_ach_rate'), 'use_constant_ach_rate', '__httpteaser_boundary_AHUType_httpteaser_boundaryuse_constant_ach_rate', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 60, 6), )

    
    use_constant_ach_rate = property(__use_constant_ach_rate.value, __use_constant_ach_rate.set, None, None)

    
    # Element {http://teaser.boundary}base_ach uses Python identifier base_ach
    __base_ach = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'base_ach'), 'base_ach', '__httpteaser_boundary_AHUType_httpteaser_boundarybase_ach', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 61, 6), )

    
    base_ach = property(__base_ach.value, __base_ach.set, None, None)

    
    # Element {http://teaser.boundary}max_user_ach uses Python identifier max_user_ach
    __max_user_ach = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'max_user_ach'), 'max_user_ach', '__httpteaser_boundary_AHUType_httpteaser_boundarymax_user_ach', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 62, 6), )

    
    max_user_ach = property(__max_user_ach.value, __max_user_ach.set, None, None)

    
    # Element {http://teaser.boundary}max_overheating_ach uses Python identifier max_overheating_ach
    __max_overheating_ach = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'max_overheating_ach'), 'max_overheating_ach', '__httpteaser_boundary_AHUType_httpteaser_boundarymax_overheating_ach', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 63, 6), )

    
    max_overheating_ach = property(__max_overheating_ach.value, __max_overheating_ach.set, None, None)

    
    # Element {http://teaser.boundary}max_summer_ach uses Python identifier max_summer_ach
    __max_summer_ach = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'max_summer_ach'), 'max_summer_ach', '__httpteaser_boundary_AHUType_httpteaser_boundarymax_summer_ach', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 64, 6), )

    
    max_summer_ach = property(__max_summer_ach.value, __max_summer_ach.set, None, None)

    
    # Element {http://teaser.boundary}winter_reduction uses Python identifier winter_reduction
    __winter_reduction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'winter_reduction'), 'winter_reduction', '__httpteaser_boundary_AHUType_httpteaser_boundarywinter_reduction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 65, 6), )

    
    winter_reduction = property(__winter_reduction.value, __winter_reduction.set, None, None)

    _ElementMap.update({
        __min_ahu.name() : __min_ahu,
        __max_ahu.name() : __max_ahu,
        __with_ahu.name() : __with_ahu,
        __use_constant_ach_rate.name() : __use_constant_ach_rate,
        __base_ach.name() : __base_ach,
        __max_user_ach.name() : __max_user_ach,
        __max_overheating_ach.name() : __max_overheating_ach,
        __max_summer_ach.name() : __max_summer_ach,
        __winter_reduction.name() : __winter_reduction
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.AHUType = AHUType
Namespace.addCategoryObject('typeBinding', 'AHUType', AHUType)


# Complex type {http://teaser.boundary}BoundaryConditionsType with content type ELEMENT_ONLY
class BoundaryConditionsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.boundary}BoundaryConditionsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BoundaryConditionsType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 68, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.boundary}usage uses Python identifier usage
    __usage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'usage'), 'usage', '__httpteaser_boundary_BoundaryConditionsType_httpteaser_boundaryusage', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 70, 6), )

    
    usage = property(__usage.value, __usage.set, None, None)

    
    # Element {http://teaser.boundary}typical_length uses Python identifier typical_length
    __typical_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'typical_length'), 'typical_length', '__httpteaser_boundary_BoundaryConditionsType_httpteaser_boundarytypical_length', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 71, 6), )

    
    typical_length = property(__typical_length.value, __typical_length.set, None, None)

    
    # Element {http://teaser.boundary}typical_width uses Python identifier typical_width
    __typical_width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'typical_width'), 'typical_width', '__httpteaser_boundary_BoundaryConditionsType_httpteaser_boundarytypical_width', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 72, 6), )

    
    typical_width = property(__typical_width.value, __typical_width.set, None, None)

    
    # Element {http://teaser.boundary}UsageOperationTime uses Python identifier UsageOperationTime
    __UsageOperationTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UsageOperationTime'), 'UsageOperationTime', '__httpteaser_boundary_BoundaryConditionsType_httpteaser_boundaryUsageOperationTime', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 73, 6), )

    
    UsageOperationTime = property(__UsageOperationTime.value, __UsageOperationTime.set, None, None)

    
    # Element {http://teaser.boundary}Lighting uses Python identifier Lighting
    __Lighting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Lighting'), 'Lighting', '__httpteaser_boundary_BoundaryConditionsType_httpteaser_boundaryLighting', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 74, 6), )

    
    Lighting = property(__Lighting.value, __Lighting.set, None, None)

    
    # Element {http://teaser.boundary}RoomClimate uses Python identifier RoomClimate
    __RoomClimate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'RoomClimate'), 'RoomClimate', '__httpteaser_boundary_BoundaryConditionsType_httpteaser_boundaryRoomClimate', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 75, 6), )

    
    RoomClimate = property(__RoomClimate.value, __RoomClimate.set, None, None)

    
    # Element {http://teaser.boundary}InternalGains uses Python identifier InternalGains
    __InternalGains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InternalGains'), 'InternalGains', '__httpteaser_boundary_BoundaryConditionsType_httpteaser_boundaryInternalGains', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 76, 6), )

    
    InternalGains = property(__InternalGains.value, __InternalGains.set, None, None)

    
    # Element {http://teaser.boundary}AHU uses Python identifier AHU
    __AHU = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'AHU'), 'AHU', '__httpteaser_boundary_BoundaryConditionsType_httpteaser_boundaryAHU', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 77, 6), )

    
    AHU = property(__AHU.value, __AHU.set, None, None)

    _ElementMap.update({
        __usage.name() : __usage,
        __typical_length.name() : __typical_length,
        __typical_width.name() : __typical_width,
        __UsageOperationTime.name() : __UsageOperationTime,
        __Lighting.name() : __Lighting,
        __RoomClimate.name() : __RoomClimate,
        __InternalGains.name() : __InternalGains,
        __AHU.name() : __AHU
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.BoundaryConditionsType = BoundaryConditionsType
Namespace.addCategoryObject('typeBinding', 'BoundaryConditionsType', BoundaryConditionsType)


# Complex type {http://teaser.boundary}UseConditionsType with content type ELEMENT_ONLY
class UseConditionsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.boundary}UseConditionsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UseConditionsType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 80, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser.boundary}BoundaryConditions uses Python identifier BoundaryConditions
    __BoundaryConditions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BoundaryConditions'), 'BoundaryConditions', '__httpteaser_boundary_UseConditionsType_httpteaser_boundaryBoundaryConditions', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 83, 6), )

    
    BoundaryConditions = property(__BoundaryConditions.value, __BoundaryConditions.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpteaser_boundary_UseConditionsType_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 81, 4)
    __version._UseLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 81, 4)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __BoundaryConditions.name() : __BoundaryConditions
    })
    _AttributeMap.update({
        __version.name() : __version
    })
_module_typeBindings.UseConditionsType = UseConditionsType
Namespace.addCategoryObject('typeBinding', 'UseConditionsType', UseConditionsType)


UseConditions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UseConditions'), UseConditionsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', UseConditions.name().localName(), UseConditions)



UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usage_time'), integerList, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 7, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'daily_usage_hours'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 8, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'yearly_usage_days'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 9, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'yearly_usage_hours_day'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 10, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'yearly_usage_hours_night'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 11, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'daily_operation_ahu_cooling'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 12, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'yearly_heating_days'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 13, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'yearly_ahu_days'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 14, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'yearly_cooling_days'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 15, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'daily_operation_heating'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 16, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 7, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 8, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 9, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 10, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 11, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 12, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 13, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 14, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 15, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 16, 6))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage_time')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 7, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'daily_usage_hours')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 8, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearly_usage_days')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 9, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearly_usage_hours_day')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 10, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearly_usage_hours_night')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 11, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'daily_operation_ahu_cooling')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 12, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearly_heating_days')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 13, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearly_ahu_days')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 14, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'yearly_cooling_days')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 15, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'daily_operation_heating')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 16, 6))
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
UsageOperationTimeType._Automaton = _BuildAutomaton()




LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'maintained_illuminance'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 21, 6)))

LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usage_level_height'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 22, 6)))

LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'red_factor_visual'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 23, 6)))

LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rel_absence'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 24, 6)))

LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'room_index'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 25, 6)))

LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'part_load_factor_lighting'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 26, 6)))

LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ratio_conv_rad_lighting'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 27, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 21, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 22, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 23, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 24, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 25, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 26, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 27, 3))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'maintained_illuminance')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 21, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage_level_height')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 22, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'red_factor_visual')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 23, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rel_absence')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 24, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'room_index')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 25, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'part_load_factor_lighting')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 26, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ratio_conv_rad_lighting')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 27, 3))
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
LightingType._Automaton = _BuildAutomaton_()




RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'set_temp_heat'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 32, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'set_temp_cool'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 33, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'temp_set_back'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 34, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'min_temp_heat'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 35, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'max_temp_cool'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 36, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rel_humidity'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 37, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cooling_time'), integerList, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 38, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heating_time'), integerList, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 39, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'min_air_exchange'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 40, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'rel_absence_ahu'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 41, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'part_load_factor_ahu'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 42, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 32, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 33, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 34, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 35, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 36, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 37, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 38, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 39, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 40, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 41, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 42, 6))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'set_temp_heat')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 32, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'set_temp_cool')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 33, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'temp_set_back')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 34, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'min_temp_heat')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 35, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max_temp_cool')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 36, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rel_humidity')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 37, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'cooling_time')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 38, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heating_time')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 39, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'min_air_exchange')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 40, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'rel_absence_ahu')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 41, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'part_load_factor_ahu')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 42, 6))
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
RoomClimateType._Automaton = _BuildAutomaton_2()




InternalGainsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'persons'), pyxb.binding.datatypes.float, scope=InternalGainsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 47, 6)))

InternalGainsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'profile_persons'), floatList, scope=InternalGainsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 48, 6)))

InternalGainsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'machines'), pyxb.binding.datatypes.float, scope=InternalGainsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 49, 6)))

InternalGainsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'profile_machines'), floatList, scope=InternalGainsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 50, 6)))

InternalGainsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'lighting_power'), pyxb.binding.datatypes.float, scope=InternalGainsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 51, 3)))

InternalGainsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'profile_lighting'), floatList, scope=InternalGainsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 52, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 47, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 48, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 49, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 50, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 51, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 52, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InternalGainsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'persons')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 47, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InternalGainsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'profile_persons')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 48, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(InternalGainsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'machines')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 49, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(InternalGainsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'profile_machines')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 50, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(InternalGainsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'lighting_power')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 51, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(InternalGainsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'profile_lighting')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 52, 3))
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
InternalGainsType._Automaton = _BuildAutomaton_3()




AHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'min_ahu'), pyxb.binding.datatypes.float, scope=AHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 57, 6)))

AHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'max_ahu'), pyxb.binding.datatypes.float, scope=AHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 58, 6)))

AHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'with_ahu'), pyxb.binding.datatypes.boolean, scope=AHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 59, 6)))

AHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'use_constant_ach_rate'), pyxb.binding.datatypes.boolean, scope=AHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 60, 6)))

AHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'base_ach'), pyxb.binding.datatypes.float, scope=AHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 61, 6)))

AHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'max_user_ach'), pyxb.binding.datatypes.float, scope=AHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 62, 6)))

AHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'max_overheating_ach'), floatList, scope=AHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 63, 6)))

AHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'max_summer_ach'), floatList, scope=AHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 64, 6)))

AHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'winter_reduction'), floatList, scope=AHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 65, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 57, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 58, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 59, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 60, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 61, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 62, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 63, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 64, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 65, 6))
    counters.add(cc_8)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AHUType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'min_ahu')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 57, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AHUType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max_ahu')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 58, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AHUType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'with_ahu')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 59, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(AHUType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'use_constant_ach_rate')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 60, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(AHUType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'base_ach')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 61, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(AHUType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max_user_ach')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 62, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(AHUType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max_overheating_ach')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 63, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(AHUType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'max_summer_ach')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 64, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(AHUType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'winter_reduction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 65, 6))
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
AHUType._Automaton = _BuildAutomaton_4()




BoundaryConditionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'usage'), pyxb.binding.datatypes.string, scope=BoundaryConditionsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 70, 6)))

BoundaryConditionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'typical_length'), pyxb.binding.datatypes.float, scope=BoundaryConditionsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 71, 6)))

BoundaryConditionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'typical_width'), pyxb.binding.datatypes.float, scope=BoundaryConditionsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 72, 6)))

BoundaryConditionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UsageOperationTime'), UsageOperationTimeType, scope=BoundaryConditionsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 73, 6)))

BoundaryConditionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Lighting'), LightingType, scope=BoundaryConditionsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 74, 6)))

BoundaryConditionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'RoomClimate'), RoomClimateType, scope=BoundaryConditionsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 75, 6)))

BoundaryConditionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InternalGains'), InternalGainsType, scope=BoundaryConditionsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 76, 6)))

BoundaryConditionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'AHU'), AHUType, scope=BoundaryConditionsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 77, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 70, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 71, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 72, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 73, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 74, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 75, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 76, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 77, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryConditionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'usage')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 70, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryConditionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'typical_length')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 71, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryConditionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'typical_width')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 72, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryConditionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UsageOperationTime')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 73, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryConditionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Lighting')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 74, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryConditionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'RoomClimate')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 75, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryConditionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InternalGains')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 76, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(BoundaryConditionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'AHU')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 77, 6))
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
BoundaryConditionsType._Automaton = _BuildAutomaton_5()




UseConditionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoundaryConditions'), BoundaryConditionsType, scope=UseConditionsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 83, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 83, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UseConditionsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BoundaryConditions')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\BoundaryConditions.xsd', 83, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UseConditionsType._Automaton = _BuildAutomaton_6()

