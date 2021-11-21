initial_list = [300, 2, 12, 40, 1, 2, 0, 200, 200]
new_list = [b for a, b in zip(initial_list, initial_list[1:]) if b > a]
print(new_list)
