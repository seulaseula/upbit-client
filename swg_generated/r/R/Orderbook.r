# Upbit Open API
#
# ## REST API for Upbit Exchange - Base URL: [https://api.upbit.com] - Official Upbit API Documents: [https://docs.upbit.com] - Official Support email: [open-api@upbit.com] 
#
# OpenAPI spec version: 1.0.0
# Contact: ujhin942@gmail.com
# Generated by: https://github.com/swagger-api/swagger-codegen.git


#' Orderbook Class
#'
#' @field market 
#' @field timestamp 
#' @field total_ask_size 
#' @field total_bid_size 
#' @field orderbook_units 
#'
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
Orderbook <- R6::R6Class(
  'Orderbook',
  public = list(
    `market` = NULL,
    `timestamp` = NULL,
    `total_ask_size` = NULL,
    `total_bid_size` = NULL,
    `orderbook_units` = NULL,
    initialize = function(`market`, `timestamp`, `total_ask_size`, `total_bid_size`, `orderbook_units`){
      if (!missing(`market`)) {
        stopifnot(is.character(`market`), length(`market`) == 1)
        self$`market` <- `market`
      }
      if (!missing(`timestamp`)) {
        self$`timestamp` <- `timestamp`
      }
      if (!missing(`total_ask_size`)) {
        stopifnot(is.numeric(`total_ask_size`), length(`total_ask_size`) == 1)
        self$`total_ask_size` <- `total_ask_size`
      }
      if (!missing(`total_bid_size`)) {
        stopifnot(is.numeric(`total_bid_size`), length(`total_bid_size`) == 1)
        self$`total_bid_size` <- `total_bid_size`
      }
      if (!missing(`orderbook_units`)) {
        stopifnot(is.list(`orderbook_units`), length(`orderbook_units`) != 0)
        lapply(`orderbook_units`, function(x) stopifnot(R6::is.R6(x)))
        self$`orderbook_units` <- `orderbook_units`
      }
    },
    toJSON = function() {
      OrderbookObject <- list()
      if (!is.null(self$`market`)) {
        OrderbookObject[['market']] <- self$`market`
      }
      if (!is.null(self$`timestamp`)) {
        OrderbookObject[['timestamp']] <- self$`timestamp`
      }
      if (!is.null(self$`total_ask_size`)) {
        OrderbookObject[['total_ask_size']] <- self$`total_ask_size`
      }
      if (!is.null(self$`total_bid_size`)) {
        OrderbookObject[['total_bid_size']] <- self$`total_bid_size`
      }
      if (!is.null(self$`orderbook_units`)) {
        OrderbookObject[['orderbook_units']] <- lapply(self$`orderbook_units`, function(x) x$toJSON())
      }

      OrderbookObject
    },
    fromJSON = function(OrderbookJson) {
      OrderbookObject <- jsonlite::fromJSON(OrderbookJson)
      if (!is.null(OrderbookObject$`market`)) {
        self$`market` <- OrderbookObject$`market`
      }
      if (!is.null(OrderbookObject$`timestamp`)) {
        self$`timestamp` <- OrderbookObject$`timestamp`
      }
      if (!is.null(OrderbookObject$`total_ask_size`)) {
        self$`total_ask_size` <- OrderbookObject$`total_ask_size`
      }
      if (!is.null(OrderbookObject$`total_bid_size`)) {
        self$`total_bid_size` <- OrderbookObject$`total_bid_size`
      }
      if (!is.null(OrderbookObject$`orderbook_units`)) {
        self$`orderbook_units` <- lapply(OrderbookObject$`orderbook_units`, function(x) {
          orderbook_unitsObject <- OrderbookUnit$new()
          orderbook_unitsObject$fromJSON(jsonlite::toJSON(x, auto_unbox = TRUE))
          orderbook_unitsObject
        })
      }
    },
    toJSONString = function() {
       sprintf(
        '{
           "market": %s,
           "timestamp": %s,
           "total_ask_size": %d,
           "total_bid_size": %d,
           "orderbook_units": [%s]
        }',
        self$`market`,
        self$`timestamp`,
        self$`total_ask_size`,
        self$`total_bid_size`,
        lapply(self$`orderbook_units`, function(x) paste(x$toJSON(), sep=","))
      )
    },
    fromJSONString = function(OrderbookJson) {
      OrderbookObject <- jsonlite::fromJSON(OrderbookJson)
      self$`market` <- OrderbookObject$`market`
      self$`timestamp` <- OrderbookObject$`timestamp`
      self$`total_ask_size` <- OrderbookObject$`total_ask_size`
      self$`total_bid_size` <- OrderbookObject$`total_bid_size`
      self$`orderbook_units` <- lapply(OrderbookObject$`orderbook_units`, function(x) OrderbookUnit$new()$fromJSON(jsonlite::toJSON(x, auto_unbox = TRUE)))
    }
  )
)
