class MyComplex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма комплексных чисел равна: {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'Произведение комплексных чисел равно: {self.a * other.a - (self.b * other.b)} + ' \
               f'{self.a * other.b + self.b * other.a} * i'


my_c1 = MyComplex(2, 12)
my_c2 = MyComplex(10, -1)
print(my_c1 + my_c2)
print(my_c1 * my_c2)