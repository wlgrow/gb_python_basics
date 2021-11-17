def division(num_1, num_2):
    try:
        return round(num_1 / num_2, 4)
    except ZeroDivisionError:
        print("Делить на ноль нельзя")


result = division(float(input("Введите делимое: ")), float(input("Введите делитель: ")))
print(result)
