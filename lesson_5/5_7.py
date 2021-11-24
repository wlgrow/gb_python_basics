import json

my_dict = {}
with open("Примеры_файлов/text_7.txt", "r") as f:
    for line in f.readlines():
        company = line.split()[0]
        fin_res = float(line.split()[2]) - float(line.split()[3])
        my_dict[company] = fin_res

filtered = {k: v for k, v in my_dict.items() if v > 0}
result = sum(filtered.values()) / len(filtered)

with open("5_7.json", "w", encoding='utf-8') as f:
    json.dump([my_dict, {"average_profit": result}], f, ensure_ascii=False, indent=4)
