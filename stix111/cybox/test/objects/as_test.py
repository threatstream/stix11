# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix111.mixbox import u

from cybox.objects.as_object import AutonomousSystem
from cybox.test.objects import ObjectTestCase


class TestAccount(ObjectTestCase, unittest.TestCase):
    object_type = "ASObjectType"
    klass = AutonomousSystem

    _full_dict = {
        'number': 22222,
        'name': u("OMAHASTEAKS"),
        'handle': u("AS22222"),
        'regional_internet_registry': u("ARIN"),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
