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
from pyjama.model.meta_list_wrapper import MetaListWrapper
from pyjama.model.release import Release

globals()["Link"] = Link
globals()["MetaListWrapper"] = MetaListWrapper
globals()["Release"] = Release
from pyjama.model.release_data_list_wrapper import ReleaseDataListWrapper


class TestReleaseDataListWrapper(unittest.TestCase):
    """ReleaseDataListWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testReleaseDataListWrapper(self):
        """Test ReleaseDataListWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ReleaseDataListWrapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
