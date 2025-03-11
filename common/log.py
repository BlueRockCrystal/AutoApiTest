#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging
from datetime import datetime
from logging import handlers
from functools import wraps

import colorlog

from common.base import ProjectConfig
from common.util.caller_info import caller_file_line


_logger = logging.getLogger()
_logger.setLevel(ProjectConfig.log.level)

_fmt_str = '%(asctime)s-[%(levelname)s]'
if ProjectConfig.log.thread_info:
    _fmt_str += '-[PID:%(process)d-TID:%(thread)d-%(threadName)s]'
_fmt_str += '-%(message)s'

if ProjectConfig.log.color:
    _fmt_str = '%(log_color)s' + _fmt_str
    _log_colors = {'DEBUG': 'cyan', 'INFO': 'green', 'WARNING': 'yellow', 'ERROR': 'red',
                   'CRITICAL': 'purple'}
    _log_formatter = colorlog.ColoredFormatter(_fmt_str, log_colors=_log_colors)
else:
    _log_formatter = logging.Formatter(_fmt_str)


if ProjectConfig.log.console_handler:
    _ch = logging.StreamHandler(sys.stdout)
    _ch.setFormatter(_log_formatter)
    _logger.addHandler(_ch)

if ProjectConfig.log.file_handler:
    _log_file_path = ProjectConfig.log.file_path
    try:
        if not os.path.exists(_log_file_path):
            os.makedirs(_log_file_path)
    except Exception as e:
        raise Exception('Create_log_dir: {}; failed: {}'.format(_log_file_path, e))

    _log_file_name = ProjectConfig.log.file_name
    if not _log_file_name:
        _log_file_name = '{}.log'.format(datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
    _file_name = str(os.path.join(_log_file_path, _log_file_name))
    _th = handlers.TimedRotatingFileHandler(filename=_file_name, backupCount=10, encoding='utf-8')
    _th.setFormatter(_log_formatter)
    _logger.addHandler(_th)


def _caller_info(func):
    """log func caller file name and lineno
    """
    @wraps(func)
    def inner(*args):
        caller = caller_file_line()
        new_args = '[{}:{}]--{}'.format(caller[0], caller[1], *args)
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
    """warning log func
    """
    _logger.warning(msg)


@_caller_info
def error(msg):
    """error log func
    """
    _logger.error(msg)


@_caller_info
def critical(msg):
    """critical log func
    """
    _logger.critical(msg)

