"""
1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Вывести на экран исходный и отсортированный массивы.
"""

def bubble_sort(array):

    n = len(array)

    while n > 0:
        for i in range(1, n):
            if array[-i] > array[-(i + 1)]:
                array[-i], array[-(i + 1)] = array[-(i + 1)], array[-i]

        n -= 1
    return array

import random

array = [random.randint(-100, 99) for _ in range(10)]

print(f'source: {array}')
print(f'sorted: {bubble_sort(array[:])}')
