# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.11.8
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ApiKeyRespBody(BaseModel):
    """
    ApiKeyRespBody
    """ # noqa: E501
    created_at: datetime
    dataset_ids: Optional[List[StrictStr]] = None
    id: StrictStr
    name: StrictStr
    organization_ids: Optional[List[StrictStr]] = None
    role: StrictInt
    updated_at: datetime
    user_id: StrictStr
    __properties: ClassVar[List[str]] = ["created_at", "dataset_ids", "id", "name", "organization_ids", "role", "updated_at", "user_id"]

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
        """Create an instance of ApiKeyRespBody from a JSON string"""
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
        # set to None if dataset_ids (nullable) is None
        # and model_fields_set contains the field
        if self.dataset_ids is None and "dataset_ids" in self.model_fields_set:
            _dict['dataset_ids'] = None

        # set to None if organization_ids (nullable) is None
        # and model_fields_set contains the field
        if self.organization_ids is None and "organization_ids" in self.model_fields_set:
            _dict['organization_ids'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiKeyRespBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "dataset_ids": obj.get("dataset_ids"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "organization_ids": obj.get("organization_ids"),
            "role": obj.get("role"),
            "updated_at": obj.get("updated_at"),
            "user_id": obj.get("user_id")
        })
        return _obj

