# O(2^N) - Terrible, do not try for n > 40
# def f(n):
#     return n if n <= 1 else f(n-1) + f(n-2)


# # f = [f(n) for n in range(10)]
# # print(f)

# Linear solution O(n) - Recursive
cache = {0: 0, 1: 1}
def f(n):
    if n in cache:
        return cache[n]
    cache[n] = f(n-1) + f(n-2)
    return cache[n]

# Iterative solution
def f_it(n):
    cache=[0, 1]
    for i in range(n-len(cache)):
        cache.append((cache[i] + cache[i+1]))
    return cache

N = 20
f = [f(n) for n in range(N)]
print(f"Recursive: {f}")
print(f"Iterative: {f_it(N)}")