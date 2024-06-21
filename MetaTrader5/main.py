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


mt.shutdown()
