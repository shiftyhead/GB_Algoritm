"""
3. В массиве случайных целых чисел поменять местами
минимальный и максимальный элементы.
"""

import random

SIZE = 10
source = [random.randint(0, SIZE * SIZE) for _ in range(0, SIZE)]

max_ = 0
max_id = 0
min_ = SIZE * SIZE
min_id = 0

for id, val in enumerate(source):
    if val > max_:
        max_ = val
        max_id = id
    if val < min_:
        min_ = val
        min_id = id

print(f'исходный массив:   {source}, макс.: {max_}, мин.: {min_}')
source[min_id] = max_
source[max_id] = min_
print(f'измененный массив: {source}')
