from abc import ABC, abstractmethod


class MyException(Exception):
    def __init__(self, text):
        self.text = text


class Equipment(ABC):
    def __init__(self, model, price, *args):
        self.name = ''
        self.model = model
        self.price = price

    @abstractmethod
    def form_equipment_info(self):
        pass

    @classmethod
    def validate_init(cls, model, price, *args):
        try:
            price = float(price)
        except ValueError:
            print(f"Цена {price} оборудования {model} должна быть числом")
            return cls(model, 0, *args)
        else:
            return cls(model, price, *args)


class Division:
    def __init__(self, name):
        self.name = name
        self.equipment = dict()
        self.equipment_cost = dict()

    def get_equipment(self, model: Equipment):
        if self.equipment.get(model.name) is None:
            self.equipment[model.name] = list()
            self.equipment[model.name].append(model)
        else:
            self.equipment[model.name].append(model)

    def calculate_the_cost(self):
        self.equipment_cost = {eq_type: sum(cost) for eq_type, cost in self.equipment.items()}

    def __str__(self):
        s = f'В подразделении {self.name} имеются:\n'
        for t, eq in self.equipment.items():
            for e in eq:
                s += e.form_equipment_info() + '\n'
            s += '\n'
        return s


class Warehouse(Division):
    def __init__(self, name):
        super().__init__(name)
        self.equipment = dict()

    def transfer(self, eq_name: str, model_count: int, division: Division):
        if self.equipment.get(eq_name) is None or len(self.equipment.get(eq_name)) == 0:
            print(f"На складе не осталось {eq_name}")
        elif len(self.equipment[eq_name]) >= model_count:
            print(f"Переводим {len(self.equipment[eq_name])} единиц техники {eq_name} в {division.name}")
            for _ in range(model_count):
                division.get_equipment(self.equipment[eq_name].pop())
        else:
            print(f"Можем перевести только {len(self.equipment[eq_name])} единиц техники {eq_name} в {division.name}")
            for _ in range(len(self.equipment[eq_name])):
                division.get_equipment(self.equipment[eq_name].pop())


class Printer(Equipment):
    def __init__(self, model, price, is_jet: bool):
        super().__init__(model, price)
        self.is_jet = is_jet
        self.name = 'Printer'

    def form_equipment_info(self):
        return f"{self.name} {self.model}, струйный: {self.is_jet}, стоимость {self.price}"


class Scanner(Equipment):
    def __init__(self, model, price, dpi: int):
        super().__init__(model, price)
        self.dpi = dpi
        self.name = 'Scanner'

    def form_equipment_info(self):
        return f"{self.name} {self.model}, dpi: {self.dpi}, стоимость {self.price}"


class Copier(Equipment):
    def __init__(self, model, price, page_count: int):
        super().__init__(model, price)
        self.page_count = page_count
        self.name = 'Copier'

    def form_equipment_info(self):
        return f"{self.name} {self.model}, ресурс страниц: {self.page_count}, стоимость {self.price}"


d = Division("RiskDepartment")
w = Warehouse("Warehouse")

w.get_equipment(Printer.validate_init("Epson L800", 15000, True))
w.get_equipment(Printer.validate_init("Brother T1000", 10000, False))
w.get_equipment(Scanner.validate_init("HP 789", 12000, 1200))
w.get_equipment(Scanner.validate_init("HP 789", "Ab", 1200))
w.get_equipment(Copier.validate_init("Brother C500", 10000, 10000))
w.get_equipment(Copier.validate_init("Samsung C500", 40000, 8000))

print(w)

w.transfer("Printer", 1, d)
w.transfer("Copier", 3, d)
w.transfer("Copier", 1, d)

print()
print(d)

print()
print(w)
