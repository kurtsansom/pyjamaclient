"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import unittest

import pyjama
from pyjama.api.itemtypes_api import ItemtypesApi  # noqa: E501


class TestItemtypesApi(unittest.TestCase):
    """ItemtypesApi unit test stubs"""

    def setUp(self):
        self.api = ItemtypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_item_type(self):
        """Test case for get_item_type

        Get the item type with the specified ID  # noqa: E501
        """
        pass

    def test_get_item_types(self):
        """Test case for get_item_types

        Get all item types  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
