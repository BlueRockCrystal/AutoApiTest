#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect

from common.base.project_env import PROJECT_NAME


def caller_file_line():
    """
    Call path analysis, find caller file name(with path) and line number
    :return: caller file name & line number
    """
    cur_func = inspect.currentframe()
    cur_func_name = inspect.getouterframes(cur_func, 3)
    file, line = cur_func_name[2].filename, cur_func_name[2].lineno
    paths = file.split(PROJECT_NAME)
    caller_path = PROJECT_NAME + paths[1]
    return caller_path, line

