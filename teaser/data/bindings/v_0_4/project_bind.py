# .\project_bind.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:f5ae7850b2e91390f964b3dcf48cd22f3d76364e
# Generated 2017-01-09 16:25:18.350211 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace http://teaser.project

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier(
    'urn:uuid:d3a05e02-d67f-11e6-871f-2cd444b2e704')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.5'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import teaser.data.bindings.v_0_4.boundaryconditions_bind as \
    _ImportedBinding__usecond
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(
    'http://teaser.project', create_if_missing=True)
Namespace.configureCategories(['typeBinding_04', 'elementBinding_04'])


def CreateFromDocument(xml_text, default_namespace=None, location_base=None):
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
    saxer = pyxb.binding.saxer.make_parser(
        fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {http://teaser.project}UseConditionType with content type
# ELEMENT_ONLY
class UseConditionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}UseConditionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'UseConditionType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 7, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}BoundaryConditions uses Python identifier
    # BoundaryConditions
    __BoundaryConditions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BoundaryConditions'), 'BoundaryConditions',
                                                                   '__httpteaser_project_UseConditionType_httpteaser_projectBoundaryConditions', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 9, 6), )

    BoundaryConditions = property(
        __BoundaryConditions.value, __BoundaryConditions.set, None, None)

    _ElementMap.update({
        __BoundaryConditions.name(): __BoundaryConditions
    })
    _AttributeMap.update({

    })


_module_typeBindings.UseConditionType = UseConditionType
Namespace.addCategoryObject(
    'typeBinding_04', 'UseConditionType', UseConditionType)


# Complex type {http://teaser.project}MaterialType with content type
# ELEMENT_ONLY
class MaterialType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}MaterialType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 12, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_MaterialType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 14, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}density uses Python identifier density
    __density = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'density'), 'density', '__httpteaser_project_MaterialType_httpteaser_projectdensity',
                                                        False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 15, 6), )

    density = property(__density.value, __density.set, None, None)

    # Element {http://teaser.project}thermal_conduc uses Python identifier
    # thermal_conduc
    __thermal_conduc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'thermal_conduc'), 'thermal_conduc', '__httpteaser_project_MaterialType_httpteaser_projectthermal_conduc', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 16, 6), )

    thermal_conduc = property(__thermal_conduc.value,
                              __thermal_conduc.set, None, None)

    # Element {http://teaser.project}heat_capac uses Python identifier
    # heat_capac
    __heat_capac = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'heat_capac'), 'heat_capac', '__httpteaser_project_MaterialType_httpteaser_projectheat_capac', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 17, 6), )

    heat_capac = property(__heat_capac.value, __heat_capac.set, None, None)

    # Element {http://teaser.project}solar_absorp uses Python identifier
    # solar_absorp
    __solar_absorp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'solar_absorp'), 'solar_absorp', '__httpteaser_project_MaterialType_httpteaser_projectsolar_absorp', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 18, 6), )

    solar_absorp = property(__solar_absorp.value,
                            __solar_absorp.set, None, None)

    # Element {http://teaser.project}ir_emissivity uses Python identifier
    # ir_emissivity
    __ir_emissivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'ir_emissivity'), 'ir_emissivity', '__httpteaser_project_MaterialType_httpteaser_projectir_emissivity', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 19, 6), )

    ir_emissivity = property(__ir_emissivity.value,
                             __ir_emissivity.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __density.name(): __density,
        __thermal_conduc.name(): __thermal_conduc,
        __heat_capac.name(): __heat_capac,
        __solar_absorp.name(): __solar_absorp,
        __ir_emissivity.name(): __ir_emissivity
    })
    _AttributeMap.update({

    })


_module_typeBindings.MaterialType = MaterialType
Namespace.addCategoryObject('typeBinding_04', 'MaterialType', MaterialType)


# Complex type {http://teaser.project}LayerType with content type ELEMENT_ONLY
class LayerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}LayerType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'LayerType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 22, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}id uses Python identifier id
    __id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'id'), 'id', '__httpteaser_project_LayerType_httpteaser_projectid',
                                                   False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 24, 6), )

    id = property(__id.value, __id.set, None, None)

    # Element {http://teaser.project}thickness uses Python identifier thickness
    __thickness = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'thickness'), 'thickness', '__httpteaser_project_LayerType_httpteaser_projectthickness', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 25, 6), )

    thickness = property(__thickness.value, __thickness.set, None, None)

    # Element {http://teaser.project}Material uses Python identifier Material
    __Material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Material'), 'Material', '__httpteaser_project_LayerType_httpteaser_projectMaterial',
                                                         False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 26, 6), )

    Material = property(__Material.value, __Material.set, None, None)

    _ElementMap.update({
        __id.name(): __id,
        __thickness.name(): __thickness,
        __Material.name(): __Material
    })
    _AttributeMap.update({

    })


_module_typeBindings.LayerType = LayerType
Namespace.addCategoryObject('typeBinding_04', 'LayerType', LayerType)


# Complex type {http://teaser.project}OuterWallType with content type
# ELEMENT_ONLY
class OuterWallType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}OuterWallType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OuterWallType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 29, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_OuterWallType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 31, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_OuterWallType_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 32, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}construction_type uses Python identifier
    # construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type',
                                                                  '__httpteaser_project_OuterWallType_httpteaser_projectconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 33, 6), )

    construction_type = property(
        __construction_type.value, __construction_type.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_OuterWallType_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 34, 6), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'area'), 'area', '__httpteaser_project_OuterWallType_httpteaser_projectarea',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 35, 6), )

    area = property(__area.value, __area.set, None, None)

    # Element {http://teaser.project}tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilt'), 'tilt', '__httpteaser_project_OuterWallType_httpteaser_projecttilt',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 36, 6), )

    tilt = property(__tilt.value, __tilt.set, None, None)

    # Element {http://teaser.project}orientation uses Python identifier
    # orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'orientation'), 'orientation', '__httpteaser_project_OuterWallType_httpteaser_projectorientation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 37, 6), )

    orientation = property(__orientation.value, __orientation.set, None, None)

    # Element {http://teaser.project}inner_convection uses Python identifier
    # inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_project_OuterWallType_httpteaser_projectinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 38, 6), )

    inner_convection = property(
        __inner_convection.value, __inner_convection.set, None, None)

    # Element {http://teaser.project}inner_radiation uses Python identifier
    # inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_project_OuterWallType_httpteaser_projectinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 39, 6), )

    inner_radiation = property(
        __inner_radiation.value, __inner_radiation.set, None, None)

    # Element {http://teaser.project}outer_convection uses Python identifier
    # outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'outer_convection'), 'outer_convection', '__httpteaser_project_OuterWallType_httpteaser_projectouter_convection', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 40, 6), )

    outer_convection = property(
        __outer_convection.value, __outer_convection.set, None, None)

    # Element {http://teaser.project}outer_radiation uses Python identifier
    # outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'outer_radiation'), 'outer_radiation', '__httpteaser_project_OuterWallType_httpteaser_projectouter_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 41, 6), )

    outer_radiation = property(
        __outer_radiation.value, __outer_radiation.set, None, None)

    # Element {http://teaser.project}Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layer'), 'Layer', '__httpteaser_project_OuterWallType_httpteaser_projectLayer',
                                                      True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 42, 6), )

    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __year_of_construction.name(): __year_of_construction,
        __construction_type.name(): __construction_type,
        __year_of_retrofit.name(): __year_of_retrofit,
        __area.name(): __area,
        __tilt.name(): __tilt,
        __orientation.name(): __orientation,
        __inner_convection.name(): __inner_convection,
        __inner_radiation.name(): __inner_radiation,
        __outer_convection.name(): __outer_convection,
        __outer_radiation.name(): __outer_radiation,
        __Layer.name(): __Layer
    })
    _AttributeMap.update({

    })


_module_typeBindings.OuterWallType = OuterWallType
Namespace.addCategoryObject('typeBinding_04', 'OuterWallType', OuterWallType)


# Complex type {http://teaser.project}RooftopType with content type
# ELEMENT_ONLY
class RooftopType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}RooftopType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'RooftopType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 45, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_RooftopType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 47, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_RooftopType_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 48, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}construction_type uses Python identifier
    # construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type',
                                                                  '__httpteaser_project_RooftopType_httpteaser_projectconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 49, 6), )

    construction_type = property(
        __construction_type.value, __construction_type.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_RooftopType_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 50, 6), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'area'), 'area', '__httpteaser_project_RooftopType_httpteaser_projectarea',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 51, 6), )

    area = property(__area.value, __area.set, None, None)

    # Element {http://teaser.project}tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilt'), 'tilt', '__httpteaser_project_RooftopType_httpteaser_projecttilt',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 52, 6), )

    tilt = property(__tilt.value, __tilt.set, None, None)

    # Element {http://teaser.project}orientation uses Python identifier
    # orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'orientation'), 'orientation', '__httpteaser_project_RooftopType_httpteaser_projectorientation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 53, 6), )

    orientation = property(__orientation.value, __orientation.set, None, None)

    # Element {http://teaser.project}inner_convection uses Python identifier
    # inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_project_RooftopType_httpteaser_projectinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 54, 6), )

    inner_convection = property(
        __inner_convection.value, __inner_convection.set, None, None)

    # Element {http://teaser.project}inner_radiation uses Python identifier
    # inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_project_RooftopType_httpteaser_projectinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 55, 6), )

    inner_radiation = property(
        __inner_radiation.value, __inner_radiation.set, None, None)

    # Element {http://teaser.project}outer_convection uses Python identifier
    # outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'outer_convection'), 'outer_convection', '__httpteaser_project_RooftopType_httpteaser_projectouter_convection', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 56, 6), )

    outer_convection = property(
        __outer_convection.value, __outer_convection.set, None, None)

    # Element {http://teaser.project}outer_radiation uses Python identifier
    # outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'outer_radiation'), 'outer_radiation', '__httpteaser_project_RooftopType_httpteaser_projectouter_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 57, 6), )

    outer_radiation = property(
        __outer_radiation.value, __outer_radiation.set, None, None)

    # Element {http://teaser.project}Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layer'), 'Layer', '__httpteaser_project_RooftopType_httpteaser_projectLayer',
                                                      True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 58, 6), )

    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __year_of_construction.name(): __year_of_construction,
        __construction_type.name(): __construction_type,
        __year_of_retrofit.name(): __year_of_retrofit,
        __area.name(): __area,
        __tilt.name(): __tilt,
        __orientation.name(): __orientation,
        __inner_convection.name(): __inner_convection,
        __inner_radiation.name(): __inner_radiation,
        __outer_convection.name(): __outer_convection,
        __outer_radiation.name(): __outer_radiation,
        __Layer.name(): __Layer
    })
    _AttributeMap.update({

    })


_module_typeBindings.RooftopType = RooftopType
Namespace.addCategoryObject('typeBinding_04', 'RooftopType', RooftopType)


