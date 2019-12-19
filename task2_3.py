"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
"""
import random
import cProfile
import functools

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
# cProfile.run('GetReverse1("0123456789" * 1)')
# 1    0.000    0.000    0.000    0.000 task2_3.py:15(GetReverse1)
# 10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('GetReverse1("0123456789" * 5)')
# 50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# cProfile.run('GetReverse1("0123456789" * 10)')
# 100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
    # сама функция вызывается один раз, метод добавления в список - в зависимости от входных данных
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse1('0123456789' * 1)"
# 100 loops, best of 5: 1.62 usec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse1('0123456789' * 5)"
# 100 loops, best of 5: 5.88 usec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse1('0123456789' * 10)"
# 100 loops, best of 5: 11.3 usec per loop
    # скорость выполнения растет линейно, алгоритм линейной сложности O(n)

# 2. Рекурсия
def GetReverse2(input):
    if len(input) < 2:
        return input
    else:
        return input[-1:] + GetReverse2(input[:-1])

# TestGetReverse(GetReverse2)
# cProfile.run('GetReverse2("0123456789" * 1)')
# 10/1    0.000    0.000    0.000    0.000 task2_3.py:41(GetReverse2)
# cProfile.run('GetReverse2("0123456789" * 5)')
# 50/1    0.000    0.000    0.000    0.000 task2_3.py:41(GetReverse2)
# cProfile.run('GetReverse2("0123456789" * 10)')
# 100/1    0.000    0.000    0.000    0.000 task2_3.py:41(GetReverse2)
    # глубина рекурсии зависит от входных данных
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse2('0123456789' * 1)"
# 100 loops, best of 5: 3.17 usec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse2('0123456789' * 5)"
# 100 loops, best of 5: 16.6 usec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse2('0123456789' * 10)"
# 100 loops, best of 5: 32.6 usec per loop
    # алгоритм так же линейный, скорость выполнения увеличилась в три раза по сравнению с циклом

# 2. Рекурсия с кэшем
@functools.lru_cache()
def GetReverse2(input):
    if len(input) < 2:
        return input
    else:
        return input[-1:] + GetReverse2(input[:-1])

# TestGetReverse(GetReverse2)
# cProfile.run('GetReverse2("0123456789" * 1)')
# 10/1    0.000    0.000    0.000    0.000 task2_3.py:65(GetReverse2)
# cProfile.run('GetReverse2("0123456789" * 5)')
# 40/1    0.000    0.000    0.000    0.000 task2_3.py:41(GetReverse2)
# cProfile.run('GetReverse2("0123456789" * 10)')
# 50/1    0.000    0.000    0.000    0.000 task2_3.py:41(GetReverse2)
    # глубина рекурсии изменилась, для кешированных результатов функция не вызывается
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse2('0123456789' * 1)"
# 100 loops, best of 5: 110 nsec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse2('0123456789' * 5)"
# 100 loops, best of 5: 107 nsec per loop
# :0: UserWarning: The test results are likely unreliable. The worst time (599 nsec) was more than four times slower than the best time (107 nsec).
# sh-4.4$ python3 -m timeit -n 100 -s "import task2_3" "task2_3.GetReverse2('0123456789' * 10)"
# 100 loops, best of 5: 111 nsec per loop
# :0: UserWarning: The test results are likely unreliable. The worst time (713 nsec) was more than four times slower than the best time (111 nsec).
    # скорость выполнения увеличилась примерно на порядок, если оценивать первый запуск,
    # в последующих прирастает уже не с той зависимостью от входных данных,
    # наклон графика f(n) сильно изменился и - если так можно выразиться -
    # стремится к параллельности с осью n
