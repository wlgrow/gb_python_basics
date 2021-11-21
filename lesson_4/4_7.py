from itertools import count
from math import factorial


def fact(n):
    for i in count(1):
        if i > n:
            break
        else:
            yield factorial(i)


def my_func(n):
    for i, el in enumerate(fact(n)):
        print(el)


my_func(5)

