class MyException(Exception):
    def __init__(self, message):
        self.message = message


class MyDate:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def parse_date(cls, str_date):
        result = []
        for i in str_date.split("-"):
            try:
                result.append(int(i))
            except ValueError:
                print("Введены не числовые данные")
                result.append(1)
        return cls(f"{result[0]}-{result[1]}-{result[2]}")

    @staticmethod
    def date_validation(obj):
        d, m, y = map(int, obj.str_date.split("-"))
        month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        month_dict2 = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if y % 4 == 0:
            if month_dict.get(m) is None or d <= 0 or d > month_dict2[m]:
                print("Invalid date format")
            else:
                print(f"день {d}, месяц {m}, год {y}")
        else:
            if month_dict.get(m) is None or d <= 0 or d > month_dict[m]:
                print("Invalid date format")
            else:
                print(f"день {d}, месяц {m}, год {y}")


my_date = MyDate.parse_date("01-12-21")
MyDate.date_validation(my_date)
