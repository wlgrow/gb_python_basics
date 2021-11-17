def int_func(text: str):
    return text.capitalize()


def my_func(text):
    return " ".join(map(int_func, text.split()))


print(my_func(input("Введите строку из нескольки слов на латинице: ")))