# Complex type {http://teaser.project}InnerWallType with content type
# ELEMENT_ONLY
class InnerWallType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}InnerWallType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InnerWallType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 61, 3)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_InnerWallType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 63, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_InnerWallType_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 64, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}construction_type uses Python identifier
    # construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type',
                                                                  '__httpteaser_project_InnerWallType_httpteaser_projectconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 65, 6), )

    construction_type = property(
        __construction_type.value, __construction_type.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_InnerWallType_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 66, 6), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'area'), 'area', '__httpteaser_project_InnerWallType_httpteaser_projectarea',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 67, 6), )

    area = property(__area.value, __area.set, None, None)

    # Element {http://teaser.project}tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilt'), 'tilt', '__httpteaser_project_InnerWallType_httpteaser_projecttilt',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 68, 6), )

    tilt = property(__tilt.value, __tilt.set, None, None)

    # Element {http://teaser.project}orientation uses Python identifier
    # orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'orientation'), 'orientation', '__httpteaser_project_InnerWallType_httpteaser_projectorientation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 69, 6), )

    orientation = property(__orientation.value, __orientation.set, None, None)

    # Element {http://teaser.project}inner_convection uses Python identifier
    # inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_project_InnerWallType_httpteaser_projectinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 70, 6), )

    inner_convection = property(
        __inner_convection.value, __inner_convection.set, None, None)

    # Element {http://teaser.project}inner_radiation uses Python identifier
    # inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_project_InnerWallType_httpteaser_projectinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 71, 6), )

    inner_radiation = property(
        __inner_radiation.value, __inner_radiation.set, None, None)

    # Element {http://teaser.project}Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layer'), 'Layer', '__httpteaser_project_InnerWallType_httpteaser_projectLayer',
                                                      True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 72, 6), )

    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __year_of_construction.name(): __year_of_construction,
        __construction_type.name(): __construction_type,
        __year_of_retrofit.name(): __year_of_retrofit,
        __area.name(): __area,
        __tilt.name(): __tilt,
        __orientation.name(): __orientation,
        __inner_convection.name(): __inner_convection,
        __inner_radiation.name(): __inner_radiation,
        __Layer.name(): __Layer
    })
    _AttributeMap.update({

    })


_module_typeBindings.InnerWallType = InnerWallType
Namespace.addCategoryObject('typeBinding_04', 'InnerWallType', InnerWallType)


# Complex type {http://teaser.project}CeilingType with content type
# ELEMENT_ONLY
class CeilingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}CeilingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CeilingType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 75, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_CeilingType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 77, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_CeilingType_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 78, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}construction_type uses Python identifier
    # construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type',
                                                                  '__httpteaser_project_CeilingType_httpteaser_projectconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 79, 6), )

    construction_type = property(
        __construction_type.value, __construction_type.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_CeilingType_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 80, 6), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'area'), 'area', '__httpteaser_project_CeilingType_httpteaser_projectarea',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 81, 6), )

    area = property(__area.value, __area.set, None, None)

    # Element {http://teaser.project}tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilt'), 'tilt', '__httpteaser_project_CeilingType_httpteaser_projecttilt',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 82, 6), )

    tilt = property(__tilt.value, __tilt.set, None, None)

    # Element {http://teaser.project}orientation uses Python identifier
    # orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'orientation'), 'orientation', '__httpteaser_project_CeilingType_httpteaser_projectorientation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 83, 6), )

    orientation = property(__orientation.value, __orientation.set, None, None)

    # Element {http://teaser.project}inner_convection uses Python identifier
    # inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_project_CeilingType_httpteaser_projectinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 84, 6), )

    inner_convection = property(
        __inner_convection.value, __inner_convection.set, None, None)

    # Element {http://teaser.project}inner_radiation uses Python identifier
    # inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_project_CeilingType_httpteaser_projectinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 85, 6), )

    inner_radiation = property(
        __inner_radiation.value, __inner_radiation.set, None, None)

    # Element {http://teaser.project}Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layer'), 'Layer', '__httpteaser_project_CeilingType_httpteaser_projectLayer',
                                                      True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 86, 6), )

    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __year_of_construction.name(): __year_of_construction,
        __construction_type.name(): __construction_type,
        __year_of_retrofit.name(): __year_of_retrofit,
        __area.name(): __area,
        __tilt.name(): __tilt,
        __orientation.name(): __orientation,
        __inner_convection.name(): __inner_convection,
        __inner_radiation.name(): __inner_radiation,
        __Layer.name(): __Layer
    })
    _AttributeMap.update({

    })


_module_typeBindings.CeilingType = CeilingType
Namespace.addCategoryObject('typeBinding_04', 'CeilingType', CeilingType)


# Complex type {http://teaser.project}FloorType with content type ELEMENT_ONLY
class FloorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}FloorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'FloorType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 89, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_FloorType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 91, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_FloorType_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 92, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}construction_type uses Python identifier
    # construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type',
                                                                  '__httpteaser_project_FloorType_httpteaser_projectconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 93, 6), )

    construction_type = property(
        __construction_type.value, __construction_type.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_FloorType_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 94, 6), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'area'), 'area', '__httpteaser_project_FloorType_httpteaser_projectarea',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 95, 6), )

    area = property(__area.value, __area.set, None, None)

    # Element {http://teaser.project}tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilt'), 'tilt', '__httpteaser_project_FloorType_httpteaser_projecttilt',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 96, 6), )

    tilt = property(__tilt.value, __tilt.set, None, None)

    # Element {http://teaser.project}orientation uses Python identifier
    # orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'orientation'), 'orientation', '__httpteaser_project_FloorType_httpteaser_projectorientation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 97, 6), )

    orientation = property(__orientation.value, __orientation.set, None, None)

    # Element {http://teaser.project}inner_convection uses Python identifier
    # inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_project_FloorType_httpteaser_projectinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 98, 6), )

    inner_convection = property(
        __inner_convection.value, __inner_convection.set, None, None)

    # Element {http://teaser.project}inner_radiation uses Python identifier
    # inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_project_FloorType_httpteaser_projectinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 99, 6), )

    inner_radiation = property(
        __inner_radiation.value, __inner_radiation.set, None, None)

    # Element {http://teaser.project}Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layer'), 'Layer', '__httpteaser_project_FloorType_httpteaser_projectLayer',
                                                      True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 100, 6), )

    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __year_of_construction.name(): __year_of_construction,
        __construction_type.name(): __construction_type,
        __year_of_retrofit.name(): __year_of_retrofit,
        __area.name(): __area,
        __tilt.name(): __tilt,
        __orientation.name(): __orientation,
        __inner_convection.name(): __inner_convection,
        __inner_radiation.name(): __inner_radiation,
        __Layer.name(): __Layer
    })
    _AttributeMap.update({

    })


_module_typeBindings.FloorType = FloorType
Namespace.addCategoryObject('typeBinding_04', 'FloorType', FloorType)


# Complex type {http://teaser.project}GroundFloorType with content type
# ELEMENT_ONLY
class GroundFloorType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}GroundFloorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroundFloorType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 103, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_GroundFloorType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 105, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_GroundFloorType_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 106, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}construction_type uses Python identifier
    # construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type',
                                                                  '__httpteaser_project_GroundFloorType_httpteaser_projectconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 107, 6), )

    construction_type = property(
        __construction_type.value, __construction_type.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_GroundFloorType_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 108, 6), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'area'), 'area', '__httpteaser_project_GroundFloorType_httpteaser_projectarea',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 109, 6), )

    area = property(__area.value, __area.set, None, None)

    # Element {http://teaser.project}tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilt'), 'tilt', '__httpteaser_project_GroundFloorType_httpteaser_projecttilt',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 110, 6), )

    tilt = property(__tilt.value, __tilt.set, None, None)

    # Element {http://teaser.project}orientation uses Python identifier
    # orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'orientation'), 'orientation', '__httpteaser_project_GroundFloorType_httpteaser_projectorientation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 111, 6), )

    orientation = property(__orientation.value, __orientation.set, None, None)

    # Element {http://teaser.project}inner_convection uses Python identifier
    # inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_project_GroundFloorType_httpteaser_projectinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 112, 6), )

    inner_convection = property(
        __inner_convection.value, __inner_convection.set, None, None)

    # Element {http://teaser.project}inner_radiation uses Python identifier
    # inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_project_GroundFloorType_httpteaser_projectinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 113, 6), )

    inner_radiation = property(
        __inner_radiation.value, __inner_radiation.set, None, None)

    # Element {http://teaser.project}Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layer'), 'Layer', '__httpteaser_project_GroundFloorType_httpteaser_projectLayer',
                                                      True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 114, 6), )

    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __year_of_construction.name(): __year_of_construction,
        __construction_type.name(): __construction_type,
        __year_of_retrofit.name(): __year_of_retrofit,
        __area.name(): __area,
        __tilt.name(): __tilt,
        __orientation.name(): __orientation,
        __inner_convection.name(): __inner_convection,
        __inner_radiation.name(): __inner_radiation,
        __Layer.name(): __Layer
    })
    _AttributeMap.update({

    })


_module_typeBindings.GroundFloorType = GroundFloorType
Namespace.addCategoryObject('typeBinding_04', 'GroundFloorType', GroundFloorType)


