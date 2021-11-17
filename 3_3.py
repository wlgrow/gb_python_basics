def my_func(*args):
    return sum(args) - min(args)


res = my_func(1, 4, 2)
print(res)
