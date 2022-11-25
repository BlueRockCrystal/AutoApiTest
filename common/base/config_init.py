#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from common.base.project_env import PROJECT_PATH
from common.read_ini import project_config

all_config = project_config()


class _LogConfig:
    """project log config class
    """
    _console_handler = all_config.get('log_config').get('console_handler')
    if _console_handler == 'true' or _console_handler is None or _console_handler == '':
        console_handler = True
    elif _console_handler == 'false':
        console_handler = False
    else:
        raise Exception('~/config/conf.ini,[log_config].console_handler illegal!')

    _file_handler = all_config.get('log_config').get('file_handler')
    if _file_handler == 'true' or _file_handler is None or _file_handler == '':
        file_handler = True
    elif _file_handler == 'false':
        file_handler = False
    else:
        raise Exception('~/config/conf.ini,[log_config].file_handler illegal!')

    if not file_handler and not console_handler:
        raise Exception('~/config/conf.ini,[log_config].file_handler and .console_handler False!')

    _file_path = all_config.get('log_config').get('file_path')
    if _file_path == '' or _file_handler is None:
        file_path = os.path.join(PROJECT_PATH, 'logs/')
    else:
        file_path = _file_path

    _file_name = all_config.get('log_config').get('file_name')
    if _file_name == '' or _file_handler is None:
        file_name = ''
    else:
        file_name = _file_name

    _level = all_config.get('log_config').get('level')
    if _level == 'debug' or _level is None or _level == '':
        level = logging.DEBUG
    elif _level == 'info':
        level = logging.INFO
    elif _level == 'warning':
        level = logging.WARNING
    elif _level == 'error':
        level = logging.ERROR
    elif _level == 'critical':
        level = logging.CRITICAL
    else:
        raise Exception('~/config/conf.ini,[log_config].level illegal!')

    _pid = all_config.get('log_config').get('thread_info')
    if _pid == 'true' or _pid is None or _pid == '':
        thread_info = True
    elif _pid == 'false':
        thread_info = False
    else:
        raise Exception('~/config/conf.ini,[log_config].thread_info illegal!')

    _color = all_config.get('log_config').get('color')
    if _color == 'true' or _color is None or _color == '':
        color = True
    elif _color == 'false':
        color = False
    else:
        raise Exception('~/config/conf.ini,[log_config].color illegal!')
