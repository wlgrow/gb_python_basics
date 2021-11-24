my_dict = {}
with open("Примеры_файлов/text_6.txt", "r") as f:
    for line in f.readlines():
        my_key, my_val = line.split(":")
        my_val = [int(n.split("(")[0]) for n in my_val.split() if n != "-"]
        my_dict[my_key] = sum(my_val)

print(my_dict)
