# coding: utf-8

"""
    Upbit Open API

    ## REST API for Upbit Exchange - Base URL: [https://api.upbit.com] - Official Upbit API Documents: [https://docs.upbit.com] - Official Support email: [open-api@upbit.com]   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: ujhin942@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class DepositApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def deposit_coin_address(self, currency, **kwargs):  # noqa: E501
        """개별 입금 주소 조회  # noqa: E501

        ## 개별 입금 주소 조회 **NOTE**: 입금 주소 조회 요청 API 유의사항 입금 주소 생성 요청 이후 아직 발급되지 않은 상태일 경우 deposit_address가 null일 수 있습니다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deposit_coin_address(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: Currency symbol  (required)
        :return: DepositCompleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deposit_coin_address_with_http_info(currency, **kwargs)  # noqa: E501
        else:
            (data) = self.deposit_coin_address_with_http_info(currency, **kwargs)  # noqa: E501
            return data

    def deposit_coin_address_with_http_info(self, currency, **kwargs):  # noqa: E501
        """개별 입금 주소 조회  # noqa: E501

        ## 개별 입금 주소 조회 **NOTE**: 입금 주소 조회 요청 API 유의사항 입금 주소 생성 요청 이후 아직 발급되지 않은 상태일 경우 deposit_address가 null일 수 있습니다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deposit_coin_address_with_http_info(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: Currency symbol  (required)
        :return: DepositCompleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deposit_coin_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in params or
                params['currency'] is None):
            raise ValueError("Missing the required parameter `currency` when calling `deposit_coin_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/deposits/coin_address', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DepositCompleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deposit_coin_addresses(self, **kwargs):  # noqa: E501
        """전체 입금 주소 조회  # noqa: E501

        ## 내가 보유한 자산 리스트를 보여줍니다. **NOTE**: 입금 주소 조회 요청 API 유의사항 입금 주소 생성 요청 이후 아직 발급되지 않은 상태일 경우 deposit_address가 null일 수 있습니다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deposit_coin_addresses(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deposit_coin_addresses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.deposit_coin_addresses_with_http_info(**kwargs)  # noqa: E501
            return data

    def deposit_coin_addresses_with_http_info(self, **kwargs):  # noqa: E501
        """전체 입금 주소 조회  # noqa: E501

        ## 내가 보유한 자산 리스트를 보여줍니다. **NOTE**: 입금 주소 조회 요청 API 유의사항 입금 주소 생성 요청 이후 아직 발급되지 않은 상태일 경우 deposit_address가 null일 수 있습니다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deposit_coin_addresses_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deposit_coin_addresses" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/deposits/coin_addresses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deposit_generate_coin_address(self, currency, **kwargs):  # noqa: E501
        """입금 주소 생성 요청  # noqa: E501

        입금 주소 생성을 요청한다. **NOTE**: 입금 주소 생성 요청 API 유의사항 입금 주소의 생성은 서버에서 비동기적으로 이뤄집니다. 비동기적 생성 특성상 요청과 동시에 입금 주소가 발급되지 않을 수 있습니다. 주소 발급 요청 시 결과로 Response1이 반환되며 주소 발급 완료 이전까지 계속 Response1이 반환됩니다. 주소가 발급된 이후부터는 새로운 주소가 발급되는 것이 아닌 이전에 발급된 주소가 Response2 형태로 반환됩니다. 정상적으로 주소가 생성되지 않는다면 일정 시간 이후 해당 API를 다시 호출해주시길 부탁드립니다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deposit_generate_coin_address(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: Currency 코드  (required)
        :return: DepositCompleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deposit_generate_coin_address_with_http_info(currency, **kwargs)  # noqa: E501
        else:
            (data) = self.deposit_generate_coin_address_with_http_info(currency, **kwargs)  # noqa: E501
            return data

    def deposit_generate_coin_address_with_http_info(self, currency, **kwargs):  # noqa: E501
        """입금 주소 생성 요청  # noqa: E501

        입금 주소 생성을 요청한다. **NOTE**: 입금 주소 생성 요청 API 유의사항 입금 주소의 생성은 서버에서 비동기적으로 이뤄집니다. 비동기적 생성 특성상 요청과 동시에 입금 주소가 발급되지 않을 수 있습니다. 주소 발급 요청 시 결과로 Response1이 반환되며 주소 발급 완료 이전까지 계속 Response1이 반환됩니다. 주소가 발급된 이후부터는 새로운 주소가 발급되는 것이 아닌 이전에 발급된 주소가 Response2 형태로 반환됩니다. 정상적으로 주소가 생성되지 않는다면 일정 시간 이후 해당 API를 다시 호출해주시길 부탁드립니다.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deposit_generate_coin_address_with_http_info(currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: Currency 코드  (required)
        :return: DepositCompleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deposit_generate_coin_address" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'currency' is set
        if ('currency' not in params or
                params['currency'] is None):
            raise ValueError("Missing the required parameter `currency` when calling `deposit_generate_coin_address`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'currency' in params:
            form_params.append(('currency', params['currency']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/deposits/generate_coin_address', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DepositCompleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deposit_info(self, **kwargs):  # noqa: E501
        """개별 입금 조회  # noqa: E501

        ## 개별 입금 조회   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deposit_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: 입금 UUID 
        :param str txid: 입금 TXID 
        :param str currency: Currency 코드 
        :return: Deposit
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deposit_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.deposit_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def deposit_info_with_http_info(self, **kwargs):  # noqa: E501
        """개별 입금 조회  # noqa: E501

        ## 개별 입금 조회   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deposit_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: 입금 UUID 
        :param str txid: 입금 TXID 
        :param str currency: Currency 코드 
        :return: Deposit
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid', 'txid', 'currency']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deposit_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'uuid' in params:
            query_params.append(('uuid', params['uuid']))  # noqa: E501
        if 'txid' in params:
            query_params.append(('txid', params['txid']))  # noqa: E501
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/deposit', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Deposit',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deposit_info_all(self, **kwargs):  # noqa: E501
        """입금 리스트 조회  # noqa: E501

        ## 입금 리스트 조회   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deposit_info_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: Currency 코드 
        :param str state: 출금 상태 - submitting : 처리 중 - submitted : 처리완료 - almost_accepted : 입금 대기 중 - rejected : 거절 - accepted : 승인됨 - processing : 처리 중 
        :param list[str] uuids: 입금 UUID의 목록 
        :param list[str] txids: 입금 TXID의 목록 
        :param float limit: 개수 제한 (default: 100, max: 100) 
        :param float page: 페이지 수, default: 1 
        :param str order_by: 정렬 방식 - asc : 오름차순 - desc : 내림차순 (default) 
        :return: list[Deposit]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deposit_info_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.deposit_info_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def deposit_info_all_with_http_info(self, **kwargs):  # noqa: E501
        """입금 리스트 조회  # noqa: E501

        ## 입금 리스트 조회   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deposit_info_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str currency: Currency 코드 
        :param str state: 출금 상태 - submitting : 처리 중 - submitted : 처리완료 - almost_accepted : 입금 대기 중 - rejected : 거절 - accepted : 승인됨 - processing : 처리 중 
        :param list[str] uuids: 입금 UUID의 목록 
        :param list[str] txids: 입금 TXID의 목록 
        :param float limit: 개수 제한 (default: 100, max: 100) 
        :param float page: 페이지 수, default: 1 
        :param str order_by: 정렬 방식 - asc : 오름차순 - desc : 내림차순 (default) 
        :return: list[Deposit]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['currency', 'state', 'uuids', 'txids', 'limit', 'page', 'order_by']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deposit_info_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'uuids' in params:
            query_params.append(('uuids', params['uuids']))  # noqa: E501
            collection_formats['uuids'] = 'multi'  # noqa: E501
        if 'txids' in params:
            query_params.append(('txids', params['txids']))  # noqa: E501
            collection_formats['txids'] = 'multi'  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('order_by', params['order_by']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/deposits', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Deposit]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)