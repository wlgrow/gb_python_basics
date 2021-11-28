import random


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name}. Я еду")

    def stop(self):
        print(f"{self.name}. Я остановилась")

    def turn(self, direction):
        print(f"{self.name}. Я повернула {direction}")

    def show_speed(self):
        print(f"{self.name}. Моя скорость {self.speed}")


class TownCar(Car):

    def __init__(self, s, c, n, i):
        super().__init__(s, c, n, i)

    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name}. Превышение скорости 60 км/ч. Моя скорость {self.speed}")
        else:
            print(f"{self.name}. Моя скорость {self.speed}")


class SportCar(Car):

    def __init__(self, s, c, n, i):
        super().__init__(s, c, n, i)


class WorkCar(Car):

    def __init__(self, s, c, n, i):
        super().__init__(s, c, n, i)

    def show_speed(self):
        if self.speed > 40:
            print(f"{self.name}. Превышение скорости 40 км/ч. Моя скорость {self.speed}")
        else:
            print(f"{self.name}. Моя скорость {self.speed}")


class PoliceCar(Car):

    def __init__(self, s, c, n, i):
        super().__init__(s, c, n, i)


tc = TownCar(random.randint(1, 120), "black", "mazda", False)
tc.go()
tc.turn("направо")
tc.show_speed()
tc.stop()

print()

sc = SportCar(random.randint(1, 120), "red", "ferrari", False)
sc.go()
sc.turn("направо")
sc.show_speed()
sc.stop()

print()

wc = WorkCar(random.randint(1, 120), "brown", "lada", False)
wc.go()
wc.turn("налево")
wc.show_speed()
wc.stop()

print()

pc = PoliceCar(random.randint(1, 120), "red", "ford", True)
pc.go()
pc.turn("направо")
pc.show_speed()
pc.stop()
