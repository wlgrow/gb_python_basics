def my_func(x, y):
    if x <= 0:
        print("x должен быть больше нуля")
        return None
    elif y >= 0:
        print("y должен быть меньше нуля")
        return None
    else:
        res = 1
        for i in range(0, y, -1):
            res /= x
        return res


print(my_func(2, -4))
