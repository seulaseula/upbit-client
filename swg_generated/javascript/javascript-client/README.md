# upbit_open_api

UpbitOpenApi - JavaScript client for upbit_open_api
## REST API for Upbit Exchange - Base URL: [https://api.upbit.com] - Official Upbit API Documents: [https://docs.upbit.com] - Official Support email: [open-api@upbit.com] 
This SDK is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.JavascriptClientCodegen
For more information, please visit [https://github.com/uJhin](https://github.com/uJhin)

## Installation

### For [Node.js](https://nodejs.org/)

#### npm

To publish the library as a [npm](https://www.npmjs.com/),
please follow the procedure in ["Publishing npm packages"](https://docs.npmjs.com/getting-started/publishing-npm-packages).

Then install it via:

```shell
npm install upbit_open_api --save
```

##### Local development

To use the library locally without publishing to a remote npm registry, first install the dependencies by changing 
into the directory containing `package.json` (and this README). Let's call this `JAVASCRIPT_CLIENT_DIR`. Then run:

```shell
npm install
```

Next, [link](https://docs.npmjs.com/cli/link) it globally in npm with the following, also from `JAVASCRIPT_CLIENT_DIR`:

```shell
npm link
```

Finally, switch to the directory you want to use your upbit_open_api from, and run:

```shell
npm link /path/to/<JAVASCRIPT_CLIENT_DIR>
```

You should now be able to `require('upbit_open_api')` in javascript files from the directory you ran the last 
command above from.

#### git
#
If the library is hosted at a git repository, e.g.
https://github.com/YOUR_USERNAME/upbit_open_api
then install it via:

```shell
    npm install YOUR_USERNAME/upbit_open_api --save
```

### For browser

The library also works in the browser environment via npm and [browserify](http://browserify.org/). After following
the above steps with Node.js and installing browserify with `npm install -g browserify`,
perform the following (assuming *main.js* is your entry file, that's to say your javascript file where you actually 
use this library):

```shell
browserify main.js > bundle.js
```

Then include *bundle.js* in the HTML pages.

### Webpack Configuration

Using Webpack you may encounter the following error: "Module not found: Error:
Cannot resolve module", most certainly you should disable AMD loader. Add/merge
the following section to your webpack config:

```javascript
module: {
  rules: [
    {
      parser: {
        amd: false
      }
    }
  ]
}
```

## Getting Started

Please follow the [installation](#installation) instruction and execute the following JS code:

```javascript
var UpbitOpenApi = require('upbit_open_api');

var defaultClient = UpbitOpenApi.ApiClient.instance;

// Configure API key authorization: Bearer
var Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = "YOUR API KEY"
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix['Authorization'] = "Token"

var api = new UpbitOpenApi.APIKeyApi()

var callback = function(error, data, response) {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
};
api.aPIKeyInfo(callback);

```

## Documentation for API Endpoints

All URIs are relative to *https://api.upbit.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*UpbitOpenApi.APIKeyApi* | [**aPIKeyInfo**](docs/APIKeyApi.md#aPIKeyInfo) | **GET** /api_keys | API 키 리스트 조회
*UpbitOpenApi.AccountApi* | [**accountInfo**](docs/AccountApi.md#accountInfo) | **GET** /accounts | 전체 계좌 조회
*UpbitOpenApi.AccountApi* | [**accountWallet**](docs/AccountApi.md#accountWallet) | **GET** /status/wallet | 입출금 현황
*UpbitOpenApi.CandleApi* | [**candleDays**](docs/CandleApi.md#candleDays) | **GET** /candles/days | 시세 캔들 조회 (일 단위)
*UpbitOpenApi.CandleApi* | [**candleMinutes**](docs/CandleApi.md#candleMinutes) | **GET** /candles/minutes/{unit} | 시세 캔들 조회 (분 단위)
*UpbitOpenApi.CandleApi* | [**candleMonth**](docs/CandleApi.md#candleMonth) | **GET** /candles/months | 시세 캔들 조회 (월 단위)
*UpbitOpenApi.CandleApi* | [**candleWeeks**](docs/CandleApi.md#candleWeeks) | **GET** /candles/weeks | 시세 캔들 조회 (주 단위)
*UpbitOpenApi.DepositApi* | [**depositCoinAddress**](docs/DepositApi.md#depositCoinAddress) | **GET** /deposits/coin_address | 개별 입금 주소 조회
*UpbitOpenApi.DepositApi* | [**depositCoinAddresses**](docs/DepositApi.md#depositCoinAddresses) | **GET** /deposits/coin_addresses | 전체 입금 주소 조회
*UpbitOpenApi.DepositApi* | [**depositGenerateCoinAddress**](docs/DepositApi.md#depositGenerateCoinAddress) | **POST** /deposits/generate_coin_address | 입금 주소 생성 요청
*UpbitOpenApi.DepositApi* | [**depositInfo**](docs/DepositApi.md#depositInfo) | **GET** /deposit | 개별 입금 조회
*UpbitOpenApi.DepositApi* | [**depositInfoAll**](docs/DepositApi.md#depositInfoAll) | **GET** /deposits | 입금 리스트 조회
*UpbitOpenApi.MarketApi* | [**marketInfoAll**](docs/MarketApi.md#marketInfoAll) | **GET** /market/all | 마켓 코드 조회
*UpbitOpenApi.OrderApi* | [**orderCancel**](docs/OrderApi.md#orderCancel) | **DELETE** /order | 주문 취소 접수
*UpbitOpenApi.OrderApi* | [**orderChance**](docs/OrderApi.md#orderChance) | **GET** /orders/chance | 주문 가능 정보
*UpbitOpenApi.OrderApi* | [**orderInfo**](docs/OrderApi.md#orderInfo) | **GET** /order | 개별 주문 조회
*UpbitOpenApi.OrderApi* | [**orderInfoAll**](docs/OrderApi.md#orderInfoAll) | **GET** /orders | 주문 리스트 조회
*UpbitOpenApi.OrderApi* | [**orderNew**](docs/OrderApi.md#orderNew) | **POST** /orders | 주문하기
*UpbitOpenApi.OrderApi* | [**orderOrderbook**](docs/OrderApi.md#orderOrderbook) | **GET** /orderbook | 시세 호가 정보(Orderbook) 조회
*UpbitOpenApi.TradeApi* | [**tradeTicker**](docs/TradeApi.md#tradeTicker) | **GET** /ticker | 시세 Ticker 조회
*UpbitOpenApi.TradeApi* | [**tradeTicks**](docs/TradeApi.md#tradeTicks) | **GET** /trades/ticks | 시세 체결 조회
*UpbitOpenApi.WithdrawApi* | [**withdrawChance**](docs/WithdrawApi.md#withdrawChance) | **GET** /withdraws/chance | 출금 가능 정보
*UpbitOpenApi.WithdrawApi* | [**withdrawCoin**](docs/WithdrawApi.md#withdrawCoin) | **POST** /withdraws/coin | 코인 출금하기
*UpbitOpenApi.WithdrawApi* | [**withdrawInfo**](docs/WithdrawApi.md#withdrawInfo) | **GET** /withdraw | 개별 출금 조회
*UpbitOpenApi.WithdrawApi* | [**withdrawInfoAll**](docs/WithdrawApi.md#withdrawInfoAll) | **GET** /withdraws | 출금 리스트 조회
*UpbitOpenApi.WithdrawApi* | [**withdrawKrw**](docs/WithdrawApi.md#withdrawKrw) | **POST** /withdraws/krw | 원화 출금하기


## Documentation for Models

 - [UpbitOpenApi.APIKey](docs/APIKey.md)
 - [UpbitOpenApi.Account](docs/Account.md)
 - [UpbitOpenApi.Ask](docs/Ask.md)
 - [UpbitOpenApi.AskAccount](docs/AskAccount.md)
 - [UpbitOpenApi.Bid](docs/Bid.md)
 - [UpbitOpenApi.BidAccount](docs/BidAccount.md)
 - [UpbitOpenApi.CandleDate](docs/CandleDate.md)
 - [UpbitOpenApi.CandleDays](docs/CandleDays.md)
 - [UpbitOpenApi.CandleMinutes](docs/CandleMinutes.md)
 - [UpbitOpenApi.Currency](docs/Currency.md)
 - [UpbitOpenApi.Deposit](docs/Deposit.md)
 - [UpbitOpenApi.DepositCompleteResponse](docs/DepositCompleteResponse.md)
 - [UpbitOpenApi.DepositTransferResponse](docs/DepositTransferResponse.md)
 - [UpbitOpenApi.Error](docs/Error.md)
 - [UpbitOpenApi.ErrorInfo](docs/ErrorInfo.md)
 - [UpbitOpenApi.Market](docs/Market.md)
 - [UpbitOpenApi.MarketInfo](docs/MarketInfo.md)
 - [UpbitOpenApi.MemberLevel](docs/MemberLevel.md)
 - [UpbitOpenApi.NewOrder](docs/NewOrder.md)
 - [UpbitOpenApi.Order](docs/Order.md)
 - [UpbitOpenApi.OrderChance](docs/OrderChance.md)
 - [UpbitOpenApi.OrderInfo](docs/OrderInfo.md)
 - [UpbitOpenApi.Orderbook](docs/Orderbook.md)
 - [UpbitOpenApi.OrderbookUnit](docs/OrderbookUnit.md)
 - [UpbitOpenApi.Ticker](docs/Ticker.md)
 - [UpbitOpenApi.Trade](docs/Trade.md)
 - [UpbitOpenApi.TradeTicks](docs/TradeTicks.md)
 - [UpbitOpenApi.Wallet](docs/Wallet.md)
 - [UpbitOpenApi.Withdraw](docs/Withdraw.md)
 - [UpbitOpenApi.WithdrawChance](docs/WithdrawChance.md)
 - [UpbitOpenApi.WithdrawCoin](docs/WithdrawCoin.md)
 - [UpbitOpenApi.WithdrawLimit](docs/WithdrawLimit.md)


## Documentation for Authorization


### Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header
