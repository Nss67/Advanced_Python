import numpy as np

# Arrays
_list = [4, 3, 5, 7, 1]
print(_list)

array = np.array(_list)
print(array)

print(type(_list))
print(type(array))

print(_list[3])
print(array[3])

_list[3] = 6
array[3] = 2

print(_list[3])
print(array[3])

print(len(_list))
print(array.size)
print(len(array))

_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
array = np.array(_list)

print(_list)
print(array)

print(len(_list))
print(len(array))
print(array.size)

for row in _list:
    print(row)

for row in array:
    print(row)

_list = list(range(1, 10))
array = np.array(_list)

print(_list)
print(array)

for i in range(len(_list)):
    _list[i] += 3

print(_list)
array += 3
print(array)

print("different between arrays sum and lists sum")
lst01 = [1, 2, 3]
lst02 = [4, 5, 6]
print(lst01 + lst02)

array01 = np.array(lst01)
array02 = np.array(lst02)
print(array01 + array02)

print("make a list of 10 zeros")
lst = [0 for i in range(10)]
print(lst)

print("make a array of 10 zeros")
array = np.zeros(10, dtype=np.int8)
print(array)
print()
print("make a 3D array")
array = np.zeros((3, 4, 5), dtype=np.int8)
print(array)
print(f"This array is {array.ndim} dimensional")
print()
print("make a 3D array")
array = np.ones((6, 4, 5), dtype=np.int8)
print(array)
print(f"This array is {array.ndim} dimensional")
print()
print("make a 3D array")
array = np.full((2, 4, 5), 33, dtype=np.int8)
print(array)
print(f"This array is {array.ndim} dimensional")
print()
print("Vector")
print(np.random.random(5))
print(np.random.random(5)*10)
print(np.random.random(5)*100)
print(np.random.random(5)*1000)
x = np.random.random(5) * 100
x = np.array([int(i) for i in x])
print(x)

y = np.random.random(3) * 10
print(y)
print(type(y))
for i in y:
    print(int(i))

array = np.array(list(range(1, 11)))
print(array)
print(array.reshape(5, 2))
print(array)

array.resize(5, 2)
print(array)

print(array.reshape(-1))
array.resize(10)
print(array)
print()
print("line space")
print(np.linspace(0, 21, 5))
print()
print("before Transpose")
array.resize(5, 2)
print(array)
print("Transpose")
print(array.transpose())
print()
print("Numpy range")
_range = np.arange(1, 100, 3)
print(_range)
print(type(_range))
_range.resize(10, 3)
print(_range)
print(_range.ndim)


# # Overflow & Underflow
# x = np.full((3, 3), 127, dtype=np.int8)
# print(x)
# print()
#
# overflow = np.full((3, 3), 128, dtype=np.int8)
# print(overflow)
