#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common import log
from common.util.caller_info import caller_file_line


def retry(times=3):
    """
    func return None or return False need retry decorator function
    demo:
    @retry(5)
    def go_retry():
        return False
    :param times: retry times, default 3
    """
    def decorator(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            number = 0
            caller = caller_file_line()

            if not ret:
                while number < times:
                    number += 1
                    log.warning('{}:{} retry {} times'.format(caller[0], caller[1], number))
                    result = func(*args, **kwargs)
                    if result:
                        break
            return func(*args, **kwargs)
        return inner
    return decorator


def retry_reason(reason, max_times=3):
    """
    retry by raise Error or Exception
    demo:
    @retry_reason(ZeroDivisionError, 5)
    def go_retry():
        try:
            1/0
        except ZeroDivisionError:
            raise ZeroDivisionError
    :param reason: retry reason, need use raise Error or Exception
    :param max_times:
    """
    def decorator(func):
        def inner(*args, **kwargs):
            caller = caller_file_line()
            count = 1
            while count <= max_times:
                try:
                    return func(*args, **kwargs)
                except reason:
                    log.warning('{}:{} retry {} times, reason is {}'.format(caller[0], caller[1],
                                                                            count, reason))
                    count += 1
            return func(*args, **kwargs)
        return inner
    return decorator


