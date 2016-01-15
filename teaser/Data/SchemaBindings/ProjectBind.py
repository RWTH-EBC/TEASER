# .\ProjectBind.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2016-01-15 12:17:47.544648 by PyXB version 1.2.4 using Python 3.4.3.final.0
# Namespace AbsentNamespace0

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:9b2a9dd0-bb79-11e5-b247-f4b7e2dccf42')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.CreateAbsentNamespace()
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


# List simple type: integerList
# superclasses pyxb.binding.datatypes.anySimpleType
class integerList (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'integerList')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 78, 2)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.integer
integerList._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'integerList', integerList)

# List simple type: floatList
# superclasses pyxb.binding.datatypes.anySimpleType
class floatList (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.float."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'floatList')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 81, 4)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.float
floatList._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'floatList', floatList)

# Complex type UsageOperationTimeType with content type ELEMENT_ONLY
class UsageOperationTimeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type UsageOperationTimeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UsageOperationTimeType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element usage_time uses Python identifier usage_time
    __usage_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'usage_time'), 'usage_time', '__AbsentNamespace0_UsageOperationTimeType_usage_time', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 6, 6), )

    
    usage_time = property(__usage_time.value, __usage_time.set, None, None)

    
    # Element daily_usage_hours uses Python identifier daily_usage_hours
    __daily_usage_hours = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'daily_usage_hours'), 'daily_usage_hours', '__AbsentNamespace0_UsageOperationTimeType_daily_usage_hours', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 7, 6), )

    
    daily_usage_hours = property(__daily_usage_hours.value, __daily_usage_hours.set, None, None)

    
    # Element yearly_usage_days uses Python identifier yearly_usage_days
    __yearly_usage_days = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'yearly_usage_days'), 'yearly_usage_days', '__AbsentNamespace0_UsageOperationTimeType_yearly_usage_days', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 8, 6), )

    
    yearly_usage_days = property(__yearly_usage_days.value, __yearly_usage_days.set, None, None)

    
    # Element yearly_usage_hours_day uses Python identifier yearly_usage_hours_day
    __yearly_usage_hours_day = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'yearly_usage_hours_day'), 'yearly_usage_hours_day', '__AbsentNamespace0_UsageOperationTimeType_yearly_usage_hours_day', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 9, 6), )

    
    yearly_usage_hours_day = property(__yearly_usage_hours_day.value, __yearly_usage_hours_day.set, None, None)

    
    # Element yearly_usage_hours_night uses Python identifier yearly_usage_hours_night
    __yearly_usage_hours_night = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'yearly_usage_hours_night'), 'yearly_usage_hours_night', '__AbsentNamespace0_UsageOperationTimeType_yearly_usage_hours_night', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 10, 6), )

    
    yearly_usage_hours_night = property(__yearly_usage_hours_night.value, __yearly_usage_hours_night.set, None, None)

    
    # Element daily_operation_ahu_cooling uses Python identifier daily_operation_ahu_cooling
    __daily_operation_ahu_cooling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'daily_operation_ahu_cooling'), 'daily_operation_ahu_cooling', '__AbsentNamespace0_UsageOperationTimeType_daily_operation_ahu_cooling', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 11, 6), )

    
    daily_operation_ahu_cooling = property(__daily_operation_ahu_cooling.value, __daily_operation_ahu_cooling.set, None, None)

    
    # Element yearly_heating_days uses Python identifier yearly_heating_days
    __yearly_heating_days = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'yearly_heating_days'), 'yearly_heating_days', '__AbsentNamespace0_UsageOperationTimeType_yearly_heating_days', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 12, 6), )

    
    yearly_heating_days = property(__yearly_heating_days.value, __yearly_heating_days.set, None, None)

    
    # Element yearly_ahu_days uses Python identifier yearly_ahu_days
    __yearly_ahu_days = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'yearly_ahu_days'), 'yearly_ahu_days', '__AbsentNamespace0_UsageOperationTimeType_yearly_ahu_days', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 13, 6), )

    
    yearly_ahu_days = property(__yearly_ahu_days.value, __yearly_ahu_days.set, None, None)

    
    # Element yearly_cooling_days uses Python identifier yearly_cooling_days
    __yearly_cooling_days = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'yearly_cooling_days'), 'yearly_cooling_days', '__AbsentNamespace0_UsageOperationTimeType_yearly_cooling_days', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 14, 6), )

    
    yearly_cooling_days = property(__yearly_cooling_days.value, __yearly_cooling_days.set, None, None)

    
    # Element daily_operation_heating uses Python identifier daily_operation_heating
    __daily_operation_heating = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'daily_operation_heating'), 'daily_operation_heating', '__AbsentNamespace0_UsageOperationTimeType_daily_operation_heating', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 15, 6), )

    
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
Namespace.addCategoryObject('typeBinding', 'UsageOperationTimeType', UsageOperationTimeType)


# Complex type LightingType with content type ELEMENT_ONLY
class LightingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type LightingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LightingType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 18, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element maintained_illuminace uses Python identifier maintained_illuminace
    __maintained_illuminace = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'maintained_illuminace'), 'maintained_illuminace', '__AbsentNamespace0_LightingType_maintained_illuminace', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 20, 6), )

    
    maintained_illuminace = property(__maintained_illuminace.value, __maintained_illuminace.set, None, None)

    
    # Element usage_level_height uses Python identifier usage_level_height
    __usage_level_height = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'usage_level_height'), 'usage_level_height', '__AbsentNamespace0_LightingType_usage_level_height', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 21, 6), )

    
    usage_level_height = property(__usage_level_height.value, __usage_level_height.set, None, None)

    
    # Element red_factor_visual uses Python identifier red_factor_visual
    __red_factor_visual = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'red_factor_visual'), 'red_factor_visual', '__AbsentNamespace0_LightingType_red_factor_visual', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 22, 6), )

    
    red_factor_visual = property(__red_factor_visual.value, __red_factor_visual.set, None, None)

    
    # Element rel_absence uses Python identifier rel_absence
    __rel_absence = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rel_absence'), 'rel_absence', '__AbsentNamespace0_LightingType_rel_absence', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 23, 6), )

    
    rel_absence = property(__rel_absence.value, __rel_absence.set, None, None)

    
    # Element room_index uses Python identifier room_index
    __room_index = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'room_index'), 'room_index', '__AbsentNamespace0_LightingType_room_index', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 24, 6), )

    
    room_index = property(__room_index.value, __room_index.set, None, None)

    
    # Element part_load_factor_lighting uses Python identifier part_load_factor_lighting
    __part_load_factor_lighting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'part_load_factor_lighting'), 'part_load_factor_lighting', '__AbsentNamespace0_LightingType_part_load_factor_lighting', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 25, 6), )

    
    part_load_factor_lighting = property(__part_load_factor_lighting.value, __part_load_factor_lighting.set, None, None)

    
    # Element ratio_conv_rad_lighting uses Python identifier ratio_conv_rad_lighting
    __ratio_conv_rad_lighting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ratio_conv_rad_lighting'), 'ratio_conv_rad_lighting', '__AbsentNamespace0_LightingType_ratio_conv_rad_lighting', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 26, 3), )

    
    ratio_conv_rad_lighting = property(__ratio_conv_rad_lighting.value, __ratio_conv_rad_lighting.set, None, None)

    _ElementMap.update({
        __maintained_illuminace.name() : __maintained_illuminace,
        __usage_level_height.name() : __usage_level_height,
        __red_factor_visual.name() : __red_factor_visual,
        __rel_absence.name() : __rel_absence,
        __room_index.name() : __room_index,
        __part_load_factor_lighting.name() : __part_load_factor_lighting,
        __ratio_conv_rad_lighting.name() : __ratio_conv_rad_lighting
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'LightingType', LightingType)


# Complex type RoomClimateType with content type ELEMENT_ONLY
class RoomClimateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type RoomClimateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RoomClimateType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 29, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element set_temp_heat uses Python identifier set_temp_heat
    __set_temp_heat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'set_temp_heat'), 'set_temp_heat', '__AbsentNamespace0_RoomClimateType_set_temp_heat', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 31, 6), )

    
    set_temp_heat = property(__set_temp_heat.value, __set_temp_heat.set, None, None)

    
    # Element set_temp_cool uses Python identifier set_temp_cool
    __set_temp_cool = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'set_temp_cool'), 'set_temp_cool', '__AbsentNamespace0_RoomClimateType_set_temp_cool', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 32, 6), )

    
    set_temp_cool = property(__set_temp_cool.value, __set_temp_cool.set, None, None)

    
    # Element temp_set_back uses Python identifier temp_set_back
    __temp_set_back = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'temp_set_back'), 'temp_set_back', '__AbsentNamespace0_RoomClimateType_temp_set_back', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 33, 6), )

    
    temp_set_back = property(__temp_set_back.value, __temp_set_back.set, None, None)

    
    # Element min_temp_heat uses Python identifier min_temp_heat
    __min_temp_heat = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_temp_heat'), 'min_temp_heat', '__AbsentNamespace0_RoomClimateType_min_temp_heat', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 34, 6), )

    
    min_temp_heat = property(__min_temp_heat.value, __min_temp_heat.set, None, None)

    
    # Element max_temp_cool uses Python identifier max_temp_cool
    __max_temp_cool = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_temp_cool'), 'max_temp_cool', '__AbsentNamespace0_RoomClimateType_max_temp_cool', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 35, 6), )

    
    max_temp_cool = property(__max_temp_cool.value, __max_temp_cool.set, None, None)

    
    # Element rel_humidity uses Python identifier rel_humidity
    __rel_humidity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rel_humidity'), 'rel_humidity', '__AbsentNamespace0_RoomClimateType_rel_humidity', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 36, 6), )

    
    rel_humidity = property(__rel_humidity.value, __rel_humidity.set, None, None)

    
    # Element cooling_time uses Python identifier cooling_time
    __cooling_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'cooling_time'), 'cooling_time', '__AbsentNamespace0_RoomClimateType_cooling_time', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 37, 6), )

    
    cooling_time = property(__cooling_time.value, __cooling_time.set, None, None)

    
    # Element heating_time uses Python identifier heating_time
    __heating_time = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'heating_time'), 'heating_time', '__AbsentNamespace0_RoomClimateType_heating_time', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 38, 6), )

    
    heating_time = property(__heating_time.value, __heating_time.set, None, None)

    
    # Element min_air_exchange uses Python identifier min_air_exchange
    __min_air_exchange = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_air_exchange'), 'min_air_exchange', '__AbsentNamespace0_RoomClimateType_min_air_exchange', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 39, 6), )

    
    min_air_exchange = property(__min_air_exchange.value, __min_air_exchange.set, None, None)

    
    # Element rel_absence_ahu uses Python identifier rel_absence_ahu
    __rel_absence_ahu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'rel_absence_ahu'), 'rel_absence_ahu', '__AbsentNamespace0_RoomClimateType_rel_absence_ahu', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 40, 6), )

    
    rel_absence_ahu = property(__rel_absence_ahu.value, __rel_absence_ahu.set, None, None)

    
    # Element part_load_factor_ahu uses Python identifier part_load_factor_ahu
    __part_load_factor_ahu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'part_load_factor_ahu'), 'part_load_factor_ahu', '__AbsentNamespace0_RoomClimateType_part_load_factor_ahu', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 41, 6), )

    
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
Namespace.addCategoryObject('typeBinding', 'RoomClimateType', RoomClimateType)


