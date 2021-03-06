"""
1. Пользователь вводит данные о количестве предприятий, их наименования
и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего
и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import Counter

num_ = int(input('Сколько предприятий? '))
items_ = {}
sum_all = Counter()

for i in range(num_):
    title = input(f'Предприятие {i + 1}. Название: ')
    sum_ = 0
    for j in range(1, 5):
        sum_ += int(input(f'Прибыль за квартал {j}: '))
    avg_ = sum_ / 4

    items_[title] = Counter(
        {
        'sum_': sum_,
        'avg_': avg_
        }
    )
    sum_all += items_[title] # притянуто за уши конечно, но больше ничего не пришло в голову

avg_all = sum_all['sum_'] / num_
print(f'Средняя прибыль за год: {avg_all}')

high = {j for j in items_ if items_[j]['sum_'] > avg_all}
low = set(items_.keys()) - set(high)
print(f'Выше среднего: {high}')
print(f'Ниже среднего: {low}')
