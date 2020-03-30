# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix111.mixbox.vendor.six import u

from stix111.cybox.core import Observables
from stix111.cybox.objects.link_object import Link
from stix111.cybox.objects.uri_object import URI
from stix111.cybox.test.objects import ObjectTestCase


class TestLink(ObjectTestCase, unittest.TestCase):
    object_type = "LinkObjectType"
    klass = Link

    _full_dict = {
        'value': u("http://www.example.com"),
        'type': URI.TYPE_URL,
        'url_label': u("Click Here!"),
        'xsi:type': object_type,
    }

    # https://github.com/CybOXProject/python-cybox/issues/202
    def test_correct_namespace_output(self):
        link = Link()
        link.value = u("https://www.example.com")

        xml = Observables(link).to_xml()
        self.assertTrue(b"cybox:Properties" in xml)
        self.assertTrue(b"LinkObj:Properties" not in xml)


if __name__ == "__main__":
    unittest.main()