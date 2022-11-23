#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.base.config_init import _LogConfig


class ProjectConfig:
    """project config init class
    project base config, read by ~/config/conf.ini
    """
    log = _LogConfig()

