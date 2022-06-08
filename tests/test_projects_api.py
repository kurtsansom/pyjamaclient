"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import unittest

import pyjama
from pyjama.api.projects_api import ProjectsApi  # noqa: E501


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_project(self):
        """Test case for add_project

        Create a new project  # noqa: E501
        """
        pass

    def test_get_project(self):
        """Test case for get_project

        Get the project with the specified ID  # noqa: E501
        """
        pass

    def test_get_project_item_types(self):
        """Test case for get_project_item_types

        Get all item types for the project with the specified ID  # noqa: E501
        """
        pass

    def test_get_project_tags(self):
        """Test case for get_project_tags

        Get all tags for the project with the specified ID  # noqa: E501
        """
        pass

    def test_get_projects(self):
        """Test case for get_projects

        Get all projects  # noqa: E501
        """
        pass

    def test_post_attachment(self):
        """Test case for post_attachment

        Create a new attachment in the project with the specified ID  # noqa: E501
        """
        pass

    def test_put_project(self):
        """Test case for put_project

        Update the project with the specified ID  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()