x = True
y = False

k, v = (2, "s")
_list = [1, 3, "y"]
while (k == 2) and (v == "s") and ("y" in _list):
    print(k, v, _list)
    break
if x or y:
    print("OR")

num1, num2 = 13, float("13")

print(type(num1), type(num2), "\n")
result1 = num1 == num2  # checked base on their values
print(result1)

result2 = num1 is num2  # checks base on their objects class
print(result2)
