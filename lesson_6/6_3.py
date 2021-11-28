class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}

    def get_income(self):
        return self.__income


class Position(Worker):

    def __init__(self, n, s, p, w, b):
        super().__init__(n, s, p, w, b)

    def get_full_name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        income = super().get_income()
        return income["wage"] + income["bonus"]


p1 = Position("Иван", "Иванов", "директор", 50000, 10000)
print(p1.get_full_name())
print(p1.get_total_income())

print()
p2 = Position("Петр", "Петров", "водитель", 30000, 5000)
print(p2.get_full_name())
print(p2.get_total_income())