"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""

import random

SIZE = 10
source = [random.randint(-1 * SIZE, SIZE) for _ in range(0, SIZE)]

max_ = -1 * SIZE
max_id = 0
for id_, val in enumerate(source):
    if val < 0 and val > max_:
        max_ = val
        max_id = id_

print(f'в массиве {source}')
print(f'максимальное отрицательное число: {max_} (позиция {max_id})')
