user_list = input("Введите значения списка через пробел: ").split()

for i in range(0, len(user_list) - 1, 2):
    temp = user_list[i]
    user_list[i]=user_list[i+1]
    user_list[i+1] = temp

print(user_list)
