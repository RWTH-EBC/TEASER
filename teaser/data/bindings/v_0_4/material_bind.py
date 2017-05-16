# .\material_bind.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:5ffda81d40abe0f3bf00799d81fb473cb8de8e07
# Generated 2017-01-09 16:21:36.153994 by PyXB version 1.2.5 using Python 3.5.2.final.0
# Namespace http://teaser.material

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:4f482dd2-d67f-11e6-9d44-2cd444b2e704')

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
Namespace = pyxb.namespace.NamespaceForURI('http://teaser.material', create_if_missing=True)
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


# Complex type {http://teaser.material}MaterialType with content type ELEMENT_ONLY
class MaterialType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.material}MaterialType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 5, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.material}name uses Python identifier name
    __name = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'name'), 'name', '__httpteaser_material_MaterialType_httpteaser_materialname', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 8, 6), )


    name = property(__name.value, __name.set, None, None)


    # Element {http://teaser.material}density uses Python identifier density
    __density = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'density'), 'density', '__httpteaser_material_MaterialType_httpteaser_materialdensity', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 9, 6), )


    density = property(__density.value, __density.set, None, None)


    # Element {http://teaser.material}thermal_conduc uses Python identifier thermal_conduc
    __thermal_conduc = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'thermal_conduc'), 'thermal_conduc', '__httpteaser_material_MaterialType_httpteaser_materialthermal_conduc', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 10, 6), )


    thermal_conduc = property(__thermal_conduc.value, __thermal_conduc.set, None, None)


    # Element {http://teaser.material}heat_capac uses Python identifier heat_capac
    __heat_capac = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'heat_capac'), 'heat_capac', '__httpteaser_material_MaterialType_httpteaser_materialheat_capac', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 11, 6), )


    heat_capac = property(__heat_capac.value, __heat_capac.set, None, None)


    # Element {http://teaser.material}solar_absorp uses Python identifier solar_absorp
    __solar_absorp = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'solar_absorp'), 'solar_absorp', '__httpteaser_material_MaterialType_httpteaser_materialsolar_absorp', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 12, 6), )


    solar_absorp = property(__solar_absorp.value, __solar_absorp.set, None, None)


    # Element {http://teaser.material}ir_emissivity uses Python identifier ir_emissivity
    __ir_emissivity = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ir_emissivity'), 'ir_emissivity', '__httpteaser_material_MaterialType_httpteaser_materialir_emissivity', False, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 13, 6), )


    ir_emissivity = property(__ir_emissivity.value, __ir_emissivity.set, None, None)


    # Attribute material_id uses Python identifier material_id
    __material_id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'material_id'), 'material_id', '__httpteaser_material_MaterialType_material_id', pyxb.binding.datatypes.string)
    __material_id._DeclarationLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 6, 1)
    __material_id._UseLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 6, 1)

    material_id = property(__material_id.value, __material_id.set, None, None)

    _ElementMap.update({
        __name.name() : __name,
        __density.name() : __density,
        __thermal_conduc.name() : __thermal_conduc,
        __heat_capac.name() : __heat_capac,
        __solar_absorp.name() : __solar_absorp,
        __ir_emissivity.name() : __ir_emissivity
    })
    _AttributeMap.update({
        __material_id.name() : __material_id
    })
_module_typeBindings.MaterialType = MaterialType
Namespace.addCategoryObject('typeBinding', 'MaterialType', MaterialType)


# Complex type {http://teaser.material}MaterialTemplatesType with content type ELEMENT_ONLY
class MaterialTemplatesType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://teaser.material}MaterialTemplatesType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'MaterialTemplatesType')
    _XSDLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 16, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://teaser.material}Material uses Python identifier Material
    __Material = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Material'), 'Material', '__httpteaser_material_MaterialTemplatesType_httpteaser_materialMaterial', True, pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 19, 6), )


    Material = property(__Material.value, __Material.set, None, None)


    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpteaser_material_MaterialTemplatesType_version', pyxb.binding.datatypes.string)
    __version._DeclarationLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 17, 4)
    __version._UseLocation = pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 17, 4)

    version = property(__version.value, __version.set, None, None)

    _ElementMap.update({
        __Material.name() : __Material
    })
    _AttributeMap.update({
        __version.name() : __version
    })
_module_typeBindings.MaterialTemplatesType = MaterialTemplatesType
Namespace.addCategoryObject('typeBinding', 'MaterialTemplatesType', MaterialTemplatesType)


MaterialTemplates = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MaterialTemplates'), MaterialTemplatesType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 4, 2))
Namespace.addCategoryObject('elementBinding', MaterialTemplates.name().localName(), MaterialTemplates)



MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'name'), pyxb.binding.datatypes.string, scope=MaterialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 8, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'density'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 9, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'thermal_conduc'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 10, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'heat_capac'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 11, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'solar_absorp'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 12, 6)))

MaterialType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ir_emissivity'), pyxb.binding.datatypes.float, scope=MaterialType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 13, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 12, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 13, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'name')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 8, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'density')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 9, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'thermal_conduc')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 10, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'heat_capac')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 11, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'solar_absorp')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 12, 6))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(MaterialType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ir_emissivity')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 13, 6))
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
    transitions.append(fac.Transition(st_5, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
MaterialType._Automaton = _BuildAutomaton()




MaterialTemplatesType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Material'), MaterialType, scope=MaterialTemplatesType, location=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 19, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 18, 1))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(MaterialTemplatesType._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Material')), pyxb.utils.utility.Location('D:\\GIT\\TEASER\\teaser\\data\\bindings\\schemas\\MaterialTemplates.xsd', 19, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MaterialTemplatesType._Automaton = _BuildAutomaton_()

