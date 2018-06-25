# .\typeelement_bind.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:1e7a3b63a48543ead2f13414d1d1ee2d4278511b
# Generated 2017-05-16 15:12:04.895462 by PyXB version 1.2.5 using Python 3.6.0.final.0
# Namespace http://teaser/0.6/elements

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:41b1994c-3a39-11e7-a127-2cd444b2e704')

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
Namespace = pyxb.namespace.NamespaceForURI('http://teaser/0.6/elements', create_if_missing=True)
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


# List simple type: {http://teaser/0.6/elements}integerList
# superclasses pyxb.binding.datatypes.anySimpleType
class integerList (pyxb.binding.basis.STD_list):

    """Simple type that is a list of pyxb.binding.datatypes.integer."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'integerList')
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 132, 2)
    _Documentation = None

    _ItemType = pyxb.binding.datatypes.integer
integerList._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'integerList', integerList)
_module_typeBindings.integerList = integerList

# Complex type {http://teaser/0.6/elements}layerType with content type ELEMENT_ONLY
class layerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser/0.6/elements}layerType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'layerType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser/0.6/elements}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpteaser0_6elements_layerType_httpteaser0_6elementsid', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 9, 6), )

    
    id = property(__id.value, __id.set, None, None)

    
    # Element {http://teaser/0.6/elements}thickness uses Python identifier thickness
    __thickness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'thickness'), 'thickness', '__httpteaser0_6elements_layerType_httpteaser0_6elementsthickness', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 10, 6), )

    
    thickness = property(__thickness.value, __thickness.set, None, None)

    
    # Element {http://teaser/0.6/elements}material uses Python identifier material
    __material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'material'), 'material', '__httpteaser0_6elements_layerType_httpteaser0_6elementsmaterial', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 11, 6), )

    
    material = property(__material.value, __material.set, None, None)

    _ElementMap.update({
        __id.name() : __id,
        __thickness.name() : __thickness,
        __material.name() : __material
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.layerType = layerType
Namespace.addCategoryObject('typeBinding', 'layerType', layerType)


# Complex type [anonymous] with content type SIMPLE
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """Complex type [anonymous] with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    
    # Attribute material_id uses Python identifier material_id
    __material_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'material_id'), 'material_id', '__httpteaser0_6elements_CTD_ANON_material_id', pyxb.binding.datatypes.string)
    __material_id._DeclarationLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 15, 5)
    __material_id._UseLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 15, 5)
    
    material_id = property(__material_id.value, __material_id.set, None, None)

    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __material_id.name() : __material_id
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://teaser/0.6/elements}LayersType with content type ELEMENT_ONLY
class LayersType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser/0.6/elements}LayersType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LayersType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 22, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser/0.6/elements}layer uses Python identifier layer
    __layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'layer'), 'layer', '__httpteaser0_6elements_LayersType_httpteaser0_6elementslayer', True, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 24, 6), )

    
    layer = property(__layer.value, __layer.set, None, None)

    _ElementMap.update({
        __layer.name() : __layer
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.LayersType = LayersType
Namespace.addCategoryObject('typeBinding', 'LayersType', LayersType)


# Complex type {http://teaser/0.6/elements}OuterWallType with content type ELEMENT_ONLY
class OuterWallType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser/0.6/elements}OuterWallType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OuterWallType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 27, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser/0.6/elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser0_6elements_OuterWallType_httpteaser0_6elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 29, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser/0.6/elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser0_6elements_OuterWallType_httpteaser0_6elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 30, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser/0.6/elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser0_6elements_OuterWallType_httpteaser0_6elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 31, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser0_6elements_OuterWallType_httpteaser0_6elementsinner_convection', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 32, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser0_6elements_OuterWallType_httpteaser0_6elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 33, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser/0.6/elements}outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), 'outer_convection', '__httpteaser0_6elements_OuterWallType_httpteaser0_6elementsouter_convection', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 34, 6), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element {http://teaser/0.6/elements}outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), 'outer_radiation', '__httpteaser0_6elements_OuterWallType_httpteaser0_6elementsouter_radiation', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 35, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element {http://teaser/0.6/elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser0_6elements_OuterWallType_httpteaser0_6elementsLayers', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 36, 6), )

    
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
_module_typeBindings.OuterWallType = OuterWallType
Namespace.addCategoryObject('typeBinding', 'OuterWallType', OuterWallType)


