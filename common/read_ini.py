#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import os.path

from common.project_variable import PROJECT_PATH


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


def dict_ini_file(file_name):
    """
    read ini file to dict
    :param file_name: file path and name of PROJECT_PATH
    :return: dict of ini file
    """
    ptd = ParserToDict()
    ptd.read(os.path.join(PROJECT_PATH, file_name), encoding='utf-8')
    return ptd.as_dict()


def project_base_config():
    """project base config
    """
    return dict_ini_file('config/conf.ini')

