class MyException(Exception):
    def __init__(self, text):
        self.text = text


class TypeCheck:
    def __init__(self):
        self.result = []

    def combine_list(self):
        while True:
            n = input("Введите число для добавления в список (stop для выхода): ")
            if n == "stop":
                break
            try:
                if n.isdigit():
                    self.result.append(int(n))
                else:
                    raise MyException("Вы ввели не число")
            except MyException as e:
                print(f"Невалидные входные данные: {e}")
        print(self.result)


c = TypeCheck()
c.combine_list()
