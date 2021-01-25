--[[
  Upbit Open API
 
  ## REST API for Upbit Exchange - Base URL: [https://api.upbit.com] - Official Upbit API Documents: [https://docs.upbit.com] - Official Support email: [open-api@upbit.com] 
 
  OpenAPI spec version: 1.0.0
  Contact: ujhin942@gmail.com
  Generated by: https://github.com/swagger-api/swagger-codegen.git
]]

-- order_chance class
local order_chance = {}
local order_chance_mt = {
	__name = "order_chance";
	__index = order_chance;
}

local function cast_order_chance(t)
	return setmetatable(t, order_chance_mt)
end

local function new_order_chance(bid_fee, ask_fee, market, bid_account, ask_account)
	return cast_order_chance({
		["bid_fee"] = bid_fee;
		["ask_fee"] = ask_fee;
		["market"] = market;
		["bid_account"] = bid_account;
		["ask_account"] = ask_account;
	})
end

return {
	cast = cast_order_chance;
	new = new_order_chance;
}