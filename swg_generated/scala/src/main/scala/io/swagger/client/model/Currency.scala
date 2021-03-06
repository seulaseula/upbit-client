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

package io.swagger.client.model


case class Currency (
  // 화폐를 의미하는 영문 대문자 코드
  code: Option[String] = None,
  // 해당 화폐의 출금 수수료
  withdrawFee: Option[String] = None,
  // 화폐의 코인 여부
  isCoin: Option[Boolean] = None,
  // 해당 화폐의 지갑 상태
  walletState: Option[String] = None,
  // 해당 화폐가 지원하는 입출금 정보
  walletSupport: Option[List[String]] = None
)

