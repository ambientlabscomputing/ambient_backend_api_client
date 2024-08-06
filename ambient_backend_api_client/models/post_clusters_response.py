# coding: utf-8

"""
    Ambient API

     This API provides access to Ambient services. It is designed to be used by Ambient applications and services. 

    The version of the OpenAPI document: 0.3.2
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
from ambient_backend_api_client.models.cluster import Cluster
from typing import Optional, Set
from typing_extensions import Self

class PostClustersResponse(BaseModel):
    """
    PostClustersResponse
    """ # noqa: E501
    request_id: StrictInt
    requested_ts: Optional[StrictStr] = '2024-08-05T19:53:47.274973'
    location_root: Optional[StrictStr] = 'http://localhost:8001/requests/'
    refresh_interval: Optional[StrictInt] = 10
    location: Optional[StrictStr] = None
    cluster: Cluster
    __properties: ClassVar[List[str]] = ["request_id", "requested_ts", "location_root", "refresh_interval", "location", "cluster"]

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
        """Create an instance of PostClustersResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cluster
        if self.cluster:
            _dict['cluster'] = self.cluster.to_dict()
        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostClustersResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "request_id": obj.get("request_id"),
            "requested_ts": obj.get("requested_ts") if obj.get("requested_ts") is not None else '2024-08-05T19:53:47.274973',
            "location_root": obj.get("location_root") if obj.get("location_root") is not None else 'http://localhost:8001/requests/',
            "refresh_interval": obj.get("refresh_interval") if obj.get("refresh_interval") is not None else 10,
            "location": obj.get("location"),
            "cluster": Cluster.from_dict(obj["cluster"]) if obj.get("cluster") is not None else None
        })
        return _obj


