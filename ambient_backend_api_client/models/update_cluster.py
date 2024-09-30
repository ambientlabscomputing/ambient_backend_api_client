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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ambient_backend_api_client.models.docker_cluster_data import DockerClusterData
from ambient_backend_api_client.models.resource_type_enum import ResourceTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class UpdateCluster(BaseModel):
    """
    UpdateCluster
    """ # noqa: E501
    id: Optional[StrictInt] = None
    name: StrictStr
    resource_type: Optional[ResourceTypeEnum] = None
    description: Optional[StrictStr] = None
    org_id: Optional[StrictInt] = None
    user_id: Optional[StrictInt] = None
    tags: Optional[List[StrictStr]] = None
    docker_data: Optional[DockerClusterData] = None
    __properties: ClassVar[List[str]] = ["id", "name", "resource_type", "description", "org_id", "user_id", "tags", "docker_data"]

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
        """Create an instance of UpdateCluster from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of docker_data
        if self.docker_data:
            _dict['docker_data'] = self.docker_data.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if org_id (nullable) is None
        # and model_fields_set contains the field
        if self.org_id is None and "org_id" in self.model_fields_set:
            _dict['org_id'] = None

        # set to None if user_id (nullable) is None
        # and model_fields_set contains the field
        if self.user_id is None and "user_id" in self.model_fields_set:
            _dict['user_id'] = None

        # set to None if docker_data (nullable) is None
        # and model_fields_set contains the field
        if self.docker_data is None and "docker_data" in self.model_fields_set:
            _dict['docker_data'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateCluster from a dict"""
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
            "tags": obj.get("tags"),
            "docker_data": DockerClusterData.from_dict(obj["docker_data"]) if obj.get("docker_data") is not None else None
        })
        return _obj


