import pandas as pd

data = [
    ["May", 31, "Spring"],
    ["Jun", 30, "Spring"],
    ["April", 30, "Spring"],
    ["August", 31, "Summer"]
]

df = pd.DataFrame(data, columns=["Month", "Days", "Season"], index=[1, 2, 3, 4])

print("\n", df, "\n")
print(df.columns, "\n")
print(df.values, "\n")
print(f"This array is {df.ndim} dimensional\n")
print(df.index, "\n")

file01 = pd.read_csv(r"Files/InputData.txt")

print(file01.index)
# # way 01
# file01.index = range(1, 6, 1)

# # way 02
# start = file01.index.start + 1
# stop = file01.index.stop + 1
# step = file01.index.step
# file01.index = range(start, stop, step)

# way 3 the best
file01.index = range(1, len(file01.index)+1, 1)

print("\n", file01, "\n")


file02 = pd.read_csv(r"Files/weather.txt")
file02.index = range(1, len(file02.index)+1, 1)
print("\n", file02, "\n")

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
print(mean)
_mean = file02["avg_high"].mean()
print(f"{mean} is same {_mean}")
print()
file02.info()
print()
print(file02["avg_low"])
print()
print(file02.avg_low)
print()
print(file02[["month", "avg_precipitation"]])
print(file02["month"][3])

_save = file02[["month", "avg_precipitation"]]
_save.to_csv("./Files/new_weather.txt")

print()
print(file02)

file02.columns = ["a", "b", "c", "d", "e", "f"]
print()
print(file02)
print()
print(file02.columns)

file02.rename(columns={"b": "month", "f": "avg_precipitation"}, inplace=True)
print()
print(file02)
print()

file02 = pd.read_csv("./Files/weather.txt")
file03 = pd.read_csv("./Files/weather.txt", usecols=["month", "avg_high", "record_high", "avg_precipitation"])
print(file02)
print()
print(file03)
print()