# Complex type {http://teaser.project}WindowType with content type ELEMENT_ONLY
class WindowType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}WindowType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'WindowType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 117, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_WindowType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 119, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_WindowType_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 120, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}construction_type uses Python identifier
    # construction_type
    __construction_type = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), 'construction_type',
                                                                  '__httpteaser_project_WindowType_httpteaser_projectconstruction_type', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 121, 6), )

    construction_type = property(
        __construction_type.value, __construction_type.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_WindowType_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 122, 6), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'area'), 'area', '__httpteaser_project_WindowType_httpteaser_projectarea',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 123, 6), )

    area = property(__area.value, __area.set, None, None)

    # Element {http://teaser.project}tilt uses Python identifier tilt
    __tilt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tilt'), 'tilt', '__httpteaser_project_WindowType_httpteaser_projecttilt',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 124, 6), )

    tilt = property(__tilt.value, __tilt.set, None, None)

    # Element {http://teaser.project}orientation uses Python identifier
    # orientation
    __orientation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'orientation'), 'orientation', '__httpteaser_project_WindowType_httpteaser_projectorientation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 125, 6), )

    orientation = property(__orientation.value, __orientation.set, None, None)

    # Element {http://teaser.project}inner_convection uses Python identifier
    # inner_convection
    __inner_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection'), 'inner_convection', '__httpteaser_project_WindowType_httpteaser_projectinner_convection', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 126, 6), )

    inner_convection = property(
        __inner_convection.value, __inner_convection.set, None, None)

    # Element {http://teaser.project}inner_radiation uses Python identifier
    # inner_radiation
    __inner_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation'), 'inner_radiation', '__httpteaser_project_WindowType_httpteaser_projectinner_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 127, 6), )

    inner_radiation = property(
        __inner_radiation.value, __inner_radiation.set, None, None)

    # Element {http://teaser.project}outer_convection uses Python identifier
    # outer_convection
    __outer_convection = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'outer_convection'), 'outer_convection', '__httpteaser_project_WindowType_httpteaser_projectouter_convection', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 128, 3), )

    outer_convection = property(
        __outer_convection.value, __outer_convection.set, None, None)

    # Element {http://teaser.project}outer_radiation uses Python identifier
    # outer_radiation
    __outer_radiation = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'outer_radiation'), 'outer_radiation', '__httpteaser_project_WindowType_httpteaser_projectouter_radiation', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 129, 6), )

    outer_radiation = property(
        __outer_radiation.value, __outer_radiation.set, None, None)

    # Element {http://teaser.project}g_value uses Python identifier g_value
    __g_value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'g_value'), 'g_value', '__httpteaser_project_WindowType_httpteaser_projectg_value',
                                                        False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 130, 3), )

    g_value = property(__g_value.value, __g_value.set, None, None)

    # Element {http://teaser.project}a_conv uses Python identifier a_conv
    __a_conv = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'a_conv'), 'a_conv', '__httpteaser_project_WindowType_httpteaser_projecta_conv',
                                                       False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 131, 6), )

    a_conv = property(__a_conv.value, __a_conv.set, None, None)

    # Element {http://teaser.project}shading_g_total uses Python identifier
    # shading_g_total
    __shading_g_total = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'shading_g_total'), 'shading_g_total', '__httpteaser_project_WindowType_httpteaser_projectshading_g_total', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 132, 6), )

    shading_g_total = property(
        __shading_g_total.value, __shading_g_total.set, None, None)

    # Element {http://teaser.project}shading_max_irr uses Python identifier
    # shading_max_irr
    __shading_max_irr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'shading_max_irr'), 'shading_max_irr', '__httpteaser_project_WindowType_httpteaser_projectshading_max_irr', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 133, 6), )

    shading_max_irr = property(
        __shading_max_irr.value, __shading_max_irr.set, None, None)

    # Element {http://teaser.project}Layer uses Python identifier Layer
    __Layer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Layer'), 'Layer', '__httpteaser_project_WindowType_httpteaser_projectLayer',
                                                      True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 134, 6), )

    Layer = property(__Layer.value, __Layer.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __year_of_construction.name(): __year_of_construction,
        __construction_type.name(): __construction_type,
        __year_of_retrofit.name(): __year_of_retrofit,
        __area.name(): __area,
        __tilt.name(): __tilt,
        __orientation.name(): __orientation,
        __inner_convection.name(): __inner_convection,
        __inner_radiation.name(): __inner_radiation,
        __outer_convection.name(): __outer_convection,
        __outer_radiation.name(): __outer_radiation,
        __g_value.name(): __g_value,
        __a_conv.name(): __a_conv,
        __shading_g_total.name(): __shading_g_total,
        __shading_max_irr.name(): __shading_max_irr,
        __Layer.name(): __Layer
    })
    _AttributeMap.update({

    })


_module_typeBindings.WindowType = WindowType
Namespace.addCategoryObject('typeBinding_04', 'WindowType', WindowType)


# Complex type {http://teaser.project}ThermalZoneType with content type
# ELEMENT_ONLY
class ThermalZoneType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}ThermalZoneType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ThermalZoneType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 137, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_ThermalZoneType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 139, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}area uses Python identifier area
    __area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'area'), 'area', '__httpteaser_project_ThermalZoneType_httpteaser_projectarea',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 140, 6), )

    area = property(__area.value, __area.set, None, None)

    # Element {http://teaser.project}volume uses Python identifier volume
    __volume = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'volume'), 'volume', '__httpteaser_project_ThermalZoneType_httpteaser_projectvolume',
                                                       False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 141, 6), )

    volume = property(__volume.value, __volume.set, None, None)

    # Element {http://teaser.project}infiltration_rate uses Python identifier
    # infiltration_rate
    __infiltration_rate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'infiltration_rate'), 'infiltration_rate',
                                                                  '__httpteaser_project_ThermalZoneType_httpteaser_projectinfiltration_rate', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 142, 6), )

    infiltration_rate = property(
        __infiltration_rate.value, __infiltration_rate.set, None, None)

    # Element {http://teaser.project}typical_length uses Python identifier
    # typical_length
    __typical_length = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'typical_length'), 'typical_length', '__httpteaser_project_ThermalZoneType_httpteaser_projecttypical_length', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 143, 6), )

    typical_length = property(__typical_length.value,
                              __typical_length.set, None, None)

    # Element {http://teaser.project}typical_width uses Python identifier
    # typical_width
    __typical_width = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'typical_width'), 'typical_width', '__httpteaser_project_ThermalZoneType_httpteaser_projecttypical_width', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 144, 2), )

    typical_width = property(__typical_width.value,
                             __typical_width.set, None, None)

    # Element {http://teaser.project}UseCondition uses Python identifier
    # UseCondition
    __UseCondition = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'UseCondition'), 'UseCondition', '__httpteaser_project_ThermalZoneType_httpteaser_projectUseCondition', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 145, 6), )

    UseCondition = property(__UseCondition.value,
                            __UseCondition.set, None, None)

    # Element {http://teaser.project}OuterWall uses Python identifier OuterWall
    __OuterWall = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'OuterWall'), 'OuterWall', '__httpteaser_project_ThermalZoneType_httpteaser_projectOuterWall', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 146, 6), )

    OuterWall = property(__OuterWall.value, __OuterWall.set, None, None)

    # Element {http://teaser.project}Rooftop uses Python identifier Rooftop
    __Rooftop = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Rooftop'), 'Rooftop', '__httpteaser_project_ThermalZoneType_httpteaser_projectRooftop',
                                                        True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 147, 6), )

    Rooftop = property(__Rooftop.value, __Rooftop.set, None, None)

    # Element {http://teaser.project}GroundFloor uses Python identifier
    # GroundFloor
    __GroundFloor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'GroundFloor'), 'GroundFloor', '__httpteaser_project_ThermalZoneType_httpteaser_projectGroundFloor', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 148, 6), )

    GroundFloor = property(__GroundFloor.value, __GroundFloor.set, None, None)

    # Element {http://teaser.project}InnerWall uses Python identifier InnerWall
    __InnerWall = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'InnerWall'), 'InnerWall', '__httpteaser_project_ThermalZoneType_httpteaser_projectInnerWall', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 149, 6), )

    InnerWall = property(__InnerWall.value, __InnerWall.set, None, None)

    # Element {http://teaser.project}Ceiling uses Python identifier Ceiling
    __Ceiling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Ceiling'), 'Ceiling', '__httpteaser_project_ThermalZoneType_httpteaser_projectCeiling',
                                                        True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 150, 6), )

    Ceiling = property(__Ceiling.value, __Ceiling.set, None, None)

    # Element {http://teaser.project}Floor uses Python identifier Floor
    __Floor = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Floor'), 'Floor', '__httpteaser_project_ThermalZoneType_httpteaser_projectFloor',
                                                      True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 151, 6), )

    Floor = property(__Floor.value, __Floor.set, None, None)

    # Element {http://teaser.project}Window uses Python identifier Window
    __Window = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Window'), 'Window', '__httpteaser_project_ThermalZoneType_httpteaser_projectWindow',
                                                       True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 152, 6), )

    Window = property(__Window.value, __Window.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __area.name(): __area,
        __volume.name(): __volume,
        __infiltration_rate.name(): __infiltration_rate,
        __typical_length.name(): __typical_length,
        __typical_width.name(): __typical_width,
        __UseCondition.name(): __UseCondition,
        __OuterWall.name(): __OuterWall,
        __Rooftop.name(): __Rooftop,
        __GroundFloor.name(): __GroundFloor,
        __InnerWall.name(): __InnerWall,
        __Ceiling.name(): __Ceiling,
        __Floor.name(): __Floor,
        __Window.name(): __Window
    })
    _AttributeMap.update({

    })


_module_typeBindings.ThermalZoneType = ThermalZoneType
Namespace.addCategoryObject('typeBinding_04', 'ThermalZoneType', ThermalZoneType)


# Complex type {http://teaser.project}BuildingAHUType with content type
# ELEMENT_ONLY
class BuildingAHUType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}BuildingAHUType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingAHUType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 155, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}heating uses Python identifier heating
    __heating = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heating'), 'heating', '__httpteaser_project_BuildingAHUType_httpteaser_projectheating',
                                                        False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 157, 6), )

    heating = property(__heating.value, __heating.set, None, None)

    # Element {http://teaser.project}cooling uses Python identifier cooling
    __cooling = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'cooling'), 'cooling', '__httpteaser_project_BuildingAHUType_httpteaser_projectcooling',
                                                        False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 158, 6), )

    cooling = property(__cooling.value, __cooling.set, None, None)

    # Element {http://teaser.project}dehumidification uses Python identifier
    # dehumidification
    __dehumidification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'dehumidification'), 'dehumidification', '__httpteaser_project_BuildingAHUType_httpteaser_projectdehumidification', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 159, 6), )

    dehumidification = property(
        __dehumidification.value, __dehumidification.set, None, None)

    # Element {http://teaser.project}humidification uses Python identifier
    # humidification
    __humidification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'humidification'), 'humidification', '__httpteaser_project_BuildingAHUType_httpteaser_projecthumidification', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 160, 6), )

    humidification = property(__humidification.value,
                              __humidification.set, None, None)

    # Element {http://teaser.project}heat_recovery uses Python identifier
    # heat_recovery
    __heat_recovery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'heat_recovery'), 'heat_recovery', '__httpteaser_project_BuildingAHUType_httpteaser_projectheat_recovery', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 161, 6), )

    heat_recovery = property(__heat_recovery.value,
                             __heat_recovery.set, None, None)

    # Element {http://teaser.project}by_pass_dehumidification uses Python
    # identifier by_pass_dehumidification
    __by_pass_dehumidification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'by_pass_dehumidification'), 'by_pass_dehumidification',
                                                                         '__httpteaser_project_BuildingAHUType_httpteaser_projectby_pass_dehumidification', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 162, 6), )

    by_pass_dehumidification = property(
        __by_pass_dehumidification.value, __by_pass_dehumidification.set, None, None)

    # Element {http://teaser.project}efficiency_recovery uses Python
    # identifier efficiency_recovery
    __efficiency_recovery = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'efficiency_recovery'), 'efficiency_recovery',
                                                                    '__httpteaser_project_BuildingAHUType_httpteaser_projectefficiency_recovery', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 163, 6), )

    efficiency_recovery = property(
        __efficiency_recovery.value, __efficiency_recovery.set, None, None)

    # Element {http://teaser.project}efficiency_revocery_false uses Python
    # identifier efficiency_revocery_false
    __efficiency_revocery_false = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'efficiency_revocery_false'), 'efficiency_revocery_false',
                                                                          '__httpteaser_project_BuildingAHUType_httpteaser_projectefficiency_revocery_false', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 164, 6), )

    efficiency_revocery_false = property(
        __efficiency_revocery_false.value, __efficiency_revocery_false.set, None, None)

    # Element {http://teaser.project}profile_min_relative_humidity uses Python
    # identifier profile_min_relative_humidity
    __profile_min_relative_humidity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'profile_min_relative_humidity'), 'profile_min_relative_humidity',
                                                                              '__httpteaser_project_BuildingAHUType_httpteaser_projectprofile_min_relative_humidity', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 165, 6), )

    profile_min_relative_humidity = property(
        __profile_min_relative_humidity.value, __profile_min_relative_humidity.set, None, None)

    # Element {http://teaser.project}profile_max_relative_humidity uses Python
    # identifier profile_max_relative_humidity
    __profile_max_relative_humidity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'profile_max_relative_humidity'), 'profile_max_relative_humidity',
                                                                              '__httpteaser_project_BuildingAHUType_httpteaser_projectprofile_max_relative_humidity', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 166, 6), )

    profile_max_relative_humidity = property(
        __profile_max_relative_humidity.value, __profile_max_relative_humidity.set, None, None)

    # Element {http://teaser.project}profile_v_flow uses Python identifier
    # profile_v_flow
    __profile_v_flow = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'profile_v_flow'), 'profile_v_flow', '__httpteaser_project_BuildingAHUType_httpteaser_projectprofile_v_flow', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 167, 6), )

    profile_v_flow = property(__profile_v_flow.value,
                              __profile_v_flow.set, None, None)

    # Element {http://teaser.project}profile_temperature uses Python
    # identifier profile_temperature
    __profile_temperature = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'profile_temperature'), 'profile_temperature',
                                                                    '__httpteaser_project_BuildingAHUType_httpteaser_projectprofile_temperature', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 168, 6), )

    profile_temperature = property(
        __profile_temperature.value, __profile_temperature.set, None, None)

    _ElementMap.update({
        __heating.name(): __heating,
        __cooling.name(): __cooling,
        __dehumidification.name(): __dehumidification,
        __humidification.name(): __humidification,
        __heat_recovery.name(): __heat_recovery,
        __by_pass_dehumidification.name(): __by_pass_dehumidification,
        __efficiency_recovery.name(): __efficiency_recovery,
        __efficiency_revocery_false.name(): __efficiency_revocery_false,
        __profile_min_relative_humidity.name(): __profile_min_relative_humidity,
        __profile_max_relative_humidity.name(): __profile_max_relative_humidity,
        __profile_v_flow.name(): __profile_v_flow,
        __profile_temperature.name(): __profile_temperature
    })
    _AttributeMap.update({

    })


