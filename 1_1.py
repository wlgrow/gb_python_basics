years = 5
print("число лет для расчета", years)

name = input("Введите ваше имя: ")
age = int(input("Введите ваш возраст: "))
position = input("Ваша должность: ")
salary = float(input("Ваша зарплата: "))

if salary >= 0:
    print(f"{name}, ваш возраст {age} и ваша должность - {position}. "
          f"К {age+years} годам вы заработаете {salary*12*years:.2f}")
else:
    print("Значение зарплаты должно быть положительным")

