# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ambient_backend_api_client.api.nodes_api import NodesApi


class TestNodesApi(unittest.TestCase):
    """NodesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NodesApi()

    def tearDown(self) -> None:
        pass

    def test_authorize_node_nodes_node_id_authorize_post(self) -> None:
        """Test case for authorize_node_nodes_node_id_authorize_post

        Authorize Node
        """
        pass

    def test_create_node_nodes_post(self) -> None:
        """Test case for create_node_nodes_post

        Create Node
        """
        pass

    def test_delete_node_nodes_node_id_delete(self) -> None:
        """Test case for delete_node_nodes_node_id_delete

        Delete Node
        """
        pass

    def test_get_node_nodes_node_id_get(self) -> None:
        """Test case for get_node_nodes_node_id_get

        Get Node
        """
        pass

    def test_get_nodes_nodes_get(self) -> None:
        """Test case for get_nodes_nodes_get

        Get Nodes
        """
        pass

    def test_refresh_node_token_nodes_node_id_refresh_token_post(self) -> None:
        """Test case for refresh_node_token_nodes_node_id_refresh_token_post

        Refresh Node Token
        """
        pass

    def test_request_new_auth_nodes_node_id_auth_post(self) -> None:
        """Test case for request_new_auth_nodes_node_id_auth_post

        Request New Auth
        """
        pass

    def test_update_node_nodes_node_id_patch(self) -> None:
        """Test case for update_node_nodes_node_id_patch

        Update Node
        """
        pass


if __name__ == '__main__':
    unittest.main()
