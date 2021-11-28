class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print(f"Запуск отрисовки ручкой: {self.title}")


class Pencil(Stationery):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print(f"Запуск отрисовки карандашом: {self.title}")


class Handle(Stationery):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        print(f"Запуск отрисовки маркером: {self.title}")


pen = Pen("parker")
pen.draw()

pencil = Pencil("brauberg")
pencil.draw()

handle = Handle("marker")
handle.draw()
