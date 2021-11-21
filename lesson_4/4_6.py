from itertools import count, cycle


def first(n):
    for i in count(n):
        if i > n + 20:
            break
        else:
            print(i)


def second(my_list, n):
    """
    итератор, повторяющий элементы некоторого списка, определенного заранее
    :param my_list: список
    :param n: сколько раз необходимо повторять cycle
    :return:
    """
    for i, j in enumerate(cycle(my_list)):
        if i >= n * len(my_list):
            break
        else:
            print(j)


print("First function:")
first(5)
print("\nSecond function:")
second([2, 3, 4, 5, 6], 2)
