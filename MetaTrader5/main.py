import time
from datetime import datetime
import pytz
import pandas as pd
import MetaTrader5 as mt

print("version:", mt.__version__)
print("Author:", mt.__author__)

if not mt.initialize():
    print("initialize failed with this error:", mt.last_error())
    quit()

print(mt.version())
# print(mt.terminal_info())

account = 5027186360
connect_to = mt.login(account, password="@pDkDj0g", server="MetaQuotes-Demo")
if connect_to:
    print(f"you are connect to this account: {account} successfully")
else:
    print("your connection is failed, because of this error:", mt.last_error())

connect_to_with_pass = mt.login(account, password="@pDkDj0g", server="MetaQuotes-Demo")
if connect_to_with_pass:
    print(mt.account_info())
    print("show account_info()._asdict():")
    account_info_dict = mt.account_info()._asdict()
    print("\n************ Account information ************")
    for i in account_info_dict:
        print(f"{i} = {account_info_dict[i]}")

    terminal_info_dict = mt.terminal_info()._asdict()
    print("\n************ Termina information ************")
    for i in terminal_info_dict:
        print(f"{i} = {terminal_info_dict[i]}")
else:
    print("failed to connect your account because of :", mt.last_error())


# symbols_total = mt.symbols_total()
# if symbols_total > 0:
#     print(f"Total symbols are {symbols_total}")
# else:
#     print("there is any symbol")
#
# symbols_get = mt.symbols_get()
# print(f"Symbols are {len(symbols_get)}")
#
# count = 0
# for i in symbols_get:
#     count += 1
#     print(f"{count}.{i.name}")
#     if count == 5:
#         break
#
# symbols_get_ru = mt.symbols_get("*RU*")
# print(f"I found {len(symbols_get_ru)} symbols")
#
# count = 0
# for i in symbols_get_ru:
#     count += 1
#     print(f"{count}.{i.name}")
#
# symbols_get_group = mt.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")
# print(f"I find {len(symbols_get_group)} of USD currency")
#
# count = 0
# for i in symbols_get_group:
#     count += 1
#     print(f"{count}.{i.name}")
#
#
# symbols_get_group = mt.symbols_get(group="*USD*,*EUR*,*JPY*,*GBP*")
# print(f"I find {len(symbols_get_group)} of USD currency")
#
# count = 0
# for i in symbols_get_group:
#     count += 1
#     print(f"{count}.{i.name}")
#
#
# symbols_get = mt.symbols_get("XAU*")
# print(f"I find {len(symbols_get)} of USD currency")
#
# count = 0
# for i in symbols_get:
#     count += 1
#     print(f"{count}.{i.name}")
#
#
# selected_symbol = mt.symbol_select("XAUUSD", True)
# if not selected_symbol:
#     print("Failed to select XAUUSD")
#     mt.shutdown()
#     quit()
#
# print(selected_symbol)
#
#
# _symbol_info = mt.symbol_info("XAUUSD")
# if _symbol_info:
#     for i in _symbol_info._asdict():
#         print(f"{i} = {_symbol_info._asdict()[i]}")
#
#     print(f"The symbol name is {_symbol_info.name} that it is stand for {_symbol_info.description}"
#           f" and its spread is {_symbol_info.spread} with {_symbol_info.digits} digits")
#
#
# last_tick = mt.symbol_info_tick("XAUUSD")
# print(last_tick)
#
# for i in last_tick._asdict():
#     print(f"{i} = {last_tick._asdict()[i]}")
#
#
# # if mt.market_book_add("XAUUSD"):
# #     for i in range(2):
# #         items = mt.market_book_get("XAUUSD")
# #         print(items)
# #         if items:
# #             for x in items:
# #                 print(x._asdict())
# #         time.sleep(3)
# #     mt.market_book_release("XAUUSD")
# #
# # else:
# #     print("Market book Failed. Error Code is:", mt.last_error())
#
# timezone = pytz.timezone("Asia/Tehran")
# local_time = datetime.now()
# print(local_time)
#
# # Get 10 candles info for 4H and 15min and 3min timeframe with timezone
# candles_4h = mt.copy_rates_from("XAUUSD", mt.TIMEFRAME_H4, local_time, 10)
# candles_15m = mt.copy_rates_from("XAUUSD", mt.TIMEFRAME_M15, local_time, 10)
# candles_3m = mt.copy_rates_from("XAUUSD", mt.TIMEFRAME_M3, local_time, 10)
#
# print(type(candles_3m))
#
# candles_4h_dataframe = pd.DataFrame(candles_4h)
# candles_4h_dataframe.index = range(1, len(candles_4h_dataframe.index)+1)
# candles_4h_dataframe["time"] = pd.to_datetime(candles_4h_dataframe["time"], unit="s", utc=True)
# candles_4h_dataframe["time"] = candles_4h_dataframe["time"].dt.tz_convert(tz=timezone)
# print(candles_4h_dataframe, "\n")
#
# candles_15m_dataframe = pd.DataFrame(candles_15m)
# candles_15m_dataframe.index = range(1, len(candles_15m_dataframe.index)+1)
# candles_15m_dataframe["time"] = pd.to_datetime(candles_15m_dataframe["time"], unit="s", utc=True)
# candles_15m_dataframe["time"] = candles_15m_dataframe["time"].dt.tz_convert(tz=timezone)
# print(candles_15m_dataframe, "\n")
#
# candles_3m_dataframe = pd.DataFrame(candles_3m)
# candles_3m_dataframe.index = range(1, len(candles_3m_dataframe.index)+1)
# candles_3m_dataframe["time"] = pd.to_datetime(candles_3m_dataframe["time"], unit="s", utc=True)
# candles_3m_dataframe["time"] = candles_3m_dataframe["time"].dt.tz_convert(tz=timezone)
# print(candles_3m_dataframe, "\n")
#
# # Get 10 candle info for 1D timeframe with number of candle bars from now to before
# candles_bar = mt.copy_rates_from_pos("XAUUSD", mt.TIMEFRAME_D1, 0, 10)
# candles_bar_dataframe = pd.DataFrame(candles_bar)
# candles_bar_dataframe.index = range(1, len(candles_bar_dataframe.index)+1)
# candles_bar_dataframe["time"] = pd.to_datetime(candles_bar_dataframe["time"], unit="s", utc=True)
# candles_bar_dataframe["time"] = candles_bar_dataframe["time"].dt.tz_convert(tz=timezone)
# print(candles_bar_dataframe, "\n")
#
# # Get range of candles between two different range times
# time01 = datetime(2023, 6, 25, tzinfo=pytz.utc)
# time02 = datetime(2024, 6, 25, tzinfo=pytz.utc)
# candles_range = mt.copy_rates_range("XAUUSD", mt.TIMEFRAME_W1, time01, time02)
# candles_range_dataframe = pd.DataFrame(candles_range)
# candles_range_dataframe.index = range(1, len(candles_range_dataframe.index)+1)
# candles_range_dataframe["time"] = pd.to_datetime(candles_range_dataframe["time"], unit="s", utc=True)
# candles_range_dataframe["time"] = candles_range_dataframe["time"].dt.tz_convert(tz=timezone)
# print(candles_range_dataframe, "\n")
#
# # Get range ticks from specific date to now in specific number of ticks with flag to define kind of ticks
# specific_date = datetime(2024, 3, 12, tzinfo=pytz.utc)
# count = 1500
# flag = mt.COPY_TICKS_ALL
# tick_range_from = mt.copy_ticks_from("XAUUSD", specific_date, count, flag)
# tick_range_from_dataframe = pd.DataFrame(tick_range_from)
# tick_range_from_dataframe.index = range(1, len(tick_range_from_dataframe.index)+1)
# tick_range_from_dataframe["time"] = pd.to_datetime(tick_range_from_dataframe["time"], unit="s", utc=True)
# tick_range_from_dataframe["time"] = tick_range_from_dataframe["time"].dt.tz_convert(tz=timezone)
# print(tick_range_from_dataframe, "\n")
#
# # Get range ticks from specific date to other specific date with flag to define kind of ticks
# first_specific_date = datetime(2024, 3, 12, tzinfo=pytz.utc)
# second_specific_date = datetime(2024, 6, 12, tzinfo=pytz.utc)
# flag = mt.COPY_TICKS_ALL
# tick_range_from = mt.copy_ticks_range("XAUUSD", first_specific_date, second_specific_date, flag)
# tick_range_from_dataframe = pd.DataFrame(tick_range_from)
# tick_range_from_dataframe.index = range(1, len(tick_range_from_dataframe.index)+1)
# tick_range_from_dataframe["time"] = pd.to_datetime(tick_range_from_dataframe["time"], unit="s", utc=True)
# tick_range_from_dataframe["time"] = tick_range_from_dataframe["time"].dt.tz_convert(tz=timezone)
# print(tick_range_from_dataframe, "\n")
#
# # Get info Account Currency
# balance = mt.account_info().balance
# currency = mt.account_info().currency
# print(f"You account balace is {balance} {currency}")
#
# # calculate the margin
# symbol = "XAUUSD"
# action = mt.ORDER_TYPE_BUY
# lot = 1.0
# ask = mt.symbol_info_tick(symbol).ask
# margin = mt.order_calc_margin(action, symbol, lot, ask)
#
# if margin:
#     print(f"You set order {symbol} / {action} in volume {lot} lot in price {ask} your margin is {margin} {currency}")
# else:
#     print("You don't have order")
#
# print()
#
# # Calculate the profit
# symbol = "XAUUSD"
# lot = 1.0
# distance = 300
# point = mt.symbol_info(symbol).point
# print(point)
# symbol_tick = mt.symbol_info_tick(symbol)
# ask = symbol_tick.ask
# bid = symbol_tick.bid
#
# take_profit = ask + (distance * point)
# print(take_profit, ask, (take_profit - ask))
# action = mt.ORDER_TYPE_BUY
# buy_profit = mt.order_calc_profit(action, symbol, lot, ask, take_profit)
#
# if buy_profit:
#     print(f"Your profit in {symbol} by volume {lot} lot in {distance} point is {buy_profit} {currency}")
# else:
#     print("something is wrong")
#
# take_profit = bid - (distance * point)
# print(bid, take_profit, (bid - take_profit))
# action = mt.ORDER_TYPE_SELL
# sell_profit = mt.order_calc_profit(action, symbol, lot, bid, take_profit)
#
# if sell_profit:
#     print(f"Your profit in {symbol} by volume {lot} lot in {distance} point is {sell_profit} {currency}")
# else:
#     print("something is wrong")
#
# print()

