import random

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
array.sort()
print(array)

find = int(input('введиье число: '))
pos = len(array) // 2
left = 0
right = len(array) - 1
count = 0

while array[pos] != find and left <=right:
    count += 1
    if find > array[pos]:
        left = pos +1
    elif find < array[pos]:
        right = pos - 1
    pos = (left + right) // 2
print('Элемент отсутствует' if left > right else f'позиция элемента равна {pos}')
print(count)
