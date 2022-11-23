#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.log import debug


class _EnvClass:
    """run test env class
    """

    def __init__(self, env_dict):
        """init env class
        """
        self.idc = env_dict.get('idc')
        self.tag = env_dict.get('tag')


def run_test_env():
    """run test case env info
    """
    idc = 'qa_test'
    tag = 'prod'
    return _EnvClass(dict(idc=idc, tag=tag))


ENV_INFO = run_test_env()

debug('run test idc is {}, tag is {}'.format(ENV_INFO.idc, ENV_INFO.tag))
