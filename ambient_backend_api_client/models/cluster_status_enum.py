# coding: utf-8

"""
    Ambient API

     This API provides access to Ambient services. It is designed to be used by Ambient applications and services. 

    The version of the OpenAPI document: 0.5.2
    Contact: jose@ambientlabscomputing.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ClusterStatusEnum(str, Enum):
    """
    ClusterStatusEnum
    """

    """
    allowed enum values
    """
    CREATED = 'created'
    ACTIVE = 'active'
    ERROR = 'error'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ClusterStatusEnum from a JSON string"""
        return cls(json.loads(json_str))


