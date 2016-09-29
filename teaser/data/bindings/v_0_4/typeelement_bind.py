# .\typeelement_bind.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:e92452c8d3e28a9e27abfc9994d2007779e7f4c9
# Generated 2016-09-26 09:34:06.704842 by PyXB version 1.2.4 using Python 3.5.2.final.0
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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:9b1db966-83bb-11e6-8801-2cd444b2e704')

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
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 116, 2)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.integer
integerList._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'integerList', integerList)

# Complex type layerType with content type ELEMENT_ONLY
class layerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type layerType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'layerType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 4, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__AbsentNamespace0_layerType_id', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 6, 6), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element thickness uses Python identifier thickness
    __thickness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'thickness'), 'thickness', '__AbsentNamespace0_layerType_thickness', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 7, 6), )

    
    thickness = property(__thickness.value, __thickness.set, None, None)

    
    # Element material uses Python identifier material
    __material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'material'), 'material', '__AbsentNamespace0_layerType_material', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 8, 6), )

    
    material = property(__material.value, __material.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __thickness.name() : __thickness,
        __material.name() : __material
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'layerType', layerType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 9, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute material_id uses Python identifier material_id
    __material_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'material_id'), 'material_id', '__AbsentNamespace0_CTD_ANON_material_id', pyxb.binding.datatypes.string)
    __material_id._DeclarationLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 12, 5)
    __material_id._UseLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 12, 5)
    
    material_id = property(__material_id.value, __material_id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __material_id.name() : __material_id
    })



# Complex type LayersType with content type ELEMENT_ONLY
class LayersType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type LayersType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LayersType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 19, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element layer uses Python identifier layer
    __layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'layer'), 'layer', '__AbsentNamespace0_LayersType_layer', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 21, 6), )

    
    layer = property(__layer.value, __layer.set, None, None)

    _ElementMap.update({
        __layer.name() : __layer
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'LayersType', LayersType)


# Complex type OuterWallType with content type ELEMENT_ONLY
class OuterWallType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type OuterWallType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OuterWallType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 24, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_OuterWallType_year_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 26, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'building_age_group'), 'building_age_group', '__AbsentNamespace0_OuterWallType_building_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 27, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_OuterWallType_construction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 28, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_OuterWallType_inner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 29, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_OuterWallType_inner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 30, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_convection'), 'outer_convection', '__AbsentNamespace0_OuterWallType_outer_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 31, 6), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_radiation'), 'outer_radiation', '__AbsentNamespace0_OuterWallType_outer_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 32, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layers'), 'Layers', '__AbsentNamespace0_OuterWallType_Layers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 33, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __outer_convection.name() : __outer_convection,
        __outer_radiation.name() : __outer_radiation,
        __Layers.name() : __Layers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'OuterWallType', OuterWallType)


# Complex type InnerWallType with content type ELEMENT_ONLY
class InnerWallType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type InnerWallType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InnerWallType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 36, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_InnerWallType_year_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 38, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'building_age_group'), 'building_age_group', '__AbsentNamespace0_InnerWallType_building_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 39, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_InnerWallType_construction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 40, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_InnerWallType_inner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 41, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_InnerWallType_inner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 42, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layers'), 'Layers', '__AbsentNamespace0_InnerWallType_Layers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 43, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __Layers.name() : __Layers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'InnerWallType', InnerWallType)


# Complex type RooftopType with content type ELEMENT_ONLY
class RooftopType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type RooftopType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RooftopType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 46, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_RooftopType_year_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 48, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'building_age_group'), 'building_age_group', '__AbsentNamespace0_RooftopType_building_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 49, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_RooftopType_construction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 50, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_RooftopType_inner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 51, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_RooftopType_inner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 52, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_convection'), 'outer_convection', '__AbsentNamespace0_RooftopType_outer_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 53, 6), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_radiation'), 'outer_radiation', '__AbsentNamespace0_RooftopType_outer_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 54, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layers'), 'Layers', '__AbsentNamespace0_RooftopType_Layers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 55, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __outer_convection.name() : __outer_convection,
        __outer_radiation.name() : __outer_radiation,
        __Layers.name() : __Layers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'RooftopType', RooftopType)


