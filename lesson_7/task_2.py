'''
2 Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

Разбор задачи не смотрел.
алгоритм и реализвцию метода нашел в интернете.

'''
import random

def merge(left, right):
    i = 0
    j = 0
    new_array =[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            new_array.append(left[i])
            i += 1
        else:
            new_array.append(right[j])
            j += 1
    new_array += left[i:] + right[j:]
    return new_array

def merge_sort(array):
    if len(array) <= 1:
        return array
    else:
        a = len(array) // 2
        left = merge_sort(array[a:])
        right = merge_sort(array[:a])
    return merge(left, right)

a = [random.uniform(0, 50) for i in range(10) if i < 50]
print(a)
print(merge_sort(a))
