#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging

import curlify
import urllib3
import requests

from common import log
from common.read_ini import service_api_conf, service_host_conf
from common.base.run_test_env import ENV_INFO

urllib3.disable_warnings()
urllib3.add_stderr_logger(logging.ERROR)

logging.getLogger('requests').setLevel(logging.ERROR)
logging.captureWarnings(True)


class RequestTranslate:
    """http request detail class, dict to class
    """

    def __init__(self, request_dict: dict):
        """Init RequestDetail class
        """
        self._req_dict = request_dict
        self._config = self._api_config()
        self._common_config = self._api_common_config()

        self.req_method = self._config.get('method')
        self.req_url = self._host() + self._uri()
        self.req_headers = self._headers()
        self.req_params = self._params()
        self.req_body = self._body()
        self.req_body_type = self._config.get('body_type')

        self.req_timeout_assert = self._timeout()
        self.req_timecost_expect = self._timecost()

    def _api_config(self):
        """get ini file api config
        """
        return service_api_conf(self._req_dict.get('service'), self._req_dict.get('api'))

    def _api_common_config(self):
        """get ini file api common config
        """
        return service_api_conf(self._req_dict.get('service'), 'common')

    def _host(self):
        """request host
        """
        host = service_host_conf(ENV_INFO.env, self._req_dict.get('service'))
        if host[-1] == '/':
            host = host[:-1]
        return host

    def _uri(self):
        """request uri
        """
        req_uri, default_params = self._config.get('uri'), self._config.get('uri_params')
        real_uri_params = dict()
        if self._req_dict.get('default_uri_param') and default_params:
            for k, v in json.loads(default_params).items():
                real_uri_params[k] = v

        uri_params = self._req_dict.get('uri_params')
        if uri_params:
            for k, v in uri_params.items():
                real_uri_params[k] = v

        if '{%' in req_uri and '%}' in req_uri and real_uri_params:
            for k, v in real_uri_params.items():
                print(k, v)
                req_uri = req_uri.replace('{%'+'{}'.format(k)+'%}', '{}'.format(v))
        if req_uri[0] != '/':
            req_uri = '/' + req_uri
        if req_uri[-1] == '/':
            req_uri = req_uri[:-1]
        return req_uri

    def _headers(self):
        """request headers
        """
        req_headers = dict()
        if self._req_dict.get('common_headers'):
            common_headers = self._common_config.get('headers')
            if common_headers:
                for k, v in json.loads(common_headers).items():
                    req_headers[k] = v

        if self._req_dict.get('default_headers'):
            default_headers = self._config.get('headers')
            if default_headers:
                for k, v in json.loads(default_headers).items():
                    req_headers[k] = v

        headers = self._req_dict.get('headers')
        if headers:
            for k, v in headers.items():
                req_headers[k] = v

        return req_headers

    def _params(self):
        """request params
        """
        req_params = dict()
        if self._req_dict.get('common_params'):
            common_params = self._common_config.get('params')
            if common_params:
                for k, v in json.loads(common_params).items():
                    req_params[k] = v

        if self._req_dict.get('default_params'):
            default_params = self._config.get('params')
            if default_params:
                for k, v in json.loads(default_params).items():
                    req_params[k] = v

        params = self._req_dict.get('params')
        if params:
            for k, v in params:
                req_params[k] = v

        return req_params

    def _body(self):
        """request body
        """
        req_body = dict()
        if self._req_dict.get('common_body'):
            common_body = self._common_config.get('body')
            if common_body:
                for k, v in json.loads(common_body).items():
                    req_body[k] = v

        if self._req_dict.get('default_body'):
            default_body = self._config.get('body')
            if default_body:
                for k, v in json.loads(default_body).items():
                    req_body[k] = v

        body = self._req_dict.get('body')
        if body:
            for k, v in body.items():
                req_body[k] = v
        return req_body

    def _timeout(self):
        """request timeout assert
        """
        req_expect = self._req_dict.get('timeout_assert')
        if req_expect != 0:
            return req_expect
        api_expect = self._config.get('timeout_assert')
        if api_expect:
            return int(api_expect)
        common_expect = self._common_config.get('timeout_assert')
        if common_expect:
            return int(common_expect)
        return 0

    def _timecost(self):
        """request time cost expect
        """
        req_expect = self._req_dict.get('timecost_expect')
        if req_expect != 0:
            return req_expect
        api_expect = self._config.get('timecost_expect')
        if api_expect:
            return int(api_expect)
        common_expect = self._common_config.get('timecost_expect')
        if common_expect:
            return int(common_expect)
        return 0


class RequestClass:
    """use requests package, send http request
    """

    def __init__(self, req: RequestTranslate):
        """init request class
        """
        self._request = req
        self._connection_timout = 5

    def send(self):
        """send http request method
        """
        log.debug('http_request_start: {} {}'.format(self._request.req_method,
                                                     self._request.req_url))
        expect_timeout = self._request.req_timeout_assert
        if expect_timeout == 0:
            timeout = None
        else:
            timeout = (self._connection_timout, expect_timeout / 1000)

        body_type, body = self._request.req_body_type, self._request.req_body
        if not body_type or body_type == 'json':
            body = json.dumps(body, separators=(',', ':'), ensure_ascii=False).encode('utf-8')
        resp = None
        try:
            resp = requests.request(method=self._request.req_method,
                                    url=self._request.req_url,
                                    headers=self._request.req_headers,
                                    params=self._request.req_params,
                                    data=body,
                                    timeout=timeout)
        except Exception as e:
            log.critical('http_connection_error: {}'.format(e))
        resp_obj = ResponseClass(self._request, resp)
        log.debug(log_format(resp_obj))
        return resp_obj


class ResponseClass(RequestClass):
    """response class
    """

    def __init__(self, req: RequestTranslate, response: requests.Response):
        """init response class
        """
        super().__init__(req)
        self.req_method = req.req_method
        self.req_url = req.req_url
        self.req_params = req.req_params
        self.req_headers = req.req_headers
        self.req_body = req.req_body

        if hasattr(response, 'status_code'):
            self.request = response.request
            self.resp_status_code = response.status_code
            self.resp_headers = response.headers
            self.resp_content = response.content
            self.resp_timecost = int(format(float(response.elapsed.total_seconds())*1000, '.0f'))
        else:
            self.resp_status_code = None
            self.resp_headers = None
            self.resp_content = None
            self.resp_timecost = None


def log_format(resp_obj):
    """http request and response log format
    """
    msg = 'http_request_finished: {} {}'.format(resp_obj.req_method, resp_obj.req_url)
    msg = msg + '\n' + '='*50 + '>'*10
    msg = msg + '\n' + 'request_params: {}'.format(resp_obj.req_params)
    if resp_obj.req_method != 'GET':
        msg = msg + '\n' + 'request_body: {}'.format(resp_obj.req_body)
    if resp_obj.resp_status_code:
        msg = msg + '\n' + 'request_as_curl: {}'.format(curlify.to_curl(resp_obj.request,
                                                                        compressed=True))
        msg = msg + '\n' + '<'*10 + '='*50
        msg = msg + '\n' + 'response_timecost: {}ms'.format(resp_obj.resp_timecost)
        msg = msg + '\n' + 'response_headers: {}'.format(resp_obj.resp_headers)
        msg = msg + '\n' + 'response_content: {}'.format(resp_obj.resp_content.decode('utf-8'))

    return msg
