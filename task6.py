import string

i1 = int(input('введите индекс символа:\n'))

alphabet = string.printable[
    string.printable.find('a'):string.printable.find('z') + 1
    ]

s1 = alphabet[i1 - 1]

print('символ: ', s1)