# Complex type {http://teaser/0.6/elements}DoorType with content type ELEMENT_ONLY
class DoorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser/0.6/elements}DoorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DoorType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 39, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser/0.6/elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser0_6elements_DoorType_httpteaser0_6elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 41, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser/0.6/elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser0_6elements_DoorType_httpteaser0_6elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 42, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser/0.6/elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser0_6elements_DoorType_httpteaser0_6elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 43, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser0_6elements_DoorType_httpteaser0_6elementsinner_convection', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 44, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser0_6elements_DoorType_httpteaser0_6elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 45, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser/0.6/elements}outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), 'outer_convection', '__httpteaser0_6elements_DoorType_httpteaser0_6elementsouter_convection', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 46, 6), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element {http://teaser/0.6/elements}outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), 'outer_radiation', '__httpteaser0_6elements_DoorType_httpteaser0_6elementsouter_radiation', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 47, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element {http://teaser/0.6/elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser0_6elements_DoorType_httpteaser0_6elementsLayers', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 48, 6), )

    
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
_module_typeBindings.DoorType = DoorType
Namespace.addCategoryObject('typeBinding', 'DoorType', DoorType)


# Complex type {http://teaser/0.6/elements}InnerWallType with content type ELEMENT_ONLY
class InnerWallType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser/0.6/elements}InnerWallType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InnerWallType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 51, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser/0.6/elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser0_6elements_InnerWallType_httpteaser0_6elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 53, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser/0.6/elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser0_6elements_InnerWallType_httpteaser0_6elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 54, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser/0.6/elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser0_6elements_InnerWallType_httpteaser0_6elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 55, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser0_6elements_InnerWallType_httpteaser0_6elementsinner_convection', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 56, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser0_6elements_InnerWallType_httpteaser0_6elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 57, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser/0.6/elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser0_6elements_InnerWallType_httpteaser0_6elementsLayers', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 58, 6), )

    
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
_module_typeBindings.InnerWallType = InnerWallType
Namespace.addCategoryObject('typeBinding', 'InnerWallType', InnerWallType)


# Complex type {http://teaser/0.6/elements}RooftopType with content type ELEMENT_ONLY
class RooftopType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser/0.6/elements}RooftopType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RooftopType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 61, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser/0.6/elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser0_6elements_RooftopType_httpteaser0_6elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 63, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser/0.6/elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser0_6elements_RooftopType_httpteaser0_6elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 64, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser/0.6/elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser0_6elements_RooftopType_httpteaser0_6elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 65, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser0_6elements_RooftopType_httpteaser0_6elementsinner_convection', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 66, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser0_6elements_RooftopType_httpteaser0_6elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 67, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser/0.6/elements}outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), 'outer_convection', '__httpteaser0_6elements_RooftopType_httpteaser0_6elementsouter_convection', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 68, 6), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element {http://teaser/0.6/elements}outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), 'outer_radiation', '__httpteaser0_6elements_RooftopType_httpteaser0_6elementsouter_radiation', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 69, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element {http://teaser/0.6/elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser0_6elements_RooftopType_httpteaser0_6elementsLayers', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 70, 6), )

    
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
_module_typeBindings.RooftopType = RooftopType
Namespace.addCategoryObject('typeBinding', 'RooftopType', RooftopType)


# Complex type {http://teaser/0.6/elements}GroundFloorType with content type ELEMENT_ONLY
class GroundFloorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser/0.6/elements}GroundFloorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroundFloorType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 73, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser/0.6/elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser0_6elements_GroundFloorType_httpteaser0_6elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 75, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser/0.6/elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser0_6elements_GroundFloorType_httpteaser0_6elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 76, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser/0.6/elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser0_6elements_GroundFloorType_httpteaser0_6elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 77, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser0_6elements_GroundFloorType_httpteaser0_6elementsinner_convection', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 78, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser0_6elements_GroundFloorType_httpteaser0_6elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 79, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser/0.6/elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser0_6elements_GroundFloorType_httpteaser0_6elementsLayers', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 80, 6), )

    
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
_module_typeBindings.GroundFloorType = GroundFloorType
Namespace.addCategoryObject('typeBinding', 'GroundFloorType', GroundFloorType)