# Complex type InternalGainsType with content type ELEMENT_ONLY
class InternalGainsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type InternalGainsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InternalGainsType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 44, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element persons uses Python identifier persons
    __persons = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'persons'), 'persons', '__AbsentNamespace0_InternalGainsType_persons', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 46, 6), )

    
    persons = property(__persons.value, __persons.set, None, None)

    
    # Element profile_persons uses Python identifier profile_persons
    __profile_persons = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'profile_persons'), 'profile_persons', '__AbsentNamespace0_InternalGainsType_profile_persons', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 47, 6), )

    
    profile_persons = property(__profile_persons.value, __profile_persons.set, None, None)

    
    # Element machines uses Python identifier machines
    __machines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'machines'), 'machines', '__AbsentNamespace0_InternalGainsType_machines', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 48, 6), )

    
    machines = property(__machines.value, __machines.set, None, None)

    
    # Element profile_machines uses Python identifier profile_machines
    __profile_machines = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'profile_machines'), 'profile_machines', '__AbsentNamespace0_InternalGainsType_profile_machines', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 49, 6), )

    
    profile_machines = property(__profile_machines.value, __profile_machines.set, None, None)

    
    # Element lighting_power uses Python identifier lighting_power
    __lighting_power = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'lighting_power'), 'lighting_power', '__AbsentNamespace0_InternalGainsType_lighting_power', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 50, 3), )

    
    lighting_power = property(__lighting_power.value, __lighting_power.set, None, None)

    
    # Element profile_lighting uses Python identifier profile_lighting
    __profile_lighting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'profile_lighting'), 'profile_lighting', '__AbsentNamespace0_InternalGainsType_profile_lighting', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 51, 3), )

    
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
Namespace.addCategoryObject('typeBinding', 'InternalGainsType', InternalGainsType)


# Complex type AHUType with content type ELEMENT_ONLY
class AHUType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type AHUType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AHUType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 54, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element min_ahu uses Python identifier min_ahu
    __min_ahu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'min_ahu'), 'min_ahu', '__AbsentNamespace0_AHUType_min_ahu', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 56, 6), )

    
    min_ahu = property(__min_ahu.value, __min_ahu.set, None, None)

    
    # Element max_ahu uses Python identifier max_ahu
    __max_ahu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'max_ahu'), 'max_ahu', '__AbsentNamespace0_AHUType_max_ahu', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 57, 6), )

    
    max_ahu = property(__max_ahu.value, __max_ahu.set, None, None)

    
    # Element with_ahu uses Python identifier with_ahu
    __with_ahu = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'with_ahu'), 'with_ahu', '__AbsentNamespace0_AHUType_with_ahu', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 58, 6), )

    
    with_ahu = property(__with_ahu.value, __with_ahu.set, None, None)

    _ElementMap.update({
        __min_ahu.name() : __min_ahu,
        __max_ahu.name() : __max_ahu,
        __with_ahu.name() : __with_ahu
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'AHUType', AHUType)


# Complex type UseConditions18599Type with content type ELEMENT_ONLY
class UseConditions18599Type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type UseConditions18599Type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UseConditions18599Type')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 61, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element usage uses Python identifier usage
    __usage = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'usage'), 'usage', '__AbsentNamespace0_UseConditions18599Type_usage', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 63, 6), )

    
    usage = property(__usage.value, __usage.set, None, None)

    
    # Element typical_length uses Python identifier typical_length
    __typical_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'typical_length'), 'typical_length', '__AbsentNamespace0_UseConditions18599Type_typical_length', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 64, 6), )

    
    typical_length = property(__typical_length.value, __typical_length.set, None, None)

    
    # Element typical_width uses Python identifier typical_width
    __typical_width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'typical_width'), 'typical_width', '__AbsentNamespace0_UseConditions18599Type_typical_width', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 65, 6), )

    
    typical_width = property(__typical_width.value, __typical_width.set, None, None)

    
    # Element UsageOperationTime uses Python identifier UsageOperationTime
    __UsageOperationTime = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UsageOperationTime'), 'UsageOperationTime', '__AbsentNamespace0_UseConditions18599Type_UsageOperationTime', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 66, 6), )

    
    UsageOperationTime = property(__UsageOperationTime.value, __UsageOperationTime.set, None, None)

    
    # Element Lighting uses Python identifier Lighting
    __Lighting = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Lighting'), 'Lighting', '__AbsentNamespace0_UseConditions18599Type_Lighting', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 67, 6), )

    
    Lighting = property(__Lighting.value, __Lighting.set, None, None)

    
    # Element RoomClimate uses Python identifier RoomClimate
    __RoomClimate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'RoomClimate'), 'RoomClimate', '__AbsentNamespace0_UseConditions18599Type_RoomClimate', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 68, 6), )

    
    RoomClimate = property(__RoomClimate.value, __RoomClimate.set, None, None)

    
    # Element InternalGains uses Python identifier InternalGains
    __InternalGains = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InternalGains'), 'InternalGains', '__AbsentNamespace0_UseConditions18599Type_InternalGains', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 69, 6), )

    
    InternalGains = property(__InternalGains.value, __InternalGains.set, None, None)

    
    # Element AHU uses Python identifier AHU
    __AHU = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'AHU'), 'AHU', '__AbsentNamespace0_UseConditions18599Type_AHU', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 70, 6), )

    
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
Namespace.addCategoryObject('typeBinding', 'UseConditions18599Type', UseConditions18599Type)


