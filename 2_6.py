goods= []

while True:
    good_info = input("Введите сведения о товаре через пробел в следующем порядке (название, цена, кол-во, ед.изм.). Чтобы выйти, введите 0: ")
    if good_info == '0':
        break
    good_info_list = good_info.split()
    temp_dict = {"name": good_info_list[0], "price": float(good_info_list[1]),
                 "amount": float(good_info_list[2]), "measure": good_info_list[3]}
    goods.append((len(goods)+1, temp_dict))

print("Структура данных:")
print(goods)


# goods = [
#     (1, {"name": "книга", "price": 100, "amount": 999, "measure": "шт"}),
#     (2, {"name": "ручка", "price": 5, "amount": 300, "measure": "шт"}),
#     (3, {"name": "чернила", "price": 500, "amount": 20, "measure": "л"})
# ]

result = {}

for n in goods:
    for k, v in n[1].items():
        if result.get(k) is None:
            result[k] = []
            result[k].append(v)
        else:
            result[k].append(v)

print("Итоговый словарь: ")
print(result)