# Complex type {http://teaser/0.6/elements}WindowType with content type ELEMENT_ONLY
class WindowType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser/0.6/elements}WindowType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WindowType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 83, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser/0.6/elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser0_6elements_WindowType_httpteaser0_6elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 85, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser/0.6/elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser0_6elements_WindowType_httpteaser0_6elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 86, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser/0.6/elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser0_6elements_WindowType_httpteaser0_6elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 87, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser0_6elements_WindowType_httpteaser0_6elementsinner_convection', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 88, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser0_6elements_WindowType_httpteaser0_6elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 89, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser/0.6/elements}outer_convection uses Python identifier outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), 'outer_convection', '__httpteaser0_6elements_WindowType_httpteaser0_6elementsouter_convection', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 90, 6), )

    
    outer_convection = property(__outer_convection.value, __outer_convection.set, None, None)

    
    # Element {http://teaser/0.6/elements}outer_radiation uses Python identifier outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), 'outer_radiation', '__httpteaser0_6elements_WindowType_httpteaser0_6elementsouter_radiation', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 91, 6), )

    
    outer_radiation = property(__outer_radiation.value, __outer_radiation.set, None, None)

    
    # Element {http://teaser/0.6/elements}g_value uses Python identifier g_value
    __g_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'g_value'), 'g_value', '__httpteaser0_6elements_WindowType_httpteaser0_6elementsg_value', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 92, 6), )

    
    g_value = property(__g_value.value, __g_value.set, None, None)

    
    # Element {http://teaser/0.6/elements}a_conv uses Python identifier a_conv
    __a_conv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'a_conv'), 'a_conv', '__httpteaser0_6elements_WindowType_httpteaser0_6elementsa_conv', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 93, 6), )

    
    a_conv = property(__a_conv.value, __a_conv.set, None, None)

    
    # Element {http://teaser/0.6/elements}shading_g_total uses Python identifier shading_g_total
    __shading_g_total = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shading_g_total'), 'shading_g_total', '__httpteaser0_6elements_WindowType_httpteaser0_6elementsshading_g_total', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 94, 6), )

    
    shading_g_total = property(__shading_g_total.value, __shading_g_total.set, None, None)

    
    # Element {http://teaser/0.6/elements}shading_max_irr uses Python identifier shading_max_irr
    __shading_max_irr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'shading_max_irr'), 'shading_max_irr', '__httpteaser0_6elements_WindowType_httpteaser0_6elementsshading_max_irr', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 95, 6), )

    
    shading_max_irr = property(__shading_max_irr.value, __shading_max_irr.set, None, None)

    
    # Element {http://teaser/0.6/elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser0_6elements_WindowType_httpteaser0_6elementsLayers', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 96, 6), )

    
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
_module_typeBindings.WindowType = WindowType
Namespace.addCategoryObject('typeBinding', 'WindowType', WindowType)


# Complex type {http://teaser/0.6/elements}CeilingType with content type ELEMENT_ONLY
class CeilingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser/0.6/elements}CeilingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CeilingType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 99, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser/0.6/elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser0_6elements_CeilingType_httpteaser0_6elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 101, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser/0.6/elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser0_6elements_CeilingType_httpteaser0_6elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 102, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser/0.6/elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser0_6elements_CeilingType_httpteaser0_6elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 103, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser0_6elements_CeilingType_httpteaser0_6elementsinner_convection', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 104, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser0_6elements_CeilingType_httpteaser0_6elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 105, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser/0.6/elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser0_6elements_CeilingType_httpteaser0_6elementsLayers', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 106, 6), )

    
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
_module_typeBindings.CeilingType = CeilingType
Namespace.addCategoryObject('typeBinding', 'CeilingType', CeilingType)


# Complex type {http://teaser/0.6/elements}FloorType with content type ELEMENT_ONLY
class FloorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser/0.6/elements}FloorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FloorType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 109, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser/0.6/elements}year_of_construction uses Python identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction', '__httpteaser0_6elements_FloorType_httpteaser0_6elementsyear_of_construction', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 111, 6), )

    
    year_of_construction = property(__year_of_construction.value, __year_of_construction.set, None, None)

    
    # Element {http://teaser/0.6/elements}building_age_group uses Python identifier building_age_group
    __building_age_group = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), 'building_age_group', '__httpteaser0_6elements_FloorType_httpteaser0_6elementsbuilding_age_group', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 112, 3), )

    
    building_age_group = property(__building_age_group.value, __building_age_group.set, None, None)

    
    # Element {http://teaser/0.6/elements}construction_type uses Python identifier construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type', '__httpteaser0_6elements_FloorType_httpteaser0_6elementsconstruction_type', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 113, 6), )

    
    construction_type = property(__construction_type.value, __construction_type.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_convection uses Python identifier inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), 'inner_convection', '__httpteaser0_6elements_FloorType_httpteaser0_6elementsinner_convection', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 114, 6), )

    
    inner_convection = property(__inner_convection.value, __inner_convection.set, None, None)

    
    # Element {http://teaser/0.6/elements}inner_radiation uses Python identifier inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser0_6elements_FloorType_httpteaser0_6elementsinner_radiation', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 115, 6), )

    
    inner_radiation = property(__inner_radiation.value, __inner_radiation.set, None, None)

    
    # Element {http://teaser/0.6/elements}Layers uses Python identifier Layers
    __Layers = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layers'), 'Layers', '__httpteaser0_6elements_FloorType_httpteaser0_6elementsLayers', False, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 116, 6), )

    
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
_module_typeBindings.FloorType = FloorType
Namespace.addCategoryObject('typeBinding', 'FloorType', FloorType)


