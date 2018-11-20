"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
from collections import deque

def union_sort(array):
    if len(array) < 3:
        if len(array) == 2:
            return [min(array), max(array)]
        return array
    else:
        med = len(array) // 2
        ar1 = union_sort(array[:med])
        ar2 = union_sort(array[med:])

        res = deque([], maxlen=len(ar1) + len(ar2))
        length = min(len(ar1), len(ar2))

        while length > 0:
            if ar1[-1] > ar2[-1]:
                res.appendleft(ar1.pop(-1))
            else:
                res.appendleft(ar2.pop(-1))
            length = min(len(ar1), len(ar2))

        return ar1 + ar2 + list(res)

import random

array = [6.6, 0.1, 1.2, 4.5, 3.3, 7.6, 1.1, 1.9, 8.5, 8.3] #[random.uniform(0, 50) for _ in range(10)]

print(f'source: {array}')
print(f'sorted: {union_sort(array)}')
