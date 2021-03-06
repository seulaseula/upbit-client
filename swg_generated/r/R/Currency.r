# Upbit Open API
#
# ## REST API for Upbit Exchange - Base URL: [https://api.upbit.com] - Official Upbit API Documents: [https://docs.upbit.com] - Official Support email: [open-api@upbit.com] 
#
# OpenAPI spec version: 1.0.0
# Contact: ujhin942@gmail.com
# Generated by: https://github.com/swagger-api/swagger-codegen.git


#' Currency Class
#'
#' @field code 
#' @field withdraw_fee 
#' @field is_coin 
#' @field wallet_state 
#' @field wallet_support 
#'
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
Currency <- R6::R6Class(
  'Currency',
  public = list(
    `code` = NULL,
    `withdraw_fee` = NULL,
    `is_coin` = NULL,
    `wallet_state` = NULL,
    `wallet_support` = NULL,
    initialize = function(`code`, `withdraw_fee`, `is_coin`, `wallet_state`, `wallet_support`){
      if (!missing(`code`)) {
        stopifnot(is.character(`code`), length(`code`) == 1)
        self$`code` <- `code`
      }
      if (!missing(`withdraw_fee`)) {
        stopifnot(is.character(`withdraw_fee`), length(`withdraw_fee`) == 1)
        self$`withdraw_fee` <- `withdraw_fee`
      }
      if (!missing(`is_coin`)) {
        self$`is_coin` <- `is_coin`
      }
      if (!missing(`wallet_state`)) {
        stopifnot(is.character(`wallet_state`), length(`wallet_state`) == 1)
        self$`wallet_state` <- `wallet_state`
      }
      if (!missing(`wallet_support`)) {
        stopifnot(is.list(`wallet_support`), length(`wallet_support`) != 0)
        lapply(`wallet_support`, function(x) stopifnot(is.character(x)))
        self$`wallet_support` <- `wallet_support`
      }
    },
    toJSON = function() {
      CurrencyObject <- list()
      if (!is.null(self$`code`)) {
        CurrencyObject[['code']] <- self$`code`
      }
      if (!is.null(self$`withdraw_fee`)) {
        CurrencyObject[['withdraw_fee']] <- self$`withdraw_fee`
      }
      if (!is.null(self$`is_coin`)) {
        CurrencyObject[['is_coin']] <- self$`is_coin`
      }
      if (!is.null(self$`wallet_state`)) {
        CurrencyObject[['wallet_state']] <- self$`wallet_state`
      }
      if (!is.null(self$`wallet_support`)) {
        CurrencyObject[['wallet_support']] <- self$`wallet_support`
      }

      CurrencyObject
    },
    fromJSON = function(CurrencyJson) {
      CurrencyObject <- jsonlite::fromJSON(CurrencyJson)
      if (!is.null(CurrencyObject$`code`)) {
        self$`code` <- CurrencyObject$`code`
      }
      if (!is.null(CurrencyObject$`withdraw_fee`)) {
        self$`withdraw_fee` <- CurrencyObject$`withdraw_fee`
      }
      if (!is.null(CurrencyObject$`is_coin`)) {
        self$`is_coin` <- CurrencyObject$`is_coin`
      }
      if (!is.null(CurrencyObject$`wallet_state`)) {
        self$`wallet_state` <- CurrencyObject$`wallet_state`
      }
      if (!is.null(CurrencyObject$`wallet_support`)) {
        self$`wallet_support` <- CurrencyObject$`wallet_support`
      }
    },
    toJSONString = function() {
       sprintf(
        '{
           "code": %s,
           "withdraw_fee": %s,
           "is_coin": %s,
           "wallet_state": %s,
           "wallet_support": [%s]
        }',
        self$`code`,
        self$`withdraw_fee`,
        self$`is_coin`,
        self$`wallet_state`,
        lapply(self$`wallet_support`, function(x) paste(paste0('"', x, '"'), sep=","))
      )
    },
    fromJSONString = function(CurrencyJson) {
      CurrencyObject <- jsonlite::fromJSON(CurrencyJson)
      self$`code` <- CurrencyObject$`code`
      self$`withdraw_fee` <- CurrencyObject$`withdraw_fee`
      self$`is_coin` <- CurrencyObject$`is_coin`
      self$`wallet_state` <- CurrencyObject$`wallet_state`
      self$`wallet_support` <- CurrencyObject$`wallet_support`
    }
  )
)