# Complex type {http://teaser/0.6/elements}TypeBuildingElementsType with content type ELEMENT_ONLY
class TypeBuildingElementsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser/0.6/elements}TypeBuildingElementsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'TypeBuildingElementsType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 119, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://teaser/0.6/elements}OuterWall uses Python identifier OuterWall
    __OuterWall = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OuterWall'), 'OuterWall', '__httpteaser0_6elements_TypeBuildingElementsType_httpteaser0_6elementsOuterWall', True, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 122, 6), )

    
    OuterWall = property(__OuterWall.value, __OuterWall.set, None, None)

    
    # Element {http://teaser/0.6/elements}Door uses Python identifier Door
    __Door = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Door'), 'Door', '__httpteaser0_6elements_TypeBuildingElementsType_httpteaser0_6elementsDoor', True, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 123, 6), )

    
    Door = property(__Door.value, __Door.set, None, None)

    
    # Element {http://teaser/0.6/elements}InnerWall uses Python identifier InnerWall
    __InnerWall = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InnerWall'), 'InnerWall', '__httpteaser0_6elements_TypeBuildingElementsType_httpteaser0_6elementsInnerWall', True, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 124, 6), )

    
    InnerWall = property(__InnerWall.value, __InnerWall.set, None, None)

    
    # Element {http://teaser/0.6/elements}Rooftop uses Python identifier Rooftop
    __Rooftop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rooftop'), 'Rooftop', '__httpteaser0_6elements_TypeBuildingElementsType_httpteaser0_6elementsRooftop', True, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 125, 6), )

    
    Rooftop = property(__Rooftop.value, __Rooftop.set, None, None)

    
    # Element {http://teaser/0.6/elements}GroundFloor uses Python identifier GroundFloor
    __GroundFloor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GroundFloor'), 'GroundFloor', '__httpteaser0_6elements_TypeBuildingElementsType_httpteaser0_6elementsGroundFloor', True, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 126, 6), )

    
    GroundFloor = property(__GroundFloor.value, __GroundFloor.set, None, None)

    
    # Element {http://teaser/0.6/elements}Window uses Python identifier Window
    __Window = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Window'), 'Window', '__httpteaser0_6elements_TypeBuildingElementsType_httpteaser0_6elementsWindow', True, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 127, 6), )

    
    Window = property(__Window.value, __Window.set, None, None)

    
    # Element {http://teaser/0.6/elements}Ceiling uses Python identifier Ceiling
    __Ceiling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ceiling'), 'Ceiling', '__httpteaser0_6elements_TypeBuildingElementsType_httpteaser0_6elementsCeiling', True, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 128, 6), )

    
    Ceiling = property(__Ceiling.value, __Ceiling.set, None, None)

    
    # Element {http://teaser/0.6/elements}Floor uses Python identifier Floor
    __Floor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Floor'), 'Floor', '__httpteaser0_6elements_TypeBuildingElementsType_httpteaser0_6elementsFloor', True, pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 129, 6), )

    
    Floor = property(__Floor.value, __Floor.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpteaser0_6elements_TypeBuildingElementsType_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 120, 1)
    __version._UseLocation = pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 120, 1)
    
    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __OuterWall.name() : __OuterWall,
        __Door.name() : __Door,
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
_module_typeBindings.TypeBuildingElementsType = TypeBuildingElementsType
Namespace.addCategoryObject('typeBinding', 'TypeBuildingElementsType', TypeBuildingElementsType)


TypeBuildingElements = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'TypeBuildingElements'), TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 6, 2))
Namespace.addCategoryObject('elementBinding', TypeBuildingElements.name().localName(), TypeBuildingElements)



layerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), pyxb.binding.datatypes.int, scope=layerType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 9, 6)))

layerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'thickness'), pyxb.binding.datatypes.float, scope=layerType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 10, 6)))

layerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'material'), CTD_ANON, scope=layerType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 11, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(layerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'id')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 9, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(layerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'thickness')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 10, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(layerType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'material')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 11, 6))
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




LayersType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'layer'), layerType, scope=LayersType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 24, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 24, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(LayersType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'layer')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 24, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
LayersType._Automaton = _BuildAutomaton_()




OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 29, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 30, 3)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 31, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 32, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 33, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 34, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), pyxb.binding.datatypes.float, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 35, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 36, 6)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 29, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 29, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 30, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 31, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 32, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 33, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_convection')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 34, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 35, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 36, 6))
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




DoorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=DoorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 41, 6)))

DoorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=DoorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 42, 3)))

DoorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=DoorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 43, 6)))

DoorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=DoorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 44, 6)))

DoorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=DoorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 45, 6)))

DoorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), pyxb.binding.datatypes.float, scope=DoorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 46, 6)))

DoorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), pyxb.binding.datatypes.float, scope=DoorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 47, 6)))

DoorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=DoorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 48, 6)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 41, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 41, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 42, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 43, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 44, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 45, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_convection')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 46, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 47, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(DoorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 48, 6))
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
DoorType._Automaton = _BuildAutomaton_3()




InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 53, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 54, 3)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 55, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 56, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 57, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 58, 6)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 53, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 53, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 54, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 55, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 56, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 57, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 58, 6))
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
InnerWallType._Automaton = _BuildAutomaton_4()




RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 63, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 64, 3)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 65, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 66, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 67, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 68, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), pyxb.binding.datatypes.float, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 69, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=RooftopType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 70, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 63, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 63, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 64, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 65, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 66, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 67, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_convection')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 68, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 69, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 70, 6))
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
RooftopType._Automaton = _BuildAutomaton_5()




GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 75, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 76, 3)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 77, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 78, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 79, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 80, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 75, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 75, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 76, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 77, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 78, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 79, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 80, 6))
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
GroundFloorType._Automaton = _BuildAutomaton_6()




WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=WindowType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 85, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=WindowType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 86, 3)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=WindowType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 87, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 88, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 89, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 90, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 91, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'g_value'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 92, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'a_conv'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 93, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shading_g_total'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 94, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shading_max_irr'), pyxb.binding.datatypes.float, scope=WindowType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 95, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=WindowType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 96, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 85, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 85, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 86, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 87, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 88, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 89, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_convection')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 90, 6))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 91, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'g_value')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 92, 6))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'a_conv')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 93, 6))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shading_g_total')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 94, 6))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'shading_max_irr')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 95, 6))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 96, 6))
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
WindowType._Automaton = _BuildAutomaton_7()




CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 101, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 102, 3)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 103, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 104, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 105, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=CeilingType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 106, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 101, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 101, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 102, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 103, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 104, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 105, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 106, 6))
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
CeilingType._Automaton = _BuildAutomaton_8()




FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int, scope=FloorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 111, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'building_age_group'), integerList, scope=FloorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 112, 3)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string, scope=FloorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 113, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float, scope=FloorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 114, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float, scope=FloorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 115, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layers'), LayersType, scope=FloorType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 116, 6)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 111, 6))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 111, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'building_age_group')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 112, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 113, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 114, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 115, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Layers')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 116, 6))
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
FloorType._Automaton = _BuildAutomaton_9()




TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OuterWall'), OuterWallType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 122, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Door'), DoorType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 123, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InnerWall'), InnerWallType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 124, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rooftop'), RooftopType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 125, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GroundFloor'), GroundFloorType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 126, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Window'), WindowType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 127, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ceiling'), CeilingType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 128, 6)))

TypeBuildingElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Floor'), FloorType, scope=TypeBuildingElementsType, location=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 129, 6)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 121, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OuterWall')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 122, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Door')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 123, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InnerWall')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 124, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Rooftop')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 125, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GroundFloor')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 126, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Window')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 127, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Ceiling')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 128, 6))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TypeBuildingElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Floor')), pyxb.utils.utility.Location('D:\\\\GIT\\\\TEASER\\\\teaser\\\\data\\\\bindings\\\\schemas\\\\TypeBuildingElements.xsd', 129, 6))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_6._set_transitionSet(transitions)
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
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TypeBuildingElementsType._Automaton = _BuildAutomaton_10()

