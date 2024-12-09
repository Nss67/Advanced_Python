

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I don.t have any song"


class Dog(Animal):
    def speak(self):
        return "Hoop Hoop"


class Cat(Animal):
    def speak(self):
        return "Mio Mio"


teddy = Animal("Teddy")
peaty = Dog("Peaty")
jerry = Cat("Jerry")

print(teddy.speak())
print(peaty.speak())
print(jerry.speak())
