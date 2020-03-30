# MAEC Object Reference Class

# Copyright (c) 2018, The MITRE Corporation
# All rights reserved

from stix111.mixbox import fields

import stix111.maec
from . import _namespace
import stix111.maec.bindings.maec_bundle as bundle_binding

class ObjectReference(stix111.maec.Entity):
    _binding = bundle_binding
    _binding_class = bundle_binding.ObjectReferenceType
    _namespace = _namespace

    def __init__(self, object_idref = None):
        super(ObjectReference, self).__init__()
        self.object_idref = object_idref

class ObjectReferenceList(stix111.maec.EntityList):
    _binding_class = bundle_binding.ObjectReferenceListType
    _namespace = _namespace
    object_reference = fields.TypedField("Object_Reference", ObjectReference, multiple=True)