"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pyjama
from pyjama.model.link import Link
from pyjama.model.meta_wrapper import MetaWrapper
from pyjama.model.versioned_test_run import VersionedTestRun

globals()["Link"] = Link
globals()["MetaWrapper"] = MetaWrapper
globals()["VersionedTestRun"] = VersionedTestRun
from pyjama.model.versioned_test_run_data_wrapper import VersionedTestRunDataWrapper


class TestVersionedTestRunDataWrapper(unittest.TestCase):
    """VersionedTestRunDataWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVersionedTestRunDataWrapper(self):
        """Test VersionedTestRunDataWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VersionedTestRunDataWrapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()