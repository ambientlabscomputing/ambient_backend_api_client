# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ambient_backend_api_client.models.service import Service

class TestService(unittest.TestCase):
    """Service unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Service:
        """Test Service
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Service`
        """
        model = Service()
        if include_optional:
            return Service(
                name = '',
                resource_type = 'cluster',
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
                image = '',
                replicas = 56,
                cluster_groups = [
                    ''
                    ],
                tags = [
                    ''
                    ],
                clusters = [
                    ''
                    ],
                ports = [
                    ''
                    ],
                compose_location = '',
                state = 10,
                status = 'active'
            )
        else:
            return Service(
                name = '',
                image = '',
                replicas = 56,
                status = 'active',
        )
        """

    def testService(self):
        """Test Service"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