# Set Buy PreOrder
# symbol = "EURUSD"
# point = mt.symbol_info(symbol).point
# tp_distance = 300
# sl_distance = 100
# lot = 10.0
# symbol_info_tick = mt.symbol_info_tick(symbol)
# price = symbol_info_tick.ask
# tp = price + (tp_distance * point)
# sl = price - (sl_distance * point)
# request = {
#     "action": mt.TRADE_ACTION_DEAL,
#     "symbol": symbol,
#     "volume": lot,
#     "type": mt.ORDER_TYPE_BUY,
#     "price": price,
#     "sl": sl,
#     "tp": tp,
#     "deviation": 20,
#     "magic": 234000,
#     "comment": "Python",
#     "type_time": mt.ORDER_TIME_GTC,
#     "type_filling": mt.ORDER_FILLING_RETURN
# }
#
# result = mt.order_check(request)._asdict()
# for i in result:
#     print(i, result[i])
# print()

# Get total order history
timezone = pytz.timezone("Asia/Tehran")
from_date = datetime(2024, 7, 1)
to_date = datetime(2024, 7, 2)
total_history = mt.history_orders_total(from_date, to_date)
total_deals_history = mt.history_deals_total(from_date, to_date)
total_history_group = mt.history_orders_get(from_date, to_date, group="*USD*")
total_deals_history_group = mt.history_deals_get(from_date, to_date, group="*USD*")

