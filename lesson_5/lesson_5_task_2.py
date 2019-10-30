'''
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

from collections import deque
from collections import defaultdict

a = {}
b = {}

for i in range(16):
    if i < 10:
        a[str(i)] = i
        b[i] = str(i)
    elif 16 > i > 9:
        a[chr(55 + i)] = i
        b[i] = chr(55 + i)

nun_1 = deque(input('введите 1-е число от 1 до F: ').upper())
nun_2 = deque(input('введите 2-е число от 1 до F: ').upper())

print(nun_1)
print(nun_2)

num_summ = deque()

len_1 = len(nun_1)
len_2 = len(nun_2)

for i in range(abs(len_1 - len_2)):
    if len_1 > len_2:
        nun_2.appendleft('0')
    elif len_2 > len_1:
        nun_1.appendleft('0')

over = 0
for _ in range(len_1 | len_2):
    n1, n2 = a[nun_1.pop()], a[nun_2.pop()]
    if n1 + n2 + over > 15:
        num_summ.appendleft(b[n1 + n2 + over - 16])
        over = (n1 + n2 + over) // 16
    elif n1 + n2 + over < 16:
        num_summ.appendleft(b[n1 + n2 + over])
        over = 0
if over != 0:
    num_summ.appendleft(b[over])

print(f'сумма {num_summ}')