# Complex type GroundFloorType with content type ELEMENT_ONLY
class GroundFloorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type GroundFloorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroundFloorType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 58, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_GroundFloorType_year_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 60, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'building_age_group'), 'building_age_group', '__AbsentNamespace0_GroundFloorType_building_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 61, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_GroundFloorType_construction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 62, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_GroundFloorType_inner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 63, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_GroundFloorType_inner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 64, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layers'), 'Layers', '__AbsentNamespace0_GroundFloorType_Layers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 65, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __Layers.name() : __Layers
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
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 68, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_WindowType_year_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 70, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'building_age_group'), 'building_age_group', '__AbsentNamespace0_WindowType_building_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 71, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_WindowType_construction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 72, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_WindowType_inner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 73, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_WindowType_inner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 74, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_convection'), 'outer_convection', '__AbsentNamespace0_WindowType_outer_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 75, 6), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'outer_radiation'), 'outer_radiation', '__AbsentNamespace0_WindowType_outer_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 76, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element g_value uses Python identifier g_value
    __g_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'g_value'), 'g_value', '__AbsentNamespace0_WindowType_g_value', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 77, 6), )

    
    g_value = property(__g_value.value, __g_value.set, None, None)

    
    # Element a_conv uses Python identifier a_conv
    __a_conv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'a_conv'), 'a_conv', '__AbsentNamespace0_WindowType_a_conv', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 78, 6), )

    
    a_conv = property(__a_conv.value, __a_conv.set, None, None)

    
    # Element shading_g_total uses Python identifier shading_g_total
    __shading_g_total = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shading_g_total'), 'shading_g_total', '__AbsentNamespace0_WindowType_shading_g_total', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 79, 6), )

    
    shading_g_total = property(__shading_g_total.value, __shading_g_total.set, None, None)

    
    # Element shading_max_irr uses Python identifier shading_max_irr
    __shading_max_irr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'shading_max_irr'), 'shading_max_irr', '__AbsentNamespace0_WindowType_shading_max_irr', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 80, 6), )

    
    shading_max_irr = property(__shading_max_irr.value, __shading_max_irr.set, None, None)

    
    # Element Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layers'), 'Layers', '__AbsentNamespace0_WindowType_Layers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 81, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __outer_convection.name() : __outer_convection,
        __outer_radiation.name() : __outer_radiation,
        __g_value.name() : __g_value,
        __a_conv.name() : __a_conv,
        __shading_g_total.name() : __shading_g_total,
        __shading_max_irr.name() : __shading_max_irr,
        __Layers.name() : __Layers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'WindowType', WindowType)


