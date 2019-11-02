'''
1 Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
'''

import random

def bubb_inv(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - 1, n - 1, -1):
            if array[i] > array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
        n += 1
    return array

array = [random.randint(-100, 100) for i in range(10) if i < 100]
print(array)
print('*' * 50)
print(bubb_inv(array))
