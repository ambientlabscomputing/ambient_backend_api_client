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
from ambient_backend_api_client.models.ambient_action_enum import AmbientActionEnum
from ambient_backend_api_client.models.ambient_event_type_enum import AmbientEventTypeEnum
from ambient_backend_api_client.models.event_label import EventLabel
from ambient_backend_api_client.models.resource_type_enum import ResourceTypeEnum
from typing import Optional, Set
from typing_extensions import Self

class Event(BaseModel):
    """
    Event
    """ # noqa: E501
    root: StrictStr
    event_label: EventLabel
    event_type: AmbientEventTypeEnum
    resource_type: ResourceTypeEnum
    resource_id: StrictStr
    action: Optional[AmbientActionEnum] = None
    timestamp: Union[StrictFloat, StrictInt]
    event_data: Dict[str, Any]
    request_id: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["root", "event_label", "event_type", "resource_type", "resource_id", "action", "timestamp", "event_data", "request_id"]

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
        """Create an instance of Event from a JSON string"""
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
        # set to None if action (nullable) is None
        # and model_fields_set contains the field
        if self.action is None and "action" in self.model_fields_set:
            _dict['action'] = None

        # set to None if request_id (nullable) is None
        # and model_fields_set contains the field
        if self.request_id is None and "request_id" in self.model_fields_set:
            _dict['request_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Event from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "root": obj.get("root"),
            "event_label": obj.get("event_label"),
            "event_type": obj.get("event_type"),
            "resource_type": obj.get("resource_type"),
            "resource_id": obj.get("resource_id"),
            "action": obj.get("action"),
            "timestamp": obj.get("timestamp"),
            "event_data": obj.get("event_data"),
            "request_id": obj.get("request_id")
        })
        return _obj


