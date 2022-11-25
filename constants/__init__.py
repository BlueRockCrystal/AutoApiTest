#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants.service_name import _AdServices
from constants.api_ad import _AdApi


class ServiceNames:
    """微服务项目名常量
    需要和~/config/{dir_name}/api.ini文件路径中的dir_name保持一致
    需要和~/config/host.ini文件中的每个段落中的key保持一致
    """
    ad = _AdServices


class ApiNames:
    """接口名常量
    需要和~/config/{dir_name}/api.ini文件中的接口名称保持一致
    """
    ad = _AdApi
