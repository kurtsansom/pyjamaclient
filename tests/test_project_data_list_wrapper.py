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
from pyjama.model.project import Project

globals()["Link"] = Link
globals()["MetaListWrapper"] = MetaListWrapper
globals()["Project"] = Project
from pyjama.model.project_data_list_wrapper import ProjectDataListWrapper


class TestProjectDataListWrapper(unittest.TestCase):
    """ProjectDataListWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProjectDataListWrapper(self):
        """Test ProjectDataListWrapper"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProjectDataListWrapper()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()