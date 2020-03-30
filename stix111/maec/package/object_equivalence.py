# MAEC Action Equivalence Class

# Copyright (c) 2018, The MITRE Corporation
# All rights reserved

from stix111.mixbox import fields

import stix111.maec
from . import _namespace
import stix111.maec.bindings.maec_package as package_binding
from stix111.maec.bundle import ObjectReference

class ObjectEquivalence(stix111.maec.Entity):
    _binding = package_binding
    _binding_class = package_binding.ObjectEquivalenceType
    _namespace = _namespace

    id_ = fields.TypedField("id")
    object_reference = fields.TypedField("Object_Reference", ObjectReference, multiple = True)

    def init(self, id = None):
        super(ObjectEquivalence, self).__init__()
        self.id_ = id

class ObjectEquivalenceList(stix111.maec.EntityList):
    _binding_class = package_binding.ObjectEquivalenceListType
    _namespace = _namespace
    object_equivalence = fields.TypedField("Object_Equivalence", ObjectEquivalence, multiple=True)