if total_history > 0:
    print(total_history)
    print(total_deals_history)
    df = pd.DataFrame(total_deals_history_group, columns=total_deals_history_group[0]._asdict().keys())
    df.index = range(1, len(df.index) + 1)
    df["time"] = pd.to_datetime(df["time"], unit="s", utc=True)
    df["time"] = df["time"].dt.tz_convert(tz=timezone)
    new_df = df[["ticket", "time", "profit", "symbol"]]
    print(new_df)

else:
    print("You have no trade in this account")

# =====================================================
timezone = pytz.timezone("Asia/Tehran")
counter = 10
e_count = 0
trade_number = 0
while counter > 0:
    # Send and Set Order
    symbol = "EURUSD"
    lot = 10.0
    point = mt.symbol_info(symbol).point
    price = mt.symbol_info_tick(symbol).ask
    tp_distance = 15
    sl_distance = 5
    tp = price + (tp_distance * point)
    sl = price - (sl_distance * point)
    deviation = 0
    request = {
        "action": mt.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt.ORDER_TYPE_BUY,
        "price": price,
        "sl": sl,
        "tp": tp,
        "deviation": deviation,
        "magic": 234000,
        "comment": "Good Job Nss67",
        "type_time": mt.ORDER_TIME_GTC,
        "type_filling": mt.ORDER_FILLING_RETURN
    }

    # result = mt.order_check(request)._asdict()
    # for i in result:
    #     print(i, result[i])
    # print()

    result = mt.order_send(request)
    if result.retcode != mt.TRADE_RETCODE_DONE:
        counter += 1
        e_count += 1
        print(f"Order send is failed. Return Code is {result.retcode}")
        result_dict = result._asdict()
        for i in result_dict:
            if i == "comment":
                print(i, result_dict[i])
                print(f"Error number is {e_count}")
            # if i == "request":
            #     trade_request_dict = result_dict[i]._asdict()
            #     for x in trade_request_dict:
            #         print(x, trade_request_dict[x])
        # print("quit")
        # mt.shutdown()
        # quit()

    else:
        # print(f"Order send is done with {result}")
        print(f"Opened position with Position ticket {result.order}")
        print(f"Sleep for 33 seconds before closing position {result.order}")
        trade_number += 1
        print(f"Trade number is {trade_number}")
        while True:
            if mt.positions_total() == 0:
                time.sleep(3)
                break
            # else:
            #     print(symbol)
            #     position = mt.positions_get(symbol=symbol)
            #     position_dataframe = pd.DataFrame(position, columns=position[0]._asdict().keys())  # P:2839
            #     position_dataframe.index = range(1, len(position_dataframe.index) + 1)
            #     position_dataframe["time"] = pd.to_datetime(position_dataframe["time"], unit="s", utc=True)
            #     position_dataframe["time"] = position_dataframe["time"].dt.tz_convert(tz=timezone)
            #     print(position_dataframe, "\n")
            #     time.sleep(3)

    counter -= 1