_module_typeBindings.BuildingAHUType = BuildingAHUType
Namespace.addCategoryObject('typeBinding_04', 'BuildingAHUType', BuildingAHUType)


# Complex type {http://teaser.project}BuildingType with content type
# ELEMENT_ONLY
class BuildingType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}BuildingType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BuildingType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 171, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_BuildingType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 173, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}street_name uses Python identifier
    # street_name
    __street_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'street_name'), 'street_name', '__httpteaser_project_BuildingType_httpteaser_projectstreet_name', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 174, 6), )

    street_name = property(__street_name.value, __street_name.set, None, None)

    # Element {http://teaser.project}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httpteaser_project_BuildingType_httpteaser_projectcity',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 175, 6), )

    city = property(__city.value, __city.set, None, None)

    # Element {http://teaser.project}type_of_building uses Python identifier
    # type_of_building
    __type_of_building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'type_of_building'), 'type_of_building', '__httpteaser_project_BuildingType_httpteaser_projecttype_of_building', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 176, 6), )

    type_of_building = property(
        __type_of_building.value, __type_of_building.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_BuildingType_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 177, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_BuildingType_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 178, 1), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}number_of_floors uses Python identifier
    # number_of_floors
    __number_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'number_of_floors'), 'number_of_floors', '__httpteaser_project_BuildingType_httpteaser_projectnumber_of_floors', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 179, 6), )

    number_of_floors = property(
        __number_of_floors.value, __number_of_floors.set, None, None)

    # Element {http://teaser.project}height_of_floors uses Python identifier
    # height_of_floors
    __height_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'height_of_floors'), 'height_of_floors', '__httpteaser_project_BuildingType_httpteaser_projectheight_of_floors', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 180, 6), )

    height_of_floors = property(
        __height_of_floors.value, __height_of_floors.set, None, None)

    # Element {http://teaser.project}net_leased_area uses Python identifier
    # net_leased_area
    __net_leased_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'net_leased_area'), 'net_leased_area', '__httpteaser_project_BuildingType_httpteaser_projectnet_leased_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 181, 6), )

    net_leased_area = property(
        __net_leased_area.value, __net_leased_area.set, None, None)

    # Element {http://teaser.project}outer_area uses Python identifier
    # outer_area
    __outer_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'outer_area'), 'outer_area', '__httpteaser_project_BuildingType_httpteaser_projectouter_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 182, 6), )

    outer_area = property(__outer_area.value, __outer_area.set, None, None)

    # Element {http://teaser.project}window_area uses Python identifier
    # window_area
    __window_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'window_area'), 'window_area', '__httpteaser_project_BuildingType_httpteaser_projectwindow_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 183, 1), )

    window_area = property(__window_area.value, __window_area.set, None, None)

    # Element {http://teaser.project}ThermalZone uses Python identifier
    # ThermalZone
    __ThermalZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'ThermalZone'), 'ThermalZone', '__httpteaser_project_BuildingType_httpteaser_projectThermalZone', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 184, 6), )

    ThermalZone = property(__ThermalZone.value, __ThermalZone.set, None, None)

    # Element {http://teaser.project}CentralAHU uses Python identifier
    # CentralAHU
    __CentralAHU = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'CentralAHU'), 'CentralAHU', '__httpteaser_project_BuildingType_httpteaser_projectCentralAHU', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 185, 6), )

    CentralAHU = property(__CentralAHU.value, __CentralAHU.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __street_name.name(): __street_name,
        __city.name(): __city,
        __type_of_building.name(): __type_of_building,
        __year_of_construction.name(): __year_of_construction,
        __year_of_retrofit.name(): __year_of_retrofit,
        __number_of_floors.name(): __number_of_floors,
        __height_of_floors.name(): __height_of_floors,
        __net_leased_area.name(): __net_leased_area,
        __outer_area.name(): __outer_area,
        __window_area.name(): __window_area,
        __ThermalZone.name(): __ThermalZone,
        __CentralAHU.name(): __CentralAHU
    })
    _AttributeMap.update({

    })


_module_typeBindings.BuildingType = BuildingType
Namespace.addCategoryObject('typeBinding_04', 'BuildingType', BuildingType)


# Complex type {http://teaser.project}OfficeType with content type ELEMENT_ONLY
class OfficeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}OfficeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OfficeType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 188, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_OfficeType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 190, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}street_name uses Python identifier
    # street_name
    __street_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'street_name'), 'street_name', '__httpteaser_project_OfficeType_httpteaser_projectstreet_name', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 191, 6), )

    street_name = property(__street_name.value, __street_name.set, None, None)

    # Element {http://teaser.project}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httpteaser_project_OfficeType_httpteaser_projectcity',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 192, 6), )

    city = property(__city.value, __city.set, None, None)

    # Element {http://teaser.project}type_of_building uses Python identifier
    # type_of_building
    __type_of_building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'type_of_building'), 'type_of_building', '__httpteaser_project_OfficeType_httpteaser_projecttype_of_building', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 193, 6), )

    type_of_building = property(
        __type_of_building.value, __type_of_building.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_OfficeType_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 194, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_OfficeType_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 195, 3), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}number_of_floors uses Python identifier
    # number_of_floors
    __number_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'number_of_floors'), 'number_of_floors', '__httpteaser_project_OfficeType_httpteaser_projectnumber_of_floors', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 196, 6), )

    number_of_floors = property(
        __number_of_floors.value, __number_of_floors.set, None, None)

    # Element {http://teaser.project}height_of_floors uses Python identifier
    # height_of_floors
    __height_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'height_of_floors'), 'height_of_floors', '__httpteaser_project_OfficeType_httpteaser_projectheight_of_floors', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 197, 6), )

    height_of_floors = property(
        __height_of_floors.value, __height_of_floors.set, None, None)

    # Element {http://teaser.project}net_leased_area uses Python identifier
    # net_leased_area
    __net_leased_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'net_leased_area'), 'net_leased_area', '__httpteaser_project_OfficeType_httpteaser_projectnet_leased_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 198, 6), )

    net_leased_area = property(
        __net_leased_area.value, __net_leased_area.set, None, None)

    # Element {http://teaser.project}outer_area uses Python identifier
    # outer_area
    __outer_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'outer_area'), 'outer_area', '__httpteaser_project_OfficeType_httpteaser_projectouter_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 199, 6), )

    outer_area = property(__outer_area.value, __outer_area.set, None, None)

    # Element {http://teaser.project}window_area uses Python identifier
    # window_area
    __window_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'window_area'), 'window_area', '__httpteaser_project_OfficeType_httpteaser_projectwindow_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 200, 3), )

    window_area = property(__window_area.value, __window_area.set, None, None)

    # Element {http://teaser.project}ThermalZone uses Python identifier
    # ThermalZone
    __ThermalZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'ThermalZone'), 'ThermalZone', '__httpteaser_project_OfficeType_httpteaser_projectThermalZone', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 201, 6), )

    ThermalZone = property(__ThermalZone.value, __ThermalZone.set, None, None)

    # Element {http://teaser.project}CentralAHU uses Python identifier
    # CentralAHU
    __CentralAHU = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'CentralAHU'), 'CentralAHU', '__httpteaser_project_OfficeType_httpteaser_projectCentralAHU', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 202, 6), )

    CentralAHU = property(__CentralAHU.value, __CentralAHU.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __street_name.name(): __street_name,
        __city.name(): __city,
        __type_of_building.name(): __type_of_building,
        __year_of_construction.name(): __year_of_construction,
        __year_of_retrofit.name(): __year_of_retrofit,
        __number_of_floors.name(): __number_of_floors,
        __height_of_floors.name(): __height_of_floors,
        __net_leased_area.name(): __net_leased_area,
        __outer_area.name(): __outer_area,
        __window_area.name(): __window_area,
        __ThermalZone.name(): __ThermalZone,
        __CentralAHU.name(): __CentralAHU
    })
    _AttributeMap.update({

    })


_module_typeBindings.OfficeType = OfficeType
Namespace.addCategoryObject('typeBinding_04', 'OfficeType', OfficeType)


