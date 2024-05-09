# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ambient_backend_api_client.api.clusters_api import ClustersApi


class TestClustersApi(unittest.TestCase):
    """ClustersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ClustersApi()

    def tearDown(self) -> None:
        pass

    def test_create_cluster_clusters_post(self) -> None:
        """Test case for create_cluster_clusters_post

        Create Cluster
        """
        pass

    def test_delete_cluster_clusters_cluster_id_delete(self) -> None:
        """Test case for delete_cluster_clusters_cluster_id_delete

        Delete Cluster
        """
        pass

    def test_deploy_cluster_clusters_cluster_id_deployments_post(self) -> None:
        """Test case for deploy_cluster_clusters_cluster_id_deployments_post

        Deploy Cluster
        """
        pass

    def test_get_cluster_clusters_cluster_id_get(self) -> None:
        """Test case for get_cluster_clusters_cluster_id_get

        Get Cluster
        """
        pass

    def test_get_cluster_deployments_clusters_cluster_id_deployments_get(self) -> None:
        """Test case for get_cluster_deployments_clusters_cluster_id_deployments_get

        Get Cluster Deployments
        """
        pass

    def test_get_clusters_clusters_get(self) -> None:
        """Test case for get_clusters_clusters_get

        Get Clusters
        """
        pass

    def test_patch_cluster_clusters_cluster_id_patch(self) -> None:
        """Test case for patch_cluster_clusters_cluster_id_patch

        Patch Cluster
        """
        pass


if __name__ == '__main__':
    unittest.main()
