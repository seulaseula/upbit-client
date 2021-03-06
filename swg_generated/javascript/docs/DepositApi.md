# UpbitOpenApi.DepositApi

All URIs are relative to *https://api.upbit.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**depositCoinAddress**](DepositApi.md#depositCoinAddress) | **GET** /deposits/coin_address | 개별 입금 주소 조회
[**depositCoinAddresses**](DepositApi.md#depositCoinAddresses) | **GET** /deposits/coin_addresses | 전체 입금 주소 조회
[**depositGenerateCoinAddress**](DepositApi.md#depositGenerateCoinAddress) | **POST** /deposits/generate_coin_address | 입금 주소 생성 요청
[**depositInfo**](DepositApi.md#depositInfo) | **GET** /deposit | 개별 입금 조회
[**depositInfoAll**](DepositApi.md#depositInfoAll) | **GET** /deposits | 입금 리스트 조회


<a name="depositCoinAddress"></a>
# **depositCoinAddress**
> DepositCompleteResponse depositCoinAddress(currency)

개별 입금 주소 조회

## 개별 입금 주소 조회  **NOTE**: 입금 주소 조회 요청 API 유의사항  입금 주소 생성 요청 이후 아직 발급되지 않은 상태일 경우 deposit_address가 null일 수 있습니다. 

### Example
```javascript
var UpbitOpenApi = require('upbit_open_api');
var defaultClient = UpbitOpenApi.ApiClient.instance;

// Configure API key authorization: Bearer
var Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

var apiInstance = new UpbitOpenApi.DepositApi();

var currency = "currency_example"; // String | Currency symbol 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.depositCoinAddress(currency, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **String**| Currency symbol  | 

### Return type

[**DepositCompleteResponse**](DepositCompleteResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="depositCoinAddresses"></a>
# **depositCoinAddresses**
> Object depositCoinAddresses()

전체 입금 주소 조회

## 내가 보유한 자산 리스트를 보여줍니다.  **NOTE**: 입금 주소 조회 요청 API 유의사항  입금 주소 생성 요청 이후 아직 발급되지 않은 상태일 경우 deposit_address가 null일 수 있습니다. 

### Example
```javascript
var UpbitOpenApi = require('upbit_open_api');
var defaultClient = UpbitOpenApi.ApiClient.instance;

// Configure API key authorization: Bearer
var Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

var apiInstance = new UpbitOpenApi.DepositApi();

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.depositCoinAddresses(callback);
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="depositGenerateCoinAddress"></a>
# **depositGenerateCoinAddress**
> DepositCompleteResponse depositGenerateCoinAddress(currency)

입금 주소 생성 요청

입금 주소 생성을 요청한다.  **NOTE**: 입금 주소 생성 요청 API 유의사항  입금 주소의 생성은 서버에서 비동기적으로 이뤄집니다. 비동기적 생성 특성상 요청과 동시에 입금 주소가 발급되지 않을 수 있습니다. 주소 발급 요청 시 결과로 Response1이 반환되며 주소 발급 완료 이전까지 계속 Response1이 반환됩니다. 주소가 발급된 이후부터는 새로운 주소가 발급되는 것이 아닌 이전에 발급된 주소가 Response2 형태로 반환됩니다. 정상적으로 주소가 생성되지 않는다면 일정 시간 이후 해당 API를 다시 호출해주시길 부탁드립니다. 

### Example
```javascript
var UpbitOpenApi = require('upbit_open_api');
var defaultClient = UpbitOpenApi.ApiClient.instance;

// Configure API key authorization: Bearer
var Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

var apiInstance = new UpbitOpenApi.DepositApi();

var currency = "currency_example"; // String | Currency 코드 


var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.depositGenerateCoinAddress(currency, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **String**| Currency 코드  | 

### Return type

[**DepositCompleteResponse**](DepositCompleteResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

<a name="depositInfo"></a>
# **depositInfo**
> Deposit depositInfo(opts)

개별 입금 조회

## 개별 입금 조회 

### Example
```javascript
var UpbitOpenApi = require('upbit_open_api');
var defaultClient = UpbitOpenApi.ApiClient.instance;

// Configure API key authorization: Bearer
var Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

var apiInstance = new UpbitOpenApi.DepositApi();

var opts = { 
  'uuid': "uuid_example", // String | 입금 UUID 
  'txid': "txid_example", // String | 입금 TXID 
  'currency': "currency_example" // String | Currency 코드 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.depositInfo(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **String**| 입금 UUID  | [optional] 
 **txid** | **String**| 입금 TXID  | [optional] 
 **currency** | **String**| Currency 코드  | [optional] 

### Return type

[**Deposit**](Deposit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="depositInfoAll"></a>
# **depositInfoAll**
> [Deposit] depositInfoAll(opts)

입금 리스트 조회

## 입금 리스트 조회 

### Example
```javascript
var UpbitOpenApi = require('upbit_open_api');
var defaultClient = UpbitOpenApi.ApiClient.instance;

// Configure API key authorization: Bearer
var Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

var apiInstance = new UpbitOpenApi.DepositApi();

var opts = { 
  'currency': "currency_example", // String | Currency 코드 
  'state': "state_example", // String | 출금 상태 - submitting : 처리 중 - submitted : 처리완료 - almost_accepted : 입금 대기 중 - rejected : 거절 - accepted : 승인됨 - processing : 처리 중 
  'uuids': ["uuids_example"], // [String] | 입금 UUID의 목록 
  'txids': ["txids_example"], // [String] | 입금 TXID의 목록 
  'limit': 8.14, // Number | 개수 제한 (default: 100, max: 100) 
  'page': 8.14, // Number | 페이지 수, default: 1 
  'orderBy': "orderBy_example" // String | 정렬 방식 - asc : 오름차순 - desc : 내림차순 (default) 
};

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
apiInstance.depositInfoAll(opts, callback);
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **String**| Currency 코드  | [optional] 
 **state** | **String**| 출금 상태 - submitting : 처리 중 - submitted : 처리완료 - almost_accepted : 입금 대기 중 - rejected : 거절 - accepted : 승인됨 - processing : 처리 중  | [optional] 
 **uuids** | [**[String]**](String.md)| 입금 UUID의 목록  | [optional] 
 **txids** | [**[String]**](String.md)| 입금 TXID의 목록  | [optional] 
 **limit** | **Number**| 개수 제한 (default: 100, max: 100)  | [optional] 
 **page** | **Number**| 페이지 수, default: 1  | [optional] 
 **orderBy** | **String**| 정렬 방식 - asc : 오름차순 - desc : 내림차순 (default)  | [optional] 

### Return type

[**[Deposit]**](Deposit.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