# Complex type {http://teaser.project}ResidentialType with content type
# ELEMENT_ONLY
class ResidentialType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}ResidentialType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ResidentialType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 205, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_ResidentialType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 207, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}street_name uses Python identifier
    # street_name
    __street_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'street_name'), 'street_name', '__httpteaser_project_ResidentialType_httpteaser_projectstreet_name', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 208, 6), )

    street_name = property(__street_name.value, __street_name.set, None, None)

    # Element {http://teaser.project}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httpteaser_project_ResidentialType_httpteaser_projectcity',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 209, 6), )

    city = property(__city.value, __city.set, None, None)

    # Element {http://teaser.project}type_of_building uses Python identifier
    # type_of_building
    __type_of_building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'type_of_building'), 'type_of_building', '__httpteaser_project_ResidentialType_httpteaser_projecttype_of_building', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 210, 6), )

    type_of_building = property(
        __type_of_building.value, __type_of_building.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_ResidentialType_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 211, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_ResidentialType_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 212, 3), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}number_of_floors uses Python identifier
    # number_of_floors
    __number_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'number_of_floors'), 'number_of_floors', '__httpteaser_project_ResidentialType_httpteaser_projectnumber_of_floors', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 213, 6), )

    number_of_floors = property(
        __number_of_floors.value, __number_of_floors.set, None, None)

    # Element {http://teaser.project}height_of_floors uses Python identifier
    # height_of_floors
    __height_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'height_of_floors'), 'height_of_floors', '__httpteaser_project_ResidentialType_httpteaser_projectheight_of_floors', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 214, 6), )

    height_of_floors = property(
        __height_of_floors.value, __height_of_floors.set, None, None)

    # Element {http://teaser.project}net_leased_area uses Python identifier
    # net_leased_area
    __net_leased_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'net_leased_area'), 'net_leased_area', '__httpteaser_project_ResidentialType_httpteaser_projectnet_leased_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 215, 6), )

    net_leased_area = property(
        __net_leased_area.value, __net_leased_area.set, None, None)

    # Element {http://teaser.project}outer_area uses Python identifier
    # outer_area
    __outer_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'outer_area'), 'outer_area', '__httpteaser_project_ResidentialType_httpteaser_projectouter_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 216, 6), )

    outer_area = property(__outer_area.value, __outer_area.set, None, None)

    # Element {http://teaser.project}window_area uses Python identifier
    # window_area
    __window_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'window_area'), 'window_area', '__httpteaser_project_ResidentialType_httpteaser_projectwindow_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 217, 3), )

    window_area = property(__window_area.value, __window_area.set, None, None)

    # Element {http://teaser.project}ThermalZone uses Python identifier
    # ThermalZone
    __ThermalZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'ThermalZone'), 'ThermalZone', '__httpteaser_project_ResidentialType_httpteaser_projectThermalZone', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 218, 6), )

    ThermalZone = property(__ThermalZone.value, __ThermalZone.set, None, None)

    # Element {http://teaser.project}CentralAHU uses Python identifier
    # CentralAHU
    __CentralAHU = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'CentralAHU'), 'CentralAHU', '__httpteaser_project_ResidentialType_httpteaser_projectCentralAHU', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 219, 6), )

    CentralAHU = property(__CentralAHU.value, __CentralAHU.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __street_name.name(): __street_name,
        __city.name(): __city,
        __type_of_building.name(): __type_of_building,
        __year_of_construction.name(): __year_of_construction,
        __year_of_retrofit.name(): __year_of_retrofit,
        __number_of_floors.name(): __number_of_floors,
        __height_of_floors.name(): __height_of_floors,
        __net_leased_area.name(): __net_leased_area,
        __outer_area.name(): __outer_area,
        __window_area.name(): __window_area,
        __ThermalZone.name(): __ThermalZone,
        __CentralAHU.name(): __CentralAHU
    })
    _AttributeMap.update({

    })


_module_typeBindings.ResidentialType = ResidentialType
Namespace.addCategoryObject('typeBinding_04', 'ResidentialType', ResidentialType)


# Complex type {http://teaser.project}InstituteType with content type
# ELEMENT_ONLY
class InstituteType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}InstituteType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'InstituteType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 222, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_InstituteType_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 224, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}street_name uses Python identifier
    # street_name
    __street_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'street_name'), 'street_name', '__httpteaser_project_InstituteType_httpteaser_projectstreet_name', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 225, 6), )

    street_name = property(__street_name.value, __street_name.set, None, None)

    # Element {http://teaser.project}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httpteaser_project_InstituteType_httpteaser_projectcity',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 226, 6), )

    city = property(__city.value, __city.set, None, None)

    # Element {http://teaser.project}type_of_building uses Python identifier
    # type_of_building
    __type_of_building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'type_of_building'), 'type_of_building', '__httpteaser_project_InstituteType_httpteaser_projecttype_of_building', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 227, 6), )

    type_of_building = property(
        __type_of_building.value, __type_of_building.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_InstituteType_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 228, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_InstituteType_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 229, 3), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}number_of_floors uses Python identifier
    # number_of_floors
    __number_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'number_of_floors'), 'number_of_floors', '__httpteaser_project_InstituteType_httpteaser_projectnumber_of_floors', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 230, 6), )

    number_of_floors = property(
        __number_of_floors.value, __number_of_floors.set, None, None)

    # Element {http://teaser.project}height_of_floors uses Python identifier
    # height_of_floors
    __height_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'height_of_floors'), 'height_of_floors', '__httpteaser_project_InstituteType_httpteaser_projectheight_of_floors', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 231, 6), )

    height_of_floors = property(
        __height_of_floors.value, __height_of_floors.set, None, None)

    # Element {http://teaser.project}net_leased_area uses Python identifier
    # net_leased_area
    __net_leased_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'net_leased_area'), 'net_leased_area', '__httpteaser_project_InstituteType_httpteaser_projectnet_leased_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 232, 6), )

    net_leased_area = property(
        __net_leased_area.value, __net_leased_area.set, None, None)

    # Element {http://teaser.project}outer_area uses Python identifier
    # outer_area
    __outer_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'outer_area'), 'outer_area', '__httpteaser_project_InstituteType_httpteaser_projectouter_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 233, 6), )

    outer_area = property(__outer_area.value, __outer_area.set, None, None)

    # Element {http://teaser.project}window_area uses Python identifier
    # window_area
    __window_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'window_area'), 'window_area', '__httpteaser_project_InstituteType_httpteaser_projectwindow_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 234, 3), )

    window_area = property(__window_area.value, __window_area.set, None, None)

    # Element {http://teaser.project}ThermalZone uses Python identifier
    # ThermalZone
    __ThermalZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'ThermalZone'), 'ThermalZone', '__httpteaser_project_InstituteType_httpteaser_projectThermalZone', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 235, 6), )

    ThermalZone = property(__ThermalZone.value, __ThermalZone.set, None, None)

    # Element {http://teaser.project}CentralAHU uses Python identifier
    # CentralAHU
    __CentralAHU = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'CentralAHU'), 'CentralAHU', '__httpteaser_project_InstituteType_httpteaser_projectCentralAHU', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 236, 6), )

    CentralAHU = property(__CentralAHU.value, __CentralAHU.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __street_name.name(): __street_name,
        __city.name(): __city,
        __type_of_building.name(): __type_of_building,
        __year_of_construction.name(): __year_of_construction,
        __year_of_retrofit.name(): __year_of_retrofit,
        __number_of_floors.name(): __number_of_floors,
        __height_of_floors.name(): __height_of_floors,
        __net_leased_area.name(): __net_leased_area,
        __outer_area.name(): __outer_area,
        __window_area.name(): __window_area,
        __ThermalZone.name(): __ThermalZone,
        __CentralAHU.name(): __CentralAHU
    })
    _AttributeMap.update({

    })


_module_typeBindings.InstituteType = InstituteType
Namespace.addCategoryObject('typeBinding_04', 'InstituteType', InstituteType)


# Complex type {http://teaser.project}Institute4Type with content type
# ELEMENT_ONLY
class Institute4Type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}Institute4Type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Institute4Type')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 239, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_Institute4Type_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 241, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}street_name uses Python identifier
    # street_name
    __street_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'street_name'), 'street_name', '__httpteaser_project_Institute4Type_httpteaser_projectstreet_name', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 242, 6), )

    street_name = property(__street_name.value, __street_name.set, None, None)

    # Element {http://teaser.project}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httpteaser_project_Institute4Type_httpteaser_projectcity',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 243, 6), )

    city = property(__city.value, __city.set, None, None)

    # Element {http://teaser.project}type_of_building uses Python identifier
    # type_of_building
    __type_of_building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'type_of_building'), 'type_of_building', '__httpteaser_project_Institute4Type_httpteaser_projecttype_of_building', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 244, 6), )

    type_of_building = property(
        __type_of_building.value, __type_of_building.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_Institute4Type_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 245, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_Institute4Type_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 246, 3), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}number_of_floors uses Python identifier
    # number_of_floors
    __number_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'number_of_floors'), 'number_of_floors', '__httpteaser_project_Institute4Type_httpteaser_projectnumber_of_floors', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 247, 6), )

    number_of_floors = property(
        __number_of_floors.value, __number_of_floors.set, None, None)

    # Element {http://teaser.project}height_of_floors uses Python identifier
    # height_of_floors
    __height_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'height_of_floors'), 'height_of_floors', '__httpteaser_project_Institute4Type_httpteaser_projectheight_of_floors', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 248, 6), )

    height_of_floors = property(
        __height_of_floors.value, __height_of_floors.set, None, None)

    # Element {http://teaser.project}net_leased_area uses Python identifier
    # net_leased_area
    __net_leased_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'net_leased_area'), 'net_leased_area', '__httpteaser_project_Institute4Type_httpteaser_projectnet_leased_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 249, 6), )

    net_leased_area = property(
        __net_leased_area.value, __net_leased_area.set, None, None)

    # Element {http://teaser.project}outer_area uses Python identifier
    # outer_area
    __outer_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'outer_area'), 'outer_area', '__httpteaser_project_Institute4Type_httpteaser_projectouter_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 250, 6), )

    outer_area = property(__outer_area.value, __outer_area.set, None, None)

    # Element {http://teaser.project}window_area uses Python identifier
    # window_area
    __window_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'window_area'), 'window_area', '__httpteaser_project_Institute4Type_httpteaser_projectwindow_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 251, 3), )

    window_area = property(__window_area.value, __window_area.set, None, None)

    # Element {http://teaser.project}ThermalZone uses Python identifier
    # ThermalZone
    __ThermalZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'ThermalZone'), 'ThermalZone', '__httpteaser_project_Institute4Type_httpteaser_projectThermalZone', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 252, 6), )

    ThermalZone = property(__ThermalZone.value, __ThermalZone.set, None, None)

    # Element {http://teaser.project}CentralAHU uses Python identifier
    # CentralAHU
    __CentralAHU = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'CentralAHU'), 'CentralAHU', '__httpteaser_project_Institute4Type_httpteaser_projectCentralAHU', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 253, 6), )

    CentralAHU = property(__CentralAHU.value, __CentralAHU.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __street_name.name(): __street_name,
        __city.name(): __city,
        __type_of_building.name(): __type_of_building,
        __year_of_construction.name(): __year_of_construction,
        __year_of_retrofit.name(): __year_of_retrofit,
        __number_of_floors.name(): __number_of_floors,
        __height_of_floors.name(): __height_of_floors,
        __net_leased_area.name(): __net_leased_area,
        __outer_area.name(): __outer_area,
        __window_area.name(): __window_area,
        __ThermalZone.name(): __ThermalZone,
        __CentralAHU.name(): __CentralAHU
    })
    _AttributeMap.update({

    })


