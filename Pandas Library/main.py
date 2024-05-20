import pandas as pd

data = [
    ["May", 31, "Spring"],
    ["Jun", 30, "Spring"],
    ["April", 30, "Spring"],
    ["August", 31, "Summer"]
]

df = pd.DataFrame(data, columns=["Month", "Days", "Season"], index=[1, 2, 3, 4])

print("\n", df)

file01 = pd.read_csv("InputData.txt")
print(file01.index)

file01.index = range(1, 6, 1)

print("\n", file01)


file02 = pd.read_csv("weather.txt")
file02.index = range(1, (len(file02.index)+1), 1)

_head = file02.head()
_tail = file02.tail()

limited_head = file02.head(3)
limited_tail = file02.tail(3)

print(_head)
print(_tail)

print(limited_head)
print(limited_tail)

print(file02.dtypes)
print(file02)
print(file02.describe())
print()
print(file02["avg_high"].describe())
print()
lst_avg_high = list(file02["avg_high"])
print(lst_avg_high)
print()
mean = sum(lst_avg_high) / len(lst_avg_high)
# print(f"{mean} is same {file02.describe("mean")}")
