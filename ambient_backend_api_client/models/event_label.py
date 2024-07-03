# coding: utf-8

"""
    Ambient API

     This API provides access to Ambient services. It is designed to be used by Ambient applications and services. 

    The version of the OpenAPI document: 0.3.0
    Contact: jose@ambientlabscomputing.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class EventLabel(str, Enum):
    """
    EventLabel
    """

    """
    allowed enum values
    """
    TEST_LABEL = 'TEST_LABEL'
    ERROR = 'ERROR'
    NODE_ALIVE = 'NODE_ALIVE'
    NODE_CREATED = 'NODE_CREATED'
    NODE_DELETED = 'NODE_DELETED'
    NODE_UPDATED = 'NODE_UPDATED'
    NEW_CLUSTER = 'NEW_CLUSTER'
    CLUSTER_INITIALIZED = 'CLUSTER_INITIALIZED'
    CLUSTER_ACTIVE = 'CLUSTER_ACTIVE'
    REQUEST_NODE_JOIN_CLUSTER = 'REQUEST_NODE_JOIN_CLUSTER'
    NODE_JOINED_CLUSTER = 'NODE_JOINED_CLUSTER'
    SERVICE_DEPLOYMENT_REQUESTED = 'SERVICE_DEPLOYMENT_REQUESTED'
    SERVICE_REQUEST_ACKNOWLEDGED = 'SERVICE_REQUEST_ACKNOWLEDGED'
    SERVICE_REQUEST_COMPLETED = 'SERVICE_REQUEST_COMPLETED'
    SERVICE_DEPLOYED = 'SERVICE_DEPLOYED'
    SERVICE_DEPLOYMENT_FAILED = 'SERVICE_DEPLOYMENT_FAILED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EventLabel from a JSON string"""
        return cls(json.loads(json_str))