_module_typeBindings.Institute4Type = Institute4Type
Namespace.addCategoryObject('typeBinding_04', 'Institute4Type', Institute4Type)


# Complex type {http://teaser.project}Institute8Type with content type
# ELEMENT_ONLY
class Institute8Type (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}Institute8Type with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Institute8Type')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 256, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_project_Institute8Type_httpteaser_projectname',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 258, 6), )

    name = property(__name.value, __name.set, None, None)

    # Element {http://teaser.project}street_name uses Python identifier
    # street_name
    __street_name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'street_name'), 'street_name', '__httpteaser_project_Institute8Type_httpteaser_projectstreet_name', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 259, 6), )

    street_name = property(__street_name.value, __street_name.set, None, None)

    # Element {http://teaser.project}city uses Python identifier city
    __city = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'city'), 'city', '__httpteaser_project_Institute8Type_httpteaser_projectcity',
                                                     False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 260, 6), )

    city = property(__city.value, __city.set, None, None)

    # Element {http://teaser.project}type_of_building uses Python identifier
    # type_of_building
    __type_of_building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'type_of_building'), 'type_of_building', '__httpteaser_project_Institute8Type_httpteaser_projecttype_of_building', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 261, 6), )

    type_of_building = property(
        __type_of_building.value, __type_of_building.set, None, None)

    # Element {http://teaser.project}year_of_construction uses Python
    # identifier year_of_construction
    __year_of_construction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), 'year_of_construction',
                                                                     '__httpteaser_project_Institute8Type_httpteaser_projectyear_of_construction', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 262, 6), )

    year_of_construction = property(
        __year_of_construction.value, __year_of_construction.set, None, None)

    # Element {http://teaser.project}year_of_retrofit uses Python identifier
    # year_of_retrofit
    __year_of_retrofit = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit'), 'year_of_retrofit', '__httpteaser_project_Institute8Type_httpteaser_projectyear_of_retrofit', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 263, 3), )

    year_of_retrofit = property(
        __year_of_retrofit.value, __year_of_retrofit.set, None, None)

    # Element {http://teaser.project}number_of_floors uses Python identifier
    # number_of_floors
    __number_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'number_of_floors'), 'number_of_floors', '__httpteaser_project_Institute8Type_httpteaser_projectnumber_of_floors', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 264, 6), )

    number_of_floors = property(
        __number_of_floors.value, __number_of_floors.set, None, None)

    # Element {http://teaser.project}height_of_floors uses Python identifier
    # height_of_floors
    __height_of_floors = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'height_of_floors'), 'height_of_floors', '__httpteaser_project_Institute8Type_httpteaser_projectheight_of_floors', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 265, 6), )

    height_of_floors = property(
        __height_of_floors.value, __height_of_floors.set, None, None)

    # Element {http://teaser.project}net_leased_area uses Python identifier
    # net_leased_area
    __net_leased_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'net_leased_area'), 'net_leased_area', '__httpteaser_project_Institute8Type_httpteaser_projectnet_leased_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 266, 6), )

    net_leased_area = property(
        __net_leased_area.value, __net_leased_area.set, None, None)

    # Element {http://teaser.project}outer_area uses Python identifier
    # outer_area
    __outer_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'outer_area'), 'outer_area', '__httpteaser_project_Institute8Type_httpteaser_projectouter_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 267, 6), )

    outer_area = property(__outer_area.value, __outer_area.set, None, None)

    # Element {http://teaser.project}window_area uses Python identifier
    # window_area
    __window_area = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'window_area'), 'window_area', '__httpteaser_project_Institute8Type_httpteaser_projectwindow_area', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 268, 3), )

    window_area = property(__window_area.value, __window_area.set, None, None)

    # Element {http://teaser.project}ThermalZone uses Python identifier
    # ThermalZone
    __ThermalZone = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'ThermalZone'), 'ThermalZone', '__httpteaser_project_Institute8Type_httpteaser_projectThermalZone', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 269, 6), )

    ThermalZone = property(__ThermalZone.value, __ThermalZone.set, None, None)

    # Element {http://teaser.project}CentralAHU uses Python identifier
    # CentralAHU
    __CentralAHU = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'CentralAHU'), 'CentralAHU', '__httpteaser_project_Institute8Type_httpteaser_projectCentralAHU', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 270, 6), )

    CentralAHU = property(__CentralAHU.value, __CentralAHU.set, None, None)

    _ElementMap.update({
        __name.name(): __name,
        __street_name.name(): __street_name,
        __city.name(): __city,
        __type_of_building.name(): __type_of_building,
        __year_of_construction.name(): __year_of_construction,
        __year_of_retrofit.name(): __year_of_retrofit,
        __number_of_floors.name(): __number_of_floors,
        __height_of_floors.name(): __height_of_floors,
        __net_leased_area.name(): __net_leased_area,
        __outer_area.name(): __outer_area,
        __window_area.name(): __window_area,
        __ThermalZone.name(): __ThermalZone,
        __CentralAHU.name(): __CentralAHU
    })
    _AttributeMap.update({

    })


_module_typeBindings.Institute8Type = Institute8Type
Namespace.addCategoryObject('typeBinding_04', 'Institute8Type', Institute8Type)


# Complex type {http://teaser.project}ProjectType with content type
# ELEMENT_ONLY
class ProjectType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.project}ProjectType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ProjectType')
    _XSDLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 273, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.project}Building uses Python identifier Building
    __Building = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Building'), 'Building', '__httpteaser_project_ProjectType_httpteaser_projectBuilding',
                                                         True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 276, 6), )

    Building = property(__Building.value, __Building.set, None, None)

    # Element {http://teaser.project}Office uses Python identifier Office
    __Office = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Office'), 'Office', '__httpteaser_project_ProjectType_httpteaser_projectOffice',
                                                       True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 277, 3), )

    Office = property(__Office.value, __Office.set, None, None)

    # Element {http://teaser.project}Residential uses Python identifier
    # Residential
    __Residential = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'Residential'), 'Residential', '__httpteaser_project_ProjectType_httpteaser_projectResidential', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 278, 3), )

    Residential = property(__Residential.value, __Residential.set, None, None)

    # Element {http://teaser.project}Institute uses Python identifier Institute
    __Institute = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'Institute'), 'Institute', '__httpteaser_project_ProjectType_httpteaser_projectInstitute', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 279, 3), )

    Institute = property(__Institute.value, __Institute.set, None, None)

    # Element {http://teaser.project}Institute4 uses Python identifier
    # Institute4
    __Institute4 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'Institute4'), 'Institute4', '__httpteaser_project_ProjectType_httpteaser_projectInstitute4', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 280, 3), )

    Institute4 = property(__Institute4.value, __Institute4.set, None, None)

    # Element {http://teaser.project}Institute8 uses Python identifier
    # Institute8
    __Institute8 = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(
        Namespace, 'Institute8'), 'Institute8', '__httpteaser_project_ProjectType_httpteaser_projectInstitute8', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 281, 3), )

    Institute8 = property(__Institute8.value, __Institute8.set, None, None)

    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(
        None, 'version'), 'version', '__httpteaser_project_ProjectType_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 274, 4)
    __version._UseLocation = pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 274, 4)

    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __Building.name(): __Building,
        __Office.name(): __Office,
        __Residential.name(): __Residential,
        __Institute.name(): __Institute,
        __Institute4.name(): __Institute4,
        __Institute8.name(): __Institute8
    })
    _AttributeMap.update({
        __version.name(): __version
    })


_module_typeBindings.ProjectType = ProjectType
Namespace.addCategoryObject('typeBinding_04', 'ProjectType', ProjectType)


Project = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Project'), ProjectType, location=pyxb.utils.utility.Location(
    'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 6, 2))
Namespace.addCategoryObject(
    'elementBinding_04', Project.name().localName(), Project)


UseConditionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BoundaryConditions'), _ImportedBinding__usecond.BoundaryConditionsType,
                                                        scope=UseConditionType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 9, 6)))


def _BuildAutomaton():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 9, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(UseConditionType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'BoundaryConditions')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 9, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


UseConditionType._Automaton = _BuildAutomaton()


MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                    scope=MaterialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 14, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'density'), pyxb.binding.datatypes.float,
                                                    scope=MaterialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 15, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'thermal_conduc'), pyxb.binding.datatypes.float,
                                                    scope=MaterialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 16, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heat_capac'), pyxb.binding.datatypes.float,
                                                    scope=MaterialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 17, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'solar_absorp'), pyxb.binding.datatypes.float,
                                                    scope=MaterialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 18, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ir_emissivity'), pyxb.binding.datatypes.float,
                                                    scope=MaterialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 19, 6)))


def _BuildAutomaton_():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 14, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'density')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 15, 6))
    st_1 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'thermal_conduc')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 16, 6))
    st_2 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'heat_capac')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 17, 6))
    st_3 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'solar_absorp')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 18, 6))
    st_4 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'ir_emissivity')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 19, 6))
    st_5 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
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


MaterialType._Automaton = _BuildAutomaton_()


LayerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'id'), pyxb.binding.datatypes.int,
                                                 scope=LayerType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 24, 6)))

LayerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'thickness'), pyxb.binding.datatypes.float,
                                                 scope=LayerType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 25, 6)))

LayerType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Material'), MaterialType, scope=LayerType,
                                                 location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 26, 6)))


def _BuildAutomaton_2():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LayerType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'id')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 24, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(LayerType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'thickness')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 25, 6))
    st_1 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LayerType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Material')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 26, 6))
    st_2 = fac.State(symbol, is_initial=False,
                     final_update=final_update, is_unordered_catenation=False)
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


LayerType._Automaton = _BuildAutomaton_2()


OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                     scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 31, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int,
                                                     scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 32, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string,
                                                     scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 33, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.int,
                                                     scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 34, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'area'), pyxb.binding.datatypes.float,
                                                     scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 35, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilt'), pyxb.binding.datatypes.float,
                                                     scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 36, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orientation'), pyxb.binding.datatypes.float,
                                                     scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 37, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float,
                                                     scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 38, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float,
                                                     scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 39, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), pyxb.binding.datatypes.float,
                                                     scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 40, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), pyxb.binding.datatypes.float,
                                                     scope=OuterWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 41, 6)))

OuterWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layer'), LayerType, scope=OuterWallType,
                                                     location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 42, 6)))


