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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from trieve_py_client.models.chunk_metadata_string_tag_set import ChunkMetadataStringTagSet
from typing import Optional, Set
from typing_extensions import Self

class RagQueryEvent(BaseModel):
    """
    RagQueryEvent
    """ # noqa: E501
    created_at: StrictStr
    dataset_id: StrictStr
    id: StrictStr
    rag_type: StrictStr
    results: List[ChunkMetadataStringTagSet]
    search_id: StrictStr
    user_id: StrictStr
    user_message: StrictStr
    __properties: ClassVar[List[str]] = ["created_at", "dataset_id", "id", "rag_type", "results", "search_id", "user_id", "user_message"]

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
        """Create an instance of RagQueryEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RagQueryEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created_at": obj.get("created_at"),
            "dataset_id": obj.get("dataset_id"),
            "id": obj.get("id"),
            "rag_type": obj.get("rag_type"),
            "results": [ChunkMetadataStringTagSet.from_dict(_item) for _item in obj["results"]] if obj.get("results") is not None else None,
            "search_id": obj.get("search_id"),
            "user_id": obj.get("user_id"),
            "user_message": obj.get("user_message")
        })
        return _obj