# Complex type UseConditionsType with content type ELEMENT_ONLY
class UseConditionsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type UseConditionsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UseConditionsType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 73, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element UseConditions18599 uses Python identifier UseConditions18599
    __UseConditions18599 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UseConditions18599'), 'UseConditions18599', '__AbsentNamespace0_UseConditionsType_UseConditions18599', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 75, 6), )

    
    UseConditions18599 = property(__UseConditions18599.value, __UseConditions18599.set, None, None)

    _ElementMap.update({
        __UseConditions18599.name() : __UseConditions18599
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'UseConditionsType', UseConditionsType)


# Complex type UseConditionType with content type ELEMENT_ONLY
class UseConditionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type UseConditionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UseConditionType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 5, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element UseConditions18599 uses Python identifier UseConditions18599
    __UseConditions18599 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UseConditions18599'), 'UseConditions18599', '__AbsentNamespace0_UseConditionType_UseConditions18599', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 7, 6), )

    
    UseConditions18599 = property(__UseConditions18599.value, __UseConditions18599.set, None, None)

    _ElementMap.update({
        __UseConditions18599.name() : __UseConditions18599
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'UseConditionType', UseConditionType)


# Complex type MaterialType with content type ELEMENT_ONLY
class MaterialType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type MaterialType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 10, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_MaterialType_name', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 12, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element density uses Python identifier density
    __density = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'density'), 'density', '__AbsentNamespace0_MaterialType_density', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 13, 6), )

    
    density = property(__density.value, __density.set, None, None)

    
    # Element thermal_conduc uses Python identifier thermal_conduc
    __thermal_conduc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'thermal_conduc'), 'thermal_conduc', '__AbsentNamespace0_MaterialType_thermal_conduc', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 14, 6), )

    
    thermal_conduc = property(__thermal_conduc.value, __thermal_conduc.set, None, None)

    
    # Element heat_capac uses Python identifier heat_capac
    __heat_capac = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'heat_capac'), 'heat_capac', '__AbsentNamespace0_MaterialType_heat_capac', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 15, 6), )

    
    heat_capac = property(__heat_capac.value, __heat_capac.set, None, None)

    
    # Element solar_absorp uses Python identifier solar_absorp
    __solar_absorp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'solar_absorp'), 'solar_absorp', '__AbsentNamespace0_MaterialType_solar_absorp', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 16, 6), )

    
    solar_absorp = property(__solar_absorp.value, __solar_absorp.set, None, None)

    
    # Element ir_emissivity uses Python identifier ir_emissivity
    __ir_emissivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ir_emissivity'), 'ir_emissivity', '__AbsentNamespace0_MaterialType_ir_emissivity', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 17, 6), )

    
    ir_emissivity = property(__ir_emissivity.value, __ir_emissivity.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __density.name() : __density,
        __thermal_conduc.name() : __thermal_conduc,
        __heat_capac.name() : __heat_capac,
        __solar_absorp.name() : __solar_absorp,
        __ir_emissivity.name() : __ir_emissivity
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'MaterialType', MaterialType)


# Complex type LayerType with content type ELEMENT_ONLY
class LayerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type LayerType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LayerType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 20, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_LayerType_id', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 22, 6), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element thickness uses Python identifier thickness
    __thickness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'thickness'), 'thickness', '__AbsentNamespace0_LayerType_thickness', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 23, 6), )

    
    thickness = property(__thickness.value, __thickness.set, None, None)

    
    # Element Material uses Python identifier Material
    __Material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Material'), 'Material', '__AbsentNamespace0_LayerType_Material', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 24, 6), )

    
    Material = property(__Material.value, __Material.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __thickness.name() : __thickness,
        __Material.name() : __Material
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'LayerType', LayerType)


# Complex type OuterWallType with content type ELEMENT_ONLY
class OuterWallType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type OuterWallType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OuterWallType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 27, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_OuterWallType_year_of_construction', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 29, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_OuterWallType_construction_type', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 30, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element year_of_retrofit uses Python identifier year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), 'year_of_retrofit', '__AbsentNamespace0_OuterWallType_year_of_retrofit', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 31, 6), )

    
    year_of_retrofit = property(__year_of_retrofit.value, __year_of_retrofit.set, None, None)

    
    # Element area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'area'), 'area', '__AbsentNamespace0_OuterWallType_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 32, 6), )

    
    area = property(__area.value, __area.set, None, None)

    
    # Element tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tilt'), 'tilt', '__AbsentNamespace0_OuterWallType_tilt', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 33, 6), )

    
    tilt = property(__tilt.value, __tilt.set, None, None)

    
    # Element orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orientation'), 'orientation', '__AbsentNamespace0_OuterWallType_orientation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 34, 6), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_OuterWallType_inner_convection', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 35, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_OuterWallType_inner_radiation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 36, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_convection'), 'outer_convection', '__AbsentNamespace0_OuterWallType_outer_convection', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 37, 6), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_radiation'), 'outer_radiation', '__AbsentNamespace0_OuterWallType_outer_radiation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 38, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layer'), 'Layer', '__AbsentNamespace0_OuterWallType_Layer', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 39, 6), )

    
    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __construction_type.name() : __construction_type,
        __year_of_retrofit.name() : __year_of_retrofit,
        __area.name() : __area,
        __tilt.name() : __tilt,
        __orientation.name() : __orientation,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __outer_convection.name() : __outer_convection,
        __outer_radiation.name() : __outer_radiation,
        __Layer.name() : __Layer
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'OuterWallType', OuterWallType)


# Complex type RooftopType with content type ELEMENT_ONLY
class RooftopType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type RooftopType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RooftopType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 42, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_RooftopType_year_of_construction', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 44, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_RooftopType_construction_type', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 45, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element year_of_retrofit uses Python identifier year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), 'year_of_retrofit', '__AbsentNamespace0_RooftopType_year_of_retrofit', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 46, 6), )

    
    year_of_retrofit = property(__year_of_retrofit.value, __year_of_retrofit.set, None, None)

    
    # Element area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'area'), 'area', '__AbsentNamespace0_RooftopType_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 47, 6), )

    
    area = property(__area.value, __area.set, None, None)

    
    # Element tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tilt'), 'tilt', '__AbsentNamespace0_RooftopType_tilt', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 48, 6), )

    
    tilt = property(__tilt.value, __tilt.set, None, None)

    
    # Element orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orientation'), 'orientation', '__AbsentNamespace0_RooftopType_orientation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 49, 6), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_RooftopType_inner_convection', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 50, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_RooftopType_inner_radiation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 51, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_convection'), 'outer_convection', '__AbsentNamespace0_RooftopType_outer_convection', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 52, 6), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_radiation'), 'outer_radiation', '__AbsentNamespace0_RooftopType_outer_radiation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 53, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layer'), 'Layer', '__AbsentNamespace0_RooftopType_Layer', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 54, 6), )

    
    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __construction_type.name() : __construction_type,
        __year_of_retrofit.name() : __year_of_retrofit,
        __area.name() : __area,
        __tilt.name() : __tilt,
        __orientation.name() : __orientation,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __outer_convection.name() : __outer_convection,
        __outer_radiation.name() : __outer_radiation,
        __Layer.name() : __Layer
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RooftopType', RooftopType)


# Complex type InnerWallType with content type ELEMENT_ONLY
class InnerWallType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type InnerWallType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InnerWallType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 57, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_InnerWallType_year_of_construction', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 59, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_InnerWallType_construction_type', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 60, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element year_of_retrofit uses Python identifier year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), 'year_of_retrofit', '__AbsentNamespace0_InnerWallType_year_of_retrofit', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 61, 6), )

    
    year_of_retrofit = property(__year_of_retrofit.value, __year_of_retrofit.set, None, None)

    
    # Element area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'area'), 'area', '__AbsentNamespace0_InnerWallType_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 62, 6), )

    
    area = property(__area.value, __area.set, None, None)

    
    # Element tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tilt'), 'tilt', '__AbsentNamespace0_InnerWallType_tilt', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 63, 6), )

    
    tilt = property(__tilt.value, __tilt.set, None, None)

    
    # Element orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orientation'), 'orientation', '__AbsentNamespace0_InnerWallType_orientation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 64, 6), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_InnerWallType_inner_convection', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 65, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_InnerWallType_inner_radiation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 66, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layer'), 'Layer', '__AbsentNamespace0_InnerWallType_Layer', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 67, 6), )

    
    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __construction_type.name() : __construction_type,
        __year_of_retrofit.name() : __year_of_retrofit,
        __area.name() : __area,
        __tilt.name() : __tilt,
        __orientation.name() : __orientation,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __Layer.name() : __Layer
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'InnerWallType', InnerWallType)


