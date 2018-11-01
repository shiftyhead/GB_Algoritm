"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

length = int(input("Введите целое число n: "))

row = [1,]
sum = row[0]

for i in range(1, length):
    row.append(row[i - 1] / -2)
    sum = sum + row[i]

print(f'Сумма {length} элементов ряда {row} \nравна {sum}')
