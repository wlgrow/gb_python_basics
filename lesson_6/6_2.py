class Road:

    def __init__(self, length: int, width: int):
        self.__length = length
        self.__width = width

    # returns asphalt mass in tons
    def calc(self, weight: int, thickness: int):
        return self.__length * self.__width * weight * thickness / 1000


r = Road(20, 5000)
print(r.calc(25, 5))
