'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

разбор не смотрел
'''

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_elem = MAX_ITEM
min_index = 0
max_elem = 0
max_index = 0

for i, item in enumerate(array):
    if min_elem > item:
        min_elem = item
        min_index = i
    if max_elem < item:
        max_elem = item
        max_index = i
print(f'min-{min_elem}, index-{min_index}')
print(f'max-{max_elem}, index {max_index}')

array[min_index], array[max_index] = array[max_index], array[min_index]
print(array)

