"""
    Jama REST API

    This is the documentation for the Jama REST API.  # noqa: E501

    The version of the OpenAPI document: latest
    Generated by: https://openapi-generator.tech
"""


import unittest

import pyjama
from pyjama.api.attachments_api import AttachmentsApi  # noqa: E501


class TestAttachmentsApi(unittest.TestCase):
    """AttachmentsApi unit test stubs"""

    def setUp(self):
        self.api = AttachmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_download_file(self):
        """Test case for download_file

        Download attachment file from the attachment with the specified ID  # noqa: E501
        """
        pass

    def test_get_attachment(self):
        """Test case for get_attachment

        Get the attachment with the specified ID  # noqa: E501
        """
        pass

    def test_get_attachment_comments(self):
        """Test case for get_attachment_comments

        Get all comments for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_attachment_lock(self):
        """Test case for get_attachment_lock

        Get the locked state, last locked date, and last locked by user for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_attachment_version(self):
        """Test case for get_attachment_version

        Get the  snapshot of the attachment at the specified version  # noqa: E501
        """
        pass

    def test_get_attachment_versioned(self):
        """Test case for get_attachment_versioned

        Get the numbered version for the item with the specified ID  # noqa: E501
        """
        pass

    def test_get_attachment_versions(self):
        """Test case for get_attachment_versions

        Get all versions for the item with the specified ID  # noqa: E501
        """
        pass

    def test_update_attachment_lock(self):
        """Test case for update_attachment_lock

        Update the locked state of the item with the specified ID  # noqa: E501
        """
        pass

    def test_upload_file(self):
        """Test case for upload_file

        Upload attachment file to the attachment with the specified ID  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
