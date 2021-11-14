sentence = input("Введите несколько слов через пробел: ")

for i, word in enumerate(sentence.split(), 1):
    print(f"{i} - {word[:10]}")
