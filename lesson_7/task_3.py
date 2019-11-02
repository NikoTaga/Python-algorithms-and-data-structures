'''
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
'''
import statistics
import random

def gnom_sort(x):
    i_mem = 1
    i = 0
    while True:
        if i < 0:
            i = i_mem
        if i + 1 >= len(x):
            return x
        elif x[i] < x[i + 1]:
            i = i_mem
            i += 1
            i_mem = i
        else:
            x[i], x[i + 1] = x[i + 1], x[i]
            i -= 1

array = [random.randint(-100, 100) for i in range(11)]
print(array)

array_sort = gnom_sort(array)
med = array_sort[len(array_sort) // 2]

print(array_sort, med, sep='\n')

