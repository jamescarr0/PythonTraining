g = (i for i in range(1, 6))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

import sys

lst = [i for i in range(1, 10_000)]
print(f'Sizeof list: {sys.getsizeof(lst)}')

g = (i for i in range(1, 10_000)) # Generator will always be the same size regardless of its length
print(f'Sizeof generator: {sys.getsizeof(g)}')


def f():
    ''' Generator Function, will pickup from it left off returning the next value when next is called '''
    yield 1
    yield 2
    yield 3

g = f()
print(next(g))
print(next(g))
print(next(g))