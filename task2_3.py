"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
"""
import random

def TestGetReverse(func):
    lst = [str(random.randint(100, 199)) for _ in range(10)]
    for i, item in enumerate(lst):
        assert item[::-1] == func(item)
        print(f'Test {i} OK')

# 1. Цикл
def GetReverse1(input):
    length = len(input)
    reverse = []
    for i in range(length):
        reverse.append(input[length - i - 1])

    return ''.join(reverse)

# TestGetReverse(GetReverse1)

# 100 loops, best of 5: 1.6 usec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse1('0123456789' * 5)"
# 100 loops, best of 5: 5.96 usec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse1('0123456789' * 10)"
# 100 loops, best of 5: 11.8 usec per loop

# 2. Рекурсия
def GetReverse2(input):
    if not input:
        return input
    else:
        return input[-1:] + GetReverse2(input[:-1])

# TestGetReverse(GetReverse2)

# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse2('0123456789' * 1)"
# 100 loops, best of 5: 4.83 usec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse2('0123456789' * 5)"
# 100 loops, best of 5: 28.4 usec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse2('0123456789' * 10)"
# 100 loops, best of 5: 52.5 usec per loop
