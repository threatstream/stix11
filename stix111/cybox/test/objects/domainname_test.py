# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix111.mixbox.vendor.six import u

from stix111.cybox.objects.domain_name_object import DomainName
from stix111.cybox.test.objects import ObjectTestCase


class TestDomainName(ObjectTestCase, unittest.TestCase):
    object_type = "DomainNameObjectType"
    klass = DomainName

    _full_dict = {
        'type': u("FQDN"),
        'value': "www.example.com",
        'xsi:type': object_type,
    }

if __name__ == "__main__":
    unittest.main()
