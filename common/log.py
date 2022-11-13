#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os.path
import sys
import inspect
from datetime import datetime
from logging import handlers
from functools import wraps

from common.project_config import ProjectConfig
from common.project_variable import PROJECT_NAME
from common.error_msg import ConfigError

_logger = logging.getLogger()
_logger.setLevel(ProjectConfig.log_config.log_level)


_fmt_str = '%(asctime)s-[%(levelname)s]'
if ProjectConfig.log_config.pid_tid_info:
    _fmt_str += '-[PID:%(process)d-TID:%(thread)d-%(threadName)s]'
_fmt_str += '-%(message)s'

_log_formatter = logging.Formatter(_fmt_str)

if ProjectConfig.log_config.log_console_handler:
    _ch = logging.StreamHandler(sys.stdout)
    _ch.setFormatter(_log_formatter)
    _logger.addHandler(_ch)

if ProjectConfig.log_config.log_file_handler:
    _log_file_path = ProjectConfig.log_config.log_file_path
    try:
        if not os.path.exists(_log_file_path):
            os.makedirs(_log_file_path)
    except Exception as e:
        raise ValueError(ConfigError.log_file_path)

    _file_name = os.path.join(_log_file_path,
                              '{}.log'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))
    _th = handlers.TimedRotatingFileHandler(filename=_file_name,
                                            backupCount=10,
                                            encoding='utf-8')
    _th.setFormatter(_log_formatter)
    _logger.addHandler(_th)


def _caller_info(func):
    """log func caller file name and lineno
    """
    @wraps(func)
    def inner(*args):
        cur_func = inspect.currentframe()
        cur_func_name = inspect.getouterframes(cur_func, 2)
        file, line = cur_func_name[1].filename, cur_func_name[1].lineno
        paths = file.split(PROJECT_NAME)
        caller_path = PROJECT_NAME + paths[1]
        new_args = '[{}:{}]||{}'.format(caller_path, line, *args)
        return func(new_args)
    return inner


@_caller_info
def debug(msg):
    """debug log func
    """
    _logger.debug(msg)


@_caller_info
def info(msg):
    """info log func
    """
    _logger.info(msg)


@_caller_info
def warning(msg):
    """info log func
    """
    _logger.warning(msg)


@_caller_info
def error(msg):
    """info log func
    """
    _logger.error(msg)


@_caller_info
def critical(msg):
    """info log func
    """
    _logger.critical(msg)
