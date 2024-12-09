

class A:
    def __init__(self, value):
        self.value = value
        self.line = "="*100
        self.message = "Hello, World"

    def __str__(self):
        return self.message

    def __add__(self, other):
        print(self.line)
        print(self.value)
        print(other.value)
        print(self.line)
        print(self.value * other.value)
        print(self.value - other.value)
        return self.value + other.value


class B:

    def __init__(self):
        # super().__init__(self)
        print("a call to the constractor method.")

    def __new__(cls):
        print("a call to the __new__ method.")
        return object.__new__(cls)

    def __del__(self):
        print("a call to destructor method")


if __name__ == "__main__":

    x = A(25)
    print(x)
    print(x.value)

    x.message = "Woof Woof!!"
    print(x)
    x.value = 45
    print(x)
    print(x.value)

    x = A(55)
    y = A(88)
    print(x)
    print(y)

    z = x + y
    print(z)

    new_class = B()
    print(new_class)
    del new_class
    print("End App")

    first_instance = A(66)
    second_instance = B()

    class EmptyClass:
        pass

    cc = EmptyClass()
    print(dir(cc))
    print(dir(second_instance))
    print(dir(first_instance))


