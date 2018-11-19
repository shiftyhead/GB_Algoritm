"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найти в массиве медиану. Медианой называется элемент ряда, делящий его
на две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше ее.
"""
import random

M = 5

array = [random.randint(0, 100) for _ in range(2 * M + 1)]
print(f'дан массив: {array}')
# print(sorted(array), sorted(array)[M])


count = [[0, 0] for i in range(len(array))]

for key_i, val_i in enumerate(array):
    for val_j in array:
        if val_j < val_i:
            count[key_i][0] += 1
        elif val_j > val_i:
            count[key_i][1] += 1

res = [array[key] for key, val in enumerate(count) if abs(val[1] - val[0]) < 2]
print(f'его медиана равна {res[0]}')
