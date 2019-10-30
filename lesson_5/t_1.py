from collections import Counter

a = Counter()
b = Counter('abrakadabra') #!!!!!!!!!!!!!!!!!!!!!
c =Counter({'cats': 10, 'dogs': 5})
print(a, b, c, sep='\n')

print(b['z'])
b['z'] = 3
print(b)
print(b.most_common(3)) #!!!!!!!!!!!!!!!!!!!

print(list(b.elements()))

print('*' * 50)
x = Counter(a = 3, b = 2, c = -3) #+ Counter()
y = Counter(a = 4, b = 1, c = 2)
print(x, y, sep='\n')
print(x + y)
print(x - y)
print(x & y)
print(x | y)


