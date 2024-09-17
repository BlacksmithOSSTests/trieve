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
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from trieve_py_client.models.count_queries import CountQueries
from trieve_py_client.models.head_queries1 import HeadQueries1
from trieve_py_client.models.latency_graph import LatencyGraph
from trieve_py_client.models.low_confidence_queries import LowConfidenceQueries
from trieve_py_client.models.no_result_queries import NoResultQueries
from trieve_py_client.models.popular_filters1 import PopularFilters1
from trieve_py_client.models.query_details import QueryDetails
from trieve_py_client.models.search_metrics import SearchMetrics
from trieve_py_client.models.search_queries import SearchQueries
from trieve_py_client.models.search_usage_graph import SearchUsageGraph
from pydantic import StrictStr, Field
from typing import Union, List, Optional, Dict
from typing_extensions import Literal, Self

SEARCHANALYTICS_ONE_OF_SCHEMAS = ["CountQueries", "HeadQueries1", "LatencyGraph", "LowConfidenceQueries", "NoResultQueries", "PopularFilters1", "QueryDetails", "SearchMetrics", "SearchQueries", "SearchUsageGraph"]

class SearchAnalytics(BaseModel):
    """
    SearchAnalytics
    """
    # data type: LatencyGraph
    oneof_schema_1_validator: Optional[LatencyGraph] = None
    # data type: SearchUsageGraph
    oneof_schema_2_validator: Optional[SearchUsageGraph] = None
    # data type: SearchMetrics
    oneof_schema_3_validator: Optional[SearchMetrics] = None
    # data type: HeadQueries1
    oneof_schema_4_validator: Optional[HeadQueries1] = None
    # data type: LowConfidenceQueries
    oneof_schema_5_validator: Optional[LowConfidenceQueries] = None
    # data type: NoResultQueries
    oneof_schema_6_validator: Optional[NoResultQueries] = None
    # data type: SearchQueries
    oneof_schema_7_validator: Optional[SearchQueries] = None
    # data type: CountQueries
    oneof_schema_8_validator: Optional[CountQueries] = None
    # data type: QueryDetails
    oneof_schema_9_validator: Optional[QueryDetails] = None
    # data type: PopularFilters1
    oneof_schema_10_validator: Optional[PopularFilters1] = None
    actual_instance: Optional[Union[CountQueries, HeadQueries1, LatencyGraph, LowConfidenceQueries, NoResultQueries, PopularFilters1, QueryDetails, SearchMetrics, SearchQueries, SearchUsageGraph]] = None
    one_of_schemas: List[str] = Field(default=Literal["CountQueries", "HeadQueries1", "LatencyGraph", "LowConfidenceQueries", "NoResultQueries", "PopularFilters1", "QueryDetails", "SearchMetrics", "SearchQueries", "SearchUsageGraph"])

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = SearchAnalytics.model_construct()
        error_messages = []
        match = 0
        # validate data type: LatencyGraph
        if not isinstance(v, LatencyGraph):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LatencyGraph`")
        else:
            match += 1
        # validate data type: SearchUsageGraph
        if not isinstance(v, SearchUsageGraph):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SearchUsageGraph`")
        else:
            match += 1
        # validate data type: SearchMetrics
        if not isinstance(v, SearchMetrics):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SearchMetrics`")
        else:
            match += 1
        # validate data type: HeadQueries1
        if not isinstance(v, HeadQueries1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `HeadQueries1`")
        else:
            match += 1
        # validate data type: LowConfidenceQueries
        if not isinstance(v, LowConfidenceQueries):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LowConfidenceQueries`")
        else:
            match += 1
        # validate data type: NoResultQueries
        if not isinstance(v, NoResultQueries):
            error_messages.append(f"Error! Input type `{type(v)}` is not `NoResultQueries`")
        else:
            match += 1
        # validate data type: SearchQueries
        if not isinstance(v, SearchQueries):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SearchQueries`")
        else:
            match += 1
        # validate data type: CountQueries
        if not isinstance(v, CountQueries):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CountQueries`")
        else:
            match += 1
        # validate data type: QueryDetails
        if not isinstance(v, QueryDetails):
            error_messages.append(f"Error! Input type `{type(v)}` is not `QueryDetails`")
        else:
            match += 1
        # validate data type: PopularFilters1
        if not isinstance(v, PopularFilters1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PopularFilters1`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in SearchAnalytics with oneOf schemas: CountQueries, HeadQueries1, LatencyGraph, LowConfidenceQueries, NoResultQueries, PopularFilters1, QueryDetails, SearchMetrics, SearchQueries, SearchUsageGraph. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in SearchAnalytics with oneOf schemas: CountQueries, HeadQueries1, LatencyGraph, LowConfidenceQueries, NoResultQueries, PopularFilters1, QueryDetails, SearchMetrics, SearchQueries, SearchUsageGraph. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into LatencyGraph
        try:
            instance.actual_instance = LatencyGraph.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SearchUsageGraph
        try:
            instance.actual_instance = SearchUsageGraph.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SearchMetrics
        try:
            instance.actual_instance = SearchMetrics.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into HeadQueries1
        try:
            instance.actual_instance = HeadQueries1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LowConfidenceQueries
        try:
            instance.actual_instance = LowConfidenceQueries.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into NoResultQueries
        try:
            instance.actual_instance = NoResultQueries.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SearchQueries
        try:
            instance.actual_instance = SearchQueries.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CountQueries
        try:
            instance.actual_instance = CountQueries.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into QueryDetails
        try:
            instance.actual_instance = QueryDetails.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PopularFilters1
        try:
            instance.actual_instance = PopularFilters1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into SearchAnalytics with oneOf schemas: CountQueries, HeadQueries1, LatencyGraph, LowConfidenceQueries, NoResultQueries, PopularFilters1, QueryDetails, SearchMetrics, SearchQueries, SearchUsageGraph. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into SearchAnalytics with oneOf schemas: CountQueries, HeadQueries1, LatencyGraph, LowConfidenceQueries, NoResultQueries, PopularFilters1, QueryDetails, SearchMetrics, SearchQueries, SearchUsageGraph. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], CountQueries, HeadQueries1, LatencyGraph, LowConfidenceQueries, NoResultQueries, PopularFilters1, QueryDetails, SearchMetrics, SearchQueries, SearchUsageGraph]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