# Complex type CeilingType with content type ELEMENT_ONLY
class CeilingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type CeilingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CeilingType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 70, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_CeilingType_year_of_construction', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 72, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_CeilingType_construction_type', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 73, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element year_of_retrofit uses Python identifier year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), 'year_of_retrofit', '__AbsentNamespace0_CeilingType_year_of_retrofit', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 74, 6), )

    
    year_of_retrofit = property(__year_of_retrofit.value, __year_of_retrofit.set, None, None)

    
    # Element area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'area'), 'area', '__AbsentNamespace0_CeilingType_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 75, 6), )

    
    area = property(__area.value, __area.set, None, None)

    
    # Element tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tilt'), 'tilt', '__AbsentNamespace0_CeilingType_tilt', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 76, 6), )

    
    tilt = property(__tilt.value, __tilt.set, None, None)

    
    # Element orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orientation'), 'orientation', '__AbsentNamespace0_CeilingType_orientation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 77, 6), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_CeilingType_inner_convection', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 78, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_CeilingType_inner_radiation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 79, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layer'), 'Layer', '__AbsentNamespace0_CeilingType_Layer', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 80, 6), )

    
    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __construction_type.name() : __construction_type,
        __year_of_retrofit.name() : __year_of_retrofit,
        __area.name() : __area,
        __tilt.name() : __tilt,
        __orientation.name() : __orientation,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __Layer.name() : __Layer
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'CeilingType', CeilingType)


# Complex type FloorType with content type ELEMENT_ONLY
class FloorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type FloorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FloorType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 83, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_FloorType_year_of_construction', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 85, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_FloorType_construction_type', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 86, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element year_of_retrofit uses Python identifier year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), 'year_of_retrofit', '__AbsentNamespace0_FloorType_year_of_retrofit', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 87, 6), )

    
    year_of_retrofit = property(__year_of_retrofit.value, __year_of_retrofit.set, None, None)

    
    # Element area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'area'), 'area', '__AbsentNamespace0_FloorType_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 88, 6), )

    
    area = property(__area.value, __area.set, None, None)

    
    # Element tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tilt'), 'tilt', '__AbsentNamespace0_FloorType_tilt', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 89, 6), )

    
    tilt = property(__tilt.value, __tilt.set, None, None)

    
    # Element orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orientation'), 'orientation', '__AbsentNamespace0_FloorType_orientation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 90, 6), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_FloorType_inner_convection', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 91, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_FloorType_inner_radiation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 92, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layer'), 'Layer', '__AbsentNamespace0_FloorType_Layer', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 93, 6), )

    
    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __construction_type.name() : __construction_type,
        __year_of_retrofit.name() : __year_of_retrofit,
        __area.name() : __area,
        __tilt.name() : __tilt,
        __orientation.name() : __orientation,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __Layer.name() : __Layer
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'FloorType', FloorType)


# Complex type GroundFloorType with content type ELEMENT_ONLY
class GroundFloorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GroundFloorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroundFloorType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 96, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_GroundFloorType_year_of_construction', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 98, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_GroundFloorType_construction_type', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 99, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element year_of_retrofit uses Python identifier year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), 'year_of_retrofit', '__AbsentNamespace0_GroundFloorType_year_of_retrofit', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 100, 6), )

    
    year_of_retrofit = property(__year_of_retrofit.value, __year_of_retrofit.set, None, None)

    
    # Element area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'area'), 'area', '__AbsentNamespace0_GroundFloorType_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 101, 6), )

    
    area = property(__area.value, __area.set, None, None)

    
    # Element tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tilt'), 'tilt', '__AbsentNamespace0_GroundFloorType_tilt', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 102, 6), )

    
    tilt = property(__tilt.value, __tilt.set, None, None)

    
    # Element orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orientation'), 'orientation', '__AbsentNamespace0_GroundFloorType_orientation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 103, 6), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_GroundFloorType_inner_convection', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 104, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_GroundFloorType_inner_radiation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 105, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layer'), 'Layer', '__AbsentNamespace0_GroundFloorType_Layer', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 106, 6), )

    
    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __construction_type.name() : __construction_type,
        __year_of_retrofit.name() : __year_of_retrofit,
        __area.name() : __area,
        __tilt.name() : __tilt,
        __orientation.name() : __orientation,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __Layer.name() : __Layer
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'GroundFloorType', GroundFloorType)


# Complex type WindowType with content type ELEMENT_ONLY
class WindowType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type WindowType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WindowType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 109, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_WindowType_year_of_construction', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 111, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_WindowType_construction_type', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 112, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element year_of_retrofit uses Python identifier year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), 'year_of_retrofit', '__AbsentNamespace0_WindowType_year_of_retrofit', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 113, 6), )

    
    year_of_retrofit = property(__year_of_retrofit.value, __year_of_retrofit.set, None, None)

    
    # Element area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'area'), 'area', '__AbsentNamespace0_WindowType_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 114, 6), )

    
    area = property(__area.value, __area.set, None, None)

    
    # Element tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'tilt'), 'tilt', '__AbsentNamespace0_WindowType_tilt', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 115, 6), )

    
    tilt = property(__tilt.value, __tilt.set, None, None)

    
    # Element orientation uses Python identifier orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'orientation'), 'orientation', '__AbsentNamespace0_WindowType_orientation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 116, 6), )

    
    orientation = property(__orientation.value, __orientation.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_WindowType_inner_convection', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 117, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_WindowType_inner_radiation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 118, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_convection'), 'outer_convection', '__AbsentNamespace0_WindowType_outer_convection', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 119, 3), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_radiation'), 'outer_radiation', '__AbsentNamespace0_WindowType_outer_radiation', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 120, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element g_value uses Python identifier g_value
    __g_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'g_value'), 'g_value', '__AbsentNamespace0_WindowType_g_value', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 121, 3), )

    
    g_value = property(__g_value.value, __g_value.set, None, None)

    
    # Element a_conv uses Python identifier a_conv
    __a_conv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'a_conv'), 'a_conv', '__AbsentNamespace0_WindowType_a_conv', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 122, 6), )

    
    a_conv = property(__a_conv.value, __a_conv.set, None, None)

    
    # Element shading_g_total uses Python identifier shading_g_total
    __shading_g_total = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shading_g_total'), 'shading_g_total', '__AbsentNamespace0_WindowType_shading_g_total', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 123, 6), )

    
    shading_g_total = property(__shading_g_total.value, __shading_g_total.set, None, None)

    
    # Element shading_max_irr uses Python identifier shading_max_irr
    __shading_max_irr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shading_max_irr'), 'shading_max_irr', '__AbsentNamespace0_WindowType_shading_max_irr', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 124, 6), )

    
    shading_max_irr = property(__shading_max_irr.value, __shading_max_irr.set, None, None)

    
    # Element Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layer'), 'Layer', '__AbsentNamespace0_WindowType_Layer', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 125, 6), )

    
    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __construction_type.name() : __construction_type,
        __year_of_retrofit.name() : __year_of_retrofit,
        __area.name() : __area,
        __tilt.name() : __tilt,
        __orientation.name() : __orientation,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __outer_convection.name() : __outer_convection,
        __outer_radiation.name() : __outer_radiation,
        __g_value.name() : __g_value,
        __a_conv.name() : __a_conv,
        __shading_g_total.name() : __shading_g_total,
        __shading_max_irr.name() : __shading_max_irr,
        __Layer.name() : __Layer
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'WindowType', WindowType)


