# coding: utf-8

"""
    Unique ID

    API to look up or generate a unique study identifier

    OpenAPI spec version: 1.0.0
    Contact: scweber@stanford.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DefaultApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def mrn(self, token, **kwargs):
        """
        Accepts a list of Stanford MRNs with optional name and date of birth, returns a list of invalid MRNs or empty list if no problems found
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mrn(token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str token: required authentication token (required)
        :param StanfordMrnList mrns: Array of StanfordMrn
        :return: ValidMrnList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.mrn_with_http_info(token, **kwargs)
        else:
            (data) = self.mrn_with_http_info(token, **kwargs)
            return data

    def mrn_with_http_info(self, token, **kwargs):
        """
        Accepts a list of Stanford MRNs with optional name and date of birth, returns a list of invalid MRNs or empty list if no problems found
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.mrn_with_http_info(token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str token: required authentication token (required)
        :param StanfordMrnList mrns: Array of StanfordMrn
        :return: ValidMrnList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token', 'mrns']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method mrn" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params) or (params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `mrn`")


        collection_formats = {}

        resource_path = '/v1/api/mrn/:mrn'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'token' in params:
            query_params['token'] = params['token']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'mrns' in params:
            body_params = params['mrns']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ValidMrnList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)