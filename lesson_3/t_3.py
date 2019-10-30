import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

pos = 2
num = 555
# array.insert(pos, num)
# print(array)

array.append(None)
print(array)

i = len(array) -1
while i > pos:
    array[i], array[i - 1] = array[i -1], array[i]
    i -= 1
    print(array)
array[pos] = num
print(array)