# Complex type ThermalZoneType with content type ELEMENT_ONLY
class ThermalZoneType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ThermalZoneType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThermalZoneType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 128, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_ThermalZoneType_name', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 130, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'area'), 'area', '__AbsentNamespace0_ThermalZoneType_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 131, 6), )

    
    area = property(__area.value, __area.set, None, None)

    
    # Element volume uses Python identifier volume
    __volume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'volume'), 'volume', '__AbsentNamespace0_ThermalZoneType_volume', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 132, 6), )

    
    volume = property(__volume.value, __volume.set, None, None)

    
    # Element infiltration_rate uses Python identifier infiltration_rate
    __infiltration_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'infiltration_rate'), 'infiltration_rate', '__AbsentNamespace0_ThermalZoneType_infiltration_rate', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 133, 6), )

    
    infiltration_rate = property(__infiltration_rate.value, __infiltration_rate.set, None, None)

    
    # Element typical_length uses Python identifier typical_length
    __typical_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'typical_length'), 'typical_length', '__AbsentNamespace0_ThermalZoneType_typical_length', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 134, 6), )

    
    typical_length = property(__typical_length.value, __typical_length.set, None, None)

    
    # Element typical_width uses Python identifier typical_width
    __typical_width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'typical_width'), 'typical_width', '__AbsentNamespace0_ThermalZoneType_typical_width', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 135, 3), )

    
    typical_width = property(__typical_width.value, __typical_width.set, None, None)

    
    # Element UseCondition uses Python identifier UseCondition
    __UseCondition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'UseCondition'), 'UseCondition', '__AbsentNamespace0_ThermalZoneType_UseCondition', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 136, 6), )

    
    UseCondition = property(__UseCondition.value, __UseCondition.set, None, None)

    
    # Element OuterWall uses Python identifier OuterWall
    __OuterWall = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'OuterWall'), 'OuterWall', '__AbsentNamespace0_ThermalZoneType_OuterWall', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 137, 6), )

    
    OuterWall = property(__OuterWall.value, __OuterWall.set, None, None)

    
    # Element Rooftop uses Python identifier Rooftop
    __Rooftop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Rooftop'), 'Rooftop', '__AbsentNamespace0_ThermalZoneType_Rooftop', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 138, 6), )

    
    Rooftop = property(__Rooftop.value, __Rooftop.set, None, None)

    
    # Element GroundFloor uses Python identifier GroundFloor
    __GroundFloor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'GroundFloor'), 'GroundFloor', '__AbsentNamespace0_ThermalZoneType_GroundFloor', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 139, 6), )

    
    GroundFloor = property(__GroundFloor.value, __GroundFloor.set, None, None)

    
    # Element InnerWall uses Python identifier InnerWall
    __InnerWall = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InnerWall'), 'InnerWall', '__AbsentNamespace0_ThermalZoneType_InnerWall', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 140, 6), )

    
    InnerWall = property(__InnerWall.value, __InnerWall.set, None, None)

    
    # Element Ceiling uses Python identifier Ceiling
    __Ceiling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Ceiling'), 'Ceiling', '__AbsentNamespace0_ThermalZoneType_Ceiling', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 141, 6), )

    
    Ceiling = property(__Ceiling.value, __Ceiling.set, None, None)

    
    # Element Floor uses Python identifier Floor
    __Floor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Floor'), 'Floor', '__AbsentNamespace0_ThermalZoneType_Floor', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 142, 6), )

    
    Floor = property(__Floor.value, __Floor.set, None, None)

    
    # Element Window uses Python identifier Window
    __Window = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Window'), 'Window', '__AbsentNamespace0_ThermalZoneType_Window', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 143, 6), )

    
    Window = property(__Window.value, __Window.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __area.name() : __area,
        __volume.name() : __volume,
        __infiltration_rate.name() : __infiltration_rate,
        __typical_length.name() : __typical_length,
        __typical_width.name() : __typical_width,
        __UseCondition.name() : __UseCondition,
        __OuterWall.name() : __OuterWall,
        __Rooftop.name() : __Rooftop,
        __GroundFloor.name() : __GroundFloor,
        __InnerWall.name() : __InnerWall,
        __Ceiling.name() : __Ceiling,
        __Floor.name() : __Floor,
        __Window.name() : __Window
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ThermalZoneType', ThermalZoneType)


# Complex type BuildingType with content type ELEMENT_ONLY
class BuildingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type BuildingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 146, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_BuildingType_name', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 148, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element street_name uses Python identifier street_name
    __street_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'street_name'), 'street_name', '__AbsentNamespace0_BuildingType_street_name', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 149, 6), )

    
    street_name = property(__street_name.value, __street_name.set, None, None)

    
    # Element city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'city'), 'city', '__AbsentNamespace0_BuildingType_city', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 150, 6), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element type_of_building uses Python identifier type_of_building
    __type_of_building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type_of_building'), 'type_of_building', '__AbsentNamespace0_BuildingType_type_of_building', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 151, 6), )

    
    type_of_building = property(__type_of_building.value, __type_of_building.set, None, None)

    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_BuildingType_year_of_construction', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 152, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element year_of_retrofit uses Python identifier year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), 'year_of_retrofit', '__AbsentNamespace0_BuildingType_year_of_retrofit', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 153, 3), )

    
    year_of_retrofit = property(__year_of_retrofit.value, __year_of_retrofit.set, None, None)

    
    # Element number_of_floors uses Python identifier number_of_floors
    __number_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'number_of_floors'), 'number_of_floors', '__AbsentNamespace0_BuildingType_number_of_floors', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 154, 6), )

    
    number_of_floors = property(__number_of_floors.value, __number_of_floors.set, None, None)

    
    # Element height_of_floors uses Python identifier height_of_floors
    __height_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'height_of_floors'), 'height_of_floors', '__AbsentNamespace0_BuildingType_height_of_floors', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 155, 6), )

    
    height_of_floors = property(__height_of_floors.value, __height_of_floors.set, None, None)

    
    # Element net_leased_area uses Python identifier net_leased_area
    __net_leased_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'net_leased_area'), 'net_leased_area', '__AbsentNamespace0_BuildingType_net_leased_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 156, 6), )

    
    net_leased_area = property(__net_leased_area.value, __net_leased_area.set, None, None)

    
    # Element outer_area uses Python identifier outer_area
    __outer_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_area'), 'outer_area', '__AbsentNamespace0_BuildingType_outer_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 157, 6), )

    
    outer_area = property(__outer_area.value, __outer_area.set, None, None)

    
    # Element window_area uses Python identifier window_area
    __window_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'window_area'), 'window_area', '__AbsentNamespace0_BuildingType_window_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 158, 3), )

    
    window_area = property(__window_area.value, __window_area.set, None, None)

    
    # Element ThermalZone uses Python identifier ThermalZone
    __ThermalZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ThermalZone'), 'ThermalZone', '__AbsentNamespace0_BuildingType_ThermalZone', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 159, 6), )

    
    ThermalZone = property(__ThermalZone.value, __ThermalZone.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __street_name.name() : __street_name,
        __city.name() : __city,
        __type_of_building.name() : __type_of_building,
        __year_of_construction.name() : __year_of_construction,
        __year_of_retrofit.name() : __year_of_retrofit,
        __number_of_floors.name() : __number_of_floors,
        __height_of_floors.name() : __height_of_floors,
        __net_leased_area.name() : __net_leased_area,
        __outer_area.name() : __outer_area,
        __window_area.name() : __window_area,
        __ThermalZone.name() : __ThermalZone
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'BuildingType', BuildingType)


# Complex type OfficeType with content type ELEMENT_ONLY
class OfficeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type OfficeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OfficeType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 162, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_OfficeType_name', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 164, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element street_name uses Python identifier street_name
    __street_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'street_name'), 'street_name', '__AbsentNamespace0_OfficeType_street_name', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 165, 6), )

    
    street_name = property(__street_name.value, __street_name.set, None, None)

    
    # Element city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'city'), 'city', '__AbsentNamespace0_OfficeType_city', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 166, 6), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element type_of_building uses Python identifier type_of_building
    __type_of_building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type_of_building'), 'type_of_building', '__AbsentNamespace0_OfficeType_type_of_building', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 167, 6), )

    
    type_of_building = property(__type_of_building.value, __type_of_building.set, None, None)

    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_OfficeType_year_of_construction', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 168, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element year_of_retrofit uses Python identifier year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), 'year_of_retrofit', '__AbsentNamespace0_OfficeType_year_of_retrofit', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 169, 3), )

    
    year_of_retrofit = property(__year_of_retrofit.value, __year_of_retrofit.set, None, None)

    
    # Element number_of_floors uses Python identifier number_of_floors
    __number_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'number_of_floors'), 'number_of_floors', '__AbsentNamespace0_OfficeType_number_of_floors', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 170, 6), )

    
    number_of_floors = property(__number_of_floors.value, __number_of_floors.set, None, None)

    
    # Element height_of_floors uses Python identifier height_of_floors
    __height_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'height_of_floors'), 'height_of_floors', '__AbsentNamespace0_OfficeType_height_of_floors', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 171, 6), )

    
    height_of_floors = property(__height_of_floors.value, __height_of_floors.set, None, None)

    
    # Element net_leased_area uses Python identifier net_leased_area
    __net_leased_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'net_leased_area'), 'net_leased_area', '__AbsentNamespace0_OfficeType_net_leased_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 172, 6), )

    
    net_leased_area = property(__net_leased_area.value, __net_leased_area.set, None, None)

    
    # Element outer_area uses Python identifier outer_area
    __outer_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_area'), 'outer_area', '__AbsentNamespace0_OfficeType_outer_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 173, 6), )

    
    outer_area = property(__outer_area.value, __outer_area.set, None, None)

    
    # Element window_area uses Python identifier window_area
    __window_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'window_area'), 'window_area', '__AbsentNamespace0_OfficeType_window_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 174, 3), )

    
    window_area = property(__window_area.value, __window_area.set, None, None)

    
    # Element ThermalZone uses Python identifier ThermalZone
    __ThermalZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ThermalZone'), 'ThermalZone', '__AbsentNamespace0_OfficeType_ThermalZone', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 175, 6), )

    
    ThermalZone = property(__ThermalZone.value, __ThermalZone.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __street_name.name() : __street_name,
        __city.name() : __city,
        __type_of_building.name() : __type_of_building,
        __year_of_construction.name() : __year_of_construction,
        __year_of_retrofit.name() : __year_of_retrofit,
        __number_of_floors.name() : __number_of_floors,
        __height_of_floors.name() : __height_of_floors,
        __net_leased_area.name() : __net_leased_area,
        __outer_area.name() : __outer_area,
        __window_area.name() : __window_area,
        __ThermalZone.name() : __ThermalZone
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'OfficeType', OfficeType)


