print(type(3))
print(type("Hello, world"))
print(type(int))
print(type(str))


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
