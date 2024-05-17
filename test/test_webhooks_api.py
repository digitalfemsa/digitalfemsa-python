# coding: utf-8

"""
    Femsa API

    Femsa sdk

    The version of the OpenAPI document: 2.1.0
    Contact: engineering@femsa.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from digitalfemsa.api.webhooks_api import WebhooksApi


class TestWebhooksApi(unittest.TestCase):
    """WebhooksApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WebhooksApi()

    def tearDown(self) -> None:
        pass

    def test_create_webhook(self) -> None:
        """Test case for create_webhook

        Create Webhook
        """
        pass

    def test_delete_webhook(self) -> None:
        """Test case for delete_webhook

        Delete Webhook
        """
        pass

    def test_get_webhook(self) -> None:
        """Test case for get_webhook

        Get Webhook
        """
        pass

    def test_get_webhooks(self) -> None:
        """Test case for get_webhooks

        Get List of Webhooks
        """
        pass

    def test_test_webhook(self) -> None:
        """Test case for test_webhook

        Test Webhook
        """
        pass

    def test_update_webhook(self) -> None:
        """Test case for update_webhook

        Update Webhook
        """
        pass


if __name__ == '__main__':
    unittest.main()
