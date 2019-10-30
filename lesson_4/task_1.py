'''
Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать,
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),


Задача для Анализа.
Урок 3, задача 1

В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''
import time
import timeit
import cProfile


# Варивант 1
######################################

def multipl_1(n):
    MIN_NUM_1 = 2
    # MAX_NUM_1 = 99
    MIN_NUM_2 = 2
    MAX_NUM_2 = 9

    r1 = [i for i in range(MIN_NUM_1, n + 1)]
    r2 = [i for i in range(MIN_NUM_2, MAX_NUM_2 + 1)]
    count = [0] * len(r2)

    for i in r1:
        for j, item in enumerate(r2):
            if i % item == 0:
                count[j] += 1

#     for i in range(len(r2)):
#         print(f'{r2[i]} - {count[i]}')

# multipl_1(99)

s1 = '''
def multipl_1(n):
    MIN_NUM_1 = 2
    MIN_NUM_2 = 2
    MAX_NUM_2 = 9

    r1 = [i for i in range(MIN_NUM_1, n + 1)]
    r2 = [i for i in range(MIN_NUM_2, MAX_NUM_2 + 1)]
    count = [0] * len(r2)

    for i in r1:
        for j, item in enumerate(r2):
            if i % item == 0:
                count[j] += 1

multipl_1(99000)          
'''

# print(timeit.timeit(s1, number=100))
# 0.0093105 - 99
# 0.09938369999999999 - 990
# 1.0175046 - 9900
# 12.811527700000001 - 99000

# cProfile.run('multipl_1(99000)')
# 99:
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:41(multipl)
#         1    0.000    0.000    0.000    0.000 task_1.py:48(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:49(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         8    0.000    0.000    0.000    0.000 {built-in method builtins.print}
# 990:
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 task_1.py:41(multipl)
#         1    0.000    0.000    0.000    0.000 task_1.py:48(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:49(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         8    0.000    0.000    0.000    0.000 {built-in method builtins.print}
# 9900:
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#         1    0.009    0.009    0.010    0.010 task_1.py:41(multipl)
#         1    0.001    0.001    0.001    0.001 task_1.py:48(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:49(<listcomp>)
#         1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         8    0.000    0.000    0.000    0.000 {built-in method builtins.print}
# 99000
#         1    0.001    0.001    0.124    0.124 <string>:1(<module>)
#         1    0.120    0.120    0.123    0.123 task_1.py:41(multipl_1)
#         1    0.003    0.003    0.003    0.003 task_1.py:48(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:49(<listcomp>)
#         1    0.000    0.000    0.124    0.124 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}

'''
Комментарий:
Время растет линейно. Скорость обусловленна 
нахождением в функции 3-х массивов. 
'''

# Варивант 2
######################################
#
def multipl_2(n):
    MIN_NUM_1 = 2
    # MAX_NUM_1 = 99

    MIN_NUM_2 = 2
    MAX_NUM_2 = 9

    r1 = [i for i in range(MIN_NUM_1, n + 1)]
    r2 = [i for i in range(MIN_NUM_2, MAX_NUM_2 + 1)]

    for i in r2:
        c = 0
        for j in r1:
            if j % i == 0:
                c += 1
        # print(f'{i} - {c}')

# multipl_2(99)

s2 = '''
def multipl_2(n):
    MIN_NUM_1 = 2
    # MAX_NUM_1 = 99

    MIN_NUM_2 = 2
    MAX_NUM_2 = 9

    r1 = [i for i in range(MIN_NUM_1, n + 1)]
    r2 = [i for i in range(MIN_NUM_2, MAX_NUM_2 + 1)]

    for i in r2:
        c = 0
        for j in r1:
            if j % i == 0:
                c += 1

multipl_2(99000)'''

# print(timeit.timeit(s2, number=100))
# 0.004799600000000001 - 99
# 0.048353900000000005 - 990
# 0.5119393999999999 - 9900
# 7.4447536 - 99000

# cProfile.run('multipl_2(99000)')
# 99
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:117(multipl)
#         1    0.000    0.000    0.000    0.000 task_1.py:124(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:125(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#  990
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:117(multipl)
#         1    0.000    0.000    0.000    0.000 task_1.py:124(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:125(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 9900
#         1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#         1    0.005    0.005    0.005    0.005 task_1.py:117(multipl)
#         1    0.000    0.000    0.000    0.000 task_1.py:124(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:125(<listcomp>)
#         1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
# 99000
#         1    0.001    0.001    0.075    0.075 <string>:1(<module>)
#         1    0.070    0.070    0.074    0.074 task_1.py:117(multipl_2)
#         1    0.003    0.003    0.003    0.003 task_1.py:124(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_1.py:125(<listcomp>)
#         1    0.000    0.000    0.075    0.075 {built-in method builtins.exec}
'''
Комментарий:
Время изменяется линейно. Алгоритм работаетв в два раза быстрее. Возможно это из-за того, 
что в алгоритме используются 2 массива (а не 3 как в предыдущем). Также из-за изменеия 
алгоритма перебора массивов в цикле , т.е для каждого элемента из малого массива 
перебирается большой массив.
'''

# Варивант 3
######################################

def multipl_3(n):
    MIN_NUM_1 = 2
    # MAX_NUM_1 = 99
    MIN_NUM_2 = 2
    MAX_NUM_2 = 9

    for i in range(MIN_NUM_2, MAX_NUM_2 + 1):
        c = 0
        for j in range(MIN_NUM_1, n + 1):
            if j % i == 0:
                c += 1
        print(f'{i} - {c}')
#
# multipl_3(99)

s3 = '''
def multipl_3(n):
    MIN_NUM_1 = 2
    # MAX_NUM_1 = 99
    MIN_NUM_2 = 2
    MAX_NUM_2 = 9

    for i in range(MIN_NUM_2, MAX_NUM_2 + 1):
        c = 0
        for j in range(MIN_NUM_1, n + 1):
            if j % i == 0:
                c += 1

multipl_3(9900)
'''
# print(timeit.timeit(s3, number=100))
# 0.004809000000000001 - 99
# 0.053250099999999995 - 990
# 0.5581606 - 9900
# 8.0062369 - 99000

# cProfile.run('multipl_3(99000)')
# 99
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:183(multipl_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 990
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 task_1.py:183(multipl_3)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
# 9900
#         1    0.000    0.000    0.006    0.006 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 task_1.py:183(multipl_3)
#         1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
# 99000
#         1    0.000    0.000    0.093    0.093 <string>:1(<module>)
#         1    0.093    0.093    0.093    0.093 task_1.py:183(multipl_3)
#         1    0.000    0.000    0.093    0.093 {built-in method builtins.exec}
'''
Время тоже изменяется линейно. В алгоритме не используются массивы, 
при этом время затраченное на исполнение его аналогично предыдущему варианту.
'''

###############################
'''
Вывод.
В задании были рассмотренны три реализации алгоритма решения представленной задачи.
Для разных входных n были сняты показания их быстродействия.
Исходя из выявленных временных результатов, можно сделать вывод, что в данном случае 
на результат быстродействия повлиял механизм перебора - большой цикл в малом цикле. Он в два раза
более эффектиыный, чем - малый в большом.
'''