def _BuildAutomaton_3():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 31, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 32, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 33, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 34, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 35, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 36, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 37, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 38, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 39, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 40, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 41, 6))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 31, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 32, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 33, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 34, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 35, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'tilt')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 36, 6))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'orientation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 37, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 38, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 39, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'outer_convection')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 40, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'outer_radiation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 41, 6))
    st_10 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(OuterWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Layer')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 42, 6))
    st_11 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
    ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


OuterWallType._Automaton = _BuildAutomaton_3()


RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                   scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 47, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int,
                                                   scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 48, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string,
                                                   scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 49, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.int,
                                                   scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 50, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'area'), pyxb.binding.datatypes.float,
                                                   scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 51, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilt'), pyxb.binding.datatypes.float,
                                                   scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 52, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orientation'), pyxb.binding.datatypes.float,
                                                   scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 53, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float,
                                                   scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 54, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float,
                                                   scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 55, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), pyxb.binding.datatypes.float,
                                                   scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 56, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), pyxb.binding.datatypes.float,
                                                   scope=RooftopType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 57, 6)))

RooftopType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layer'), LayerType, scope=RooftopType,
                                                   location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 58, 6)))


def _BuildAutomaton_4():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 47, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 48, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 49, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 50, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 51, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 52, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 53, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 54, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 55, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 56, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 57, 6))
    counters.add(cc_10)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 47, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 48, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 49, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 50, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 51, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'tilt')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 52, 6))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'orientation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 53, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 54, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 55, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'outer_convection')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 56, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'outer_radiation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 57, 6))
    st_10 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(RooftopType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Layer')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 58, 6))
    st_11 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
    ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


RooftopType._Automaton = _BuildAutomaton_4()


InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                     scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 63, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int,
                                                     scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 64, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string,
                                                     scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 65, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.int,
                                                     scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 66, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'area'), pyxb.binding.datatypes.float,
                                                     scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 67, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilt'), pyxb.binding.datatypes.float,
                                                     scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 68, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orientation'), pyxb.binding.datatypes.float,
                                                     scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 69, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float,
                                                     scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 70, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float,
                                                     scope=InnerWallType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 71, 6)))

InnerWallType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layer'), LayerType, scope=InnerWallType,
                                                     location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 72, 6)))


def _BuildAutomaton_5():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 63, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 64, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 65, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 66, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 67, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 68, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 69, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 70, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 71, 6))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 63, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 64, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 65, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 66, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 67, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'tilt')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 68, 6))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'orientation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 69, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 70, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 71, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(InnerWallType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Layer')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 72, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
    ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


InnerWallType._Automaton = _BuildAutomaton_5()


CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                   scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 77, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int,
                                                   scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 78, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string,
                                                   scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 79, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.int,
                                                   scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 80, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'area'), pyxb.binding.datatypes.float,
                                                   scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 81, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilt'), pyxb.binding.datatypes.float,
                                                   scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 82, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orientation'), pyxb.binding.datatypes.float,
                                                   scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 83, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float,
                                                   scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 84, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float,
                                                   scope=CeilingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 85, 6)))

CeilingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layer'), LayerType, scope=CeilingType,
                                                   location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 86, 6)))


def _BuildAutomaton_6():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 77, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 78, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 79, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 80, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 81, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 82, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 83, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 84, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 85, 6))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 77, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 78, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 79, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 80, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 81, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'tilt')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 82, 6))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'orientation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 83, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 84, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 85, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CeilingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Layer')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 86, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
    ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CeilingType._Automaton = _BuildAutomaton_6()


FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                 scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 91, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int,
                                                 scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 92, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string,
                                                 scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 93, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.int,
                                                 scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 94, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'area'), pyxb.binding.datatypes.float,
                                                 scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 95, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilt'), pyxb.binding.datatypes.float,
                                                 scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 96, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orientation'), pyxb.binding.datatypes.float,
                                                 scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 97, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float,
                                                 scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 98, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float,
                                                 scope=FloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 99, 6)))

FloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layer'), LayerType, scope=FloorType,
                                                 location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 100, 6)))


def _BuildAutomaton_7():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 91, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 92, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 93, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 94, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 95, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 96, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 97, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 98, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 99, 6))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 91, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 92, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 93, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 94, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 95, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'tilt')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 96, 6))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'orientation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 97, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 98, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 99, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(FloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Layer')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 100, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
    ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


FloorType._Automaton = _BuildAutomaton_7()


GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                       scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 105, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int,
                                                       scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 106, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string,
                                                       scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 107, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.int,
                                                       scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 108, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'area'), pyxb.binding.datatypes.float,
                                                       scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 109, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilt'), pyxb.binding.datatypes.float,
                                                       scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 110, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orientation'), pyxb.binding.datatypes.float,
                                                       scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 111, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float,
                                                       scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 112, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float,
                                                       scope=GroundFloorType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 113, 6)))

GroundFloorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layer'), LayerType, scope=GroundFloorType,
                                                       location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 114, 6)))


def _BuildAutomaton_8():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 105, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 106, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 107, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 108, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 109, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 110, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 111, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 112, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 113, 6))
    counters.add(cc_8)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 105, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 106, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 107, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 108, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 109, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'tilt')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 110, 6))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'orientation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 111, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 112, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 113, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(GroundFloorType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Layer')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 114, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
    ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


GroundFloorType._Automaton = _BuildAutomaton_8()


WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 119, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.int,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 120, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'construction_type'), pyxb.binding.datatypes.string,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 121, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.int,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 122, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'area'), pyxb.binding.datatypes.float,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 123, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tilt'), pyxb.binding.datatypes.float,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 124, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'orientation'), pyxb.binding.datatypes.float,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 125, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_convection'), pyxb.binding.datatypes.float,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 126, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'inner_radiation'), pyxb.binding.datatypes.float,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 127, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_convection'), pyxb.binding.datatypes.float,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 128, 3)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_radiation'), pyxb.binding.datatypes.float,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 129, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'g_value'), pyxb.binding.datatypes.float,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 130, 3)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'a_conv'), pyxb.binding.datatypes.float,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 131, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shading_g_total'), pyxb.binding.datatypes.float,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 132, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'shading_max_irr'), pyxb.binding.datatypes.float,
                                                  scope=WindowType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 133, 6)))

WindowType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Layer'), LayerType, scope=WindowType,
                                                  location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 134, 6)))


def _BuildAutomaton_9():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 119, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 120, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 121, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 122, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 123, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 124, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 125, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 126, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 127, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 128, 3))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 129, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 130, 3))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 131, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 132, 6))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 133, 6))
    counters.add(cc_14)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 119, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 120, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'construction_type')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 121, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 122, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 123, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'tilt')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 124, 6))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'orientation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 125, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_convection')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 126, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'inner_radiation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 127, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'outer_convection')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 128, 3))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'outer_radiation')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 129, 6))
    st_10 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'g_value')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 130, 3))
    st_11 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'a_conv')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 131, 6))
    st_12 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'shading_g_total')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 132, 6))
    st_13 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'shading_max_irr')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 133, 6))
    st_14 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(WindowType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Layer')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 134, 6))
    st_15 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_11, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True)]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, False)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False)]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_14, True)]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, False)]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
    ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


WindowType._Automaton = _BuildAutomaton_9()


ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                       scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 139, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'area'), pyxb.binding.datatypes.float,
                                                       scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 140, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'volume'), pyxb.binding.datatypes.float,
                                                       scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 141, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'infiltration_rate'), pyxb.binding.datatypes.float,
                                                       scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 142, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'typical_length'), pyxb.binding.datatypes.float,
                                                       scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 143, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'typical_width'), pyxb.binding.datatypes.float,
                                                       scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 144, 2)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UseCondition'), UseConditionType,
                                                       scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 145, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OuterWall'), OuterWallType,
                                                       scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 146, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Rooftop'), RooftopType, scope=ThermalZoneType,
                                                       location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 147, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GroundFloor'), GroundFloorType,
                                                       scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 148, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InnerWall'), InnerWallType,
                                                       scope=ThermalZoneType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 149, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Ceiling'), CeilingType, scope=ThermalZoneType,
                                                       location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 150, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Floor'), FloorType, scope=ThermalZoneType,
                                                       location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 151, 6)))

ThermalZoneType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Window'), WindowType, scope=ThermalZoneType,
                                                       location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 152, 6)))


def _BuildAutomaton_10():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 139, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 140, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 141, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 142, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 143, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 144, 2))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 145, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 146, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 147, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 148, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 149, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 150, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 151, 6))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 152, 6))
    counters.add(cc_13)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 139, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 140, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'volume')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 141, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'infiltration_rate')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 142, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'typical_length')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 143, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'typical_width')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 144, 2))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'UseCondition')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 145, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'OuterWall')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 146, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Rooftop')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 147, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'GroundFloor')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 148, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'InnerWall')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 149, 6))
    st_10 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Ceiling')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 150, 6))
    st_11 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Floor')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 151, 6))
    st_12 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(ThermalZoneType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Window')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 152, 6))
    st_13 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_11, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_13, True)]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ThermalZoneType._Automaton = _BuildAutomaton_10()


BuildingAHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heating'), pyxb.binding.datatypes.boolean,
                                                       scope=BuildingAHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 157, 6)))

BuildingAHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'cooling'), pyxb.binding.datatypes.boolean,
                                                       scope=BuildingAHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 158, 6)))

BuildingAHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'dehumidification'), pyxb.binding.datatypes.boolean,
                                                       scope=BuildingAHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 159, 6)))

BuildingAHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'humidification'), pyxb.binding.datatypes.boolean,
                                                       scope=BuildingAHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 160, 6)))

BuildingAHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heat_recovery'), pyxb.binding.datatypes.boolean,
                                                       scope=BuildingAHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 161, 6)))

BuildingAHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'by_pass_dehumidification'), pyxb.binding.datatypes.float,
                                                       scope=BuildingAHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 162, 6)))

BuildingAHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'efficiency_recovery'), pyxb.binding.datatypes.float,
                                                       scope=BuildingAHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 163, 6)))

BuildingAHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'efficiency_revocery_false'), pyxb.binding.datatypes.float,
                                                       scope=BuildingAHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 164, 6)))

BuildingAHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'profile_min_relative_humidity'), _ImportedBinding__usecond.floatList,
                                                       scope=BuildingAHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 165, 6)))

BuildingAHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'profile_max_relative_humidity'), _ImportedBinding__usecond.floatList,
                                                       scope=BuildingAHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 166, 6)))

BuildingAHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'profile_v_flow'), _ImportedBinding__usecond.floatList,
                                                       scope=BuildingAHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 167, 6)))

BuildingAHUType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'profile_temperature'), _ImportedBinding__usecond.floatList,
                                                       scope=BuildingAHUType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 168, 6)))


