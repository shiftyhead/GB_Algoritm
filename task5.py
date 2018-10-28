import string

s1 = input('введите первый символ:\n').lower()
s2 = input('введите второй символ:\n').lower()

si1 = string.ascii_lowercase.find(s1) + 1
si2 = string.ascii_lowercase.find(s2) + 1
sr = abs(si1 - si2) - 1

print('индекс первого символа: ', si1)
print('индекс второго символа: ', si2)
print('символов между ними: ', sr)
