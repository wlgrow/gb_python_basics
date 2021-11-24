lines_dict = {}

with open("5_2.txt", "r") as f:
    for i, line in enumerate(f.readlines(), start=1):
        lines_dict[i] = len(line.split())

for k,v in lines_dict.items():
    print(f"строка {k} содержит {v} слов")
