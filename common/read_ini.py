#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import os.path

from common.base.project_env import PROJECT_PATH


class ParserToDict(configparser.ConfigParser):
    """read ini file to dict
    """

    def as_dict(self):
        """return as dict
        """
        to_dict = dict(self._sections)
        for k in to_dict:
            to_dict[k] = dict(to_dict[k])
        return to_dict


def ini_to_dict(file_name):
    """
    read ini file to dict
    :param file_name: file path and name of PROJECT_PATH
    :return: dict of ini file
    """
    ptd = ParserToDict()
    ptd.read(os.path.join(PROJECT_PATH, file_name), encoding='utf-8')
    return ptd.as_dict()


def project_config():
    """project base config
    """
    return ini_to_dict('config/conf.ini')


def service_api_conf(service, api):
    return ini_to_dict(os.path.join('config/services_configs/{}/api.ini'.format(service))).get(api)


def service_host_conf(env, service):
    return ini_to_dict('config/host.ini').get(env).get(service)

