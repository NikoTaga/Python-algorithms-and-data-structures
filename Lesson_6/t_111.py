import sys

a = 4287687687687.0

print(sys.getsizeof(a))

def show_size(x):
    print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key)
                show_size(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item)

q = 12
n = [i for i in range(59)]
f = 'hello word'
m = str(n)
l = set(n)
k = tuple(n)
# print(type(f))
show_size(f)




