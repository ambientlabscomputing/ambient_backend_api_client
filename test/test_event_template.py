# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ambient_backend_api_client.models.event_template import EventTemplate

class TestEventTemplate(unittest.TestCase):
    """EventTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventTemplate:
        """Test EventTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventTemplate`
        """
        model = EventTemplate()
        if include_optional:
            return EventTemplate(
                root = '',
                event_label = 'TEST_LABEL',
                event_type = 'notification',
                resource_type = 'cluster',
                resource_id = '',
                action = 'create'
            )
        else:
            return EventTemplate(
                root = '',
                event_label = 'TEST_LABEL',
                event_type = 'notification',
                resource_type = 'cluster',
        )
        """

    def testEventTemplate(self):
        """Test EventTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
