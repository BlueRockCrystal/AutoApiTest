#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ConfigError:
    """log config error
    """
    log_level = 'config/conf.ini [log_config]log_level value illegal!'
    file_handler = 'config/base_config.ini [log_config]log_file_handler value illegal!'
    console_handler = 'config/conf.ini [log_config]log_console_handler value illegal!'
    log_handler_none = 'config/conf.ini [log_config]log_console_handler and log_file_handler False!'
    pid_tid_info = 'config/conf.ini [log_config]pid_tid_info value illegal!'
    log_file_path = 'config/conf.ini [log_config]log_file_path value illegal!'


