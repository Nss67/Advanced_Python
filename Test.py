# x = True
# y = False
#
# k, v = (2, "s")
# _list = [1, 3, "y"]
# while (k == 2) and (v == "s") and ("y" in _list):
#     print(k, v, _list)
#     break
# if x or y:
#     print("OR")
#
# num1, num2 = 13, float("13")
#
# print(type(num1), type(num2), "\n")
# result1 = num1 == num2  # checked base on their values
# print(result1)
#
# result2 = num1 is num2  # checks base on their objects class
# print(result2)
#
# # everything in programing is a number
# name = "Nss67"
# str1 = "a"
# str2 = "A"
# print(len(name))
# name = chr(ord(name[0]) + 2) + name[1:len(name)-1] + str(int(name[4])+2)
# print(name)
# print(chr(ord(str1) + 2))
# print(ord(str1), str1)
# print(ord(str2), str2)
#
# if str1 > str2:
#     print(str1)
#
# else:
#     print(str2)
#
# print(__name__)
#
# if __name__ == "__main__":
#     print("Hello")

# _number1 = int(5)
# _number2 = float(5)
# _horouf = "Amin"
# _booleanT = True
# _booleanF = False
# _dictionary = {"name": "Milad", "Esm": "Amin", "age": 15, "List05": [1, 2, 3, 4, 5, 5, 6]}
# _list = [1, "A", 23, "B"]
# _set = {1, "A", 23, "B"}
# _tuple = (1, 2, 3, "A")
#
# print("A", ord("A"), bin(ord("A"))[2:])
# print("m", ord("m"), bin(ord("m"))[2:])
# print("i", ord("i"), bin(ord("i"))[2:])
# print("n", ord("n"), bin(ord("n"))[2:])
#
# x, y, z = 1, 2, 3
# print(x, y, z)
# print(_horouf[0])
# print(_list[2])
# _list[2] = "HI"
# print(_list[2])
#
# print(_dictionary.keys())


# x = 23
# y = "23"
#
# print(type(x))
# print(type(y))
#
# print(y[0], ord(y[0]), bin(ord(y[0]))[2:])
# print(y[1], ord(y[1]), bin(ord(y[1]))[2:])
# print(x, bin(x)[2:])
#
# x = int(input("ye adad benevis: "))
#
# print(x)
# print(type(x))

# x = 5
# y = "Hi!"
# x_id = id(x)
# y_id = id(y)
# x_hex = hex(x_id)
# y_hex = hex(y_id)
#
# print(x_id)
# print(x_hex)
# print()
# print(y_id)
# print(y_hex)
# print()
# print(type(x), type(x_id), type(x_hex))
# print(type(y), type(y_id), type(y_hex))
#
# print(y_hex)
# hex_y_0 = hex(id(y[0]))
# hex_y_1 = hex(id(y[1]))
# hex_y_2 = hex(id(y[2]))
# print(hex_y_0)
# print(hex_y_1)
# print(hex_y_2)

# name = input("Enter your name: ")
# for i in range(len(name)):
#     print(bin(ord(name[i]))[2:])

# x = input("write something: ")
# y = input("write same thing: ")
#
# print(x == y)
#
# y = x[0].upper()
# print(x, y)
# print(hex(id(x)))
# y = x
# print(hex(id(y)))
# x = x.capitalize()
# print(x, y)
# x_hex = hex(id(x))
# y_hex = hex(id(y))
# print(x_hex)
# print(y_hex)
# print(x_hex == y_hex)


# # Endless for
# x = [1]
# for i in x:
#     print(i)
#     x.append(i + 1)
#     if i > 100:
#         break

# _range_listed = list(range(1, 101))
# print(_range_listed[::-1])
# print(type(_range_listed))

# x = 3
# y = 100
# z = y / 3
# print(f"result is: {z:.5} and type of z is {type(z)}")
# print(f"result is: {z:.5f} and type of z is {type(z)}")

# with open("kuzey_yildizi_S01.txt", mode="w") as file:
#     for i in range(1, 59):
#         if i < 10:
#             file.write(f"https://cld17.hostdl.net/serial/foreign/2020/kuzey-yildizi/Kuzey_Yildizi_E0{i}_1080p.mkv\n")
#         else:
#             file.write(f"https://cld17.hostdl.net/serial/foreign/2020/kuzey-yildizi/Kuzey_Yildizi_E{i}_1080p.mkv\n")
#     file.close()
#
#
# with open("kuzey_yildizi_S02.txt", mode="w") as file:
#     for i in range(1, 71):
#         if i < 10:
#             file.write(f"https://cld17.hostdl.net/serial/foreign/2020/kuzey-yildizi/Kuzey_Yildizi_S02_E0{i}_1080p.mkv\n")
#         else:
#             file.write(f"https://cld17.hostdl.net/serial/foreign/2020/kuzey-yildizi/Kuzey_Yildizi_S02_E{i}_1080p.mkv\n")
#     file.close()

# count = 1


# def repeat(*args):
#     print(*args)
#     global count
#     print(count)
#     count += 1
#     if count <= 10:
#         repeat(*args)
#
#
# repeat(input("Enter some values: "))

# print("normal way")
# for i in range(3):
#     for j in range(3):
#         print("#", end="")
#     print()
#
# print("Easy way")
#
# for i in range(3):
#     print("#" * 3)

# # List Appending
# li = []
# for i in range(3):
#     x = input("Enter some: ")
#     li += [x]
# print(li)

# work with sys library
# import sys
#
# if len(sys.argv) > 2:
#     print("Hi", sys.argv[1])
#     sys.exit()
# else:
#     print("hello world")
#     sys.exit()

# x = 2
# counter = 0
# while True:
#     counter += 1
#     print(counter, "you NotCoin is: ", x)
#     input("please Click!: ")
#     x **= 2

# x = 0
# while True:
#     print("your NotCoin is: ", x)
#     input("please Click!: ")
#     x += 1

