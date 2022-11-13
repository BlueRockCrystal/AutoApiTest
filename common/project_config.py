#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging

from common.project_variable import PROJECT_PATH
from common.read_ini import project_base_config
from common.error_msg import ConfigError

all_config = project_base_config()


class _ProjectLogConfig:
    """project log config class
    """
    _console_handler = all_config.get('log_config').get('log_console_handler')
    if _console_handler == 'true' or _console_handler is None or _console_handler == '':
        log_console_handler = True
    elif _console_handler == 'false':
        log_console_handler = False
    else:
        raise ValueError(ConfigError.console_handler)

    _file_handler = all_config.get('log_config').get('log_file_handler')
    if _file_handler == 'true' or _file_handler is None or _file_handler == '':
        log_file_handler = True
    elif _file_handler == 'false':
        log_file_handler = False
    else:
        raise ValueError(ConfigError.file_handler)

    if not log_file_handler and not log_console_handler:
        raise ValueError(ConfigError.log_handler_none)

    _file_path = all_config.get('log_config').get('log_file_path')
    if _file_path == '' or _file_handler is None:
        log_file_path = os.path.join(PROJECT_PATH, 'logs/')
    else:
        log_file_path = _file_path
    _level = all_config.get('log_config').get('log_level')
    if _level == 'debug' or _level is None or _level == '':
        log_level = logging.DEBUG
    elif _level == 'info':
        log_level = logging.INFO
    elif _level == 'warning':
        log_level = logging.WARNING
    elif _level == 'error':
        log_level = logging.ERROR
    elif _level == 'critical':
        log_level = logging.CRITICAL
    else:
        raise ValueError(ConfigError.log_level)

    _pid = all_config.get('log_config').get('pid_tid_info')
    if _pid == 'true' or _pid is None or _pid == '':
        pid_tid_info = True
    elif _pid == 'false':
        pid_tid_info = False
    else:
        raise ValueError(ConfigError.pid_tid_info)


class ProjectConfig:
    """project config class
    project base config, read by ~/config/conf.ini
    """
    log_config = _ProjectLogConfig()

