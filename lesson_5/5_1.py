with open("5_1.txt", "w") as f:
    while True:
        text = input("Введите текст для записи в файл. Для выхода просто нажмите enter: ")
        if len(text) == 0:
            print("Закончили")
            break
        else:
            f.write(text + "\n")
