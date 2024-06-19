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
file03 = pd.read_csv("./Files/weather.txt", usecols=["avg_high", "month", "record_high", "avg_precipitation"])
print(file02)
print()
print(file03)
print()

file03["new_column"] = list(range(1, len(file03)+1))
print(file03)
print()

#  safe way to add new column
file03["new_avg"] = ((file03["avg_high"] + file03["avg_precipitation"]) * file03["new_column"])
print(file03)
print()

# other way to add new column
file03["new_avg"] = ((file03.avg_high + file03.avg_precipitation) * file03.new_column)
print(file03)
print()

file03.index = range(1, len(file03.index)+1)
print(file03)
print()

# Slicing
print(file03.loc[5:9])
print()

print(file03.loc[5:9, ["avg_high", "month", "new_avg"]])
print()

print(file03.iloc[5:9, [1, 0, 5]])
print()

print(file03[file03.avg_precipitation > 1])
print()

print(file03[file03.avg_precipitation > 1].loc[1:4, ["avg_high", "month", "avg_precipitation"]])
print()

print(file03[file03["month"].isin(["Feb", "Jan", "Apr"])])
print()

file03.to_csv("./Files/new_save.txt")

file04 = pd.read_csv("./Files/new_save.txt")
print(file04)
print()

file04.rename(columns={"Unnamed: 0": " "}, inplace=True)
print(file04)
print()
print(file04.columns)
print(file04.index)
print()

file04.set_index(" ", inplace=True)
print(file04)
print()
print(file04.columns)
print(file04.index)
print()

# Save file without indexes
file03.to_csv("./Files/New_Save_without_indexes.csv", index=False)

file05 = pd.read_csv("./Files/New_Save_without_indexes_NaN.csv")
file05.index = range(1, len(file05)+1)
print(file05)
print()
print(file05.columns)
print(file05.index)
print()

# remove NaN values
print(file05)
print()
file05.dropna(inplace=True)
print(file05)
print()

file05 = pd.read_csv("./Files/New_Save_without_indexes_NaN.csv")
file05.index = range(1, len(file05)+1)
print(file05)
print()

file05.fillna(1000, inplace=True)
print(file05)
print()

from random import randint as rnd

_data = [f"{rnd(1, 12)}/{rnd(1, 29)}/{rnd(1988, 2024)}" for i in range(len(file05.index))]
print(_data)
print()

file05["Date"] = _data
print(file05)
print()
file05.info()
print()

file05["Date"] = pd.to_datetime(file05["Date"])
print(file05)
print()
file05.info()
print()

print(file05.to_string())

# remove duplicated rows
file06 = pd.read_csv("./Files/new_weather_duplicated.txt")
file06.index = range(1, len(file06.index)+1)
print(file06.duplicated())

file07 = file06.drop_duplicates()

file07.index = range(1, len(file07.index)+1)
print(file07.duplicated())
print()
print(file06)
print()
print(file07)
