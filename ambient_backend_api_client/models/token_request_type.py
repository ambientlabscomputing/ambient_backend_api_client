# coding: utf-8

"""
    Ambient API

     This API provides access to Ambient services. It is designed to be used by Ambient applications and services. 

    The version of the OpenAPI document: 0.7.0
    Contact: jose@ambientlabscomputing.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TokenRequestType(str, Enum):
    """
    TokenRequestType
    """

    """
    allowed enum values
    """
    NODE_REFRESH_TOKEN = 'node_refresh_token'
    NODE_ACCESS_TOKEN = 'node_access_token'
    USER_API_TOKEN = 'user_api_token'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TokenRequestType from a JSON string"""
        return cls(json.loads(json_str))


