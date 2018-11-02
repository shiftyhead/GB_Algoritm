"""
5. Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
"""

BEGIN = 32
END = 127
ROW_LENGTH = 10

rows = (END - BEGIN) / ROW_LENGTH

for i in range(round(rows)):
    res = {}
    for j in range(BEGIN, BEGIN + ROW_LENGTH):
        if j > END:
            break
        res[j] = chr(j)
    print(res)
    BEGIN += ROW_LENGTH
