#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants import ServiceNames, ApiNames
from common.http_api.request import ServiceAPI


def test_case_1():
    print(ServiceNames.ad.gateway)
    print(ApiNames.ad.gateway.user_info)
    api = ServiceAPI(ServiceNames.ad.gateway, ApiNames.ad.gateway.user_info)
    resp = api.call(timeout_assert_ms=100000)


def test_case_2():
    api = ServiceAPI(ServiceNames.ad.gateway, ApiNames.ad.gateway.ping)
    resp = api.call(timeout_assert_ms=11000)
