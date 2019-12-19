import cProfile

def era_(n):
    sieve = [i for i in range(n)]

    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    print(len(res))
    return res

def simple_numbers(n):
    res = [0, 2,]
    counter_num = 1

    while len(res) < n + 1:
        for i in range(res[-1] + 1, res[-1] * 2):
            count_del = 0
            for j in range(2, i):
                if i % j == 0:
                    count_del += 1
                    break
            if count_del == 0:
                res.append(i)
            if n < len(res):
                break
        counter_num += 1

    return res[n]
print(era_(100))
# print(simple_numbers(16))
# cProfile.run('era_(1000)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 task4.py:15(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 task4.py:3(era_)
   #      1    0.000    0.000    0.000    0.000 task4.py:4(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# cProfile.run('simple_numbers(1000)')
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.024    0.024 <string>:1(<module>)
   #      1    0.024    0.024    0.024    0.024 task4.py:18(simple_numbers)
   #      1    0.000    0.000    0.024    0.024 {built-in method builtins.exec}
   #    168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# sh-4.4$ python3 -m timeit -n 100 -s "import task4" "task4.era_(10)"
# 100 loops, best of 5: 2.41 usec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task4" "task4.era_(100)"
# 100 loops, best of 5: 20.6 usec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task4" "task4.era_(1000)"
# 100 loops, best of 5: 245 usec per loop
    # алгоритм линейный, скорость изменяется пропорционально объему вычислений
# sh-4.4$ python3 -m timeit -n 100 -s "import task4" "task4.simple_numbers(10)"
# 100 loops, best of 5: 4.17 usec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task4" "task4.simple_numbers(100)"
# 100 loops, best of 5: 211 usec per loop
# sh-4.4$ python3 -m timeit -n 100 -s "import task4" "task4.simple_numbers(1000)"
# 100 loops, best of 5: 25.4 msec per loop
    # скорость сильнее зависит от объема вычислений

# Эратосфен эффективнее простого перебора