def _BuildAutomaton_11():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 157, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 158, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 159, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 160, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 161, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 162, 6))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 163, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 164, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 165, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 166, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 167, 6))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 168, 6))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BuildingAHUType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'heating')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 157, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BuildingAHUType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'cooling')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 158, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BuildingAHUType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'dehumidification')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 159, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BuildingAHUType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'humidification')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 160, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(BuildingAHUType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'heat_recovery')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 161, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(BuildingAHUType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'by_pass_dehumidification')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 162, 6))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(BuildingAHUType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'efficiency_recovery')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 163, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(BuildingAHUType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'efficiency_revocery_false')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 164, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(BuildingAHUType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'profile_min_relative_humidity')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 165, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(BuildingAHUType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'profile_max_relative_humidity')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 166, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(BuildingAHUType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'profile_v_flow')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 167, 6))
    st_10 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(BuildingAHUType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'profile_temperature')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 168, 6))
    st_11 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True)]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


BuildingAHUType._Automaton = _BuildAutomaton_11()


BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 173, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'street_name'), pyxb.binding.datatypes.string,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 174, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), pyxb.binding.datatypes.string,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 175, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type_of_building'), pyxb.binding.datatypes.string,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 176, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.string,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 177, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.string,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 178, 1)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'number_of_floors'), pyxb.binding.datatypes.int,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 179, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'height_of_floors'), pyxb.binding.datatypes.float,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 180, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'net_leased_area'), pyxb.binding.datatypes.float,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 181, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_area'), pyxb.binding.datatypes.float,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 182, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'window_area'), pyxb.binding.datatypes.float,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 183, 1)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThermalZone'), ThermalZoneType,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 184, 6)))

BuildingType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CentralAHU'), BuildingAHUType,
                                                    scope=BuildingType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 185, 6)))


def _BuildAutomaton_12():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 173, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 174, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 175, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 176, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 177, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 178, 1))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 179, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 180, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 181, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 182, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 183, 1))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 184, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 185, 6))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 173, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'street_name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 174, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'city')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 175, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'type_of_building')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 176, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 177, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 178, 1))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'number_of_floors')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 179, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'height_of_floors')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 180, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'net_leased_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 181, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'outer_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 182, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'window_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 183, 1))
    st_10 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'ThermalZone')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 184, 6))
    st_11 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(BuildingType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'CentralAHU')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 185, 6))
    st_12 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True)]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


BuildingType._Automaton = _BuildAutomaton_12()


OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 190, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'street_name'), pyxb.binding.datatypes.string,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 191, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), pyxb.binding.datatypes.string,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 192, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type_of_building'), pyxb.binding.datatypes.string,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 193, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.string,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 194, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.string,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 195, 3)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'number_of_floors'), pyxb.binding.datatypes.int,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 196, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'height_of_floors'), pyxb.binding.datatypes.float,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 197, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'net_leased_area'), pyxb.binding.datatypes.float,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 198, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_area'), pyxb.binding.datatypes.float,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 199, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'window_area'), pyxb.binding.datatypes.float,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 200, 3)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThermalZone'), ThermalZoneType,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 201, 6)))

OfficeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CentralAHU'), BuildingAHUType,
                                                  scope=OfficeType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 202, 6)))


def _BuildAutomaton_13():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 190, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 191, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 192, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 193, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 194, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 195, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 196, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 197, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 198, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 199, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 200, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 201, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 202, 6))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 190, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'street_name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 191, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'city')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 192, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'type_of_building')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 193, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 194, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 195, 3))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'number_of_floors')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 196, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'height_of_floors')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 197, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'net_leased_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 198, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'outer_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 199, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'window_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 200, 3))
    st_10 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'ThermalZone')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 201, 6))
    st_11 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(OfficeType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'CentralAHU')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 202, 6))
    st_12 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True)]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


OfficeType._Automaton = _BuildAutomaton_13()


ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 207, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'street_name'), pyxb.binding.datatypes.string,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 208, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), pyxb.binding.datatypes.string,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 209, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type_of_building'), pyxb.binding.datatypes.string,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 210, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.string,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 211, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.string,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 212, 3)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'number_of_floors'), pyxb.binding.datatypes.int,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 213, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'height_of_floors'), pyxb.binding.datatypes.float,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 214, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'net_leased_area'), pyxb.binding.datatypes.float,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 215, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_area'), pyxb.binding.datatypes.float,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 216, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'window_area'), pyxb.binding.datatypes.float,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 217, 3)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThermalZone'), ThermalZoneType,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 218, 6)))

ResidentialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CentralAHU'), BuildingAHUType,
                                                       scope=ResidentialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 219, 6)))


def _BuildAutomaton_14():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 207, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 208, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 209, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 210, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 211, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 212, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 213, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 214, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 215, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 216, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 217, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 218, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 219, 6))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 207, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'street_name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 208, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'city')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 209, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'type_of_building')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 210, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 211, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 212, 3))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'number_of_floors')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 213, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'height_of_floors')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 214, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'net_leased_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 215, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'outer_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 216, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'window_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 217, 3))
    st_10 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'ThermalZone')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 218, 6))
    st_11 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(ResidentialType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'CentralAHU')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 219, 6))
    st_12 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True)]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ResidentialType._Automaton = _BuildAutomaton_14()


InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 224, 6)))

InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'street_name'), pyxb.binding.datatypes.string,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 225, 6)))

InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), pyxb.binding.datatypes.string,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 226, 6)))

InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type_of_building'), pyxb.binding.datatypes.string,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 227, 6)))

InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.string,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 228, 6)))

InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.string,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 229, 3)))

InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'number_of_floors'), pyxb.binding.datatypes.int,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 230, 6)))

InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'height_of_floors'), pyxb.binding.datatypes.float,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 231, 6)))

InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'net_leased_area'), pyxb.binding.datatypes.float,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 232, 6)))

InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_area'), pyxb.binding.datatypes.float,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 233, 6)))

InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'window_area'), pyxb.binding.datatypes.float,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 234, 3)))

InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThermalZone'), ThermalZoneType,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 235, 6)))

InstituteType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CentralAHU'), BuildingAHUType,
                                                     scope=InstituteType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 236, 6)))


def _BuildAutomaton_15():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 224, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 225, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 226, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 227, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 228, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 229, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 230, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 231, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 232, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 233, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 234, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 235, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 236, 6))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 224, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'street_name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 225, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'city')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 226, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'type_of_building')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 227, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 228, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 229, 3))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'number_of_floors')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 230, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'height_of_floors')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 231, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'net_leased_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 232, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'outer_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 233, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'window_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 234, 3))
    st_10 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'ThermalZone')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 235, 6))
    st_11 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(InstituteType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'CentralAHU')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 236, 6))
    st_12 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True)]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


InstituteType._Automaton = _BuildAutomaton_15()


Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 241, 6)))

Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'street_name'), pyxb.binding.datatypes.string,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 242, 6)))

Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), pyxb.binding.datatypes.string,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 243, 6)))

Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type_of_building'), pyxb.binding.datatypes.string,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 244, 6)))

Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.string,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 245, 6)))

Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.string,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 246, 3)))

Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'number_of_floors'), pyxb.binding.datatypes.int,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 247, 6)))

Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'height_of_floors'), pyxb.binding.datatypes.float,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 248, 6)))

Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'net_leased_area'), pyxb.binding.datatypes.float,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 249, 6)))

Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_area'), pyxb.binding.datatypes.float,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 250, 6)))

Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'window_area'), pyxb.binding.datatypes.float,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 251, 3)))

Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThermalZone'), ThermalZoneType,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 252, 6)))

Institute4Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CentralAHU'), BuildingAHUType,
                                                      scope=Institute4Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 253, 6)))


def _BuildAutomaton_16():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 241, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 242, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 243, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 244, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 245, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 246, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 247, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 248, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 249, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 250, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 251, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 252, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 253, 6))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 241, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'street_name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 242, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'city')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 243, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'type_of_building')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 244, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 245, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 246, 3))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'number_of_floors')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 247, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'height_of_floors')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 248, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'net_leased_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 249, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'outer_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 250, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'window_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 251, 3))
    st_10 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'ThermalZone')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 252, 6))
    st_11 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Institute4Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'CentralAHU')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 253, 6))
    st_12 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True)]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Institute4Type._Automaton = _BuildAutomaton_16()


Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 258, 6)))

Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'street_name'), pyxb.binding.datatypes.string,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 259, 6)))

Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'city'), pyxb.binding.datatypes.string,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 260, 6)))

Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'type_of_building'), pyxb.binding.datatypes.string,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 261, 6)))

Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_construction'), pyxb.binding.datatypes.string,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 262, 6)))

Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'year_of_retrofit'), pyxb.binding.datatypes.string,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 263, 3)))

Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'number_of_floors'), pyxb.binding.datatypes.int,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 264, 6)))

Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'height_of_floors'), pyxb.binding.datatypes.float,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 265, 6)))

Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'net_leased_area'), pyxb.binding.datatypes.float,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 266, 6)))

Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'outer_area'), pyxb.binding.datatypes.float,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 267, 6)))

Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'window_area'), pyxb.binding.datatypes.float,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 268, 3)))

Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ThermalZone'), ThermalZoneType,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 269, 6)))

Institute8Type._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CentralAHU'), BuildingAHUType,
                                                      scope=Institute8Type, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 270, 6)))


def _BuildAutomaton_17():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 258, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 259, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 260, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 261, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 262, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 263, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 264, 6))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 265, 6))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 266, 6))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 267, 6))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 268, 3))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 269, 6))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 270, 6))
    counters.add(cc_12)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 258, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'street_name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 259, 6))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'city')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 260, 6))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'type_of_building')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 261, 6))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_construction')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 262, 6))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'year_of_retrofit')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 263, 3))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'number_of_floors')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 264, 6))
    st_6 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'height_of_floors')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 265, 6))
    st_7 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'net_leased_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 266, 6))
    st_8 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'outer_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 267, 6))
    st_9 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'window_area')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 268, 3))
    st_10 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'ThermalZone')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 269, 6))
    st_11 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(Institute8Type._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'CentralAHU')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 270, 6))
    st_12 = fac.State(symbol, is_initial=True,
                      final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False)]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True)]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False)]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True)]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False)]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True)]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False)]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_12, True)]))
    st_12._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


Institute8Type._Automaton = _BuildAutomaton_17()


ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Building'), BuildingType, scope=ProjectType,
                                                   location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 276, 6)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Office'), OfficeType, scope=ProjectType,
                                                   location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 277, 3)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Residential'), ResidentialType,
                                                   scope=ProjectType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 278, 3)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Institute'), InstituteType, scope=ProjectType,
                                                   location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 279, 3)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Institute4'), Institute4Type,
                                                   scope=ProjectType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 280, 3)))

ProjectType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Institute8'), Institute8Type,
                                                   scope=ProjectType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 281, 3)))


def _BuildAutomaton_18():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(
        'D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 275, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Building')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 276, 6))
    st_0 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Office')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 277, 3))
    st_1 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Residential')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 278, 3))
    st_2 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Institute')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 279, 3))
    st_3 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Institute4')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 280, 3))
    st_4 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProjectType._UseForTag(pyxb.namespace.ExpandedName(
        Namespace, 'Institute8')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\Project.xsd', 281, 3))
    st_5 = fac.State(symbol, is_initial=True,
                     final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, True)]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ProjectType._Automaton = _BuildAutomaton_18()
