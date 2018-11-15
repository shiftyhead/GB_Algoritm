"""
5. В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""

import random
import sys

# вводные данные не оцениваем
SIZE = 10
source = [random.randint(-1 * SIZE, SIZE) for _ in range(0, SIZE)]

size_count = 0

max_ = -1 * SIZE
size_count += sys.getsizeof(max_)

max_id = 0
size_count += sys.getsizeof(max_id)

enu = enumerate(source)
print(f'enu = {sys.getsizeof(enu)}, type = {type(enu)}')
for id_, val in enu:
    if val < 0 and val > max_:
        max_ = val
        max_id = id_
size_count += sys.getsizeof(enu)
print(f'Размер используемой памяти: {size_count} байта')
print(f'в массиве {source}')
print(f'максимальное отрицательное число: {max_} (позиция {max_id})')

# вариант 1 из файла 05_max_below_zero.py (ДЗ к уроку 3 от преподавателя)
# вводные данные не оцениваем
array = [random.randint(-800, -750) for _ in range(SIZE)]

# в этом варианте SIZE используется для цикла, так что ее тоже считаем
size_count = 0
SIZE = len(array)
print(f'SIZE = {sys.getsizeof(SIZE)}, type = {type(SIZE)}')
size_count += sys.getsizeof(SIZE)

print(array)

i = 0
size_count += sys.getsizeof(i)

index = -1
size_count += sys.getsizeof(index)

while i < SIZE:
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1
print(f'Размер используемой памяти: {size_count} байта')

if index != -1:
    print(f'Максимальное отрицательное число {array[index]} находится в ячейке {index}')

print("""
Вывод: вариант из файла 05_max_below_zero.py экономит 44 байта, так как использует
для обхода цикла не итератор (72 байта), а простое целое число (28 байт)

Данные системы:
sh-4.4$ python3 --version
    Python 3.7.0
sh-4.4$ uname -a
    Linux dmitry-virtual-machine 4.15.0-38-generic #41-Ubuntu SMP Wed Oct 10 10:59:38 UTC 2018 x86_64 GNU
    /Linux
""")
