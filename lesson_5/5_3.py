lines_dict = {}
with open("Примеры_файлов/text_3.txt", "r") as f:
    for line in f.readlines():
        lines_dict[line.split()[0]] = float(line.split()[1])

filtered = {k: v for k, v in lines_dict.items() if v < 20000}

print(f"Фамилии сотрудников с окладом меньше 20 000: {', '.join(filtered.keys())}")
print(f"Средний доход: {sum(lines_dict.values())/len(lines_dict)}")
