/* 
 * Upbit Open API
 *
 * ## REST API for Upbit Exchange - Base URL: [https://api.upbit.com] - Official Upbit API Documents: [https://docs.upbit.com] - Official Support email: [open-api@upbit.com] 
 *
 * OpenAPI spec version: 1.0.0
 * Contact: ujhin942@gmail.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using NUnit.Framework;

using IO.Swagger.Client;
using IO.Swagger.Api;
using IO.Swagger.Model;

namespace IO.Swagger.Test
{
    /// <summary>
    ///  Class for testing TradeApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by Swagger Codegen.
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    [TestFixture]
    public class TradeApiTests
    {
        private TradeApi instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new TradeApi();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of TradeApi
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOfType' TradeApi
            //Assert.IsInstanceOfType(typeof(TradeApi), instance, "instance is a TradeApi");
        }

        
        /// <summary>
        /// Test TradeTicker
        /// </summary>
        [Test]
        public void TradeTickerTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string markets = null;
            //var response = instance.TradeTicker(markets);
            //Assert.IsInstanceOf<Object> (response, "response is Object");
        }
        
        /// <summary>
        /// Test TradeTicks
        /// </summary>
        [Test]
        public void TradeTicksTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //string market = null;
            //string to = null;
            //decimal? count = null;
            //string cursor = null;
            //decimal? daysAgo = null;
            //var response = instance.TradeTicks(market, to, count, cursor, daysAgo);
            //Assert.IsInstanceOf<Object> (response, "response is Object");
        }
        
    }

}
