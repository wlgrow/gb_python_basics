class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        result = Cell(self.cell - other.cell)
        if result.cell < 0:
            print("При вычитании образовалась отрицательная разница")
        return result if result.cell > 0 else Cell(0)

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, row):
        for i in range(self.cell // row):
            print("*" * row)
        print("*" * (self.cell % row) + "\n")


c1 = Cell(7)
c2 = Cell(3)

sum = c1 + c2
print(sum.cell)
sum.make_order(5)

sub = c1 - c2
print(sub.cell)
sub.make_order(5)

mul = c1*c2
print(mul.cell)
mul.make_order(5)

res = c1/c2
print(res.cell)
res.make_order(5)