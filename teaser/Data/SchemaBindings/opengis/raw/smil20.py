# ./pyxb/bundles/opengis/raw/smil20.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:21ae4a2357cfe334f6a0ce0b0ea28423d22a1453
# Generated 2015-05-04 11:01:33.852456 by PyXB version 1.2.4 using Python 2.7.9.final.0
# Namespace http://www.w3.org/2001/SMIL20/ [xmlns:smil20]

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
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:28f33378-f23c-11e4-8104-000c29ce1afb')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import teaser.Data.SchemaBindings.opengis.raw._nsgroup

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.w3.org/2001/SMIL20/', create_if_missing=True)
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

from teaser.Data.SchemaBindings.opengis.raw._nsgroup import animate # {http://www.w3.org/2001/SMIL20/}animate
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import animateMotion # {http://www.w3.org/2001/SMIL20/}animateMotion
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import animateColor # {http://www.w3.org/2001/SMIL20/}animateColor
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import set_ # {http://www.w3.org/2001/SMIL20/}set
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import nonNegativeDecimalType # {http://www.w3.org/2001/SMIL20/}nonNegativeDecimalType
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import STD_ANON # None
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import STD_ANON_ # None
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import STD_ANON_2 # None
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import STD_ANON_3 # None
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import syncBehaviorType # {http://www.w3.org/2001/SMIL20/}syncBehaviorType
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import syncBehaviorDefaultType # {http://www.w3.org/2001/SMIL20/}syncBehaviorDefaultType
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import restartTimingType # {http://www.w3.org/2001/SMIL20/}restartTimingType
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import restartDefaultType # {http://www.w3.org/2001/SMIL20/}restartDefaultType
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import fillTimingAttrsType # {http://www.w3.org/2001/SMIL20/}fillTimingAttrsType
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import fillDefaultType # {http://www.w3.org/2001/SMIL20/}fillDefaultType
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import animatePrototype # {http://www.w3.org/2001/SMIL20/}animatePrototype
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import animateMotionPrototype # {http://www.w3.org/2001/SMIL20/}animateMotionPrototype
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import animateColorPrototype # {http://www.w3.org/2001/SMIL20/}animateColorPrototype
from teaser.Data.SchemaBindings.opengis.raw._nsgroup import setPrototype # {http://www.w3.org/2001/SMIL20/}setPrototype
