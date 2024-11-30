class Constant:
    __slots__ = ()
    PI = 3.14
    Name = "Nss67"

    @staticmethod
    def sound():
        print("Go Go Go")


obj = Constant()
print(obj.PI)
print(obj.Name)
obj.sound()

# read-only error
# obj.PI = 5
# obj.Name = "MNH"


class Constant:
    PI = 3.142
    Name = "Boxer"

    def sound(self):
        print("=====================")
        print("Booom Booom")
        print(self.PI)
        print(self.Name)
        print("=====================")


obj = Constant()
print(obj.PI)
print(obj.Name)
obj.sound()

# There is you can change your class variables
obj.PI = 5
obj.Name = "Bomber"
obj.sound()
