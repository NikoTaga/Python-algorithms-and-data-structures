'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

разбор задачи не видел

'''

from collections import Counter

a = int(input('Введите количество предприятий: '))
profit_mass = Counter()
profit_avg = 0

for i in range(a):
    name = input(f'введите наименование {i + 1} предприятия: ')
    for j in range(4):
        num_in = int(input(f'Введите прибыль {name} за {j + 1} квартал: '))
        profit_mass[name] += num_in
        profit_avg += num_in

m = 'Прибыль выше средней: '
k = 'Прибыль ниже средней: '

for i in profit_mass:
    if profit_mass[i] > profit_avg / a:
        m += i + ' '
    elif profit_mass[i] < profit_avg / a:
        k += i + ' '

print(f'Средняя пртбыль {profit_avg / a}')
print(m)
print(k)



