import random
import string

i1 = int(input('вывести целое число с:\n'))
i2 = int(input('по\n'))

print('случайное целое: ', random.randint(i1, i2))

f1 = float(input('вывести вещественное лисло с:\n'))
f2 = float(input('по\n'))

print('случайное вещественное: ', random.uniform(f1, f2))

s1 = input('вывести символ с:\n').lower()
s2 = input('по\n').lower()
si1 = string.printable.find(s1)
si2 = string.printable.find(s2)
sr = string.printable[random.randint(si1, si2)]

print('случайный символ: ', sr)
