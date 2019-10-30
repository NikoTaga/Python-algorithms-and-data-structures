'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.

решение не смотрел
'''

import random

SIZE = 20
MIN_ITEM = -20
MAX_ITEM = 20

array = [random.randint(MIN_ITEM, MAX_ITEM-1) for _ in range(SIZE)]
print(array)

num_max = abs(MIN_ITEM)
num_ind = 0

for i, item in enumerate(array):
    if item < 0 and abs(item) < abs(num_max):
        num_max = item
        num_ind = i

print(f'Максимальное отр. число {num_max} индекс {num_ind}')