# Complex type ResidentialType with content type ELEMENT_ONLY
class ResidentialType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ResidentialType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResidentialType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 178, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__AbsentNamespace0_ResidentialType_name', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 180, 6), )

    
    name = property(__name.value, __name.set, None, None)

    
    # Element street_name uses Python identifier street_name
    __street_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'street_name'), 'street_name', '__AbsentNamespace0_ResidentialType_street_name', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 181, 6), )

    
    street_name = property(__street_name.value, __street_name.set, None, None)

    
    # Element city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'city'), 'city', '__AbsentNamespace0_ResidentialType_city', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 182, 6), )

    
    city = property(__city.value, __city.set, None, None)

    
    # Element type_of_building uses Python identifier type_of_building
    __type_of_building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'type_of_building'), 'type_of_building', '__AbsentNamespace0_ResidentialType_type_of_building', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 183, 6), )

    
    type_of_building = property(__type_of_building.value, __type_of_building.set, None, None)

    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_ResidentialType_year_of_construction', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 184, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element year_of_retrofit uses Python identifier year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), 'year_of_retrofit', '__AbsentNamespace0_ResidentialType_year_of_retrofit', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 185, 3), )

    
    year_of_retrofit = property(__year_of_retrofit.value, __year_of_retrofit.set, None, None)

    
    # Element number_of_floors uses Python identifier number_of_floors
    __number_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'number_of_floors'), 'number_of_floors', '__AbsentNamespace0_ResidentialType_number_of_floors', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 186, 6), )

    
    number_of_floors = property(__number_of_floors.value, __number_of_floors.set, None, None)

    
    # Element height_of_floors uses Python identifier height_of_floors
    __height_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'height_of_floors'), 'height_of_floors', '__AbsentNamespace0_ResidentialType_height_of_floors', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 187, 6), )

    
    height_of_floors = property(__height_of_floors.value, __height_of_floors.set, None, None)

    
    # Element net_leased_area uses Python identifier net_leased_area
    __net_leased_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'net_leased_area'), 'net_leased_area', '__AbsentNamespace0_ResidentialType_net_leased_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 188, 6), )

    
    net_leased_area = property(__net_leased_area.value, __net_leased_area.set, None, None)

    
    # Element outer_area uses Python identifier outer_area
    __outer_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_area'), 'outer_area', '__AbsentNamespace0_ResidentialType_outer_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 189, 6), )

    
    outer_area = property(__outer_area.value, __outer_area.set, None, None)

    
    # Element window_area uses Python identifier window_area
    __window_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'window_area'), 'window_area', '__AbsentNamespace0_ResidentialType_window_area', False, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 190, 3), )

    
    window_area = property(__window_area.value, __window_area.set, None, None)

    
    # Element ThermalZone uses Python identifier ThermalZone
    __ThermalZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'ThermalZone'), 'ThermalZone', '__AbsentNamespace0_ResidentialType_ThermalZone', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 191, 6), )

    
    ThermalZone = property(__ThermalZone.value, __ThermalZone.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __street_name.name() : __street_name,
        __city.name() : __city,
        __type_of_building.name() : __type_of_building,
        __year_of_construction.name() : __year_of_construction,
        __year_of_retrofit.name() : __year_of_retrofit,
        __number_of_floors.name() : __number_of_floors,
        __height_of_floors.name() : __height_of_floors,
        __net_leased_area.name() : __net_leased_area,
        __outer_area.name() : __outer_area,
        __window_area.name() : __window_area,
        __ThermalZone.name() : __ThermalZone
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ResidentialType', ResidentialType)


# Complex type ProjectType with content type ELEMENT_ONLY
class ProjectType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type ProjectType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProjectType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 194, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element Building uses Python identifier Building
    __Building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Building'), 'Building', '__AbsentNamespace0_ProjectType_Building', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 196, 6), )

    
    Building = property(__Building.value, __Building.set, None, None)

    
    # Element Office uses Python identifier Office
    __Office = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Office'), 'Office', '__AbsentNamespace0_ProjectType_Office', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 197, 3), )

    
    Office = property(__Office.value, __Office.set, None, None)

    
    # Element Residential uses Python identifier Residential
    __Residential = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Residential'), 'Residential', '__AbsentNamespace0_ProjectType_Residential', True, pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 198, 3), )

    
    Residential = property(__Residential.value, __Residential.set, None, None)

    _ElementMap.update({
        __Building.name() : __Building,
        __Office.name() : __Office,
        __Residential.name() : __Residential
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'ProjectType', ProjectType)


UseConditions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UseConditions'), UseConditionsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', UseConditions.name().localName(), UseConditions)

Project = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Project'), ProjectType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', Project.name().localName(), Project)



UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'usage_time'), integerList, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 6, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'daily_usage_hours'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 7, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'yearly_usage_days'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 8, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'yearly_usage_hours_day'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 9, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'yearly_usage_hours_night'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 10, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'daily_operation_ahu_cooling'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 11, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'yearly_heating_days'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 12, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'yearly_ahu_days'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 13, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'yearly_cooling_days'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 14, 6)))

UsageOperationTimeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'daily_operation_heating'), pyxb.binding.datatypes.integer, scope=UsageOperationTimeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 15, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 6, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 7, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 8, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 9, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 10, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 11, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 12, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 13, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 14, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 15, 6))
    counters.add(cc_9)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'usage_time')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 6, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'daily_usage_hours')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 7, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'yearly_usage_days')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 8, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'yearly_usage_hours_day')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 9, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'yearly_usage_hours_night')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 10, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'daily_operation_ahu_cooling')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 11, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'yearly_heating_days')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 12, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'yearly_ahu_days')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 13, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'yearly_cooling_days')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 14, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(UsageOperationTimeType._UseForTag(pyxb.namespace.ExpandedName(None, 'daily_operation_heating')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 15, 6))
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




LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'maintained_illuminace'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 20, 6)))

LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'usage_level_height'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 21, 6)))

LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'red_factor_visual'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 22, 6)))

LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rel_absence'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 23, 6)))

LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'room_index'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 24, 6)))

LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'part_load_factor_lighting'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 25, 6)))

LightingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ratio_conv_rad_lighting'), pyxb.binding.datatypes.float, scope=LightingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 26, 3)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 20, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 21, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 22, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 23, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 24, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 25, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 26, 3))
    counters.add(cc_6)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(None, 'maintained_illuminace')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 20, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(None, 'usage_level_height')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 21, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(None, 'red_factor_visual')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 22, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(None, 'rel_absence')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 23, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(None, 'room_index')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 24, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(None, 'part_load_factor_lighting')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 25, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(LightingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ratio_conv_rad_lighting')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 26, 3))
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




RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'set_temp_heat'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 31, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'set_temp_cool'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 32, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'temp_set_back'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 33, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_temp_heat'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 34, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_temp_cool'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 35, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rel_humidity'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 36, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'cooling_time'), integerList, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 37, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'heating_time'), integerList, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 38, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_air_exchange'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 39, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'rel_absence_ahu'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 40, 6)))

RoomClimateType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'part_load_factor_ahu'), pyxb.binding.datatypes.float, scope=RoomClimateType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 41, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 31, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 33, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 34, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 35, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 36, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 37, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 38, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 39, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 40, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 41, 6))
    counters.add(cc_10)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(None, 'set_temp_heat')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 31, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(None, 'set_temp_cool')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 32, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(None, 'temp_set_back')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 33, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(None, 'min_temp_heat')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 34, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(None, 'max_temp_cool')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 35, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(None, 'rel_humidity')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 36, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(None, 'cooling_time')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 37, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(None, 'heating_time')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 38, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(None, 'min_air_exchange')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 39, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(None, 'rel_absence_ahu')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 40, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(RoomClimateType._UseForTag(pyxb.namespace.ExpandedName(None, 'part_load_factor_ahu')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 41, 6))
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




InternalGainsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'persons'), pyxb.binding.datatypes.float, scope=InternalGainsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 46, 6)))

InternalGainsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'profile_persons'), floatList, scope=InternalGainsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 47, 6)))

InternalGainsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'machines'), pyxb.binding.datatypes.float, scope=InternalGainsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 48, 6)))

InternalGainsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'profile_machines'), floatList, scope=InternalGainsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 49, 6)))

InternalGainsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'lighting_power'), pyxb.binding.datatypes.float, scope=InternalGainsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 50, 3)))

InternalGainsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'profile_lighting'), floatList, scope=InternalGainsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 51, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 46, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 47, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 48, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 49, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 50, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 51, 3))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InternalGainsType._UseForTag(pyxb.namespace.ExpandedName(None, 'persons')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 46, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InternalGainsType._UseForTag(pyxb.namespace.ExpandedName(None, 'profile_persons')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 47, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(InternalGainsType._UseForTag(pyxb.namespace.ExpandedName(None, 'machines')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 48, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(InternalGainsType._UseForTag(pyxb.namespace.ExpandedName(None, 'profile_machines')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 49, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(InternalGainsType._UseForTag(pyxb.namespace.ExpandedName(None, 'lighting_power')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 50, 3))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(InternalGainsType._UseForTag(pyxb.namespace.ExpandedName(None, 'profile_lighting')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 51, 3))
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




AHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'min_ahu'), pyxb.binding.datatypes.float, scope=AHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 56, 6)))

AHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'max_ahu'), pyxb.binding.datatypes.float, scope=AHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 57, 6)))

AHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'with_ahu'), pyxb.binding.datatypes.boolean, scope=AHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 58, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 56, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 57, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 58, 6))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AHUType._UseForTag(pyxb.namespace.ExpandedName(None, 'min_ahu')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 56, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(AHUType._UseForTag(pyxb.namespace.ExpandedName(None, 'max_ahu')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 57, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(AHUType._UseForTag(pyxb.namespace.ExpandedName(None, 'with_ahu')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 58, 6))
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
AHUType._Automaton = _BuildAutomaton_4()




UseConditions18599Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'usage'), pyxb.binding.datatypes.string, scope=UseConditions18599Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 63, 6)))

UseConditions18599Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'typical_length'), pyxb.binding.datatypes.float, scope=UseConditions18599Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 64, 6)))

UseConditions18599Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'typical_width'), pyxb.binding.datatypes.float, scope=UseConditions18599Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 65, 6)))

UseConditions18599Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UsageOperationTime'), UsageOperationTimeType, scope=UseConditions18599Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 66, 6)))

UseConditions18599Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Lighting'), LightingType, scope=UseConditions18599Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 67, 6)))

UseConditions18599Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'RoomClimate'), RoomClimateType, scope=UseConditions18599Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 68, 6)))

UseConditions18599Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InternalGains'), InternalGainsType, scope=UseConditions18599Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 69, 6)))

UseConditions18599Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'AHU'), AHUType, scope=UseConditions18599Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 70, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 63, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 64, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 65, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 66, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 67, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 68, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 69, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 70, 6))
    counters.add(cc_7)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UseConditions18599Type._UseForTag(pyxb.namespace.ExpandedName(None, 'usage')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 63, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(UseConditions18599Type._UseForTag(pyxb.namespace.ExpandedName(None, 'typical_length')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 64, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(UseConditions18599Type._UseForTag(pyxb.namespace.ExpandedName(None, 'typical_width')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 65, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(UseConditions18599Type._UseForTag(pyxb.namespace.ExpandedName(None, 'UsageOperationTime')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 66, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(UseConditions18599Type._UseForTag(pyxb.namespace.ExpandedName(None, 'Lighting')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 67, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(UseConditions18599Type._UseForTag(pyxb.namespace.ExpandedName(None, 'RoomClimate')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 68, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(UseConditions18599Type._UseForTag(pyxb.namespace.ExpandedName(None, 'InternalGains')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 69, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(UseConditions18599Type._UseForTag(pyxb.namespace.ExpandedName(None, 'AHU')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 70, 6))
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
UseConditions18599Type._Automaton = _BuildAutomaton_5()




UseConditionsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UseConditions18599'), UseConditions18599Type, scope=UseConditionsType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 75, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 75, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UseConditionsType._UseForTag(pyxb.namespace.ExpandedName(None, 'UseConditions18599')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\InputData\\XSD_Definitions\\UseConditions18599.xsd', 75, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UseConditionsType._Automaton = _BuildAutomaton_6()




UseConditionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UseConditions18599'), UseConditions18599Type, scope=UseConditionType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 7, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 7, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UseConditionType._UseForTag(pyxb.namespace.ExpandedName(None, 'UseConditions18599')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 7, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
UseConditionType._Automaton = _BuildAutomaton_7()




MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=MaterialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 12, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'density'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 13, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'thermal_conduc'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 14, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'heat_capac'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 15, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'solar_absorp'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 16, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ir_emissivity'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 17, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 12, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'density')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 13, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'thermal_conduc')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 14, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'heat_capac')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 15, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'solar_absorp')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 16, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(None, 'ir_emissivity')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 17, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MaterialType._Automaton = _BuildAutomaton_8()




LayerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'id'), pyxb.binding.datatypes.int, scope=LayerType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 22, 6)))

LayerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'thickness'), pyxb.binding.datatypes.float, scope=LayerType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 23, 6)))

LayerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Material'), MaterialType, scope=LayerType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 24, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LayerType._UseForTag(pyxb.namespace.ExpandedName(None, 'id')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 22, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LayerType._UseForTag(pyxb.namespace.ExpandedName(None, 'thickness')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 23, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LayerType._UseForTag(pyxb.namespace.ExpandedName(None, 'Material')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 24, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LayerType._Automaton = _BuildAutomaton_9()




OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.string, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 29, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 30, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), pyxb.binding.datatypes.string, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 31, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'area'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 32, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tilt'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 33, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orientation'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 34, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 35, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 36, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_convection'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 37, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_radiation'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 38, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layer'), LayerType, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 39, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 29, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 30, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 31, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 32, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 33, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 34, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 35, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 36, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 37, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 38, 6))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 29, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 30, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 31, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 32, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'tilt')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 33, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'orientation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 34, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 35, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 36, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_convection')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 37, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_radiation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 38, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layer')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 39, 6))
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
         ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OuterWallType._Automaton = _BuildAutomaton_10()




RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.string, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 44, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 45, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), pyxb.binding.datatypes.string, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 46, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'area'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 47, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tilt'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 48, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orientation'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 49, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 50, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 51, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_convection'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 52, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_radiation'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 53, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layer'), LayerType, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 54, 6)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 44, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 45, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 46, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 47, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 48, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 49, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 50, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 51, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 52, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 53, 6))
    counters.add(cc_9)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 44, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 45, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 46, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 47, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'tilt')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 48, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'orientation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 49, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 50, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 51, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_convection')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 52, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_radiation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 53, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layer')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 54, 6))
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
         ]))
    st_10._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RooftopType._Automaton = _BuildAutomaton_11()




InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.string, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 59, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 60, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), pyxb.binding.datatypes.string, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 61, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'area'), pyxb.binding.datatypes.float, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 62, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tilt'), pyxb.binding.datatypes.float, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 63, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orientation'), pyxb.binding.datatypes.float, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 64, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 65, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 66, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layer'), LayerType, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 67, 6)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 59, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 60, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 61, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 62, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 63, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 64, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 65, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 66, 6))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 59, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 60, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 61, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 62, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'tilt')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 63, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'orientation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 64, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 65, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 66, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layer')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 67, 6))
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
         ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
InnerWallType._Automaton = _BuildAutomaton_12()




CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.string, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 72, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 73, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), pyxb.binding.datatypes.string, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 74, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'area'), pyxb.binding.datatypes.float, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 75, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tilt'), pyxb.binding.datatypes.float, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 76, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orientation'), pyxb.binding.datatypes.float, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 77, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 78, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 79, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layer'), LayerType, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 80, 6)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 72, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 73, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 74, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 75, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 76, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 77, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 78, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 79, 6))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 72, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 73, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 74, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 75, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'tilt')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 76, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'orientation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 77, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 78, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 79, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layer')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 80, 6))
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
         ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CeilingType._Automaton = _BuildAutomaton_13()




FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.string, scope=FloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 85, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=FloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 86, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), pyxb.binding.datatypes.string, scope=FloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 87, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'area'), pyxb.binding.datatypes.float, scope=FloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 88, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tilt'), pyxb.binding.datatypes.float, scope=FloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 89, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orientation'), pyxb.binding.datatypes.float, scope=FloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 90, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=FloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 91, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=FloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 92, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layer'), LayerType, scope=FloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 93, 6)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 85, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 86, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 87, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 88, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 89, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 90, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 91, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 92, 6))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 85, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 86, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 87, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 88, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'tilt')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 89, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'orientation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 90, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 91, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 92, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layer')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 93, 6))
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
         ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
FloorType._Automaton = _BuildAutomaton_14()




GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.string, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 98, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 99, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), pyxb.binding.datatypes.string, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 100, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'area'), pyxb.binding.datatypes.float, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 101, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tilt'), pyxb.binding.datatypes.float, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 102, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orientation'), pyxb.binding.datatypes.float, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 103, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 104, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 105, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layer'), LayerType, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 106, 6)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 98, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 99, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 100, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 101, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 102, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 103, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 104, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 105, 6))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 98, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 99, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 100, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 101, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'tilt')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 102, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'orientation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 103, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 104, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 105, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layer')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 106, 6))
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
         ]))
    st_8._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
GroundFloorType._Automaton = _BuildAutomaton_15()




WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.string, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 111, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 112, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), pyxb.binding.datatypes.string, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 113, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'area'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 114, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'tilt'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 115, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'orientation'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 116, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 117, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 118, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_convection'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 119, 3)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_radiation'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 120, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'g_value'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 121, 3)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'a_conv'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 122, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shading_g_total'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 123, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shading_max_irr'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 124, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layer'), LayerType, scope=WindowType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 125, 6)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 111, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 112, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 113, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 114, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 115, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 116, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 117, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 118, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 119, 3))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 120, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 121, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 122, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 123, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 124, 6))
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 111, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 112, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 113, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 114, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'tilt')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 115, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'orientation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 116, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 117, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 118, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_convection')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 119, 3))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_radiation')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 120, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'g_value')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 121, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'a_conv')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 122, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'shading_g_total')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 123, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'shading_max_irr')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 124, 6))
    st_13 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layer')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 125, 6))
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
         ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WindowType._Automaton = _BuildAutomaton_16()




ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 130, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'area'), pyxb.binding.datatypes.float, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 131, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'volume'), pyxb.binding.datatypes.float, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 132, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'infiltration_rate'), pyxb.binding.datatypes.float, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 133, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'typical_length'), pyxb.binding.datatypes.float, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 134, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'typical_width'), pyxb.binding.datatypes.float, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 135, 3)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'UseCondition'), UseConditionType, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 136, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'OuterWall'), OuterWallType, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 137, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Rooftop'), RooftopType, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 138, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'GroundFloor'), GroundFloorType, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 139, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InnerWall'), InnerWallType, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 140, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Ceiling'), CeilingType, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 141, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Floor'), FloorType, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 142, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Window'), WindowType, scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 143, 6)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 130, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 131, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 132, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 133, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 134, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 135, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 136, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 137, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 138, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 139, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 140, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 141, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 142, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 143, 6))
    counters.add(cc_13)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 130, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 131, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'volume')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 132, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'infiltration_rate')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 133, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'typical_length')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 134, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'typical_width')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 135, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'UseCondition')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 136, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'OuterWall')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 137, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'Rooftop')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 138, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'GroundFloor')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 139, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'InnerWall')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 140, 6))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'Ceiling')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 141, 6))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'Floor')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 142, 6))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(None, 'Window')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 143, 6))
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
ThermalZoneType._Automaton = _BuildAutomaton_17()




BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=BuildingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 148, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'street_name'), pyxb.binding.datatypes.string, scope=BuildingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 149, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'city'), pyxb.binding.datatypes.string, scope=BuildingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 150, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type_of_building'), pyxb.binding.datatypes.string, scope=BuildingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 151, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.string, scope=BuildingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 152, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), pyxb.binding.datatypes.string, scope=BuildingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 153, 3)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'number_of_floors'), pyxb.binding.datatypes.int, scope=BuildingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 154, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'height_of_floors'), pyxb.binding.datatypes.float, scope=BuildingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 155, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'net_leased_area'), pyxb.binding.datatypes.float, scope=BuildingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 156, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_area'), pyxb.binding.datatypes.float, scope=BuildingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 157, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'window_area'), pyxb.binding.datatypes.float, scope=BuildingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 158, 3)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ThermalZone'), ThermalZoneType, scope=BuildingType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 159, 6)))

def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 148, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 149, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 150, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 151, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 152, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 153, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 154, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 155, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 156, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 157, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 158, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 159, 6))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 148, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'street_name')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 149, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'city')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 150, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'type_of_building')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 151, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 152, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 153, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'number_of_floors')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 154, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'height_of_floors')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 155, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'net_leased_area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 156, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 157, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'window_area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 158, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(None, 'ThermalZone')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 159, 6))
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
BuildingType._Automaton = _BuildAutomaton_18()




OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=OfficeType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 164, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'street_name'), pyxb.binding.datatypes.string, scope=OfficeType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 165, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'city'), pyxb.binding.datatypes.string, scope=OfficeType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 166, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type_of_building'), pyxb.binding.datatypes.string, scope=OfficeType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 167, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.string, scope=OfficeType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 168, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), pyxb.binding.datatypes.string, scope=OfficeType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 169, 3)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'number_of_floors'), pyxb.binding.datatypes.int, scope=OfficeType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 170, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'height_of_floors'), pyxb.binding.datatypes.float, scope=OfficeType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 171, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'net_leased_area'), pyxb.binding.datatypes.float, scope=OfficeType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 172, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_area'), pyxb.binding.datatypes.float, scope=OfficeType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 173, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'window_area'), pyxb.binding.datatypes.float, scope=OfficeType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 174, 3)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ThermalZone'), ThermalZoneType, scope=OfficeType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 175, 6)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 164, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 165, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 166, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 167, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 168, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 169, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 170, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 171, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 172, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 173, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 174, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 175, 6))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 164, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(None, 'street_name')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 165, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(None, 'city')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 166, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(None, 'type_of_building')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 167, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 168, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 169, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(None, 'number_of_floors')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 170, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(None, 'height_of_floors')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 171, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(None, 'net_leased_area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 172, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 173, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(None, 'window_area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 174, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(None, 'ThermalZone')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 175, 6))
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
OfficeType._Automaton = _BuildAutomaton_19()




ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'name'), pyxb.binding.datatypes.string, scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 180, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'street_name'), pyxb.binding.datatypes.string, scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 181, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'city'), pyxb.binding.datatypes.string, scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 182, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'type_of_building'), pyxb.binding.datatypes.string, scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 183, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.string, scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 184, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_retrofit'), pyxb.binding.datatypes.string, scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 185, 3)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'number_of_floors'), pyxb.binding.datatypes.int, scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 186, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'height_of_floors'), pyxb.binding.datatypes.float, scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 187, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'net_leased_area'), pyxb.binding.datatypes.float, scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 188, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_area'), pyxb.binding.datatypes.float, scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 189, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'window_area'), pyxb.binding.datatypes.float, scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 190, 3)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'ThermalZone'), ThermalZoneType, scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 191, 6)))

def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 180, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 181, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 182, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 183, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 184, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 185, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 186, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 187, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 188, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 189, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 190, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 191, 6))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(None, 'name')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 180, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(None, 'street_name')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 181, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(None, 'city')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 182, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(None, 'type_of_building')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 183, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 184, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 185, 3))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(None, 'number_of_floors')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 186, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(None, 'height_of_floors')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 187, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(None, 'net_leased_area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 188, 6))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 189, 6))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(None, 'window_area')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 190, 3))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(None, 'ThermalZone')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 191, 6))
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
ResidentialType._Automaton = _BuildAutomaton_20()




ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Building'), BuildingType, scope=ProjectType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 196, 6)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Office'), OfficeType, scope=ProjectType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 197, 3)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Residential'), ResidentialType, scope=ProjectType, location=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 198, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 195, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'Building')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 196, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'Office')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 197, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(None, 'Residential')), pyxb.utils.utility.Location('D:\\PyXB-1.2.4\\scripts\\Project.xsd', 198, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ProjectType._Automaton = _BuildAutomaton_21()

