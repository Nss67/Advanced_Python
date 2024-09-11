import builtins

import matplotlib.pyplot as plt
from matplotlib import colors
from random import randint as rnd

# # hard way
# p1_x, p1_y = 3, 4
# p2_x, p2_y = 7, 5
# p3_x, p3_y = 6, 8
#
# plt.plot([p1_x, p2_x, p3_x], [p1_y, p2_y, p3_y])
#
# #  easy way
# x = [3, 7, 6, 3]
# y = [4, 5, 8, 4]
#
# plt.plot(x, y)

# # random values plot chart
# x = list(range(25))
# y = [rnd(-10, 10) for i in range(25)]
# z = [rnd(-10, 10) for n in range(25)]
# print(len(x), len(y), len(z))
#
# plt.figure(figsize=(10, 5))
# plt.title("Random Numbers \n -10 to 10")
# plt.xlabel("Time")
# plt.ylabel("Value")
#
# plt.plot(x, y, label="BTC Price", color="red")
# plt.plot(x, z, label="ETH Price", color=(0.1, 0.5, 0.9))
# plt.legend()
# plt.grid()


# # Bar chart
# x = ["Me", "Sister", "Mother", "Father"]
# y = [(1403 - 1367), (1403 - 1358), (1403 - 1339), (1403 - 1334)]
# c = ["red", "green", "blue", "brown"]
#
# plt.bar(x, y, label="My Family Age", color=c)
# plt.plot(x, y)
#
# # plt.barh(x, y, label="My Family Age", color=c)
#
# plt.legend()
# plt.grid()

# Pie chart
# name = ["Python", "C++", "Swift", "Java", "PHP", "Go"]
# values = [15, 10, 7, 5, 6, 10]
#
# plt.pie(values, labels=name, startangle=180, colors=colors.BASE_COLORS, hatch=["/", "o", "--", "++", "\\", "||"],
#         autopct="%2.2f%%")
# plt.pie([100], colors=["white"], radius=0.8)

# plt.show()

# # Modern Pie Chart
# values = [60, 50, 40, 10, 9, 8, 7, 6, 5]
# color = ["#191871", "#011FF3", "#023AE4", "#0156D5", "#0070C6", "#018DBA", "#06A9AA", "#0CC39B", "#57E6AC"]
# labels = ["50 - 70 KM", "25 - 50 KM", "10 - 25 KM", "5 - 10 KM", "3 - 5 KM", "2 -3 KM", "1 - 2 KM", "0 KM", " < 0 KM"]
#
# plt.title("Speed of Cars")
# plt.pie(values, labels= labels, colors=color, explode=[0, 0, 0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3])
#
# plt.savefig("./Figs/Modern_Pie_Graph.png")
# plt.show()


# Scatter Plot
def r_points(num, _min, _max):
    points = [rnd(_min, _max) for i in range(num)]
    return points


b_age = r_points(33, 0, 18)
b_speed = r_points(33, 0, 115)

o_age = r_points(33, 0, 18)
o_speed = r_points(33, 0, 115)

plt.title("Car age vs Speed")
plt.ylabel("Speed of cars")
plt.xlabel("Age of cars")

# plt.scatter(b_age, b_speed, label="BMW", alpha=0.75)
# plt.scatter(o_age, o_speed, label="RAM", alpha=0.75)

# plt.scatter(b_age, b_speed, c=r_points(33, 100, 500), cmap="magma", s=90, edgecolors="green", linewidths=1,
#             label="BMW", alpha=0.75)

# plt.scatter(b_age, b_speed, c=r_points(33, 100, 500), cmap="magma",
#             s=r_points(33, 50, 250), edgecolors="green", linewidths=1, label="BMW", alpha=0.75)

plt.scatter(b_age, b_speed, marker="^", c=r_points(33, 100, 500), cmap="magma",
            s=r_points(33, 50, 250), edgecolors="green", linewidths=1, label="BMW", alpha=0.75)

plt.colorbar().set_label("Engine Power\n(100 - 500)")

plt.grid()
plt.legend()

plt.show()

