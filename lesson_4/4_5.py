from functools import reduce


def my_multiple(prev_el, cur_el):
    return prev_el * cur_el


my_gen = (i for i in range(100, 1001) if i % 2 == 0)
print(f"Результат перемножения всех четных цифр от 100 до 1000 = {reduce(my_multiple, my_gen)}")
