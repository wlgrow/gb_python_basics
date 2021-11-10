revenue = float(input("Введите выручку: "))
costs = float(input("Введите издержки: "))

result = revenue - costs

if result > 0:
    print(f"Прибыль фирмы составляет {result}")
    profitability = result/revenue
    print(f"Рентабельность фирмы составляет {profitability:.2f}")
    employees = int(input("Введите число ваших работников: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника составляет {result/employees:.2f}")
elif result < 0:
    print(f"Убыток фирмы составляет {result}")
else:
    print("Фирма отработала в ноль")

