# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix111.mixbox.vendor.six import u

from stix111.cybox.objects.user_account_object import UserAccount
from stix111.cybox.test.objects import ObjectTestCase


class TestUserAccount(ObjectTestCase, unittest.TestCase):
    object_type = "UserAccountObjectType"
    klass = UserAccount

    _full_dict = {
        # Account-specific fields
        'disabled': False,
        'locked_out': True,
        'description': u('An account'),
        'domain': u('ADMIN'),
        # UserAccount-specific fields
        # (cannot test group_list of privilege_list since
        # they are abstract)
        'password_required': True,
        'full_name': u("Guido van Rossum"),
        'home_directory': u("/home/guido/"),
        'last_login': "2001-01-01T06:56:50+04:00",
        'script_path': u("/bin/bash"),
        'username': u("guido"),
        'user_password_age': u("P90D"),
        'xsi:type': object_type,
    }


if __name__ == "__main__":
    unittest.main()
