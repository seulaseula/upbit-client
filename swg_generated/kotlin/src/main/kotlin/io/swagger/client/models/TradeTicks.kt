/**
* Upbit Open API
* ## REST API for Upbit Exchange - Base URL: [https://api.upbit.com] - Official Upbit API Documents: [https://docs.upbit.com] - Official Support email: [open-api@upbit.com] 
*
* OpenAPI spec version: 1.0.0
* Contact: ujhin942@gmail.com
*
* NOTE: This class is auto generated by the swagger code generator program.
* https://github.com/swagger-api/swagger-codegen.git
* Do not edit the class manually.
*/
package io.swagger.client.models


/**
 * 
 * @param market 마켓 구분 코드
 * @param trade_date_utc 체결 일자 (UTC 기준)
 * @param trade_time_utc 체결 시각 (UTC 기준)
 * @param timestamp 체결 타임스탬프
 * @param trade_price 체결 가격
 * @param trade_volume 체결량
 * @param prev_closing_price 전일 종가
 * @param change_price 변화량
 * @param ask_bid 매도/매수
 * @param sequential_id 체결 번호 (Unique)  `sequential_id` 필드는 체결의 유일성 판단을 위한 근거로 쓰일 수 있습니다. 하지만 체결의 순서를 보장하지는 못합니다. 
 */
data class TradeTicks (
    /* 마켓 구분 코드 */
    val market: kotlin.String? = null,
    /* 체결 일자 (UTC 기준) */
    val trade_date_utc: kotlin.String? = null,
    /* 체결 시각 (UTC 기준) */
    val trade_time_utc: kotlin.String? = null,
    /* 체결 타임스탬프 */
    val timestamp: java.math.BigDecimal? = null,
    /* 체결 가격 */
    val trade_price: kotlin.Double? = null,
    /* 체결량 */
    val trade_volume: kotlin.Double? = null,
    /* 전일 종가 */
    val prev_closing_price: kotlin.Double? = null,
    /* 변화량 */
    val change_price: kotlin.Double? = null,
    /* 매도/매수 */
    val ask_bid: kotlin.String? = null,
    /* 체결 번호 (Unique)  `sequential_id` 필드는 체결의 유일성 판단을 위한 근거로 쓰일 수 있습니다. 하지만 체결의 순서를 보장하지는 못합니다.  */
    val sequential_id: java.math.BigDecimal? = null
) {

}

