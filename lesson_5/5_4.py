digits_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("Примеры_файлов/text_4.txt", "r") as f:
    open("5_4.txt", "w").close()
    for line in f.readlines():
        eng = line.split()[0]
        rus_line = line.replace(eng, digits_dict[eng])
        with open("5_4.txt", "a") as r:
            print(rus_line, file=r, end="")
