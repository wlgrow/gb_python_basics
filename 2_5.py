ratings = [8, 6, 6, 2]

rating = float(input("Введите рейтинг (число): "))
left_neighbour = -1

for i in range(len(ratings)):
    if rating <= ratings[i]:
        left_neighbour = i


ratings.insert(left_neighbour + 1, rating)
print(ratings)
