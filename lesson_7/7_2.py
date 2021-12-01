from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, p):
        self.p = p

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    def fabric_consumption(self):
        return round(self.v/6.5 + 0.5, 2)

    @property
    def v(self):
        return self.__v

    # сеттер для создания свойств
    @v.setter
    def v(self, v):
        if v < 0:
            self.__v = 0
        elif v > 20:
            self.__v = 20
        else:
            self.__v = v


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    def fabric_consumption(self):
        return round(2*self.h + 0.3, 2)

    @property
    def h(self):
        return self.__h

    # сеттер для создания свойств
    @h.setter
    def h(self, h):
        if h < 0:
            self.__h = 0
        elif h > 10:
            self.__h = 10
        else:
            self.__h = h


class Fabric:
    def __init__(self):
        self.clothes = []

    def add_clothes(self, p, name):
        self.clothes.append(Coat(p) if name == "coat" else Suit(p))

    def common_fabric_consumption(self):
        fabric = 0
        for el in self.clothes:
            fabric += el.fabric_consumption()
        return round(fabric, 2)


f = Fabric()
f.add_clothes(20, "coat")
f.add_clothes(10, "suit")
print(f"Полный расход ткани: {f.common_fabric_consumption()}")