# Complex type CeilingType with content type ELEMENT_ONLY
class CeilingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type CeilingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CeilingType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 84, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_CeilingType_year_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 86, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'building_age_group'), 'building_age_group', '__AbsentNamespace0_CeilingType_building_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 87, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_CeilingType_construction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 88, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_CeilingType_inner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 89, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_CeilingType_inner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 90, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layers'), 'Layers', '__AbsentNamespace0_CeilingType_Layers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 91, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __Layers.name() : __Layers
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
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 94, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'year_of_construction'), 'year_of_construction', '__AbsentNamespace0_FloorType_year_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 96, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'building_age_group'), 'building_age_group', '__AbsentNamespace0_FloorType_building_age_group', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 97, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'construction_type'), 'construction_type', '__AbsentNamespace0_FloorType_construction_type', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 98, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_convection'), 'inner_convection', '__AbsentNamespace0_FloorType_inner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 99, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'inner_radiation'), 'inner_radiation', '__AbsentNamespace0_FloorType_inner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 100, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Layers'), 'Layers', '__AbsentNamespace0_FloorType_Layers', False, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 101, 6), )

    
    Layers = property(__Layers.value, __Layers.set, None, None)

    _ElementMap.update({
        __year_of_construction.name() : __year_of_construction,
        __building_age_group.name() : __building_age_group,
        __construction_type.name() : __construction_type,
        __inner_convection.name() : __inner_convection,
        __inner_radiation.name() : __inner_radiation,
        __Layers.name() : __Layers
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', 'FloorType', FloorType)


# Complex type TypeBuildingElementsType with content type ELEMENT_ONLY
class TypeBuildingElementsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type TypeBuildingElementsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TypeBuildingElementsType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 104, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element OuterWall uses Python identifier OuterWall
    __OuterWall = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'OuterWall'), 'OuterWall', '__AbsentNamespace0_TypeBuildingElementsType_OuterWall', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 107, 6), )

    
    OuterWall = property(__OuterWall.value, __OuterWall.set, None, None)

    
    # Element InnerWall uses Python identifier InnerWall
    __InnerWall = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'InnerWall'), 'InnerWall', '__AbsentNamespace0_TypeBuildingElementsType_InnerWall', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 108, 6), )

    
    InnerWall = property(__InnerWall.value, __InnerWall.set, None, None)

    
    # Element Rooftop uses Python identifier Rooftop
    __Rooftop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Rooftop'), 'Rooftop', '__AbsentNamespace0_TypeBuildingElementsType_Rooftop', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 109, 6), )

    
    Rooftop = property(__Rooftop.value, __Rooftop.set, None, None)

    
    # Element GroundFloor uses Python identifier GroundFloor
    __GroundFloor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'GroundFloor'), 'GroundFloor', '__AbsentNamespace0_TypeBuildingElementsType_GroundFloor', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 110, 6), )

    
    GroundFloor = property(__GroundFloor.value, __GroundFloor.set, None, None)

    
    # Element Window uses Python identifier Window
    __Window = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Window'), 'Window', '__AbsentNamespace0_TypeBuildingElementsType_Window', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 111, 6), )

    
    Window = property(__Window.value, __Window.set, None, None)

    
    # Element Ceiling uses Python identifier Ceiling
    __Ceiling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Ceiling'), 'Ceiling', '__AbsentNamespace0_TypeBuildingElementsType_Ceiling', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 112, 6), )

    
    Ceiling = property(__Ceiling.value, __Ceiling.set, None, None)

    
    # Element Floor uses Python identifier Floor
    __Floor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(None, 'Floor'), 'Floor', '__AbsentNamespace0_TypeBuildingElementsType_Floor', True, pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 113, 6), )

    
    Floor = property(__Floor.value, __Floor.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__AbsentNamespace0_TypeBuildingElementsType_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 105, 1)
    __version._UseLocation = pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 105, 1)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __OuterWall.name() : __OuterWall,
        __InnerWall.name() : __InnerWall,
        __Rooftop.name() : __Rooftop,
        __GroundFloor.name() : __GroundFloor,
        __Window.name() : __Window,
        __Ceiling.name() : __Ceiling,
        __Floor.name() : __Floor
    })
    _AttributeMap.update({
        __version.name() : __version
    })
Namespace.addCategoryObject('typeBinding', 'TypeBuildingElementsType', TypeBuildingElementsType)


TypeBuildingElements = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TypeBuildingElements'), TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 3, 2))
Namespace.addCategoryObject('elementBinding', TypeBuildingElements.name().localName(), TypeBuildingElements)



layerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'id'), pyxb.binding.datatypes.int, scope=layerType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 6, 6)))

layerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'thickness'), pyxb.binding.datatypes.float, scope=layerType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 7, 6)))

layerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'material'), CTD_ANON, scope=layerType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 8, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(layerType._UseForTag(pyxb.namespace.ExpandedName(None, 'id')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 6, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(layerType._UseForTag(pyxb.namespace.ExpandedName(None, 'thickness')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 7, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(layerType._UseForTag(pyxb.namespace.ExpandedName(None, 'material')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 8, 6))
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
layerType._Automaton = _BuildAutomaton()




LayersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'layer'), layerType, scope=LayersType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 21, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 21, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LayersType._UseForTag(pyxb.namespace.ExpandedName(None, 'layer')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 21, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LayersType._Automaton = _BuildAutomaton_()




OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.int, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 26, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'building_age_group'), integerList, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 27, 3)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 28, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 29, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 30, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_convection'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 31, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_radiation'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 32, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layers'), LayersType, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 33, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 26, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 26, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 27, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 28, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 29, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 30, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 31, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 32, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 33, 6))
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
OuterWallType._Automaton = _BuildAutomaton_2()




InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.int, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 38, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'building_age_group'), integerList, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 39, 3)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 40, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 41, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 42, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layers'), LayersType, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 43, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 38, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 38, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 39, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 40, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 41, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 42, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 43, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
InnerWallType._Automaton = _BuildAutomaton_3()




RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.int, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 48, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'building_age_group'), integerList, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 49, 3)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 50, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 51, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 52, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_convection'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 53, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_radiation'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 54, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layers'), LayersType, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 55, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 48, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 48, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 49, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 50, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 51, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 52, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 53, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 54, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 55, 6))
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
RooftopType._Automaton = _BuildAutomaton_4()




GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.int, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 60, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'building_age_group'), integerList, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 61, 3)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 62, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 63, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 64, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layers'), LayersType, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 65, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 60, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 60, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 61, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 62, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 63, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 64, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 65, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
GroundFloorType._Automaton = _BuildAutomaton_5()




WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.int, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 70, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'building_age_group'), integerList, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 71, 3)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 72, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 73, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 74, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_convection'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 75, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'outer_radiation'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 76, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'g_value'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 77, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'a_conv'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 78, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shading_g_total'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 79, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'shading_max_irr'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 80, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layers'), LayersType, scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 81, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 70, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 70, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 71, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 72, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 73, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 74, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 75, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'outer_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 76, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'g_value')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 77, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'a_conv')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 78, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'shading_g_total')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 79, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'shading_max_irr')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 80, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 81, 6))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
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
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
         ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
         ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
         ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
         ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
         ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
WindowType._Automaton = _BuildAutomaton_6()




CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.int, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 86, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'building_age_group'), integerList, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 87, 3)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 88, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 89, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 90, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layers'), LayersType, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 91, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 86, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 86, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 87, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 88, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 89, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 90, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 91, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
CeilingType._Automaton = _BuildAutomaton_7()




FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'year_of_construction'), pyxb.binding.datatypes.int, scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 96, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'building_age_group'), integerList, scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 97, 3)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'construction_type'), pyxb.binding.datatypes.string, scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 98, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_convection'), pyxb.binding.datatypes.float, scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 99, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'inner_radiation'), pyxb.binding.datatypes.float, scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 100, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Layers'), LayersType, scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 101, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 96, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 96, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'building_age_group')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 97, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 98, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 99, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 100, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(None, 'Layers')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 101, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
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
FloorType._Automaton = _BuildAutomaton_8()




TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'OuterWall'), OuterWallType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 107, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'InnerWall'), InnerWallType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 108, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Rooftop'), RooftopType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 109, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'GroundFloor'), GroundFloorType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 110, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Window'), WindowType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 111, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Ceiling'), CeilingType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 112, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(None, 'Floor'), FloorType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 113, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 106, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(None, 'OuterWall')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 107, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(None, 'InnerWall')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 108, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(None, 'Rooftop')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 109, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(None, 'GroundFloor')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 110, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(None, 'Window')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 111, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(None, 'Ceiling')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 112, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(None, 'Floor')), pyxb.utils.utility.Location('D:\\GIT\\pyxb\\scripts\\TypeBuildingElements.xsd', 113, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TypeBuildingElementsType._Automaton = _BuildAutomaton_9()

