print(type(3))
print(type("Hello, world"))
print(type(int))
print(type(str))

print("=============================================================")
class StaticDogs:
    def __init__(self):
        self.gen = "Corgi"
        self.weight = "25/kg"

    def sound(self):
        self.weight = "22/kg"
        print("Woof Woof")


jimmy = StaticDogs()
print(jimmy.__dict__)
jimmy.sound()
print(jimmy.__dict__)


def const(self):
    self.gen = "Golden Retriever"
    self.weight = "32/kg"


def dog_sound(self):
    self.weight = "28/kg"
    print("Hoop Hoop")


DynamicDogs = type("Dogs Collection", (), {
    "__init__": const,
    "sound": dog_sound
})

teddy = DynamicDogs()
print(teddy.__dict__)
teddy.sound()
print(teddy.__dict__)
print("=============================================================")


class Cat:
    def __init__(self):
        self.sound = "Meewiouw"


ginger = Cat()
print(ginger.sound)
print(type(ginger))


def constractor(self):
    self.sound = "Maaaawooooo"


Cats = type("Catss", (), {"__init__": constractor})

finger = Cats()
print(finger.sound)
print(type(finger))


def bigger(self):
    self.show = "Woow"


Show = type("Shows", (), {"__init__": bigger})

channel = Show()
print(channel.show)
print(type(channel))

print(channel.__dict__)
