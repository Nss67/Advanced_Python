

class Box:
    def __init__(self):
        self.value = 2
        self._value = 4
        self.__value = 9


inst = Box()
print(inst.value)
print(inst._value)
print(inst.__dict__)
print(inst._Box__value)
