# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ambient_backend_api_client.models.auth0_device_code_response import Auth0DeviceCodeResponse
from ambient_backend_api_client.models.models_node_status_enum import ModelsNodeStatusEnum
from ambient_backend_api_client.models.network_interface import NetworkInterface
from ambient_backend_api_client.models.node_architecture_enum import NodeArchitectureEnum
from ambient_backend_api_client.models.node_role_enum import NodeRoleEnum
from ambient_backend_api_client.models.resource_type_enum import ResourceTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class Node(BaseModel):
    """
    Node
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: StrictStr
    resource_type: Optional[ResourceTypeEnum] = None
    description: Optional[StrictStr] = None
    org_id: StrictInt
    user_id: StrictInt
    role: NodeRoleEnum
    architecture: NodeArchitectureEnum
    interfaces: Optional[List[NetworkInterface]] = None
    last_seen: Optional[StrictStr] = None
    status: ModelsNodeStatusEnum
    identifier: Optional[StrictStr] = None
    cluster: Optional[StrictStr] = None
    authorization: Optional[Auth0DeviceCodeResponse] = None
    __properties: ClassVar[List[str]] = ["id", "name", "resource_type", "description", "org_id", "user_id", "role", "architecture", "interfaces", "last_seen", "status", "identifier", "cluster", "authorization"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Node from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in interfaces (list)
        _items = []
        if self.interfaces:
            for _item in self.interfaces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['interfaces'] = _items
        # override the default output from pydantic by calling `to_dict()` of authorization
        if self.authorization:
            _dict['authorization'] = self.authorization.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if interfaces (nullable) is None
        # and model_fields_set contains the field
        if self.interfaces is None and "interfaces" in self.model_fields_set:
            _dict['interfaces'] = None

        # set to None if last_seen (nullable) is None
        # and model_fields_set contains the field
        if self.last_seen is None and "last_seen" in self.model_fields_set:
            _dict['last_seen'] = None

        # set to None if identifier (nullable) is None
        # and model_fields_set contains the field
        if self.identifier is None and "identifier" in self.model_fields_set:
            _dict['identifier'] = None

        # set to None if cluster (nullable) is None
        # and model_fields_set contains the field
        if self.cluster is None and "cluster" in self.model_fields_set:
            _dict['cluster'] = None

        # set to None if authorization (nullable) is None
        # and model_fields_set contains the field
        if self.authorization is None and "authorization" in self.model_fields_set:
            _dict['authorization'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Node from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "resource_type": obj.get("resource_type"),
            "description": obj.get("description"),
            "org_id": obj.get("org_id"),
            "user_id": obj.get("user_id"),
            "role": obj.get("role"),
            "architecture": obj.get("architecture"),
            "interfaces": [NetworkInterface.from_dict(_item) for _item in obj["interfaces"]] if obj.get("interfaces") is not None else None,
            "last_seen": obj.get("last_seen"),
            "status": obj.get("status"),
            "identifier": obj.get("identifier"),
            "cluster": obj.get("cluster"),
            "authorization": Auth0DeviceCodeResponse.from_dict(obj["authorization"]) if obj.get("authorization") is not None else None
        })
        return _obj


