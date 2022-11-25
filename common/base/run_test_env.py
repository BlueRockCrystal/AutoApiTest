#!/usr/bin/env python
# -*- coding: utf-8 -*-
from common.log import debug


class _EnvClass:
    """run test env class
    """

    def __init__(self, env_dict):
        """init env class
        """
        self.env = env_dict.get('env')
        self.tag = env_dict.get('tag')


def run_test_env():
    """run test case env info
    """
    env = 'qa_test'
    tag = 'prod'
    return _EnvClass(dict(env=env, tag=tag))


ENV_INFO = run_test_env()

debug('run test env is {}, tag is {}'.format(ENV_INFO.env, ENV_INFO.tag))
