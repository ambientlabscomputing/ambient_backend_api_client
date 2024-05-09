# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ambient_backend_api_client.models.notification_list import NotificationList

class TestNotificationList(unittest.TestCase):
    """NotificationList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotificationList:
        """Test NotificationList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotificationList`
        """
        model = NotificationList()
        if include_optional:
            return NotificationList(
                count = 56,
                timestamp = 'Wed May  8 19:55:26 2024',
                results = [
                    ambient_backend_api_client.models.notification.Notification(
                        name = '', 
                        resource_type = null, 
                        identifier = '', 
                        owner_id = '', 
                        owner_type = 'individual', 
                        description = '', 
                        requests = [
                            ''
                            ], 
                        notifications = [
                            ''
                            ], 
                        message = '', 
                        severity = 'info', 
                        target_resource_id = '', 
                        target_resource_type = 'cluster', 
                        timestamp = 56, 
                        read = True, )
                    ]
            )
        else:
            return NotificationList(
                count = 56,
                results = [
                    ambient_backend_api_client.models.notification.Notification(
                        name = '', 
                        resource_type = null, 
                        identifier = '', 
                        owner_id = '', 
                        owner_type = 'individual', 
                        description = '', 
                        requests = [
                            ''
                            ], 
                        notifications = [
                            ''
                            ], 
                        message = '', 
                        severity = 'info', 
                        target_resource_id = '', 
                        target_resource_type = 'cluster', 
                        timestamp = 56, 
                        read = True, )
                    ],
        )
        """

    def testNotificationList(self):
        """Test NotificationList"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
