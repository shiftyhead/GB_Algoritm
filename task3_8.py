"""
8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать
ее в ее последнюю ячейку. В конце следует вывести полученную матрицу.
"""

res = []

for i in range(4):
    sum_ = 0
    row = []

    for _ in range(4):
        user_input = int(input(f'Введите целое число для ряда {i + 1}: '))
        row.append(user_input)
        sum_ += user_input

    row.append(sum_)
    res.append(row)

print(*res, sep='\n')
