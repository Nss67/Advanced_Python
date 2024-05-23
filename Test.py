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

# everything in programing is a number
name = "Nss67"
str1 = "a"
str2 = "A"
print(len(name))
name = chr(ord(name[0]) + 2) + name[1:len(name)-1] + str(int(name[4])+2)
print(name)
print(chr(ord(str1) + 2))
print(ord(str1), str1)
print(ord(str2), str2)

if str1 > str2:
    print(str1)

else:
    print(str2)

print(__name__)

if __name__ == "__main__":
    print("Hello")
