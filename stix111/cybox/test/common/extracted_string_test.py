# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import binascii
import unittest

from stix111.mixbox.vendor import six
from stix111.mixbox.vendor.six import u

from stix111.cybox.common import ExtractedString, Hash
from stix111.cybox.test import EntityTestCase

STRING = u("This is a string")
HEX_STRING = six.text_type(binascii.hexlify(STRING.encode("ascii")))

class TestExtractedString(EntityTestCase, unittest.TestCase):
    klass = ExtractedString

    _full_dict = {
        'encoding': u("UTF-8"),
        'string_value': STRING,
        'byte_string_value': HEX_STRING,
        'hashes': [{'type': Hash.TYPE_MD5}],
        'address': u("1a2b"),
        'length': len(STRING),
        'language': u("English"),
        'english_translation': STRING,
    }


if __name__ == "__main__":
    unittest.main()