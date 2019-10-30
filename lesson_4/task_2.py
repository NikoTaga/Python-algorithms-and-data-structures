'''
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и
возвращать соответствующее простое число. Проанализировать скорость и
сложность алгоритмов.
'''
import timeit
import cProfile

def sieve(n):
    m = n ** 2 + 2
    sieve_ar = [i for i in range(m)]
    sieve_ar[1] = 0

    for i in range(2, m):
        if sieve_ar[i] != 0:
            j = i + i
            while j < m:
                sieve_ar[j] = 0
                j += i
    pr = []
    for i in sieve_ar:
        if i != 0:
            pr.append(i)
    return pr[n - 1]

s = '''
def sieve(n):
    m = n ** 2 + 2
    sieve_ar = [i for i in range(m)]
    sieve_ar[1] = 0

    for i in range(2, m):
        if sieve_ar[i] != 0:
            j = i + i
            while j < m:
                sieve_ar[j] = 0
                j += i
    pr = []
    for i in sieve_ar:
        if i != 0:
            pr.append(i)
    return pr[n - 1]
    
sieve(300)
'''
# print(timeit.timeit(s, number=100))
# 0.003010099999999998 - 10
# 0.0121869 - 20
# 0.0291073 - 30
# 0.052309100000000004 - 40
# 0.1672374 - 50
# 0.3729818 - 100
# 1.6017793 - 200
# 4.199225 - 300

# cProfile.run('sieve(50)')
# 50
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 task_2.py:10(sieve)
#         1    0.000    0.000    0.000    0.000 task_2.py:12(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       367    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

'''
Комментарий. Время выполнения изменяется линейно
'''

def prime(n):
    m = n ** 2 + 2
    # sieve = [i for i in range(m)]

    def prim_num(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    pr = []
    for i in range(2, m):
        if prim_num(i):
            pr.append(i)
    return pr[n - 1]

p = '''
def prime(n):
    m = n ** 2 + 2
    # sieve = [i for i in range(m)]

    def prim_num(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    pr = []
    for i in range(2, m):
        if prim_num(i):
            pr.append(i)
    return pr[n - 1]
    
prime(50)
'''
# print(timeit.timeit(p, number=100))
# 0.011114299999999997 - 10
# 0.1037514 - 20
# 0.5192207 - 30
# 1.4665073 - 40
# 3.0811080000000004 - 50

# cProfile.run('prime(40)')
# 100    0.000    0.000    0.000    0.000 task_2.py:62(prim_num) - 10
# 400    0.001    0.000    0.001    0.000 task_2.py:62(prim_num) - 20
# 900    0.004    0.000    0.004    0.000 task_2.py:62(prim_num) - 30
# 1600    0.013    0.000    0.013    0.000 task_2.py:62(prim_num) - 40
# 2500    0.030    0.000    0.030    0.000 task_2.py:62(prim_num) - 50


# n = int(input('введите порядковый номер простого числа'))
# print(f'Алгоритм «Решето Эратосфена» {sieve(n)}')
# print(f'Классический алгоритм {prime(n)}')

'''
Вывод.
проведя замеры времени работы двух алгоритмов при аналогичных входных параметрах, 
можно сказать, что более быстрым из них является «Решето Эратосфена»
'''