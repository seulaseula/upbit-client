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


#include "SWGBidAccount.h"

#include "SWGHelpers.h"

#include <QJsonDocument>
#include <QJsonArray>
#include <QObject>
#include <QDebug>

namespace Swagger {

SWGBidAccount::SWGBidAccount(QString json) {
    init();
    this->fromJson(json);
}

SWGBidAccount::SWGBidAccount() {
    init();
}

SWGBidAccount::~SWGBidAccount() {
    this->cleanup();
}

void
SWGBidAccount::init() {
    currency = new QString("");
    m_currency_isSet = false;
    balance = new QString("");
    m_balance_isSet = false;
    locked = new QString("");
    m_locked_isSet = false;
    avg_buy_price = new QString("");
    m_avg_buy_price_isSet = false;
    avg_buy_price_modified = false;
    m_avg_buy_price_modified_isSet = false;
    unit_currency = new QString("");
    m_unit_currency_isSet = false;
}

void
SWGBidAccount::cleanup() {
    if(currency != nullptr) { 
        delete currency;
    }
    if(balance != nullptr) { 
        delete balance;
    }
    if(locked != nullptr) { 
        delete locked;
    }
    if(avg_buy_price != nullptr) { 
        delete avg_buy_price;
    }

    if(unit_currency != nullptr) { 
        delete unit_currency;
    }
}

SWGBidAccount*
SWGBidAccount::fromJson(QString json) {
    QByteArray array (json.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
    return this;
}

void
SWGBidAccount::fromJsonObject(QJsonObject pJson) {
    ::Swagger::setValue(&currency, pJson["currency"], "QString", "QString");
    
    ::Swagger::setValue(&balance, pJson["balance"], "QString", "QString");
    
    ::Swagger::setValue(&locked, pJson["locked"], "QString", "QString");
    
    ::Swagger::setValue(&avg_buy_price, pJson["avg_buy_price"], "QString", "QString");
    
    ::Swagger::setValue(&avg_buy_price_modified, pJson["avg_buy_price_modified"], "bool", "");
    
    ::Swagger::setValue(&unit_currency, pJson["unit_currency"], "QString", "QString");
    
}

QString
SWGBidAccount::asJson ()
{
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject
SWGBidAccount::asJsonObject() {
    QJsonObject obj;
    if(currency != nullptr && *currency != QString("")){
        toJsonValue(QString("currency"), currency, obj, QString("QString"));
    }
    if(balance != nullptr && *balance != QString("")){
        toJsonValue(QString("balance"), balance, obj, QString("QString"));
    }
    if(locked != nullptr && *locked != QString("")){
        toJsonValue(QString("locked"), locked, obj, QString("QString"));
    }
    if(avg_buy_price != nullptr && *avg_buy_price != QString("")){
        toJsonValue(QString("avg_buy_price"), avg_buy_price, obj, QString("QString"));
    }
    if(m_avg_buy_price_modified_isSet){
        obj.insert("avg_buy_price_modified", QJsonValue(avg_buy_price_modified));
    }
    if(unit_currency != nullptr && *unit_currency != QString("")){
        toJsonValue(QString("unit_currency"), unit_currency, obj, QString("QString"));
    }

    return obj;
}

QString*
SWGBidAccount::getCurrency() {
    return currency;
}
void
SWGBidAccount::setCurrency(QString* currency) {
    this->currency = currency;
    this->m_currency_isSet = true;
}

QString*
SWGBidAccount::getBalance() {
    return balance;
}
void
SWGBidAccount::setBalance(QString* balance) {
    this->balance = balance;
    this->m_balance_isSet = true;
}

QString*
SWGBidAccount::getLocked() {
    return locked;
}
void
SWGBidAccount::setLocked(QString* locked) {
    this->locked = locked;
    this->m_locked_isSet = true;
}

QString*
SWGBidAccount::getAvgBuyPrice() {
    return avg_buy_price;
}
void
SWGBidAccount::setAvgBuyPrice(QString* avg_buy_price) {
    this->avg_buy_price = avg_buy_price;
    this->m_avg_buy_price_isSet = true;
}

bool
SWGBidAccount::isAvgBuyPriceModified() {
    return avg_buy_price_modified;
}
void
SWGBidAccount::setAvgBuyPriceModified(bool avg_buy_price_modified) {
    this->avg_buy_price_modified = avg_buy_price_modified;
    this->m_avg_buy_price_modified_isSet = true;
}

QString*
SWGBidAccount::getUnitCurrency() {
    return unit_currency;
}
void
SWGBidAccount::setUnitCurrency(QString* unit_currency) {
    this->unit_currency = unit_currency;
    this->m_unit_currency_isSet = true;
}


bool
SWGBidAccount::isSet(){
    bool isObjectUpdated = false;
    do{
        if(currency != nullptr && *currency != QString("")){ isObjectUpdated = true; break;}
        if(balance != nullptr && *balance != QString("")){ isObjectUpdated = true; break;}
        if(locked != nullptr && *locked != QString("")){ isObjectUpdated = true; break;}
        if(avg_buy_price != nullptr && *avg_buy_price != QString("")){ isObjectUpdated = true; break;}
        if(m_avg_buy_price_modified_isSet){ isObjectUpdated = true; break;}
        if(unit_currency != nullptr && *unit_currency != QString("")){ isObjectUpdated = true; break;}
    }while(false);
    return isObjectUpdated;
}
}
