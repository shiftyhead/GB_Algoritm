"""
5. Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""

begin = 32
end = 127
row_length = 10

rows = (end - begin) / row_length

for i in range(round(rows)):
    res = {}
    for j in range(begin, begin + row_length):
        if j > end:
            break
        res[j] = chr(j)
    print(res)
    begin += row_length
