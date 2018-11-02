"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр
и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
"""

user_input = input("Введите целое число: ")

length = len(user_input)

reverse = []

for i in range(length):
    reverse.append(user_input[length - i - 1])

print('обратное число: ' + ''.join(reverse))
