class MyException(Exception):
    def __init__(self, text):
        self.text = text


try:
    d1, d2 = map(float, input("Введите делимое и делитель через пробел: ").split())
    if d2 == 0:
        raise MyException("Делить на ноль нельзя!")
    else:
        print(d1/d2)
except ValueError:
    print("Невалидные входные данные")
