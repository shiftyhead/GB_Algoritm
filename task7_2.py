"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""
def union_sort(array):
    if len(array) < 3:
        if len(array) == 2:
            return [min(array), max(array)]
        return array
    else:
        med = len(array) // 2
        ar1 = union_sort(array[:med])
        ar2 = union_sort(array[med:])

        res = []
        length = min(len(ar1), len(ar2))

        while length > 0:
            if ar1[0] < ar2[0]:
                res.append(ar1.pop(0))
            else:
                res.append(ar2.pop(0))
            length -= 1

        res += ar1 + ar2

        return res

import random

array = [6.6, 0.1, 1.2, 4.5, 3.3, 7.6, 1.1, 1.9, 8.5, 8.3] #[random.uniform(0, 50) for _ in range(10)]

print(f'source: {array}')
print(f'sorted: {union_sort(array)}')
