# variables Scope types

# local variable
def myf(x):
    x += 1
    print(x)


myf(5)


y = 4


# Global Variables
def myb():
    global y
    y += 3
    print(y)


myb()
print(y)


# Nonlocal Variable
c = 13


def myf1():
    global c
    c += 3
    print(c)
    v = 5
    print(v)

    def myf2():
        nonlocal v
        v += 3
        print(v)

    myf2()


myf1()
print(c)
