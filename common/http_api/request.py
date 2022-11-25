#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.http_api.base import RequestTranslate, RequestClass


class ServiceAPI:
    """base service API request class
    """

    def __init__(self, service, api):
        """
        Init service API class
        :param service: service name
        :param api: api name
        """
        self.service = service
        self.api = api

    def call(self, uri_param=None, headers=None, params=None, body=None, default_uri_param=True,
             common_headers=True, default_headers=True, common_params=True, default_params=True,
             common_body=True, default_body=True,
             timeout_assert_ms=0, timecost_expect_ms=0):
        """
        http request call method
        :param uri_param:
        :param headers:
        :param params:
        :param body:
        :param default_uri_param:
        :param common_headers:
        :param default_headers:
        :param common_params:
        :param default_params:
        :param common_body:
        :param default_body:
        :param timeout_assert_ms: requests timeout params, ms
        :param timecost_expect_ms:  request timecost expect, ms
        :return:
        """
        req_class = RequestTranslate(dict(service=self.service, api=self.api,
                                          uri_param=uri_param, default_uri_param=default_uri_param,
                                          headers=headers, common_headers=common_headers,
                                          default_headers=default_headers,
                                          params=params, common_params=common_params,
                                          default_params=default_params,
                                          body=body, common_body=common_body,
                                          default_body=default_body,
                                          timeout_assert=timeout_assert_ms,
                                          timecost_expect=timecost_expect_ms))
        return RequestClass(req_class).send()