# # Create a close request
# position_id = result.order
# price = mt.symbol_info_tick(symbol).bid
# deviation = 20
# request = {
#     "action": mt.TRADE_ACTION_DEAL,
#     "symbol": symbol,
#     "volume": lot,
#     "type": mt.ORDER_TYPE_SELL,
#     "position": position_id,
#     "price": price,
#     "deviation": deviation,
#     "magic": 234000,
#     "comment": "I DID THIS :)",
#     "type_time": mt.ORDER_TIME_GTC,
#     "type_filling": mt.ORDER_FILLING_RETURN
# }
#
# result = mt.order_send(request)
# if result.retcode != mt.TRADE_RETCODE_DONE:
# result_dict = result._asdict()
# for i in result_dict:
#     print(i, result_dict[i])
#
# time.sleep(3)
#
# mt.shutdown()

# Get number of active orders
# orders = mt.orders_total()
# if orders > 1:
#     print(f"You have {orders} active orders")
# elif orders == 1:
#     print("You have 1 active order")
# else:
#     print("You don't have any active order")
#
# # Get number of active orders with symbol param
# orders_symbol = mt.orders_get(symbol="XAUUSD")
# if len(orders_symbol) > 1:
#     print(f"You have {len(orders_symbol)} active orders")
# elif len(orders_symbol) == 1:
#     print("You have 1 active order")
# else:
#     print("You don't have any active order")
#
# # Get number of active orders with group param
# orders_group = mt.orders_get(group="*USD*")
# if len(orders_group) > 1:
#     print(f"You have {len(orders_group)} active orders")
# elif len(orders_group) == 1:
#     print("You have 1 active order")
# else:
#     print("You don't have any active order")

mt.shutdown()
