#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.service_name import ServiceNameDemo
from constants.api_name import ApiServiceDemoApi
from common.http_api.request import ServiceAPI


def test_case_1():
    print(ServiceNameDemo.api_service_demo)
    print(ApiServiceDemoApi.user_info)
    api = ServiceAPI(ServiceNameDemo.api_service_demo, ApiServiceDemoApi.user_info)
    resp = api.call(timeout_assert_ms=100000)


def test_case_2():
    api = ServiceAPI(ServiceNameDemo.api_service_demo, ApiServiceDemoApi.ping)
    resp = api.call(timeout_assert_ms=11000)


def test_case_3():
    api = ServiceAPI(ServiceNameDemo.api_service_demo, ApiServiceDemoApi.ping)
    resp = api.call(default_params=False, timeout_assert_ms=11000)

