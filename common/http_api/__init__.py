#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.http_api.request import ServiceAPI


def call(service, api, **kwargs):
    """

    :param service:
    :param api:
    :param kwargs:
    :return:
    """
    with ServiceAPI(service, api).call(**kwargs):
        pass

