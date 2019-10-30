import random

SIZE = 4
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE + 1)]
print(*matrix, sep='\n')
print('*' * 50)

sum_column = [0] * len(matrix[0])

for line in matrix:
    sum_line = 0
    for i, item in enumerate(line):
        sum_line += item
        sum_column[i] += item
        print(item, end=' ')
    print(sum_line)

for i in sum_column:
    print(i, end=' ')
