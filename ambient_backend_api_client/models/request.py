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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from ambient_backend_api_client.models.owner_type_enum import OwnerTypeEnum
from ambient_backend_api_client.models.request_status_enum import RequestStatusEnum
from ambient_backend_api_client.models.resource_type_enum import ResourceTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class Request(BaseModel):
    """
    Request
    """ # noqa: E501
    name: StrictStr
    resource_type: Optional[ResourceTypeEnum] = None
    identifier: StrictStr
    owner_id: StrictStr
    owner_type: OwnerTypeEnum
    description: Optional[StrictStr] = None
    requests: Optional[List[StrictStr]] = None
    notifications: Optional[List[StrictStr]] = None
    status: Optional[RequestStatusEnum] = None
    error: Optional[StrictStr] = None
    requested_ts: Optional[Union[StrictFloat, StrictInt]] = 1.715219726437265E9
    started_ts: Optional[Union[StrictFloat, StrictInt]] = None
    failed_ts: Optional[Union[StrictFloat, StrictInt]] = None
    completed_ts: Optional[Union[StrictFloat, StrictInt]] = None
    notes: Optional[List[StrictStr]] = None
    data: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["name", "resource_type", "identifier", "owner_id", "owner_type", "description", "requests", "notifications", "status", "error", "requested_ts", "started_ts", "failed_ts", "completed_ts", "notes", "data"]

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
        """Create an instance of Request from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if error (nullable) is None
        # and model_fields_set contains the field
        if self.error is None and "error" in self.model_fields_set:
            _dict['error'] = None

        # set to None if started_ts (nullable) is None
        # and model_fields_set contains the field
        if self.started_ts is None and "started_ts" in self.model_fields_set:
            _dict['started_ts'] = None

        # set to None if failed_ts (nullable) is None
        # and model_fields_set contains the field
        if self.failed_ts is None and "failed_ts" in self.model_fields_set:
            _dict['failed_ts'] = None

        # set to None if completed_ts (nullable) is None
        # and model_fields_set contains the field
        if self.completed_ts is None and "completed_ts" in self.model_fields_set:
            _dict['completed_ts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Request from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "resource_type": obj.get("resource_type"),
            "identifier": obj.get("identifier"),
            "owner_id": obj.get("owner_id"),
            "owner_type": obj.get("owner_type"),
            "description": obj.get("description"),
            "requests": obj.get("requests"),
            "notifications": obj.get("notifications"),
            "status": obj.get("status"),
            "error": obj.get("error"),
            "requested_ts": obj.get("requested_ts") if obj.get("requested_ts") is not None else 1.715219726437265E9,
            "started_ts": obj.get("started_ts"),
            "failed_ts": obj.get("failed_ts"),
            "completed_ts": obj.get("completed_ts"),
            "notes": obj.get("notes"),
            "data": obj.get("data")
        })
        return _obj


