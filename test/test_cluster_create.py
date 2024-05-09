# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ambient_backend_api_client.models.cluster_create import ClusterCreate

class TestClusterCreate(unittest.TestCase):
    """ClusterCreate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ClusterCreate:
        """Test ClusterCreate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ClusterCreate`
        """
        model = ClusterCreate()
        if include_optional:
            return ClusterCreate(
                name = '',
                resource_type = 'cluster',
                identifier = '3e880c1c-5fa7-414c-92b4-d58119c93ee7',
                owner_id = '',
                owner_type = 'individual',
                description = '',
                requests = [
                    ''
                    ],
                notifications = [
                    ''
                    ],
                role = 'cloud',
                architecture = 'arm64',
                nodes = [
                    ''
                    ],
                docker_swarm_attrs = None,
                site = '',
                manager_node = '',
                cluster_group = 'default',
                tags = [
                    ''
                    ]
            )
        else:
            return ClusterCreate(
                name = '',
                role = 'cloud',
                architecture = 'arm64',
                nodes = [
                    ''
                    ],
        )
        """

    def testClusterCreate(self):
        """Test ClusterCreate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
