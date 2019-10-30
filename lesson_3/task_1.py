'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

Разбор задачи не видел!
'''

MIN_NUM_1 = 2
MAX_NUM_1 = 99

MIN_NUM_2 = 2
MAX_NUM_2 = 9

r1 = [i for i in range(MIN_NUM_1, MAX_NUM_1 + 1)]
r2 = [i for i in range(MIN_NUM_2, MAX_NUM_2 + 1)]

count = [0] * len(r2)

print(r1)
print(r2)

for i in r1:
    for j, item in enumerate(r2):
        if i % item == 0:
            count[j] += 1

for i in range(len(r2)):
    print(f'{r2[i]} - {count[i]}')



