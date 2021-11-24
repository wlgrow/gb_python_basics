with open("5_5.txt", "w+") as f:
    f.write(input("Введите числа разделенные пробелом: "))
    f.seek(0)
    print(f"Сумма чисел: {sum(map(int, f.readline().split()))}")
