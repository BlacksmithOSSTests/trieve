# coding: utf-8

"""
    Trieve API

    Trieve OpenAPI Specification. This document describes all of the operations available through the Trieve API.

    The version of the OpenAPI document: 0.11.8
    Contact: developers@trieve.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from trieve_py_client.models.search_ctr_metrics1 import SearchCTRMetrics1

class TestSearchCTRMetrics1(unittest.TestCase):
    """SearchCTRMetrics1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SearchCTRMetrics1:
        """Test SearchCTRMetrics1
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SearchCTRMetrics1`
        """
        model = SearchCTRMetrics1()
        if include_optional:
            return SearchCTRMetrics1(
                filter = trieve_py_client.models.search_analytics_filter.SearchAnalyticsFilter(
                    date_range = null, 
                    search_method = null, 
                    search_type = null, ),
                type = 'search_ctr_metrics'
            )
        else:
            return SearchCTRMetrics1(
                type = 'search_ctr_metrics',
        )
        """

    def testSearchCTRMetrics1(self):
        """Test SearchCTRMetrics1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()