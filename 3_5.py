def my_int(x):
    """
    Converts input arg into int. In case of error returns 0
    :param x: any symbol
    :return: integer
    """
    try:
        return int(x)
    except ValueError:
        print("Среди введенных вами символов встречаются НЕ цифры")
        return 0


res = 0
while True:
    ints = input("Введите строку чисел, разделенных пробелом (для выхода введите q): ").split()
    res += sum(map(my_int, ints))
    print(f"Сумма всех введенных ранее чисел {res}")
    if "q" in ints:
        break

