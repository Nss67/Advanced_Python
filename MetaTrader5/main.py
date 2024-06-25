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

account = 10003383653
connect_to = mt.login(account, password="VuFgPr*3", server="MetaQuotes-Demo")
if connect_to:
    print(f"you are connect to this account: {account} successfully")
else:
    print("your connection is failed, because of this error:", mt.last_error())

connect_to_with_pass = mt.login(account, password="VuFgPr*3", server="MetaQuotes-Demo")
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


symbols_total = mt.symbols_total()
if symbols_total > 0:
    print(f"Total symbols are {symbols_total}")
else:
    print("there is any symbol")

symbols_get = mt.symbols_get()
print(f"Symbols are {len(symbols_get)}")

count = 0
for i in symbols_get:
    count += 1
    print(f"{count}.{i.name}")
    if count == 5:
        break

symbols_get_ru = mt.symbols_get("*RU*")
print(f"I found {len(symbols_get_ru)} symbols")

count = 0
for i in symbols_get_ru:
    count += 1
    print(f"{count}.{i.name}")

symbols_get_group = mt.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")
print(f"I find {len(symbols_get_group)} of USD currency")

count = 0
for i in symbols_get_group:
    count += 1
    print(f"{count}.{i.name}")


symbols_get_group = mt.symbols_get(group="*USD*,*EUR*,*JPY*,*GBP*")
print(f"I find {len(symbols_get_group)} of USD currency")

count = 0
for i in symbols_get_group:
    count += 1
    print(f"{count}.{i.name}")


symbols_get = mt.symbols_get("XAU*")
print(f"I find {len(symbols_get)} of USD currency")

count = 0
for i in symbols_get:
    count += 1
    print(f"{count}.{i.name}")


selected_symbol = mt.symbol_select("XAUUSD", True)
if not selected_symbol:
    print("Failed to select XAUUSD")
    mt.shutdown()
    quit()

print(selected_symbol)


_symbol_info = mt.symbol_info("XAUUSD")
if _symbol_info:
    for i in _symbol_info._asdict():
        print(f"{i} = {_symbol_info._asdict()[i]}")

    print(f"The symbol name is {_symbol_info.name} that it is stand for {_symbol_info.description}"
          f" and its spread is {_symbol_info.spread} with {_symbol_info.digits} digits")


last_tick = mt.symbol_info_tick("XAUUSD")
print(last_tick)

for i in last_tick._asdict():
    print(f"{i} = {last_tick._asdict()[i]}")


# if mt.market_book_add("XAUUSD"):
#     for i in range(2):
#         items = mt.market_book_get("XAUUSD")
#         print(items)
#         if items:
#             for x in items:
#                 print(x._asdict())
#         time.sleep(3)
#     mt.market_book_release("XAUUSD")
#
# else:
#     print("Market book Failed. Error Code is:", mt.last_error())

timezone = pytz.timezone("Asia/Tehran")
local_time = datetime.now()
print(local_time)

# Get 10 candles for 4H time frame
candles_4h = mt.copy_rates_from("XAUUSD", mt.TIMEFRAME_H4, local_time, 10)
candles_15m = mt.copy_rates_from("XAUUSD", mt.TIMEFRAME_M15, local_time, 10)
candles_3m = mt.copy_rates_from("XAUUSD", mt.TIMEFRAME_M3, local_time, 10)

print(type(candles_3m))

candles_4h_dataframe = pd.DataFrame(candles_4h)
candles_4h_dataframe.index = range(1, len(candles_4h_dataframe)+1)
candles_4h_dataframe["time"] = pd.to_datetime(candles_4h_dataframe["time"], unit="s", utc=True)
candles_4h_dataframe["time"] = candles_4h_dataframe["time"].dt.tz_convert(tz=timezone)
print(candles_4h_dataframe, "\n")

candles_15m_dataframe = pd.DataFrame(candles_15m)
candles_15m_dataframe.index = range(1, len(candles_15m_dataframe)+1)
candles_15m_dataframe["time"] = pd.to_datetime(candles_15m_dataframe["time"], unit="s", utc=True)
candles_15m_dataframe["time"] = candles_15m_dataframe["time"].dt.tz_convert(tz=timezone)
print(candles_15m_dataframe, "\n")

candles_3m_dataframe = pd.DataFrame(candles_3m)
candles_3m_dataframe.index = range(1, len(candles_3m_dataframe)+1)
candles_3m_dataframe["time"] = pd.to_datetime(candles_3m_dataframe["time"], unit="s", utc=True)
candles_3m_dataframe["time"] = candles_3m_dataframe["time"].dt.tz_convert(tz=timezone)
print(candles_3m_dataframe, "\n")

mt.shutdown()
