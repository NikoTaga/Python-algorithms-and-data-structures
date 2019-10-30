'''
Определить, какое число в массиве встречается чаще всего.

не смотрел
'''

import random

SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM-1) for _ in range(SIZE)]
array_count = [0] * MAX_ITEM
print(array)

for i in array:
    array_count[i] += 1

num = 0
num_count = 0

for i, item in enumerate(array_count):
    if item > num_count:
        num_count = item
        num = i

print(f'Число {num} встречается {num_count} раз')
