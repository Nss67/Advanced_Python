# variables Scope types

print("-------Local variables-------")
x = 4


def myf(x):
    print("Local variable is:", x)
    x += 2
    print("Local variable is:", x)


myf(5)
print("Global variable is:", x)
print("----------------------------")


print("-------Global variables-------")
x = 2
print("Global variable", x)


def myf():
    global x  # referencing access to the global variable
    x += 3
    print("Global variable is:", x)


myf()
print("Global variable is:", x)
print("------------------------------")


print("-------NonLocal Variables-------")
x = 10


def myf1():
    x = 2
    print("Local variable is:", x)

    def myf2():
        nonlocal x  # referenced to the local variable
        x += 3
        print("Nonlocal variable is:", x)

        def myf3():
            global x  # referenced to the global variable
            print("Global variable is:", x)

        myf3()

    myf2()


myf1()

