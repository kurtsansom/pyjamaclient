"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import unittest

import pyjama
from pyjama.api.activities_api import ActivitiesApi  # noqa: E501


class TestActivitiesApi(unittest.TestCase):
    """ActivitiesApi unit test stubs"""

    def setUp(self):
        self.api = ActivitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_activit_affected_items(self):
        """Test case for get_activit_affected_items

        Get all items affected by the activity with the specified ID  # noqa: E501
        """
        pass

    def test_get_activities(self):
        """Test case for get_activities

        Get all activities in the project with the specified ID  # noqa: E501
        """
        pass

    def test_get_activity(self):
        """Test case for get_activity

        Get the activity with the specified ID  # noqa: E501
        """
        pass

    def test_restore_items(self):
        """Test case for restore_items

        Restore item(s) associated with a delete activity.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()