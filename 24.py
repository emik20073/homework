def pow(x):
    return x ** 2
def some_gen(begin, end, func):
    a = begin
    for _ in range(end):
        yield a
        a = func(a)
from inspect import isgenerator
gen = some_gen(2,4, pow)
assert isgenerator(gen) == True
assert list(gen) == [2, 4, 16, 256]
print("ok")