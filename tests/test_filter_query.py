"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pyjama
from pyjama.model.filter_order_rule import FilterOrderRule
from pyjama.model.filter_rule import FilterRule

globals()["FilterOrderRule"] = FilterOrderRule
globals()["FilterRule"] = FilterRule
from pyjama.model.filter_query import FilterQuery


class TestFilterQuery(unittest.TestCase):
    """FilterQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFilterQuery(self):
        """Test FilterQuery"""
        # FIXME: construct object with mandatory attributes with example values
        # model = FilterQuery()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
